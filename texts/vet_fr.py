#!/usr/bin/env python3
"""Vet a derived French working text against its raw Wikisource pages, word for word.

An extractor written apart from derive_fr.py (regex and a tag-depth counter, not
html.parser) takes every word out of each raw page, outside Wikisource's own
additions, the headings, the figures and the footnote back-links. The derived
file is stripped of what the deriver added (¶N, [p.N], [nN], the row and line
separators, the notes heading and the nN [¶N] labels). The two word sequences
must match exactly. Prints each difference and a count; exit 1 on any.

Usage: python3 texts/vet_fr.py SRC OUT
"""
import difflib, html, json, os, re, sys

TAG = re.compile(r'<(/?)(\w+)([^>]*)>|<!--.*?-->', re.S)
DROP_CLASS = ('ws-noexport', 'mw-cite-backlink', 'cite-bracket')
DROP_TAG = ('style', 'script', 'figure')
VOID = {'br', 'img', 'hr', 'link', 'meta', 'wbr', 'input', 'source'}
BLOCK = {'p', 'div', 'li', 'ol', 'ul', 'tr', 'td', 'table', 'tbody', 'figure', 'h2', 'h3', 'br', 'hr', 'dl', 'dd'}


def words(s):
    s = s.replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')
    return s.split()


def raw_words(text):
    out, pos, stack = [], 0, []
    for m in TAG.finditer(text):
        if not any(stack):
            out.append(text[pos:m.start()])
        pos = m.end()
        if m.group(0).startswith('<!--'):
            continue
        close, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if tag in VOID or attrs.rstrip().endswith('/'):
            if not any(stack) and tag in BLOCK:
                out.append(' ')
            continue
        if close:
            if stack:
                stack.pop()
        else:
            drop = (tag in DROP_TAG or any(c in attrs for c in DROP_CLASS)
                    or (tag == 'sup' and re.search(r'class="reference"', attrs)))
            stack.append(drop or (bool(stack) and stack[-1]))
        if not any(stack) and tag in BLOCK:
            out.append(' ')
    out.append(text[pos:])
    t = html.unescape(''.join(out))
    return words(t)


def derived_words(text):
    # put each plate caption and loose line back after the paragraph it follows
    lines = text.splitlines()
    after = {}
    for ln in lines:
        m = re.match(r'^(?:pl|ln)\d+ \[after ¶(\d+),', ln)
        if m:
            after.setdefault(int(m.group(1)), []).append(ln)
    body = after.pop(0, [])
    for ln in lines:
        if ln.startswith('hd '):
            body.append(ln)
        m = re.match(r'^¶(\d+) ', ln)
        if m:
            body.append(ln)
            k = int(m.group(1))
            if k:
                body += after.pop(k, [])
    for k in sorted(after):
        body += after[k]
    rest = [ln for ln in lines if re.match(r'^n\d+ \[', ln)]
    out = []
    for ln in body + rest:
        if ln.startswith('¶') or ln.startswith('hd '):
            ln = re.sub(r'^(¶\d+|hd) \[p\.[^\]]*\] ', '', ln)
        elif re.match(r'^(n|pl|ln)\d+ \[', ln):
            ln = re.sub(r'^(n|pl|ln)\d+ \[[^\]]*\] ', '', ln)
        else:
            continue
        ln = re.sub(r'\[n\d+\]', '', ln).replace(' | ', ' ').replace(' / ', ' ')
        out += words(ln)
    return out


def main():
    src, outd = sys.argv[1], sys.argv[2]
    raw = os.path.join('existing', src, 'raw')
    man = json.load(open(os.path.join(raw, 'manifest.json'), encoding='utf-8'))
    bad = 0
    total = 0
    for e in man:
        a = raw_words(open(os.path.join(raw, e['file']), encoding='utf-8').read())
        # the raw footnote markers are digits inside <sup class="reference">: drop them from both sides
        b = derived_words(open(os.path.join('texts', outd, e['file'].replace('.html', '.md')), encoding='utf-8').read())
        total += len(b)
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                continue
            ra, rb = ' '.join(a[i1:i2]), ' '.join(b[j1:j2])
            bad += 1
            print(f'{e["file"]}: {op}: raw [{ra[:120]}] derived [{rb[:120]}]')
    print(f'{len(man)} chapters, {total} words, {bad} differences')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
