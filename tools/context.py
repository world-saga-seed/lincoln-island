#!/usr/bin/env python3
"""Pattern matches in their context: the windows a script or a cheap judge reads instead of whole chapters.

A check that hangs on a word (a rule from the ledger, a character's name, a
number, an out-of-world phrase) does not need a reader to scan the whole book.
This finds each match and prints the sentences or paragraphs around it with
their line numbers, so a script can decide, or a small model can judge only the
windows. A fault with no mark in the words (a claim with no grounds, a lead
missing from the page) is not for this tool: it still needs a reader.

Usage:
  python3 tools/context.py FILE [FILE ...] (--pattern LABEL=REGEX ... | --patterns FILE)
                           [--near REGEX] [--unless REGEX] [--within N]
                           [--before N] [--after N] [--para N] [--narration]
                           [--merge] [--stop REGEX] [--summary] [--fail]
                           [--tags] [--jsonl] [--anchor-min N]

  --pattern L=RX  a pattern to find, case-insensitive (repeatable)
  --patterns F    a file of patterns, one per line: LABEL<TAB>REGEX, then any of
                  near=RX, unless=RX, within=N, narration=1, as more tab fields;
                  # starts a comment
  --near RX       report a match only when RX also matches within N words of it
  --unless RX     report a match only when RX does NOT match within N words
                  ("ties" unless "black": a rule that one thing goes with another)
  --within N      the distance for --near and --unless, in words (default 12)
  --before N      sentences of context before the match (default 2)
  --after N       sentences of context after (default 1)
  --para N        give context by paragraph instead: the match's paragraph and
                  the N before it (grounds come before a claim: use --para 2)
  --narration     match outside dialogue only (text in double quotes is skipped
                  for matching, and kept in the window)
  --merge         one window for matches whose windows overlap (same pattern)
  --stop RX       stop reading a file at a line matching RX (default "^## Notes")
  --summary       counts per file and pattern only
  --fail          exit 1 when anything matched: for a guard that must stay at 0
  --tags          under each match, a position tag for a later tool to find the
                  edit point: "@ file:line:col-col anchor=«...»". The anchor is
                  the shortest run of words around the match found only once in
                  the file, so it still finds the spot after lines above it move
                  (marked "not unique" if twelve words are not enough);
                  --anchor-min N words at the least (default 4), so a later edit
                  nearby is less likely to repeat it
  --jsonl         one JSON record per match in place of the windows: file, line,
                  col, end, label, match, anchor, unique, window

Output, per match: "### file:line  LABEL  «match»", then the window, each
sentence or paragraph with its line number, the matching one marked with ">".
A judge prompt can take the whole output as its input.
"""
import argparse, os, re, sys

QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”')
SENT = re.compile(r'(?<=[.!?…])["”’)]*\s+(?=["“(]?[A-Z0-9])')


def parse_patterns(a):
    pats = []
    for p in a.pattern:
        if '=' not in p:
            sys.exit(f'--pattern needs LABEL=REGEX: {p}')
        label, rx = p.split('=', 1)
        pats.append({'label': label, 'rx': rx})
    if a.patterns:
        for line in open(a.patterns, encoding='utf-8'):
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            f = line.rstrip('\n').split('\t')
            if len(f) < 2:
                sys.exit(f'{a.patterns}: a line needs LABEL<TAB>REGEX: {line.strip()}')
            d = {'label': f[0].strip(), 'rx': f[1]}
            for extra in f[2:]:
                if '=' in extra:
                    k, v = extra.split('=', 1)
                    d[k.strip()] = v
            pats.append(d)
    if not pats:
        sys.exit('give --pattern or --patterns')
    try:
        return compile_patterns(pats, a.near, a.unless, a.within, a.narration)
    except re.error as e:
        sys.exit(f'bad pattern: {e}')


def compile_patterns(specs, near=None, unless=None, within=12, narration=False, flags=re.I):
    """Patterns ready for find(): each spec a dict with label and rx, and any of near,
    unless, within and narration (a spec's own value wins over the defaults given here).
    For a tool that imports this module: compile_patterns([{'label': 'span', 'rx': RX}])."""
    out = []
    for s in specs:
        d = dict(s)
        d.setdefault('near', near)
        d.setdefault('unless', unless)
        d['within'] = int(d.get('within') or within)
        d['narration'] = str(d.get('narration', '1' if narration else '')).strip() in ('1', 'yes', 'true')
        d['re'] = re.compile(d['rx'], flags)
        d['near_re'] = re.compile(d['near'], flags) if d.get('near') else None
        d['unless_re'] = re.compile(d['unless'], flags) if d.get('unless') else None
        out.append(d)
    return out


