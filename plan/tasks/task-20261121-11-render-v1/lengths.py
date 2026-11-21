#!/usr/bin/env python3
"""Per-paragraph length check: a render's paragraphs against the French, in order.
Flags paragraphs whose English/French word ratio falls well below the chapter's median,
the mark of a clause lost. Usage: lengths.py FRENCH.md RENDER.md"""
import re, sys, statistics
fr = [(m.group(1), m.group(2)) for m in (re.match(r'^(¶\d+)(?: \[[^\]]*\])? (.*)$', l.rstrip('\n'))
      for l in open(sys.argv[1], encoding='utf-8')) if m and m.group(1) != '¶0']
en = [l.strip() for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
en = [l for l in en if not l.startswith('#') and not l.startswith('CHAPTER') and not re.match(r'^\(\d\)', l)]
en = en[1:]  # the summary line
print(f'French paragraphs {len(fr)}, render paragraphs {len(en)}')
if len(fr) != len(en):
    print('COUNTS DIFFER: the paragraphs do not align one to one'); sys.exit(1)
r = [len(e.split()) / max(1, len(f.split())) for (_, f), e in zip(fr, en)]
med = statistics.median(r)
print(f'median English/French ratio {med:.2f}')
for (n, f), e, x in zip(fr, en, r):
    if x < med * 0.8 and len(f.split()) > 15:
        print(f'{n}: ratio {x:.2f} (French {len(f.split())}, English {len(e.split())})')
