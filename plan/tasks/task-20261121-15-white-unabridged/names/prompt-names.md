# The names builder's prompt (R1121-149)

---

You are building one reference list for a novel in progress, in the current folder: Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) in the English of Stephen W. White's translation (1876). New English chapters must use White's forms of every proper name. Run no git commands of any kind (not even status or log). Do not launch agents. Work alone. You may run read-only shell commands (grep, sed, python3 reading files) to search; write only the one output file named below.

THE SOURCES:
- the French, texts/fr-1875/01.md to 62.md (paragraph-numbered "¶N"; I.1 to I.22 are 01 to 22, II.1 to II.20 are 23 to 42, III.1 to III.20 are 43 to 62);
- White's text, texts/white-1876/01.md to 62.md (paragraph-numbered; White numbers his chapters straight through, I to LXII);
- the paragraph alignment, texts/align/NN.tsv (French paragraph to White paragraph), which lets you find the White paragraph for a French one;
- the names of the setting's cards: every file in world/people/ and world/places/, and in world/things/ and world/animals/ only those whose title is a proper name (a ship, a named animal such as Jup, a named document). Each card's first line gives the French name; its "Keywords:" line gives other forms.
- the list made so far for I.19 and I.20: story/voice/names.md. Keep its rows and its form; extend it.

THE TASK: for every proper name the French uses anywhere in the book (people, places on and off the island, ships, named animals, named things, and forms of address such as "monsieur Cyrus"), give White's form as he prints it, with his count in his whole text. Where White uses two forms, give both with their counts and say which is his usual one. Where White has no form (he cuts every passage that names it), say "none in White" and give the plain English a reader of 1876 would expect, marked *(Proposal.)*. Where White's form changes across the book (as "Safety Island" in Part I and "Safety Islet" later), say where.
Note in a last column the first French chapter that names it (as "II.12").

Write the list to plan/tasks/task-20261121-15-white-unabridged/names/names-book.md, with the same header and table form as story/voice/names.md, extended by the "First" column, sorted by part of the setting (people, the island's places, places off the island, ships and things, animals, forms of address). Every White form must be one you found in texts/white-1876 by search; never one from memory or from another translation.

Finish with a short report (your final message): the number of names; every name for which White has no form; every name where you were unsure which French name White's form renders, quoted.
