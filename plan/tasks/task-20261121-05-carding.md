# Task: phase 4, the carding

- **Objective:** a card for every person, animal, place, thing and made thing of *L'Île mystérieuse*, from the French, in English, each fact cited and quoted; the tool chain in order; then *Vingt mille lieues* where *L'Île* draws on it.
- **Context:** `BRIEF.md` phase 4; R1120-25, R1120-29, R1120-33, R1120-34, R1120-35 (the 12 M cap), R1121-02 (the scope), R1121-03 (`world/animals/`).
- **Related study:** `plan/tasks/task-20261120-02-budget-sample.md` (57 cards from I.1, I.13, III.16; the estimate, 7.6 M to 10.1 M plus 0.4 M to 0.75 M for *Vingt mille*).
- **Region:** writes `world/people/`, `world/animals/`, `world/places/`, `world/things/` and this task's folder. Reads `texts/fr-1875/`, the card folders.
- **Wave:** see Steps.
- **Start hash:** a579947, 2026-11-21.
- **End hash:** (on close)
- **Status:** Running, four chapters a wave.

## What a card holds *(Settled R1121-05.)*

The outlines hold the events; a card holds what is true of its subject. A card records: what it is (nature, trade, origin, age, look, traits, skills, possessions, relations); how it changes, each change dated and cited (a thing made or found, a place named or built on, a person wounded, freed or dead); for a made thing, what it is made of, by whom, when and how; and the chapters it appears in. A card does not log scenes: an act goes on a card only when it shows what the subject is or changes it. The cards made before this ruling are brought to the form when a later wave touches them (R1121-06). Where the text disagrees with itself, both readings go on the **Open** line, carded neither way (R1120-33).

## Steps

1. **Pilot:** wave 1, chapters I.2 to I.5. Two fresh Sonnet agents at once (R1120-34): A writes `world/people/` and `world/animals/`; B writes `world/places/`, `world/things/` and `world/things/tool-chain.md`. Measure; project to the book; report to the author if the projection nears the 12 M cap.
2. **Run** the waves in book order, four chapters a wave, the two agents at once on the same span, each alone in its folders. I.1, I.13 and III.16 are carded already; their cards are extended when a later chapter adds to them.
3. **Check** each wave: `tools/quotes.py` on every card against the French; `tools/cards.py build` and `check` print 0; `tools/links.py`.
4. **Vingt mille** (R1120-25, R1121-02): the passages *L'Île* draws on, carded in a last wave.
5. **The phase check:** a finder samples facts against the French; a critic judges.
6. **Close.**

## Acceptance

1. Every named person, animal, place and thing has a card, or is listed as a crowd figure in a report.
2. Every fact is in English, cited, quoted in French, marked; every quote resolves.
3. `cards.py check` and `links.py` print 0.
4. `world/things/tool-chain.md` lists the made things in order, each with its card.
5. The finder's sample and findings are logged; the tokens are in `plan/records/tokens.md`; under 12 M.

## Log

