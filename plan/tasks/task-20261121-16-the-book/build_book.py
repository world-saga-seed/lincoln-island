#!/usr/bin/env python3
"""Build the novel (phase 12): front matter, the chapters with the scholar's notes, THE END, White's glossary.

  python3 build_book.py OUT [--only 05800,01950]

Writes OUT.epub (the scholar's notes at the back of each chapter, linked both ways) and
OUT.kepub.epub (the same notes as pop-up footnotes for Kobo), R1121-166. Every addition is read from its
own file and left out when the file is missing (R1121-163): story/front/*, story/scholar/NNNNN.md, and
the chapter 01950. Paragraph ids are source line numbers (p87 is line 87), as tools/epub.py makes them.
Standard library only, except kepubify for the .kepub.epub. Run from the repo root.
"""
import glob, html, os, re, shutil, subprocess, sys, uuid, zipfile, datetime

TITLE = 'Lincoln Island'
RIGHTS = ('Verne (1875) and White (1876): public domain. The restoration, forewords, notes, XIX bis and map, made by language '
          'models in 2026 with a human’s reading: no copyright claimed; any right waived under CC0 1.0.')
AUTHOR = 'Jules Verne; the missing chapter by a model, by the World Saga Seed method'
CSS = """
body { margin: 0 4%; line-height: 1.35; }
h1 { text-align: center; margin: 20% 0 0.6em; font-size: 1.6em; font-weight: normal; }
h1.part { margin: 1.2em 0 1.2em; font-size: 1.3em; }
h2 { text-align: center; margin: 1.2em 0 0.8em; font-size: 1.3em; font-weight: normal; }
p { margin: 0; text-indent: 1.4em; text-align: justify; }
p.summary { text-indent: 0; text-align: center; font-size: 0.85em; margin: 0 1em 1.4em; }
p.vnote { font-size: 0.85em; margin: 0.4em 0 0.4em 1em; text-indent: 0; }
p.break, p.center { text-align: center; text-indent: 0; margin: 0.8em 0; }
p.titlebig { text-align: center; text-indent: 0; font-size: 1.5em; margin: 25% 0 0.5em; }
p.byline { text-align: center; text-indent: 0; margin: 0.4em 0; }
a.nref { text-decoration: none; }
sup { font-size: 0.7em; line-height: 0; }
hr.notes { margin: 2em 30% 0.8em; border: 0; border-top: 1px solid #000; }
section.notes { margin-top: 0; }
section.notes h3 { font-size: 0.95em; font-weight: normal; font-variant: small-caps; text-align: left; margin: 0 0 0.6em; }
section.notes p, aside p { font-size: 0.88em; text-indent: 0; text-align: left; margin: 0 0 0.6em; }
body.front p { text-indent: 0; text-align: left; margin: 0 0 0.75em; }
body.front ul { margin: 0 0 0.75em 1.2em; padding: 0; }
body.front li { margin: 0 0 0.3em; }
body.front p.sign { text-align: right; font-style: italic; }
body.copyright { font-size: 0.75em; line-height: 1.25; }
body.copyright h2 { font-size: 1.2em; margin: 0.5em 0 1em; }
div.img { text-align: center; margin: 1em 0; }
div.img img { max-width: 100%; }
body.gloss p { text-indent: -1.2em; margin: 0 0 0.4em 1.2em; text-align: left; font-size: 0.9em; }
"""


def roman(n):
    s = ''
    for a, b in [(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]:
        while n >= a:
            s += b; n -= a
    return s


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def page(title, body, cls=''):
    c = f' class="{cls}"' if cls else ''
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">\n'
            f'<head><meta charset="utf-8"/><title>{html.escape(title, quote=False)}</title>'
            '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
            f'<body{c}>\n' + '\n'.join(body) + '\n</body>\n</html>\n')


def notes_for(code):
    """The scholar's notes for a chapter: [(letter, anchor, [paragraphs])], or [] if the file is missing."""
    p = f'story/scholar/{code}.md'
    if not os.path.exists(p):
        return []
    out, cur = [], None
    for line in open(p, encoding='utf-8').read().split('\n'):
        m = re.match(r'^## ([a-z]+)\s*$', line)
        if m:
            cur = [m.group(1), None, []]; out.append(cur); continue
        if cur is None:
            continue
        if line.startswith('After: ') and cur[1] is None:
            cur[1] = line[7:].rstrip(); continue
        if line.strip():
            cur[2].append(line.strip())
    for n in out:
        assert n[1] and n[2], (p, n[0])
    return out


TOK = '⁣N{}⁣'


