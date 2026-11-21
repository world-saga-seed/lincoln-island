#!/usr/bin/env python3
"""Vet White's derived working text against the Gutenberg HTML, word for word.

Written apart from derive_white.py: regex, not html.parser. Takes the body from
the "THE MYSTERIOUS ISLAND." heading after the contents to the "END OF TRANSLATION"
heading, strips every tag, and compares its words, in order, with the words of
texts/white-1876/01.md to 62.md (less ¶N, hd and the ' / ' line marks).
Prints each difference and a count; exit 1 on any.

Usage: python3 texts/vet_white.py
"""
import difflib, glob, html, re, sys

raw = open('existing/white-1876/8misl10h.htm', encoding='utf-8').read()
start = raw.index('<H4>THE MYSTERIOUS ISLAND.</H4>')
end = raw.index('</H4>', raw.index('END OF TRANSLATION OF THE MYSTERIOUS ISLAND')) + 5
body = re.sub(r'</?(?:i|b|font|a|span|sup|sub|small)\b[^>]*>', '', raw[start:end], flags=re.I)
body = re.sub(r'<[^>]+>', ' ', body)
a = html.unescape(body).replace(' ', ' ').split()

b = []
for f in sorted(glob.glob('texts/white-1876/[0-9][0-9].md')):
    for ln in open(f, encoding='utf-8').read().splitlines():
        if ln.startswith('¶') or ln.startswith('hd '):
            ln = re.sub(r'^(¶\d+|hd) ', '', ln).replace(' / ', ' ')
            b += ln.split()

bad = 0
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
    if op != 'equal':
        bad += 1
        print(f'{op}: raw [{" ".join(a[i1:i2])[:120]}] derived [{" ".join(b[j1:j2])[:120]}]')
print(f'{len(b)} words, {bad} differences')
sys.exit(1 if bad else 0)
