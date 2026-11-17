#!/usr/bin/env python3
"""Check the heads of the cards, build each folder's index from them, and find cards.

A card is one short file about one thing (a person, a place, an object, a rule).
It opens with a fixed head of five lines:

    # <Name>: <what it is>
    (blank)
    *<one-line summary>*
    (blank)
    Keywords: <words a search would reach for that the card does not use>

Card folders are the subfolders of --root (for example world/people/,
world/places/). Each card folder has a README.md that holds its index table
between these two markers; the table is built by this tool, never edited by hand:

    <!-- cards: built by tools/cards.py; do not edit -->
    <!-- /cards -->

(Any comment starting "<!-- cards:" opens the table, so the wording is yours.)

Usage:
  python3 tools/cards.py check [--root DIR] [-v]   exit 1 on a head out of form or a stale table;
                                                   -v also lists keywords the card's text already uses
  python3 tools/cards.py build [--root DIR]        rewrite every folder's table from the heads
  python3 tools/cards.py find WORD ... [--root DIR]  cards whose head holds every word,
                                                   then cards whose text does
  python3 tools/cards.py index [--root DIR] [--sheets DIR]
                                                   write DIR/INDEX.md, the subject index: every
                                                   card by its name, what it is and its keywords,
                                                   every folder and every character sheet, A to Z
  python3 tools/cards.py build --index ...         build, then write the subject index
  --root DIR defaults to "world".
  --mark WORD   a status mark a card's name may end with, "(WORD)", left out of
                the tables and the index (repeatable; for example --mark proposal)

The subject index also lists the loose files at the top of --root (a guide, a
glossary) by their title.
"""
import argparse, glob, os, re, sys

BEGIN = '<!-- cards: built by tools/cards.py; do not edit -->'
BEGIN_RX = re.compile(r'<!-- cards:.*?-->')
END = '<!-- /cards -->'
MARKS = []
TOOL = os.path.relpath(sys.argv[0]) if sys.argv[0].endswith('.py') else 'tools/cards.py'
TITLE = re.compile(r'^# (.+?): (.+)$')


def folders(root):
    out = set()
    for p in glob.glob(os.path.join(root, '**', '*.md'), recursive=True):
        d = os.path.dirname(p)
        if os.path.basename(p) != 'README.md' and os.path.abspath(d) != os.path.abspath(root):
            out.add(d)
    return sorted(out)


def cards(d):
    return sorted(p for p in glob.glob(os.path.join(d, '*.md')) if os.path.basename(p) != 'README.md')


def head(p):
    """(name, what, summary, keywords, errors) for the card at p."""
    lines = open(p, encoding='utf-8').read().split('\n') + [''] * 5
    err = []
    m = TITLE.match(lines[0])
    if not m:
        err.append('line 1 is not "# <Name>: <what it is>"')
    if lines[1].strip() or lines[3].strip():
        err.append('lines 2 and 4 must be blank')
    if not re.match(r'^\*[^*].*[^*]\*$', lines[2].strip()):
        err.append('line 3 is not one italic summary line')
    if not lines[4].startswith('Keywords: ') or not lines[4][10:].strip():
        err.append('line 5 is not "Keywords: ..."')
    name, what = (m.group(1), m.group(2)) if m else (lines[0].lstrip('# '), '')
    if MARKS:
        name = re.sub(r' \((?:' + '|'.join(map(re.escape, MARKS)) + r')\)$', '', name, flags=re.I)
    kw = [k.strip() for k in lines[4][10:].split(',') if k.strip()] if lines[4].startswith('Keywords: ') else []
    return name, what, lines[2].strip().strip('*'), kw, err


def table(d):
    rows = sorted(((head(p)[:2], os.path.basename(p)) for p in cards(d)),
                  key=lambda r: re.sub(r'^the ', '', r[0][0].lower()))
    return '\n'.join(['| Card | What it is |', '|---|---|'] +
                     [f'| [{n}]({f}) | {w} |' for (n, w), f in rows])