def chapter(path, code, kobo):
    lines = open(path, encoding='utf-8').read().split('\n')
    notes = notes_for(code)
    text = '\n'.join(lines)
    for letter, anchor, _ in notes:
        assert text.count(anchor) == 1, (path, letter, anchor, text.count(anchor))
        text = text.replace(anchor, anchor + TOK.format(letter), 1)
    lines = text.split('\n')
    title, body, after_heading = None, [], False
    for n, line in enumerate(lines, 1):
        t = line.strip()
        if not t:
            continue
        if t.startswith('# ') and title is None:
            title = re.sub(r'\s*\((final|draft \d+)\)\s*$', '', t[2:]).strip(); continue
        h = inline(t)
        if re.match(r'^CHAPTER [IVXL]+', t):
            body.append(f'<h2 id="p{n}">{h}</h2>'); after_heading = True; continue
        if re.match(r'^PART [IVX]+ ?/', t, re.I) or t in ('THE MYSTERIOUS ISLAND.', 'By JULES VERNE.'):
            body.append(f'<h1 class="part" id="p{n}">{h.replace(" / ", "<br/>")}</h1>'); continue
        if after_heading and t.upper() == t and len(t) > 12:
            body.append(f'<p class="summary" id="p{n}">{h}</p>'); after_heading = False; continue
        after_heading = False
        if re.match(r'^\(\d+\) ', t):
            body.append(f'<p class="vnote" id="p{n}">{h}</p>')
        elif set(t) <= set('* ') or set(t) <= set('. '):
            body.append(f'<p class="break" id="p{n}">* * *</p>')
        else:
            body.append(f'<p id="p{n}">{h}</p>')
    def ref(m):
        k = m.group(1)
        return (f'<a class="nref" id="r-{k}" href="#n-{k}" epub:type="noteref" role="doc-noteref">'
                f'<sup>{k}</sup></a>')
    body = [re.sub('⁣N([a-z]+)⁣', ref, b) for b in body]
    if notes:
        body.append('<hr class="notes"/>')  # R1121-170: a rule before the notes
        if kobo:
            for letter, _, paras in notes:
                body.append(f'<aside id="n-{letter}" epub:type="footnote" role="doc-footnote">' +
                            ''.join(f'<p>{"<b>" + letter + ".</b> " if i == 0 else ""}{inline(p)}</p>' for i, p in enumerate(paras)) +
                            '</aside>')
        else:
            body.append('<section class="notes" epub:type="endnotes" role="doc-endnotes"><h3>The scholar’s notes</h3>')
            for letter, _, paras in notes:
                first = f'<a href="#r-{letter}" role="doc-backlink">{letter}.</a> '
                body.append(f'<div id="n-{letter}" epub:type="endnote" role="doc-endnote">' +
                            ''.join(f'<p>{first if i == 0 else ""}{inline(p)}</p>' for i, p in enumerate(paras)) + '</div>')
            body.append('</section>')
    return title, body


def front(path, images):
    text = open(path, encoding='utf-8').read().split('\n')
    title = text[0][2:].strip() if text[0].startswith('# ') else os.path.basename(path)
    body, in_list = [f'<h2>{inline(title)}</h2>'], False
    for t in (l.strip() for l in text[1:]):
        if t.startswith('- '):
            if not in_list: body.append('<ul>'); in_list = True
            body.append(f'<li>{inline(t[2:])}</li>'); continue
        if in_list: body.append('</ul>'); in_list = False
        if not t: continue
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', t)
        if m:
            src = os.path.join(os.path.dirname(path), m.group(2)); images.append(src)
            body.append(f'<div class="img"><img src="images/{os.path.basename(src)}" alt="{html.escape(m.group(1))}"/></div>'); continue
        if t.startswith('|'):
            continue  # the map's table is drawn by the table writer below
        cls = ' class="sign"' if re.match(r'^\*[^*]+\*$', t) and len(t) < 20 else ''
        body.append(f'<p{cls}>{inline(t)}</p>')
    if in_list: body.append('</ul>')
    return title, body


def map_table():
    p = 'plan/tasks/task-20261121-16-the-book/map.tsv'
    rows = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8')][1:]
    out = ['<p>What the restoration did, as a table: for each chapter, the patches made to White’s text and the French paragraphs by mark.</p>', '<table>',
           '<tr><th>Chapter</th><th>Patches</th><th>Kept</th><th>Patched</th><th>Restored</th></tr>']
    for nn, act, marks, pa, k, pt, r in rows:
        n = int(nn)
        if act == 'render':
            out.append(f'<tr><td>{roman(n)}</td><td colspan="4">rendered anew, {len(marks)} paragraphs</td></tr>')
        else:
            out.append(f'<tr><td>{roman(n)}</td><td>{pa}</td><td>{k}</td><td>{pt}</td><td>{r}</td></tr>')
        if n == 19 and os.path.exists('story/prose/01950-the-float-in-the-bar.md'):
            out.append('<tr><td>XIX bis</td><td colspan="4">added; no French</td></tr>')
    return out + ['</table>']


BIS = 'story/prose/01950-the-float-in-the-bar.md'


