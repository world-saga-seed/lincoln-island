#!/usr/bin/env python3
"""Count White's discords by kind and chapter from texts/align/NN-discords.md headings; write texts/align/SUMMARY.md.
Usage: python3 texts/sum_discords.py"""
import collections, glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
KINDS = ['cut', 'condensed', 'addition', 'changed', 'softened']
def cite(k): return ('I.%d' % k) if k <= 22 else ('II.%d' % (k - 22)) if k <= 42 else ('III.%d' % (k - 42))
rows, tot = [], collections.Counter()
for f in sorted(glob.glob(os.path.join(HERE, 'align', '[0-9][0-9]-discords.md'))):
    nn = int(os.path.basename(f)[:2]); s = open(f, encoding='utf-8').read()
    c = collections.Counter(re.findall(r'^### \d+\. (\w+):', s, re.M))
    slips = s.split('## Outline slips', 1)[1] if '## Outline slips' in s else ''
    nslip = len(re.findall(r'^- (?!None)', slips, re.M))
    rows.append((nn, c, nslip)); tot.update(c)
out = ['# White against the French: the discords, summed', '',
       '*Made by `texts/sum_discords.py` from the headings of `texts/align/NN-discords.md` (R1120-43). The outline slips were folded back into `story/outline/` (R1120-41).*', '',
       '| Chapter | White | ' + ' | '.join(KINDS) + ' | all | outline slips |', '|---|---|' + '---|' * (len(KINDS) + 2)]
for nn, c, ns in rows:
    out.append(f'| {nn * 100:05d} | {cite(nn)} | ' + ' | '.join(str(c[k]) for k in KINDS) + f' | {sum(c.values())} | {ns} |')
out.append('| **all** | | ' + ' | '.join(f'**{tot[k]}**' for k in KINDS) + f' | **{sum(tot.values())}** | **{sum(r[2] for r in rows)}** |')
out += ['', '## Book-wide', '',
        '- **The boat\'s name.** White calls the Bonadventure "Good Luck" in every chapter that names it, and says Pencroff chose the name (II.12), where the French gives it as his baptismal name. Some lists log it per chapter; it is one discord. *(Drafted.)*',
        '- **The glossary.** White III.20 ends with a glossary of 92 entries after "THE END." (White ¶54 to ¶145), the edition\'s own; not aligned. *(Drafted.)*',
        '- **No footnotes.** White prints none of Hetzel\'s footnotes, the Publisher\'s notes on the dates among them (II.17 n1, III.16 n1); the lists log them as cuts where they fall. *(Drafted.)*',
        '- **The names.** Herbert, Neb and Gideon for Harbert, Nab and Gédéon, and other settled English forms, are not counted. *(Drafted.)*',
        '- **The source.** The Gutenberg HTML has its own faults, kept as it has them: White I.2 ¶25 repeats ¶23; II.17 ¶80 and I.19 ¶31 break mid-sentence; misprints such as "l5 pounds" and "I adzes" are logged as discords marked as readings (see `texts/README.md`). *(Drafted.)*']
other = set(tot) - set(KINDS)
if other: out.append(f'\nUnknown kinds: {sorted(other)}')
open(os.path.join(HERE, 'align', 'SUMMARY.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(rows), 'chapters;', dict(tot), sum(tot.values()))
