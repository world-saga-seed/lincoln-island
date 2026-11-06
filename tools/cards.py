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

Usage:
  python3 tools/cards.py check [--root DIR] [-v]   exit 1 on a head out of form or a stale table;
                                                   -v also lists keywords the card's text already uses
  python3 tools/cards.py build [--root DIR]        rewrite every folder's table from the heads
  python3 tools/cards.py find WORD ... [--root DIR]  cards whose head holds every word,
                                                   then cards whose text does
  --root DIR defaults to "world".
"""
import argparse, glob, os, re, sys

BEGIN = '<!-- cards: built by tools/cards.py; do not edit -->'
END = '<!-- /cards -->'
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
    a, b = t.find(BEGIN), t.find(END)
    return (t, a + len(BEGIN), b) if 0 <= a < b else None


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


def main():
    ap = argparse.ArgumentParser(description='Card heads, folder indexes and search.',
                                 epilog='See the top of this file for the card head form.')
    ap.add_argument('command', choices=['check', 'build', 'find'], help='check the card heads and indexes; build the indexes; find cards by word')
    ap.add_argument('words', nargs='*', help='for find: the words to look for')
    ap.add_argument('--root', default='world', help='the folder whose subfolders are card folders (default: world)')
    ap.add_argument('-v', action='store_true', help='for check: also list keywords the card text already uses')
    a = ap.parse_args()
    if not os.path.isdir(a.root):
        sys.exit(f'no folder {a.root}')
    if a.command == 'check':
        sys.exit(1 if check(a.root, a.v) else 0)
    elif a.command == 'build':
        build(a.root)
    else:
        find(a.root, a.words)


if __name__ == '__main__':
    main()
