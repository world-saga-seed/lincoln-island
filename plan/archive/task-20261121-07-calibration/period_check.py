#!/usr/bin/env python3
"""List the words of a render found neither in White's translation (1876) nor anywhere in Webster's 1864 text.

Usage: python3 period_check.py RENDER.md [RENDER.md ...]

A word "found" is any token of the same letters, or of the same stem after one common English ending is taken off
(s, es, ed, d, ing, ly, er, est, ness, ment). Webster's OCR is rough on headwords (existing/webster-1864/SOURCE.md),
so a word counts as present if it appears anywhere in the text. A listed word is a flag for the period critic, not a
finding: it may be an OCR loss, a proper name, or a word White never needed.
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
WEB = os.path.join(ROOT, 'existing', 'webster-1864', 'americandictiona00websuoft_djvu.txt')
WHITE = sorted(glob.glob(os.path.join(ROOT, 'texts', 'white-1876', '[0-9][0-9].md')))
TOK = re.compile(r"[A-Za-z]+(?:['’][a-z]+)?")
ENDS = ('ness', 'ment', 'ing', 'est', 'es', 'ed', 'er', 'ly', 's', 'd')


def words(text):
    return [w.lower().replace('’', "'") for w in TOK.findall(text)]


def stems(w):
    out = {w}
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 3:
            b = w[: -len(e)]
            out |= {b, b + 'e'}
            if len(b) > 3 and b[-1] == b[-2]:
                out.add(b[:-1])
            if b.endswith('i'):
                out.add(b[:-1] + 'y')
    return out


def main(paths):
    known = set(words(open(WEB, encoding='utf-8', errors='replace').read()))
    for f in WHITE:
        known |= set(words(open(f, encoding='utf-8').read()))
    for p in paths:
        text = open(p, encoding='utf-8').read()
        body = '\n'.join(l for l in text.split('\n') if not l.startswith('#') and not re.match(r'^¶\d+$', l.strip()))
        miss = {}
        for w in words(body):
            if not (stems(w) & known):
                miss[w] = miss.get(w, 0) + 1
        print(f'## {os.path.basename(p)}: {len(miss)} words found in neither White nor Webster 1864')
        for w in sorted(miss):
            print(f'- {w}' + (f' ({miss[w]})' if miss[w] > 1 else ''))
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)
    main(sys.argv[1:])
