#!/usr/bin/env python3
"""Build an EPUB from drafted chapters, so the writer can read a volume as a reader would.

Each chapter becomes its own page named for its file, and every paragraph
carries its source line number as an id (p87 is line 87), so a highlight made
on the ereader can be traced back to the exact line of the source file.

Two ways to name the chapters:

  1. List the files, in order:
       python3 tools/epub.py --title "Volume 1" --out build/volume-1.epub story/prose/00*.md

  2. Give a number range, and let outlined chapters with no prose yet show
     as "[Not yet drafted.]" pages, so the gaps are visible where they fall:
       python3 tools/epub.py --title "Volume 1" --out build/volume-1.epub \\
           --prose story/prose --outline story/outline --from 100 --to 2000

  Chapter files are named by number and slug: 00100-the-causeway.md.

Options:
  --title T        the book's title (required)
  --author A       the author line (default: "Unknown")
  --series S       a series name; with --index N, readers that group series will
  --index N        group the books (EPUB 3 and calibre metadata both)
  --front FILE     a front-matter page set before the first chapter; if the
                   file has a line "---", only what follows it is used
  --out FILE       where to write the .epub (folders are created)
  --kepub          also run kepubify (if installed) for Kobo readers

What goes in: each file's text only. The first "# " line is the chapter title
(a trailing "(draft N)" is dropped); other headings become subheads; "---" is a
scene break; <!-- comments --> are dropped; *italic* and **bold** are kept.
Standard library only. Check the result with epubcheck if you have it.
"""
import argparse, glob, html, os, re, shutil, subprocess, sys, uuid, zipfile, datetime

