#!/usr/bin/env python3
"""Point the phase 8 facts and omission critics at one chapter of White made unabridged.
Usage: python3 make_critics.py NN CHAPTER.md OUTDIR"""
import re, sys
nn, chap, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
R = '.'; A = 'plan/archive/task-20261121-11-render-v1'
code = '%05d' % (nn * 100)
part, ch = ('I', nn) if nn <= 22 else ('II', nn - 22) if nn <= 42 else ('III', nn - 42)
fr = open('texts/fr-1875/%02d.md' % nn, encoding='utf-8').read()
last = re.findall(r'^¶(\d+)', fr, re.M)[-1]; notes = re.findall(r'^(n\d+)', fr, re.M)
fn = ('lines %s are footnotes' % ', '.join(notes)) if notes else 'it has no footnotes'
for kind in ['facts', 'omission']:
    s = open('%s/prompt-critic-%s-01900.md' % (A, kind), encoding='utf-8').read()
    s = s[s.index('\n---\n'):]
    s = re.sub(r'texts/fr-1875/19\.md \([^)]*\)', 'texts/fr-1875/%02d.md (paragraph-numbered ¶0 to ¶%s; ¶0 is Verne\'s summary; %s; the pl lines are plate captions and are not rendered)' % (nn, last, fn), s)
    s = s.replace('story/prose/01900-the-facade-the-ladder-and-the-warren.md', chap)
    s = s.replace('texts/white-1876/19.md', 'texts/white-1876/%02d.md' % nn)
    s = s.replace('01900:', '%s:' % code).replace('an English render of a chapter', 'an English version of a chapter (White\'s translation patched to the French, or rendered anew from it)')
    s = s.replace('Ordinary choices of English that keep the sense are not findings.', "Ordinary choices of English that keep the sense are not findings. White's names and forms of address are the house rule and never a finding: Herbert, Neb, Gideon Spilett, and \"Mr. Smith\" for \"monsieur Cyrus\" or \"monsieur Smith\".")
    assert '19.md' not in s and '01900' not in s, kind
    open('%s/prompt-critic-%s-%s.md' % (out, kind, code), 'w', encoding='utf-8').write('# The %s critic for %s (%s.%d), White made unabridged (from the phase 8 prompt)\n%s' % (kind, code, part, ch, s))
print('ok')
