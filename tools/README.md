# Tools

Twelve small Python scripts. Standard library only (Python 3.8 or later), no paths written into them, everything set by arguments. They come with the clone, in `tools/`; run each from the book's top folder. Every script answers `--help`.

They give the method its mechanical checks: verdicts nobody argues with, under every judgment a critic or reader makes. **Try each one on a case it must catch before you trust a clean result from it** (a planted broken link, a planted banned word).

| Script | Does | Typical run |
|---|---|---|
| `links.py` | counts broken links (missing file or missing `#heading`) in every `.md` file; skips web links and links inside code | `python3 tools/links.py -v` |
| `cards.py` | checks every card's five-line head, builds each card folder's index table from the heads, finds cards by word, writes the subject index | `python3 tools/cards.py check` · `build` · `find tide` · `index` |
| `tells.py` | texture numbers for chapters (similes, "and" chains, negations, sentence spread, kicker endings) and a scan for banned words | `python3 tools/tells.py story/prose/00400-*.md --banned story/voice/banned.txt` |
| `repeats.py` | phrases of 5 to 8 words found in N or more chapters, and stock patterns counted per chapter | `python3 tools/repeats.py story/prose/0*.md --min-files 3 --narration` |
| `quotes.py` | checks that every quote in a report is really in the text it quotes | `python3 tools/quotes.py findings.md --in story/prose/00400-*.md` |
| `check_clean.py` | checks that a book cloned from the kit has nothing left of the example: no `example/`, no name from it, no link into it | `python3 tools/check_clean.py` |
| `refrains.py` | a volume's refrains counted per chapter from a watch list, and sentences repeated near word for word in three chapters or more | `python3 tools/refrains.py story/prose/01*.md --list story/voice/refrains.txt --batch 3` |
| `sounds.py` | every sound span (phonetic letters between slashes) with its line, speech or narration, earlier uses and forbidden symbols; flags a volume where the device is rare | `python3 tools/sounds.py story/prose/*.md --batch 3 --forbid "ɒ ː ɹ"` |
| `firstuse.py` | words a chapter is the first to use that the cards use too: setting words that may need setting up | `python3 tools/firstuse.py story/prose/*.md --batch 1` |
| `reading.py` | one chapter's reading list: its outline's and notes' links resolved to files and line ranges, the cards and sheets it names, the chapter before, the digest | `python3 tools/reading.py 00400 --step facts --digest story/volume/1-digest.md` |
| `aged.py` | outline, note and card lines that may carry an old draft into a redraft | `python3 tools/aged.py story/outline/00*.md --cutoff 2027-04-01 --retired story/prose/00*.md` |
| `epub.py` | builds an EPUB of chosen chapters, each paragraph tagged with its source line | `python3 tools/epub.py --title "Volume 1" --out build/v1.epub story/prose/00*.md` |

## Notes on each

**links.py.** `--root DIR` checks another folder; `--exclude 'existing/*'` skips files (repeatable). Exits 1 when anything is broken, so it can stop a script. A heading's anchor is made the way common markdown viewers make it: lower case, punctuation dropped, spaces to hyphens, a repeated heading gets `-1`, `-2`.

**cards.py.** Card folders are the subfolders of `--root` (default `world`). The head form and the table markers are at the top of the script. `check -v` also lists keywords the card's text already uses (a keyword should be a word a search would try that the card does *not* already contain).

**tells.py.** Prints a `knot` line under a file's numbers for each narration sentence of 35 words or more holding a semicolon. Measures **narration** only: text inside double quotes (straight or curly) is set aside. Stops at a line starting `## Notes` (change with `--stop`). The banned list: one word or phrase per line, matched as whole words, case ignored; `re:` starts a regular expression; `#` starts a comment. `--all-text` scans dialogue for banned words too. **There is no universal good value for any number:** run it on the writer's own pages and use their range.

**repeats.py.** Give the chapters in reading order. `--skip-title '^# Interlude'` leaves out pieces in another voice. `--tics FILE` replaces the built-in pattern list with your own (one per line: `name<TAB>regex`). Sort what it finds: motifs keep their words, habits keep the gesture, tics go.

**cards.py index.** Writes `world/INDEX.md` (with `--root DIR`, `DIR/INDEX.md`): every card under its name, the parts of its "what it is" and each keyword, every folder's README title, and every character sheet (`--sheets DIR`, default `story/notes/characters`), A to Z. Rebuild it whenever heads change; a missing subject is fixed by a keyword on the card's head, never in the index.

**refrains.py.** Give the volume's chapters so far, in order; `--batch K` makes the last K the batch, so a repeated run is reported only when it reaches the batch. Thresholds: `--volume-max` (default 8) and `--chapter-max` (default 3). The repeated runs skip six-word runs made mostly of small words and join overlapping runs into one. `repeats.py` finds shared phrases across any files; this one is aimed at a volume's refrains and at whole descriptions repeated.

**sounds.py.** Give the whole book so far, so a span can be checked against earlier chapters; `--batch K` reports the last K files and `--volume V` sets the last V files as the volume for the rarity flag. `--span` and `--chars` change what counts as a span, for a book with its own notation. A span inside double quotes counts as speech.

**firstuse.py.** `--cards DIR` (default `world`) is the folder whose words count as the setting's; `--min-cards N` (default 3) how many cards must use a word. Expect plain words among the hits; the critic sorts them.

**reading.py.** Run from the book's top folder; reads `story/outline/N-*.md`, `story/notes/N-*.md` and `story/prose/`. A linked file over `--large` words (default 1,500) is listed by the sections its links name, with line ranges. A card counts as named when the outline or notes use its name, a keyword from its head, or (for a two-word proper name) the first name. `--step` gives each critic its share.

**aged.py.** `--ledger DIR` (default `plan/settled/ledger`) dates ruling IDs from the ledger rows, so a line marked only with an old ruling counts as old. `--proposals` also flags every undated proposal. `--tsv OUT` writes one row per flagged line for the agents.

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
- `cards.py index --root example/world --sheets example/story/notes/characters`: 29 entries, each linking its card; `cards.py check` still 0 problems.
- `refrains.py` on the scene and two planted chapters, with a one-line watch list: the planted refrain counted 6 and flagged over the volume limit and in the chapter that showed it 4 times; a 25-word description planted in all three reported once, as one joined run.
- `sounds.py` on the same three, with `--forbid "ɒ ː ɹ ɚ ɝ ɛə"`: the planted span found, in speech, with its forbidden symbol; the volume flagged as rare.
- `firstuse.py` on the same three, `--min-cards 2`: the planted setting words found at their first use (a possessive read as its word); words of the scene itself not repeated as first uses in the later chapters.
- `tells.py` on a planted 62-word sentence with a semicolon: one knot line.
- `reading.py 00400` on the example: the outline and notes, the two cards the notes name without linking, the narrator's sheet, the arc outline listed as not to read; `--step habits` lists only the sheet's Habits section with its lines; a chapter with no outline exits with a message.
- `aged.py` on the example's outlines with a cutoff after its ledger day: the lines marked only by older rulings flagged as aged; a planted "from the draft" line linking a retired chapter flagged for both.
- `epub.py`: a numbered build with one drafted chapter and one placeholder, and a file-list build with `--kepub`; every XML part parsed as well-formed.
