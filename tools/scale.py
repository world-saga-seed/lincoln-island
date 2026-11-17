#!/usr/bin/env python3
"""The scale sheet for a chapter: the viewpoint's height, and every size phrase.

Sizes slip in model-written prose because size is relative and the drafter loses
the reference: it writes "at the height of my chest" from the person it
pictures, not from the person the book has. This tool puts the numbers in front
of the drafter and lists every size phrase for the facts critic to judge.

Usage:
  python3 tools/scale.py CHAPTER (--height CM | --heights FILE) [--other NAME=CM ...]
                          [--facts FILE] [--prose DIR]

  CHAPTER     the chapter's number, as the prose files are named (00400-...)
  --height    the viewpoint character's height at this chapter, in cm (from
              their sheet's heights table)
  --heights   a file of the viewpoint's heights by chapter, for one who grows:
              one line each, "FIRST LAST CM", chapter numbers as the files
              are named; the line whose range holds CHAPTER is used
  --facts     a file of the setting's own size facts, one per line, printed
              on the sheet in place of the default adult line (counters built
              high, a race's height); # starts a comment
  --other     another person's height, for the "against" line (repeatable)
  --prose     the prose folder (default story/prose); with it present, the
              sheet lists every size phrase on the chapter's page and marks any
              whose reference word (belts, chest, eyes) was used in a size
              phrase within two chapters either side

The body landmarks are rough human proportions; edit BODY for another species.
It costs no tokens: the drafter gets the sheet in its brief, the facts critic
gets it with --prose and judges each phrase against the heights and the cards.
"""
import argparse, glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import context  # noqa: E402  (the shared reader: stops at the notes, skips headings)

BODY = {'eyes': 0.93, 'chin': 0.87, 'shoulder': 0.82, 'chest': 0.72,
        'waist': 0.6, 'hip': 0.5, 'knee': 0.28}
ADULT = 'an adult man is about 170 cm: belt at about 100, a counter or bench top 90 to 100'
HAND = 9  # cm

TRIGGER = re.compile(r"\b(at (?:my|his|her|our|their) height|(?:my|his|her|their) height|(?:at )?the height of|"
                     r"(?:taller|shorter|higher|lower|bigger|smaller|wider|longer) than|"
                     r"as (?:big|tall|high|wide|long|small|deep|heavy) as|the size of|(?:my|his|her|their) size|"
                     r"(?:came|reached|rose|went) (?:up )?to (?:my|his|her|their)|reached (?:my|his|her|their)|"
                     r"level with (?:my|his|her|their)|up to (?:my|his|her|their)|(?:twice|half|three times) (?:my|his|her|their|a)\b)\b", re.I)
WATCH = ['belt', 'apron', 'elbow', 'coat', 'strap', 'boot', 'wheel', 'skirt', 'leg', 'knee', 'pack']  # the crowd from below: repeats here are the ones a reader notices


def phrases(path, stop=r'^## Notes'):
    """Each size phrase: the sentence round the trigger (eight words before, twelve after), and the watch words in it.
    The page is read through context's reader, so the chapter's notes and its headings are not."""
    out = []
    pats = [{'label': 'size', 're': TRIGGER, 'near_re': None, 'unless_re': None, 'within': 0, 'narration': False}]
    paras, _, hits = context.find(path, pats, stop, merge_sentences=False)
    for h in hits:
        n, line, s = h['line'], paras[h['para']][1], h['offset']
        start = max(line.rfind('. ', 0, s), line.rfind('"', 0, s), -1) + 1
        before = re.split(r'\s+', line[start:s].strip())[-8:]
        after = re.split(r'(?<=[.;"])\s', line[s:])[0].split()[:12]
        tail = ' '.join(w for w in before + after if w)
        keys = {w for w in WATCH if re.search(r'\b' + w + r's?\b', tail, re.I)}
        if out and out[-1][0] == n and (tail in out[-1][1] or out[-1][1] in tail):
            out[-1] = (n, max(tail, out[-1][1], key=len), keys | out[-1][2])
        else:
            out.append((n, tail, keys))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter')
    ap.add_argument('--height', type=float)
    ap.add_argument('--heights')
    ap.add_argument('--facts')
    ap.add_argument('--other', action='append', default=[])
    ap.add_argument('--prose', default='story/prose')
    a = ap.parse_args()
    h = a.height
    if a.heights:
        for line in open(a.heights, encoding='utf-8'):
            f = line.split('#')[0].split()
            if len(f) >= 3 and f[0] <= a.chapter <= f[1]:
                h = float(f[2])
    if h is None and not a.heights:
        ap.error('give --height or --heights')
    facts = [l.split('#')[0].strip() for l in open(a.facts, encoding='utf-8')] if a.facts else []
    facts = [f for f in facts if f]
    print(f'# Scale sheet, {a.chapter}\n')
    if h is None:
        print(f'- **Viewpoint:** no height for {a.chapter}; add a line to {a.heights}.')
    else:
        print(f'- **Viewpoint:** about {h:g} cm.')
        for o in a.other:
            name, cm = o.split('=')
            d = float(cm) - h
            print(f'- **{name}:** {float(cm):g} cm, {abs(d) / HAND:.1f} hands {"taller" if d > 0 else "shorter"}.')
        print('- **On the viewpoint\'s body:** ' + ', '.join(f'{k} {round(h * v)}' for k, v in BODY.items()) + ' cm.')
    print(f'- **A hand** is about {HAND} cm; ' + ('; '.join(facts) if facts else ADULT) + '.')
    print('- **The rule:** a size on the page is measured from the one who sees it, at the height above, '
          'and from the card of the object or creature; vary the reference from the chapters either side.\n')

    files = sorted(glob.glob(os.path.join(a.prose, '[0-9]*.md')))
    nums = [os.path.basename(f).split('-')[0] for f in files]
    if a.chapter not in nums:
        return
    i = nums.index(a.chapter)
    near = {}
    for j in list(range(max(0, i - 2), i)) + list(range(i + 1, min(len(files), i + 3))):
        for n, s, keys in phrases(files[j]):
            for k in keys:
                near.setdefault(k, []).append(f'{nums[j]}:{n}')
    print('## Size phrases on the page\n')
    hits = phrases(files[i])
    for n, s, keys in hits:
        rep = sorted({x for k in keys for x in near.get(k, [])})
        flag = f'  **repeat near:** {", ".join(rep)} ({", ".join(sorted(keys))})' if rep else ''
        print(f'- {a.chapter}:{n} "{s}"{flag}')
    if not hits:
        print('- none')


if __name__ == '__main__':
    sys.exit(main())
