# Next: what to do now

Run when the writer asks "what now?", "what next?" or "what should I do?", and at the start of a session that has no task named. It answers with at most three options, one recommended. Claude does the checks; the writer's time goes only to what needs them.

**Grade.** Mostly mechanical: steps 1 to 3 read files and run scripts. The choice in step 5 is a judgment, given as a recommendation.

## The checks, in order

Each check can change the ones after it, so they run in this order. **The order of the checks is not the order of the answer** (step 5): the writer's part is offered first whenever the writer is at the keyboard, and the machine work runs beside it.

0. **What is already in motion.** Agents still running; uncommitted work (`git status`); commits from another window (`git log` since the session's start); a push waiting on the writer's word. Nothing new starts on top of these: a running batch is finished and checked, uncommitted work is committed or named.
1. **Close what is done** ([retrospective](retrospective.md)). Due when any task's status says done but it is not archived, or the roadmap's Now is older than the last day of commits. The checks after this read the roadmap, so a stale one gives a wrong answer. A due retrospective is the first option, and the steps after it are answered from the rewritten roadmap.
2. **The working size** (scripted, `python3 tools/sizes.py`). Lists what is too big to work with: fields over 500 words (to distill, [distill](distill.md)), cards and sheets over 3,000 words, outline and design files over 8,000 words (to page). This is a queue, not a blocker. It blocks only what reads it: a field over the limit in the next chapter's bundle is distilled before that chapter is drafted. Ranked by use: what the next horizon's bundles give comes first.
3. **The natural next workflow.** From the last wave's status and the roadmap's Next, take the first stage in the [pipeline](../../kit/pipeline/README.md) whose "Done when" fails for the current horizon. Then check that stage's gate: stale actor logs, an open `interview.md`, a chapter graded none. A gate that fails is the work, before the stage. A wave already drafted waits on "next wave"; it is offered, never started.
4. **The interview that moves things forward.** Rank the roadmap's Waiting list and every open task's questions by what each answer unblocks: the next workflow's gate first, then the questions that settle the most proposals, then the rest. Old is not a reason. The top three or four become one round of [the interview](arc-pitch.md#the-interview), each with its context and a recommendation.

## The answer

5. **At most three options, ranked,** each in a line or two:
   - what it is, and why now;
   - the writer's time it takes, and Claude's (tokens, by the token log's past runs of the same step);
   - **Recommended** on one.

   When the writer is at the keyboard, the interview (check 4) or a gate the writer must rule comes first, paired with machine work that runs meanwhile: "rule these four (your ten minutes) while the retrospective runs". When the writer is away or on a phone, offer only what needs a few words of answer.
6. **The writer answers** with a number, "as recommended", "next wave" (for a drafted wave), or something else. Claude runs it, and ends with the offer of the next step, never starting it unasked.

## Lessons

- **A stale roadmap answers wrong.** Close what is done before choosing what is next.
- **Size is a queue.** Distilling every large field at once costs more than the bundles it saves; distill what the next chapters read.
