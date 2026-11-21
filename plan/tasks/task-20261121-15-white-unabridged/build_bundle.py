#!/usr/bin/env python3
"""Build a re-render bundle for one chapter of the book (White made unabridged, R1121-144).

Usage: python3 build_bundle.py NN OUTDIR   (NN = the French file number, 01 to 62)
The French whole; the chapter's outline and notes; the facts of every card citing
the chapter, cut to what is known by it (a bullet citing a later chapter is dropped).
Adapted from plan/archive/task-20261121-11-render-v1/build_bundles.py. Run from the root.
"""
import re, sys, pathlib
sys.path.insert(0, 'plan/archive/task-20261121-11-render-v1')
from build_bundles import cut_card, LINK, key
nn = int(sys.argv[1]); out = pathlib.Path(sys.argv[2])
part, ch = ('I', nn) if nn <= 22 else ('II', nn - 22) if nn <= 42 else ('III', nn - 42)
cite = '%s.%d' % (part, ch); cutoff = key(part, ch); code = '%05d' % (nn * 100)
tag = re.compile(r'(?<![\w.])%s\.%d\b' % (part, ch))
outline = next(pathlib.Path('story/outline').glob(code + '-*.md'))
notes = next(pathlib.Path('story/notes').glob(code + '-*.md'))
parts = ['# Bundle for %s (%s), White made unabridged\n' % (code, cite),
         '*Built by `build_bundle.py`. The cards are cut to what is known by the chapter.*\n',
         '\n## The French: texts/fr-1875/%02d.md (render every sentence)\n\n' % nn,
         pathlib.Path('texts/fr-1875/%02d.md' % nn).read_text(encoding='utf-8'),
         '\n## The outline\n\n', outline.read_text(encoding='utf-8'),
         '\n## The notes\n\n', notes.read_text(encoding='utf-8'), '\n## The cards\n']
manifest = []
for p in sorted(pathlib.Path('world').glob('*/*.md')):
    if p.name == 'README.md' or not tag.search(p.read_text(encoding='utf-8')): continue
    title, body = cut_card(str(p), cutoff, cutoff)
    facts = sum(1 for l in body if re.match(r'^  - ', l))
    if not facts: continue
    parts.append('\n### %s\n\n%s\n' % (title, '\n'.join(body)))
    manifest.append('%s\t%d facts' % (p, facts))
(out / ('bundle-%s.md' % code)).write_text(LINK.sub(r'\1', ''.join(parts)), encoding='utf-8')
(out / ('manifest-%s.tsv' % code)).write_text('\n'.join(manifest) + '\n', encoding='utf-8')
print(code, len(manifest), 'cards', len(''.join(parts).split()), 'words')
