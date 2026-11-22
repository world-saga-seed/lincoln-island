#!/usr/bin/env python3
"""The restoration map's data: for each of Verne's 62 chapters, one mark per French paragraph,
drawn from the patches made (R1121-163), not from the alignment's discord lists.

Marks: k kept as White; p patched (White's words changed); r restored (words White cut put back,
or a paragraph he dropped); R the chapter rendered anew from the French; the counts per chapter.
A French paragraph takes the mark of the White paragraph(s) that render it (texts/align/NN.tsv).
Writes map.tsv: nn, action, marks, patches, kept, patched, restored. Run from the repo root.
"""
import csv, re, glob, os, sys
T = 'plan/tasks/task-20261121-15-white-unabridged'
act = {r['nn']: r['action'] for r in csv.DictReader(open(f'{T}/chapters.tsv'), delimiter='\t')}
def tsv_for(nn):
    c = '%05d' % (nn * 100)
    for p in [f'{T}/ch/{c}/patches-{c}.tsv', f'{T}/pilot/patches-{c}.tsv']:
        if os.path.exists(p): return p
rendered = {6,14,19,20,25,26,30,31,32,33,34,38,42,43,45,47,49,50,51,52,53,54,56,57}
out = []
for nn in range(1, 63):
    fr = [l for l in open('texts/fr-1875/%02d.md' % nn, encoding='utf-8') if re.match(r'^¶\d+ ', l)]
    nfr = len(fr)
    if nn in rendered:
        out.append((nn, 'render', 'R' * nfr, 0, 0, 0, nfr)); continue
    lines = open('texts/white-1876/%02d.md' % nn, encoding='utf-8').read().splitlines()
    wp = {int(m.group(1)): m.group(2) for l in lines for m in [re.match(r'^¶(\d+) (.*)', l)] if m}
    rows = list(csv.DictReader(open(tsv_for(nn), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
    mark = {}  # white ¶ -> 'p' or 'r'
    def put(w, m):
        if mark.get(w) != 'r': mark[w] = m
    for r in rows:
        old, new = r['old'], r['new'] or ''
        if r['discord'] == 'glossary': continue
        if old.startswith('@¶'):
            w = int(old[2:]); put(w, 'r' if len(new) > len(wp.get(w, '')) + 40 else 'p'); continue
        ws = [w for w, t in wp.items() if old in t] or [w for w, t in wp.items() if old[:40] in t]
        for w in ws[:1]:
            put(w, 'r' if len(new) - len(old) > 40 or '¶' in new else 'p')
    al = list(csv.DictReader(open('texts/align/%02d.tsv' % nn, encoding='utf-8'), delimiter='\t'))
    frm = {}
    for a in al:
        fs = [int(x) for x in re.findall(r'\d+', a['fr'])]
        whs = [int(x) for x in re.findall(r'\d+', a['white'])]
        ms = [mark.get(w, 'k') for w in whs] if whs else ['r']
        m = 'r' if 'r' in ms else 'p' if 'p' in ms else 'k'
        if len(fs) == 2 and ('–' in a['fr'] or '-' in a['fr']): fs = list(range(fs[0], fs[1] + 1))
        for f in fs: frm[f] = m
    marks = ''.join(frm.get(i, 'r') for i in range(nfr))
    out.append((nn, 'patch', marks, len([r for r in rows if r['discord'] != 'glossary']), marks.count('k'), marks.count('p'), marks.count('r')))
w = csv.writer(open(os.path.join(os.path.dirname(__file__), 'map.tsv'), 'w', encoding='utf-8'), delimiter='\t')
w.writerow(['nn', 'action', 'marks', 'patches', 'kept', 'patched', 'restored_or_rendered'])
for r in out: w.writerow(r)
print(sum(r[3] for r in out), 'patches;', sum(1 for r in out if r[1] == 'render'), 'rendered')
