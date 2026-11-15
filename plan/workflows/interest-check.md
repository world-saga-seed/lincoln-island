# Interest check: where a reader skims, and what to do about it

*Refinement. Add this when a volume is refined and a dull stretch is feared.*

Its prompts in [interest-check/](interest-check/) are Refinements, as the check is.

## Purpose

Before a volume is accepted, readers who know nothing of the notes read the prose in order and say where they would skim, what confused them, and whether they would read on. Reshoots and trims are made while the outlines still exist. It is a **guard against two dull stretches in a row**, not a ranking of the book.

**Grade.** A judgment, not a verdict. The writer decides every reshoot and trim.

## When to run it

After a volume is refined and before it is accepted; again after any reshoot or trim, on the same prompts.

## Inputs

- The volume's prose, in reading order.
- For any volume after the first, **the story so far:** a recap of the earlier volumes, about 1,000 words, written by one agent from their prose only (the cast, the terms as the pages gloss them, the events in order, the state at the end, the questions left open). Keep it, so a rescore uses the same one; rewrite it only when the earlier volumes change. Without it, a later volume reads cold and scores low.
- The clue register, and each chapter's clue notes.

## Steps

1. **Snapshot** the volume's prose to the scratchpad.
2. **Two readers** ([prompt](interest-check/reader.md)), fresh agents, independent, each reading the whole volume in order, prose only, after the recap if there is one. Two fixed personas, A and B, [given in the prompt](interest-check/reader.md), word for word every time so scores compare. Adjust B's genre to the book; never change the wording between volumes.
3. **The closed-book quiz** (the [reader tests](reader-tests.md#5-the-closed-book-quiz)): each reader answers from memory in its own session; a grader marks both.
4. **Merge** into `merged.md` in the task folder ([form](../templates/interest-merged.md)): scores side by side; what both flag is a finding, what one flags is taste; reshoot candidates (a chapter both score low, or a beat both find soft); trims (the same passage skimmed by both); shared confusions; the blind guesses set against the clue register (a guessed payoff is a hook too readable). Check every quote with `tools/quotes.py`; drop any that does not resolve.
5. **Read the spread, not the mean** (below).
6. **The writer picks:** reshoots go back through the outline and the drafter; trims go to the trim pass.
7. **The trim pass** ([prompt](interest-check/trim.md)), at most two agents, each with a fixed chapter list: cut only the flagged passage and its joins, wording only; every clue, every settled line and every keep phrase stays.
8. **Seam critics** ([prompt](interest-check/seam.md)) on the diffs against the snapshot: joins, **lost setups** (every cut detail grepped across later chapters), **lost clues** (always restored, listed first), lost meaning, rule breaks. Apply the fixes; a restore puts the snapshot text back.
9. **Landing check:** every keep phrase and every clue still on the page (`tools/quotes.py` on the keep list); rebuild the book.

## Reading the scores

- **Model readers score high.** These numbers, like every number in the kit, were measured on another book: check them against a chapter you know is good and one you know is weak. Ordinary competent published adventure scores about 3.0 to 3.3 on these readers; a recognized classic about 4; a raw one-pass model draft of a calm slice of life about 3.2. **Model readers rate model prose roughly 0.7 to 0.9 above comparable human prose,** so an absolute score never ranks the book against a human one.
- **Use them for:** where a reader slides within the book; agreement between the two readers; consistency between your own volumes. **The first accepted volume is the baseline:** each later volume is read against its profile with the same prompts.
- **Read for spread.** A book of daily life cannot hold constant interest, and lulls set up payoffs. **A lull is fine when the chapter after it lifts and when something in it pays off later.** Flag a lull only when nothing it sets up pays off, or when two lulls run together.
- **Half points are noise.** A move of half a point on one chapter between runs is the scale, not the chapter. A move counts when it is a whole point, or when both readers move the same way.

## Outputs

- `merged.md`; the trims and their seam reports; the rebuilt book; the reshoots on the roadmap.

## Lessons and failure modes

- **Clues outrank interest:** a skimmed passage that holds a clue is made livelier around it, never trimmed through ([no fix may cut a clue](reader-tests.md#how-failures-route-back)).
- **Grep every cut noun forward.** A cut breaks a setup more often than a join: a detail cut that a later line leaned on.
- **A settled line can protect a dull passage.** Trim around it and put the ruling to the writer.
- **A quiet stretch both readers flag is a structural note,** not something trimming fixes, because the readers reward pace and open questions.
- **Score secondary pieces in their volume, not cold.** A letter or interlude read alone loses the cast the book gave it and scores low.
- **Vary the landing.** Several pieces that each end on a twist read as predictable when every twist lands the same way. The fix is a different landing for each, not fewer twists.
- **Trust it for ranking chapters and for an opening's early-reader experience,** not for a slow burn's payoff, which it underrates by design.
- **The blind guesses test the hooks for free.** Read what each reader guessed against the clue register.
- **Give the readers neutral file names.** A slug such as `00900-the-stolen-ring.md` answers its own quiz question; copy the chapters to numbered names only.
- **The recap must carry the plants the stretch pays off.** A stretch read after a recap cannot test a payoff whose plant the recap leaves out. List the stretch's payoffs first and put each plant's line in the recap, plainly, without its meaning.
- **Speculations are hooks to sort.** Every guess a reader makes that cites a line goes on a list, marked **hit** (a plant read right), **near** (a plant read wrong) or **unplanted** (a pattern nobody planted). For each near and unplanted one the writer chooses: drop it, keep it as a red herring, or make the reader right and land it. A kept one joins the clue register, guarded like any clue.
- **A sag in the middle is often a routine shown again.** When both readers slide over the same stretch, look first for a journey, a counter or a camp shown in full for the third time. Cut it to a line from the third showing, and keep that chapter's own event whole. The [procedures critic](drafting/prompts/procedures.md) reads the digest's "Routines shown in full" to stop it at drafting.
- **An outside whole-volume read catches what batch critics cannot.** A critic that sees two or three chapters cannot count a volume. Each fault such a read finds that a script could count (a refrain's total, a description repeated word for word, a setting word used before it is set up, a long tangled sentence) becomes a mechanical check ahead of the batch critics. See [mechanical.md](drafting/mechanical.md#volume-checks-before-the-batch-critics).
- **Do not cut restraint because a reader found it strange.** Keep withholding in feeling and mystery; fix lapses of orientation (who, where, when, what a term means).
