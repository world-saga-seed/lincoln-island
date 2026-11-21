#!/usr/bin/env python3
"""Write side/ID.md for each rendered passage: the French, the render and White, paragraph by paragraph.

Usage: python3 side.py [ID ...]   (no IDs: every passage with a render)

White's paragraphs for each French paragraph come from texts/align/NN.tsv (phase 3's alignment). A French paragraph
White drops shows White as "—". Footnotes (n1) are matched to White's text by hand where White has one; White carries
almost none, so a note shows "—".
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
S = {'A1': (56, list(range(30, 42)), []), 'A2': (1, [14], []), 'A3': (14, [74, 75], []),
     'A4': (58, [27] + list(range(38, 51)) + [62], []), 'A5': (39, [28, 58, 59, 79], ['n1']), 'A6': (15, [26], []),
     'S1': (4, [9], []), 'S2': (6, [41], ['n1']), 'S3': (17, [49], []), 'S4': (22, [41], []), 'S5': (24, [14], []),
     'S6': (25, [70], []), 'S7': (34, [90], []), 'S8': (35, [29], []), 'S9': (46, [49], []), 'S10': (52, [40], []),
     'S11': (53, [30], []), 'S12': (55, [3], []), 'P1': (41, [2], []), 'P2': (62, [10], [])}


def numbered(path):
    d = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'(¶\d+|n\d+) (?:\[p\.\d+\] )?(.*)', line.rstrip('\n'))
        if m:
            d[m.group(1)] = m.group(2)
    return d


def white_for(k):
    out = {}
    for line in open(os.path.join(ROOT, 'texts', 'align', f'{k:02d}.tsv'), encoding='utf-8').read().split('\n')[1:]:
        c = line.split('\t')
        if len(c) < 2:
            continue
        frs = re.findall(r'¶(\d+)', c[0])
        whs = c[1]
        for f in frs:
            out[int(f)] = whs
    return out


def render_paras(path):
    d, cur = {}, None
    for line in open(path, encoding='utf-8'):
        s = line.strip()
        m = re.match(r'^(¶\d+|n\d+)$', s)
        if m:
            cur = m.group(1)
            d[cur] = []
        elif cur and s and not s.startswith('# '):
            d[cur].append(s)
    return {k: ' '.join(v) for k, v in d.items()}


def main(ids):
    os.makedirs(os.path.join(HERE, 'side'), exist_ok=True)
    for pid in ids:
        rp = os.path.join(HERE, 'renders', f'{pid}.md')
        if not os.path.exists(rp):
            print(pid, 'no render')
            continue
        k, ps, ns = S[pid]
        fr = numbered(os.path.join(ROOT, 'texts', 'fr-1875', f'{k:02d}.md'))
        wh = numbered(os.path.join(ROOT, 'texts', 'white-1876', f'{k:02d}.md'))
        al = white_for(k)
        rd = render_paras(rp)
        out = [f'# {pid}: the French, the render, White', '']
        for p in ps:
            wcell = al.get(p, '')
            wpar = [x for x in re.findall(r'¶\d+', wcell)]
            wtext = ' / '.join(f'({w}) ' + wh.get(w, '') for w in wpar) or '—'
            out += [f'## ¶{p}', '', f'**French:** {fr.get(f"¶{p}", "")}', '', f'**Render:** {rd.get(f"¶{p}", "(not rendered)")}', '',
                    f'**White** ({wcell or "—"}): {wtext}', '']
        for n in ns:
            out += [f'## {n}', '', f'**French:** {fr.get(n, "")}', '', f'**Render:** {rd.get(n, "(not rendered)")}', '', '**White:** —', '']
        open(os.path.join(HERE, 'side', f'{pid}.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
        print(pid, 'ok', len(ps), 'paragraphs', 'missing:', [p for p in ps if f'¶{p}' not in rd])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)
    main(sys.argv[1:] or list(S))
