# Why plan/: the book's memory between sessions

## The problem

Claude does not remember the last session. Each new session knows only what is on disk. Within a long session, early instructions fade, and when the conversation is summarized to make room, the summary keeps conclusions and loses the reasons.

A long novel suffers from this more than most work. A detail settled in week two is contradicted in week nine because nobody had it in front of them. A ruling given in passing is gone by the next morning. And a model left to its own habits writes the usual version of a scene: where the writer did something unusual on purpose, the model, trying to help, puts the usual thing back.

## The answer

Keep the book's memory in plain files that Claude reads at the start of every session.

- `world/` and `story/` hold **what is true**: the cards, the outlines, the notes, the voice sheet. A chapter is checked against them, never the reverse.
- `plan/` holds **the work and the decisions**: the roadmap, the state of every chapter, the tasks, the ledger of rulings, the settled decisions, the workflows and the archive.

A session reads the roadmap and the state table, picks up one task, does it, checks it, writes down what changed, and closes cleanly. The next session starts from the files.

## Why it works

- **The files teach better than rules.** Claude follows what it sees. A few good cards and one good outline show the form more reliably than a page of instructions. So the kit's habit is: let the files show each convention, and keep written rules for what the files cannot show (commit only when asked; never trim a clue).
- **A decision with its reason survives.** A settled decision that names what it rules out ("not a ghost story") lets a later session recognize the usual answer as already considered, instead of proposing it as an improvement.
- **Small steps can be checked.** One chapter outline can be checked against its cards. A whole book cannot be checked at once. So the work is cut into small steps, each checked before the next.
- **Every claim can be traced.** A line in the notes carries a mark saying whose it is, and a ruling carries an ID that leads to the ledger. When something goes wrong, the trail says where it came from, and that is the file to fix.

## When something goes wrong, fix the source

If Claude keeps producing the same wrong thing, correcting the output each time does not stop it. Find what it was following (a card that says the wrong thing, a stale outline line, an old task paper still lying in the working set) and fix that. Then the next session reads the right thing.

## What it costs

Every task costs a little upkeep: a task file, a ledger row, a line in the state table, a clean close. That cost is steady and it is the reason methods like this get dropped. Weigh it against a contradiction found in volume three that needs five chapters redrafted.

## What it is not

- It is not a way to write faster at first. The first weeks are slower.
- It is not a substitute for taste. The method catches drift and contradiction. Whether a scene is good is for readers, and the last reader is the writer.
- It is not a cage. When a rule stops serving the book, change it, and write down why.

## The test for anything said in a session

Ask: will this survive the session?

| | Survives |
|---|---|
| A card, an outline, a ledger row | Yes. Every later session reads it. |
| A task's working papers | Until the task closes. Then its results move to the cards and ledger, and the papers are archived. |
| Something said in conversation | No. If it matters, it goes on the ledger now. |

The last row is the one to watch.
