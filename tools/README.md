# Tools

Eighteen small Python scripts. Standard library only (Python 3.8 or later), no paths written into them, everything set by arguments. They come with the clone, in `tools/`; run each from the book's top folder. Every script answers `--help`.

They give the method its mechanical checks: verdicts nobody argues with, under every judgment a critic or reader makes. **Try each one on a case it must catch before you trust a clean result from it** (a planted broken link, a planted banned word).

Every script is tested as code, on a planted case in the kit's `example/` (the list is at the end). Only `scale.py` has also been proven on a real book's prose, against planted faults and in a sweep; the rest are proven as code, not yet as craft.

They come in three levels. Start with the basic ones; add the refinement checks when a draft stands; take a speciality tool only when your book needs it.

### Basic

*For every book and every chapter: the links hold, the cards are in form, each run's reading list, quotes that are really in the text, and an ereader build to read from.*

| Script | Does | Typical run |
|---|---|---|
| `links.py` | counts broken links (missing file or missing `#heading`) in every `.md` file; skips web links and links inside code | `python3 tools/links.py -v` |
| `cards.py` | checks every card's five-line head, builds each card folder's index table from the heads, finds cards by word, writes the subject index | `python3 tools/cards.py check` · `build` · `find tide` · `index` |
| `reading.py` | one chapter's reading list: its outline's and notes' links resolved to files and line ranges, the cards and sheets it names, the chapter before, the digest | `python3 tools/reading.py 00400 --step facts --digest story/volume/1-digest.md` |
| `quotes.py` | checks that every quote in a report is really in the text it quotes | `python3 tools/quotes.py findings.md --in story/prose/00400-*.md` |
| `epub.py` | builds an EPUB of chosen chapters, each paragraph tagged with its source line | `python3 tools/epub.py --title "Volume 1" --out build/v1.epub story/prose/00*.md` |
| `check_clean.py` | checks that a book cloned from the kit has nothing left of the example: no `example/`, no name from it, no link into it | `python3 tools/check_clean.py` |

### Refinement

*For the prose over a volume: the model's texture and habit words, phrases and refrains repeated across chapters, setting words used before they are set up, and old drafts carried into a redraft. Run them once a draft stands, before the critics.*

| Script | Does | Typical run |
|---|---|---|
| `tells.py` | texture numbers for chapters (similes, "and" chains, negations, sentence spread, kicker endings) and a scan for banned words | `python3 tools/tells.py story/prose/00400-*.md --banned story/voice/banned.txt` |
| `repeats.py` | phrases of 5 to 8 words found in N or more chapters, and stock patterns counted per chapter | `python3 tools/repeats.py story/prose/0*.md --min-files 3 --narration` |
| `refrains.py` | a volume's refrains counted per chapter from a watch list, and sentences repeated near word for word in three chapters or more | `python3 tools/refrains.py story/prose/01*.md --list story/voice/refrains.txt --batch 3` |
| `stutters.py` | the same short phrase twice within a few paragraphs of one chapter, a capped frame ("as if", "the way X") twice in a paragraph, and the chapter's count against each cap | `python3 tools/stutters.py story/prose/00400-*.md --clues plan/reread-hooks.md` |
| `firstuse.py` | words a chapter is the first to use that the cards use too: setting words that may need setting up | `python3 tools/firstuse.py story/prose/*.md --batch 1` |
| `aged.py` | outline, note and card lines that may carry an old draft into a redraft | `python3 tools/aged.py story/outline/00*.md --cutoff 2027-04-01 --retired story/prose/00*.md` |

### Speciality

*For some books only, by what the book does: a viewpoint whose size is not an adult's, sounds written out in letters, a chapter's beats marked by source, several viewpoint heads, a narrator who knows less or believes wrongly, and a change sent back to the kit.*

| Script | Does | Typical run |
|---|---|---|
| `scale.py` | the viewpoint's height and body landmarks at a chapter, and every size phrase on its page, with repeats of the crowd-from-below view within two chapters marked | `python3 tools/scale.py 00400 --height 139 --other Ada=141 --prose story/prose` |
| `sounds.py` | every sound span (phonetic letters between slashes) with its line, speech or narration, earlier uses and forbidden symbols; flags a volume where the device is rare | `python3 tools/sounds.py story/prose/*.md --batch 3 --forbid "ɒ ː ɹ"` |
| `attribution.py` | unlabeled paragraphs for a blind attribution test in a book with several viewpoint heads, and the key to score it | `python3 tools/attribution.py story/prose/03*.md --heads "03100-x.md:1-40=Ada,03100-x.md:41-200=Ben" --out attribution.md --key key.md` |
| `knowledge.py` | the knowledge-guard entries in force at one chapter (what each narrating head knows, believes wrongly and does not know), for the drafter's and critics' briefs | `python3 tools/knowledge.py 00500 --out tmp/knowledge-00500.md` |
| `markup.py` | a chapter as local HTML coloured by whose beat each passage carries (keyframe, assisted, tween), the clues highlighted, lore underlined, every source in a tooltip, from the finds of cheap locators ([markup](../plan/workflows/markup.md)) | `python3 tools/markup.py items 00400` · `render 00400` |
| `check_leak.py` | checks that a change meant for the kit carries nothing of your book: names from its cards and sheets, runs of words from its prose and notes, email addresses ([CONTRIBUTING](../CONTRIBUTING.md)) | `git diff upstream/master \| python3 tools/check_leak.py --book ../my-book` |

