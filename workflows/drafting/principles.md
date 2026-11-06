# Principles of a critic

*Basic.*

Prose has no compiler. A critic is the nearest thing: an agent asked one narrow question about a chapter, made to point at the text, run where it cannot see what it should not. It is still a judgment, not a verdict. These principles push it as close to a verdict as it can get.

## 1. One narrow question

A broad question gets broad praise. "Is this chapter good?" returns three paragraphs of encouragement. "Where does this chapter contradict the notes?" returns lines.

So each critic owns one dimension, and its prompt says to ignore everything else, however tempting. Two small related questions can share a critic (coverage and slip; setup and belief) when they read the same files. Never more.

## 2. Primed to look hard

The voice critic's question opens: "I think this chapter is poorly matched with the voice. Can you tell me where?" A critic told something is wrong searches harder. The price is more false findings. Verification and the writer filter those. Precision (below) says whether the trade is paying.

## 3. Every finding points at the text

Every finding has the same form ([templates/critic-report.md](../../templates/critic-report.md)): the exact quote, copied character for character, 25 words at most; file and line; the rule it breaks (or the note it goes against), quoted; why, in one sentence; severity; and a one-line direction, never rewritten prose. Severity is **break** (breaks a stated rule or a settled fact), **weak** (allowed but poor, or resting on a proposal against a settled line), or **taste**.

The quote is what makes a judgment checkable. A script confirms each quote is really in the chapter (`tools/quotes.py`). A finding whose quote does not resolve is dropped, and the drop is counted. A critic that drops often is inventing.

Every prompt also says: "If you find nothing, say 'No findings' and stop. That is an acceptable answer. Inventing a finding is worse than missing one." And: "Do not rewrite. Do not praise."

## 4. Run where it cannot see what it should not

Each critic gets the files its question needs and nothing else. It never sees the writer's reasoning or the conversation, so it is a **fresh agent, never a fork** of the session. [critics.md](critics.md#why-each-excludes-what-it-excludes) lists, for each critic, what it gets and never gets, and why.

## 5. Calibrated before it is trusted

A critic that has never been tried on planted faults has no measured recall, so its "no findings" says nothing. So before a critic is trusted on a dimension, it is scored on two texts, then tried on a third:

1. **A clean one:** a chapter the writer is happy with. Copy it to the scratchpad.
2. **A planted one:** a copy of the same chapter with five to eight faults of the critic's dimension. Write the key where the critic cannot read it.

Run the critic on both. Then run it on **a weak one:** a chapter the writer knows is poor; a critic quiet on it is blind to real faults, not only planted ones. Verify the findings. Then sort them: on the planted copy, a finding on a planted fault is a hit. Any other finding, on either copy, goes to the writer. One the writer accepts is a real flaw in the "clean" chapter and joins the key. One the writer rejects is a false hit.

- **Recall** = planted faults found ÷ planted faults.
- **Precision** = (hits + accepted findings) ÷ all findings on the planted copy.
- **Clean findings:** the count on the clean original. On a chapter the writer is happy with, this should be near zero.

**Every number here** (reader scores, the recall and precision bars, card and file sizes, batch sizes) **was measured on another book.** Before trusting one, run it on a chapter you know is good and one you know is weak, and set your own.

Trust a critic at recall of about three in four and precision of about one in two (bars from another book: set your own, as above). Below either, revise the prompt and calibrate again. Record every run in `plan/state.md` under "Critic calibration": prompt version, planted, found, false hits, clean findings, recall, precision.

**Plant new faults every time.** A reused key teaches both critic and writer what to expect.

**Examples of planted faults**, by dimension, using the kit's toy example:

| Critic | Planted faults |
|---|---|
| Facts | the causeway two miles long; the lamp lit at dawn; Dell bringing the almanac in June |
| Voice | a modern word in narration ("stressed"); a hindsight line ("I would understand later"); a comparison the narrator could not know (a railway timetable, for a girl who has never seen a train) |
| Coverage | delete a beat; swap two beats; add a visitor the outline never sends |
| Slip | Wren reading the inspector's letter before it arrives; Wren saying what Agnes thinks rather than what she sees |
| Setup | a fisherman who happens by exactly when the inspector is in the water, with no earlier beat that sends him |
| Mechanism | the narration explaining the sandbar |
| Habits | Wren wiping her hands on her apron (Agnes's habit) |
| Belief | Agnes acting on something only Wren knows |

**The writer's own lines are the reference, not findings.** Give the voice critic the style samples as "the voice as the writer set it". At verification, drop any finding whose quote is in a sample (`grep -F` it there). Otherwise most voice findings land on the writer's own lines.

**Recalibrate whenever the prompt or the model changes.**

## 6. Prompts are versioned

Each prompt template carries a version. Every run logs the version it used. A change of wording is a new version, and a new version is calibrated before it is trusted.

| Version | Change |
|---|---|
| v1 | The template as given in `prompts/`. |

Rotate the wording between versions. The point is not novelty; it is that neither the critic nor the writer learns to satisfy a phrasing instead of the rule behind it.

## 7. Keeping critics honest

The risk is reward hacking aimed at prose: a reviser, or a writer, who learns what a critic flags and smooths that away without fixing what was wrong.

- **The writer does not read the critic prompts,** and the critic does not read the writer's notes or reasons.
- **Check the fix, not only the finding.** A finding "resolved" by deleting the line it quoted is not resolved. The supervisor reads each fix against its finding.
- **Watch for drift toward taste.** When most verified findings are "taste", the critic has run out of rules to check, and its findings are opinions.
- **A clean report is a result, not a success.** "No findings" on an uncalibrated critic means nothing.

## The invention check

*Refinement. Add this when inventions start contradicting cards.*

Invention is allowed. A drafter, a reviser, a register pass, an outliner may all add facts the cards do not hold. What is checked is whether each is **consistent**, not whether it is the best choice. People in a story do not pick the optimum; they pick what they would think of.

**The agent that invents logs; it does not check.** Checking means opening many cards, and that context dilutes the main task. So every pass that writes prose, tweens or proposals ends its report with an **Inventions** list, and appends the same rows to the task's `inventions.md`:

| # | The new fact, plainly | File:line | Cards it touches | Who made it |
|---|---|---|---|---|

**The check is a small separate run,** after the pass, one log at a time ([prompt](prompts/invention-check.md)). Its file list is the log, the lines cited, and the cards each row names, plus the setting's core rules. No agent on the main path runs it, and it edits nothing. For each row:

1. **Against the canon.** Grep the cards it touches. A clash is a break, and the fix takes the canon's version.
2. **Against what is to hand.** Could a person in that place, time and trade reach it, with the tools, materials and knowledge they have? Would they think of it? For a custom or an institution, also: what pressure made it, and what came of the same pressure in real history? No pressure and no precedent is a free invention: give it to the writer.
3. **Verdict:** **stands** (to the carding step), **reword** (consistent in substance, a word or a part wrong; give the fix), **break** (a canon clash; give the canon line), or **to the writer** (it touches a settled line or a key frame).

The supervisor applies rewords and breaks, sends the writer's items in the next batch of questions, and carries the stands to carding, marked *(Proposal, from the draft, NNNNN.)*.
