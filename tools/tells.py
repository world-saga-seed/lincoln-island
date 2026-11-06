#!/usr/bin/env python3
"""Texture numbers for drafted chapters, and a scan for banned words.

Model-written prose gives itself away by rhythm more than by vocabulary: the
same simile frame, long "and" chains, paragraphs that end on a short kicker,
too many negations. This tool measures those on the narration (text outside
double quotes), so a chapter can be set beside the writer's own samples.

Usage:
  python3 tools/tells.py FILE [FILE ...] [--banned LIST] [--stop REGEX] [--all-text]

  FILE          markdown chapters; headings (# lines) are ignored
  --banned LIST a word list: one word or phrase per line, matched as whole
                words, case ignored; a line starting "re:" is a regular
                expression; lines starting "#" are comments
  --stop REGEX  ignore everything from the first line matching REGEX
                (default "^## Notes", so notes kept under a draft are skipped)
  --all-text    scan dialogue too when looking for banned words
                (by default only narration is scanned)

Per file it prints one line of numbers:
  w            narration words
  way/k        "the way you / the way a ..." similes per 1,000 words
  asif/k       "as if / as though" per 1,000 words
  and/s        "and" per sentence
  neg/k        negations (not, no, nothing, never, nobody, none) per 1,000 words
  med, sd      median and spread of sentence length in words
  short%       sentences of 6 words or fewer;  long%  sentences of 25 or more
  button%      paragraphs of two sentences or more that end on one of 5 words or fewer
Then any banned-word hits as  file:line  word  | the line.
Read the numbers against the same numbers for the writer's own pages; there is
no universal good value.
"""
import argparse, re, sys

QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”')


def load_banned(path):
    rx = []
    for line in open(path, encoding='utf-8'):
        t = line.strip()
        if not t or t.startswith('#'):
            continue
        if t.startswith('re:'):
            rx.append((t, re.compile(t[3:].strip(), re.I)))
        else:
            rx.append((t, re.compile(r'\b' + re.escape(t) + r'\b', re.I)))
    return rx


def body_lines(path, stop):
    out = []
    for line in open(path, encoding='utf-8').read().split('\n'):
        if stop and re.search(stop, line):
            break
        out.append(line)
    return out


def numbers(lines):
    text = '\n'.join('' if l.startswith('#') else l for l in lines)
    narr = QUOTED.sub('', text)
    words = narr.split()
    w = max(1, len(words))
    sents = [s for s in re.split(r'[.!?]+(?:\s|$)', narr) if s.strip()]
    lens = sorted(len(s.split()) for s in sents) or [0]
    mean = sum(lens) / len(lens)
    sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** .5
    paras = [QUOTED.sub('', p) for p in text.split('\n\n') if p.strip() and not p.lstrip().startswith(('"', '“'))]
    multi = [[s for s in re.split(r'(?<=[.!?])\s+', p.strip()) if s.split()] for p in paras]
    multi = [s for s in multi if len(s) >= 2]
    c = lambda rx: len(re.findall(rx, narr, re.I))
    return {
        'w': len(words),
        'way/k': 1000 * c(r'\bthe way (you|a|an|he|she|they|it|people|somebody|someone)\b') / w,
        'asif/k': 1000 * c(r'\bas (if|though)\b') / w,
        'and/s': c(r'\band\b') / max(1, len(sents)),
        'neg/k': 1000 * c(r'\b(not|no|nothing|never|nobody|none)\b') / w,
        'med': lens[len(lens) // 2],
        'sd': sd,
        'short%': 100 * sum(x <= 6 for x in lens) / len(lens),
        'long%': 100 * sum(x >= 25 for x in lens) / len(lens),
        'button%': 100 * sum(len(s[-1].split()) <= 5 for s in multi) / max(1, len(multi)),
    }


def main():
    ap = argparse.ArgumentParser(description='Texture numbers and banned-word scan for chapters.')
    ap.add_argument('files', nargs='+', help='chapter files to measure')
    ap.add_argument('--banned', help='banned list: one word or phrase per line; re: starts a regex; # a comment')
    ap.add_argument('--stop', default=r'^## Notes', help='stop reading a file at a line matching this regex (default: ^## Notes)')
    ap.add_argument('--all-text', action='store_true', help='scan dialogue for banned words too')
    a = ap.parse_args()
    banned = load_banned(a.banned) if a.banned else []
    hits = []
    for f in a.files:
        lines = body_lines(f, a.stop)
        n = numbers(lines)
        name = f.replace('\\', '/').split('/')[-1][:30]
        print(f"{name:30} w={n['w']:5} way/k={n['way/k']:4.1f} asif/k={n['asif/k']:4.1f} "
              f"and/s={n['and/s']:.2f} neg/k={n['neg/k']:4.1f} med={n['med']:2} sd={n['sd']:4.1f} "
              f"short%={n['short%']:3.0f} long%={n['long%']:3.0f} button%={n['button%']:3.0f}")
        for i, line in enumerate(lines, 1):
            if line.startswith('#'):
                continue
            scan = line if a.all_text else QUOTED.sub(' ', line)
            for label, rx in banned:
                for m in rx.finditer(scan):
                    hits.append(f'{f}:{i}  {m.group(0)}  | {line.strip()[:100]}')
    if banned:
        print(f'\n{len(hits)} banned-word hits' + (':' if hits else ''))
        for h in hits:
            print(h)


if __name__ == '__main__':
    main()
