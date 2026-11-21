#!/usr/bin/env python3
"""Apply the sorters' translations (R1120-39): each "translate" span is replaced by its English
on each line where find_french.py found it. Quote lines and "at:" lines are never touched.
Logs every miss (span not found as written on that line) to french-misses.tsv. Prints counts."""
import collections, os, re
D = os.path.dirname(os.path.abspath(__file__))
os.chdir(D.rsplit('/plan/', 1)[0])
sort = {}
for p in ('french-sorted-s1.tsv', 'french-sorted-s2.tsv'):
    for l in open(f'{D}/{p}', encoding='utf-8'):
        c = l.rstrip('\n').split('\t')
        if c[0].isdigit():
            sort[int(c[0])] = (c[1].strip(), c[2].strip() if len(c) > 2 else '')
cands = [l.rstrip('\n').split('\t') for l in open(f'{D}/french-candidates.tsv', encoding='utf-8') if l.strip()]
edits = collections.defaultdict(list)          # file -> [(line, span, english)]
for i, (span, n, places) in enumerate(cands, 1):
    b, en = sort[i]
    if b != 'translate' or not en:
        continue
    for pl in places.split(', '):
        f, ln = pl.rsplit(':', 1)
        edits[f].append((int(ln), span, en))
done = miss = 0
misses = ['file\tline\tspan\tenglish']
for f, es in edits.items():
    L = open(f, encoding='utf-8').read().split('\n')
    # longest spans first, so a short span inside a long one is not replaced first
    for ln, span, en in sorted(es, key=lambda e: -len(e[1])):
        s = L[ln - 1]
        if re.match(r'^\s*-\s*(quote|at):', s):
            continue
        if span in s:
            L[ln - 1] = s.replace(span, en, 1); done += 1
        else:
            misses.append(f'{f}\t{ln}\t{span}\t{en}'); miss += 1
    open(f, 'w', encoding='utf-8').write('\n'.join(L))
open(f'{D}/french-misses.tsv', 'w', encoding='utf-8').write('\n'.join(misses) + '\n')
print(f'{done} replaced, {miss} missed (french-misses.tsv)')
