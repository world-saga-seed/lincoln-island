#!/usr/bin/env python3
"""Trace each critic finding to its source: was the fact in the drafter's bundle?

Usage:
  python3 tools/gaps.py --manifest MANIFEST REPORT [REPORT ...] [--severity break,weak] [--rules FILE ...]

MANIFEST is what `reading.py --bundle --manifest FILE` wrote for the chapter's
drafter: one line a file, path<TAB>what was given ("fields: A; B", "sections: ...",
"whole", "cited: not given", "named, not given", "the chapter, inline").

A REPORT is a critic's findings, one numbered or bulleted finding with an
"against:" line naming the file it rests on (the critic prompts ask for that).
For each finding this prints where its fact lives and what that means:

  given            the bundle held it: a drafter slip, fixed in the draft
  field not given  the card was included but not that field: add the field to
                   the chapter's include
  not included     the card was cited or named but not given, or not linked at
                   all: add an include to the chapter's notes
  chapter          the outline or notes hold it (read inline): a drafter slip
  earlier page     a chapter before this one holds it; if the drafter did not read
                   that page, the fact belongs on a card (or the digest)
  rules            a rules file the drafter reads whole: a drafter slip
  no such file     the critic cited a file that does not exist: check the finding
  no source        the critic named no file: judge it by hand

Then a list of the fixes to the source: the includes and fields to add, so the
next draft of any chapter that uses the card gets it. A finding is a lead, not a
verdict: check it against the page before you change anything.
"""
import argparse, os, re, sys

PATH = re.compile(r'((?:world|story|plan)/[\w./-]+?\.md)')
SHORT = re.compile(r'(?<![\w/.-])((?:[\w-]+/)*[\w-]+\.md)')
CHAPTER = re.compile(r'\b(?:the )?(?:outline|notes for drafting|beat\s+\d|staging)\b', re.I)


def resolve(name, manifest, rules):
    """A file a critic names loosely ("voice.md", "notes/characters/x.md"): the manifest's or the rules'
    file it ends with, else the one file under world/ or story/ it ends with."""
    name = os.path.normpath(name)
    for p in list(manifest) + list(rules):
        if p == name or p.endswith('/' + name):
            return p
    hits = []
    for root in ('world', 'story'):
        for d, _, fs in os.walk(root):
            for f in fs:
                q = os.path.normpath(os.path.join(d, f))
                if q.endswith('/' + name):
                    hits.append(q)
    return hits[0] if len(hits) == 1 else None


def load_manifest(path):
    m = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or '\t' not in line:
            continue
        p, g = line.rstrip('\n').split('\t', 1)
        m[os.path.normpath(p)] = g
    return m


def findings(path):
    """(number, severity, quote, against) for each finding in a critic's report."""
    text = open(path, encoding='utf-8').read()
    out = []
    # a finding starts at a numbered line ("3. ..."); a report with no numbers, at each bullet opening "quote:"
    starts = r'\n(?=\d+\.\s)' if re.search(r'^\d+\.\s', text, re.M) else r'\n(?=-\s+\**quote:)'
    for i, part in enumerate(re.split(starts, '\n' + text)):
        ag = re.search(r'against:?\**\s*(.+?)(?=\n\s*[-*]?\s*\**(?:why|severity|direction)\b)', part, re.I | re.S)
        sev = re.search(r'severity:?\**\s*(break|weak|taste)', part, re.I)
        if not ag or not sev:
            continue
        q = re.search(r'quote:?\**\s*(.+)', part, re.I)
        n = re.match(r'\s*(\d+)\.', part)
        out.append((n.group(1) if n else str(i), sev.group(1).lower(), (q.group(1).strip() if q else '')[:70],
                    ' '.join(ag.group(1).split())))
    return out


def card_fields(p):
    if not os.path.exists(p):
        return []
    return re.findall(r'^- \*\*([^*]+?)\.\*\*', open(p, encoding='utf-8').read(), re.M)


def trace(against, manifest, rules, chapter=None):
    paths = [os.path.normpath(p) for p in PATH.findall(against)]
    paths += [r for r in (resolve(s, manifest, rules) for s in SHORT.findall(against)
                          if not any(os.path.normpath(p).endswith(os.path.normpath(s)) for p in paths)) if r]
    if not paths:
        return [('chapter', '(the outline or notes)', '')] if CHAPTER.search(against) else [('no source', '', '')]
    out = []
    for p in dict.fromkeys(paths):
        g = manifest.get(p)
        if p in rules:
            out.append(('rules', p, ''))
        elif g and g.startswith('the chapter'):
            out.append(('chapter', p, ''))
        elif not os.path.exists(p):
            out.append(('no such file', p, ''))
        elif p.startswith('story/prose/'):
            if chapter and os.path.basename(p).startswith(chapter):
                continue  # the draft itself
            out.append(('earlier page', p, 'read' if g else 'not read: the fact belongs on a card or the digest'))
        elif g is None or 'not given' in g:
            out.append(('not included', p, g or 'not linked'))
        elif g.startswith('fields:'):
            have = [x.strip().lower() for x in g[7:].split(';')]
            named = [f for f in card_fields(p) if re.search(r'\b' + re.escape(f) + r'\b', against, re.I)]
            miss = [f for f in named if f.lower() not in have]
            out.append(('field not given', p, ', '.join(miss)) if miss and not any(f.lower() in have for f in named)
                       else ('given', p, ''))
        else:
            out.append(('given', p, ''))
    return out


def main():
    ap = argparse.ArgumentParser(description="Trace critics' findings to the drafter's bundle.")
    ap.add_argument('reports', nargs='+')
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--severity', default='break,weak', help='the severities to trace (default break,weak)')
    ap.add_argument('--rules', nargs='*', default=[], help='files the drafter reads whole (the rules)')
    ap.add_argument('--chapter', help="the chapter's number: its own draft cited is not a source")
    a = ap.parse_args()
    manifest = load_manifest(a.manifest)
    rules = {os.path.normpath(r) for r in a.rules}
    keep = set(a.severity.split(','))
    fixes, pages = {}, {}
    print('| Report | # | Severity | Quote | Source | Trace |')
    print('|---|---|---|---|---|---|')
    for r in a.reports:
        for n, sev, q, ag in findings(r):
            if sev not in keep:
                continue
            for kind, p, extra in trace(ag, manifest, rules, a.chapter):
                print(f'| {os.path.basename(os.path.dirname(os.path.abspath(r)))}/{os.path.basename(r)} | {n} | {sev} | '
                      f'{q.replace("|", "/")} | `{p}` | {kind}{": " + extra if extra else ""} |')
                if kind == 'earlier page' and extra.startswith('not read'):
                    pages.setdefault(p, []).append(n)
                elif kind == 'not included':
                    fixes.setdefault(p, set())
                elif kind == 'field not given':
                    fixes.setdefault(p, set()).update(x.strip() for x in extra.split(','))
    print('\n## Fixes to the source\n')
    if not fixes and not pages:
        print('None: every traced finding was in the bundle or the chapter.')
    for p, fs in sorted(fixes.items()):
        print(f'- include `{p}`' + (f' with {", ".join(sorted(fs))}' if fs else ''))
    for p, ns in sorted(pages.items()):
        print(f'- card the page fact from `{p}` (findings {", ".join(ns)}): the drafter did not read that page')
    return 0


if __name__ == '__main__':
    sys.exit(main())
