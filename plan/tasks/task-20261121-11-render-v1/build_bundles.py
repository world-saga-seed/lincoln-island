#!/usr/bin/env python3
"""Build the phase 8 drafters' bundles: one file per chapter, cut to the horizon.

A card bullet is kept only if every citation in it (I.19 ¶5, II.2 ...) falls at or
before the chapter's cutoff, or it carries no citation and is a settled ruling.
Its quote sub-bullets go with it. Run from the repository root.
"""
import re, pathlib

ROMAN = {'I': 1, 'II': 2, 'III': 3}
CITE = re.compile(r'\b(III|II|I)\.(\d+)\b')

def key(part, ch): return ROMAN[part] * 100 + int(ch)

def cut_card(path, cutoff, own=None):
    """Card text, its bullets cut at cutoff (part*100+ch). own: keep only bullets citing that chapter."""
    out, keep = [], False
    lines = pathlib.Path(path).read_text(encoding='utf-8').splitlines()
    title = lines[0].lstrip('# ').strip()
    for l in lines[1:]:
        if l.startswith('## ') or l.startswith('- **'):
            out.append(l); keep = True; continue
        m = re.match(r'^(\s*)- ', l)
        if m and len(m.group(1)) == 2:          # a fact bullet
            cites = [key(p, c) for p, c in CITE.findall(l)]
            if own is not None:
                keep = own in cites and all(c <= cutoff for c in cites)
            elif cites:
                keep = all(c <= cutoff for c in cites)
            else:
                keep = '(Settled R' in l
            if keep: out.append(l)
        elif m and len(m.group(1)) >= 4:        # quote under a fact
            if keep: out.append(l)
    # drop headings left empty
    body = [l for i, l in enumerate(out)
            if not (l.startswith('- **') and (i + 1 == len(out) or out[i+1].startswith('- **') or out[i+1].startswith('## ')))]
    return title, body

LINK = re.compile(r'\[([^\]]+)\]\([^)]+\)')

def drop_sections(path, drop, drop_lines=()):
    text = pathlib.Path(path).read_text(encoding='utf-8')
    text = '\n'.join(l for l in text.splitlines() if not any(d in l for d in drop_lines)) + '\n'
    parts = re.split(r'(?m)^(?=## )', text)
    return ''.join(p for p in parts if not any(p.startswith('## ' + d) for d in drop))

def french(n):
    return pathlib.Path('texts/fr-1875/%02d.md' % n).read_text(encoding='utf-8')

CH = {
 '01900': dict(fr=19, cutoff=key('I', 19), own=key('I', 19), drop=['The seam with 01950'], lines=[],
               cards='auto'),
 '01950': dict(fr=None, cutoff=key('I', 19), own=None, drop=['Clues'], lines=['*(Settled R1121-24.)* It foreshadows the chest'],
               cards=['people/pencroff', 'people/harbert', 'places/ilot-du-salut', 'places/the-channel',
                      'places/the-granite-wall', 'places/granite-house', 'places/mercy-river',
                      'places/the-chimneys', 'places/baie-de-l-union', 'things/the-rope-ladder',
                      'things/the-shutters', 'things/knife-blades', 'things/iron-tools',
                      'things/bottom-lines', 'things/lens', 'things/window-glass']),
 '02000': dict(fr=20, cutoff=key('I', 20), own=key('I', 20), drop=['The seam with 01950'], lines=[],
               cards='auto'),
}

def auto_cards(n):
    """Every card citing the chapter's own French."""
    tag = re.compile(r'\bI\.%d\b' % CH[n]['fr'])
    return sorted(str(p)[6:-3] for p in pathlib.Path('world').glob('*/*.md')
                  if p.name != 'README.md' and tag.search(p.read_text(encoding='utf-8')))

if __name__ == '__main__':
    here = pathlib.Path(__file__).parent
    for n, c in CH.items():
        outline = next(pathlib.Path('story/outline').glob(n + '-*.md'))
        notes = next(pathlib.Path('story/notes').glob(n + '-*.md'))
        parts = ['# Bundle for %s (drafter, phase 8)\n' % n,
                 '*Built by `build_bundles.py`. The cards are cut to what is known by the chapter: a fact citing a later chapter is left out.*\n']
        if c['fr']:
            parts += ['\n## The French: texts/fr-1875/%02d.md (render every sentence)\n\n' % c['fr'], french(c['fr'])]
        parts += ['\n## The outline\n\n', drop_sections(outline, c['drop'], c['lines']),
                  '\n## The notes\n\n', notes.read_text(encoding='utf-8')]
        cards = auto_cards(n) if c['cards'] == 'auto' else c['cards']
        parts.append('\n## The cards\n')
        manifest = []
        for card in cards:
            title, body = cut_card('world/%s.md' % card, c['cutoff'], c['own'])
            facts = sum(1 for l in body if re.match(r'^  - ', l))
            if not facts: continue
            parts.append('\n### %s\n\n%s\n' % (title, '\n'.join(body)))
            manifest.append('world/%s.md\t%d facts' % (card, facts))
        (here / ('bundle-%s.md' % n)).write_text(LINK.sub(r'\1', ''.join(parts)), encoding='utf-8')
        (here / ('manifest-%s.tsv' % n)).write_text('\n'.join(manifest) + '\n', encoding='utf-8')
