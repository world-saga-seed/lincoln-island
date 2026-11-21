# Task: the budget sample, carding three chapters

- **Objective:** card three French chapters of different kinds, measure the cost, and estimate the whole carding for the author before phase 2.
- **Context:** R1120-11, R1120-27, R1120-32 to -34; `BRIEF.md` phase 0 item 5 and phase 4.
- **Related study:** none.
- **Region:** writes new cards in `world/people/`, `world/places/` and `world/things/`, the two agents' reports in this task's folder, and `plan/records/tokens.md`. Reads `texts/fr-1875/01.md`, `13.md` and `58.md`.
- **Wave:** none.
- **Start hash:** b6bdffe, 2026-11-20.
- **End hash:** (on close)
- **Status:** Done.

## Steps

1. **Plan.** Run card-existing (`plan/workflows/card-existing.md`) on I.1 (`01.md`, the fall and the people), I.13 (`13.md`, bricks and pottery, the tool chain) and III.16 (`58.md`, Nemo's story). Two fresh Sonnet agents (R1120-34) run at once. Agent A writes `world/people/`; agent B writes `world/places/` and `world/things/`. Each gets the reading list and writing list below. No git, no sub-agents.
2. **Execute.** Run both agents.
3. **Check.** Every quote resolves (`tools/quotes.py` against the three chapters); `tools/cards.py build` and `check` print 0; a read of the cards against the form and the marks.
4. **Measure.** Each agent's tokens, calls and minutes, from its result, go in the token log.
5. **Estimate.** Scale by words to the 62 chapters (205,324 words), plus the merging of cards that recur across chapters, plus R1120-25's *Vingt mille* scope. Send to the author.

**Both agents read:** `CLAUDE.md` rule 2 (the marks) and the "About the writer" section, `plan/templates/card.md`, `texts/README.md`, and `texts/fr-1875/01.md`, `13.md`, `58.md`.

**Agent A writes:** `world/people/*.md` (new files only) and `plan/tasks/task-20261120-02-budget-sample/report-people.md`.

**Agent B writes:** `world/places/*.md` and `world/things/*.md` (new files only), and `plan/tasks/task-20261120-02-budget-sample/report-places-things.md`.

## Acceptance

1. Every quote in both reports and in every card resolves in the three chapters.
2. `tools/cards.py check` and `tools/links.py` print 0.
3. Every fact is in English, followed by its French quote and citation (R1120-29); every line carries a mark.
4. The token rows are in `plan/records/tokens.md`.
5. The estimate is sent to the author.

## Log

- 2026-11-20 Opened.
- 2026-11-20 Both agents ran at once on Sonnet. People: 8 cards, 112,859 tokens, 17 calls, 5.2 min. Places and things: 49 cards (16 places, 33 things), 138,953 tokens, 16 calls, 8.3 min.
- 2026-11-20 Checked: all 604 quotes on the cards and every quote in both reports resolve in the three chapters; `cards.py build` and `check` print 0; `links.py` prints 0; `check_clean` is clean. A spot read of the bricks card against I.13 ¶32 and ¶42, and of Nemo's numbers against III.16 ¶55, ¶60 and ¶62, found the English true to the French.
- 2026-11-20 The agents raise the following, all held for phase 4:
  - Animals have no card folder. Top, the dog, is carded by neither agent. Rec: `world/animals/`.
  - The text disagrees with itself: Nemo's years (III.16 ¶19, ¶21, ¶39, ¶45, ¶55, ¶60, ¶62) and I.13 ¶34's night length against its own footnote. Both are held on Open lines, carded neither way.
  - Ayrton's card is thin, because III.16 only names him. The part II chapters fill it.

## Resolution

**The sample:** 57 cards, about 560 facts, from 10,234 words of French; 251,812 agent tokens in all, which is 24.6 tokens per word of source.

**The estimate for phase 4,** sent to the author:
- **Flat scaling** to the 62 chapters (205,324 words): about 5.1 M agent tokens.
- **Merging:** later batches must find and extend cards that already exist (Cyrus's card already holds 54 quotes from three chapters), so reading cards adds to each batch. Allow 1.5 to 2 times the flat figure: **7.6 M to 10.1 M**.
- ***Vingt mille*** (R1120-25): only the passages *L'Île* draws on, perhaps 15,000 to 30,000 words, so **0.4 M to 0.75 M** at the same rate.
- **Time:** at two agents at once, about 8 minutes of wall time per three chapters, so about 3 hours for the 62 chapters before merging.
- **Not counted:** the main session's checking, and the phase 4 finder that samples facts against the French.
