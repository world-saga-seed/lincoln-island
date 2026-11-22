#!/usr/bin/env python3
"""Build the run's book (R1121-160; roadmap phase 12): XIX, XIX bis and XX, each as White, the two prompt-only
controls, v1 and the final, labelled; then the three chapters' cards and the ledger. Run from the repo root.
  python3 build_run.py build/lincoln-island-run
"""
import glob, html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_book as B

C = 'plan/tasks/task-20261121-09-controls'
V1 = 'plan/archive/task-20261121-11-render-v1/snapshot'
HERE = os.path.dirname(__file__)

def plain_lines(path, skip_title):
    lines = open(path, encoding='utf-8').read().split('\n')
    if skip_title and lines and lines[0].startswith('# '): lines = lines[1:]
    return lines

def chapter_body(lines):
    body, after = [], False
    for t in (l.strip() for l in lines):
        if not t: continue
        h = B.inline(t)
        if re.match(r'^CHAPTER [IVXL]+', t): body.append(f'<h2>{h}</h2>'); after = True; continue
        if after and t.upper() == t and len(t) > 12: body.append(f'<p class="summary">{h}</p>'); after = False; continue
        after = False
        if set(t) <= set('* ') or t == '---': body.append('<p class="break">* * *</p>')
        elif re.match(r'^\(\d+\) ', t): body.append(f'<p class="vnote">{h}</p>')
        else: body.append(f'<p>{h}</p>')
    return body

def white(nn):
    out = []
    for l in open(f'texts/white-1876/{nn}.md', encoding='utf-8'):
        m = re.match(r'^(hd|¶\d+|n\d+)(?: \[[^\]]*\])? (.*)$', l.rstrip('\n'))
        if m: out.append(m.group(2))
    return out

def md_page(path):
    """Cards and ledger: headings, lists, tables as paragraphs; links reduced to their text."""
    body = []
    for raw in open(path, encoding='utf-8').read().split('\n'):
        t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', raw.rstrip())
        s = t.strip()
        if not s or re.match(r'^\|[-| :]+\|$', s): continue
        if s.startswith('#'):
            lvl = len(s) - len(s.lstrip('#'))
            body.append(f'<h{min(lvl + 1, 4)}>{B.inline(s.lstrip("#").strip())}</h{min(lvl + 1, 4)}>'); continue
        if s.startswith('|'):
            cells = [c.strip() for c in s.strip('|').split('|')]
            body.append('<p class="row">' + ' · '.join(B.inline(c) for c in cells if c) + '</p>'); continue
        m = re.match(r'^(\s*)[-*] (.*)', t)
        if m:
            ind = len(m.group(1)) // 2
            body.append(f'<p class="li" style="margin-left:{1 + ind * 1.2}em">• {B.inline(m.group(2))}</p>'); continue
        body.append(f'<p>{B.inline(s)}</p>')
    return body

CSS_EXTRA = """
p.row, p.li { text-indent: 0; text-align: left; font-size: 0.85em; margin: 0 0 0.45em; }
body.rec p { text-indent: 0; text-align: left; font-size: 0.88em; margin: 0 0 0.5em; }
h4 { font-size: 0.95em; font-weight: normal; font-style: italic; margin: 1em 0 0.4em; }
p.label { text-indent: 0; text-align: center; font-style: italic; margin: 0 0 1em; }
"""

def main():
    out = sys.argv[1]
    entries, images = [], []
    pg = lambda t, b, c='': B.page(t, b, c)
    entries.append(('title.xhtml', 'Title', pg('Title', ['<p class="titlebig">LINCOLN ISLAND: THE RUN</p>',
        '<p class="byline">chapters XIX, XIX bis and XX in every version, with the cards and the ledger</p>'])))
    t, b = B.front(os.path.join(HERE, 'run-front.md'), images)
    entries.append(('about.xhtml', t, pg(t, b, 'front')))
    chs = [('01900', '19', 'XIX'), ('01950', None, 'XIX bis'), ('02000', '20', 'XX')]
    for code, nn, rom in chs:
        final = glob.glob(f'story/prose/{code}-*.md')[0]
        versions = []
        if nn: versions.append(('white', 'White’s translation (1876)', white(nn)))
        versions.append(('opus', 'The Opus control (prompt only)', plain_lines(f'{C}/opus/opus-{code}.md', False)))
        versions.append(('gemini', 'The Gemini control (prompt only)', plain_lines(f'{C}/gemini/gemini-{code}.md', False)))
        versions.append(('v1', 'Version 1 (World Saga Seed, first draft)', plain_lines(glob.glob(f'{V1}/{code}-*.md')[0], True)))
        versions.append(('final', 'The final', plain_lines(final, True)))
        for key, label, lines in versions:
            body = [f'<h1 class="part">{rom}</h1>', f'<p class="label">{label}</p>'] + chapter_body(lines)
            entries.append((f'c{code}-{key}.xhtml', f'{rom}. {label}', pg(f'{rom}. {label}', body)))
    for code, _, rom in chs:
        p = glob.glob(f'story/notes/{code}-*.md')[0]
        entries.append((f'n{code}.xhtml', f'The cards: {rom}', pg(f'The cards: {rom}', [f'<h2>The cards: {rom}</h2>'] + md_page(p), 'rec')))
    for p in sorted(glob.glob('plan/settled/ledger/*.md')):
        d = os.path.basename(p)[:-3]
        entries.append((f'l{d}.xhtml', f'The ledger: {d}', pg(f'The ledger: {d}', md_page(p), 'rec')))
    B.CSS += CSS_EXTRA
    B.TITLE = 'Lincoln Island: The Run'
    B.write(out + '.epub', entries, images)
    print(out + '.epub')
    B.kepub(out)

if __name__ == '__main__':
    main()
