#!/usr/bin/env python3
"""A volume's refrains counted, and descriptions repeated near word for word.

A refrain is a detail the book comes back to: a dog's torn ear, a
character's cough, a gesture at the door. Each showing reads well in its own
chapter; across a volume the reader meets the full picture again and again and
feels it as padding. A batch critic sees two or three chapters and cannot count
the whole volume, so this script does it for them.

Usage:
  python3 tools/refrains.py FILE [FILE ...] --list REFRAINS [--batch K]
                            [--volume-max 8] [--chapter-max 3] [--stop REGEX]

  FILE            the volume's chapters so far, in reading order
  --list REFRAINS the watch list: one refrain per line, "label<TAB>regex",
                  case ignored; "#" starts a comment. Add every refrain a critic
                  or reader names, so the next count catches it for free.
  --batch K       the last K files are the batch under review: near-verbatim
                  runs are reported only when one of them is in the batch
                  (default: every file is the batch)
  --volume-max N  flag a refrain shown more than N times in the volume (default 8)
  --chapter-max N flag a chapter showing a refrain more than N times (default 3)
  --stop REGEX    stop reading a file at a line matching REGEX (default "^## Notes")

Prints a markdown report: the watch list counted per chapter with its flags,
then every six-word run shared nearly word for word by three chapters or more
(runs made mostly of small words are skipped; overlapping runs are folded into
one longer run). Give it to the habits critic: a refrain keeps its full showing
the first time, at a farewell, or where it changes something, and is cut to a
gesture or a word between.
"""
import argparse, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import context  # noqa: E402  (the shared reader and pattern matcher)

FUNC = set('''the a an of to in on at by for and or but as i my me he his she her it its
we our they them was were had is be that this with from up down out over under
far side end back edge one'''.split())


def body(path, stop):
    """The chapter's text, paragraph by paragraph, through context's reader."""
    paras, _, _ = context.units(path, stop)
    return '\n'.join(t for _, t in paras)


def norm(s):
    return ' '.join(re.findall(r"[a-z']+", s.lower()))


def shingles(s, k=6):
    w = s.split()
    return {' '.join(w[i:i + k]) for i in range(len(w) - k + 1)}


def main():
    ap = argparse.ArgumentParser(description="A volume's refrains counted, and near-verbatim descriptions found.")
    ap.add_argument('files', nargs='+', help="the volume's chapters, in reading order")
    ap.add_argument('--list', required=True, help='watch list: one "label<TAB>regex" per line')
    ap.add_argument('--batch', type=int, default=0, help='the last K files are the batch (default: all)')
    ap.add_argument('--volume-max', type=int, default=8)
    ap.add_argument('--chapter-max', type=int, default=3)
    ap.add_argument('--stop', default=r'^## Notes')
    a = ap.parse_args()

    specs = []
    for line in open(a.list, encoding='utf-8'):
        if line.strip() and not line.startswith('#'):
            label, rx = line.rstrip('\n').split('\t', 1)
            specs.append({'label': label, 'rx': rx})
    pats = context.compile_patterns(specs)
    chaps = [(os.path.basename(f)[:-3], body(f, a.stop)) for f in a.files]
    counts = {}  # (chapter, label) -> matches, from context.find
    for f, (c, _) in zip(a.files, chaps):
        for h in context.find(f, pats, a.stop, merge_sentences=False)[2]:
            counts[(c, h['label'])] = counts.get((c, h['label']), 0) + 1
    batch = {c for c, _ in chaps[-a.batch:]} if a.batch else {c for c, _ in chaps}

    print(f'# Refrains, {chaps[0][0]} to {chaps[-1][0]}\n')
    print('| Refrain | Volume | Per chapter | Flag |\n|---|---|---|---|')
    for d in pats:
        label = d['label']
        per = [(c, counts.get((c, label), 0)) for c, _ in chaps]
        tot = sum(k for _, k in per)
        if not tot:
            continue
        flag = ([f'over {a.volume_max} in the volume'] if tot > a.volume_max else [])
        flag += [f'{c}: {k}' for c, k in per if k > a.chapter_max]
        cells = ', '.join(f'{c} {k}' for c, k in per if k)
        print(f"| {label} | {tot} | {cells} | {'; '.join(flag)} |")

    index = defaultdict(set)
    sents = []
    for c, t in chaps:
        for s in re.split(r'(?<=[.!?"”])\s+', t):
            w = norm(s).split()
            if len(w) >= 8:
                sents.append((c, w))
                for i in range(len(w) - 5):
                    index[' '.join(w[i:i + 6])].add(c)
    flagged = {g: cs for g, cs in index.items()
               if len(cs) >= 3 and cs & batch and sum(x in FUNC for x in g.split()) < 4}
    # Each sentence in the batch: its flagged six-word runs joined where they overlap.
    runs = {}
    for c, w in sents:
        if c not in batch:
            continue
        i = 0
        while i < len(w) - 5:
            g = ' '.join(w[i:i + 6])
            if g not in flagged:
                i += 1
                continue
            j, cs = i, set(flagged[g])
            while j + 1 < len(w) - 5 and ' '.join(w[j + 1:j + 7]) in flagged:
                j += 1
                cs &= flagged[' '.join(w[j:j + 6])]
            run = ' '.join(w[i:j + 6])
            if not any(run in r for r in runs):
                runs = {r: v for r, v in runs.items() if r not in run}
                runs[run] = cs
            i = j + 6
    print('\n## Near-verbatim in three chapters or more (a six-word run shared)\n')
    for g, cs in sorted(runs.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f'- "{g}": {", ".join(sorted(cs))}')
    if not runs:
        print('None.')


if __name__ == '__main__':
    main()
