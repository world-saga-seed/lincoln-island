#!/usr/bin/env python3
"""Setting words on the page for the first time: candidates for the setup critic.

A drafter reads the cards; the reader has only the pages. A word the cards use
freely (a tool, a part, a step of a trade) can reach the page with nothing on
the page to set it up, and the sentence makes sense only to someone who has
read the cards ("he reset the pawls", with no winch shown before).

Usage:
  python3 tools/firstuse.py FILE [FILE ...] [--batch K] [--cards DIR]
                            [--min-cards 3] [--stop REGEX]

  FILE            the book's chapters so far, in reading order
  --batch K       report only the last K files (default: all)
  --cards DIR     the card folder whose words count as the setting's (default world)
  --min-cards N   a word is the setting's when N or more cards use it (default 3)
  --stop REGEX    stop reading a file at a line matching REGEX (default "^## Notes")

For each chapter in the batch, lists the words of four letters or more (a plural
folded to its singular) that no earlier chapter uses and that N or more cards use,
with the first line holding each. Most are plain words; the setup critic judges
each one that names a thing, a tool or a step: plain from context, set up on the
page, or needing a line.
"""
import argparse, glob, os, re
from collections import Counter

STOP = set('''that this with from they them then there their what when where which while
have were been into upon over under about after before would could should said
only once more most some such than very just like your yours mine ours here back
down even ever every much many each other another again away also because'''.split())


def words(t):
    for w in re.findall(r"[a-z][a-z'-]{3,}", t.lower()):
        w = re.sub(r"'s$", '', w).strip("'-")
        if len(w) < 4 or w in STOP:
            continue
        yield w[:-1] if w.endswith('s') and not w.endswith('ss') else w


def body(path, stop):
    out = []
    for line in open(path, encoding='utf-8').read().split('\n'):
        if stop and re.search(stop, line):
            break
        out.append('' if line.startswith('#') else line)
    return out


def main():
    ap = argparse.ArgumentParser(description='Setting words on the page for the first time.')
    ap.add_argument('files', nargs='+', help='the chapters so far, in reading order')
    ap.add_argument('--batch', type=int, default=0)
    ap.add_argument('--cards', default='world')
    ap.add_argument('--min-cards', type=int, default=3)
    ap.add_argument('--stop', default=r'^## Notes')
    a = ap.parse_args()
    lore = Counter()
    for p in glob.glob(os.path.join(a.cards, '**', '*.md'), recursive=True):
        lore.update(set(words(open(p, encoding='utf-8').read())))
    batch = set(a.files[-(a.batch or len(a.files)):])
    seen = set()
    for f in a.files:
        lines = body(f, a.stop)
        if f in batch:
            new = {}
            for i, line in enumerate(lines, 1):
                for w in words(line):
                    if w not in seen and w not in new and lore[w] >= a.min_cards:
                        new[w] = (i, line.strip())
            if new:
                print(f'## {os.path.basename(f)}\n')
                for w, (i, line) in new.items():
                    m = re.search(re.escape(w), line, re.I)
                    s = max(0, m.start() - 60) if m else 0
                    print(f'- **{w}** ({lore[w]} cards), line {i}: …{line[s:s + 140]}…')
                print()
        seen.update(w for line in lines for w in words(line))


if __name__ == '__main__':
    main()
