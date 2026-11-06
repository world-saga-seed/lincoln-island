# Drafting and criticism: the chain

*Basic.*

This is the core of the method. Everything before it (the interview, the cards, the outlines, the key frames) exists so that a chapter can be drafted from a clear brief. Everything here exists so that the draft can be checked without a test suite, and so that the model's habits never become the book's voice.

The chain runs **cheapest first**. A grep costs nothing and catches what a critic would otherwise spend its attention on. A critic costs a fresh agent and catches what a grep cannot. The writer's read costs the most, and comes last, on a chapter that has already been cleaned.

## The chain, in order

| # | Step | Kind | Runs on | File | Tier |
|---|---|---|---|---|---|
| 0 | **Gate:** the horizon is accepted for drafting | the writer | the horizon | [the gate](#the-gate) | Basic |
| 1 | **Draft** one chapter per agent, from its outline, cards, voice sheet and rulings | judgment | each chapter | [drafter.md](drafter.md), [prompts/drafter.md](prompts/drafter.md) | Basic |
| 2 | **Mechanical checks:** banned words, texture numbers, links, first appearances | mechanical | each chapter | [mechanical.md](mechanical.md) | Basic |
| 3 | **Per-chapter critics:** facts (Basic); coverage and slip, setup and belief (Refinements) | judgment | each chapter | [critics.md](critics.md) | Basic |
| 4 | **Per-batch critics:** voice and mechanism, last (Basic); continuity, out-of-world phrases, habits (Refinements) | judgment | each batch of two or three | [critics.md](critics.md) | Basic |
| 5 | **Verify** every finding: the quote resolves, the rule exists, duplicates merged | mechanical | every report | [verify.md](verify.md) | Basic |
| 6 | **Dispose:** each verified finding fixed, held, or put to the writer | judgment | the batch paper | [verify.md](verify.md#dispositions) | Basic |
| 7 | **Revise** from a snapshot, on the verified findings only | judgment | the batch | [reviser.md](reviser.md), [prompts/reviser.md](prompts/reviser.md) | Basic |
| 8 | **Re-check:** the greps and scripts again; the keep list still on the page; a facts check on the changed passages | mechanical, then judgment | the changed passages | [reviser.md](reviser.md#re-check) | Basic |
| 9 | **Invention check:** a small separate run on the logged inventions | judgment | the inventions log | [principles.md](principles.md#the-invention-check), [prompts/invention-check.md](prompts/invention-check.md) | Refinement |
| 10 | **Card the drafted details** so the next drafter meets the same stair | judgment, quotes checked | the batch | [draft-cards](../draft-cards.md) | Refinement |
| 11 | **Register pass** across the whole volume, once every batch is settled | mechanical count, judgment fix | the volume | [register-pass.md](register-pass.md) | Refinement |
| 12 | **Landing check:** every settled beat is on the page | mechanical, then the writer | the volume | [register-pass.md](register-pass.md#the-landing-check) | Refinement |
| 13 | **Fold-back:** the draft into the outline and notes; the Next pass list | judgment, quotes checked | each chapter | [fold-back.md](fold-back.md), [prompts/fold-back.md](prompts/fold-back.md) | Refinement |

Then the stretch goes to the [reader tests](../reader-tests.md) (the blind probe first), the interest check, and the writer's ereader read. Their comments join the Next pass lists, and the second drafting pass drafts from those lists.

## The pieces

| File | Tier | What it holds |
|---|---|---|
| [principles.md](principles.md) | Basic | What makes a critic trustworthy: one narrow question, quotes, fresh eyes, calibration, versioned prompts; the invention check |
| [rulings.md](rulings.md) | Basic | **The rulings of the page:** your house style, the one file every drafter and critic reads. A template you fill in |
| [drafter.md](drafter.md) | Basic | What a drafter gets and must not get; batches; style samples; the drafter's report |
| [mechanical.md](mechanical.md) | Basic | The greps and scripts, their thresholds, and how to read them against your own pages |
| [critics.md](critics.md) | Basic | The critics, one dimension each: what each asks, gets and never gets |
| [verify.md](verify.md) | Basic | Checking findings, merging them, and the dispositions |
| [reviser.md](reviser.md) | Basic | The reviser's rules, and the re-check after it |
| [register-pass.md](register-pass.md) | Refinement | The volume-wide pass on repeats and attention, and the landing check |
| [fold-back.md](fold-back.md) | Refinement | Bringing outlines and notes up to the draft, and listing what changes next pass |
| [prompts/](prompts/) | as their critic | The prompt templates, one per role, with `{PLACEHOLDERS}` to fill |

A worked run on the example's scene is in the kit's example (in the kit's repository, `example/reports/`): the scene, two critic reports, the verified list, the revision and the re-check.

## The gate

The one gate for drafting a horizon. **Basic:**

1. the outline and notes are marked;
2. `rulings.md` is filled in and the writer has read it;
3. the style samples are in `story/voice/samples/`;
4. the key (and the story questions, if used) cover the horizon's chapters;
5. the two critics (facts, and voice and mechanism) are calibrated, or the writer accepts that the first batch is their calibration;
6. no chapter in the horizon is graded **none** for key frames (a chapter graded **thin** may proceed, noted in the batch paper).

**Conditional:**

- the logic and consistency findings are settled and folded back, if the [logic](../logic-check.md) and [consistency](../consistency-check.md) checks ran;
- a ripple scan is done, if dictation ran;
- the clue register lists what each chapter plants, if the book plants clues;
- the actor log is current, if an offstage actor drives a beat.

The writer says "draft". Until then, the outlines are the work.

## The rhythm

- **Basic: one chapter at a time, in story order.** Each drafter reads the finished draft before its chapter, so no continuity critic is needed.
- **Refinement: side-by-side batches** of two or three chapters, in story order, at most two agents at once (the agent limit holds here too), then critics on each, and the continuity critic on the seams.
- **The writer reads each chapter or batch as it lands** and redirects. The next batch does not wait for the read: the drafting continues, and the writer's notes go into the Next pass lists. Stop only if the read finds a problem in the rulings themselves, because then every later batch would repeat it.
- **Every step writes to the batch paper** in the task's folder: what each drafter chose, every critic's findings, what was verified, what was fixed, held or put to the writer.
- **Progress is never measured in drafted words.** A chapter is at stage "refined" when the chain is done, and "accepted" only when the writer says so.

## What it costs

Per chapter:

- **Basic:** about 7 runs: the drafter, the facts critic, the voice critic, the reviser, the facts re-check, and the open and asked probe runs.
- **Full:** add coverage and slip, setup and belief, continuity, out-of-world phrases and habits critics, the invention check, draft-cards, and the chapter's share of the register pass, fold-back, reader tests and interest check.

Measure tokens on your first chapter (Claude Code shows usage per agent) and note it in `state.md`; a full volume runs to many millions of tokens. It is cheaper than the writer finding the same faults by hand, and the critics get cheaper to trust as their calibration builds.

**Budget note.** When usage is tight, cut in this order: run setup and belief only on chapters with a big event; merge habits into the voice critic; skip the out-of-world critic once the banned list has stopped growing. Never cut verification, and never cut the facts critic.
