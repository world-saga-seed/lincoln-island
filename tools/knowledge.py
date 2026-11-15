#!/usr/bin/env python3
"""What each narrating head knows, believes wrongly and does not know at one chapter.

Each head has one knowledge guard, story/voice/knowledge/<head>.md
(plan/templates/knowledge.md), whose entries carry their span as "*From* NNNNN" and,
where they end, "*until* NNNNN". This prints the entries in force at chapter N, for
the drafter's and the critics' briefs, so nobody keeps a copy per chapter. An entry
that ends at N is marked as turning in this chapter: in force up to the beat where
it changes.

Usage:
  python3 tools/knowledge.py N [--dir story/voice/knowledge] [--heads a,b] [--out FILE]

  N        the chapter number (e.g. 00500)
  --dir    the folder of guard files (default story/voice/knowledge)
  --heads  only these heads (file names without .md), comma-separated
  --out    write to FILE instead of printing
"""
import argparse, glob, os, re, sys

FROM = re.compile(r'\*From\*\s+(\d{5})')
UNTIL = re.compile(r'\*until\*\s+(\d{5})')
ENTRY = re.compile(r'^(?:[-*]|\d+\.)\s')


def entries(path):
    """Yield (section, text) for each entry in a guard file."""
    section, cur = None, None
    for line in open(path, encoding='utf-8').read().split('\n'):
        if line.startswith('## '):
            if cur:
                yield section, cur
            section, cur = line[3:].strip(), None
        elif section and ENTRY.match(line):
            if cur:
                yield section, cur
            cur = line
        elif section and cur and line.startswith((' ', '\t')) and line.strip():
            cur += ' ' + line.strip()
        elif cur and not line.strip():
            yield section, cur
            cur = None
    if cur:
        yield section, cur


def main():
    ap = argparse.ArgumentParser(description='Knowledge-guard entries in force at one chapter.')
    ap.add_argument('chapter')
    ap.add_argument('--dir', default='story/voice/knowledge')
    ap.add_argument('--heads', default='')
    ap.add_argument('--out')
    a = ap.parse_args()
    n = int(a.chapter)
    want = {h.strip() for h in a.heads.split(',') if h.strip()}
    files = sorted(glob.glob(os.path.join(a.dir, '*.md')))
    files = [f for f in files if not want or os.path.basename(f)[:-3] in want]
    if not files:
        sys.exit(f'no guard files in {a.dir}')
    out = [f'# Knowledge in force at {a.chapter}', '']
    for f in files:
        title = open(f, encoding='utf-8').readline().lstrip('# ').strip()
        out += [f'## {title}', '']
        last = None
        for section, text in entries(f):
            if section.lower().startswith('open'):
                continue
            m, u = FROM.search(text), UNTIL.search(text)
            lo = int(m.group(1)) if m else 0
            hi = int(u.group(1)) if u else None
            if lo > n or (hi is not None and hi < n):
                continue
            if section != last:
                out += ['', f'### {section}', '']
                last = section
            mark = ' **(turns in this chapter: in force up to the beat where it changes)**' if hi == n else ''
            out.append(text + mark)
        out.append('')
    text = '\n'.join(out).replace('\n\n\n', '\n\n')
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(text)
    else:
        print(text)


if __name__ == '__main__':
    main()
