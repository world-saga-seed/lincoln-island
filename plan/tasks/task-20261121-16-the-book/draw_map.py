#!/usr/bin/env python3
"""Draw the restoration map (R1121-163, R1121-169) in the form of the earlier draft (tmp/genome-draft/genome2.py):
one band per chapter, its length by the French text; the bands' shade is how much of each passage the patches
restored; the marks above are the patches that changed White's words. Drawn from the patches made, not the
alignment's discord lists. One image per Part, PNG and SVG, into story/front/. Run from the repo root."""
import csv, glob, os, re, statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

T = 'plan/tasks/task-20261121-15-white-unabridged'; OUT = 'story/front'
RENDERED = {6,14,19,20,25,26,30,31,32,33,34,38,42,43,45,47,49,50,51,52,53,54,56,57}
def roman(n):
    s = ''
    for a, b in [(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
        while n >= a: s += b; n -= a
    return s
def nums(s): return [int(x) for x in re.findall(r'\d+', s)]
def tsv_for(nn):
    c = '%05d' % (nn * 100)
    for p in [f'{T}/ch/{c}/patches-{c}.tsv', f'{T}/pilot/patches-{c}.tsv']:
        if os.path.exists(p): return p

beads, plen = {}, {}
for n in range(1, 63):
    beads[n] = [r for r in csv.DictReader(open('texts/align/%02d.tsv' % n, encoding='utf-8'), delimiter='\t') if r['kind'] != 'summary']
    plen[n] = {int(m.group(1)): len(m.group(2)) for l in open('texts/fr-1875/%02d.md' % n, encoding='utf-8')
               for m in [re.match(r'¶(\d+) (?:\[p\.\d+\] )?(.*)', l)] if m and m.group(1) != '0'}
base = statistics.median(int(r['white_chars']) / int(r['fr_chars']) for rs in beads.values() for r in rs
                         if r['kind'] == '1-1' and int(r['fr_chars']) > 200)

def chapter(n):
    """[(x0, x1, shade)], [x of change marks], end"""
    start, x = {}, 0
    for p in sorted(plen[n]): start[p] = x; x += plen[n][p]
    end = x
    if n in RENDERED: return None, None, end
    wp = {int(m.group(1)): m.group(2) for l in open('texts/white-1876/%02d.md' % n, encoding='utf-8')
          for m in [re.match(r'^¶(\d+) (.*)', l)] if m}
    restored, marks = {}, []   # white ¶ -> chars restored; (white ¶, fraction)
    for r in csv.DictReader(open(tsv_for(n), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['discord'] == 'glossary': continue
        old, new = r['old'], r['new'] or ''
        if old.startswith('@¶'):
            w = int(old[2:]); add = len(new) - len(wp.get(w, ''))
            if add > 40: restored[w] = restored.get(w, 0) + add
            else: marks.append((w, 0.5))
            continue
        hit = [(w, t.find(old)) for w, t in wp.items() if old in t] or [(w, t.find(old[:40])) for w, t in wp.items() if old[:40] in t]
        if not hit: continue
        w, at = hit[0]; add = len(new) - len(old)
        if add > 40 or '¶' in new: restored[w] = restored.get(w, 0) + max(add, 0)
        else: marks.append((w, (at + len(old) / 2) / max(len(wp[w]), 1)))
    bands, where = [], {}
    for b in beads[n]:
        fs, ws = nums(b['fr']), nums(b['white'])
        if not fs: continue
        x0 = start.get(fs[0], 0); x1 = start.get(fs[-1], end) + plen[n].get(fs[-1], 0)
        fr = int(b['fr_chars']) or 1
        k = 1.0 if not ws else sum(restored.get(w, 0) for w in range(ws[0], ws[-1] + 1)) / (fr * base)
        shade = '#000000' if k >= 0.95 else '#525252' if k >= 0.40 else '#969696' if k >= 0.05 else '#d9d9d9'
        bands.append((x0, x1, shade))
        if ws:
            for i, w in enumerate(range(ws[0], ws[-1] + 1)):
                where[w] = (x0 + (x1 - x0) * i / len(range(ws[0], ws[-1] + 1)), (x1 - x0) / len(range(ws[0], ws[-1] + 1)))
    xs = [where[w][0] + where[w][1] * f for w, f in marks if w in where]
    return bands, xs, end

data = {n: chapter(n) for n in range(1, 63)}
bis = os.path.exists('story/prose/01950-the-float-in-the-bar.md')
bislen = len(open('story/prose/01950-the-float-in-the-bar.md', encoding='utf-8').read()) / base if bis else 0
maxlen = max(d[2] for d in data.values())
PARTS = [('Part I: Shipwrecked in the Air', 1, 22, 1), ('Part II: The Abandoned', 23, 42, 2), ('Part III: The Secret of the Island', 43, 62, 3)]
for title, lo, hi, k in PARTS:
    rows = []
    for n in range(lo, hi + 1):
        rows.append((roman(n), n))
        if n == 19 and bis: rows.append(('XIX bis', None))
    fig, ax = plt.subplots(figsize=(8.2, 0.42 * len(rows) + 2.6))
    nmark = 0
    for i, (lab, n) in enumerate(rows):
        y = -i * 1.25
        if n is None:
            ax.barh(y, bislen, left=0, height=0.62, color='white', edgecolor='#1a1a1a', hatch='....', linewidth=0.6)
            ax.text(bislen + maxlen * 0.01, y, 'added; no French', fontsize=7.5, va='center', color='#333333')
        elif data[n][0] is None:
            ax.barh(y, data[n][2], left=0, height=0.62, color='white', edgecolor='#1a1a1a', hatch='////', linewidth=0.6)
            ax.text(data[n][2] + maxlen * 0.01, y, 'rendered anew', fontsize=7.5, va='center', color='#333333')
        else:
            bands, xs, end = data[n]
            for x0, x1, c in bands: ax.barh(y, x1 - x0, left=x0, height=0.62, color=c, linewidth=0)
            ax.scatter(xs, [y + 0.5] * len(xs), marker='v', s=9, facecolor='#1a1a1a', edgecolor='none', zorder=3)
            nmark += len(xs)
        ax.text(-maxlen * 0.012, y, lab, fontsize=8.5, ha='right', va='center', color='#1a1a1a')
    ax.set_xlim(-maxlen * 0.08, maxlen * 1.13); ax.set_ylim(-len(rows) * 1.25 + 0.4, 1.0); ax.axis('off')
    ax.set_title(f"{title}\nOne band per chapter, its length by Verne's French. Shade: what the patches put back.\nMarks: the patches that changed White's words.",
                 fontsize=10, loc='left', color='#1a1a1a')
    h = [Patch(fc=c, ec='#666666', lw=0.5, label=l) for c, l in [('#d9d9d9', "White's words stand"), ('#969696', 'Some put back (5 to 40%)'),
         ('#525252', 'Mostly put back (40 to 95%)'), ('#000000', 'Put back whole')]]
    h += [Patch(fc='white', ec='#1a1a1a', hatch='////', label='Rendered anew from the French')]
    if k == 1 and bis: h += [Patch(fc='white', ec='#1a1a1a', hatch='....', label='XIX bis, added')]
    h += [Line2D([], [], marker='v', ls='none', markerfacecolor='#1a1a1a', markeredgecolor='none', markersize=5, label=f'A patch changed the words ({nmark})')]
    ax.legend(handles=h, loc='upper left', bbox_to_anchor=(0, 0), ncol=2, fontsize=7.5, frameon=False)
    for ext in ('png', 'svg'):
        fig.savefig(os.path.join(OUT, f'map-part-{k}.{ext}'), dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
print('base %.2f' % base)
