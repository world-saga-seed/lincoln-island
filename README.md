# World Saga Seed: a method for writing a long-form novel with Claude Code

*"Saga" for long: a novel of 80,000 words or more, or a series, in any genre. "Seed" because a clone of the kit is the seed your book grows from.*

> **Alpha:** a work in progress, tested so far on one series, with its first outside testers starting now. Expect rough edges. What has been tested, what you need and what it costs are in [Before you start](#before-you-start).

This kit is for a fiction writer with existing material (a manuscript, a half-draft, a folder of notes) who wants to work with Claude Code without the story drifting, without the model's habits taking over the voice, and without losing their own decisions. You do not need to be technical. It suits long work best. You can also start from nothing: the method was first run with no manuscript at all, from the interview alone.

It is a set of workflows: procedures Claude Code runs on your book, each saying what it is for, when to run it, what it reads, its steps, its prompts, its checks and what it produces, with the lessons and failure modes that came out of using it. They were developed over many months on one long series. Everything specific to that series has been taken out. What is left is the procedures, some small tools, and one toy novel carried through every stage as an example.

**What it is not:** it does not write your book for you. Claude drafts the prose; you supply every scene and decision, and can write any chapter yourself and use only the checks and reader tests on it. Claude places your scenes, proposes what goes between them, drafts to your rulings and checks the result, and nothing is done until you say so.

## Words used here

- **Card:** one short note per person, place or thing, holding the facts the book has settled about it.
- **Ruling:** a decision you made about the story, written once, dated, in a list called the ledger. Two other files hold rules of other kinds: `rulings.md` is your house style for the prose (the rules every drafter keeps and every critic enforces, each citing the ledger line it came from), and `plan/README.md` holds the rules for how the work itself is run.
- **Marks:** every line Claude adds to your notes carries one of three: *settled* (you ruled it), *proposal* (Claude suggests it, not yet yours), or *my reading* (Claude's reading of your shorthand, for you to confirm). The prose itself carries no marks.
- **Key frame and tween:** a key frame is a scene or beat you see and give; a tween is what Claude proposes to go between your key frames.
- **Critic:** a fresh Claude agent that reads a drafted chapter and asks one question of it (do the facts match the cards? does the voice hold?).
- **Render:** taking a chapter from outline to checked prose: a drafter writes it, the critics check it, a reviser fixes what they found.
- **Horizon:** how far ahead the story is outlined before drafting starts; the outlines are worked out to it, then drafted, then outlined on.
- **Task and wave:** a task is one job for Claude, written as a file; a wave is a set of tasks run together.
- **Token:** the unit Claude's work is measured and billed in, about three-quarters of a word read or written.
- **Basic and Refinement:** Basic workflows run from the first chapter; a Refinement is added only when its trigger shows up.

## The big ideas

1. **Reader tests: unit tests for a novel, by chapter.** For each chapter, a spec of what a blind reader **must get**, **must not get**, and **may only guess**, written from your notes before the prose exists. Fresh readers who have never seen the notes read the prose and are scored against it: a secret they come back sure of is a leak; a plain thing they cannot work out is shown too thinly. It gives the prose a real answer key.
2. **Model readers flatter model prose, so they are used to compare within your book, never to rank it.** In one calibration, two model readers each read ten works whole on a 1-to-5 interest scale: five published human-written books and five model-written works. Model prose scored about 0.7 to 0.9 points above human books of the same kind. So the kit asks its readers where a reader slides within your book and what they get from it, and never trusts an absolute score. Your own read is the one that counts.
3. **Critics must quote, and a script checks the quotes.** The commonest way a model critic fails is to invent a problem with confidence. Every finding must quote the text it is about, and a script throws out any finding whose quote is not really in the chapter before anyone acts on it. That proves only that the quote is real: a real quote with a made-up problem still passes, which is why the critics are tested first (next) and you rule on each finding.
4. **Critics are tested on planted faults before they are trusted.** Each critic is run on a chapter with faults planted in it, and trusted only once it finds them. In the latest test, five versions of one chapter were written in five narrations with four faults planted in each: the critics, as they were before that test, caught 19 of the 20, and a blind attribution test (a reader who names whose head each unlabeled paragraph is in) caught the twentieth. The fixes that test found are now in the kit.
5. **The drafting and criticism chain.** Prose has no compiler, so a chapter goes through a chain cheapest first: scripts, then the narrow critics, then the quote check, then a reviser that sees only the verified findings, then the checks again.
6. **You give the key frames; Claude fills the tweens.** Claude places your scenes and proposes what goes between, marked as proposals. Where a chapter has no key frame, Claude writes a brief and you dictate the scene.
7. **Every decision written once, as a ruling, and every line marked.** Every line Claude adds is marked as settled, proposal or reading, so your book never blurs with the model's suggestions.
8. **Outlines before prose, to a horizon.** Outlines are cheap to change and prose is not, so the story is worked out in outlines first.
9. **You are the only one who says "done".** Critics find, Claude recommends, you decide.

## Before you start

**What happens to what you have already written.** Your files in `existing/` are never changed; they stay as the record. That is held by Claude's instructions, as the readers' blindness is (below), and git keeps a copy of every version besides. Claude reads them, puts the facts on cards and takes each scene back into an outline. Your own pages become the style samples every new draft is measured against. A chapter is redrafted only when you ask for it.

**What has been tested.** One long series (three volumes, about 250,000 words) in **first person, past tense**. Other narrations (close third, omniscient, several viewpoints, an expressive narrator) have been through one test of a single chapter, and the fixes it found are in the kit: a POV file that every critic reads (who narrates, how close, and what each narrator may know), the attribution test for books with several viewpoints, and a knowledge guard (what a narrator knows, wrongly believes and does not know, chapter by chapter), so an unreliable narrator's wrong beliefs are voiced on purpose and never corrected. They have not yet carried a whole book, so expect rough edges there.

**How blind the readers are.** Each reader and critic is a fresh agent, never a copy of the session that wrote the chapter, told to read only the prose and given neutral file names, so the test does not give itself away. That is held by the prompt, not by a locked sandbox. And the readers are the same kind of model as the drafter, so they can share its blind spots: something the model gets wrong without noticing, its readers may not notice either. That is one more reason your own read is the last test.

**What you need:** a computer with Claude Code installed and signed in. You do not need to know Python or git: Claude does. The kit's scripts use Python 3 and the book's history is kept in git; Claude checks both are there, helps you install either if it is missing, and runs every script and git command for you. After the setup the daily work can run from a phone ([kit/phone.md](kit/phone.md)).

**What it costs, in tokens and time.** Measured on the series the kit came from, one pass over a chapter of 2,000 to 5,000 words (the drafter, then the critics) took 350,000 to 600,000 tokens and about 15 to 25 minutes of Claude working on its own; you need not watch. A chapter usually takes more than one pass: a revision and a second check bring it to about a million tokens, and reruns add more. A volume of twenty chapters runs to tens of millions.
- **On a Pro or Max plan** this draws on your usage limit, not a bill, and a volume will not fit in one day's allowance.
- **On the API,** at Claude Opus 5.5's listed price (checked on 2026-11-15: $4 per million tokens read, $20 per million written, and much less for text read again from cache), a pass costs at most a few dollars. Most of what Claude reads is read again from cache, so a volume comes to tens of dollars; with nothing cached it could reach about $100.
- **Your own time** is the interview, your key frames, and reading and ruling on what the critics find. It has not been measured yet; if you test the kit, log yours.

Prices and limits change, so measure: render one chapter, then type `/usage` in Claude Code (or check the bill) to see what share it took, before you start a volume. The token log (its form is [plan/templates/tokens.md](plan/templates/tokens.md)) records what each step cost on your book.

**Where your manuscript goes.** As with any Claude Code session, the files Claude reads are sent to Anthropic to be processed, under the terms of your plan; check your account's privacy settings for whether your chats may be used to train models. The kit sends nothing anywhere else: its scripts run on your computer, and the book is copied to an online backup (such as a private GitHub repository) only if you ask.

**Feedback:** open an issue for anything that breaks, confuses you, or makes Claude do something odd. Say which workflow and step you were on. To give back an improvement you found (a better critic, a voice rule, a cheaper step), see [CONTRIBUTING.md](CONTRIBUTING.md): describe it in an issue, or send it yourself through your own fork, reviewed there first.

## How to start

A clone of the kit is the skeleton of your book: the workflows, templates and tools are already where the book needs them.

Claude does the technical steps; you say what you want. Open Claude Code in an empty folder named for your book and say: "Set up this folder as a book from the World Saga Seed kit at https://github.com/world-saga-seed/world-saga-seed, check Python 3 and git are installed, delete the example, and run the clean check." Behind that request, Claude clones the kit (a copy that remembers where it came from, so it can pull improvements later) into the folder, deletes the toy novel in `example/` (it stays readable in the kit's repository) and runs a check that nothing of the example is left.

Then you put your manuscripts in `existing/` (drag them into the folder) and give Claude the working title. Then, for your first chapter:

1. **The [intake](kit/interview/intake.md).** Say: "Read CLAUDE.md, then plan/workflows/README.md, then kit/interview/intake.md. Do the intake on my existing work in existing/: list what is there, what kind of material each file is, and what you would ask me first. Do not change any file in existing/. Write your report to plan/tasks/ and stop." You get a list of what is there and Claude's first questions.
2. **The [interview](kit/interview/README.md),** one or two sessions: your answers on the book, written down, and the style samples (passages of your own prose the voice is measured against), picked from the intake's candidates.
3. **[Set up `plan/`](kit/pipeline/03-set-up-plan.md):** the roadmap, the state of each chapter and the ledger of rulings, ready to use.
4. **Card the existing work:** one card per person, place and thing ([card-existing](plan/workflows/card-existing.md)); scene outlines taken back out of the prose you have already written ([scene-outlines](plan/workflows/scene-outlines.md), its "deconstruct" prompt); and a character sheet for the narrator ([character-sheet](plan/workflows/character-sheet.md)).
5. **Outline one chapter** ([scene-outlines](plan/workflows/scene-outlines.md), its "outline" prompt) and write its reader-test key: what a blind reader must get, must not get and may only guess ([reader-tests, the key](plan/workflows/reader-tests.md#1-the-key)). For the first chapter, the story's shape, its ending and the chapter list as far as you know them are enough, filled in by hand from the interview's answers.
6. **Fill in [rulings.md](plan/workflows/drafting/rulings.md),** the rules the drafter must keep, and draft the chapter ([drafter.md](plan/workflows/drafting/drafter.md)).
7. **Check it:** the scripted checks ([mechanical.md](plan/workflows/drafting/mechanical.md)), the facts critic and the voice critic ([critics.md](plan/workflows/drafting/critics.md)), the quote check ([verify.md](plan/workflows/drafting/verify.md)), and a revision that fixes only the verified findings ([reviser.md](plan/workflows/drafting/reviser.md)).
8. **Run the [blind probe](plan/workflows/reader-tests.md#3-the-blind-probe):** a fresh reader's answers on that chapter, scored against its key.
9. **Close the session** ([retrospective.md](plan/workflows/retrospective.md)): what was learned written down and the plan's state brought up to date.

Everything else is a Refinement; each says when to add it. To run the daily work from a phone once this is done, see [kit/phone.md](kit/phone.md). A book made from the kit can later pull improved workflows from it: ask Claude to update the kit, and it shows you any place where the new version meets your own edits.

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
| [tools/](tools/README.md) | Small Python scripts that Claude runs: checks for broken links, the model's habit words and banned words, repeated phrases, words used before they are explained, and quotes; builders for cards, reading lists, the reader tests and an EPUB of your book for an ereader; and a few more, each listed in tools/README.md. |
| [kit/interview/](kit/interview/README.md) | The intake and interview script. |
| [kit/pipeline/](kit/pipeline/README.md) | The stages in order: when each runs and which workflows it uses. |
| [kit/phone.md](kit/phone.md) | Running the daily work from a phone, and an always-on host. |
| [kit/method/](kit/method/README.md) | The reasons: tasks and waves, the book's memory, oracles for prose, marks and the ledger, cards, horizons, key frames, agent limits, craft principles, closing cleanly. |
| [existing/](existing/README.md) | Where your manuscripts and notes go. Claude reads it and never changes it. |
| `example/` | A toy novel through every stage in miniature, with a worked run of the drafting chain and a reader-test spec. The only thing you delete to start a book; it stays readable in the kit's repository. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to give an improvement back: an issue, or a change sent through your own fork and reviewed there before it comes to the kit. |
| [CLAUDE.md](CLAUDE.md) | The instructions Claude reads in your book's folder. A template: the title now, the rest after the interview. |

## Three things to know

- **It is slow at the start on purpose.** The first weeks are interview, cards and outlines. That is where the book is decided.
- **Every number here was measured on another book** (reader scores, the bars a critic must pass on planted faults: how many it finds, and how many of its findings are real, card and file sizes, batch sizes). Before trusting one, run it on a chapter you know is good and one you know is weak, and set your own.
- **The rules are yours to change.** When a rule stops serving your book, change it in `plan/README.md` and say why.

## License

The docs are [CC BY 4.0](LICENSE): use and adapt them freely, with credit. The scripts in `tools/` are [MIT](tools/LICENSE). The license applies only to the files published in this repository. Anything you make with the kit is your own (your book, your notes, your cards and your plan/), and the license claims nothing over it. If you share the kit's files or an adaptation of them, give credit. For a book made with the kit, credit is asked, not required: *Made with World Saga Seed, by Karl Nelson.*
