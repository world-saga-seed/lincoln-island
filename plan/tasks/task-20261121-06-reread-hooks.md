# Task: the clue register

- **Objective:** `plan/reread-hooks.md`: every clue *L'Île mystérieuse* plants, at every distance, each with its plants, payoff and the French words to keep; then every line pruned from the cards in phase 4 checked against it, and any that falls on a hook restored.
- **Context:** R1121-10 (hooks before phase 5); CLAUDE.md rule 11; `plan/workflows/series-critic.md` and `plan/templates/reread-hooks.md` (the form); the phase 4 close, which carried the pruned lines forward.
- **Related study:** `plan/tasks/task-20261121-05-carding.md` (the lesson: a Clues section is not a complete list of a chapter's clues).
- **Region:** writes `plan/reread-hooks.md`, this task's folder, and (for restorations only) the cards in `world/`. Reads `story/notes/` (the Clues sections), `texts/fr-1875/`, `texts/align/` (White's cuts).
- **Wave:** none.
- **Start hash:** 0f89622, 2026-11-21.
- **End hash:** (on close)
- **Status:** Running.

## Steps

1. **Plan.** One fresh Sonnet agent builds the register from (a) the Clues sections of the 62 notes (`clues-all.md`, a reading copy; the notes are the source), (b) III.16 ¶65, the book's own list of the incidents Nemo explains, the payoff of the main thread, (c) White's two cut clues held in phase 3 (I.9 ¶105, the capybara "voyait-il des hommes pour la première fois"; III.9 ¶41, Ben Joyce), (d) any other cut in `texts/align/*-discords.md` that removes a line the Clues name. Each row: the thing, named neutrally (for the series critic's blind pass); its plants (chapter and ¶); its payoff (chapter and ¶, or "none: left open"); its distance (chapters, part, book); the exact French words to keep. Puzzles answered within the same chapter or the next are listed in a short second table, so the main table stays the book's threads.
2. **Study.** The main session reads the register against III.16 ¶65 and the Clues: every incident of ¶65 a row; every Clues line in some row or the second table.
3. **Execute.** A script lists every line pruned from `world/` in phase 4 (wave 3's `pruned-w3.json`; the other waves from the wave commits' diffs; the check's three deletions), with its cites; any whose cite falls on a register plant or a Clues paragraph is read by the main session and restored if it carries the clue.
4. **Check:** every Keep quote resolves (`tools/quotes.py`); `links.py` prints 0.
5. **Final report** in Resolution.

## Acceptance

1. Every incident of III.16 ¶65 has a row, with its plants.
2. Every line of every Clues section is in a row or the second table, or is listed as not a clue, with the reason.
3. Every Keep quote resolves in the cited paragraph.
4. Every pruned line on a hook is restored, or its loss logged with the reason.

## Log

- 2026-11-21 Opened (R1121-10).

## Resolution

(On close.)
