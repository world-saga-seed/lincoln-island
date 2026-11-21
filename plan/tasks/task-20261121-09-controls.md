# Task: phase 7, the prompt-only controls

- **Objective:** the three chapters (01900, 01950, 02000) from Opus and from Gemini by prompts alone, with no cards, no ledger and no checks: one fixed prompt per chapter, the same for both models, frozen and committed before phase 8.
- **Context:** `BRIEF.md` phase 7; the author, 2026-11-21: "Write them the way someone who knows the book would prompt a model: the scene as settled, in a paragraph or two, not our ledger. Same prompt for both models." White's neighbouring chapters go in whole.
- **Related study:** none.
- **Region:** writes this task and its folder (`build_prompts.py`, the three prompts, and later the six replies with their records). Reads `texts/white-1876/18.md` to `21.md` and `texts/fr-1875/19.md`, `20.md`.
- **Wave:** none.
- **Start hash:** db2c80c 2026-11-21.
- **End hash:** (on close)
- **Status:** Executing: the prompts are approved and frozen (R1121-88); the runs are next.

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

## Resolution

(On close.)
