#!/usr/bin/env python3
"""Align White's paragraphs to the French paragraphs, chapter by chapter (phase 3).

A monotone dynamic-programming alignment, in the manner of Gale and Church, over
beads of French and White paragraphs: 1-1, n-1 and 1-n up to 5, and 1-0 or 0-1
(a French paragraph White leaves out, or a White paragraph with no French).
A bead's cost is the length mismatch (characters, against the chapter's own
English/French ratio) less a bonus for shared anchors: numbers written in
figures, and proper names, with White's spellings mapped (Herbert = Harbert,
Neb = Nab, Gideon = Gédéon) and number words in both languages up to twenty.

The summary ¶0 is aligned to White's ¶0; notes, plates and loose lines are not
aligned (White has no plates). The output is a starting point for the labeller,
not a finding: a bead it gets wrong is corrected by whoever reads the chapter.

Usage: python3 texts/align_white.py NN [NN ...]   (writes texts/align/NN.tsv)
       python3 texts/align_white.py all
Columns: fr (¶ range or -), white (¶ range or -), kind (1-1, 2-1, ..., cut?, add?; "short?" where White
         is under 0.6 of the French by the chapter's ratio, "long?" over 1.6, for beads over 150 characters),
         cost, fr_chars, white_chars.
"""
import math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARA = re.compile(r'^¶(\d+)(?: \[p\.\d+\])? (.*)$')

NAMES = {  # French form -> shared key; White's forms map to the same key
    'cyrus': 'cyrus', 'smith': 'smith', 'pencroff': 'pencroff', 'harbert': 'harbert', 'herbert': 'harbert',
    'nab': 'nab', 'neb': 'nab', 'gédéon': 'gedeon', 'gideon': 'gedeon', 'spilett': 'spilett', 'top': 'top',
    'jup': 'jup', 'jupiter': 'jup', 'ayrton': 'ayrton', 'nemo': 'nemo', 'nautilus': 'nautilus',
    'tabor': 'tabor', 'lincoln': 'lincoln', 'grant': 'grant', 'franklin': 'franklin', 'mercy': 'mercy',
    'richmond': 'richmond', 'washington': 'washington', 'duncan': 'duncan', 'speedy': 'speedy',
    'bonadventure': 'bonadventure', 'glenarvan': 'glenarvan', 'forster': 'forster', 'grant': 'grant',
    'granite': 'granite', 'pacifique': 'pacific', 'pacific': 'pacific', 'amérique': 'america', 'america': 'america',
    'harvey': 'harvey', 'joyce': 'joyce', 'britannia': 'britannia', 'dakkar': 'dakkar', 'tasmanie': 'tasmania',
    'tasmania': 'tasmania', 'zélande': 'zealand', 'zealand': 'zealand', 'australie': 'australia', 'australia': 'australia',
}
NUMS = {
    'un': 1, 'une': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7, 'huit': 8, 'neuf': 9,
    'dix': 10, 'onze': 11, 'douze': 12, 'quinze': 15, 'vingt': 20, 'cent': 100, 'cents': 100, 'mille': 1000,
    'two': 2, 'three': 3, 'four': 4, 'five': 5, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'fifteen': 15, 'twenty': 20, 'hundred': 100, 'thousand': 1000,
}  # "one"/"six" are left out on the English side where ambiguous; "six" is shared by both


