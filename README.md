# World Saga Seed: a method for writing a long-form novel with Claude Code

This kit is a set of workflows. Each one is a procedure Claude Code can run on your book: what it is for, when to run it, what it reads, its steps, its prompts as templates, its checks, what it produces, and the lessons and failure modes that came out of using it. They were developed over many months on one long series. Everything specific to that series has been taken out. What is left is the procedures, some small tools, and one toy novel carried through every stage as an example.

It is for a fiction writer with existing material (a manuscript, a half-draft, a folder of notes) who wants to work with Claude Code without the story drifting, without the model's habits taking over the voice, and without losing their own decisions. You do not need to be technical. It suits long work best: a novel of 80,000 words or more, or a series.


> **Alpha:** a work in progress, shared privately with a few early testers before a public release. What has been tested, what you need and what it costs are in [Before you start](#before-you-start).

**What it is not:** it does not write your book for you. You bring the story, the scenes you see and every decision; Claude places your key frames, proposes what goes between them, drafts to your rulings and checks the result, and nothing is done until you say so.

## The big ideas

1. **Reader tests: unit tests for a novel, by chapter.** For each chapter, a spec of what a blind reader **must get**, **must not get**, and **may only guess**, written from your notes before the prose exists. Fresh readers who have never seen the notes read the prose and are scored against it: a secret they come back sure of is a leak; a plain thing they cannot work out is shown too thinly. It gives the prose a real answer key. **[plan/workflows/reader-tests.md](plan/workflows/reader-tests.md)**.
2. **Critics must quote, and a script checks the quotes.** The commonest way a model critic fails is to invent a problem with confidence. Every critic finding must quote the text it is about, and a script throws out any finding whose quote is not really in the chapter before anyone acts on it. **[plan/workflows/drafting/verify.md](plan/workflows/drafting/verify.md)**.
3. **The drafting and criticism chain.** Prose has no compiler, so a chapter goes through a chain cheapest first: scripts and greps, then narrow critics that each ask one question, then the quote check, then a reviser that sees only the verified findings, then the checks again. Critics are trusted only after they have been tested on planted faults. **[plan/workflows/drafting/](plan/workflows/drafting/README.md)**, the largest part of the kit.
4. **You give the key frames; Claude fills the tweens.** You supply the scenes and beats you see; Claude places them and proposes what goes between, marked as proposals. Where a chapter has no key frame, Claude writes a brief and you dictate. The workflows: **[dictation](plan/workflows/dictation.md)** (you tell a scene, Claude writes it down to your words) and **[arc-pitch](plan/workflows/arc-pitch.md)** (Claude pitches the shape of an arc for you to accept or change).
5. **Every decision written once, as a ruling, and every line marked.** A dated ledger of your rulings; one short card per person, place and thing; every line Claude adds marked as settled, proposal or reading, so your book never blurs with the model's suggestions. **[kit/method/marks-and-ledger.md](kit/method/marks-and-ledger.md)**, **[kit/method/cards.md](kit/method/cards.md)**.
6. **Outlines before prose, to a horizon.** The story is worked out in outlines, which are cheap to change, up to a horizon; then drafted, read and corrected; then outlined on. **[kit/method/horizon.md](kit/method/horizon.md)**.
7. **You are the only one who says "done".** Critics find, Claude recommends, you decide.

## Before you start

**What has been tested.** One long series (three volumes, about 250,000 words) in **first person, past tense**. Other narrations (close third, omniscient, several viewpoints, an expressive narrator) have been through one test of a single chapter, and the fixes it found are in the kit: a POV file that every critic reads (template: [plan/templates/pov.md](plan/templates/pov.md)); an attribution test for books with several viewpoints (prompt: [plan/workflows/drafting/prompts/attribution.md](plan/workflows/drafting/prompts/attribution.md)); and a knowledge guard, so an unreliable narrator's wrong beliefs are voiced on purpose and never corrected (template: [plan/templates/knowledge.md](plan/templates/knowledge.md)). They have not yet carried a whole book, so expect rough edges there.

**What you need:** a computer with Claude Code installed and signed in. You do not need to know Python or git: Claude does. The kit's scripts use Python 3 and the book's history is kept in git; Claude checks both are there, helps you install either if it is missing, and runs every script and git command for you. After the setup the daily work can run from a phone ([kit/phone.md](kit/phone.md)).

**What it costs.** A full render uses a lot of tokens: one chapter through the drafter and its critics runs to several hundred thousand, and a volume of twenty chapters to many millions. On a Pro or Max plan that draws on your usage limit, not a bill, and a volume will not fit in one day's allowance; on the API, at Claude Opus 5.5's price in November 2026 ($4 per million tokens read, $20 per million written), a chapter costs a few dollars and a volume tens of dollars. Prices and limits change, so measure: render one chapter first, then check `/usage` in Claude Code (or the bill) to see what share it took, before you start a volume. The token log (its form is [plan/templates/tokens.md](plan/templates/tokens.md)) records what each step cost on your book.

**Where your manuscript goes.** As with any Claude Code session, the files Claude reads are sent to Anthropic to be processed, under the terms of your plan; check your account's privacy settings for whether your chats may be used to train models. The kit sends nothing anywhere else: its scripts run on your computer, and the book is pushed to a remote only if you ask.

**Feedback:** open an issue for anything that breaks, confuses you, or makes Claude do something odd. Say which workflow and step you were on.

## How to start

A clone of the kit is the skeleton of your book: the workflows, templates and tools are already where the book needs them.

Claude does the technical steps; you say what you want. Open Claude Code in an empty folder named for your book and say: "Set up this folder as a book from the World Saga Seed kit at <the kit's address>, check Python 3 and git are installed, delete the example, and run the clean check." Behind that request:

1. Claude clones the kit into the folder (or you use GitHub's "Use this template").
2. Claude deletes `example/` and runs `python3 tools/check_clean.py`, which must pass. The example stays readable in the kit's repository.
3. You put your manuscripts in `existing/` (drag them into the folder) and give Claude the working title for `CLAUDE.md` (the rest is filled in after the interview). Then start the intake by saying:

> Read CLAUDE.md, then plan/workflows/README.md, then kit/interview/intake.md. Do the intake on my existing work in existing/: list what is there, what kind of material each file is, and what you would ask me first. Do not change any file in existing/. Write your report to plan/tasks/ and stop.

4. Then the interview ([kit/interview/](kit/interview/README.md)), one or two sessions. After it, Claude sets up the rest of `plan/` ([stage 03](kit/pipeline/03-set-up-plan.md)) and you begin.

To run the daily work from a phone once this is done, see [kit/phone.md](kit/phone.md).

A book cloned from the kit can later pull improved workflows from it: ask Claude to update the kit, and it shows you any place where the new version meets your own edits.

## Start here: your first chapter

The shortest path through the method, for one chapter:

1. The [intake](kit/interview/intake.md): Claude lists what is in `existing/` and what it would ask you first.
2. The [interview](kit/interview/README.md): your answers on the book, written down, and the style samples (passages of your own prose the voice is measured against), picked from the intake's candidates.
3. [Set up `plan/`](kit/pipeline/03-set-up-plan.md): the roadmap, the state of each chapter and the ledger of rulings, ready to use.
4. Card the existing work: one card per person, place and thing ([card-existing](plan/workflows/card-existing.md)); scene outlines taken back out of the prose you have already written ([scene-outlines](plan/workflows/scene-outlines.md), its "deconstruct" prompt); and a character sheet for the narrator ([character-sheet](plan/workflows/character-sheet.md)).
5. Outline one chapter ([scene-outlines](plan/workflows/scene-outlines.md), its "outline" prompt) and write its reader-test key: what a blind reader must get, must not get and may only guess ([reader-tests, the key](plan/workflows/reader-tests.md#1-the-key)). For the first chapter the arc outline's head is enough: the shape, the ending and the chapter list as far as they are known, filled in by hand from the interview's answers.
6. Fill in [rulings.md](plan/workflows/drafting/rulings.md), the rules the drafter must keep, and draft the chapter ([drafter.md](plan/workflows/drafting/drafter.md)).
7. Check it: the scripted checks ([mechanical.md](plan/workflows/drafting/mechanical.md)), the facts critic and the voice critic ([critics.md](plan/workflows/drafting/critics.md)), the quote check ([verify.md](plan/workflows/drafting/verify.md)), and a revision that fixes only the verified findings ([reviser.md](plan/workflows/drafting/reviser.md)).
8. Run the [blind probe](plan/workflows/reader-tests.md#3-the-blind-probe): a fresh reader's answers on that chapter, scored against its key.
9. Close the session ([retrospective.md](plan/workflows/retrospective.md)): what was learned written down and the plan's state brought up to date.

Everything else is a Refinement; each says when to add it.

## The workflows

The [kit/pipeline/](kit/pipeline/README.md) is the one map of stages to workflows, in order. The work runs as tasks and waves ([kit/method/tasks-and-waves.md](kit/method/tasks-and-waves.md)).

| Tier | Workflows | When |
|---|---|---|
| **Basic** | the intake and interview; [card-existing](plan/workflows/card-existing.md); [task-form](plan/workflows/task-form.md), [retrospective](plan/workflows/retrospective.md); [scene-outlines](plan/workflows/scene-outlines.md), [character-sheet](plan/workflows/character-sheet.md); the core of [drafting/](plan/workflows/drafting/README.md) (the drafter, mechanical checks, the facts and voice critics, verify, reviser); [reader-tests](plan/workflows/reader-tests.md) (the key and the blind probe) | from the first chapter |
| **Refinement** | everything else | each workflow's first line says when to add it; the full list is in [plan/workflows/](plan/workflows/README.md) |

## Map of the kit

| Folder | Holds |
|---|---|
| [plan/workflows/](plan/workflows/README.md) | **The kit.** Every procedure, complete in itself, with its prompts. [drafting/](plan/workflows/drafting/README.md) is the largest section. |
| [plan/templates/](plan/templates/README.md) | Empty forms for the plan, tasks, ledger, cards, sheets, outlines, the reader-test spec, reports. |
| [tools/](tools/README.md) | Small Python scripts (standard library only): links, cards, tells and banned words, repeats, refrains, sounds, first use, reading lists, aged lines, quotes, attribution, knowledge, EPUB, and the clean check for a new book. |
| [kit/interview/](kit/interview/README.md) | The intake and interview script. |
| [kit/pipeline/](kit/pipeline/README.md) | The stages in order: when each runs and which workflows it uses. |
| [kit/phone.md](kit/phone.md) | Running the daily work from a phone, and an always-on host. |
| [kit/method/](kit/method/README.md) | The reasons: tasks and waves, the book's memory, oracles for prose, marks and the ledger, cards, horizons, key frames, agent limits, craft principles, closing cleanly. |
| [existing/](existing/README.md) | Where your manuscripts and notes go. Claude reads it and never changes it. |
| `example/` | A toy novel through every stage in miniature, with a worked run of the drafting chain and a reader-test spec. The only thing you delete to start a book; it stays readable in the kit's repository. |
| [CLAUDE.md](CLAUDE.md) | The instructions Claude reads in your book's folder. A template: the title now, the rest after the interview. |

## Four things to know first

- **It is slow at the start on purpose.** The first weeks are interview, cards and outlines. That is where the book is decided.
- **Model readers flatter model prose.** On the interest check's 1-to-5 scale, model readers scored model prose about 0.7 to 0.9 points above published human books of the same kind, measured by giving the same readers both ([interest-check](plan/workflows/interest-check.md)). The kit uses model readers to find where a reader slides within your book, never to rank it against human books. Your own read is the one that counts.
- **Every number here was measured on another book** (reader scores, the recall and precision bars, card and file sizes, batch sizes). Before trusting one, run it on a chapter you know is good and one you know is weak, and set your own.
- **The rules are yours to change.** When a rule stops serving your book, change it in `plan/README.md` and say why.

## License

The docs are [CC BY 4.0](LICENSE): use and adapt them freely, with credit. The scripts in `tools/` are [MIT](tools/LICENSE). The license applies only to the files published in this repository. Anything you make with the kit is your own (your book, your notes, your cards and your plan/), and the license claims nothing over it. If you share the kit's files or an adaptation of them, give credit. For a book made with the kit, credit is asked, not required: *Made with World Saga Seed, by Karl Nelson.*
