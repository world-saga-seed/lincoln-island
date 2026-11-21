# Task: White made unabridged (R1121-144 to R1121-147), the pilot

- **Objective:** White's translation made whole: each chapter patched by its departures from the French, or rendered whole from the French in White's voice where he departs too far (R1121-144, R1121-145); first a pilot of one patch (I.5) and one re-render (III.14), measured before any more (R1121-147).
- **Context:** the author, 2026-11-21. The measure (R1121-145): the missing share, 1 − (White's words ÷ French words) ÷ 0.885, and discords per 1,000 French words; re-render at 20% or 8. The patch rule (R1121-146). Every chapter passes the critics before it counts as done.
- **Horizon:** CLAUDE.md rule 8 holds prose to the inserted chapter and its neighbours; the whole book waits for the human's own word (R1121-147). Until then the pilot's chapters stay in this task's folder, not in `story/prose/`.
- **Region:** writes this task and its folder. Reads `texts/fr-1875/`, `texts/white-1876/`, `texts/align/`, `story/voice/`, `plan/workflows/drafting/rulings.md`, the chapters' outlines and notes, and `world/`.
- **Wave:** none.
- **Start hash:** (at the first commit)
- **End hash:** (on close)
- **Status:** Planned: waits for the controls' checks (the author's order).

## Steps

1. **Patch I.5:** a fresh Opus patcher writes `pilot/patches-00500.tsv` from the French, White and `texts/align/05-discords.md`; `apply.py` applies it to White's text (every old text found once) into `pilot/00500-the-last-match-and-the-fire.md`.
2. **Re-render III.14:** a fresh Opus drafter, from `pilot/bundle-05600.md` (built by `build_bundle.py`), into `pilot/05600-the-new-ship-and-the-third-winter.md`.
3. **Mechanical checks:** tells.py with the banned list; spelling.py.
4. **Critics** (fresh Sonnet, the phase 8 prompts pointed at the files): facts and omission on each; voice on the two together.
5. **Measure:** tokens and time per chapter, by step; findings per chapter; the projection to the 60; put to the author.

## Acceptance

1. Each pilot chapter passes the critics (no break left standing) or its faults are listed for the author.
2. The measured cost and the projection are put to the author before any other chapter starts.

## Log

- 2026-11-21 Opened (R1121-144 to R1121-147). The bundle for III.14: 56 cards, 12,570 words. The prompts written.
