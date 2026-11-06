# Aims sweep: mark intentions apart from facts

*Refinement. Add this when agents read aims as facts.*

Finds every intended effect and claim of quality in the notes and marks it *(Aim.)*, so no agent reads an aim as something the story already does.

**An aim** is an intended effect on the reader or a claim of quality: it lands, earns, pays off, the reader feels or knows, it reads as, the irony works. **A fact** is what happens, what a character does or knows, how the setting works, or a rule about what the page shows. Leave facts alone.

**Grade.** Marks and splits only, never a changed fact. The diff is the check.

## The loop

1. **Agents by file group,** at most two, no file in two groups, logs to the task folder ([prompt](#prompt)).
2. **Touchstones:** collect the comparisons to other works the agents logged into one list in the story notes (the work, what it stands for here, where it applies), and point the inline comparisons at it.
3. **Check:** links resolve; `git diff --word-diff` shows only marks, splits and links; no settled mark lost.
4. **Present** the diff summary and anything left.

## Prompt

> The notes of a novel, in the folder {REPO}. Read `CLAUDE.md` and `plan/README.md`, then your files whole: {FILES}. Edit only those; write your log to {LOG}. Run no git commands; do not launch agents. Other agents edit other files: edit by small exact replacements. For each aim, put *(Aim.)* immediately before it. Where an aim is a clause in a longer sentence, split it into its own sentence after the fact it serves and mark that, moving words, never changing them (a joining "and", "so" or "which" may become a full stop). Keep every existing mark on the text it governs; a settled aim stays settled and gains *(Aim.)* too. Leave comparisons to other works in place and log each (file, heading, quote, what it stands for). Never reword or add a fact, rename a heading or delete a line. Log every change as a table, then a report under 150 words.

## Lessons

- Inside an italic aside, write the mark plain, `(Aim.)`, since nested asterisks break the italics.
- Most logged comparisons are genre references, not touchstones.
