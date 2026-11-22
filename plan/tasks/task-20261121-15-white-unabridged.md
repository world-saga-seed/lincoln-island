# Task: White made unabridged (R1121-144 to R1121-147), the pilot

- **Objective:** White's translation made whole: each chapter patched by its departures from the French, or rendered whole from the French in White's voice where he departs too far (R1121-144, R1121-145); first a pilot of one patch (I.5) and one re-render (III.14), measured before any more (R1121-147).
- **Context:** the author, 2026-11-21. The measure (R1121-145): the missing share, 1 − (White's words ÷ French words) ÷ 0.885, and discords per 1,000 French words; re-render at 20% or 8. The patch rule (R1121-146). Every chapter passes the critics before it counts as done.
- **Horizon:** widened by the human to the whole book for this phase, at about 17M tokens (R1121-148). The pilot's chapters go to `story/prose/` once they pass the critics (R1121-146).
- **Region:** writes this task and its folder. Reads `texts/fr-1875/`, `texts/white-1876/`, `texts/align/`, `story/voice/`, `plan/workflows/drafting/rulings.md`, the chapters' outlines and notes, and `world/`.
- **Wave:** none.
- **Start hash:** (at the first commit)
- **End hash:** (on close)
- **Status:** Executing: the pilot's patcher and drafter are running.

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
- 2026-11-21 R1121-148: the human widens the horizon. The controls' checks in. The pilot launched: the I.5 patcher and the III.14 drafter, fresh Opus agents.
- 2026-11-21 I.5 patched: 7 patches from the list, then 12 the patcher found ("new") and one more (P20, the raft moored, not built; added by the main session); P14 reworded on the main session's call ("he could not, or would not, live any longer"). 20 patches apply; banned 0, spelling 0; tells: med 17, sd 11.6, short 20, long 25 (White's own I.5: 17, 11.3, 17, 26). **The lesson:** the phase 3 list holds 7 of at least 20 departures in the chapter with the fewest, so the lists undercount and the patcher must read for departures, not only patch the list. The facts critic runs.
- 2026-11-21 III.14 drafted: 3,570 words (0.94 of the French's 3,803); tells med 20, sd 12.0, short 7, long 35, banned 0, spelling 0. The drafter broke its prompt: it ran a python script (it failed before writing; the same splits then made by hand). Names set to White's on the main session's call (rulings.md): Balloon Harbor, Jetsam Point, Good Luck (White's boat), Mr. Smith for "monsieur Cyrus". **Lesson:** story/voice/names.md covers I.19 and I.20; the whole book needs White's names list first, from texts/white-1876 and the French.
- 2026-11-21 The I.5 facts critic, round 1: 11 more departures where White still stands. So I.5 holds at least 31, against 7 listed. Patcher's third pass running; then the omission critic.
- 2026-11-21 III.14 facts critic: faithful; 4 findings, all the rulings' "Mr. Smith"; 0 standing. The omission critic runs.
- 2026-11-21 III.14 omission critic: 0 losses. III.14 waits only for the voice critic.
- 2026-11-21 The patcher's third pass: P21 to P31 for the critic's 11, and P32 to P46 for 15 more it found; P46 smoothed on the main session's call ("Herbert soon fell asleep."). 46 patches apply. The patched I.5 keeps 2,623 of White's 2,711 words (96.8%) and runs 2,828 words, 0.87 of the French (the measure's 0.885). Four places the patcher judged close enough are left for the critics (¶4, ¶26, ¶43, ¶84). The voice critic (both chapters) and a second facts critic on I.5 run.
- 2026-11-21 The second I.5 facts critic: 12 more, all where White's words stand ("scratching" for rubbing; Neb's hope held out, reversed by White; "je vous en prie"; "Non"; "je ne veux pas"; "chargea"; the bluish flame; into the cone; "fort bien"; Verne's "Ah ! si…"; the one incident; "veillant"). Patched by the main session (P47 to P57, and P36 to "scratching"): 57 patches apply. Round 1 found 11 and round 2 found 12: the tail is long, so a patched chapter needs about three passes of patcher and critic.
- 2026-11-21 Voice critic on the pilot: no standing break (the "&" is Verne's). I.5: White's print slips patched (P58 to P61) and two seams smoothed; 61 patches. III.14: two knots and repeated connectives, weak. I.5's omission critic: 0 losses. A third facts round on I.5 runs, to see whether the tail has ended.
- 2026-11-21 The third facts round on I.5: 3 (lost, extreme, "Poor fellow!"). Two patched (P62, P63); "Poor fellow!" kept as a stylistic addition (R1121-146). The tail: 11, 12, 3. **Both pilot chapters pass** (no break standing) and go to `story/prose/` as final (R1121-146).

## The pilot's measure

| | I.5, patched | III.14, re-rendered |
|---|---|---|
| Departures found | 7 listed; 63 patches in all (7 from the list, 39 from the patcher's own reading and the first facts round, 13 from the second and third facts rounds, 4 White's print slips) | — |
| Rounds to pass | patcher ×3, facts ×3, omission, voice | drafter, facts, omission, voice |
| Tokens (agents) | about 490k (patcher 207k; facts 63k + 63k + about 60k; omission 52k; voice 47k) | 263k (drafter 105k; facts 58k; omission 53k; voice 47k) |
| White's words kept | 2,623 of 2,711 (96.8%) | none (new render) |
| Length against the French | 0.87 | 0.94 |
| Standing findings | taste only | weak: two knots, repeated connectives |

Lessons: (1) the phase 3 lists undercount White's departures by a factor of about eight (7 listed, 59 departures patched), so a patcher must read for departures, not only patch the list; (2) story/voice/names.md covers I.19 and I.20 only, and later names (Balloon Harbor, Jetsam Point, Good Luck, Tabor Island) must come from White's own text; the book needs White's names list first; (3) a drafter broke its one-command rule.
- 2026-11-21 R1121-149 (option A). `chapters.tsv`: 37 to patch, 21 to re-render, 4 done (I.5, I.19, I.20, III.14). `patcher-v2.md` (a full reading against the French), `chap.py` (a chapter's folder, prompts and title; `apply`). The names builder runs (`names/`), for the re-renders. The patches start in book order with I.1, since a patch keeps White's names.

## The loop, per chapter

Patch: patcher v2 (Opus) → apply → facts critic → patcher's second pass on the findings → apply → facts critic 2 → the last findings patched by the main session → omission critic → voice critic by threes → into `story/prose/` as final. Re-render: drafter (Opus, a bundle by `build_bundle.py`, the names list) → facts → omission → voice → final.