def build(out, only, kobo):
    global AUTHOR
    bis = os.path.exists(BIS)
    if not bis:  # a fork that took the chapter out (R1121-163): no byline for it, and the map redrawn without it
        AUTHOR = 'Jules Verne'
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'draw_map.py')],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    entries, images = [], []   # (href, title, xhtml)
    entries.append(('title.xhtml', 'Title', page('Title', [
        '<p class="titlebig">THE MYSTERIOUS ISLAND</p>', '<p class="byline">by Jules Verne</p>',
        '<p class="byline">in Stephen W. White’s English of 1876, made unabridged against the French of 1875</p>'] +
        (['<p class="byline">with a missing chapter by a model, by the World Saga Seed method</p>'] if bis else []))))
    for f in ['copyright', 'foreword', 'scholar-preface', 'map']:
        p = f'story/front/{f}.md'
        if os.path.exists(p):
            t, b = front(p, images)
            if f == 'map':
                if not bis:
                    b = [x.replace('; the dotted band is XIX bis, which has no French', '') for x in b]
                b += map_table()
            entries.append((f'{f}.xhtml', t, page(t, b, 'front copyright' if f == 'copyright' else 'front')))
    files = sorted(glob.glob('story/prose/[0-9][0-9][0-9][0-9][0-9]-*.md'))
    for path in files:
        code = os.path.basename(path)[:5]
        if only and code not in only:
            continue
        t, b = chapter(path, code, kobo)
        k = int(code)
        label = f'{roman(k // 100)} bis' if k % 100 else roman(k // 100)
        if code == '06200':
            b.append('<p class="center">THE END.</p>')
        entries.append((f'c{code}.xhtml', f'{label}. {t}', page(t, b)))
    g = 'story/backmatter/white-1876-glossary.md'
    if os.path.exists(g) and not only:
        lines = open(g, encoding='utf-8').read().split('\n')
        body = ['<h2>White’s Glossary (1876)</h2>'] + [f'<p>{inline(l.strip())}</p>' for l in lines[1:]
                                                       if l.strip() and not l.startswith('*') and l.strip() != 'GLOSSARY.']
        entries.append(('glossary.xhtml', 'White’s Glossary (1876)', page('Glossary', body, 'gloss')))
    return write(out, entries, images, sample=bool(only))


def write(out, entries, images, sample=False):
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, TITLE + (' sample' if sample else '')))
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    man = '\n'.join(f'<item id="i{k}" href="{h}" media-type="application/xhtml+xml"/>' for k, (h, _, _) in enumerate(entries))
    man += '\n' + '\n'.join(f'<item id="img{k}" href="images/{os.path.basename(s)}" media-type="image/png"/>' for k, s in enumerate(images))
    spine = '\n'.join(f'<itemref idref="i{k}"/>' for k in range(len(entries)))
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier>
<dc:title>{html.escape(TITLE + (': sample' if sample else ''))}</dc:title>
<dc:creator>{html.escape(AUTHOR)}</dc:creator>
<dc:language>en</dc:language>
<dc:rights>{html.escape(RIGHTS)}</dc:rights>
<meta property="dcterms:modified">{now}</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
{man}
</manifest>
<spine toc="ncx">
{spine}
</spine>
</package>'''
    nav = page('Contents', ['<nav epub:type="toc"><h2>Contents</h2><ol>'] +
               [f'<li><a href="{h}">{html.escape(t, quote=False)}</a></li>' for h, t, _ in entries] + ['</ol></nav>'])
    ncx = ('<?xml version="1.0" encoding="utf-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           f'<head><meta name="dtb:uid" content="{uid}"/></head><docTitle><text>{html.escape(TITLE)}</text></docTitle><navMap>' +
           ''.join(f'<navPoint id="n{k}" playOrder="{k}"><navLabel><text>{html.escape(t, quote=False)}</text></navLabel>'
                   f'<content src="{h}"/></navPoint>' for k, (h, t, _) in enumerate(entries, 1)) + '</navMap></ncx>')
    D = zipfile.ZIP_DEFLATED
    with zipfile.ZipFile(out, 'w') as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', compress_type=D)
        z.writestr('OEBPS/content.opf', opf, compress_type=D)
        z.writestr('OEBPS/nav.xhtml', nav, compress_type=D)
        z.writestr('OEBPS/toc.ncx', ncx, compress_type=D)
        z.writestr('OEBPS/style.css', CSS, compress_type=D)
        for h, _, x in entries:
            z.writestr('OEBPS/' + h, x, compress_type=D)
        for s in images:
            z.write(s, 'OEBPS/images/' + os.path.basename(s), compress_type=zipfile.ZIP_STORED)
    return out


def kepub(base, src=None):
    src = src or base + '.epub'
    k = base + '.kepub.epub'
    if os.path.exists(k):
        os.remove(k)
    if shutil.which('kepubify'):
        subprocess.run(['kepubify', '--output', k, src], check=True, stdout=subprocess.DEVNULL)
        print(k)


def main():
    base = sys.argv[1]
    only = set(sys.argv[3].split(',')) if len(sys.argv) > 3 and sys.argv[2] == '--only' else set()
    os.makedirs(os.path.dirname(base) or '.', exist_ok=True)
    print(build(base + '.epub', only, kobo=False))
    tmp = build(base + '.kobo-src.epub', only, kobo=True)
    kepub(base, tmp)
    os.remove(tmp)


if __name__ == '__main__':
    main()