def paras(path):
    out = {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('## '):          # notes, plates and loose lines follow; not aligned
            break
        m = PARA.match(ln.rstrip('\n'))
        if m:
            if m.group(2).strip() == 'THE END.':   # White III.20: the glossary that follows is the edition's, not aligned
                break
            out[int(m.group(1))] = m.group(2)
    return out


def anchors(text):
    toks = re.findall(r"[A-Za-zÀ-ÿ]+|\d+", text.lower())
    a = set()
    for t in toks:
        if t.isdigit():
            a.add('n' + t)
        elif t in NAMES:
            a.add(NAMES[t])
        elif t in NUMS:
            a.add('w%d' % NUMS[t])
    if '?' in text:
        a.add('?')
    if '!' in text:
        a.add('!')
    return a


def align(fr, wh):
    F = [fr[k] for k in sorted(fr) if k > 0]
    W = [wh[k] for k in sorted(wh) if k > 0]
    Fk = [k for k in sorted(fr) if k > 0]
    Wk = [k for k in sorted(wh) if k > 0]
    ratio = (sum(map(len, W)) or 1) / (sum(map(len, F)) or 1)
    FA, WA = [anchors(x) for x in F], [anchors(x) for x in W]
    n, m = len(F), len(W)
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    beads = [(1, 1)] + [(k, 1) for k in range(2, 6)] + [(1, k) for k in range(2, 6)] + [(1, 0), (0, 1)]
    SKIP = float(os.environ.get('ALIGN_SKIP', 1.6))  # cost of a cut or an addition

    def cost(i, j, a, b):
        if a == 0 or b == 0:
            L = len(W[j]) if a == 0 else len(F[i]) * ratio
            return SKIP + 0.15 * math.log1p(L / 80)
        fl = sum(len(F[x]) for x in range(i, i + a)) * ratio
        wl = sum(len(W[y]) for y in range(j, j + b))
        c = abs(math.log((wl + 20) / (fl + 20))) * 2.0
        fa = set().union(*FA[i:i + a]); wa = set().union(*WA[j:j + b])
        if fa or wa:
            c -= 1.2 * len(fa & wa) / max(1, len(fa | wa))
        return c + 0.35 * (a + b - 2)

    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            for a, b in beads:
                if i + a > n or j + b > m:
                    continue
                c = D[i][j] + cost(i, j, a, b)
                if c < D[i + a][j + b]:
                    D[i + a][j + b] = c
                    B[i + a][j + b] = (a, b, c - D[i][j])
    out, i, j = [], n, m
    while i or j:
        a, b, c = B[i][j]
        i, j = i - a, j - b
        fr_r = '-' if a == 0 else (f'¶{Fk[i]}' if a == 1 else f'¶{Fk[i]}–¶{Fk[i + a - 1]}')
        wh_r = '-' if b == 0 else (f'¶{Wk[j]}' if b == 1 else f'¶{Wk[j]}–¶{Wk[j + b - 1]}')
        kind = 'cut?' if b == 0 else 'add?' if a == 0 else f'{a}-{b}'
        fl = sum(len(F[x]) for x in range(i, i + a)) * ratio; wl = sum(len(W[y]) for y in range(j, j + b))
        if a and b and fl > 150 and wl < 0.6 * fl:
            kind += ' short?'
        elif a and b and wl > 150 and wl > 1.6 * fl:
            kind += ' long?'
        out.append((fr_r, wh_r, kind, round(c, 2),
                    sum(len(F[x]) for x in range(i, i + a)), sum(len(W[y]) for y in range(j, j + b))))
    out.reverse()
    return [('¶0', '¶0', 'summary', 0, len(fr.get(0, '')), len(wh.get(0, '')))] + out


def main():
    args = sys.argv[1:]
    if args == ['all']:
        args = ['%02d' % k for k in range(1, 63)]
    os.makedirs(os.path.join(HERE, 'align'), exist_ok=True)
    for nn in args:
        fr = paras(os.path.join(HERE, 'fr-1875', f'{nn}.md'))
        wh = paras(os.path.join(HERE, 'white-1876', f'{nn}.md'))
        rows = align(fr, wh)
        with open(os.path.join(HERE, 'align', f'{nn}.tsv'), 'w', encoding='utf-8') as fh:
            fh.write('fr\twhite\tkind\tcost\tfr_chars\twhite_chars\n')
            for r in rows:
                fh.write('\t'.join(map(str, r)) + '\n')
        cuts = sum(r[2] == 'cut?' for r in rows); adds = sum(r[2] == 'add?' for r in rows)
        short = sum('short?' in r[2] for r in rows); long_ = sum('long?' in r[2] for r in rows)
        print(f'{nn}: {len(fr)} fr, {len(wh)} white, {len(rows)} beads, {cuts} cut?, {adds} add?, {short} short?, {long_} long?')


if __name__ == '__main__':
    main()
