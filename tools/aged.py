#!/usr/bin/env python3
"""Outline beats, and note and card lines, that may carry an old draft into a redraft.

After a restructure, outlines still hold beats lifted from drafts written
before it, and proposals older than the rulings around them. A consistency check
reads outline against outline, so it cannot see them; a drafter given such an
outline blends the old book back in. This lists the lines to rule before a
redraft (plan/workflows/outline-clean.md).

Usage:
  python3 tools/aged.py FILE [FILE ...] [--cutoff YYYY-MM-DD] [--ledger DIR]
                        [--retired FILE ...] [--proposals] [--beats] [--cites-only] [--tsv OUT]

  FILE            outlines to scan, or (for the second round) notes and cards
  --cutoff DATE   a line whose newest date mark or ruling is older than this is
                  flagged "aged" (for example the date the current outline was
                  accepted); without it, no line is flagged for age
  --ledger DIR    the ledger folder, to date ruling IDs (default plan/settled/ledger)
  --retired FILE  drafts being replaced (for example story/prose/004*.md): any
                  line linking one (the link resolved from the file's folder), or
                  naming it with its folder as a locator ("prose/0410-x.md:12"),
                  is flagged "cites-retired". Kept drafts are simply not listed
  --proposals     also flag every *(Proposal.)* with no date or ruling on its
                  line: before a full redraft each open proposal is ruled too
  --beats         read only list items (lines starting "- " or "1. "): an
                  outline's beats, not its headers and prose
  --cites-only    flag only "cites-retired": the second round, over notes and
                  cards, where "from the draft" is history and not a beat
  --tsv OUT       also write one row per flagged line: file, line, reasons, text

A line is flagged when it says it is drawn "from the draft", links a retired
draft, or is older than the cutoff (and, with --proposals, any undated proposal).
Prints per file the lines read, the lines flagged and the count of each reason.
"""
import argparse, glob, os, re
from collections import Counter

DATE = re.compile(r'\b(\d{4})-(\d\d)-(\d\d)\b')
RID = re.compile(r'\b[A-Z](\d{4})-\d+(?:-\d+)?\b')


def ledger_dates(d):
    """ruling ID -> its ledger day, from rows whose first cell is the ID."""
    out = {}
    for p in glob.glob(os.path.join(d, '*.md')):
        m = DATE.search(os.path.basename(p))
        if not m:
            continue
        for line in open(p, encoding='utf-8'):
            c = re.match(r'\|\s*([A-Z]\d{4}-\d+(?:-\d+)?)\s*\|', line)
            if c:
                out[c.group(1)] = '-'.join(m.groups())
    return out


def main():
    ap = argparse.ArgumentParser(description='Lines that may carry an old draft into a redraft.')
    ap.add_argument('files', nargs='+')
    ap.add_argument('--cutoff')
    ap.add_argument('--ledger', default='plan/settled/ledger')
    ap.add_argument('--retired', nargs='*', default=[])
    ap.add_argument('--proposals', action='store_true')
    ap.add_argument('--beats', action='store_true')
    ap.add_argument('--cites-only', action='store_true')
    ap.add_argument('--tsv')
    a = ap.parse_args()
    dates = ledger_dates(a.ledger)
    retired = {os.path.normpath(r) for r in a.retired}
    named = {os.path.basename(os.path.dirname(r)) + '/' + os.path.basename(r) for r in retired}
    link = re.compile(r'\]\(([^)#\s]+)')
    rows, total = [], Counter()
    for f in a.files:
        n, why_n = 0, Counter()
        for i, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            if not line.strip() or line.startswith('#'):
                continue
            if a.beats and not re.match(r'\s*(- |\d+\. )', line):
                continue
            n += 1
            why = []
            if re.search(r'\bfrom the drafts?\b', line, re.I):
                why.append('from-draft')
            if (any(os.path.normpath(os.path.join(os.path.dirname(f), t)) in retired for t in link.findall(line))
                    or any(n in line for n in named)):
                why.append('cites-retired')
            marks = ['-'.join(m) for m in DATE.findall(line)]
            marks += [dates[m.group(0)] for m in RID.finditer(line) if m.group(0) in dates]
            if a.cutoff and marks and max(marks) < a.cutoff:
                why.append('aged')
            if a.proposals and '*(Proposal.)*' in line and not DATE.search(line) and not RID.search(line):
                why.append('undated-proposal')
            if a.cites_only:
                why = [w for w in why if w == 'cites-retired']
            if why:
                why_n.update(why)
                rows.append((f, i, ','.join(why), line.strip()))
        total.update(why_n)
        if why_n:
            print(f"{f}: {n} lines, {sum(1 for r in rows if r[0] == f)} flagged ("
                  + ', '.join(f'{k} {v}' for k, v in sorted(why_n.items())) + ')')
    print(f"\n{len(rows)} lines flagged in {len(a.files)} files"
          + (': ' + ', '.join(f'{k} {v}' for k, v in sorted(total.items())) if total else ''))
    if a.tsv:
        with open(a.tsv, 'w', encoding='utf-8') as out:
            for r in rows:
                out.write('\t'.join(map(str, r)) + '\n')


if __name__ == '__main__':
    main()
