#!/usr/bin/env python3
"""Overlap: every run of N or more words a text shares with a reference text.

  python3 tools/overlap.py --ref REF [REF ...] --pub FILE [FILE ...] [--n 8] [--show 5]
                           [--between START END] [--tsv OUT]

For the clearance before release. Each --pub file is compared with the union of the --ref
files: a token of the published text is "covered" when it lies inside some run of N words
(after normalizing) that also occurs in a reference. Reports, per published file, the share
of its words covered, the number of maximal shared runs, and the longest runs (with --show).

Normalizing: lower case, curly quotes and dashes made plain, words kept, punctuation dropped,
so a shared run ignores quotes and commas but not word order or spelling.
--between START END keeps only the part of every reference between the first line containing
START and the first later line containing END (to drop a distributor's header and footer).
Markdown headings and the cards' "# Title (final)" line are read as text like any other line.

Overlap with a public-domain reference is not a problem in itself; it measures how much a text
leans on that reference. Against a copyrighted reference, every long run needs review.
Due diligence, not a legal opinion. Standard library only.
"""
import argparse, csv, os, re, sys

TRANS = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '—': ' ', '–': ' ', '-': ' '})


def words(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text.lower().translate(TRANS))


def read(path, between=None):
    text = open(path, encoding='utf-8', errors='replace').read()
    if between:
        start, end = between
        i = text.find(start)
        j = text.find(end, i + 1) if i >= 0 else -1
        if i >= 0:
            text = text[text.find('\n', i) + 1: j if j > 0 else None]
    return text


def grams(ws, n):
    return {hash(tuple(ws[i:i + n])) for i in range(len(ws) - n + 1)}


def runs(ws, ref, n):
    """Maximal runs [a, b) of tokens covered by shared n-grams."""
    out, a, b = [], None, None
    for i in range(len(ws) - n + 1):
        if hash(tuple(ws[i:i + n])) in ref:
            if a is not None and i <= b:
                b = i + n
            else:
                if a is not None:
                    out.append((a, b))
                a, b = i, i + n
    if a is not None:
        out.append((a, b))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ref', nargs='+', required=True)
    ap.add_argument('--pub', nargs='+', required=True)
    ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--show', type=int, default=0, help='list the longest runs per file')
    ap.add_argument('--between', nargs=2, metavar=('START', 'END'))
    ap.add_argument('--tsv', help='write one row per published file')
    a = ap.parse_args()
    ref = set()
    for r in a.ref:
        ref |= grams(words(read(r, a.between)), a.n)
    rows, tot_w, tot_c = [], 0, 0
    for p in a.pub:
        ws = words(read(p))
        rs = runs(ws, ref, a.n)
        cov = sum(b - a_ for a_, b in rs)
        longest = max((b - a_ for a_, b in rs), default=0)
        tot_w += len(ws); tot_c += cov
        rows.append([os.path.basename(p), len(ws), cov, f'{100 * cov / max(len(ws), 1):.1f}', len(rs), longest])
        print(f'{rows[-1][0]}\t{len(ws)} words\t{rows[-1][3]}% covered\t{len(rs)} runs\tlongest {longest}')
        for a_, b in sorted(rs, key=lambda r: r[0] - r[1])[:a.show]:
            print(f'    {b - a_:4d}  {" ".join(ws[a_:b])[:300]}')
    print(f'TOTAL\t{tot_w} words\t{100 * tot_c / max(tot_w, 1):.1f}% covered')
    if a.tsv:
        with open(a.tsv, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, delimiter='\t')
            w.writerow(['file', 'words', 'covered', 'pct', 'runs', 'longest'])
            w.writerows(rows)


if __name__ == '__main__':
    main()
