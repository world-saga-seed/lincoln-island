# Prompt: trim pass (v1)

```text
You are trimming chapters of a novel in progress, in the folder {REPO}, on two readers'
interest check. Every file is read-only except the chapter files on your list: {CHAPTERS}.
Run no git commands. Do not launch agents.

Read: story/voice/voice.md, story/voice/banned.txt and plan/workflows/drafting/rulings.md;
two style samples; the merged interest check, {MERGED}, and, for your chapters, the two
readers' notes beside it; each chapter's outline (only to see which lines are settled) and
its notes (the Clues line); the clue register plan/reread-hooks.md.

In each chapter, the passage both readers skimmed (the merged list's Trims) is cut down so a
reader no longer slides over it. Tighten that passage and its joins only: drop the steps,
items or repeats a reader gets at once; keep the one or two details that hold the narrator's
eye; keep every beat, so the scene still happens and still means what it meant. A typical
trim takes the passage to between a third and two thirds of its length.

Rules:
- Change wording only. Add no fact, object, person or event; move no beat.
- Never remove or reword a line that carries a settled outline line; trim around it.
- Never trim away a clue: keep every line the clue notes or the register point to, with
  every name, order and number in it, word for word. A line that looks like a clue and is
  listed nowhere is kept and reported.
- Keep every phrase on the keep list {KEEP} exactly.
- Keep the texture inside the samples' range (python3 tools/tells.py <file>): do not chop.
- When done, run python3 tools/tells.py <file> --banned story/voice/banned.txt and fix any
  narration hit.

Report per chapter: what you cut (the passage's opening words, its word count before and
after), the chapter's word count and tells line before and after, and anything you could not
trim without touching a settled line or a clue. Then an Inventions list (expected: none).
```
