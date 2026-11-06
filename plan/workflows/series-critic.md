# Series critic: is each clue fair, and still there?

*Refinement. Add this when a clue's plant and payoff are both drafted.*

## Purpose

A book that is a puzzle plants clues at several distances: a few chapters, a volume, across volumes, the whole series. Each is listed in the clue register, `plan/reread-hooks.md` ([form](../templates/reread-hooks.md)). A clue fails two ways: it reads too plainly, so a first reader guesses the payoff early; or it is too faint, or was cut in a redraft, so a rereader finds nothing to reread. This critic tests both, one clue at a time, with two fresh agents that never see the register's reasoning.

It is the per-clue form of the [reader tests](reader-tests.md)' reread test.

## When to run it

- On a clue when it enters the register, once its plants and payoff are drafted.
- After any redraft of a chapter the register lists as a plant: the informed pass alone, to confirm nothing was wiped out.
- Before a volume goes to the writer's read: every clue with a plant in the volume, blind pass.

## Steps

1. **Blind pass.** A fresh agent reads the plant chapters in order, prose only, and stops before the payoff. It answers: what does it think is going on with *the thing* (named neutrally: "the keeper's habit with the tide table"), and what does it guess will turn out true? Every guess quotes its lines.
   - **Guessed the payoff:** too readable. List the lines that gave it away.
   - **Read the plants as ordinary story:** the first read holds. Good.
   - **Confused or stopped by a plant:** flag the line.
2. **Informed pass.** A second fresh agent gets the payoff (as the truth) first, then the plant chapters in order, with the reread test's [informed-reader prompt](reader-tests/informed-reader.md). It explains each plant it now sees, quoting it.
   - **A plant in the register it does not find:** too faint, or gone. Check the text: if the line was cut or reworded in a redraft, it is a lost clue: restore it, or log the loss for the writer.
   - **A plant it finds that the register does not list:** add it, marked as found by the critic.
3. **Verify:** drop any finding whose quote is not in the text. Hand the rest to the writer with the clue's row.

## Rules

- At most two agents; the blind agent is never the informed agent; neither sees the register's Payoff or Keep columns.
- A clue whose payoff is not drafted yet gets the blind pass only, against the outline's payoff.
- Results go on the clue's row (date, pass, result) and in the task log.

## Prompt (blind)

> You are reading part of a novel, in the folder {REPO}. Read only {CHAPTERS}, in order; nothing else. Run no git commands; do not launch agents. When done: what do you think is going on with {THE THING, NAMED NEUTRALLY}? What do you guess will turn out to be true about it? Quote every line your answer rests on (exact, 25 words at most), and mark each guess sure or guessed. If you noticed nothing about it, say so. Write it to {OUT}.

## Lessons

- **Name the thing neutrally.** A blind prompt that names the secret ("the keeper's failing eyes") gives it away.
- **Lost clues come from trims and register passes,** not from drafters. Run the informed pass after every one.
