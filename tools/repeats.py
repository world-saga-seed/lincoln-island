#!/usr/bin/env python3
"""Phrases repeated across chapters, and stock patterns counted per chapter.

One chapter can be clean and a whole volume still read as wallpaper, because
the same small phrase turns up in chapter after chapter. This tool finds every
run of 5 to 8 words that appears in N or more files, and counts a set of stock
patterns ("tics") per file.

Usage:
  python3 tools/repeats.py FILE [FILE ...] [--min-files N] [--narration]
                           [--min-n 5] [--max-n 8] [--tics TICS] [--skip-title REGEX]

  FILE            chapters, in reading order (a shell glob is fine)
  --min-files N   report a phrase found in N or more files (default 3)
  --narration     drop text inside double quotes first
  --min-n/--max-n phrase length in words (default 5 to 8)
  --tics TICS     your own pattern list: one per line, "name<TAB>regex";
                  replaces the built-in list
  --skip-title RX skip a file whose first line matches RX
                  (for example '^# Interlude' for pieces in another voice)

Prints a markdown report: the pattern table (one column per file), then the
shared phrases with the files they are in. Sort the phrases yourself into
motifs (keep the words), habits (keep the gesture, vary the words) and tics (cut).
"""
import argparse, os, re
from collections import defaultdict

TICS = {
    '"the way you/a ..." simile': r'\bthe way (you|a|an|he|she|they|it|people|someone)\b',
    '"as if / as though"': r'\bas (if|though)\b',
    'gaze chain (looked at X, then at Y)': r'\blooked at [^.;]{1,40}, (and )?then at\b',
    'body part went/came': r'\b(eyes?|gaze|hands?|head|chin|shoulders?|mouth|face|fingers?|jaw)\s+(went|came)\b',
    '"for a moment" / "a long moment"': r'\b(for a moment|a long moment)\b',
    '"something shifted / changed"': r'\bsomething (shifted|changed)\b',
    '"I realized"': r'\bI realized\b',
    '"did not say anything" / "said nothing"': r'\b(did not say anything|said nothing)\b',
    'negation then correction ("not X. It was Y")': r'\b(was|is) not [^.]{1,40}\. (It|That|This) (was|is)\b',
    '"let out a breath" / "held my breath"': r'\b(let out a breath|held my breath|breath I did not know)\b',
}
STOP_ONLY = set('the a an and of to in on at it i he she was had her his my me you is that with for as not be but'.split())
QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”')


def text_of(p, narration):
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'^#.*$', '', t, flags=re.M)
    t = re.sub(r'^---$', '', t, flags=re.M)
    return QUOTED.sub(' ', t) if narration else t


def main():
    ap = argparse.ArgumentParser(description='Repeated phrases across chapters, and stock patterns per chapter.')
    ap.add_argument('files', nargs='+', help='chapter files, in reading order')
    ap.add_argument('--min-files', type=int, default=3, help='report a phrase found in at least this many files (default: 3)')
    ap.add_argument('--narration', action='store_true', help='narration only: set aside text inside double quotes')
    ap.add_argument('--min-n', type=int, default=5, help='shortest phrase, in words (default: 5)')
    ap.add_argument('--max-n', type=int, default=8, help='longest phrase, in words (default: 8)')
    ap.add_argument('--tics', help='file of stock patterns replacing the built-in list, one per line: name<TAB>regex')
    ap.add_argument('--skip-title', help="leave out files whose title matches this regex, e.g. '^# Interlude'")
    a = ap.parse_args()
    tics = TICS
    if a.tics:
        tics = {}
        for line in open(a.tics, encoding='utf-8'):
            if line.strip() and not line.startswith('#') and '\t' in line:
                name, rx = line.rstrip('\n').split('\t', 1)
                tics[name] = rx
    files = []
    for p in a.files:
        if a.skip_title and re.search(a.skip_title, open(p, encoding='utf-8').readline()):
            continue
        files.append(p)
    names = [os.path.splitext(os.path.basename(p))[0][:12] for p in files]
    texts = {p: text_of(p, a.narration) for p in files}
    print('# Repeats' + (' (narration only)' if a.narration else ''))
    print()
    print('## Patterns per file')
    print()
    print('| Pattern | ' + ' | '.join(names) + ' | All |')
    print('|---|' + '---|' * (len(files) + 1))
    for name, rx in tics.items():
        counts = [len(re.findall(rx, texts[p], re.I)) for p in files]
        print(f'| {name} | ' + ' | '.join(map(str, counts)) + f' | {sum(counts)} |')
    print()
    grams = defaultdict(set)
    for p, nm in zip(files, names):
        w = re.findall(r"[a-z']+", texts[p].lower())
        for n in range(a.min_n, a.max_n + 1):
            for i in range(len(w) - n + 1):
                g = tuple(w[i:i + n])
                if not all(x in STOP_ONLY for x in g):
                    grams[g].add(nm)
    hits = {g: fs for g, fs in grams.items() if len(fs) >= a.min_files}
    keep = []
    for g, fs in sorted(hits.items(), key=lambda x: -len(x[0])):
        s = ' '.join(g)
        if any(s in ' '.join(k) and fs <= kfs for k, kfs in keep):
            continue          # a shorter phrase inside a longer one with the same files
        keep.append((g, fs))
    keep.sort(key=lambda x: (-len(x[1]), -len(x[0])))
    print(f'## Phrases in {a.min_files} or more files')
    print()
    print('| Phrase | Files | Where |')
    print('|---|---|---|')
    for g, fs in keep:
        print(f'| {" ".join(g)} | {len(fs)} | {", ".join(sorted(fs))} |')
    if not keep:
        print('| (none) | 0 | |')


if __name__ == '__main__':
    main()
