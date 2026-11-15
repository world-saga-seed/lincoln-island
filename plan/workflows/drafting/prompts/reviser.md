# Prompt: reviser (v2)

*One batch, from a snapshot, on the verified findings only.*

```text
You are revising chapters of a novel in progress, in the folder {REPO}, on verified critic
findings. Every file is read-only except these: {CHAPTERS}. Run no git commands of any kind.
Do not launch agents.

Read: story/voice/voice.md, story/voice/banned.txt and plan/workflows/drafting/rulings.md
(the rules); two or three of the style samples in story/voice/samples/;
the verified findings, {FINDINGS}; the keep list, {KEEP}; and the batch paper, {PAPER},
whose fixes section lists every fix already made on these chapters. Do not undo any of
those fixes; some quotes in the findings may have changed because of them.

Address every finding on the list: cut, trim or make plain, as the direction says, or by a
better cut of your own that meets the same point. Where a finding's quote is already gone,
say so and move on. Each beat said once; no sentence reused across the chapters or from
earlier chapters; the narrator never lines up the plot for the reader.

Rules:
- Change wording only. Add no fact, object, person, name or event; move no beat. Where a
  cut leaves a gap, close it with a few plain words.
- Keep every line of dialogue unless a finding names it.
- Keep every line on the keep list exactly.
- Never cut or reword a clue: a line in plan/reread-hooks.md, a chapter's clue notes, or
  any name, order or number a reader could solve the story from. Where a finding asks for
  that cut, keep the clue and say so.
- Keep each chapter inside the texture of the samples, measured with
  python3 tools/tells.py <file>. Do not chop. Split every sentence tells.py prints as a
  "knot" that runs two main clauses through a semicolon.
- Word ranges: {WORDS}. Do not cut below; if the findings force it, say so.
- Everything in the rulings holds.
- When done, run python3 tools/tells.py <file> --banned story/voice/banned.txt and fix any
  narration hit.

Finish with a short report: each finding by number and what you did (or why you left it);
for each chapter the word count and the tells.py line, before and after; then an
Inventions list of any fact you added that the notes lack (expected: none), one line each:
the fact, the line, the cards it touches.
```