def readme(d):
    p = os.path.join(d, 'README.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    m = BEGIN_RX.search(t)
    b = t.find(END)
    return (t, m.end(), b) if m and m.end() <= b else None


def check(root, verbose):
    bad = 0
    for d in folders(root):
        for p in cards(d):
            name, what, summary, kw, err = head(p)
            for e in err:
                print(f'{p}: {e}')
                bad += 1
            if verbose:
                body = open(p, encoding='utf-8').read().split('\n', 5)[-1].lower()
                for k in kw:
                    if re.search(r'\b' + re.escape(k.lower()) + r'\b', body):
                        print(f'{p}: keyword already in the text: {k}')
        r = readme(d)
        if not r:
            print(f'{d}/README.md: no table markers')
            bad += 1
        elif r[0][r[1]:r[2]].strip() != table(d):
            print(f'{d}/README.md: table is stale; run build')
            bad += 1
    print(bad, 'card problems')
    return bad


def build(root):
    for d in folders(root):
        r = readme(d)
        if not r:
            print(f'{d}/README.md: no table markers, skipped')
            continue
        t, a, b = r
        new = t[:a] + '\n' + table(d) + '\n' + t[b:]
        if new != t:
            open(os.path.join(d, 'README.md'), 'w', encoding='utf-8').write(new)
            print('rebuilt', d)


def find(root, words):
    words = [w.lower() for w in words]
    hits, body = [], []
    for d in folders(root):
        for p in cards(d):
            name, what, summary, kw, _ = head(p)
            h = ' '.join([name, what, summary] + kw).lower()
            if all(w in h for w in words):
                hits.append(f'{p}: {name}: {what}')
            elif all(w in open(p, encoding='utf-8').read().lower() for w in words):
                body.append(f'{p}: {name}: {what} (in the text)')
    print('\n'.join(hits + body) or 'no card')


def index(root, sheets):
    ent = {}

    def add(term, label, path):
        t = term.strip().strip('.').strip()
        if len(t) >= 3:
            ent.setdefault(t[0].upper() + t[1:], set()).add((label, path))

    for d in folders(root):
        for p in cards(d):
            name, what, summary, kw, _ = head(p)
            label = f'{name}: {what}' if what else name
            add(name, label, p)
            for k in kw:
                add(k, label, p)
            for part in re.split(r',|;| and | or ', what):
                part = re.sub(r'^\s*(the|a|an|its|their|his|her)\s+', '', part.strip())
                if 3 <= len(part) <= 40 and len(part.split()) <= 4:
                    add(part, label, p)
        r = os.path.join(d, 'README.md')
        if os.path.exists(r):
            t = open(r, encoding='utf-8').readline().lstrip('# ').strip()
            add(t.split(':')[0], t, r)
    for p in sorted(glob.glob(os.path.join(root, '*.md'))):
        if os.path.basename(p) not in ('README.md', 'INDEX.md'):
            t = open(p, encoding='utf-8').readline().lstrip('# ').strip()
            add(t.split(':')[0], t, p)
    if sheets and os.path.isdir(sheets):
        for p in sorted(glob.glob(os.path.join(sheets, '**', '*.md'), recursive=True)):
            if os.path.basename(p) != 'README.md':
                t = open(p, encoding='utf-8').readline().lstrip('# ').strip()
                add(t.split('(')[0].split(':')[0], t, p)
    key = lambda s: re.sub(r'^(the|a|an) ', '', s.lower())
    out = os.path.join(root, 'INDEX.md')
    lines = ['# Subject index', '',
             '*Every card by its name and its search words, every folder and every character sheet, A to Z. '
             f'Built by `{TOOL} index` from the card heads; never edit by hand (fix the card\'s head). '
             f'For a subject not here, `python3 {TOOL} find WORDS` searches the text.*']
    letter = None
    for term in sorted(ent, key=key):
        L = key(term)[:1].upper()
        if L != letter:
            letter = L
            lines += ['', f'## {L}', '']
        refs = '; '.join(f'[{lab}]({os.path.relpath(p, root)})' for lab, p in sorted(ent[term]))
        lines.append(f'- **{term}**: {refs}')
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f'{out}: {len(ent)} entries')


def main():
    ap = argparse.ArgumentParser(description='Card heads, folder indexes and search.',
                                 epilog='See the top of this file for the card head form.')
    ap.add_argument('command', choices=['check', 'build', 'find', 'index'], help='check the card heads and indexes; build the indexes; find cards by word; write the subject index')
    ap.add_argument('words', nargs='*', help='for find: the words to look for')
    ap.add_argument('--root', default='world', help='the folder whose subfolders are card folders (default: world)')
    ap.add_argument('--sheets', default='story/notes/characters', help='for index: the character sheets folder (default: story/notes/characters)')
    ap.add_argument('-v', action='store_true', help='for check: also list keywords the card text already uses')
    ap.add_argument('--mark', action='append', default=[], help='a status mark a name may end with, "(WORD)", left out of tables and index (repeatable)')
    ap.add_argument('--index', action='store_true', help='for build: also write the subject index')
    a = ap.parse_args()
    MARKS.extend(a.mark)
    if not os.path.isdir(a.root):
        sys.exit(f'no folder {a.root}')
    if a.command == 'check':
        sys.exit(1 if check(a.root, a.v) else 0)
    elif a.command == 'build':
        build(a.root)
        if a.index:
            index(a.root, a.sheets)
    elif a.command == 'index':
        index(a.root, a.sheets)
    else:
        find(a.root, a.words)


if __name__ == '__main__':
    main()