def units(path, stop):
    """Paragraphs as (first line, text), sentences as (line, paragraph index, text, start, end),
    and for each paragraph the source lines it joins: (line, offset in the paragraph, indent)."""
    paras, cur, start, segs, seg, size = [], [], None, [], [], 0
    for i, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if stop and re.search(stop, line):
            break
        t = line.strip()
        if not t or t.startswith('#') or t == '---':
            if cur:
                paras.append((start, ' '.join(cur)))
                segs.append(seg)
                cur, seg, size = [], [], 0
            continue
        if not cur:
            start = i
        seg.append((i, size, len(line) - len(line.lstrip())))
        size += len(t) + 1
        cur.append(t)
    if cur:
        paras.append((start, ' '.join(cur)))
        segs.append(seg)
    sents = []
    for k, (ln, text) in enumerate(paras):
        # break sentences where the narration does, never inside a quotation
        cuts = [m.end() for m in SENT.finditer(blank_quotes(text))]
        for s0, s1 in zip([0] + cuts, cuts + [len(text)]):
            if text[s0:s1].strip():
                sents.append((ln, k, text[s0:s1].strip(), s0, s1))
    return paras, sents, segs


def position(segs, off):
    """(line, column from 1) of an offset in a paragraph."""
    ln, o, ind = segs[0]
    for s in segs:
        if s[1] <= off:
            ln, o, ind = s
    return ln, off - o + ind + 1


def anchor(text, start, end, least=4, most=12):
    """The shortest run of words around text[start:end] that occurs once in text."""
    words = list(re.finditer(r'\S+', text))
    first = next((i for i, w in enumerate(words) if w.end() > start), 0)
    last = next((i for i in range(len(words) - 1, -1, -1) if words[i].start() < end), first)
    lo, hi, grow_left = first, last, False
    while True:
        a = text[words[lo].start():words[hi].end()]
        if text.count(a) == 1 and (hi - lo + 1 >= least or (lo == 0 and hi == len(words) - 1)):
            return a, True
        if hi - lo + 1 >= most or (lo == 0 and hi == len(words) - 1):
            return a, False
        if (grow_left and lo > 0) or hi == len(words) - 1:
            lo -= 1
        else:
            hi += 1
        grow_left = not grow_left


def blank_quotes(s):
    return QUOTED.sub(lambda m: ' ' * len(m.group(0)), s)


def near(text, start, end, rx, n):
    """Does rx match within n words of text[start:end]?"""
    words = list(re.finditer(r'\S+', text))
    if not words:
        return False
    first = next((i for i, w in enumerate(words) if w.end() > start), len(words) - 1)
    last = next((i for i in range(len(words) - 1, -1, -1) if words[i].start() < end), first)
    lo, hi = max(0, first - n), min(len(words) - 1, last + n)
    return bool(rx.search(text[words[lo].start():words[hi].end()]))


def scan(path, pats, a):
    return find(path, pats, a.stop, anchors=a.tags or a.jsonl, anchor_min=a.anchor_min)


def find(path, pats, stop=r'^## Notes', anchors=False, anchor_min=4, merge_sentences=True):
    """Every match of the compiled patterns in one file: (paragraphs, sentences, matches).
    A match is a dict: label, match, line, col, end (columns from 1), para, sent (indexes
    into the two lists), offset (where it starts in its paragraph's text), quoted (inside
    dialogue), and with anchors=True, anchor and unique.
    merge_sentences keeps one match per pattern per sentence (as the windows want); a tool
    that counts every match passes False."""
    paras, sents, segs = units(path, stop)
    raw = open(path, encoding='utf-8').read()
    lines = raw.split('\n')
    flat = ' '.join(t for _, t in paras)
    offsets, pos = [], 0
    for _, t in paras:
        offsets.append(pos)
        pos += len(t) + 1
    hits = []
    for d in pats:
        for k, (ln, text) in enumerate(paras):
            scope = blank_quotes(text) if d['narration'] else text
            for m in d['re'].finditer(scope):
                s, e = offsets[k] + m.start(), offsets[k] + m.end()
                if d['near_re'] and not near(flat, s, e, d['near_re'], d['within']):
                    continue
                if d['unless_re'] and near(flat, s, e, d['unless_re'], d['within']):
                    continue
                si = next((j for j, sn in enumerate(sents) if sn[1] == k and sn[3] <= m.start() < sn[4]),
                          next(j for j, sn in enumerate(sents) if sn[1] == k))
                line, col = position(segs[k], m.start())
                quoted = bool(m.group(0).strip()) and blank_quotes(text)[m.start():m.end()].strip() == ''
                h = {'label': d['label'], 'match': m.group(0), 'line': line, 'col': col,
                     'end': col + len(m.group(0)) - 1, 'para': k, 'sent': si, 'quoted': quoted,
                     'offset': m.start()}
                if anchors:
                    lstart = sum(len(x) + 1 for x in lines[:line - 1])
                    h['anchor'], h['unique'] = anchor(raw, lstart + col - 1, lstart + col - 1 + len(m.group(0)), anchor_min)
                hits.append(h)
    hits.sort(key=lambda h: (h['para'], h['sent'], h['col'], h['label']))
    return paras, sents, (dedupe(hits) if merge_sentences else hits)


