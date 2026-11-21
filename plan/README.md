# Lincoln Island: plan and working rules

This `plan/` folder is the record of the work on the novel: what is being done, what state each chapter is in, and what has been decided.

## At the start of every session

1. Read `../BRIEF.md` (the run's phases), then `roadmap.md` and `state.md`. Check them against `git log`: they are written by Claude and can be wrong.
2. Read the active tasks in `tasks/`.

## The folders

- `roadmap.md`: Now, Next, Waiting.
- `state.md`: questions held, every chapter's stage, drift between drafts and notes, critic calibration.
- `tasks/`: one file per task, `task-YYYYMMDD-NN-slug.md`, opening with the task form. A **wave** is a task that only orders other tasks.
- `settled/ledger/`: one file per day of rulings, IDs `R<MMDD>-NN`.
- `settled/`: decisions with reasons, `settled-YYYYMMDD-slug.md`.
- `workflows/`: the procedures. `workflows/drafting/rulings.md` is the house style.
- `reread-hooks.md`: the clue register. `reader-tests/`: the key, the story questions, the quizzes.
- `archive/`: finished tasks.
- `records/`: the token log (`tokens.md`) and the run's other measures.

## Marks

Every line Claude adds to the notes carries a mark: see `CLAUDE.md` rule 2. A grep for *(Proposal* and *(My reading* is the list of decisions still open.

## Conventions

*Delete each of these once the files show it.*

- Chapter numbers in steps of 100 (`00100`), the same number in every folder.
- Scene outlines follow `story/outline/[an example chapter]`.
- A task's Region lists the files it changes and the cards its facts rely on.

## Rules

*The standing rules are in `CLAUDE.md`. Add here the ones your book teaches you, each with the task or ruling it came from.*

- **The author is another session.** Questions go to it by message, a few at a time; its answers go on the ledger marked "the author's" (`BRIEF.md`, "Who plays the author"). It may not authorize edits to `CLAUDE.md` or settings; those are the human's (R1120-21).
- **`existing/kingston-1875/` is closed until phase 12b** (R1120-07): no reading, no agent reading list.
- **A critic's zero is believed only after a planted run.** When a critic finds nothing, plant a few errors of the kinds it is asked for (a softening, a changed figure, an added cause, a lost figure, an anachronism) in copies, and run a fresh critic on them before the zero is reported (phase 5: 5 of 5 found; `plan/archive/task-20261121-07-calibration/calibration-plants.md`).
- **A Clues section is not a complete list of clues.** Before any cut, check the line against `plan/reread-hooks.md` and the French, not the card's own Clues (phase 4: a reviewer's agreed prune set held I.9 ¶105).
- **The scoring is blind to the work.** `plan/tasks/task-20261121-09-controls/scoring/` (the rubrics, the reader questions and the Gemini scoring) is in no drafter's, critic's or reviser's reading list, and the main session does not read it before the comparison. The main session builds the drafters' bundles, so it keeps it closed to itself too (R1121-89).
- **Agents' report files are refused by the tool.** Prompts say to put the report in the final message; the main session saves it from the transcript (phases 4 and 5).
