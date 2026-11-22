#!/usr/bin/env python3
"""Draw the restoration map (R1121-163, R1121-167) from map.tsv: one image per Part, as SVG and PNG,
and the plain table, into story/front/. One row per chapter, one cell per French paragraph.
Greys that read on e-ink: kept white, patched mid grey, restored black, rendered hatched; XIX bis dotted."""
import csv, os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(__file__); OUT = 'story/front'
os.makedirs(OUT, exist_ok=True)
rows = list(csv.DictReader(open(os.path.join(HERE, 'map.tsv'), encoding='utf-8'), delimiter='\t'))
ROM = lambda n: ['', 'I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII'][n] if n <= 22 else None
def roman(n):
    v = [(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]; s=''
    for a,b in v:
        while n >= a: s += b; n -= a
    return s
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
parts = [('Part I. Shipwrecked in the Air', 1, 22), ('Part II. The Abandoned', 23, 42), ('Part III. The Secret of the Island', 43, 62)]
W, LEFT, CW, RH, TOP = 1200, 80, 5, 30, 70
GREY = {'k': (255,255,255), 'p': (150,150,150), 'r': (0,0,0)}
maxn = max(len(r['marks']) for r in rows)
def chapter_rows(lo, hi):
    out = []
    for r in rows:
        n = int(r['nn'])
        if lo <= n <= hi:
            out.append((roman(n), r))
            if n == 19: out.append(('XIX bis', None))
    return out
def label(r):
    if r is None: return 'added: no French'
    if r['action'] == 'render': return f"rendered anew, {len(r['marks'])} ¶"
    return f"{r['patches']} patches: {r['kept']} kept, {r['patched']} patched, {r['restored_or_rendered']} restored"
def draw(title, lo, hi, stem):
    cr = chapter_rows(lo, hi)
    H = TOP + RH * len(cr) + 20
    im = Image.new('L', (W, H), 255); d = ImageDraw.Draw(im)
    f, fb, fs = ImageFont.truetype(FONT, 17), ImageFont.truetype(FB, 22), ImageFont.truetype(FONT, 14)
    d.text((LEFT, 18), title, font=fb, fill=0)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{title}: the restoration, paragraph by paragraph">',
           '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/><line x1="0" y1="0" x2="0" y2="6" stroke="#000" stroke-width="3"/></pattern>'
           '<pattern id="dots" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fff"/><circle cx="3" cy="3" r="1.4" fill="#000"/></pattern></defs>',
           f'<rect width="{W}" height="{H}" fill="#fff"/>',
           f'<text x="{LEFT}" y="40" font-family="serif" font-weight="bold" font-size="22">{title}</text>']
    for i, (name, r) in enumerate(cr):
        y = TOP + i * RH; h = RH - 10
        d.text((6, y - 2), name, font=f, fill=0)
        svg.append(f'<text x="6" y="{y + 14}" font-family="serif" font-size="17">{name}</text>')
        if r is None or r['action'] == 'render':
            n = len(r['marks']) if r else 40
            x1 = LEFT + n * CW
            d.rectangle([LEFT, y, x1, y + h], fill=255, outline=0)
            if r is None:
                for xx in range(LEFT + 3, x1, 6):
                    for yy in range(y + 3, y + h, 6): d.ellipse([xx - 1, yy - 1, xx + 1, yy + 1], fill=0)
            else:
                for k in range(0, x1 - LEFT, 7): d.line([(LEFT + k, y + h), (LEFT + k + h, y)], fill=0, width=2)
                d.rectangle([LEFT, y + h + 1, x1 + h + 2, y + h + 6], fill=255); d.rectangle([x1 + 1, y - 1, x1 + h + 2, y + h + 6], fill=255)
                d.rectangle([LEFT, y, x1, y + h], outline=0)
            svg.append(f'<rect x="{LEFT}" y="{y}" width="{n * CW}" height="{h}" fill="url(#{"dots" if r is None else "hatch"})" stroke="#000" stroke-width="1"/>')
        else:
            for j, m in enumerate(r['marks']):
                x = LEFT + j * CW
                d.rectangle([x, y, x + CW - 1, y + h], fill=GREY[m][0], outline=0 if m == 'k' else None)
                fill = {'k': '#fff', 'p': '#969696', 'r': '#000'}[m]
                svg.append(f'<rect x="{x}" y="{y}" width="{CW - 1}" height="{h}" fill="{fill}" stroke="#000" stroke-width="{0.6 if m == "k" else 0}"/>')
        tx = LEFT + maxn * CW + 12
        d.text((tx, y), label(r), font=fs, fill=0)
        svg.append(f'<text x="{tx}" y="{y + 14}" font-family="serif" font-size="14">{label(r)}</text>')
    svg.append('</svg>')
    im.save(os.path.join(OUT, stem + '.png'), optimize=True)
    open(os.path.join(OUT, stem + '.svg'), 'w', encoding='utf-8').write('\n'.join(svg) + '\n')
for (t, lo, hi), stem in zip(parts, ['map-part-1', 'map-part-2', 'map-part-3']):
    draw(t, lo, hi, stem)
print('ok', maxn * CW + LEFT + 12)
