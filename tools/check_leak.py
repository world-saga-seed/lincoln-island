#!/usr/bin/env python3
"""Check that a change meant for the kit carries nothing of your book.

An improvement found while writing a book (a better critic, a voice rule, a
cheaper step) is ported to a separate fork of the kit before it is offered
back. This check reads the lines the change adds, as a unified diff, and lists
each hit:

  - a name from your book: the heading of every card under world/ and of every
    character sheet under story/notes/characters/, matched as whole words,
    case kept;
  - a run of WORDS words or more (default 8) that also appears in your book's
    prose, outlines, notes, cards or existing/ manuscripts;
  - an email address.

A hit is not always a leak (a common word that is also a name, a stock
phrase); Claude reads each one with you. No hits prints "clean" and exits 0;
any hit exits 1.

Usage, from the fork's folder:
  git diff upstream/master | python3 tools/check_leak.py --book ../my-book
  python3 tools/check_leak.py --book ../my-book --diff change.diff [--words 8]
"""
import argparse, os, re, sys

TEXT = ('.md', '.txt')
SOURCES = ('story', 'world', 'existing')
SKIP_NAMES = {'The', 'A', 'An', 'Of', 'And', 'In', 'On', 'At', 'To', 'Index', 'README'}


def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def heading_names(head, person):
    """The proper names in a card's heading ("Name: what it is")."""
    found = set()
    name = head.split(':', 1)[0].strip()
    name = re.sub(r'^The\s+', '', name)
    if name[:1].isupper():
        found.add(name)
    toks = re.findall(r"[\w'-]+", head)
    for i, t in enumerate(toks):
        if t[:1].isupper() and len(t) > 2 and t not in SKIP_NAMES and (i > 0 or person):
            found.add(t)
    return {f for f in found if f and f not in SKIP_NAMES}


def book_names(book):
    names = set()
    dirs = [os.path.join(book, 'world'), os.path.join(book, 'story', 'notes', 'characters')]
    for d in dirs:
        for root, _, files in os.walk(d):
            for f in files:
                if not f.endswith('.md') or f in ('README.md', 'INDEX.md'):
                    continue
                for line in open(os.path.join(root, f), encoding='utf-8', errors='replace'):
                    if line.startswith('# '):
                        names.update(heading_names(line[2:].strip(), person='people' in root or 'characters' in root))
                        break
    return {n for n in names if n}


def book_runs(book, n):
    runs = set()
    for src in SOURCES:
        for root, _, files in os.walk(os.path.join(book, src)):
            for f in files:
                if f.endswith(TEXT):
                    w = words(open(os.path.join(root, f), encoding='utf-8', errors='replace').read())
                    runs.update(' '.join(w[i:i + n]) for i in range(len(w) - n + 1))
    return runs


def added_lines(diff):
    path, num = None, 0
    for line in diff:
        if line.startswith('+++ '):
            path = line[4:].strip().removeprefix('b/')
        elif line.startswith('@@'):
            m = re.search(r'\+(\d+)', line)
            num = int(m.group(1)) if m else 0
        elif line.startswith('+'):
            yield path, num, line[1:].rstrip('\n')
            num += 1
        elif not line.startswith('-'):
            num += 1


def main():
    ap = argparse.ArgumentParser(description='Check a change for the kit carries nothing of your book.')
    ap.add_argument('--book', required=True, help="your book's top folder")
    ap.add_argument('--diff', default='-', help='a unified diff (default: standard input)')
    ap.add_argument('--words', type=int, default=8, help='shortest shared run of words to flag (default 8)')
    a = ap.parse_args()

    names = book_names(a.book)
    pats = [(nm, re.compile(r'(?<![\w-])' + re.escape(nm) + r'(?![\w-])')) for nm in sorted(names, key=len, reverse=True)]
    runs = book_runs(a.book, a.words)
    email = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    diff = sys.stdin if a.diff == '-' else open(a.diff, encoding='utf-8', errors='replace')

    hits = 0
    for path, num, text in added_lines(diff):
        hit = [nm for nm, p in pats if p.search(text)]
        found = [f'name "{nm}"' for nm in hit if not any(nm != o and nm in o for o in hit)]
        w = words(text)
        shared = next((' '.join(w[i:i + a.words]) for i in range(len(w) - a.words + 1)
                       if ' '.join(w[i:i + a.words]) in runs), None)
        if shared:
            found.append(f'shared run "{shared}"')
        found += [f'email {e}' for e in email.findall(text) if not e.startswith('noreply@')]
        for f in found:
            print(f'{path}:{num}  {f}')
            hits += 1
    print('clean' if not hits else f'{hits} hits: read each before offering the change')
    sys.exit(1 if hits else 0)


if __name__ == '__main__':
    main()
