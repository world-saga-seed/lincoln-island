#!/usr/bin/env python3
"""Phase 9: stage the ereader book and build it with tools/epub.py.

Reading order: White XIX; v1 XIX; v1 XIX bis (with its note: no translation); v1 XX; White XX.
The v1 run reads straight through, with White's own chapter on either side to compare.
Staged copies go to a scratch folder; the prose files are not touched. Run from the repo root.
"""
import re, sys, pathlib, subprocess, glob

STAGE = pathlib.Path(sys.argv[1]); STAGE.mkdir(parents=True, exist_ok=True)
OUT = sys.argv[2]
HERE = pathlib.Path(__file__).parent

def white(n, roman, label):
    out = [f'# {roman}. White\'s translation (1876)', '']
    for l in open(f'texts/white-1876/{n:02d}.md', encoding='utf-8'):
        m = re.match(r'^(hd|¶\d+|n\d+)(?: \[[^\]]*\])? (.*)$', l.rstrip('\n'))
        if not m: continue
        k, t = m.groups()
        out += [t, ''] if k != 'hd' else [t, '']
    p = STAGE / f'{label}.md'; p.write_text('\n'.join(out), encoding='utf-8'); return p

def v1(path, title, note=None):
    lines = open(path, encoding='utf-8').read().splitlines()
    assert lines[0].startswith('# ')
    body = lines[1:]
    head = [f'# {title}', '']
    if note: head += [note, '']
    p = STAGE / (pathlib.Path(path).stem + '.md'); p.write_text('\n'.join(head + body) + '\n', encoding='utf-8'); return p

files = [
  white(19, 'XIX', '1-white-19'),
  v1(glob.glob('story/prose/01900-*.md')[0], 'XIX. Version 1, rendered from the French'),
  v1(glob.glob('story/prose/01950-*.md')[0], 'XIX bis. The missing chapter',
     '*This chapter has no French original and no translation by White. It is the chapter inserted into the book, written by a model by the World Saga Seed method, in Verne\'s manner and White\'s English.*'),
  v1(glob.glob('story/prose/02000-*.md')[0], 'XX. Version 1, rendered from the French'),
  white(20, 'XX', '5-white-20'),
]
cmd = ['python3', 'tools/epub.py', '--title', 'Lincoln Island: chapters XIX to XX',
       '--author', 'Jules Verne; the missing chapter by a model, by the World Saga Seed method',
       '--front', str(HERE / 'front.md'), '--out', OUT] + [str(f) for f in files]
print(' '.join(cmd)); sys.exit(subprocess.call(cmd))