def window(h, paras, sents, a):
    if a.para is not None:
        lo = max(0, h['para'] - a.para)
        return [(paras[k][0], paras[k][1], k == h['para']) for k in range(lo, h['para'] + 1)], ('para', lo, h['para'])
    lo, hi = max(0, h['sent'] - a.before), min(len(sents) - 1, h['sent'] + a.after)
    return [(sents[j][0], sents[j][2], j == h['sent']) for j in range(lo, hi + 1)], ('sent', lo, hi)


def dedupe(hits):
    """One hit per pattern per sentence: two matches in one sentence are one window."""
    seen, out = set(), []
    for h in hits:
        k = (h['label'], h['sent'])
        if k not in seen:
            seen.add(k)
            out.append(h)
    return out


def main():
    ap = argparse.ArgumentParser(description='Pattern matches in their context, for a script or a cheap judge.')
    ap.add_argument('files', nargs='+')
    ap.add_argument('--pattern', action='append', default=[])
    ap.add_argument('--patterns')
    ap.add_argument('--near')
    ap.add_argument('--unless')
    ap.add_argument('--within', type=int, default=12)
    ap.add_argument('--before', type=int, default=2)
    ap.add_argument('--after', type=int, default=1)
    ap.add_argument('--para', type=int)
    ap.add_argument('--narration', action='store_true')
    ap.add_argument('--merge', action='store_true')
    ap.add_argument('--stop', default=r'^## Notes')
    ap.add_argument('--summary', action='store_true')
    ap.add_argument('--fail', action='store_true')
    ap.add_argument('--tags', action='store_true')
    ap.add_argument('--jsonl', action='store_true')
    ap.add_argument('--anchor-min', type=int, default=4)
    a = ap.parse_args()
    pats = parse_patterns(a)
    total, words_out, words_in = 0, 0, 0
    if a.summary:
        print('| File | Pattern | Matches |\n|---|---|---|')
    for f in a.files:
        paras, sents, hits = scan(f, pats, a)
        words_in += sum(len(t.split()) for _, t in paras)
        total += len(hits)
        name = os.path.basename(f)
        if a.summary:
            for label in dict.fromkeys(h['label'] for h in hits):
                print(f'| {name} | {label} | {sum(h["label"] == label for h in hits)} |')
            continue
        if a.jsonl:
            import json
            for h in hits:
                win, _ = window(h, paras, sents, a)
                rec = {'file': f, 'line': h['line'], 'col': h['col'], 'end': h['end'], 'label': h['label'],
                       'match': h['match'], 'anchor': h['anchor'], 'unique': h['unique'],
                       'window': [{'line': ln, 'text': t, 'hit': mk} for ln, t, mk in win]}
                words_out += sum(len(t.split()) for _, t, _ in win)
                print(json.dumps(rec, ensure_ascii=False))
            continue
        shown = {}
        for h in hits:
            win, key = window(h, paras, sents, a)
            if a.merge and (h['label'], key[0]) in shown:
                kind, plo, phi = shown[(h['label'], key[0])]
                if key[1] <= phi:
                    shown[(h['label'], key[0])] = (kind, plo, max(phi, key[2]))
                    print(f'  (also at {name}:{h["line"]} «{h["match"]}»)')
                    continue
            shown[(h['label'], key[0])] = key
            print(f'### {name}:{h["line"]}  {h["label"]}  «{h["match"]}»\n')
            if a.tags:
                print(f'@ {f}:{h["line"]}:{h["col"]}-{h["end"]} anchor=«{h["anchor"]}»' + ('' if h['unique'] else ' (not unique)') + '\n')
            for ln, text, mark in win:
                words_out += len(text.split())
                print(f'{">" if mark else " "} {ln}: {text}')
            print()
    if a.summary:
        print(f'\n**Total:** {total} matches.')
    else:
        pct = f', {100 * words_out / words_in:.0f}% of the {words_in} words read' if words_in else ''
        print(f'**Total:** {total} matches; windows hold {words_out} words{pct}.', file=sys.stderr if a.jsonl else sys.stdout)
    sys.exit(1 if a.fail and total else 0)


if __name__ == '__main__':
    main()
