# Prompt: write the closed-book quiz (v1)

*One agent that reads the prose and the clue register. Its key is never shown to a reader.*

```text
You are writing a closed-book quiz for readers of a novel, in the folder {REPO}. Every file
is read-only except your two outputs. Run no git commands. Do not launch agents.

Read the chapters {CHAPTERS}, the clue register plan/reread-hooks.md, and each chapter's
clue notes in story/notes/<N>-*.md (the Clues line). Per chapter, write:
- two or three "should know" questions on what the page must land (who did what, where,
  what changed), each keyed to the exact line that lands it;
- where the register or the clue notes list a hook planted in the chapter, one "guess"
  question, keyed to the true answer from the notes, with what counts as too plain, on
  target, off, or too faint.

Questions must be answerable from memory by someone who read the chapter once. No question
may name the hidden truth. Write the questions to {QUIZ} and the key to {KEY}.
```
