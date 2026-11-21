# Task: the clue register

- **Objective:** `plan/reread-hooks.md`: every clue *L'Île mystérieuse* plants, at every distance, each with its plants, payoff and the French words to keep; then every line pruned from the cards in phase 4 checked against it, and any that falls on a hook restored.
- **Context:** R1121-10 (hooks before phase 5); CLAUDE.md rule 11; `plan/workflows/series-critic.md` and `plan/templates/reread-hooks.md` (the form); the phase 4 close, which carried the pruned lines forward.
- **Related study:** `plan/archive/task-20261121-05-carding.md` (the lesson: a Clues section is not a complete list of a chapter's clues).
- **Region:** writes `plan/reread-hooks.md`, this task's folder, and (for restorations only) the cards in `world/`. Reads `story/notes/` (the Clues sections), `texts/fr-1875/`, `texts/align/` (White's cuts).
- **Wave:** none.
- **Start hash:** 0f89622, 2026-11-21.
- **End hash:** the commit "The clue register", 2026-11-21.
- **Status:** Done, 2026-11-21.

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

- 2026-11-21 The register built by one fresh Sonnet agent (197,266 tokens): 33 threads, 17 near puzzles, about 45 Clues lines set aside as not clues, each with a reason. Every incident of III.16 ¶65 has its row (H1 to H3, H6, H8 to H13). Eleven threads the book leaves open (among them the dugong's wound, the lead shot, the marked verse, the fire of 19 to 20 October, the apes' flight). The main session re-tested all 150 Keep quotes against their plant paragraphs: all resolve. White cuts or changes a plant in about twenty places beyond the two known (`report-register.md`).
- 2026-11-21 The pruned lines. A script took every fact line deleted from `world/` from a579947 to now and not on any card today: 292, of which 48 keep their quoted French on another card (reworded or moved), leaving 244. Of those, 44 cite a register plant or payoff, or a Clues paragraph (`pruned-flagged.md`). For 38 the paragraph is still carried by another line on some card. The main session read the six that are carried nowhere: five carry a clue and are restored with their quotes, in book order (Nab hiding his mishap over the turtle, II.1 ¶80, thread H28; Top taken for lost, I.6 ¶36; Top's bark as if his master were saved, I.7 ¶74; Spilett on the double disappearance, I.7 ¶18; Spilett's boat if land is near, I.13 ¶66); one is not (Nemo stopping the thanks, III.16 ¶34, which the III.16 Clues cite only for the footnote on the dates). The capybara of I.9 ¶105 is held on `lincoln-island.md`.

## Resolution

The clue register is `plan/reread-hooks.md`: 33 threads and 17 near puzzles, 150 French plants to keep, every one resolving. Against the acceptance: 1, every III.16 ¶65 incident has a row; 2, every Clues line is placed, or set aside with a reason, but for two the builder left for the author (the uprooted telegraph pole of III.6 ¶80 to ¶83, and the withheld talk of III.17); 3, every Keep quote resolves; 4, every pruned line on a hook is held by another card or restored (five restored). Cost 197,266 agent tokens. The builder's questions for the author are in `report-register.md`; three are put now, the rest wait for the work to lean on them (R1121-07).
