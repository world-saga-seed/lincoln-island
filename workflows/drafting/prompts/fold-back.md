# Prompt: fold-back (v1)

*One drafting batch per agent. It edits only its chapters' outlines and notes.*

```text
You are bringing a novel's outlines and notes up to date with its draft, in the folder
{REPO}. Every file is read-only except the outlines and notes of your chapters. Run no git
commands; what changed since the draft is given to you below. Do not launch agents. Other sessions may have unsaved edits: never revert or reformat anything you did not
change, and edit by small exact replacements.

Your chapters: {CHAPTERS}. For each: the prose story/prose/N-*.md, the outline
story/outline/N-*.md and the notes story/notes/N-*.md. Write your report to {REPORT}.

Read first: README.md; plan/README.md (the marks and the rules);
plan/workflows/drafting/fold-back.md (the job, and the Next pass form);
plan/workflows/drafting/rulings.md; story/voice/voice.md. Then, for your chapters: the prose,
outline and notes in full; the batch paper {PAPER}; the drift rows in plan/state.md that
name your chapters; what changed in the notes and cards since the draft,
{CHANGES}; and the cards and sheets for
everyone and everything on your pages.

Per chapter:
1. The draft into the outline and notes. Fold each choice the batch kept into the beat it
   belongs to, in one line, marked "(Proposal, from the draft, N.)" with N linked to the
   prose file. Do not copy prose into the outline; keep lore in the notes. Delete outline
   text the draft and its batch settled otherwise; deleting a "(Settled ...)" line needs a
   source that settles it, so if you have none, leave it and list the draft as drift. In
   the notes' "Open and flags", replace each item the draft answered with its answer,
   marked "(Answered by the draft, N; overturnable.)". Never fold a choice that
   contradicts a settled line: that is drift.
2. The Next pass list. Add "## Next pass" as the last section of the notes, in the form
   and kinds the workflow gives: drift, held, beat, voice (at most eight, the strongest),
   length. Every quote in backticks, copied exactly, 25 words at most, and it must
   resolve: copy the Next pass section to a scratch file, run python3 tools/quotes.py
   <that file> --in story/prose/N-*.md --backticks, and fix every miss.

Every line you add carries a mark. Delete stale text; do not strike it. Verify every link
and anchor you write. Never edit prose, cards, sheets, the arc outlines or plan/state.md;
put what they need in your report.

Report, headed "# Fold-back, {GROUP}": by chapter, what you folded and the Next pass count
by kind; what shared files need (quote, file, why); state.md drift rows to delete or carry;
questions only the writer can answer, each with the plain option first and a
recommendation. Finish with a one-line tally.
```

**`{CHANGES}`** is supplied by the supervisor, who runs the git command itself (agents run no git): the output of `git log --since=<draft date> --stat -- world story/notes`.
