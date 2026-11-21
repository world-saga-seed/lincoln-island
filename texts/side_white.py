#!/usr/bin/env python3
"""Write texts/align/NN-side.md: each bead of texts/align/NN.tsv with its French and White text, for the labeller.
Usage: python3 texts/side_white.py all | NN [NN ...]"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from align_white import paras

def rng(r):
    if r == '-': return []
    a = [int(x) for x in re.findall(r'\d+', r)]
    return list(range(a[0], a[-1] + 1))

def cite(nn):
    k = int(nn); return ('I.%d' % k) if k <= 22 else ('II.%d' % (k - 22)) if k <= 42 else ('III.%d' % (k - 42))

args = sys.argv[1:]
if args == ['all']: args = ['%02d' % k for k in range(1, 63)]
for nn in args:
    fr = paras(os.path.join(HERE, 'fr-1875', f'{nn}.md')); wh = paras(os.path.join(HERE, 'white-1876', f'{nn}.md'))
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'align', f'{nn}.tsv'), encoding='utf-8')][1:]
    out = [f'# {cite(nn)}: the French beside White, bead by bead', '',
           f'*Made by `texts/side_white.py` from `texts/align/{nn}.tsv` (`texts/align_white.py`). The beads are a machine guess: the kinds "cut?", "add?", "short?" and "long?" are hints, not findings. French paragraphs are cited {cite(nn)} ¶N; White\'s are White ¶N.*', '']
    for k, (f, w, kind, *_rest) in enumerate(rows, 1):
        out.append(f'## Bead {k}: French {f}, White {w} ({kind})'); out.append('')
        for i in rng(f): out.append(f'FR ¶{i} {fr[i]}')
        if not rng(f): out.append('FR (none)')
        out.append('')
        for j in rng(w): out.append(f'WH ¶{j} {wh[j]}')
        if not rng(w): out.append('WH (none)')
        out.append('')
    open(os.path.join(HERE, 'align', f'{nn}-side.md'), 'w', encoding='utf-8').write('\n'.join(out))
print('done', len(args))
