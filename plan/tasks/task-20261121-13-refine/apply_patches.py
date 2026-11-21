#!/usr/bin/env python3
"""Apply patches.tsv to the draft 3 copies, each old text found exactly once; set the title to draft 3."""
import csv, glob, pathlib, sys
T = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(T / 'patches.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
done = {}
for r in rows:
    f = glob.glob(str(T / 'draft3' / (r['chapter'] + '-*.md')))[0]
    s = open(f, encoding='utf-8').read()
    if r['new'] in s and r['old'] not in s: print(r['id'], 'already applied'); continue
    n = s.count(r['old'])
    if n != 1: sys.exit(f"{r['id']}: old text found {n} times in {f}")
    s = s.replace(r['old'], r['new']); open(f, 'w', encoding='utf-8').write(s); print(r['id'], 'applied')
for f in glob.glob(str(T / 'draft3' / '*.md')):
    s = open(f, encoding='utf-8').read()
    for d in ('(draft 2)', '(draft 1)'): s = s.replace(d, '(draft 3)', 1)
    open(f, 'w', encoding='utf-8').write(s)
