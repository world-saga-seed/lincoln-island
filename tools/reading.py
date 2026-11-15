#!/usr/bin/env python3
"""The reading list for one chapter's agents, one hop from its outline and notes.

A drafter or critic told "read the cards it needs" opens whole files and reads
far more than it uses; one told "read the drafts before" reads the whole volume.
This builds the list instead: every link in the chapter's outline and notes,
resolved to its file and, where the link names a heading in a large file, to
that section's line range; any card the outline or notes name without a link (by its name, a
person's first name, or a keyword); the sheets of the people the chapter names; the
chapter before; and the volume digest in place of the rest of the volume.

Usage:
  python3 tools/reading.py N [--step STEP] [--digest FILE] [--rules FILE ...]
                          [--sheets DIR] [--large WORDS]

  N              the chapter number, as it starts the file names (e.g. 00400)
  --step STEP    narrow the list for one role: drafter (default, everything),
                 facts (cards, sections and sheet heads), setup (cards, whole
                 sheets), procedures (cards and sections), habits (sheets'
                 Habits sections only), continuity (digest and prose)
  --digest FILE  the volume digest, read in place of the earlier chapters
  --rules FILE   files every drafter reads (default: story/voice/voice.md,
                 plan/workflows/drafting/rulings.md)
  --sheets DIR   the character sheets' folder (default story/notes/characters)
  --large WORDS  a file over this many words is listed by section (default 1500)

Reads story/outline/N-*.md and story/notes/N-*.md and story/prose/. Prints the
list as markdown; write it to the task's folder and give it to the agent with
"read these and nothing else, unless a fact you need is missing; then follow
one link and say so in your report". Run from the book's top folder.
"""
import argparse, collections, glob, os, re


def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- ]', '', h)
    return h.replace(' ', '-')


_cache = {}


def sections(path):
    """anchor -> (title, level, first line, last line, words); '' is the whole file."""
    if path in _cache:
        return _cache[path]
    lines = open(path, encoding='utf-8').read().split('\n')
    heads, seen = [], collections.Counter()
    for i, line in enumerate(lines, 1):
        m = re.match(r'(#+) (.*)', line)
        if m:
            s = slug(m.group(2))
            k = seen[s]
            seen[s] += 1
            heads.append((s if k == 0 else f'{s}-{k}', m.group(2).strip(), len(m.group(1)), i))
    out = {'': ('(whole file)', 0, 1, len(lines), sum(len(l.split()) for l in lines))}
    for j, (an, t, lv, st) in enumerate(heads):
        end = len(lines)
        for _, _, lv2, st2 in heads[j + 1:]:
            if lv2 <= lv:
                end = st2 - 1
                break
        out[an] = (t, lv, st, end, sum(len(l.split()) for l in lines[st - 1:end]))
    _cache[path] = out
    return out


def fmt(path, anchors, large):
    S = sections(path)
    whole = S['']
    anchors = {a for a in anchors if a in S}
    if not anchors or '' in anchors or whole[4] <= large:
        return f'- `{path}` (whole, {whole[4]} words)'
    keep = []
    for an in sorted(anchors, key=lambda x: (S[x][2], -S[x][3])):
        if not any(S[k][2] <= S[an][2] and S[an][3] <= S[k][3] for k in keep):
            keep.append(an)
    rows = [f'- `{path}` ({whole[4]} words in all; read only these sections, by line):']
    for an in keep:
        t, _, st, en, w = S[an]
        rows.append(f'  - lines {st} to {en}: "{t}" ({w} words)')
    return '\n'.join(rows)


def habits_of(sh, large):
    S = sections(sh)
    hs = [x for x in S if x and 'habit' in x]
    if hs:
        return fmt(sh, {hs[0]}, 0)
    for i, line in enumerate(open(sh, encoding='utf-8'), 1):
        if re.match(r'-\s+\*\*Habits', line):
            return f'- `{sh}`: line {i}, the **Habits** item'
    return f'- `{sh}`: no Habits section; read the head only'