## Notes on each

**links.py.** `--root DIR` checks another folder; `--exclude 'existing/*'` skips files (repeatable). Exits 1 when anything is broken, so it can stop a script. A heading's anchor is made the way common markdown viewers make it: lower case, punctuation dropped, spaces to hyphens, a repeated heading gets `-1`, `-2`.

**cards.py.** Card folders are the subfolders of `--root` (default `world`). The head form and the table markers are at the top of the script. `check -v` also lists keywords the card's text already uses (a keyword should be a word a search would try that the card does *not* already contain).

**tells.py.** Prints a `knot` line under a file's numbers for each narration sentence of 35 words or more holding a semicolon. Measures **narration** only: text inside double quotes (straight or curly) is set aside. Stops at a line starting `## Notes` (change with `--stop`). The banned list: one word or phrase per line, matched as whole words, case ignored; `re:` starts a regular expression; `#` starts a comment. `--all-text` scans dialogue for banned words too. **There is no universal good value for any number:** run it on the writer's own pages and use their range.

**repeats.py.** Give the chapters in reading order. `--skip-title '^# Interlude'` leaves out pieces in another voice. `--tics FILE` replaces the built-in pattern list with your own (one per line: `name<TAB>regex`). Sort what it finds: motifs keep their words, habits keep the gesture, tics go.

**cards.py index.** Writes `world/INDEX.md` (with `--root DIR`, `DIR/INDEX.md`): every card under its name, the parts of its "what it is" and each keyword, every folder's README title, and every character sheet (`--sheets DIR`, default `story/notes/characters`), A to Z. Rebuild it whenever heads change; a missing subject is fixed by a keyword on the card's head, never in the index.

**refrains.py.** Give the volume's chapters so far, in order; `--batch K` makes the last K the batch, so a repeated run is reported only when it reaches the batch. Thresholds: `--volume-max` (default 8) and `--chapter-max` (default 3). The repeated runs skip six-word runs made mostly of small words and join overlapping runs into one. `repeats.py` finds shared phrases across any files; this one is aimed at a volume's refrains and at whole descriptions repeated.

**stutters.py.** The other repeat tools see a volume; this one sees a page. It lists every run used again within `--window` words (default 250): three words with two that are not filler, or longer runs. A run used `--standing` times or more in the chapter (default 6) is a name or a tag and listed apart. `--clues` takes your clue register or a chapter's planted lines and marks a hit whose words are in one. It finds candidates; you judge them, and rerun after the fix.

**sounds.py.** Give the whole book so far, so a span can be checked against earlier chapters; `--batch K` reports the last K files and `--volume V` sets the last V files as the volume for the rarity flag. `--span` and `--chars` change what counts as a span, for a book with its own notation. A span inside double quotes counts as speech.

**firstuse.py.** `--cards DIR` (default `world`) is the folder whose words count as the setting's; `--min-cards N` (default 3) how many cards must use a word. Expect plain words among the hits; the critic sorts them.

**reading.py.** Run from the book's top folder; reads `story/outline/N-*.md`, `story/notes/N-*.md` and `story/prose/`. A linked file over `--large` words (default 1,500) is listed by the sections its links name, with line ranges. A card counts as named when the outline or notes use its name, a keyword from its head, or (for a two-word proper name) the first name. `--step` gives each critic its share.

**aged.py.** `--ledger DIR` (default `plan/settled/ledger`) dates ruling IDs from the ledger rows, so a line marked only with an old ruling counts as old. `--proposals` also flags every undated proposal. `--tsv OUT` writes one row per flagged line for the agents.

**attribution.py.** `--heads` names whose head each stretch of lines is in; a file with one head throughout is given as `file.md=Name`. It takes at least five paragraphs from each head that has them, then fills to `--count`. The key goes in a file the reader is never given. The prompt and how to score it are in [the attribution test](../plan/workflows/drafting/prompts/attribution.md).

**knowledge.py.** Reads every guard in `story/voice/knowledge/` ([the template](../plan/templates/knowledge.md)), or only `--heads`. An entry is in force from its `*From* NNNNN` (from the start when it has none) through its `*until* NNNNN`; at its until chapter it is printed marked as turning there. An Open section is skipped. One guard per head with spans, never a copy per chapter: when a belief changes, one line changes.

