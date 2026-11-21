#!/usr/bin/env python3
"""Triplets for rhythm (R1121-117): series of three ("A, B and C", "A, B, and C") in an
English text that the aligned French does not have.

For each aligned unit (French paragraphs <-> English paragraphs), count the series of three
or more in the English narration and in the French ("A, B et C", "A, B, C"). A series in the
English beyond the French count is one not in the French: a triplet for rhythm, or one the
render made. Verne's lists are the ones the French has. Speech is left out on both sides.

  triplets.py white NN          White's chapter NN, aligned by texts/align/NN.tsv
  triplets.py render NN FILE    a render that follows the French paragraph by paragraph
"""
import re, sys

# A series: three items of one to four words each, the last two joined by and/or (et/ou/ni).
W = r"[\w’'-]+"
ITEM = W + r"(?: " + W + r"){0,3}"
EN = re.compile(r"(?<![\w,] )\b" + ITEM + r", " + ITEM + r",? (?:and|or|nor) " + ITEM + r"(?=[.;:,!?]|$)", re.I | re.M)
FR = re.compile(r"\b" + ITEM + r", " + ITEM + r",? (?:et|ou|ni) " + ITEM + r"(?=[.;:,!?]|$)", re.I | re.M)
QUOTES = re.compile(r'[“"«][^”"»]*[”"»]|^—.*$', re.M)

def narr(t): return QUOTES.sub(' ', t)
def count(rx, t): return len(rx.findall(narr(t)))

def paras(path, prefix='¶'):
    d = {}
    for l in open(path, encoding='utf-8'):
        m = re.match(r'^¶(\d+)(?: \[[^\]]*\])? (.*)$', l.rstrip('\n'))
        if m: d[int(m.group(1))] = m.group(2)
    return d

def rng(s):
    a = [int(x) for x in re.findall(r'\d+', s)]
    return list(range(a[0], a[-1] + 1)) if a else []

def report(units, label):
    words = sum(len(narr(e).split()) for _, e in units)
    extra, found = 0, []
    for f, e in units:
        ne, nf = count(EN, e), count(FR, f)
        if ne > nf:
            extra += ne - nf
            found += [m for m in EN.findall(narr(e))][:ne - nf]
    print(f'{label}: narration {words} words; series not in the French {extra}; per 1,000 words {1000*extra/max(1,words):.2f}')
    for m in found: print('   ', m)
    return extra, words

if __name__ == '__main__':
    mode, nn = sys.argv[1], int(sys.argv[2])
    fr = paras('texts/fr-1875/%02d.md' % nn)
    if mode == 'white':
        wh = paras('texts/white-1876/%02d.md' % nn)
        units = []
        for l in list(open('texts/align/%02d.tsv' % nn, encoding='utf-8'))[1:]:
            c = l.rstrip('\n').split('\t')
            if c[0] == '¶0' or not c[0] or not c[1] or c[0] == '—' or c[1] == '—': continue
            units.append((' '.join(fr.get(i, '') for i in rng(c[0])), ' '.join(wh.get(i, '') for i in rng(c[1]))))
        report(units, 'White %s' % nn)
    else:
        en = [l.strip() for l in open(sys.argv[3], encoding='utf-8') if l.strip()]
        en = [l for l in en if not l.startswith('#') and not l.startswith('CHAPTER') and not re.match(r'^\(\d\)', l)][1:]
        fk = sorted(k for k in fr if k > 0)
        assert len(fk) == len(en), (len(fk), len(en))
        report([(fr[k], e) for k, e in zip(fk, en)], sys.argv[3].split('/')[-1][:5])
