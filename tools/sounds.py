#!/usr/bin/env python3
"""Sound spans on the page, held to the book's convention.

Some books write a sound the narrator cannot yet spell: a foreign word in
phonetic letters (/ˈtʃɑklət/), a coined name before it is learned. Such a device
has rules (who may say it, when it turns to italics, then plain words; which
accent it is transcribed in), and it breaks in two ways a chapter critic misses:
a stray symbol from another accent or system, and a volume where the device is
so rare that a reader takes the one span for a typesetting slip.

Usage:
  python3 tools/sounds.py FILE [FILE ...] [--batch K] [--volume V] [--forbid SYMBOLS]
                          [--span REGEX] [--chars CHARS] [--stop REGEX]

  FILE            the book's chapters so far, in reading order (the whole book,
                  so a span can be checked against earlier chapters)
  --batch K       report spans only in the last K files (default: all)
  --volume V      the last V files are the volume, for the rarity flag
                  (default: the batch)
  --forbid S      symbols that break the convention, separated by spaces
                  (for General American IPA: "ɒ ː ɹ ɚ ɝ ɛə")
  --span REGEX    what a span looks like (default: text between slashes)
  --chars CHARS   a span counts only if it holds one of these characters
                  (default: the common IPA letters and stress marks)
  --stop REGEX    stop reading a file at a line matching REGEX (default "^## Notes")

Prints each span in the batch with its file and line, whether it falls inside
speech or in narration, how many earlier chapters carry the same span, and any
forbidden symbol in it; then how many chapters of the volume carry a span, with
a flag when that is one or none. Give it to the voice critic with the rule from
the voice sheet: a span in narration, or one for a word that already reached
italics or plain words on an earlier page, is a candidate.
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import context  # noqa: E402  (the shared reader: paragraphs, dialogue, line and column)

IPA = 'ɪʊəɛɔæɑʌɜɹʃʒθðŋˈˌːɐɒʔɾɚɝ'


def spans(path, span, chars, stop):
    """Each sound span in a file: (line, span, in speech), from context's reader."""
    pats = context.compile_patterns([{'label': 'span', 'rx': span}], flags=0)
    _, _, hits = context.find(path, pats, stop, merge_sentences=False)
    return [(h['line'], h['match'], h['quoted']) for h in hits if chars & set(h['match'])]


def main():
    ap = argparse.ArgumentParser(description="Sound spans on the page, held to the book's convention.")
    ap.add_argument('files', nargs='+', help='the chapters so far, in reading order')
    ap.add_argument('--batch', type=int, default=0)
    ap.add_argument('--volume', type=int, default=0)
    ap.add_argument('--forbid', default='')
    ap.add_argument('--span', default=r'/[^/\s][^/\n]{0,40}?/')
    ap.add_argument('--chars', default=IPA)
    ap.add_argument('--stop', default=r'^## Notes')
    a = ap.parse_args()
    chars, forbid = set(a.chars), a.forbid.split()
    k = a.batch or len(a.files)
    batch = set(a.files[-k:])
    volume = set(a.files[-(a.volume or k):])
    seen, vol, out = {}, set(), []
    for pos, f in enumerate(a.files):
        name = os.path.basename(f)[:-3]
        for i, sp, inside in spans(f, a.span, chars, a.stop):
            if f in volume:
                vol.add(f)
            if f in batch:
                prior = len({c for c in seen.get(sp, set()) if c < pos})
                bad = [s for s in forbid if s in sp]
                out.append(f"- {name}:{i} {sp} {'in speech' if inside else '**in narration**'}; "
                           f"earlier chapters: {prior}" + (f"; **forbidden: {' '.join(bad)}**" if bad else ''))
            seen.setdefault(sp, set()).add(pos)
    print('# Sound spans\n')
    print('\n'.join(out) or 'None.')
    print(f'\nSpans in the volume: in {len(vol)} chapter(s).'
          + (' **Rare: check each span reads as a sound, not a slip.**' if len(vol) <= 1 else ''))


if __name__ == '__main__':
    main()
