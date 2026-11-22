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
num = {int(re.match(r'^¶(\d+) ', l).group(1)): re.sub(r'^¶\d+ ', '', l) for l in lines if re.match(r'^¶\d+ ', l)}
rows = list(csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
# A whole White paragraph: old "@¶N"; an empty new deletes it.
for r in rows:
    if r['old'].startswith('@¶'):
        n = int(r['old'][2:])
        if n not in num: print('FAIL', r['id'], 'no paragraph', n); sys.exit(1)
        if r['new']: num[n] = r['new'].replace('¶', '\n\n')
        else: del num[n]
        print('ok', r['id'])
rows = [r for r in rows if not r['old'].startswith('@¶')]
text = '\n\n'.join(num[k] for k in sorted(num))
bad = 0
for r in rows:
    n = text.count(r['old'])
    if n != 1:
        print('FAIL', r['id'], n, r['old'][:60]); bad += 1; continue
    text = text.replace(r['old'], r['new'].replace('¶', '\n\n'))
    print('ok', r['id'])
if bad: sys.exit(1)
# Footnotes: "{fn: text}" in a patch becomes "(k)" there, and "(k) text" as a paragraph after its own (as 01900 sets them).
out_paras, k = [], 0
for para in text.split('\n\n'):
    notes = []
    def sub(m):
        global k
        k += 1; notes.append('(%d) %s' % (k, m.group(1).strip())); return '(%d)' % k
    out_paras.append(re.sub(r'\{fn:([^}]*)\}', sub, para)); out_paras += notes
text = '\n\n'.join(out_paras)
open(out, 'w', encoding='utf-8').write('# %s\n\n%s\n\n%s\n' % (title, '\n\n'.join(head), text))
