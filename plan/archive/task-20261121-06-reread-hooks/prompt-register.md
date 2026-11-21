# The register-builder's prompt

You are building the clue register for a study of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875). The French is the authority. The repository is the current folder; every path below is relative to it. Run no git commands of any kind, not even read-only ones; to see what you have written, read your file. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-hooks/ and nowhere else.

READ:
- plan/templates/reread-hooks.md (the form) and plan/workflows/series-critic.md (what the register is for);
- plan/archive/task-20261121-06-reread-hooks/clues-all.md: the Clues sections of the 62 chapter notes, gathered (each "## I.9" heading is a chapter; ¶ numbers are that chapter's);
- texts/README.md (how the French is cited) and the French, texts/fr-1875/NN.md (I.n is NN = n; II.n is 22 + n; III.n is 42 + n), the paragraphs you cite;
- texts/fr-1875/58.md ¶65 (III.16): the book's own list of the incidents Captain Nemo explains;
- texts/align/SUMMARY.md and, as needed, texts/align/NN-discords.md: where White's English translation cuts a line that is a clue (two are known: I.9 ¶105 and III.9 ¶41).

WRITE ONLY: plan/reread-hooks.md, and your report, plan/archive/task-20261121-06-reread-hooks/report-register.md. If the tool refuses the report file, do not work around it: your final message is the report.

THE REGISTER. The template's head and columns, with two changes: Distance is "chapter" (the next one or two), "part", or "book"; and Plants and Payoff cite the French as "I.7 ¶64". Two tables:
1. **The threads** (H1, H2, ...): each clue whose plants and payoff stand apart, or that the book leaves open. Group the Clues lines into threads: one row per thing, however many chapters plant it (for example, Top at the lake and at the well is one thread, or two if the text pays them off apart). Every incident in III.16 ¶65 gets a row whose Payoff is III.16 ¶65 (and any later paragraph that explains it). A thread the book never explains (say, the lead shot's first firer, if the Clues show it) has Payoff "none: left open", with the ¶ where the text last raises it.
2. **Near puzzles** (N1, N2, ...): Clues lines answered in the same chapter or the next (the smoke of I.9, the arrowheads of I.13), one row each, same columns.
- **The thing** is named neutrally, so that a blind reader is not told the answer: "the dog's return to the Chimneys", not "Nemo brings Top back".
- **Keep** is the decisive French words of each plant, copied character for character from the cited paragraph, with the text's own apostrophes (’); one quote a plant, separated by " / ". Where a Clues line already quotes the French, use that quote if it holds the plant.
- **Tests** is left empty.
After the tables, a section **Not a clue** listing any Clues line you judged not a clue (a plain fact, a measure), each with its chapter and one-line reason.

YOUR REPORT (the file, and the same text as your final message): the count of threads, near puzzles and not-a-clue lines; that every ¶65 incident has its row (list them with their IDs); any Clues line you could not place; any White cut you found that removes a plant (chapter, ¶, discord number); questions for the author, each with your recommendation.

CHECK before you finish: every Keep quote must be found in its cited paragraph: write a short script that reads each row's Plants and Keep and tests each quote against the paragraph, and fix any that fails.
