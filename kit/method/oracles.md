# Oracles for prose: critics, guards and calibration

## The problem

Software has tests. A test gives a verdict nobody argues with: it passes or fails. Fiction has nothing like it. Whether a scene works is a judgment.

Without a verdict, a model working hard toward "good" will produce the look of good. It smooths away whatever a reader would object to without fixing what was wrong. It is not dishonesty. It is what happens when the only target is "make it read well" and nothing outside the model checks the result.

## Two grades of check

- **A mechanical check** gives a verdict the agent did not write: a script, a grep, a count. "Is this quote in the chapter?" "Does this link resolve?" "Is the word *okay* in the narration?" Prefer these wherever they exist.
- **A judgment** comes from reading. A critic's opinion of a scene is a judgment. It raises the floor; it never proves anything.

The kit uses mechanical checks wherever it can, and wraps every judgment in one.

## Critics: judgments pushed toward verdicts

A critic is a fresh agent asked one narrow question about a chapter or an outline.

- **One question each.** "Is this good?" gets praise. "Where does this contradict the notes?" gets lines. The kit's critics are listed in [critics.md](../../plan/workflows/drafting/critics.md).
- **Primed to look hard.** The voice critic is told "I think this chapter is poorly matched with the voice. Can you tell me where?" It finds more, real and false. The verification and the writer filter the false ones.
- **Fresh eyes.** A critic never sees the writer's reasoning, the conversation, or the outline's proposals when it judges the page. It is a new agent, not a fork of the session.
- **Every finding quotes the text.** A script checks each quote is really there (`tools/quotes.py`). A finding whose quote does not resolve is dropped, and the drop is counted against the critic.
- **Every finding cites a rule.** If the rule it cites does not exist, the finding is dropped.

## Calibration and honesty

A critic that has never been tried on planted faults has no measured recall, so its "no findings" says nothing. So each critic is scored on a clean chapter, a planted copy and a weak chapter, and again whenever its prompt or model changes, and it is trusted only once it meets the trust bars for recall and precision, which you set for your own book ([the procedure](../../plan/workflows/drafting/principles.md#5-calibrated-before-it-is-trusted)). This is the most important habit in the kit. And "the critics found nothing" never means "done": the writer accepts, rejects or defers each finding, and only the writer accepts a chapter. The guards against a reviser or writer learning to please a critic are in [principles §7](../../plan/workflows/drafting/principles.md#7-keeping-critics-honest).

## The one real oracle: reader tests

There is one test of prose with a true answer key: your notes say how your world works.

- **The spec:** per chapter, what a blind reader must get, must not get, and may only guess, written from the notes before the prose.
- **The blind probe:** a fresh agent reads only the prose and explains the world; a plain thing it cannot explain is shown too thinly, a hidden thing it states as sure is a leak.
- The procedure is in [reader-tests](../../plan/workflows/reader-tests.md).

## Model readers score model prose high

The interest check's model readers rate model prose above comparable human prose, so use them for where a reader slides within your book, never to rank it against a human one ([the numbers](../../plan/workflows/interest-check.md#reading-the-scores)).

## Every number says how it was made

A report that gives a number (a score, a count, a share) says how it was made and where it is weakest: "counted by grep; dialogue not excluded; the simile count is rough." Then the writer can check it with a closer look instead of taking it on trust.
