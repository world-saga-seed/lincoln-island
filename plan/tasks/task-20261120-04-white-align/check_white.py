#!/usr/bin/env python3
"""Check the phase 3 discord lists (texts/align/NN-discords.md, R1120-43).

For each discord heading "### N. kind: label (CITE ¶a[–¶b]; White ¶c[–¶d] | White —)":
  - kind is one of cut, condensed, addition, changed, softened;
  - the cite names the chapter's own part and number; the ¶ exist in the French;
  - every "quote:" resolves in the cited French paragraphs (all of the chapter if the range is short of it: a warning);
  - every "white:" resolves in the cited White paragraphs, or is "—";
  - every top-level bullet carries a mark.
The "Outline slips" section: every "quote:" resolves in the French chapter; every "outline:" in the outline file.
Usage: python3 check_white.py [NN ...]   (default: every discords-NN.md present)
"""
import glob, os, re, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
TASK = os.path.dirname(os.path.abspath(__file__))
KINDS = {'cut', 'condensed', 'addition', 'changed', 'softened'}
MARK = re.compile(r'\*\((Drafted|My reading, to confirm|Proposal)[^)]*\)\*')
HEAD = re.compile(r'^### (\d+)\. (\w+): .*\(([IV]+\.\d+) ((?:¶\d+(?:[–-]¶?\d+)?|(?:n|ln|pl)\d+)(?:,? (?:¶\d+(?:[–-]¶?\d+)?|(?:n|ln|pl)\d+))*); White ((?:¶\d+(?:[–-]¶?\d+)?)(?:, ¶\d+(?:[–-]¶?\d+)?)*|—)\)\s*$')


def refs(t):
    # "¶3–¶5, ¶9 n1" -> ([3,4,5,9], ['n1'])
    ps, ns = [], re.findall(r'(?:n|ln|pl)\d+', t)
    for a, b in re.findall(r'¶(\d+)(?:[–-]¶?(\d+))?', t):
        ps += list(range(int(a), int(b or a) + 1))
    return ps, ns


def norm(s):
    s = unicodedata.normalize('NFC', s)
    return re.sub(r'\s+', ' ', s.replace(' ', ' ').replace(' ', ' ')).strip()


def paras(path):
    d = {}
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'^¶(\d+)(?: \[p\.\d+\])? (.*)$', ln.rstrip('\n'))
        if m:
            d[int(m.group(1))] = norm(m.group(2))
    return d


def cite(nn):
    k = int(nn)
    return ('I.%d' % k) if k <= 22 else ('II.%d' % (k - 22)) if k <= 42 else ('III.%d' % (k - 42))


def check(nn):
    p = os.path.join(ROOT, 'texts/align', f'{nn}-discords.md')
    fr = paras(os.path.join(ROOT, 'texts/fr-1875', f'{nn}.md'))
    wh = paras(os.path.join(ROOT, 'texts/white-1876', f'{nn}.md'))
    frall, whall = ' '.join(fr.values()), ' '.join(wh.values())
    frfile = norm(open(os.path.join(ROOT, 'texts/fr-1875', f'{nn}.md'), encoding='utf-8').read())
    frall += ' ' + frfile
    outl = glob.glob(os.path.join(ROOT, 'story/outline', f'{int(nn) * 100:05d}-*.md'))
    outtext = norm(open(outl[0], encoding='utf-8').read()) if outl else ''
    probs, warns, n = [], [], 0
    cur = None; in_slips = False
    for i, ln in enumerate(open(p, encoding='utf-8'), 1):
        s = ln.rstrip('\n')
        if s.startswith('## Outline slips'):
            in_slips = True; cur = None; continue
        if s.startswith('### '):
            m = HEAD.match(s)
            if not m:
                probs.append(f'{i}: heading does not parse: {s[:90]}'); cur = None; continue
            n += 1
            kind, c = m.group(2), m.group(3)
            fr_r, notes = refs(m.group(4)); wh_r, _ = refs(m.group(5))
            if kind not in KINDS: probs.append(f'{i}: kind "{kind}"')
            if c != cite(nn): probs.append(f'{i}: cite {c}, chapter is {cite(nn)}')
            for k in fr_r:
                if k not in fr: probs.append(f'{i}: French ¶{k} does not exist')
            for k in wh_r:
                if k not in wh: probs.append(f'{i}: White ¶{k} does not exist')
            frtxt = ' '.join(fr.get(k, '') for k in fr_r)
            if notes: frtxt += ' ' + frfile   # a footnote: its text is under the chapter's Notes
            cur = (frtxt, ' '.join(wh.get(k, '') for k in wh_r)); continue
        if re.match(r'^- ', s) and (cur or in_slips) and not MARK.search(s) and not re.match(r'^- None found\.?$', s):
            probs.append(f'{i}: bullet without a mark')
        m = re.match(r'^\s+- (quote|white|outline): (.*)$', s)
        if not m:
            continue
        what, q = m.group(1), norm(m.group(2))
        if what == 'quote':
            if cur and q not in cur[0]:
                (warns if q in frall else probs).append(f'{i}: French quote {"outside its cited ¶" if q in frall else "does not resolve"}: {q[:70]}')
            elif in_slips and q not in frall:
                probs.append(f'{i}: slip quote does not resolve: {q[:70]}')
        elif what == 'white' and q not in ('—', '-'):
            if cur and q not in cur[1]:
                (warns if q in whall else probs).append(f'{i}: White quote {"outside its cited ¶" if q in whall else "does not resolve"}: {q[:70]}')
        elif what == 'outline' and q not in outtext:
            probs.append(f'{i}: outline words do not resolve: {q[:70]}')
    return n, probs, warns


def main():
    args = sys.argv[1:] or sorted(re.findall(r'(\d\d)-discords\.md', ' '.join(os.listdir(os.path.join(ROOT, 'texts/align')))))
    bad = 0
    for nn in args:
        n, probs, warns = check(nn)
        print(f'{nn} {cite(nn)}: {n} discords, {len(probs)} problems, {len(warns)} warnings')
        for x in probs: print('   P', x)
        for x in warns: print('   w', x)
        bad += len(probs)
    print(f'{len(args)} lists, {bad} problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
