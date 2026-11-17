#!/usr/bin/env python3
"""Stutters: the same short phrase twice within a few paragraphs of one chapter.

A chapter can pass every per-chapter cap and still stutter: the same three or
four words come back a paragraph later ("on either side ... and none of it"
twice in one crossing). No critic's question covers it, because each critic
reads for one dimension and a close echo reads fine for sense. This tool finds
the candidates; you, or the reviser, judge them.

Usage:
  python3 tools/stutters.py FILE [FILE ...] [--window W] [--standing N]
                            [--clues FILE ...] [--stop HEADING] [--summary]

  FILE          chapters (a shell glob is fine)
  --window W    the most words between the two uses (default 250)
  --standing N  a run used N times or more in a chapter is a name, a tag or a
                motif, listed apart and not as hits (default 6)
  --clues FILE  files holding your clue register or a chapter's planted lines;
                a hit whose words are in one is marked "clue?" (repeatable)
  --stop H      stop reading a file at a line starting H (default "## Notes")
  --summary     one line per chapter, no hits

Per chapter it prints:
  - every run used again within W words, merged to the longest shared run,
    with both line numbers: a run of three words needs two that are not
    filler, a longer run one, and a run of four or more all filler
    ("as if he were") counts within 100 words;
  - the capped frames ("as if"/"as though", "the way X") used twice in one
    paragraph, and the chapter's count against its cap (4 and 5);
  - the standing phrases.

Judge each hit: a clue or a motif keeps its words; a callback, a refrain or a
line echoed back in dialogue is deliberate; the rest are reworded at the
later use. Rerun after the fix: a rewording can make a new stutter nearby.
"""
import argparse, os, re
from collections import defaultdict

FILLER = set('''a an the and or but nor so yet of to in on at by for from with into onto out up down off over
under about as than then that this these those it its it's is was were be been being am are had has have do did
does done not no i me my mine you your he him his she her they them their we us our one there here what which who
when where while if all some any each every more most very too just only also even still again back
said says say'''.split())
WORD = re.compile(r"[A-Za-z][A-Za-z'’]*")
FRAMES = {
    '"as if" / "as though"': (re.compile(r'\bas (if|though)\b', re.I), 4),
    '"the way X"': (re.compile(r'\bthe way (you|a|an|he|she|they|it|i|people|someone|somebody|my|his|her)\b', re.I), 5),
}


def lines_of(path, stop):
    out = []
    for i, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if stop and line.startswith(stop):
            break
        if line.startswith('#') or line.strip() == '---' or not line.strip():
            continue
        out.append((i, line))
    return out


def scan(path, a, clues):
    words, para_frames, counts = [], [], defaultdict(int)
    for ln, text in lines_of(path, a.stop):
        for w in WORD.findall(text):
            words.append((w.lower().replace('’', "'"), ln))
        for name, (rx, cap) in FRAMES.items():
            k = len(rx.findall(text))
            counts[name] += k
            if k >= 2:
                para_frames.append((ln, name, k))
    last_seen, hits = defaultdict(list), {}
    for i in range(len(words) - 2):
        g = tuple(w for w, _ in words[i:i + 3])
        for j in last_seen[g]:
            if i - j < 3 or i - j > a.window or (j - 1, i - 1) in hits and hits[(j - 1, i - 1)] > 3:
                continue
            n = 3
            while i + n < len(words) and j + n < i and words[j + n][0] == words[i + n][0]:
                n += 1
            hits[(j, i)] = n
        last_seen[g] = [j for j in last_seen[g] if i - j <= a.window] + [i]
    hits = {k: n for k, n in hits.items() if not any(
        (p, q) != k and q - p == k[1] - k[0] and p <= k[0] and k[0] + n <= p + m for (p, q), m in hits.items())}
    text = ' ' + ' '.join(w for w, _ in words) + ' '
    standing, found = set(), []
    for (j, i), n in sorted(hits.items()):
        run = [w for w, _ in words[i:i + n]]
        content = sum(w not in FILLER for w in run)
        if not (content >= 2 or (n >= 4 and content >= 1) or (n >= 4 and i - j <= 100)):
            continue
        phrase = ' '.join(run)
        if text.count(' ' + phrase + ' ') >= a.standing:
            standing.add(phrase)
            continue
        found.append((words[j][1], words[i][1], i - j, phrase, ' **clue?**' if phrase in clues else ''))
    over = [(name, counts[name], cap) for name, (rx, cap) in FRAMES.items() if counts[name] > cap]
    return found, para_frames, over, sorted(standing)


def main():
    ap = argparse.ArgumentParser(description='Short phrases repeated within a few paragraphs of one chapter.')
    ap.add_argument('files', nargs='+')
    ap.add_argument('--window', type=int, default=250)
    ap.add_argument('--standing', type=int, default=6)
    ap.add_argument('--clues', action='append', default=[])
    ap.add_argument('--stop', default='## Notes')
    ap.add_argument('--summary', action='store_true')
    a = ap.parse_args()
    clues = ' '.join(open(c, encoding='utf-8').read().lower() for c in a.clues)
    total = 0
    print(f'# Stutters, window {a.window} words, {len(a.files)} files\n')
    if a.summary:
        print('| File | Hits | Frames twice in a paragraph | Over cap |\n|---|---|---|---|')
    for path in a.files:
        found, para_frames, over, standing = scan(path, a, clues)
        total += len(found)
        name = os.path.basename(path)
        if a.summary:
            oc = '; '.join(f'{n} {c}/{cap}' for n, c, cap in over)
            print(f'| {name} | {len(found)} | {len(para_frames)} | {oc} |')
            continue
        print(f'## {name}: {len(found)} hits\n')
        for n, c, cap in over:
            print(f'- **Over cap:** {n} {c} (cap {cap})')
        for ln, n, k in para_frames:
            print(f'- **Twice in a paragraph:** {n} x{k} at line {ln}')
        if standing:
            print(f'- Standing phrases (not hits): {", ".join(standing)}')
        if found:
            print('\n| Lines | Gap (words) | Phrase |\n|---|---|---|')
            for p, q, gap, phrase, mark in found:
                print(f'| {p}, {q} | {gap} | {phrase}{mark} |')
        print()
    print(f'\n**Total:** {total} hits.')


if __name__ == '__main__':
    main()
