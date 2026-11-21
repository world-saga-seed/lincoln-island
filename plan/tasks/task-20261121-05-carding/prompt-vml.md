# The Vingt mille carder's prompt (step 4; R1120-25, R1121-02)

You are carding what Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) draws from his *Vingt mille lieues sous les mers* (Hetzel, 1870). The repository is the current folder; every path below is relative to it. Run no git commands of any kind, not even read-only ones; to see what you have written, read your files. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-vml/ and nowhere else.

THE RULING (the author's, R1120-25): only what *L'Île* draws on from *Vingt mille* is carded, each card line citing the earlier book. Nothing else from *Vingt mille* is carded, however interesting.

READ:
- plan/templates/card.md and texts/README.md (how both French texts are cited);
- the "What a card holds" section of plan/tasks/task-20261121-05-carding.md;
- in *L'Île*: texts/fr-1875/58.md (III.16) in full, with its note n1; texts/fr-1875/57.md (III.15) from ¶100 to the end; texts/fr-1875/59.md (III.17);
- the cards you may extend: world/people/captain-nemo.md, and in world/places/ and world/things/ every card whose name begins `nautilus` or `the-nautilus`, plus `crypte-dakkar.md`, `mobilis-in-mobili.md`, `bundelkund.md`;
- in *Vingt mille* (texts/vml-1870/, 47 chapters, about 150,000 words; INDEX.md lists them): **do not read it through.** Search it (grep, or a short script) for the passages that bear on each thing *L'Île* says, and read those paragraphs only.

THE TASK. Go through what *L'Île* says of Nemo's past and of the Nautilus (III.15 ¶100 on, III.16, III.17). For each statement that rests on *Vingt mille* (for example: the submarine built on a desert island of the Pacific, its electricity, the Vigo bay treasure, the three men thrown aboard on 6 November 1866, the Nautilus taken for a cetacean, the seven months and twenty thousand leagues, the escape of 22 June 1867 in the Maelstrom, the coral cemetery, the diving dress, the device "Mobilis in mobili", the saloon, library and organ, the ship's measures), find the passage in *Vingt mille* that tells it, and card it:
- on the card the *L'Île* fact already sits on, add a bullet under it citing *Vingt mille* as "VML I.13 ¶12" (VML II.n for its second part), marked *(Drafted.)*, with its quote copied character for character from that paragraph of `texts/vml-1870/`;
- where *Vingt mille* says something *L'Île* contradicts (a date, a measure, a count, a name), put both readings, quoted and cited, on the card's **Open** line and card neither. Hetzel's note III.16 n1 already says the dates do not agree: quote it there too. Never reconcile them;
- a subject *L'Île* names from *Vingt mille* that has no card yet (the three men, the Vigo bay, the coral cemetery, the Maelstrom, and the like) gets a new card in the right folder (people/, places/, things/), cited from *L'Île* first and *Vingt mille* under it, under the name *L'Île* gives it; if *L'Île* gives no name ("un professeur français, son domestique et un pêcheur canadien"), card it under that description and give *Vingt mille*'s names as a *Vingt mille* fact, cited;
- a thing in *Vingt mille* that *L'Île* does not mention is not carded.

THE FORM. As the cards already in place: each fact one bullet, its cite and its mark, the French words under it (`  - quote: ...`), copied exactly. Mark what the text states *(Drafted.)*, your inference *(My reading, to confirm.)*. Add VML to **Appears in:** as "VML I.13, VML II.22" after the *L'Île* chapters. Never delete or reword a line already on a card; an Open line recording a gap may be replaced when you answer it from *Vingt mille*, with the answer carded.

WRITE ONLY: the cards named above under READ, new cards in world/people/, world/places/ and world/things/ for subjects as above, and your report: plan/tasks/task-20261121-05-carding/report-vml.md. Do not run `tools/cards.py build`. If the tool refuses the report file, do not work around it: your final message is the report.

CHECK before you finish: `python3 tools/quotes.py CARD --in texts/fr-1875/*.md texts/vml-1870/[0-9]*.md` on every card you touched (run from the repository's folder), and `python3 tools/links.py`.

YOUR REPORT (the file, and the same text as your final message): the cards made and the cards extended, as two lists; each *L'Île* statement you traced, with the *Vingt mille* cite you found (or "not found", with what you searched); the discords put on Open lines; questions for the author, each with your recommendation; one line of totals (cards made, cards extended, facts added).
