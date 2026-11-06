# Story kit: workflows for writing a long novel with Claude Code

This kit is a set of workflows. Each one is a procedure Claude Code can run on your book: what it is for, when to run it, what it reads, its steps, its prompts as templates, its checks, what it produces, and the lessons and failure modes that came out of using it. They were developed over many months on one long series. Everything specific to that series has been taken out. What is left is the procedures, some small tools, and one toy novel carried through every stage as an example.

It is for a fiction writer with existing material (a manuscript, a half-draft, a folder of notes) who wants to work with Claude Code without the story drifting, without the model's habits taking over the voice, and without losing their own decisions. You do not need to be technical. It suits long work best: a novel of 80,000 words or more, or a series.

## The big ideas

1. **The drafting and criticism chain.** Prose has no compiler, so a chapter goes through a chain cheapest first: scripts and greps, then narrow critics that each ask one question and must quote the text, then a script that throws out any finding whose quote is not really there, then a reviser that sees only the verified findings, then the checks again. Critics are trusted only after they have been tested on planted faults. **[workflows/drafting/](workflows/drafting/README.md)**, the largest part of the kit.
2. **Reader tests: unit tests for a novel, by chapter.** For each chapter, a spec of what a blind reader **must get**, **must not get**, and **may only guess**, written from your notes before the prose exists. Fresh readers who have never seen the notes read the prose and are scored against it: a secret they come back sure of is a leak; a plain thing they cannot work out is shown too thinly. **[workflows/reader-tests.md](workflows/reader-tests.md)**.
3. **You give the key frames; Claude fills the tweens.** You supply the scenes and beats you see; Claude places them and proposes what goes between, marked as proposals. Where a chapter has no key frame, Claude writes a brief and you dictate. **[dictation](workflows/dictation.md)**, **[arc-pitch](workflows/arc-pitch.md)**.
4. **Every decision written once, as a ruling, and every line marked.** A dated ledger of your rulings; one short card per person, place and thing; every line Claude adds marked as settled, proposal or reading, so your book never blurs with the model's suggestions. **[method/marks-and-ledger.md](method/marks-and-ledger.md)**, **[method/cards.md](method/cards.md)**.
5. **Outlines before prose, to a horizon.** The story is worked out in outlines, which are cheap to change, up to a horizon; then drafted, read and corrected; then outlined on. **[method/horizon.md](method/horizon.md)**.
6. **You are the only one who says "done".** Critics find, Claude recommends, you decide.

## How to start

1. Make a folder for your book. Put your existing work in `existing/` inside it.
2. Copy the kit's `CLAUDE.md` into the folder and fill in the bracketed lines. Copy `workflows/` to `plan/workflows/`, `templates/` to `plan/templates/`, and `tools/` to `tools/`. This early copy is deliberate: the intake prompt below reads `plan/workflows/README.md`, though the rest of `plan/` is set up after the interview ([stage 03](pipeline/03-set-up-plan.md)).
3. Open Claude Code in the folder and say:

> Read CLAUDE.md, then plan/workflows/README.md, then the intake in [path to the kit]/interview/intake.md. Do the intake on my existing work in existing/: list what is there, what kind of material each file is, and what you would ask me first. Do not change any file in existing/. Write your report to plan/tasks/ and stop.

4. Then the interview ([interview/](interview/README.md)), one or two sessions. After it, Claude sets up `plan/` and you begin.

## Start here: your first chapter

The shortest path through the method, for one chapter:

1. The [intake](interview/intake.md).
2. The [interview](interview/README.md).
3. [Set up `plan/`](pipeline/03-set-up-plan.md).
4. Card the existing work: [scene-outlines](workflows/scene-outlines.md) prompt D, and [character-sheet](workflows/character-sheet.md) for the narrator.
5. Outline one chapter ([scene-outlines](workflows/scene-outlines.md) prompt O) and write its key ([reader-tests §1](workflows/reader-tests.md#1-the-key)).
6. Fill in [rulings.md](workflows/drafting/rulings.md), pick the style samples, and draft the chapter ([drafter.md](workflows/drafting/drafter.md)).
7. Run [mechanical.md](workflows/drafting/mechanical.md), the facts critic and the voice critic ([critics.md](workflows/drafting/critics.md)), then [verify.md](workflows/drafting/verify.md) and [reviser.md](workflows/drafting/reviser.md).
8. Run the [blind probe](workflows/reader-tests.md#3-the-blind-probe) on that chapter.
9. Close the session ([retrospective.md](workflows/retrospective.md)).

Everything else is a Refinement; each says when to add it.

## The workflows

The [pipeline/](pipeline/README.md) is the one map of stages to workflows: twelve stages in order. The work runs as tasks and waves ([method/tasks-and-waves.md](method/tasks-and-waves.md)).

| Tier | Workflows | When |
|---|---|---|
| **Basic** | the intake and interview; [task-form](workflows/task-form.md), [retrospective](workflows/retrospective.md); [scene-outlines](workflows/scene-outlines.md), [character-sheet](workflows/character-sheet.md); the core of [drafting/](workflows/drafting/README.md) (the drafter, mechanical checks, the facts and voice critics, verify, reviser); [reader-tests](workflows/reader-tests.md) (the key and the blind probe) | from the first chapter |
| **Refinement** | everything else | each workflow's first line says when to add it; the full list is in [workflows/](workflows/README.md) |

## Map of the kit

| Folder | Holds |
|---|---|
| [workflows/](workflows/README.md) | **The kit.** Every procedure, complete in itself, with its prompts. [drafting/](workflows/drafting/README.md) is the largest section. Copied into your book. |
| [interview/](interview/README.md) | The intake and interview script. |
| [pipeline/](pipeline/README.md) | The twelve stages in order: when each runs and which workflows it uses. |
| [method/](method/README.md) | The reasons: tasks and waves, the book's memory, oracles for prose, marks and the ledger, cards, horizons, key frames, agent limits, craft principles, closing cleanly. |
| [templates/](templates/README.md) | Empty forms for the plan, tasks, ledger, cards, sheets, outlines, the reader-test spec, reports. |
| [tools/](tools/README.md) | Six small Python scripts (standard library only): links, cards, tells and banned words, repeats, quotes, EPUB. |
| [example/](example/README.md) | A toy novel, *The Tide Clock*, through every stage in miniature, with a worked run of the drafting chain and a reader-test spec. |
| [CLAUDE.md](CLAUDE.md) | The instructions Claude reads in your book's folder. A template. |

## Four things to know first

- **It is slow at the start on purpose.** The first weeks are interview, cards and outlines. That is where the book is decided.
- **Model readers flatter model prose.** They rate it roughly 0.7 to 0.9 above comparable human prose. The kit uses model readers to find where a reader slides within your book, never to rank it against human books. Your own read is the one that counts.
- **Every number here was measured on another book** (reader scores, the recall and precision bars, card and file sizes, batch sizes). Before trusting one, run it on a chapter you know is good and one you know is weak, and set your own.
- **The rules are yours to change.** When a rule stops serving your book, change it in `plan/README.md` and say why.

## License

The docs are [CC BY 4.0](LICENSE): use and adapt them freely, with credit. The scripts in `tools/` are [MIT](tools/LICENSE). The license covers this kit only; it claims nothing over any book you make with it.
