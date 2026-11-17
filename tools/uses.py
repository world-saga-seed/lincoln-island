#!/usr/bin/env python3
"""When a card changes, which drafted chapters used what changed, and where on their pages.

Usage:
  python3 tools/uses.py --manifests DIR --since REV          the cards changed since a commit
  python3 tools/uses.py --manifests DIR CARD [CARD ...]      these cards (every field counts as changed)
      [--prose story/prose] [--called FILE] [--context 0]

DIR holds the saved drafter manifests, one a chapter (`reading.py --bundle
--manifest DIR/NNNNN-drafter.tsv`): what the drafter's bundle gave of each file.

For each changed card (with --since, git compares each field of the card at REV with
the card now, so a card whose fields did not change but whose body did is listed
whole), this prints every chapter whose manifest gave a changed field, or gave the
card whole or by its sections, and then the lines of that chapter's prose that name
the card (its name, or a Keywords word of five letters or more), with their line
numbers. Those lines are where to look: the draft was written from the old field.
A chapter whose bundle did not give the changed field is listed apart, since its
drafter never saw it; a manifest marks such a card "cited" or "named, not given".

Exit 0. It changes nothing; the critics or the reviser act on what it lists.
"""
import argparse, glob, os, re, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cards as cardtool  # noqa: E402


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True).stdout


def fields_of(text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(text)
    try:
        return {l: t for l, _, _, t in cardtool.fields(f.name)}
    finally:
        os.unlink(f.name)


def changed(since, paths):
    """{card: set of changed field labels, or None for the whole card}."""
    out = {}
    if since:
        names = [p for p in git('diff', '--name-only', since, '--', *(paths or ['world', 'story/notes/characters'])).split('\n')
                 if p.endswith('.md') and os.path.exists(p) and not p.endswith('README.md')]
        for p in names:
            old, new = fields_of(git('show', f'{since}:{p}')), fields_of(open(p, encoding='utf-8').read())
            diff = {l for l in set(old) | set(new) if old.get(l) != new.get(l)}
            out[os.path.normpath(p)] = diff or None
    else:
        for p in paths:
            out[os.path.normpath(p)] = None
    return out


def load(path):
    m, rev = {}, ''
    for line in open(path, encoding='utf-8'):
        if line.startswith('# commit '):
            rev = line.split()[2]
        elif '\t' in line and not line.startswith('#'):
            p, g = line.rstrip('\n').split('\t', 1)
            m[os.path.normpath(p)] = g
    return m, rev


def load_called(path):
    """{card: [what the page calls it]} from a file of card<TAB>names (';'-separated): the narrator's own
    words for a person or thing ("my mother"), which a card's name and keywords may not hold."""
    c = {}
    for line in open(path, encoding='utf-8') if path else []:
        if line.strip() and not line.startswith('#') and '\t' in line:
            k, v = line.rstrip('\n').split('\t', 1)
            c[os.path.normpath(k.strip())] = [x.strip() for x in v.split(';') if x.strip()]
    return c


def names_of(p, called=None):
    name, _, _, kw, _ = cardtool.head(p)
    words = (called or {}).get(os.path.normpath(p), []) + [re.sub(r'\s*\(.*', '', name).strip()] + [k for k in kw if len(k) >= 5]
    return [w for w in dict.fromkeys(words) if w]


def main():
    ap = argparse.ArgumentParser(description='Chapters to inspect when a card changes.')
    ap.add_argument('cards', nargs='*')
    ap.add_argument('--manifests', required=True)
    ap.add_argument('--since', help='a commit: list the cards changed since it, by field')
    ap.add_argument('--prose', default='story/prose')
    ap.add_argument('--called', help="a file of card<TAB>what the page calls it (';'-separated), e.g. a mother the narrator calls \"my mother\"")
    ap.add_argument('--context', type=int, default=0, help='lines of the page to show around each hit')
    a = ap.parse_args()
    if not a.since and not a.cards:
        sys.exit('name the cards, or give --since')
    ch = changed(a.since, a.cards)
    called = load_called(a.called)
    mans = {os.path.basename(m)[:5]: load(m) for m in sorted(glob.glob(os.path.join(a.manifests, '*.tsv')))}
    for card, fs in sorted(ch.items()):
        print(f'## {card}: ' + ('whole card' if fs is None else 'changed: ' + ', '.join(sorted(fs))))
        names = names_of(card, called) if os.path.exists(card) else []
        rx = re.compile(r'\b(' + '|'.join(re.escape(n) for n in names) + r')', re.I) if names else None
        hit_any, unseen = False, []
        for n, (m, rev) in mans.items():
            g = m.get(card)
            if g is None:
                continue
            if 'not given' in g:
                unseen.append(n)
                continue
            given = [x.strip() for x in g[7:].split(';')] if g.startswith('fields:') else None
            if fs is not None and given is not None and not set(fs) & set(given):
                unseen.append(n)
                continue
            hit_any = True
            what = ', '.join(sorted(set(fs) & set(given))) if fs is not None and given is not None else g
            print(f'\n- **{n}** (drafted at {rev or "?"}; given {what})')
            for pr in sorted(glob.glob(os.path.join(a.prose, f'{n}-*.md')))[:1]:
                lines = open(pr, encoding='utf-8').read().split('\n')
                for i, l in enumerate(lines, 1):
                    if rx and rx.search(l):
                        lo, hi = max(1, i - a.context), min(len(lines), i + a.context)
                        print(f'  - `{pr}:{i}`' + (f'-{hi}' if hi > i else '') + f': {l.strip()[:120]}')
        if not hit_any:
            print('\n- no drafted chapter was given what changed')
        if unseen:
            print(f'\n- not given to the drafter (cited, named, or other fields): {", ".join(unseen)}')
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