CSS = """html { font-size: 100%; }
body { margin: 0 4%; font-size: 1em; line-height: 1.35; }
h1 { text-align: center; margin: 30% 0 0.5em; font-size: 1.8em; font-weight: normal; }
h2 { text-align: center; margin: 2em 0 1.5em; font-size: 1.4em; font-weight: normal; }
h3 { text-align: center; font-size: 1.1em; font-weight: normal; }
p { margin: 0; text-indent: 1.4em; text-align: justify; }
h2 + p, p.break + p { text-indent: 0; }
p.break { text-align: center; text-indent: 0; margin: 0.8em 0; }
p.placeholder, p.byline { text-indent: 0; text-align: center; }
body.front p { text-indent: 0; text-align: left; margin: 0 0 0.75em; }
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    return s


def chapter(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    title, body, comment = None, [], False
    for n, line in enumerate(lines, 1):
        t = line.strip()
        if comment or t.startswith('<!--'):
            comment = '-->' not in t
            continue
        if not t:
            continue
        if t.startswith('# ') and title is None:
            title = re.sub(r'\s*\(draft \d+\)\s*$', '', t[2:]).strip()
            continue
        if t.startswith('#'):
            body.append(f'<h3 id="p{n}">{inline(t.lstrip("#").strip())}</h3>')
        elif t in ('---', '* * *', '***'):
            body.append(f'<p id="p{n}" class="break">*</p>')
        else:
            body.append(f'<p id="p{n}">{inline(t)}</p>')
    return title or os.path.splitext(os.path.basename(path))[0], body


def front(path):
    text = open(path, encoding='utf-8').read()
    if '\n---\n' in text:
        text = text.split('\n---\n', 1)[1]
    title, body = 'Before you begin', []
    for t in (l.strip() for l in text.split('\n')):
        if not t:
            continue
        if t.startswith('# '):
            title = t[2:].strip()
        elif t.startswith('#'):
            body.append(f'<h3>{inline(t.lstrip("#").strip())}</h3>')
        else:
            body.append(f'<p>{inline(t[2:] if t.startswith("- ") else t)}</p>')
    return title, body


def page(title, body, cls='', heading=True):
    h = f'<h2>{html.escape(title, quote=False)}</h2>\n' if heading else ''
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n'
            f'<head><title>{html.escape(title, quote=False)}</title>'
            '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
            f'<body class="{cls}">{h}' + '\n'.join(body) + '\n</body></html>\n')


def numbered(folder):
    out = {}
    for p in glob.glob(os.path.join(folder, '[0-9][0-9][0-9][0-9][0-9]*.md')):
        out[int(os.path.basename(p)[:5])] = p
    return out


def main():
    ap = argparse.ArgumentParser(description='Build an EPUB from drafted chapters.')
    ap.add_argument('files', nargs='*', help='prose files in reading order (or use --prose with --from and --to)')
    ap.add_argument('--title', required=True, help='the book title')
    ap.add_argument('--author', default='Unknown', help='the author name (default: Unknown)')
    ap.add_argument('--series', help='series name, for series metadata')
    ap.add_argument('--index', type=int, default=1, help='the book number in the series (default: 1)')
    ap.add_argument('--front', help="front-matter file; only what follows its first '---' is used")
    ap.add_argument('--out', required=True, help='the EPUB file to write')
    ap.add_argument('--prose', help='folder of numbered prose files (00100-slug.md), taken by --from and --to')
    ap.add_argument('--outline', help='folder of numbered outlines; an outlined chapter with no prose gets a "[Not yet drafted.]" page')
    ap.add_argument('--from', dest='lo', type=int, help='first chapter number, e.g. 100')
    ap.add_argument('--to', dest='hi', type=int, help='last chapter number, e.g. 2000')
    ap.add_argument('--kepub', action='store_true', help='also run kepubify, if installed, for Kobo readers')
    a = ap.parse_args()

    entries = []   # (id, href, title, xhtml)
    if a.front:
        t, b = front(a.front)
        entries.append(('front', 'front.xhtml', t, page(t, b, 'front')))
    if a.files:
        for p in a.files:
            t, b = chapter(p)
            stem = re.sub(r'[^A-Za-z0-9_-]', '-', os.path.splitext(os.path.basename(p))[0])
            entries.append((f'c-{stem}', f'c-{stem}.xhtml', t, page(t, b)))
    elif a.prose and a.lo is not None and a.hi is not None:
        prose = numbered(a.prose)
        outline = numbered(a.outline) if a.outline else {}
        for n in sorted(k for k in set(prose) | set(outline) if a.lo <= k <= a.hi):
            if n in prose:
                t, b = chapter(prose[n])
            else:
                t = re.sub(r'^#\s*', '', open(outline[n], encoding='utf-8').readline()).strip()
                t = re.sub(r'\s*\(outline\)\s*$', '', t)
                b = ['<p class="placeholder">[Not yet drafted.]</p>']
            entries.append((f'c{n:05d}', f'c{n:05d}.xhtml', t, page(t, b)))
    else:
        ap.error('give chapter files, or --prose with --from and --to')
    if not [e for e in entries if e[0] != 'front']:
        sys.exit('no chapters found')

    titlepage = page(a.title, [f'<h1>{html.escape(a.title, quote=False)}</h1>',
                               f'<p class="byline">{html.escape(a.author, quote=False)}</p>'], heading=False)
    uid = f'urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, "story-kit/" + a.title)}'
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    series = ''
    if a.series:
        s = html.escape(a.series, quote=False)
        series = (f'<meta property="belongs-to-collection" id="series">{s}</meta>\n'
                  '<meta refines="#series" property="collection-type">series</meta>\n'
                  f'<meta refines="#series" property="group-position">{a.index}</meta>\n'
                  f'<meta name="calibre:series" content="{html.escape(a.series)}"/>\n'
                  f'<meta name="calibre:series_index" content="{a.index}"/>\n')
    manifest = '\n'.join(f'<item id="{i}" href="{h}" media-type="application/xhtml+xml"/>' for i, h, _, _ in entries)
    spine = '\n'.join(f'<itemref idref="{i}"/>' for i, _, _, _ in entries)
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier>
<dc:title>{html.escape(a.title, quote=False)}</dc:title>
<dc:creator>{html.escape(a.author, quote=False)}</dc:creator>
<dc:language>en</dc:language>
{series}<meta property="dcterms:modified">{stamp}</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
<item id="titlepage" href="title.xhtml" media-type="application/xhtml+xml"/>
{manifest}
</manifest>
<spine toc="ncx">
<itemref idref="titlepage"/>
{spine}
</spine>
</package>'''
    nav = page('Contents', ['<nav epub:type="toc"><ol>'] +
               [f'<li><a href="{h}">{html.escape(t, quote=False)}</a></li>' for _, h, t, _ in entries] +
               ['</ol></nav>'])
    ncx = ('<?xml version="1.0" encoding="utf-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           f'<head><meta name="dtb:uid" content="{uid}"/></head>'
           f'<docTitle><text>{html.escape(a.title, quote=False)}</text></docTitle><navMap>' +
           ''.join(f'<navPoint id="n{k}" playOrder="{k}"><navLabel><text>{html.escape(t, quote=False)}</text>'
                   f'</navLabel><content src="{h}"/></navPoint>' for k, (_, h, t, _) in enumerate(entries, 1)) +
           '</navMap></ncx>')
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    D = zipfile.ZIP_DEFLATED
    with zipfile.ZipFile(a.out, 'w') as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml',
                   '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                   '</rootfiles></container>', compress_type=D)
        z.writestr('OEBPS/content.opf', opf, compress_type=D)
        z.writestr('OEBPS/nav.xhtml', nav, compress_type=D)
        z.writestr('OEBPS/toc.ncx', ncx, compress_type=D)
        z.writestr('OEBPS/style.css', CSS, compress_type=D)
        z.writestr('OEBPS/title.xhtml', titlepage, compress_type=D)
        for _, href, _, text in entries:
            z.writestr('OEBPS/' + href, text, compress_type=D)
    words = sum(len(re.sub('<[^>]+>', ' ', e[3]).split()) for e in entries)
    print(f'{a.out}: {len(entries)} pages, about {words} words')
    if a.kepub:
        if shutil.which('kepubify'):
            kepub = re.sub(r'\.epub$', '', a.out) + '.kepub.epub'
            if os.path.exists(kepub):
                os.remove(kepub)
            subprocess.run(['kepubify', '--output', kepub, a.out], check=True, stdout=subprocess.DEVNULL)
            print(kepub)
        else:
            print('kepubify not found; built the plain EPUB only')


if __name__ == '__main__':
    main()
