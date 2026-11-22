# Task: the full actor logs for 01900 to 02000

- **Objective:** build the full actor logs for the stretch 01900, 01950, 02000, Captain Nemo first, audit them by the three critics, and bring the author an interview of every rank (a) finding before anything is drafted.
- **Context:** the author's word, 2026-11-21 (after R1121-61): "Run the actor logs for the stretch from 01900 to 02000, the full ones, Nemo first." Workflow: `plan/workflows/actor-log.md` (the full log, Refinement).
- **Related study:** none.
- **Region:** writes `story/calendar/captain-nemo/01900-02000.md`, `story/calendar/household/01900-02000.md`, `story/calendar/pencroff-and-harbert/01900-02000.md`, this task and its folder. Rests on the three outlines (`story/outline/01900-…`, `01950-…`, `02000-…`), their notes, `world/rules.md`, the cards of Nemo, the crypt, Granite-house, the well, the islet, Top, and the ledger R1121-23 to -61.
- **Wave:** none.
- **Start hash:** c51effb 2026-11-21.
- **End hash:** the commit that archives this task.
- **Status:** Closed, 2026-11-21.

## Steps

1. **Plan.** Actors: Captain Nemo; the household not in the secret (Smith, Spilett, Nab), as a group; Pencroff and Harbert off the page; Top inside the household's log. Extraction by the main session, not one agent per actor: the stretch is three chapters and every source is already quoted in this session's rulings (a change from the workflow, logged). Quotes checked by grep. The audit by fresh agents, at most two at a time, none spawning, no git: (1) logistics and physics, (2) causal chain; then the cross-log check at the meeting places. The character invariant does not run: no character sheets exist (`plan/workflows/actor-log.md`, "It runs only on people with a sheet"); the critics read the people cards instead, and the author is told.
2. **Execute.** Build the logs; run the critics; merge into `interview.md`.
3. **Check** against Acceptance.

## Acceptance

1. Every beat Nemo drives in 01950 traces to a row of his log.
2. Every quote in the logs resolves.
3. Every rank (a) finding is in `interview.md` with both sides quoted, the plain fix first and a recommendation.

## Log

- 2026-11-21 Opened. Logs built by the main session; 16 quotes resolve. Critics 1 (logistics and physics) and 2 (causal chain) launched.
- 2026-11-21 The author: full logs for Nemo, Pencroff and Harbert; the light pass only for Smith, Spilett and Nab. The household log is relabelled as a light pass. The critics already running read it as it stands, which is the light pass's content.

- 2026-11-21 The author replaced the light-boat net with the crew's old net (R1121-62; R1121-29 replaced, R1121-26 amended). Nemo's log rebuilt; he drives no beat. The critics, launched before, audit the old version: their findings on Nemo's trip are dropped as stale (rank b).
- 2026-11-21 Critics in: logistics 16 (10 a, 6 c), causal 13 (8 a, 1 b, 4 c). Saved as critic-logistics.md and critic-causal.md. Stale under R1121-62: L4, L5, L12, L14. The b and c items written into the logs. Eleven a items merged into interview.md, with the check that nothing turns up (R1121-65). Rulings R1121-63 to -65 applied. The cross-log check is folded in: the meeting places (the bar, Granite-house's windows, the Chimneys, the well) are items 1, 2, 7 and 11.
- 2026-11-21 The author ruled all eleven (R1121-68 to -79). Applied to the outline and the logs; the quotes resolve, and links.py reports 0 broken.

## Resolution

The full logs for Captain Nemo and for Pencroff and Harbert, and the light pass for the household, are built in `story/calendar/`. The two critics ran (logistics and physics; the causal chain). The character invariant did not run: there are no character sheets. Of 29 findings, 4 were stale under R1121-62, 8 small ones were fixed by the main session, and 11 went to the author, who ruled them all (R1121-68 to -79), along with the old net and the float's end (R1121-62 to -67). The gap pass followed in `story/notes/01950-the-float-in-the-bar.md` (R1121-80 to -82). One change from the workflow: the main session did the extraction, not one agent per actor. No agent broke its brief. The logs are current to these rulings; they go stale if an outline of the stretch changes.
