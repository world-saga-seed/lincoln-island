#!/usr/bin/env python3
"""Check the phase 2 outlines against the working text.

For each story/outline/NNNNN-*.md (NNNNN a multiple of 100, 00100 to 06200):
  - its beats' paragraph ranges, "### N. Beat (I.1 ¶1–¶15)", cover ¶1 to the
    chapter's last paragraph with no gap and no overlap, in order;
  - the range's part.chapter matches the chapter;
  - every quote in the outline and its notes file resolves in that chapter
    (tools/quotes.py's matching, run on the chapter's own text);
  - every bullet in the outline carries a mark.
Prints one line per chapter and a count of problems; exit 1 on any.

Usage: python3 plan/tasks/task-20261120-03-outline-french/check_outlines.py [NNNNN ...]
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__)).rsplit('/plan/', 1)[0]
os.chdir(ROOT)


def cite(n):
    return f'I.{n}' if n <= 22 else f'II.{n - 22}' if n <= 42 else f'III.{n - 42}'


def last_par(n):
    nums = [int(m.group(1)) for m in re.finditer(r'^¶(\d+) ', open(f'texts/fr-1875/{n:02d}.md', encoding='utf-8').read(), re.M)]
    return max(nums)


def quotes_ok(path, n):
    r = subprocess.run(['python3', 'tools/quotes.py', path, '--in', f'texts/fr-1875/{n:02d}.md'],
                       capture_output=True, text=True)
    return r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()


def main():
    want = sys.argv[1:]
    files = sorted(glob.glob('story/outline/[0-9][0-9][0-9]00-*.md'))
    if want:
        files = [f for f in files if os.path.basename(f)[:5] in want]
    bad = 0
    for f in files:
        num = int(os.path.basename(f)[:5])
        n = num // 100
        text = open(f, encoding='utf-8').read()
        probs = []
        ranges = []
        for m in re.finditer(r'^### \d+\. .*\(([IV]+\.\d+) ¶(\d+)(?:[–-]¶?(\d+))?(?:, (?:pl|n|ln)\d+)*\)\s*$', text, re.M):
            c, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            if c != cite(n):
                probs.append(f'range cites {c}, not {cite(n)}')
            ranges.append((a, b))
        heads = len(re.findall(r'^### ', text, re.M))
        if heads != len(ranges):
            probs.append(f'{heads - len(ranges)} beat heading(s) without a readable ¶ range')
        expect = 1
        for a, b in ranges:
            if a != expect:
                probs.append(f'¶{expect} expected, beat starts ¶{a}')
            expect = b + 1
        lp = last_par(n)
        if expect - 1 != lp:
            probs.append(f'beats end ¶{expect - 1}, chapter ends ¶{lp}')
        for ln in text.splitlines():
            if re.match(r'^- ', ln) and not re.search(r'\*\((Drafted|My reading|Proposal|Settled)', ln):
                probs.append(f'unmarked: {ln[:60]}')
        ok, msg = quotes_ok(f, n)
        if not ok:
            probs.append(f'outline quotes: {msg}')
        notes = glob.glob(f'story/notes/{num:05d}-*.md')
        if not notes:
            probs.append('no notes file')
        else:
            ok, msg = quotes_ok(notes[0], n)
            if not ok and '0 quotes found' not in msg:
                probs.append(f'notes quotes: {msg}')
        bad += len(probs)
        print(f'{num:05d} {cite(n)}: {len(ranges)} beats, ¶1–¶{lp}: ' + ('ok' if not probs else '; '.join(probs)))
    print(f'{len(files)} outlines, {bad} problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
