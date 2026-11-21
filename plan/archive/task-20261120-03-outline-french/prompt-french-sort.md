# The French sorter's prompt (R1120-39)

*Filled in for each sorter: {PART} (s1, s2).*

---

You are sorting short French phrases that have crept into the English notes and outlines of a study of Jules Verne's *L'Île mystérieuse*. The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone. Write no files: your answer is your final message.

READ ONLY: plan/archive/task-20261120-03-outline-french/french-sort-{PART}.tsv. Each row: an id, a French span, how often it occurs, and one line it occurs in, for context.

The rule of the run: the notes are written in English, and French appears only in the cited quotes. Sort each span into one of four bins:

- **name**: a proper name of a person, place, ship, book or work (Cyrus Smith, Granite-house, pointe de l’Épave, le Bonadventure, Vingt mille lieues sous les mers). Kept as it is.
- **term**: a word the book keeps in French and an English text would keep too, or a measure or title with no fair English (e.g. "Cheminées" as the castaways' name for their shelter, "convicts", "corral"). Kept, and listed.
- **wording**: the line is about the French words themselves: a misprint, a variant spelling, two wordings set side by side, or a phrase whose exact French the argument depends on (e.g. "pin pigeon" against "pin pignon"; "la veille" where the point is what "la veille" refers to). Kept as it is.
- **translate**: anything else. Give a plain English rendering that fits the context line, keeping its sense and its numbers exactly.

Where a span mixes a name into French (e.g. "à six milles environ des Cheminées"), it is "translate", and the English keeps the name ("about six miles from the Chimneys"). If the span is not French at all (an English phrase the script caught), give the bin "skip".

YOUR ANSWER: one line per id, in id order, tab-separated, with nothing before or after the table but one header line:

    id	bin	english
    17	translate	the day before
    18	name
    19	wording

The english column is filled only for "translate". Then, after the table, one line "TERMS:" followed by the term-bin spans, comma-separated.
