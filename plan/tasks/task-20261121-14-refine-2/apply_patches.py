#!/usr/bin/env python3
"""Apply patches.tsv (¶ in a new text is a paragraph break; an empty new text deletes) to the draft 3 copies, each old text found exactly once; set the title to draft 3."""
import csv, glob, pathlib, re, shutil, sys
T = pathlib.Path(__file__).parent
# Always rebuild from v1 (base/, from 45bdeb0), so no patch applies twice.
for src in glob.glob(str(T / 'base' / '*.md')):
    shutil.copy(src, T / 'draft4' / pathlib.Path(src).name)
rows = list(csv.DictReader(open(T / 'patches.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
done = {}
for r in rows:
    f = glob.glob(str(T / 'draft4' / (r['chapter'] + '-*.md')))[0]
    s = open(f, encoding='utf-8').read()
    n = s.count(r['old'])
    if n != 1: sys.exit(f"{r['id']}: old text found {n} times in {f}")
    s = s.replace(r['old'], r['new'].replace('¶', '\n\n')); s = re.sub(r'\n{3,}', '\n\n', s); open(f, 'w', encoding='utf-8').write(s); print(r['id'], 'applied')
for f in glob.glob(str(T / 'draft4' / '*.md')):
    s = open(f, encoding='utf-8').read()
    for d in ('(draft 2)', '(draft 1)'): s = s.replace(d, '(draft 4)', 1)
    open(f, 'w', encoding='utf-8').write(s)
