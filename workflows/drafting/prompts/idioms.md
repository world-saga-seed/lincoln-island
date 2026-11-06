# Prompt: out-of-world phrase finder (v1)

*One batch, narration only. The banned list finds what is already on it; this finds what should be.*

Make the narration-only file first, so the critic reads nothing else: strip the dialogue (text in double quotes) from the batch's chapters into one scratch file, keeping line numbers per chapter.

```text
You are reading a novel narrated by {NARRATOR}: {WHO THEY ARE, IN ONE LINE: where and when
they live, and what they have never seen or heard of}. Read only {THREAD}; do not read
anything else.

List every phrase in the narration that only makes sense to someone outside that world:
- idioms and stock phrases that carry a picture from elsewhere;
- animals, machines, sports, foods, money, stories, places, measures and units of time
  the narrator could not know;
- single words that carry an outside picture (for example, a modern word in a
  historical narrator's mouth);
{EXTRA_KINDS}

Dialogue counts only when {NARRATOR} speaks it. Do not list plain words with an innocent
sense unless the sense here is the outside one.

For each: the exact quote, 25 words at most; its line; the outside picture it carries; and
one shifted phrasing the narrator could say instead, built from their own world, not a
synonym. If you find nothing, say so; inventing a finding is worse than missing one.

Write your list to {OUT}, headed "# Out-of-world phrases in {RANGE}", numbered. Run no git
commands. Do not launch agents. Every file is read-only except that output file.
```

**For a book set in our own world and time,** this critic changes its question: "List every phrase that a reader would recognize as a stock phrase, a cliché, or a model's habit, and every word wrong for the narrator's age, place or period." The form is the same.
