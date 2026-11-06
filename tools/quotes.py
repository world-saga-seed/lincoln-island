#!/usr/bin/env python3
"""Check that every quote in a report is really in the text it quotes.

Every finding a critic or reader makes must quote the text exactly. A quote
that is not in the text means the finding was invented or the text has since
changed; either way the finding is dropped before the writer sees it. This is
the one mechanical check that sits under every judgment in the method.

Usage:
  python3 tools/quotes.py REPORT --in FILE [FILE ...] [--backticks] [-v]

  REPORT       a findings file. Quotes are read from lines of the form
                 - quote: the exact words
                 quote: "the exact words"
               and, with --backticks, from every `backticked span` too
  --in FILE    the text the quotes must be found in (one or more files)
  --backticks  also check backticked spans (fold-back lists, card extracts)
  -v           list the quotes that resolve as well

Matching ignores differences in spacing, curly against straight quotes, and
markdown emphasis (* and _), so a quote copied from a rendered page still counts.
Prints the quotes that do not resolve and a count. Exits 1 if any do not, and
also when the report holds no quotes at all ("0 quotes found"): a report with
nothing to check is more likely in the wrong form than clean.
"""
import argparse, re, sys

QUOTE_LINE = re.compile(r'^\s*[-*]?\s*\**quote\**\s*:\s*(.+?)\s*$', re.I)
TICKS = re.compile(r'`([^`]{4,})`')


def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    s = s.replace('—', '--').replace('–', '-')
    s = re.sub(r'[*_]', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def strip_wrap(q):
    q = q.strip()
    for a, b in (('"', '"'), ('“', '”'), ('`', '`'), ("'", "'")):
        if len(q) > 2 and q.startswith(a) and q.endswith(b):
            return q[1:-1]
    return q


def main():
    ap = argparse.ArgumentParser(description='Check that report quotes resolve in the text.')
    ap.add_argument('report', help='the report whose quotes are checked (lines like "- quote: the exact words")')
    ap.add_argument('--in', dest='targets', nargs='+', required=True, help='the text file(s) the quotes must be found in')
    ap.add_argument('--backticks', action='store_true', help='also check every backticked span (run it on a file that holds only quotes in backticks)')
    ap.add_argument('-v', action='store_true', help='list every quote checked, not only the missing ones')
    a = ap.parse_args()
    text = norm(' '.join(open(f, encoding='utf-8').read() for f in a.targets))
    quotes = []
    for i, line in enumerate(open(a.report, encoding='utf-8'), 1):
        m = QUOTE_LINE.match(line)
        if m:
            quotes.append((i, strip_wrap(m.group(1))))
        elif a.backticks:
            quotes += [(i, q) for q in TICKS.findall(line)]
    if not quotes:
        print('0 quotes found')
        sys.exit(1)
    missing = 0
    for i, q in quotes:
        ok = norm(q) in text
        if not ok:
            missing += 1
            print(f'MISSING  {a.report}:{i}  {q[:90]}')
        elif a.v:
            print(f'ok       {a.report}:{i}  {q[:90]}')
    print(f'{len(quotes) - missing} of {len(quotes)} quotes resolve')
    sys.exit(1 if missing else 0)


if __name__ == '__main__':
    main()
