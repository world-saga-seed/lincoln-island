#!/usr/bin/env python3
"""Apply a patcher's TSV to White's chapter (White made unabridged, R1121-146).

Usage: python3 apply.py NN PATCHES.tsv OUT.md "Title"
Rebuilds from texts/white-1876/NN.md every run. Every old text must occur exactly once
in White's text (the "¶N " prefixes stripped); "¶" in new is a paragraph break.
"""
import csv, re, sys
nn, tsv, out, title = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
lines = open('texts/white-1876/%02d.md' % nn, encoding='utf-8').read().splitlines()
head = [l[3:] for l in lines if l.startswith('hd ')]
paras = [re.sub(r'^¶\d+ ', '', l) for l in lines if re.match(r'^¶\d+ ', l)]
text = '\n\n'.join(paras)
bad = 0
for r in csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
    n = text.count(r['old'])
    if n != 1:
        print('FAIL', r['id'], n, r['old'][:60]); bad += 1; continue
    text = text.replace(r['old'], r['new'].replace('¶', '\n\n'))
    print('ok', r['id'])
if bad: sys.exit(1)
open(out, 'w', encoding='utf-8').write('# %s\n\n%s\n\n%s\n' % (title, '\n\n'.join(head), text))
