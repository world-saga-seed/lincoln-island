# Logic check: an arc against its own notes

*Refinement. Add this when the arc turns on timing, travel or who-knows-what, or an outline already broke on a date or a cause.*

Checks a pitched or outlined arc for logic flaws: impossible timing, knowledge a character could not have, causes that do not connect, rules broken, motives that do not hold. Run it when an arc's frames are settled, before it is outlined chapter by chapter, so the outlines do not inherit a flaw.

**Grade.** A judgment. Agents find; the writer decides. Nothing here edits a note.

## Dimensions

- **Time:** calendars, seasons, ages, travel, the order of events.
- **Knowledge and causality:** who knows what, and when; how news travels; whether each beat has a cause (chance with a cause, not convenience).
- **The setting's rules:** every beat against the cards and topic files: money, law, travel, the trades, how any special element works.
- **Character and story:** motives, the narrator's reach (what they can see), the book's own rules, tension and density, the hand-offs from the arc before.

## The loop

1. **Open a task** naming the arc, its pitch, the outline sections that settle it, and the start hash.
2. **Fresh agents, one per dimension,** at most two at a time, each writing only its own file.
3. **Verify** every finding: quotes resolve; the flaw survives a fair reading of both sides. Merge duplicates; drop what is held, open or logged as drift.
4. **Present to the writer** one at a time, most severe first, with context and a recommendation, the plain fix first.
5. **Fold back** the writer's calls; log the run; add lessons here.

## Prompt

> You are checking one dimension of a novel's arc for logic flaws, in the folder {REPO}. Every file is read-only except your output file. Run no git commands; do not launch agents. Read `README.md`, `plan/README.md`, the arc's pitch {PITCH}, the outline sections {SECTIONS}, and the cards they link that bear on your dimension. Your dimension: {DIMENSION}. Write only {OUTPUT}. Find places where the arc, as settled, cannot work or strains belief: a contradiction between two settled lines, an impossibility, a missing cause, a knowledge leak, a rule broken. For each: a title; severity (**breaks**: cannot work as written; **strains**: works only with a line the notes lack; **nit**); both sides quoted with file, line and mark; why it fails, in two or three sentences; two or three fixes, the plain one first, with your recommendation. Skip anything held, open, or logged as drift in `plan/state.md`, and anything that is only wording. Do not invent lore to fix a flaw; say what the notes would need. At most fifteen findings, most severe first. Verify every quote with `grep -F`.

## Lessons

- **A cluster that turns on a character with no sheet** waits for that sheet.
- **The writer overrules where the notes are silent.** Flag findings that rest on silence, not conflict, and expect the writer's own answer there.
- **Verify quotes across the whole folder,** not one file and line; line numbers drift.
- **Fold an aside at once.** A rule the writer gives in passing goes on the ledger the moment it is given.
