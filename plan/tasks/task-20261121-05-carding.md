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

## Resolution

(On close.)
