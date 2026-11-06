#!/usr/bin/env python3
"""Count broken links in a tree of markdown notes.

A link is broken when its file does not exist, or when it names a heading
(#anchor) that the target file does not have. Web links are skipped, and so
are links shown as examples inside `inline code` or fenced code blocks.

Usage:
  python3 tools/links.py [--root DIR] [-v] [--exclude PATTERN ...]

  --root DIR       the folder to check (default: the current folder)
  -v               list every broken link as  file:line  target
  --exclude PAT    skip files whose path (relative to root) matches this
                   shell pattern; repeatable, e.g. --exclude 'existing/*'

Prints "N broken" last. Exits 1 when N is above 0, so a script can stop on it.
"""
import argparse, fnmatch, os, re, sys

LINK = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
CODE_SPAN = re.compile(r'`[^`]*`')
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')


def slug(text):
    """The anchor a heading gets, the way common markdown viewers make it."""
    t = text.strip().lower()
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)   # a link in a heading keeps its words
    t = re.sub(r'[*_`]', '', t)
    t = ''.join(ch for ch in t if ch.isalnum() or ch in '-_ ')
    return t.replace(' ', '-')


def anchors(text):
    seen, found, fence = {}, set(), False
    for line in text.splitlines():
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING.match(line)
        if m:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            found.add(s if n == 0 else f'{s}-{n}')
            seen[s] = n + 1
    return found


def links_in(text):
    """(line number, target) for every link outside code."""
    fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for m in LINK.finditer(CODE_SPAN.sub('', line)):
            yield i, m.group(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--root', default='.', help='the folder to check (default: the current folder)')
    ap.add_argument('-v', action='store_true', help='list every broken link as file:line target')
    ap.add_argument('--exclude', action='append', default=[], help="skip files whose path (relative to root) matches this shell pattern; repeatable, e.g. 'existing/*'")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    files = []
    for d, dirs, names in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        for n in names:
            if n.endswith('.md'):
                p = os.path.join(d, n)
                rel = os.path.relpath(p, root)
                if not any(fnmatch.fnmatch(rel, pat) for pat in a.exclude):
                    files.append(p)
    cache, bad = {}, []
    for p in sorted(files):
        text = open(p, encoding='utf-8').read()
        for line, target in links_in(text):
            if re.match(r'^[a-z]+:', target):          # http:, https:, mailto:
                continue
            path, _, anchor = target.partition('#')
            f = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
            if not os.path.exists(f):
                bad.append((p, line, target))
                continue
            if anchor and f.endswith('.md'):
                if f not in cache:
                    cache[f] = anchors(open(f, encoding='utf-8').read())
                if anchor not in cache[f]:
                    bad.append((p, line, target))
    if a.v:
        for p, line, target in bad:
            print(f'{os.path.relpath(p, root)}:{line}  {target}')
    print(len(bad), 'broken')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