def main():
    ap = argparse.ArgumentParser(description="The reading list for one chapter's agents.")
    ap.add_argument('n')
    ap.add_argument('--step', default='drafter',
                    choices=['drafter', 'facts', 'setup', 'procedures', 'habits', 'continuity'])
    ap.add_argument('--digest')
    ap.add_argument('--rules', nargs='*', default=['story/voice/voice.md', 'plan/workflows/drafting/rulings.md'])
    ap.add_argument('--sheets', default='story/notes/characters')
    ap.add_argument('--large', type=int, default=1500)
    a = ap.parse_args()
    N, step = a.n, a.step
    srcs = [p for p in (sorted(glob.glob(f'story/outline/{N}-*.md')) + sorted(glob.glob(f'story/notes/{N}-*.md')))]
    if not srcs:
        raise SystemExit(f'no outline or notes for {N}')

    links = collections.defaultdict(set)
    for p in srcs:
        for m in re.finditer(r'\]\(([^)\s]+)\)', open(p, encoding='utf-8').read()):
            f, _, an = m.group(1).partition('#')
            if re.match(r'^[a-z]+:', f):
                continue
            t = os.path.normpath(os.path.join(os.path.dirname(p), f)) if f else p
            if t in srcs or not t.endswith('.md') or not os.path.exists(t):
                continue
            links[t].add(an)

    text = ' '.join(open(p, encoding='utf-8').read() for p in srcs).lower()
    sheets = {t for t in links if t.startswith(a.sheets.rstrip('/') + '/')}
    for sh in glob.glob(os.path.join(a.sheets, '**', '*.md'), recursive=True):
        if os.path.basename(sh) == 'README.md':
            continue
        stem = os.path.basename(sh)[:-3].replace('-', ' ')
        first = open(sh, encoding='utf-8').readline().lstrip('# ').split(':')[0].split('(')[0].strip().lower()
        if any(len(nm) > 3 and re.search(r'\b' + re.escape(nm) + r'\b', text) for nm in {stem, first}):
            sheets.add(os.path.normpath(sh))

    # cards the outline or notes name without linking: by the card's name, a
    # person's first name (two capitalized words), or a keyword from its head
    raw = ' '.join(open(p, encoding='utf-8').read() for p in srcs)
    for c in glob.glob('world/**/*.md', recursive=True):
        if os.path.basename(c) in ('README.md', 'INDEX.md') or c in links:
            continue
        head = open(c, encoding='utf-8').read().split('\n')[:5]
        nm = head[0].lstrip('# ').split(':')[0].strip()
        terms = [re.sub(r'^(the|a|an) ', '', nm.lower())]
        terms += [k.strip().lower() for k in head[4][10:].split(',')] if head[4:] and head[4].startswith('Keywords: ') else []
        hit = any(len(t) > 3 and re.search(r'\b' + re.escape(t) + r'\b', text) for t in terms)
        if re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+$', nm):
            hit = hit or bool(re.search(r'\b' + nm.split()[0] + r'\b', raw))
        if hit:
            links[os.path.normpath(c)].add('')

    prose = sorted(p for p in glob.glob('story/prose/*.md') if os.path.basename(p) < N)
    prev = prose[-1] if prose else None
    cards = sorted(t for t in links if t not in sheets and t.startswith('world/'))
    other = sorted(t for t in links if t not in sheets and t not in cards and t.startswith('story/'))

    out = [f'# Reading list for {N} ({step})', '',
           'Built by `tools/reading.py`. Read these and nothing else, unless a fact you need is missing; '
           'then follow one link and say so in your report.', '']
    if step == 'drafter':
        out += ['## Rules', '', *[f'- `{p}`' for p in a.rules if os.path.exists(p)],
                '- two or three of `story/voice/samples/`', '']
    out += ['## The chapter', '', *[f'- `{p}` (whole)' for p in srcs], '']
    if step in ('drafter', 'facts', 'setup', 'procedures'):
        out += ['## Cards and sections', '', *[fmt(t, links[t], a.large) for t in cards], '']
        if other:
            out += ['## Linked but not to read', '',
                    "Other chapters' outlines and method notes. The chapter's own outline and notes carry what "
                    'binds it; open one only if a settled line there is quoted to you as a conflict.', '',
                    ', '.join(f'`{t}`' for t in other), '']
    if step in ('drafter', 'facts', 'setup', 'habits'):
        out += ['## People', '']
        for sh in sorted(sheets):
            if step == 'habits':
                out.append(habits_of(sh, a.large))
            elif step == 'facts':
                S = sections(sh)
                out.append(fmt(sh, links.get(sh, set()) | {x for x in S if x and S[x][1] <= 2 and 'glance' in x}, a.large))
            else:
                out.append(fmt(sh, {''}, a.large))
        out.append('')
    if step in ('drafter', 'facts', 'setup', 'procedures', 'continuity'):
        out += ['## Prose', '']
        if a.digest and os.path.exists(a.digest):
            out.append(f"- `{a.digest}`: what the volume's pages have already set; read whole, in place of the earlier chapters")
        if prev:
            out.append(f'- `{prev}`: the chapter before; read closely')
        out.append('')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
