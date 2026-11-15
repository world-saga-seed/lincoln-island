# World Saga Seed: a method for writing a long-form novel with Claude Code

This kit is a set of workflows. Each one is a procedure Claude Code can run on your book: what it is for, when to run it, what it reads, its steps, its prompts as templates, its checks, what it produces, and the lessons and failure modes that came out of using it. They were developed over many months on one long series. Everything specific to that series has been taken out. What is left is the procedures, some small tools, and one toy novel carried through every stage as an example.

It is for a fiction writer with existing material (a manuscript, a half-draft, a folder of notes) who wants to work with Claude Code without the story drifting, without the model's habits taking over the voice, and without losing their own decisions. You do not need to be technical. It suits long work best: a novel of 80,000 words or more, or a series.


> **Alpha.** This is a work in progress, shared privately with a few early testers before a public release. What it has been tested on so far: one long series (three volumes, about 250,000 words) in **first person, past tense**. Other narrations (close third, omniscient, several viewpoints, an expressive narrator) have been through one test of a single chapter, and the fixes it found are in the kit: a POV file that every critic reads ([the template](plan/templates/pov.md)) an attribution test for several viewpoints, and a knowledge guard so an unreliable narrator's wrong beliefs are voiced on purpose and never corrected ([the template](plan/templates/knowledge.md)). They have not yet carried a whole book, so expect rough edges there.
>
> **What you need:** a computer with Claude Code installed and signed in. You do not need to know Python or git: Claude does. The kit's scripts use Python 3 and the book's history is kept in git; Claude checks both are there, helps you install either if it is missing, and runs every script and git command for you. After the setup the daily work can run from a phone ([Working from a phone](#working-from-a-phone)). A full render uses a lot of tokens: one chapter through the drafter and its critics runs to several hundred thousand, and a volume to many millions. Start with one chapter. The token log ([plan/templates/tokens.md](plan/templates/tokens.md)) shows what each step costs on your book.
>
> **Feedback:** open an issue for anything that breaks, confuses you, or makes Claude do something odd. Say which workflow and step you were on.
## The big ideas

1. **The drafting and criticism chain.** Prose has no compiler, so a chapter goes through a chain cheapest first: scripts and greps, then narrow critics that each ask one question and must quote the text, then a script that throws out any finding whose quote is not really there, then a reviser that sees only the verified findings, then the checks again. Critics are trusted only after they have been tested on planted faults. **[plan/workflows/drafting/](plan/workflows/drafting/README.md)**, the largest part of the kit.
2. **Reader tests: unit tests for a novel, by chapter.** For each chapter, a spec of what a blind reader **must get**, **must not get**, and **may only guess**, written from your notes before the prose exists. Fresh readers who have never seen the notes read the prose and are scored against it: a secret they come back sure of is a leak; a plain thing they cannot work out is shown too thinly. **[plan/workflows/reader-tests.md](plan/workflows/reader-tests.md)**.
3. **You give the key frames; Claude fills the tweens.** You supply the scenes and beats you see; Claude places them and proposes what goes between, marked as proposals. Where a chapter has no key frame, Claude writes a brief and you dictate. **[dictation](plan/workflows/dictation.md)**, **[arc-pitch](plan/workflows/arc-pitch.md)**.
4. **Every decision written once, as a ruling, and every line marked.** A dated ledger of your rulings; one short card per person, place and thing; every line Claude adds marked as settled, proposal or reading, so your book never blurs with the model's suggestions. **[kit/method/marks-and-ledger.md](kit/method/marks-and-ledger.md)**, **[kit/method/cards.md](kit/method/cards.md)**.
5. **Outlines before prose, to a horizon.** The story is worked out in outlines, which are cheap to change, up to a horizon; then drafted, read and corrected; then outlined on. **[kit/method/horizon.md](kit/method/horizon.md)**.
6. **You are the only one who says "done".** Critics find, Claude recommends, you decide.

## How to start

A clone of the kit is the skeleton of your book: the workflows, templates and tools are already where the book needs them.

Claude does the technical steps; you say what you want. Open Claude Code in an empty folder named for your book and say: "Set up this folder as a book from the World Saga Seed kit at <the kit's address>, check Python 3 and git are installed, delete the example, and run the clean check." Behind that request:

1. Claude clones the kit into the folder (or you use GitHub's "Use this template").
2. Claude deletes `example/` and runs `python3 tools/check_clean.py`, which must pass. The example stays readable in the kit's repository.
3. You put your manuscripts in `existing/` (drag them into the folder) and give Claude the working title for `CLAUDE.md` (the rest is filled in after the interview). Then start the intake by saying:

> Read CLAUDE.md, then plan/workflows/README.md, then kit/interview/intake.md. Do the intake on my existing work in existing/: list what is there, what kind of material each file is, and what you would ask me first. Do not change any file in existing/. Write your report to plan/tasks/ and stop.

4. Then the interview ([kit/interview/](kit/interview/README.md)), one or two sessions. After it, Claude sets up the rest of `plan/` ([stage 03](kit/pipeline/03-set-up-plan.md)) and you begin.

A book cloned from the kit can later pull improved workflows from it: ask Claude to update the kit, and it shows you any place where the new version meets your own edits.

## Working from a phone

Set up once on the computer; then the writing loop can run from a phone. Everything still runs on the computer, in the book's folder: the files, the scripts, the agents. The phone is a window onto that session through Claude Code's Remote Control, so you can dictate a key frame on a walk, rule on a critic's finding from the couch, or comment while you read on an ereader.

**Once, at the computer:** the setup in How to start. Then start a session in the book's folder with Remote Control on, by typing `claude --remote-control "My book"` (the one command you type yourself), and open it from the Claude app on your phone. If the session is closed, `claude remote-control --continue` reattaches to the last one.

**What works well from the phone:** the interview and the key-frame walk (answer by voice or by typing); dictating a scene; ruling on questions, which Claude puts a few at a time, each with a recommendation; starting a render and coming back when it is done; commenting while you read ([the read](plan/workflows/ereader.md#the-read-comments-from-the-phone)).

**The gotchas:**
- **The computer must stay on, awake and online,** with the session open. If it sleeps, the phone loses the session; set its power settings so it does not. For daily work, a small always-on machine is better than a laptop: a Raspberry Pi 5 (8 GB) or a mini PC running Linux, with the book on an SSD rather than an SD card, on wired network. Claude Code runs on it as on any Linux machine; you reach it only through the phone, and Claude can push the book to a private remote each day so a dead card or drive loses nothing.
- **Don't read diffs or long critic reports on the phone.** Ask Claude for the verdict in a few lines, then the findings one at a time with its recommendation. The kit's `CLAUDE.md` already tells Claude to answer a phone in a few lines.
- **Permission prompts come to the phone.** Read what you approve, as you would at the desk; an agent run or a push is worth a second look.
- **The ereader book has to reach the reader.** Copy it over at the computer, or put the build folder in a cloud folder the reader syncs.
- **Autocorrect and voice typing swap words.** Claude reads each message by the scene it points at, and asks only when a misread word could change a ruling.
- **Long runs cost tokens whether you watch or not.** Each run is logged ([the token log](plan/templates/tokens.md)); check it at the computer now and then.

## Start here: your first chapter

The shortest path through the method, for one chapter:

1. The [intake](kit/interview/intake.md).
2. The [interview](kit/interview/README.md). The style samples are picked here, from the intake's candidates.
3. [Set up `plan/`](kit/pipeline/03-set-up-plan.md).
4. Card the existing work: [card-existing](plan/workflows/card-existing.md) for the people, places and things, [scene-outlines](plan/workflows/scene-outlines.md) prompt D, and [character-sheet](plan/workflows/character-sheet.md) for the narrator.
5. Outline one chapter ([scene-outlines](plan/workflows/scene-outlines.md) prompt O) and write its key ([reader-tests §1](plan/workflows/reader-tests.md#1-the-key)). For the first chapter the arc outline's head is enough: the shape, the ending and the chapter list as far as they are known, filled in by hand from the interview's answers.
6. Fill in [rulings.md](plan/workflows/drafting/rulings.md) and draft the chapter ([drafter.md](plan/workflows/drafting/drafter.md)).
7. Run [mechanical.md](plan/workflows/drafting/mechanical.md), the facts critic and the voice critic ([critics.md](plan/workflows/drafting/critics.md)), then [verify.md](plan/workflows/drafting/verify.md) and [reviser.md](plan/workflows/drafting/reviser.md).
8. Run the [blind probe](plan/workflows/reader-tests.md#3-the-blind-probe) on that chapter.
9. Close the session ([retrospective.md](plan/workflows/retrospective.md)).

Everything else is a Refinement; each says when to add it.

## The workflows

The [kit/pipeline/](kit/pipeline/README.md) is the one map of stages to workflows: twelve stages in order. The work runs as tasks and waves ([kit/method/tasks-and-waves.md](kit/method/tasks-and-waves.md)).

| Tier | Workflows | When |
|---|---|---|
| **Basic** | the intake and interview; [card-existing](plan/workflows/card-existing.md); [task-form](plan/workflows/task-form.md), [retrospective](plan/workflows/retrospective.md); [scene-outlines](plan/workflows/scene-outlines.md), [character-sheet](plan/workflows/character-sheet.md); the core of [drafting/](plan/workflows/drafting/README.md) (the drafter, mechanical checks, the facts and voice critics, verify, reviser); [reader-tests](plan/workflows/reader-tests.md) (the key and the blind probe) | from the first chapter |
| **Refinement** | everything else | each workflow's first line says when to add it; the full list is in [plan/workflows/](plan/workflows/README.md) |

## Map of the kit

| Folder | Holds |
|---|---|
| [plan/workflows/](plan/workflows/README.md) | **The kit.** Every procedure, complete in itself, with its prompts. [drafting/](plan/workflows/drafting/README.md) is the largest section. |
| [plan/templates/](plan/templates/README.md) | Empty forms for the plan, tasks, ledger, cards, sheets, outlines, the reader-test spec, reports. |
| [tools/](tools/README.md) | Fourteen small Python scripts (standard library only): links, cards, tells and banned words, repeats, refrains, sounds, first use, reading lists, aged lines, quotes, attribution, knowledge, EPUB, and the clean check for a new book. |
| [kit/interview/](kit/interview/README.md) | The intake and interview script. |
| [kit/pipeline/](kit/pipeline/README.md) | The twelve stages in order: when each runs and which workflows it uses. |
| [kit/method/](kit/method/README.md) | The reasons: tasks and waves, the book's memory, oracles for prose, marks and the ledger, cards, horizons, key frames, agent limits, craft principles, closing cleanly. |
| [existing/](existing/README.md) | Where your manuscripts and notes go. Claude reads it and never changes it. |
| `example/` | A toy novel through every stage in miniature, with a worked run of the drafting chain and a reader-test spec. The only thing you delete to start a book; it stays readable in the kit's repository. |
| [CLAUDE.md](CLAUDE.md) | The instructions Claude reads in your book's folder. A template: the title now, the rest after the interview. |

## Four things to know first

- **It is slow at the start on purpose.** The first weeks are interview, cards and outlines. That is where the book is decided.
- **Model readers flatter model prose.** They rate it roughly 0.7 to 0.9 above comparable human prose. The kit uses model readers to find where a reader slides within your book, never to rank it against human books. Your own read is the one that counts.
- **Every number here was measured on another book** (reader scores, the recall and precision bars, card and file sizes, batch sizes). Before trusting one, run it on a chapter you know is good and one you know is weak, and set your own.
- **The rules are yours to change.** When a rule stops serving your book, change it in `plan/README.md` and say why.

## License

The docs are [CC BY 4.0](LICENSE): use and adapt them freely, with credit. The scripts in `tools/` are [MIT](tools/LICENSE). The license applies only to the files published in this repository. Anything you make with the kit is your own (your book, your notes, your cards and your plan/), and the license claims nothing over it. If you share the kit's files or an adaptation of them, give credit. For a book made with the kit, credit is asked, not required: *Made with World Saga Seed, by Karl Nelson.*