**quotes.py.** Reads quotes from lines like `- quote: the exact words`; with `--backticks`, also from every backticked span (for fold-back lists and card extracts; run it on a file or section that holds only quotes in backticks, or every backticked command will be checked too). Matching ignores spacing, curly against straight quotes, and `*` and `_`. Exits 1 if any quote is missing, and prints "0 quotes found" and exits 1 when the report holds none, since that usually means the quotes are not in the `- quote:` form.

**check_leak.py.** Run from your fork of the kit, never from the book. It reads a unified diff (standard input, or `--diff FILE`) and checks only the lines the change adds. Names are the proper names in the headings of the book's cards (`world/`) and character sheets (`story/notes/characters/`), matched as whole words, case kept; a shared run is `--words` words (default 8) found in the book's `story/`, `world/` or `existing/` text. A hit is not always a leak (a word that is also a name, a stock phrase): Claude reads each one with the writer. Exits 1 on any hit, prints `clean` otherwise.

**check_clean.py.** Run it once, after deleting `example/` from a fresh clone; it must print `clean`. `--root DIR` checks another folder. Each hit is listed as `file:line` with what it found; exits 1 on any hit. The example's names (title, people, places, chapter slugs) are written into the script, with a comment on how to rebuild the list if the example changes; the script does not scan itself.

**epub.py.** Its options and how to use the build are in [plan/workflows/ereader.md](../plan/workflows/ereader.md#build). No cover image (that would need an image library); readers show the title page.

## Tested

Each script was run on the kit's `example/` folder:

- `links.py --root example`: 0 broken; a planted broken link was found.
- `cards.py check --root example/world`: stale tables found before `build`, then 0 problems; `find tide` returns the two cards whose heads hold it, then the one whose text does.
- `tells.py` on the scene and the writer's sample, with the banned list: numbers for both, 0 hits; on a planted file, all three planted phrases found, and the same phrase inside dialogue left alone.
- `repeats.py` on the sample and the scene: one stock pattern counted; on two copies of one file, the shared phrases found.
- `quotes.py` on the facts critic's report against draft 1: 2 of 3 resolve, the invented quote reported missing (exit 1); on the keep list against draft 2: 6 of 6; on a file with no quote lines: "0 quotes found" (exit 1).
- `check_leak.py`: on a diff adding a line that names a person and a place from the example's cards, and an email address, with `--book example`, the full name, the place and the email found; a line about critics found clean.
- `check_clean.py`: in the kit, fails on `example/` (exit 1); on a copy with `example/` deleted, `clean`; a planted example name and a planted link into `example/` each found.
- `cards.py index --root example/world --sheets example/story/notes/characters`: 29 entries, each linking its card; `cards.py check` still 0 problems.
- `refrains.py` on the scene and two planted chapters, with a one-line watch list: the planted refrain counted 6 and flagged over the volume limit and in the chapter that showed it 4 times; a 25-word description planted in all three reported once, as one joined run.
- `stutters.py` on the scene: 3 hits; on a copy with a ten-word run planted again 96 words later and "as if" twice in one paragraph, both found, and a hit marked `clue?` when its words were in the `--clues` file.
- `sounds.py` on the same three, with `--forbid "ɒ ː ɹ ɚ ɝ ɛə"`: the planted span found, in speech, with its forbidden symbol; the volume flagged as rare.
- `firstuse.py` on the same three, `--min-cards 2`: the planted setting words found at their first use (a possessive read as its word); words of the scene itself not repeated as first uses in the later chapters.
- `tells.py` on a planted 62-word sentence with a semicolon: one knot line.
- `reading.py 00400` on the example: the outline and notes, the two cards the notes name without linking, the narrator's sheet, the arc outline listed as not to read; `--step habits` lists only the sheet's Habits section with its lines; a chapter with no outline exits with a message.
- `aged.py` on the example's outlines with a cutoff after its ledger day: the lines marked only by older rulings flagged as aged; a planted "from the draft" line linking a retired chapter flagged for both.
- `attribution.py` on a two-head draft with a paragraph planted in the wrong head's voice: 15 paragraphs, 10 and 5, the planted one among them, the key holding each line and head. A cold reader given the file put all 15 in the right head and named the planted one as wrong for its head.
- `knowledge.py` on the example's guard at 00100, 00500 and 00600: 6, 8 and 6 entries, the right ones; at 00500 the belief and the not-known that end there marked as turning.
- `markup.py` on the example's 00400 with four planted finds: 20 items listed (8 keyframe sources, 12 assisted); three finds placed with their colours, the planted one with words not on the page dropped and listed.
- `epub.py`: a numbered build with one drafted chapter and one placeholder, and a file-list build with `--kepub`; every XML part parsed as well-formed.