- 2026-11-21 Opened. `world/animals/` made (R1121-03).
- 2026-11-21 The pilot, wave 1 (I.2 to I.5). A: 7 cards made (Top, gulls, skuas, rock pigeons, lithodomes, Jonathan Forster, Ulysses Grant), 5 extended, 186 facts; 122,492 tokens. B: 24 made (11 places, 13 things), 7 extended, 194 facts, the tool chain begun; 143,216 tokens; it ran `git diff --stat` against its prompt (read-only). 265,708 tokens for four chapters; all 993 quotes on the cards resolve; `cards.py check` and `links.py` print 0. Projected to the book at this rate, about 4 to 5 M with growth, under the 12 M cap.
- 2026-11-21 What the pilot showed, and the prompt's fixes: A logged scenes on the people's cards ("He asks whether the lost engineer can swim"), against "What a card holds"; the prompt now gives examples of what belongs and what does not. B carded unnamed features under descriptions (`the-snow-capped-mountain`, `the-islet`, `the-bay`), which I.11 names; carders now read I.11 ¶63 to ¶81 and card under the book's names, and the wave that reaches I.11 renames those cards. Stale gap lines on Open may now be deleted when answered (rule 9); the text's own disagreements never. The pilot's lines stay as written. The author's ruling R1121-04 came in: stubs for one-chapter subjects on no Clues list, full cards for the rest; the carders read their chapters' Clues sections.
- 2026-11-21 Wave 2 (I.6 to I.9). A: 6 made (3 stubs), 8 extended, 130 facts; 154,124 tokens; ran `git diff --stat`. B: 40 made (24 stubs), 16 extended, 151 facts, 8 tool-chain lines; 209,227 tokens; ran `git status`. Both read-only, both against the prompt; the prompts from wave 3 tell carders to read their files instead. 135 cards in all, 27 of them stubs; all 1,328 quotes resolve; `cards.py check` and `links.py` print 0. B kept extending the descriptive place cards rather than carding under the book's names; the I.11 wave renames them. For the close: stubs whose subject also appears in I.1, I.13 or III.16 (the chapters no wave reaches) are built then; the first is the jacamar (I.9, I.13 ¶36).
- 2026-11-21 Wave 3 (I.10 to I.12, I.14). A: 20 made (3 stubs), 9 extended, 140 facts, 195 lines pruned (R1121-06); 198,745 tokens. B: 46 made (14 stubs), 36 extended, 11 tool-chain lines, 46 lines pruned; the renames done (`mont-franklin`, `baie-de-l-union`, `ilot-du-salut`; `the-southern-point` merged into `cap-griffe`, marked as a reading); 274,328 tokens. Neither ran git. The pruning went too far: a sample showed traits and skills cut with the scenes ("He and the reporter become very skilful archers"). A fresh Sonnet reviewer sorted the 245 pruned lines: 68 keep, 177 scene (`pruned-w3-review.tsv`; 53,850 tokens); the 68 are restored in place, with their quotes. The prompt from wave 4 keeps a line that shows a trait, skill, knowledge, capacity or limit, and says "when in doubt, keep". One stale link to `the-bay.md` repointed. 198 cards; all 1,635 quotes resolve; `cards.py check` and `links.py` print 0.
- 2026-11-21 Wave 4 (I.15 to I.18). A: 9 made (2 stubs), 11 extended, 130 facts, 7 pruned; 172,953 tokens. B: 31 made (16 stubs), 26 extended, 23 tool-chain lines, 3 pruned; 224,775 tokens. Neither ran git; the sharper pruning rule held. B rebuilt the index tables while A was writing; from wave 5 the main session rebuilds them after each wave. 238 cards, 56 stubs; all 2,111 quotes resolve; `cards.py check` and `links.py` print 0.
- 2026-11-21 Wave 5 (I.19 to I.22), the end of Part I. A: 10 made (3 stubs), 15 extended, 164 facts, none pruned; 190,994 tokens. B: 39 made (18 stubs), 5 stubs built, 45 extended, 17 tool-chain lines, 12 pruned (3 more refused by the clue check); 270,746 tokens; tried `git log` once (refused by the tool). 287 cards, 72 stubs; all 2,815 quotes resolve; `cards.py check` and `links.py` print 0. Questions held for one batch to the author at the close: wild boars or peccaries (I.15, I.22); the two "lapins d'Amérique"; the "lagon" of I.19 ¶30; the upper cave of I.19 ¶16; the well of I.22 ¶53; the wheat bed's place; the cap-griffe merge (wave 3).
- 2026-11-21 Wave 6 (II.1 to II.4). A: 6 made (2 stubs), the jacamar stub built, 21 extended, none pruned; 183,986 tokens. B: 24 full and 46 stubs made (the chest's inventory, one a thing), 4 stubs built, 31 extended, 3 tool-chain lines, 2 pruned; 218,250 tokens. No git. 363 cards, 115 stubs; all 3,409 quotes resolve; checks print 0. Held for the author: the Falls-river cove and the "western creek"; the "lunette" and the chest's two glasses; the early "pointe de l'Épave" (I.21 ¶20); the jaguar's "congénères d'Asie" (II.4 ¶63).
- 2026-11-21 Wave 7 (II.5 to II.8). A: 15 made (9 stubs; tinamous and bustards built), 21 extended, 14 pruned; 219,258 tokens. B: 43 made (21 stubs; 9 stubs built), 43 extended, 15 tool-chain lines, none pruned; 266,902 tokens. No git. 410 cards, 134 stubs; all 4,080 quotes resolve; checks print 0. Held for the author: one card for the apes and Jup; the "renards" of II.7 ¶33 as culpeux; moorhens apart from coots; the dovecot pigeons; the II.5 dates (31 October, "2 novembre", "3 novembre"); the balloon "à air chaud" (II.7 ¶47) against gas (I.1 ¶49); the two cuts of II.7 ¶18 and ¶39.

## Resolution

(On close.)
