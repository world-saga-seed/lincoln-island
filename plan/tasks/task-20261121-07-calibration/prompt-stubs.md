# The stub-builder's prompt (R1121-15)

You are building six stub cards into full cards, for a study of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875), from the French. The repository is the current folder; every path below is relative to it. Run no git commands of any kind, not even read-only ones; to see what you have written, read your files. Do not launch agents. Work alone.

THE STUBS: world/animals/red-worms.md, world/things/dwarf-acacia.md, world/things/tetras-lines.md, world/places/greenwich.md, world/things/sulphate-furnace.md, world/things/willow-bark.md.

READ: plan/templates/card.md; texts/README.md; the "What a card holds" section of plan/tasks/task-20261121-05-carding.md; a full card of the same folder for the form (for example world/things/tinder.md); each stub's Appears-in paragraphs in the French, texts/fr-1875/NN.md (I.n is NN = n; II.n is 22 + n; III.n is 42 + n), with a paragraph either side. To find other chapters that name the subject: `python3 tools/cards.py find WORD` or a search of `texts/fr-1875/`.

THE TASK. Build each stub into a full card in place: keep its head (rewrite the italic summary if it is no longer true), replace the stub's "Build if needed" line with the facts, each one bullet with its cite and mark and the French words under it, copied exactly (`    - quote: ...`), in the sections **What it is.**, **On the page.**, **Appears in:** and, where the text disagrees with itself, **Open:** (both readings quoted, neither carded). A card holds what is true of its subject, not the story's events. Mark what the text states *(Drafted.)*, your inference *(My reading, to confirm.)*. If the subject appears in other chapters than the stub lists, card those too and add them to **Appears in:**.

WRITE ONLY the six files named, and your report: plan/tasks/task-20261121-07-calibration/report-stubs.md. Do not run `tools/cards.py build`. If the tool refuses the report file, do not work around it: your final message is the report.

CHECK before you finish: `python3 tools/quotes.py CARD --in texts/fr-1875/*.md` on each card, from the repository's folder.

YOUR REPORT (the file, and the same text as your final message): each card with the chapters it now covers and its count of facts; any disagreement put on an Open line; questions, each with your recommendation.
