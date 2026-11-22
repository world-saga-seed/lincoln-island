# Task: phase 7, the prompt-only controls

- **Objective:** the three chapters (01900, 01950, 02000) from Opus and from Gemini by prompts alone, with no cards, no ledger and no checks: one fixed prompt per chapter, the same for both models, frozen and committed before phase 8.
- **Context:** `BRIEF.md` phase 7; the author, 2026-11-21: "Write them the way someone who knows the book would prompt a model: the scene as settled, in a paragraph or two, not our ledger. Same prompt for both models." White's neighbouring chapters go in whole.
- **Related study:** none.
- **Region:** writes this task and its folder (`build_prompts.py`, the three prompts, and later the six replies with their records). Reads `texts/white-1876/18.md` to `21.md` and `texts/fr-1875/19.md`, `20.md`.
- **Wave:** none.
- **Start hash:** 1815e4b 2026-11-21.
- **End hash:** (on close)
- **Status:** Closed.

## Steps

1. **Draft the prompts** with `build_prompts.py`, from its fixed texts and the working texts as plain paste: paragraph numbers, page marks and plate captions stripped, Verne's footnotes kept.
2. **The author approves** them. Then they are frozen and committed.
3. **Run.** Opus in a fresh context, each prompt verbatim, one try. Gemini in the human's account, the same prompts. Record every reply verbatim, with the model, the date and the number of tries.
4. **Check** the six replies with the same checks and critics as phase 8, when phase 8 runs them.

## Acceptance

1. The three prompts are committed before any phase 8 draft exists.
2. The six replies are kept verbatim, each with its model, date and tries.

## Log

- 2026-11-21 Opened. Prompts built: 01900 7,805 words, 01950 5,185, 02000 8,199.
- 2026-11-21 Approved by the author as they stand (R1121-88) and frozen, with their checksums in SHA256SUMS. The author reports that the Gemini runs used these exact files.
- 2026-11-21 The Gemini replies were placed in `gemini/` by the author at 07:31 local, with their checksums; `sha256sum -c` passes. Their record is `gemini/RECORD.md`, as reported and unverified; the number of tries is not stated and has been asked.
- 2026-11-21 The Opus controls were run by the main session, one try each, 15:31 to 15:35 UTC, all ending end_turn. The record is `opus/RECORD.md`.
- 2026-11-21 The author: Gemini, one try each. The author's blind scoring of the Gemini three was placed in `scoring/`: two judge rubrics, twelve reader questions, the prompts as run and Gemini's replies. The three instruments pass `sha256sum -c`. Committed as it stands, and closed to the main session and every agent until the comparison (R1121-89). The main session checked only the file types, sizes and checksums, and did not read the contents.

## Resolution

The six controls were written, checked by the same critics as v1 (`checks/batch-paper.md`) and scored blind by the human (R1121-181; `task-20261121-16-the-book/blind-scores.md`). They are printed in the run's book.
- 2026-11-21 The checks begin (the author's word). Copies under neutral labels in `checks/`, prompts in `checks/prompts/`, the batch paper `checks/batch-paper.md`. Mechanical checks in.
- 2026-11-21 The checks are in: 16 critics on the six replies; findings in `checks/findings/`, the sum in `checks/batch-paper.md`. Not revised (controls).
