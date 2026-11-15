# Workflows: the procedures

A workflow is a procedure a task cites instead of restating: its loop, its prompts, its checks and its lessons. It comes with the clone of the kit, as `plan/workflows/`; a book can later pull the kit's improved workflows with git. When a task develops a method worth keeping, the method comes here and the task cites it; each run's lessons are appended to the workflow's Lessons.

**Rules every workflow follows:** the marks; the ledger first; at most two agents, none spawning another (but for lookup assistants, [the librarian](drafting/prompts/librarian.md)), each with a named file list; every run logged in the token log; no git commands in any agent; fresh agents (not forks) for critics and readers; every finding quotes the text, and the quote is checked; work inside the horizon.

The two largest are **[drafting/](drafting/README.md)**, the drafting and criticism chain, and **[reader-tests](reader-tests.md)**, unit tests for a novel by chapter. Which stage uses which workflow is in `kit/pipeline/`.

## Every workflow

**Basic** workflows run from the first chapter. A **Refinement** is added when its trigger shows up; each workflow's first line says so.

| Workflow | Tier | Add it when |
|---|---|---|
| [actor-log](actor-log.md) | Refinement | an offstage actor drives a beat |
| [aims-sweep](aims-sweep.md) | Refinement | a critic or drafter treats a "the reader feels…" line as already done |
| [apply-terms](apply-terms.md) | Refinement | a placeholder name is settled |
| [arc-pitch](arc-pitch.md) | Refinement | an arc has enough frames to lay out |
| [capture-notes](capture-notes.md) | Refinement | the writer brings an outside document |
| [card-audit](card-audit.md) | Refinement | cards pass about 1,500 words |
| [card-existing](card-existing.md) | Basic |  |
| [character-sheet](character-sheet.md) | Basic |  |
| [consistency-check](consistency-check.md) | Refinement | several chapters are outlined and a horizon is about to be drafted |
| [daily-life-study](daily-life-study.md) | Refinement | scenes default to the reader's own world |
| [dictation](dictation.md) | Refinement | a chapter is graded thin or none |
| [distill](distill.md) | Refinement | a card collects restatements |
| [draft-cards](draft-cards.md) | Refinement | a second chapter meets people a drafter made up |
| [drafting/](drafting/README.md) | Basic | the core; its later steps are Refinements, each marked |
| [echo-audit](echo-audit.md) | Refinement | an outcome rhymes with real history |
| [ereader](ereader.md) | Refinement | a stretch is long enough to read as a book |
| [habits](habits.md) | Refinement | one character's tic shows up on another |
| [interest-check](interest-check.md) | Refinement | a volume is refined and a dull stretch is feared |
| [ledger-roll](ledger-roll.md) | Refinement | a ledger file runs past its day |
| [logic-check](logic-check.md) | Refinement | the arc turns on timing, travel or who-knows-what, or an outline already broke on a date or a cause |
| [outline-clean](outline-clean.md) | Refinement | outlines written before a restructure are about to be redrafted from |
| [proposals](proposals.md) | Refinement | the setting needs a set of things the notes leave thin |
| [publication](publication.md) | Refinement | a volume is about to be released (once per volume) |
| [reader-tests](reader-tests.md) | Basic | the key and the blind probe; the story questions, reread test and quiz are Refinements, each marked |
| [readings-inventory](readings-inventory.md) | Refinement | readings pile up |
| [restructure](restructure.md) | Refinement | a topic file passes about 5,000 words with two subjects |
| [retire](retire.md) | Refinement | closed tasks pile up |
| [retrospective](retrospective.md) | Basic |  |
| [reveal-pacing](reveal-pacing.md) | Refinement | the book withholds a large truth |
| [ripple](ripple.md) | Refinement | a settled change contradicts earlier notes |
| [scene-outlines](scene-outlines.md) | Basic |  |
| [series-critic](series-critic.md) | Refinement | a clue's plant and payoff are both drafted |
| [task-form](task-form.md) | Basic |  |
| [telephone-decay](telephone-decay.md) | Refinement | an in-world text (a scripture, a legend, an old record) must hide the truth beneath it |
| [voice-render](voice-render.md) | Refinement | the writer wants to listen |

## Belongs here, and does not

- **Belongs:** a reusable procedure (`name.md`), its prompt files (`name/`), and its lessons.
- **Does not:** a run's output (that goes to the task's folder), lore (to the cards), rulings (to the ledger).
