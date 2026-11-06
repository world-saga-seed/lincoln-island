# The register pass: the volume's repeats, fixed by attention

*Refinement. Add this when a volume is drafted and repeats.py finds shared phrases.*

A revision pass over a drafted volume, after every batch is settled. The per-chapter critics thin each chapter's own repeats, but they never see the volume at once. Read straight through, the same small devices recur, because drafts sit in the default register almost everywhere and stock phrases carry what variety there is. A scene that is all one register reads flat.

**Grade.** Mechanical for the count; a judgment for the fix.

## The steps

1. **Count.** `python3 tools/repeats.py story/prose/0*.md --min-files 3 --narration` over the volume's main thread (pieces in another voice are left out with `--skip-title`). It prints the stock patterns per chapter and every phrase of five to eight words found in three or more chapters. Save it as `repeats-before.md` in the task folder.
2. **Sort the repeats into three kinds,** in the task file:
   - **Motifs keep their exact words.** A deliberate device the reader should recognize: a refrain, a family saying, a line that comes back at the turns. Cap one whose count reads as wallpaper (once a chapter at most, and only where it marks something).
   - **Sheet habits keep the gesture and vary the words,** at most once a chapter. A habit carded in a set phrase is copied word for word by every drafter. The gesture is the habit, not the sentence.
   - **Tics are cut or replaced:** stock connective phrases and frames ("I did not know what", "for a long time", gaze chains, the "the way you…" simile that only decorates).
3. **Fix by register, per chapter.** Each chapter gets:
   - **one or two detail passages,** where something holds the narrator and the draft looked away: their trade, a tool in skilled hands, a person they love in danger, whatever the voice sheet says holds them. The narration slows and gives the thing itself, its parts and how it moves, from what the narrator knows. Never how it works, if the book does not explain;
   - **one gloss,** where something bores the narrator and the draft reports it in full: cut to a line, if no beat is lost;
   - **the tics in its rows** replaced, mostly by what the narrator is actually looking at.
   Small facts a detail passage needs are allowed, and logged on the Inventions list. No new beats.
4. **Figures.** While in each chapter, sort every simile and figure into **keep** (the narrator's own idiom, a thing they know), **convert** (it maps to a real detail of the scene and becomes a plain report), or **cut** (it is only pretty). Plain sentences stay plain.
5. **Check.** Re-run the count (`repeats-after.md`), `tells.py` with the banned list on every chapter, the keep list with `quotes.py`, one facts critic over the changed passages only, and the invention check on the log as its own small run.
6. **Report** in the task file: the counts before and after; each chapter's detail and gloss passages; the inventions to card.

**Agents.** At most two at once, none spawning its own. Each takes a run of chapters in story order and a named file list, works from a snapshot, and writes its own report.

## The landing check

After the register pass and before the volume is built for the writer's read:

1. List every settled beat for the volume's chapters: the outlines' *(Settled …)* lines, the ledger rows whose Applies to names these chapters, the offstage timelines' settled rows.
2. For each, find it on the page. Quote the line that lands it.
3. **A settled beat with no landing is not placed or dropped by an agent.** It goes to the writer, because the writer builds on beats they believe happened, and an absent beat is the hardest gap to see.

## Then

Build the volume for the writer's read (the `ereader` workflow), and run the interest check before the volume is accepted.
