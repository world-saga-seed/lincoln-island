#!/usr/bin/env python3
"""Draw the map (R1124-07, replacing R1121-169) in the form of the first draft (genome2.py): what White's 1876
English did to Verne's French. One band per chapter, its length by the French text; the bands' shade is how much of
each passage White kept (from the alignment, texts/align/NN.tsv); the marks are White's departures (from the labelled
discord lists, texts/align/NN-discords.md). A chapter rendered anew is drawn the same, with a symbol at its row's end;
XIX bis, which has no French, is a symbol alone. One image per Part, PNG and SVG, into story/front/. Run from the
repo root."""
import csv, glob, os, re, statistics
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt'] = 'lincoln-island'  # stable ids, so a rebuild leaves the files unchanged
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

def pnum(s): return [int(x) for x in re.findall(r'¶(\d+)', s)]
disc = {}
for n in range(1, 63):
    disc[n] = []
    dp = 'texts/align/%02d-discords.md' % n
    if os.path.exists(dp):
        for line in open(dp, encoding='utf-8'):
            m = re.match(r'### \d+\. ([a-z]+): .*\(([IV]+)\.\d+ (¶\d+(?:–¶\d+)?)', line)
            if m:
                ps = pnum(m.group(3)); disc[n].append((m.group(1), ps[0], ps[-1]))

SH = [(0.75, '#d9d9d9'), (0.40, '#969696'), (0.05, '#525252'), (-1, '#000000')]
def shade(r):
    fr, wh = int(r['fr_chars']), int(r['white_chars'] or 0)
    k = wh / fr / base if fr else 1
    return next(c for lo, c in SH if k >= lo)
MK = {'changed': ('v', '#1a1a1a', 'Changed fact or meaning'), 'softened': ('o', '#ffffff', 'Softened'),
      'addition': ('P', '#1a1a1a', 'White adds'), 'cut': ('|', '#1a1a1a', 'Cut within a passage')}

def chapter(n):
    """[(x0, x1, shade)], [(kind, x)], end"""
    start, x = {}, 0
    for p in sorted(plen[n]): start[p] = x; x += plen[n][p]
    end = x
    bands = []
    for r in beads[n]:
        ps = pnum(r['fr'])
        if not ps: continue
        a, b = ps[0], ps[-1]
        bands.append((start.get(a, 0), start.get(b, end) + plen[n].get(b, 0), shade(r)))
    marks = [(k, (start.get(a, 0) + start.get(b, 0) + plen[n].get(b, 0)) / 2) for k, a, b in disc[n] if k in MK]
    return bands, marks, end

data = {n: chapter(n) for n in range(1, 63)}
bis = os.path.exists('story/prose/01950-the-float-in-the-bar.md')
maxlen = max(d[2] for d in data.values())
PARTS = [('Part I: Shipwrecked in the Air', 1, 22, 1), ('Part II: The Abandoned', 23, 42, 2), ('Part III: The Secret of the Island', 43, 62, 3)]
REND = dict(marker='*', s=70, facecolor='#1a1a1a', edgecolor='none', zorder=3)
BIS = dict(marker='D', s=30, facecolor='white', edgecolor='#1a1a1a', linewidths=0.9, zorder=3)
for title, lo, hi, k in PARTS:
    rows = []
    for n in range(lo, hi + 1):
        rows.append((roman(n), n))
        if n == 19 and bis: rows.append(('XIX bis', None))
    fig, ax = plt.subplots(figsize=(8.2, 0.42 * len(rows) + 2.6))
    counts = {}
    for i, (lab, n) in enumerate(rows):
        y = -i * 1.25
        if n is None:
            ax.scatter([maxlen * 0.012], [y], **BIS)
        else:
            bands, marks, end = data[n]
            for x0, x1, c in bands: ax.barh(y, x1 - x0, left=x0, height=0.62, color=c, linewidth=0)
            for kind, xm in marks:
                counts[kind] = counts.get(kind, 0) + 1
                if kind == 'cut':
                    ax.plot([xm, xm], [y - 0.36, y - 0.5], color='#1a1a1a', lw=1.0)
                else:
                    m, fc, _ = MK[kind]
                    ax.scatter([xm], [y + 0.48], marker=m, s=16, facecolor=fc, edgecolor='#1a1a1a', linewidths=0.6, zorder=3)
            if n in RENDERED: ax.scatter([end + maxlen * 0.025], [y], **REND)
        ax.text(-maxlen * 0.012, y, lab, fontsize=8.5, ha='right', va='center', color='#1a1a1a')
    ax.set_xlim(-maxlen * 0.08, maxlen * 1.06); ax.set_ylim(-len(rows) * 1.25 + 0.4, 1.0); ax.axis('off')
    ax.set_title(f"{title}\nWhat White's English of 1876 did to Verne's French. One band per chapter, its length by the French.\nShade: how much of each passage White kept. Marks: where he departed from it.",
                 fontsize=10, loc='left', color='#1a1a1a')
    h = [Patch(fc=c, ec='#666666', lw=0.5, label=l) for (lo_, c), l in zip(SH, ['Kept', 'Condensed (40 to 75% kept)', 'Mostly cut (5 to 40% kept)', 'Cut whole'])]
    h += [Line2D([], [], marker=MK[q][0], ls='none', markerfacecolor=MK[q][1], markeredgecolor='#1a1a1a', markersize=5, label=f'{MK[q][2]} ({counts.get(q, 0)})') for q in ('changed', 'softened', 'addition')]
    h += [Line2D([], [], marker='|', ls='none', color='#1a1a1a', markersize=7, label=f"{MK['cut'][2]} ({counts.get('cut', 0)})")]
    h += [Line2D([], [], marker='*', ls='none', markerfacecolor='#1a1a1a', markeredgecolor='none', markersize=9, label='Rendered anew from the French')]
    if k == 1 and bis: h += [Line2D([], [], marker='D', ls='none', markerfacecolor='white', markeredgecolor='#1a1a1a', markersize=5, label='XIX bis, added; no French')]
    ax.legend(handles=h, loc='upper left', bbox_to_anchor=(0, 0), ncol=2, fontsize=7.5, frameon=False)
    for ext in ('png', 'svg'):
        fig.savefig(os.path.join(OUT, f'map-part-{k}.{ext}'), dpi=170, bbox_inches='tight', facecolor='white',
                    metadata={'Date': None} if ext == 'svg' else {'Software': None})
    plt.close(fig)
print('base %.2f' % base)
