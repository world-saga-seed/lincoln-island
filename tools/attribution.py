#!/usr/bin/env python3
"""Unlabeled paragraphs for a blind attribution test, and the key to score it.

In a book with two or more viewpoint heads, drafters copy each other's voices
and a fix can flatten one head into another. A cold reader given paragraphs with
their labels removed, asked whose head each is in, finds the bleed by voice
alone (plan/workflows/drafting/prompts/attribution.md).

Usage:
  python3 tools/attribution.py FILE [FILE ...] --heads SPEC --out TEST --key KEY
                               [--count 15] [--min-words 40] [--seed N] [--stop REGEX]

  FILE          the chapters, in order
  --heads SPEC  whose head each stretch is in: "FILE:FIRST-LAST=Name" items
                separated by commas, lines inclusive (e.g. "a.md:1-40=Ada,a.md:41-200=Ben");
                a file with one head throughout: "b.md=Ben"
  --out TEST    the file to give the reader: paragraphs headed "## P1", "## P2"...
  --key KEY     the file to keep: each P's file, line and head (never give it to the reader)
  --count N     how many paragraphs (default 15), at least five from each head when it has them
  --min-words N skip paragraphs shorter than this (default 40)
  --seed N      shuffle seed, for a test you can rebuild (default 7)
  --stop REGEX  stop reading a file at a line matching REGEX (default "^## Notes")
"""
import argparse, os, random, re


def main():
    ap = argparse.ArgumentParser(description='Unlabeled paragraphs for a blind attribution test.')
    ap.add_argument('files', nargs='+')
    ap.add_argument('--heads', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--key', required=True)
    ap.add_argument('--count', type=int, default=15)
    ap.add_argument('--min-words', type=int, default=40)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--stop', default=r'^## Notes')
    a = ap.parse_args()

    spans = []
    for item in a.heads.split(','):
        where, name = item.rsplit('=', 1)
        m = re.match(r'(.+):(\d+)-(\d+)$', where)
        f, lo, hi = (m.group(1), int(m.group(2)), int(m.group(3))) if m else (where, 1, 10 ** 9)
        spans.append((os.path.basename(f), lo, hi, name.strip()))

    def head(f, i):
        for sf, lo, hi, name in spans:
            if sf == os.path.basename(f) and lo <= i <= hi:
                return name
        return None

    paras = {}
    for f in a.files:
        for i, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            if a.stop and re.search(a.stop, line):
                break
            h = head(f, i)
            if h and not line.startswith('#') and len(line.split()) >= a.min_words:
                paras.setdefault(h, []).append((f, i, line.strip()))
    rnd = random.Random(a.seed)
    for h in paras:
        rnd.shuffle(paras[h])
    pick = []
    for h in paras:
        pick += paras[h][:5]
    rest = [p for h in paras for p in paras[h][5:]]
    rnd.shuffle(rest)
    pick += rest[:max(0, a.count - len(pick))]
    rnd.shuffle(pick)
    with open(a.out, 'w', encoding='utf-8') as out, open(a.key, 'w', encoding='utf-8') as key:
        out.write('# Unlabeled paragraphs\n\n')
        key.write('# Attribution key\n\n')
        for k, (f, i, text) in enumerate(pick, 1):
            out.write(f'## P{k}\n\n{text}\n\n')
            key.write(f'- P{k}: {os.path.basename(f)}:{i}, {head(f, i)}\n')
    counts = {h: sum(1 for f, i, _ in pick if head(f, i) == h) for h in paras}
    print(f'{len(pick)} paragraphs: ' + ', '.join(f'{h} {n}' for h, n in counts.items()))


if __name__ == '__main__':
    main()
