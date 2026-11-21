You are carding Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) from the French, in English, one wave of chapters at a time. The repository is the current folder; every path below is relative to it. Run no git commands of any kind, not even read-only ones. To see what you have written, read your files; never run git status, git diff or git log. To see what you have written, read your files; never run git status, git diff or git log. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-w9b/ and nowhere else.

YOUR CHAPTERS (read every paragraph, footnote, plate caption and loose line):

- II.13: texts/fr-1875/35.md
- II.14: texts/fr-1875/36.md
- II.15: texts/fr-1875/37.md
- II.16: texts/fr-1875/38.md

READ:
- plan/templates/card.md (the card's form) and texts/README.md (how the French is cited);
- the "What a card holds" section of plan/tasks/task-20261121-05-carding.md;
- the **Clues.** section of each of your chapters' notes, story/notes/NNNNN-*.md (00600 is I.6, 02300 is II.1, 04300 is III.1): it decides what gets a full card (below);
- the names the colonists give the island's features, texts/fr-1875/11.md ¶63 to ¶81. Card a place or thing under the name the book gives it, even before your chapters give it: the mountain is "mont Franklin", the islet "l’îlot du Salut", the river "la Mercy". The first bullet says where it is named, cited.
- your folders' index tables (README.md in each), to see which cards exist; and the existing cards you will extend, but only those. To find a card by a word: `python3 tools/cards.py find WORD` (run it from the repository's folder).

YOUR ROLE: B
- **A** writes `world/people/` (every named person) and `world/animals/` (Top, Jup, and each kind of beast, bird, fish or insect the colonists meet, hunt, tame, breed or eat: one card a kind).
- **B** writes `world/places/` (every named or described place: island features, rooms, coasts, waters, and places off the island), `world/things/` (every thing found, owned, made or used, and every plant put to use: one card a thing), and `world/things/tool-chain.md` (see below).
Write nothing outside your folders, except your report: plan/tasks/task-20261121-05-carding/report-w9b.md.

THE CARD. A new card follows `plan/templates/card.md`: the five-line head (title "# Name: what it is, in a few words", the italic one-line summary, the Keywords line), then the sections **What it is.**, **On the page.**, **Habits.** (people only), **Appears in:**, **Open:** (only if needed). A file name is the name in lower case with hyphens, ASCII only (gedeon-spilett.md).

Each fact is one bullet under its section, in English, with its cite and its mark, and under it the French words it rests on, copied exactly:

    - He knows something of forge work (I.13 ¶7). *(Drafted.)*
      - quote: il s’entendait quelque peu au travail de la forge

Mark a fact the text states *(Drafted.)*; mark your inference *(My reading, to confirm.)*. Cite part, chapter and paragraph (I.2 ¶14; a footnote "I.2 n1"; a plate caption "I.2 pl1"; a loose line "II.9 ln4"). Every quote is copied character for character from the cited paragraph, with the text's own apostrophes (’) and spacing; keep it to the decisive words.

WHAT A CARD HOLDS. What is true of its subject, not the story's events, which the outlines hold: nature, trade, origin, age, look, traits, skills, possessions, relations; each change dated and cited (made, found, named, built on, wounded, freed, dead); for a made thing, what it is made of, by whom, when and how. An act goes on a card only when it shows what the subject is or changes it. Where the text disagrees with itself, quote both readings on the **Open** line and card neither.
  - Belongs: "He is a sailor of thirty-five to forty, powerfully built, very tanned" (I.2 ¶24). "He knows fifty-two ways of dressing eggs" (I.5 ¶84). "He keeps the name 'Chimneys' for the dwelling" (I.4 ¶27). "Made of dead wood bound with dry lianas, by Pencroff and Harbert, in an hour" (I.4 ¶39).
  - Does not belong: "He asks whether the lost engineer can swim." "He says three hours will bring the ebb." "In the storm he says they will get through." Lines like these are scenes: leave them to the outlines.

FULL CARD OR STUB (the author's ruling, R1121-04). A subject gets a **full card** if it appears in more than one chapter, or already has a card, or is on a Clues section of your chapters' notes. Anything else (met in one chapter only, on no Clues list) gets a **stub**: the five-line head, then only

    - **What it is.** A <kind: a bird, a tool, a cove...>. Build if needed. *(Drafted.)*
    - **Appears in:** I.6 ¶12, ¶15

with no facts and no quotes. If a subject has a stub and your chapters meet it again, build the stub into a full card: read the paragraphs the stub cites, and card them with yours.

RENAMING. If your chapters give a name to a subject carded under a description (for example `the-snow-capped-mountain.md`, `the-islet.md`, `the-bay.md`), write the card under its name as a new file, carrying over every line, and delete the old file. Say so in your report.

EXTENDING A CARD. When your chapters add to an existing card, add the new facts in their sections, in book order, and add your chapters to **Appears in:** (written as I.2, I.3, ...). Never delete or reword a line already on a card, with one exception: an **Open** line that records a gap ("the chapters do not say how wide") may be deleted when your chapters answer it, with the answer carded in its place. An Open line that records the text's own disagreement is never deleted. A second exception (the author's ruling, R1121-06): when you extend a card, bring it to the form above. Delete the lines that only log a scene (as in the "Does not belong" examples), and only those: a line that shows by a telling act a trait, skill, knowledge, capacity or limit of its subject ("he becomes a skilful archer", "he is not a man to let an occasion slip", "he knows the couroucous are good to eat") stays. When in doubt, keep, unless the line is on a Clues section of the notes for its chapter, which you then keep (clues are never trimmed). List each card you pruned, and how many lines, in your report. If a new fact contradicts one on the card, put both on the **Open** line.

A NEW FOLDER CARD. If `world/animals/README.md` does not exist and you are A, make it: copy world/people/README.md's first three lines, retitled "# Animals" with the line "A card for every animal named or met in the French, one a kind, each fact cited by part, chapter and paragraph.", then a blank line and the two marker lines `<!-- cards: built by tools/cards.py; do not edit -->` and `<!-- /cards -->` with nothing between them.

THE TOOL CHAIN (B only). `world/things/tool-chain.md` lists, in book order, every thing the colonists make or obtain by a process: one line each, as the file's existing lines are written: the thing's name in bold, its cite, what it is made from, by whom, with what, and a link to its card, marked *(Drafted.)*. Add your chapters' lines at the end, in order.

A CROWD FIGURE. A name met once with nothing to say about it gets no card: list it in your report.

YOUR REPORT (the file named above, and the same text as your final message): the cards you made and the cards you extended, as two lists of file names; the crowd figures; the text's own disagreements you put on Open lines; questions for the author, each with your recommendation; and one line of totals (cards made, cards extended, facts added).
