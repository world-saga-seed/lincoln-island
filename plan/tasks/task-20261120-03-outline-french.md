# Task: phase 2, the scene outline of the French

- **Objective:** a scene outline of every chapter of the French, each beat citing its paragraphs, and a timeline; the ground truth every later row cites.
- **Context:** `BRIEF.md` phase 2; R1120-29, R1120-32, R1120-33, R1120-36, R1120-37.
- **Related study:** `plan/tasks/task-20261120-02-budget-sample.md` (the carders' Open lines on the text's own discords).
- **Region:** writes `story/outline/NNNNN-slug.md`, `story/notes/NNNNN-slug.md` and `story/calendar/timeline.md`, and this task's folder. Reads `texts/fr-1875/`.
- **Wave:** none.
- **Start hash:** 9ceda4b, 2026-11-20.
- **End hash:** (on close)
- **Status:** Running: the remaining chapters, four a span.

## Numbering

Chapter `NNNNN` is the French chapter in book order, in steps of 100: 00100 is I.1, 02200 is I.22, 02300 is II.1, 04300 is III.1, 06200 is III.20. The working text's file `texts/fr-1875/NN.md` is chapter NN × 100. The insert, when phase 6 places it, takes a number in between.

## Steps

1. **Pilot** (R1120-37): two Sonnet agents at once. Agent A outlines 00100 and 00200; agent B outlines 00300. Measure, project to the 62 chapters, and add the cost of the phase check. Under 6 M, carry on and report the figure to the author; over 6 M, stop and ask.
2. **Run** the remaining 59 chapters in contiguous spans, two agents at a time, each writing its own timeline fragment to this task's folder.
3. **Merge** the fragments into `story/calendar/timeline.md` (the main session).
4. **Check:** `tools/quotes.py` on every outline, note and fragment against its chapter; `tools/links.py`. Then the brief's check: a Haiku finder samples beats against the French, and a Sonnet critic judges the outlines (findings quote the text, R10).
5. **Close:** fold back what the check finds; commit.

## Acceptance

1. 62 outlines and 62 notes files, each beat marked, cited by ¶ range and anchored by a quote that resolves.
2. Each chapter's first beat follows from the last beat of the chapter before.
3. The timeline cites every date; the text's discords are set side by side, not reconciled.
4. The finder's sample and the critic's findings are logged, and every finding's quote resolves.
5. The token rows are in `plan/records/tokens.md`.

## Log

- 2026-11-20 Opened.
- 2026-11-20 The pilot ran two Sonnet agents. Agent a, 00100 and 00200: 98,247 tokens, 12 calls, 4.5 min. Agent b, 00300: 58,889 tokens, 8 calls, 1.3 min. All three outlines pass `check_outlines.py`: coverage ¶1 to the end, every quote resolves, every bullet marked. The checker's first run reported six false faults: it could not read a heading that names a plate, "(I.2 ¶1–¶2, pl1)". The checker was fixed, not the outlines.
- 2026-11-20 The projection: about 25 k tokens fixed per agent plus about 12 per word, so 3.1 M at four chapters a span (3.8 M by flat scaling), plus about 0.3 M for the check. Under 6 M, so the run carries on (R1120-37), and the figure was sent to the author.
- 2026-11-20 Wave 1 launched: c on 00400 to 00700, d on 00800 to 01100. The prompts are made by filling `prompt-outliner.md`; the seam is the French last paragraph of the chapter before.

- 2026-11-20 Wave 1 back. c (00400 to 00700): 120,658 tokens, 33 calls, 5.0 min. d (00800 to 01100): 154,607 tokens, 23 calls, 7.8 min. The harness refused both agents' report files; the main session saved them from the returned text, and the prompt now asks for the report as the final message. d had written plate and note citations inside quote lines, as in "(I.8 pl1)", so 11 quotes failed. The citations were moved to "at:" lines by a script, and the prompt now says so. The checker now tests notes against the whole French, since notes may quote another chapter (d's four declared cross-chapter quotes). All 11 outlines pass.
- 2026-11-20 Wave 2 back. e (01200 to 01500): 149,080 tokens, 24 calls, 7.4 min. f (01600 to 01900): 129,204 tokens, 22 calls, 5.7 min. Both pass `check_outlines.py`, and both reports' and timelines' quotes resolve. e notes short French phrases left in the English prose, uncited (R1120-29). These are held for the critic pass, not edited by hand. f's "claie" in I.17 ¶37 is the hurdle of I.13 and I.15 (`world/things/hurdle.md`). The running total is 810,685 tokens for 19 chapters.
- 2026-11-20 Wave 3 back. g (02000 to 02300): 146,523 tokens, 27 calls, 7.3 min. h (02400 to 02700): 151,157 tokens, 23 calls, 6.2 min. Both pass. g's scratch script was overwritten by h's in the shared scratch folder, and g re-ran its check under another name. The prompt now gives each agent its own scratch folder, as the workflow's step 2 says. The running total is 1,108,365 tokens for 27 chapters.

## Resolution

(On close.)
