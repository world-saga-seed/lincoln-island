# The French reviewer's prompt (R1120-39, second pass)

*Filled in for each reviewer: {PART} (r1, r2). Written after the first pass: a script put the sorters' English in place of French spans, but the spans had been cut at punctuation, so some lines came out half French ("the ladder had absolutely disappeared disparu").*

---

You are checking lines of English notes on Jules Verne's *L'Île mystérieuse*, after a script translated the French phrases in them. The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone. Write no files: your answer is your final message.

READ ONLY: plan/archive/task-20261120-03-outline-french/french-review-{PART}.tsv. Each row: an id, the place (file:line), the line before the script, and the line after it. Where before and after are the same, the line still holds French the script did not reach.

THE RULE. The line must be in English. These stay as they are:
- **proper names** of people, places, ships and books (Cyrus Smith, Granite-house, la pointe de l’Épave, Port-Ballon, the Bonadventure, Vingt mille lieues sous les mers);
- **these kept terms:** Cheminées (the Chimneys), pan coupé, déodars, poivrière, précintes, ptéropode, tétras, échidné;
- **French the line is about:** where the line discusses the French words themselves (a misprint, a variant spelling, two wordings set side by side, what "la veille" refers to). Keep those words in French, in backticks or quotation marks, as the "before" line has them;
- **citations** like (I.12 ¶41), marks like *(Drafted.)*, markdown, links and numbers, exactly.

FOR EACH ROW, decide:
- **ok**: the "after" line is good, fluent English that keeps the sense of "before".
- **fix**: anything else. Half-French phrases, doubled words ("disappeared disparu"), French left over, a wrong sense, a lost number, a broken mark or citation. Give the whole corrected line, starting from "after", in plain English, keeping everything listed above.

YOUR ANSWER: one line per id, in id order, tab-separated, with one header line and nothing else:

    id	verdict	line
    r1-1	ok
    r1-2	fix	- The corrected line, whole, exactly as it should stand in the file. *(Drafted.)*

The corrected line keeps the "before" line's leading "- " or other markdown. Do not add or drop lines. Do not wrap a line.
