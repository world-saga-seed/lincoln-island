# Tools

Seven small Python scripts. Standard library only (Python 3.8 or later), no paths written into them, everything set by arguments. They come with the clone, in `tools/`; run each from the book's top folder. Every script answers `--help`.

They give the method its mechanical checks: verdicts nobody argues with, under every judgment a critic or reader makes. **Try each one on a case it must catch before you trust a clean result from it** (a planted broken link, a planted banned word).

| Script | Does | Typical run |
|---|---|---|
| `links.py` | counts broken links (missing file or missing `#heading`) in every `.md` file; skips web links and links inside code | `python3 tools/links.py -v` |
| `cards.py` | checks every card's five-line head, builds each card folder's index table from the heads, finds cards by word | `python3 tools/cards.py check` · `build` · `find tide` |
| `tells.py` | texture numbers for chapters (similes, "and" chains, negations, sentence spread, kicker endings) and a scan for banned words | `python3 tools/tells.py story/prose/00400-*.md --banned story/voice/banned.txt` |
| `repeats.py` | phrases of 5 to 8 words found in N or more chapters, and stock patterns counted per chapter | `python3 tools/repeats.py story/prose/0*.md --min-files 3 --narration` |
| `quotes.py` | checks that every quote in a report is really in the text it quotes | `python3 tools/quotes.py findings.md --in story/prose/00400-*.md` |
| `check_clean.py` | checks that a book cloned from the kit has nothing left of the example: no `example/`, no name from it, no link into it | `python3 tools/check_clean.py` |
| `epub.py` | builds an EPUB of chosen chapters, each paragraph tagged with its source line | `python3 tools/epub.py --title "Volume 1" --out build/v1.epub story/prose/00*.md` |

## Notes on each

**links.py.** `--root DIR` checks another folder; `--exclude 'existing/*'` skips files (repeatable). Exits 1 when anything is broken, so it can stop a script. A heading's anchor is made the way common markdown viewers make it: lower case, punctuation dropped, spaces to hyphens, a repeated heading gets `-1`, `-2`.

**cards.py.** Card folders are the subfolders of `--root` (default `world`). The head form and the table markers are at the top of the script. `check -v` also lists keywords the card's text already uses (a keyword should be a word a search would try that the card does *not* already contain).

**tells.py.** Measures **narration** only: text inside double quotes (straight or curly) is set aside. Stops at a line starting `## Notes` (change with `--stop`). The banned list: one word or phrase per line, matched as whole words, case ignored; `re:` starts a regular expression; `#` starts a comment. `--all-text` scans dialogue for banned words too. **There is no universal good value for any number:** run it on the writer's own pages and use their range.

**repeats.py.** Give the chapters in reading order. `--skip-title '^# Interlude'` leaves out pieces in another voice. `--tics FILE` replaces the built-in pattern list with your own (one per line: `name<TAB>regex`). Sort what it finds: motifs keep their words, habits keep the gesture, tics go.

**quotes.py.** Reads quotes from lines like `- quote: the exact words`; with `--backticks`, also from every backticked span (for fold-back lists and card extracts; run it on a file or section that holds only quotes in backticks, or every backticked command will be checked too). Matching ignores spacing, curly against straight quotes, and `*` and `_`. Exits 1 if any quote is missing, and prints "0 quotes found" and exits 1 when the report holds none, since that usually means the quotes are not in the `- quote:` form.

**check_clean.py.** Run it once, after deleting `example/` from a fresh clone; it must print `clean`. `--root DIR` checks another folder. Each hit is listed as `file:line` with what it found; exits 1 on any hit. The example's names (title, people, places, chapter slugs) are written into the script, with a comment on how to rebuild the list if the example changes; the script does not scan itself.

**epub.py.** Its options and how to use the build are in [plan/workflows/ereader.md](../plan/workflows/ereader.md#build). No cover image (that would need an image library); readers show the title page.

## Tested

Each script was run on the kit's `example/` folder:

- `links.py --root example`: 0 broken; a planted broken link was found.
- `cards.py check --root example/world`: stale tables found before `build`, then 0 problems; `find tide` returns the two cards whose heads hold it, then the one whose text does.
- `tells.py` on the scene and the writer's sample, with the banned list: numbers for both, 0 hits; on a planted file, all three planted phrases found, and the same phrase inside dialogue left alone.
- `repeats.py` on the sample and the scene: one stock pattern counted; on two copies of one file, the shared phrases found.
- `quotes.py` on the facts critic's report against draft 1: 2 of 3 resolve, the invented quote reported missing (exit 1); on the keep list against draft 2: 6 of 6; on a file with no quote lines: "0 quotes found" (exit 1).
- `check_clean.py`: in the kit, fails on `example/` (exit 1); on a copy with `example/` deleted, `clean`; a planted example name and a planted link into `example/` each found.
- `epub.py`: a numbered build with one drafted chapter and one placeholder, and a file-list build with `--kepub`; every XML part parsed as well-formed.
