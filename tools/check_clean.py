#!/usr/bin/env python3
"""Check that a book cloned from the kit has nothing left of the kit's example.

A clone of the kit is the skeleton of a book. The toy novel in example/ is the
only thing deleted to start one. This check fails (exit 1) and lists each hit
when any of these is true:

  - example/ still exists;
  - a file outside .git/ holds a name from the example (its title, its people,
    its places, its chapter slugs);
  - a markdown link resolves into example/.

Otherwise it prints "clean" and exits 0.

Usage:
  python3 tools/check_clean.py [--root DIR]

  --root DIR   the book's top folder (default: the current folder)

The names are matched as whole words, case kept. This script itself is not
scanned, since it holds the list.
"""
import argparse, os, re, sys

# The example's names, hard-coded so the check still works once example/ is gone.
# To regenerate: read the title, every person, place and chapter slug in
# example/ (the people and places cards, the arc outline's chapter index, the
# file names under example/story/), and list each one here.
NAMES = [
    'The Tide Clock', 'Tide Clock',                        # the title
    'Wren', 'Ashby', 'Agnes', 'Rook', 'Dell',              # the people
    'Skerry Holm', 'Saltby',                               # the places
    'the-forty-minutes', 'caught-on-the-causeway',         # chapter slugs
    'spring-tides',                                        # the arc's slug
]

LINK = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
PATTERN = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(n) for n in NAMES) + r')(?![\w-])')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--root', default='.', help='the book\'s top folder (default: the current folder)')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    example = os.path.join(root, 'example')
    me = os.path.abspath(__file__)
    hits = []
    if os.path.exists(example):
        hits.append('example/ exists: delete it to start a book')
    for d, dirs, names in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x != '.git' and os.path.join(d, x) != example)
        for n in sorted(names):
            p = os.path.join(d, n)
            if os.path.abspath(p) == me:
                continue
            rel = os.path.relpath(p, root)
            try:
                text = open(p, encoding='utf-8').read()
            except (UnicodeDecodeError, OSError):
                continue                                   # not a text file
            for i, line in enumerate(text.splitlines(), 1):
                for m in PATTERN.finditer(line):
                    hits.append(f'{rel}:{i}  example name: {m.group(1)}')
                if n.endswith('.md'):
                    for m in LINK.finditer(line):
                        target = m.group(1).partition('#')[0]
                        if not target or re.match(r'^[a-z]+:', target):
                            continue
                        f = os.path.normpath(os.path.join(d, target))
                        if f == example or f.startswith(example + os.sep):
                            hits.append(f'{rel}:{i}  link into example/: {m.group(1)}')
    for h in hits:
        print(h)
    if hits:
        print(f'{len(hits)} hits: not clean')
        sys.exit(1)
    print('clean')


if __name__ == '__main__':
    main()
