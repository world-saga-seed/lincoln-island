You are carding Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) from the French, in English, one wave of chapters at a time. The repository is the current folder; every path below is relative to it. Run no git commands of any kind, not even read-only ones. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-w1a/ and nowhere else.

YOUR CHAPTERS (read every paragraph, footnote, plate caption and loose line):

- I.2: texts/fr-1875/02.md
- I.3: texts/fr-1875/03.md
- I.4: texts/fr-1875/04.md
- I.5: texts/fr-1875/05.md

READ:
- plan/templates/card.md (the card's form) and texts/README.md (how the French is cited);
- the "What a card holds" section of plan/archive/task-20261121-05-carding.md;
- your folders' index tables (README.md in each), to see which cards exist; and the existing cards you will extend, but only those. To find a card by a word: `python3 tools/cards.py find WORD` (run it from the repository's folder).

YOUR ROLE: A
- **A** writes `world/people/` (every named person) and `world/animals/` (Top, Jup, and each kind of beast, bird, fish or insect the colonists meet, hunt, tame, breed or eat: one card a kind).
- **B** writes `world/places/` (every named or described place: island features, rooms, coasts, waters, and places off the island), `world/things/` (every thing found, owned, made or used, and every plant put to use: one card a thing), and `world/things/tool-chain.md` (see below).
Write nothing outside your folders, except your report: plan/archive/task-20261121-05-carding/report-w1a.md.

THE CARD. A new card follows `plan/templates/card.md`: the five-line head (title "# Name: what it is, in a few words", the italic one-line summary, the Keywords line), then the sections **What it is.**, **On the page.**, **Habits.** (people only), **Appears in:**, **Open:** (only if needed). A file name is the name in lower case with hyphens, ASCII only (gedeon-spilett.md).

Each fact is one bullet under its section, in English, with its cite and its mark, and under it the French words it rests on, copied exactly:

    - He knows something of forge work (I.13 ¶7). *(Drafted.)*
      - quote: il s’entendait quelque peu au travail de la forge

Mark a fact the text states *(Drafted.)*; mark your inference *(My reading, to confirm.)*. Cite part, chapter and paragraph (I.2 ¶14; a footnote "I.2 n1"; a plate caption "I.2 pl1"; a loose line "II.9 ln4"). Every quote is copied character for character from the cited paragraph, with the text's own apostrophes (’) and spacing; keep it to the decisive words.

WHAT A CARD HOLDS. What is true of its subject, not the story's events: nature, trade, origin, age, look, traits, skills, possessions, relations; each change dated and cited (made, found, named, built on, wounded, freed, dead); for a made thing, what it is made of, by whom, when and how. An act goes on a card only when it shows what the subject is or changes it. Where the text disagrees with itself, quote both readings on the **Open** line and card neither.

EXTENDING A CARD. When your chapters add to an existing card, add the new facts in their sections, in book order, and add your chapters to **Appears in:** (written as I.2, I.3, ...). Never delete or reword a line already on a card. If a new fact contradicts one on the card, put both on the **Open** line.

A NEW FOLDER CARD. If `world/animals/README.md` does not exist and you are A, make it: copy world/people/README.md's first three lines, retitled "# Animals" with the line "A card for every animal named or met in the French, one a kind, each fact cited by part, chapter and paragraph.", then a blank line and the two marker lines `<!-- cards: built by tools/cards.py; do not edit -->` and `<!-- /cards -->` with nothing between them.

THE TOOL CHAIN (B only). `world/things/tool-chain.md` lists, in book order, every thing the colonists make or obtain by a process: one line each, "- **Name** (I.13 ¶42): made from what, by whom, with what; the card's link. *(Drafted.)*". If the file does not exist, start it with "# The tool chain" and the line "*The colonists' made things in book order, each with its inputs and its card.*". Add your chapters' lines at the end, in order.

A CROWD FIGURE. A name met once with nothing to say about it gets no card: list it in your report.

YOUR REPORT (the file named above, and the same text as your final message): the cards you made and the cards you extended, as two lists of file names; the crowd figures; the text's own disagreements you put on Open lines; questions for the author, each with your recommendation; and one line of totals (cards made, cards extended, facts added).
