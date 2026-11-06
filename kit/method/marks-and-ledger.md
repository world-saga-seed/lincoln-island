# Marks and the ledger: whose line is this?

## Marks

Every line Claude adds to the notes or outlines carries a mark. A whole file written as a proposal is marked at its top.

| Mark | Means |
|---|---|
| *(Settled R0302-01.)* | The writer ruled it; the ruling is on the ledger under that ID |
| *(Settled by the writer, 2027-03-02.)* | The writer ruled it before the ledger existed, or in an edit |
| *(Proposal.)* | Claude's invention, waiting for the writer |
| *(Proposal, from the draft, 00400.)* | A drafter invented it on the page; carded so later chapters agree |
| *(My reading, to confirm.)* | Claude's reading of the writer's shorthand, or a gap it thinks the writer has already filled |
| *(Resolved by judgment, overturnable.)* | The writer asked Claude to decide, and it did |
| *(Aim.)* | An intended effect on the reader. A goal, not a fact; it lands only when a drafted scene shows it |
| *(Drafted.)* | What existing prose already holds, when that prose is taken apart into an outline |

Why marks matter: without them, a proposal reads as fact by the next session, and an agent builds on it. With them, a grep for *(Proposal.)* and *(My reading* is the list of decisions still open.

**The writer settles in place.** To settle a proposal, change its mark. To reject it, delete it. Nothing moves when it is accepted.

## The ledger

When the writer rules on something in conversation, the ruling goes on the ledger before any file is edited to match it.

- **One file per day:** `plan/settled/ledger/2027-03-02.md`.
- **One row per ruling,** with an ID made from the date: `R0302-01`, `R0302-02`, numbered afresh each day. Run `date` before the first ruling of a session.
- **Columns:** ID, Kind, Ruling, Date, Asked in, Home, Applies to.
  - **Kind:** settled-author (the writer's own call), settled-recommendation (the writer took Claude's recommendation), resolved-judgment (the writer asked Claude to decide).
  - **Ruling:** one plain sentence, stated once.
  - **Home:** the card or section that now carries it.
  - **Applies to:** every file it changes, each with a status: applied, pending, or drift (a draft that still says the old thing).
- **A replaced ruling** reads "Superseded by R0310-04." and nothing in the notes cites it any more.

## Rulings, not words

The writer's words in conversation are aspiration: fast, typed on a phone, sometimes garbled. The canon is the clean sentence on the card. So:

- The ledger and the cards carry the ruling, never a transcript of what the writer said.
- When the writer's typed words are unclear, set the scene first: read the card and later rulings on that topic. The meaning is usually plain once the context is in front of you. A typed line that seems to contradict settled canon may have lost a "not" to autocorrect; test that reading before moving canon.
- Ask only when two readings still differ in substance, and ask by the topic and where it was discussed, not by quoting the garbled words back.

## Remove stale text

The writer's process is to discuss, then settle. Older lines often go unpatched when a later ruling replaces them. That leftover is debris, not a decision. Delete it, say what was cut, and keep questions for what is truly still open.

## Settled decisions with reasons

A ruling on the ledger says what. Some decisions also need why. A decision about how the book works (a narrator rule, a genre line, a pacing law) gets its own file in `plan/settled/`, `settled-YYYYMMDD-slug.md`, with four parts:

1. **What was decided.**
2. **Why.**
3. **What it rejects** — the usual answer, named, so a later session recognizes it as already considered.
4. **What would unsettle it** — the conditions under which it stops being right.

The third part does the work. Without it, the next session, trying to help, restores the usual answer.

## Canon never cites a task

A task's papers are temporary. When a task closes, its results move to the cards and the ledger. A line in `world/` or `story/` cites its ruling by ledger ID, or its fact by the card that holds it, never a task paper. Only the ledger's "Asked in" column and the task logs point into `plan/tasks/`.
