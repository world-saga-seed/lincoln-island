# Task: phase 5, the calibration

- **Objective:** render a sample of the passages White cut, changed or softened, from the cards and the French, set each beside White's and the French, and log every way a render departs from the French that White did not, as a candidate tell; and choose the voice chapter.
- **Context:** `BRIEF.md` phase 5; R1121-12 (the author's picks), R1121-13 (Verne's politics), R1121-14 (Webster 1864), R1121-15 (no stubs); R1120-29 (English only), R1120-33 (discords side by side).
- **Related study:** `texts/align/` (the 1,333 discords; `SUMMARY.md`), `plan/reread-hooks.md`.
- **Region:** writes this task's folder and, for R1121-15, the stub cards the sample rests on. Reads `texts/fr-1875/`, `texts/white-1876/` (the voice chapter only, for the drafters), `world/`, `story/outline/`, `existing/webster-1864/` (for the period check).
- **Wave:** none.
- **Start hash:** a0a2477, 2026-11-21.
- **End hash:** the commit "Phase 5: closed", 2026-11-21.
- **Status:** Closed, 2026-11-21.

## Steps

1. **The sample** (`calibration/sample.md`): the author's six picks (A1 to A6), twelve of White's cuts drawn at random, two from each sixth of the book (S1 to S12, seed 20261127), and the two other softenings that touch Verne's politics (P1, P2): 20 passages, 3,473 French words. A6 is I.15 ¶26, not I.5 ¶11 (R1121-17), since I.5 is the voice chapter and a drafter that has read White's I.5 cannot test whether it adds what White added there.
2. **The stubs** (R1121-15): the six stub cards the sampled paragraphs cite are built into full cards first (red-worms, dwarf-acacia, tetras-lines, greenwich, sulphate-furnace, willow-bark), by one fresh Sonnet carder.
3. **The voice chapter** *(Settled R1121-16.)*: I.5, White's least altered against the French (7 discords in 3,085 words, 2.27 a thousand; next I.9 at 3.02, I.7 at 3.05). Copied unchanged to `story/voice/samples/` (done).
4. **The renders** *(Settled R1121-18; cap 3 M, R1121-19.)*: fresh Opus agents, the model the method's drafter and the Opus control will use, two at a time, each given a few passages: the French of the passage with a paragraph either side, the chapter's outline, the cards it names, and White's I.5 as the voice sample; never White's own rendering of the passage. A6 gets the French alone.
5. **The checks:** a facts critic (each render against the French: what is added, lost, changed); a period critic (words and senses later than 1876, checked against Webster 1864, whose rough OCR means a miss is not proof; and for A1, science Verne could not have known: the Coriolis effect by name, ocean conveyor belts, the circumpolar current); the politics of A4, P1 and P2 against the French (R1121-13). Each finding quotes the render and the French (rule 10).
6. **The tells:** each departure from the French that White did not make, logged as a candidate tell with its quotes, in `calibration/tells.md`, for the kit's tell lists.
7. **Close.**

## Acceptance

1. Every passage rendered; every render set beside the French and White.
2. Every finding quotes the render and the French; quotes resolve.
3. The candidate tells logged, each with its quotes and kind.
4. The voice chapter approved by the author (R1121-16: done).
5. The tokens in `plan/records/tokens.md`.

## Log

- 2026-11-21 Opened (R1121-12 to R1121-15). The sample drawn. Six stubs found in the sampled paragraphs.

- 2026-11-21 The author approved the plan: I.5 the voice chapter (R1121-16), A6 I.15 ¶26 (R1121-17), Opus renders and Sonnet critics (R1121-18), a 3 M cap (R1121-19). White's I.5 copied unchanged to `story/voice/samples/white-I.5.md`.

- 2026-11-21 The stubs built (68,274 tokens): six cards, no Open lines.
- 2026-11-21 The bundles (`bundles/`, by script): the French with a paragraph either side, the outline, the card lines citing the passage; A6 the French alone; no White.
- 2026-11-21 The renders, two fresh Opus agents (127,797 and 132,952 tokens): all 20. The tool refused both reports; saved from their final messages.
- 2026-11-21 The checks. `side.py` set each render beside the French and White (`side/`). `period_check.py` flagged 14 words in neither White nor Webster 1864 (`period-flags.md`). The period critic (55,394 tokens): no word, sense or science later than 1876; the British "-our" spelling against White's American; the names. The facts and politics critic (65,952 tokens): no finding in 20 passages. A zero from an uncalibrated critic proves little, so five errors were planted in copies (`side-cal/`, `calibration-plants.md`: a softening, a changed figure, an added cause, a lost figure, an anachronism) and a fresh critic run on them (63,893 tokens): all five found, nothing else flagged. The renders' own disclosed small departures sit below that critic's line by design. The candidate tells: `tells.md`.

## Resolution

Phase 5 is done but for one question. The 20 renders, from the cards and the French in White's voice, depart from the French in no way a calibrated critic catches, and use no English or science later than 1876. They keep Verne's politics where White softens them and his figures where White changes them, and the from-the-French-alone render did not add White's addition. The candidate tells are one strong (British "-our" spelling, where White is American throughout) and five weak (small words added or dropped for idiom, each named by the renderer). The voice chapter is White's I.5 (R1121-16). Cost: about 0.51 M agent tokens, against the 3 M cap (R1121-19).

Against the acceptance: 1, every passage rendered and set beside the French and White; 2, every finding quotes the render and the French, and the quotes resolve; 3, the tells logged with quotes and kind; 4, the voice chapter approved (R1121-16); 5, the tokens logged.

The author ruled the two questions it left: the page uses White's names, the cards the French (R1121-20); the page takes White's American spelling, the "-our" forms banned (R1121-21). Both are in `story/voice/white.md` and `story/voice/banned.txt`, which flags none of White's own text.
