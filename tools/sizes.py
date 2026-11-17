#!/usr/bin/env python3
"""What is too big to work with: the queue for distilling and paging.

Usage:
  python3 tools/sizes.py [--field 500] [--card 3000] [--file 8000] [--chapters N[,N...]] [--manifests DIR]

Lists fields over --field words (the distill answer test applies), cards and
sheets over --card words, and outline, design and notes files over --file words
(to page). With --manifests (the saved drafter manifests), each large field is
marked with the chapters whose bundles gave it, so the queue can be worked by
use: what the next chapters read first. --chapters limits that to those
chapters. Exit 0; it changes nothing.
"""
import argparse, glob, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cards as cardtool  # noqa: E402

CARDS = ['world/**/*.md', 'story/notes/characters/**/*.md']
FILES = ['story/outline/*.md', 'story/design/*.md', 'story/notes/*.md', 'story/volume/*.md']


def words(p):
    return len(open(p, encoding='utf-8').read().split())


def used(mdir, chapters):
    """{(card, field lower): [chapters]} from drafter manifests: fields given, or the card whole."""
    out = {}
    for m in sorted(glob.glob(os.path.join(mdir, '*drafter*.tsv'))):
        n = os.path.basename(m)[:5]
        if chapters and n not in chapters:
            continue
        for line in open(m, encoding='utf-8'):
            if line.startswith('#') or '\t' not in line:
                continue
            p, g = line.rstrip('\n').split('\t', 1)
            p = os.path.normpath(p)
            if g.startswith('fields:'):
                for f in g[7:].split(';'):
                    out.setdefault((p, f.strip().lower()), []).append(n)
            elif 'not given' not in g:
                out.setdefault((p, '*'), []).append(n)
    return out


def main():
    ap = argparse.ArgumentParser(description='What is too big to work with.')
    ap.add_argument('--field', type=int, default=500)
    ap.add_argument('--card', type=int, default=3000)
    ap.add_argument('--file', type=int, default=8000)
    ap.add_argument('--manifests')
    ap.add_argument('--chapters', default='')
    a = ap.parse_args()
    chapters = {c.strip() for c in a.chapters.split(',') if c.strip()}
    use = used(a.manifests, chapters) if a.manifests else {}
    cards = sorted({os.path.normpath(p) for g in CARDS for p in glob.glob(g, recursive=True)
                    if os.path.basename(p) not in ('README.md', 'INDEX.md')})
    fields, big = [], []
    for p in cards:
        if words(p) > a.card:
            big.append((words(p), p))
        try:
            fs = cardtool.fields(p)
        except Exception:
            continue
        for label, _, _, text in fs:
            n = len(text.split())
            if n > a.field:
                by = sorted(set(use.get((p, label.lower()), []) + use.get((p, '*'), [])))
                fields.append((bool(by), n, p, label, by))
    files = sorted(((words(p), p) for g in FILES for p in glob.glob(g) if os.path.basename(p) != 'README.md'
                    and words(p) > a.file), reverse=True)
    print(f'## Fields over {a.field} words: {len(fields)} (the distill answer test)\n')
    for has, n, p, label, by in sorted(fields, key=lambda x: (not x[0], -x[1])):
        print(f'- {n:5}  `{p}`, {label}' + (f'  (given to {", ".join(by)})' if by else ''))
    print(f'\n## Cards and sheets over {a.card} words: {len(big)}\n')
    for n, p in sorted(big, reverse=True):
        print(f'- {n:5}  `{p}`')
    print(f'\n## Files over {a.file} words: {len(files)} (to page)\n')
    for n, p in files:
        print(f'- {n:5}  `{p}`')
    return 0


if __name__ == '__main__':
    sys.exit(main())
