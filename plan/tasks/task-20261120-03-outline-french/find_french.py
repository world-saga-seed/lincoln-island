#!/usr/bin/env python3
"""Find French outside the cited quotes in the phase 2 outlines, notes and timeline (R1120-39, R1120-29).

Skips the quote lines ("- quote: ...") and the "- at: ..." lines. On every other
line, a candidate is:
  - any run inside « », “ ”, " " or ‘ ’ quotation marks holding a French
    function word or an accented letter;
  - any run of two or more words, outside quotation marks, holding a French
    function word next to another French word (e.g. "la pointe de l’Épave").
Prints a TSV: span, count, then up to three file:line places; one line per
distinct span, most frequent first. With --places, prints every place.

Usage: python3 find_french.py [--places] > candidates.tsv
"""
import collections, glob, re, sys

FILES = sorted(glob.glob('story/outline/*.md') + glob.glob('story/notes/*.md') + ['story/calendar/timeline.md'])
FW = set('le la les des du de d l un une et est sont était à au aux en dans pour par sur avec sans sous que qui ne pas plus il elle ils elles nous vous on se sa son ses leur leurs ce cette ces mon ma mes ton ta tes y lui fut avait été être'.split())
ACC = re.compile(r'[àâäçéèêëîïôöùûüœæÀÂÇÉÈÊÎÔÙÛŒ]')
QUOTED = re.compile(r'«\s*([^»]+?)\s*»|“([^”]+)”|"([^"]+)"|‘([^’]+)’')
WORD = re.compile(r"[A-Za-zÀ-ÿœŒæÆ’'-]+")


def frenchy(s):
    toks = [t.lower().strip("’'-") for t in WORD.findall(s)]
    toks = [t.split('’')[-1].split("'")[-1] if ('’' in t or "'" in t) and t[:2] in ("l’", "d’", "l'", "d'", "s’", "s'", "n’", "n'", "qu") else t for t in toks]
    return any(t in FW for t in toks) or bool(ACC.search(s))


def runs(line):
    out = []
    for m in QUOTED.finditer(line):
        q = next(g for g in m.groups() if g)
        if frenchy(q):
            out.append(q.strip())
    rest = QUOTED.sub(' ', line)
    # runs of words where French function words sit between other French-looking words
    for m in re.finditer(r"((?:\b[A-Za-zÀ-ÿœŒ’'-]+\b[ ,]*){2,})", rest):
        chunk = m.group(1).strip(' ,')
        toks = WORD.findall(chunk)
        fr = [i for i, t in enumerate(toks) if t.lower() in FW or re.match(r"^[ldsnLDSN][’']", t)]
        if not fr:
            continue
        # keep only the stretch around French function words that also has an accented or apostrophe word
        if ACC.search(chunk) or "’" in chunk:
            # trim to the French stretch: from the first function word's neighbour to the last
            a, b = max(min(fr) - 1, 0), min(max(fr) + 2, len(toks))
            span = ' '.join(toks[a:b])
            if len(span.split()) >= 2 and frenchy(span) and not re.search(r'\b(the|and|of|to|is|was|a|in|on|at|with|for)\b', span):
                out.append(span)
    return out


def main():
    places = '--places' in sys.argv
    hits = collections.defaultdict(list)
    for f in FILES:
        for i, ln in enumerate(open(f, encoding='utf-8'), 1):
            s = ln.strip()
            if re.match(r'^-\s*(quote|at):', s) or s.startswith('#'):
                continue
            for r in runs(ln):
                hits[r].append(f'{f}:{i}')
    rows = sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    for span, where in rows:
        print(f'{span}\t{len(where)}\t' + ', '.join(where if places else where[:3]))
    print(f'# {len(rows)} distinct spans, {sum(len(w) for w in hits.values())} places', file=sys.stderr)


if __name__ == '__main__':
    main()
