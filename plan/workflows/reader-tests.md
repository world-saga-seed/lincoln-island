# Reader tests: unit tests for a novel, by chapter

*Basic.*

## Purpose

Software has unit tests: for each piece, a statement of what it must do, and a run that checks it. A novel can have the same. For each chapter, write down what a blind reader **must get**, what they **must not get**, and what they **may only guess**. Then give the prose, and only the prose, to fresh readers and score their answers against that spec.

This is the one test of prose with a real answer key. The critics judge; the reader tests measure. The notes say what the right answer is, so a reader's answer is either what the book meant or it is not.

Four instruments, one spec. Of the prompts in [reader-tests/](reader-tests/), three are Basic: [key-builder](reader-tests/key-builder.md), [probe-open](reader-tests/probe-open.md) and [probe-asked](reader-tests/probe-asked.md). The rest are Refinements.

| Instrument | Asks | Catches |
|---|---|---|
| **The key** with **the blind probe** | How does this world work? What is it? | leaks (a hidden thing stated as sure) and misses (a plain thing never worked out) |
| **The story questions** | What is the story holding back, and has it turned yet? | secrets known too early, twists that do not land, misdirections nobody believed |
| **The reread test** | Knowing the truth, how do these scenes read now? | missing plants, contradictions, plants too obvious |
| **The closed-book quiz** | What does a reader remember of this chapter? | misreads, hooks too readable, plants too faint |

## When to run it

- **Write the spec while outlining.** A horizon is not accepted for drafting until the key (and the story questions, if used) cover its chapters ([the gate](drafting/README.md#the-gate)). The spec is written from the notes, before any prose, the way a test is written before the code.
- **Run the probe** (Basic) on any stretch once it is drafted and refined, before the writer's read. The quiz comes in with the [interest check](interest-check.md), as a Refinement.
- **Run the reread test** on later chapters, where a payoff is drafted, and after any redraft of a chapter that holds a plant.
- **Rerun the quiz** on the same questions after a trim or revision, to see that nothing that landed was lost.

## Inputs

- The prose of the stretch, and only the prose, in reading order (the main narrator's thread; a second run with any secondary layer in place, if the book has one).
- The notes, for building the key (never given to a reader).
- The clue register, `plan/reread-hooks.md`.

## 1. The key

Built once from the notes by an agent that may read everything ([prompt](reader-tests/key-builder.md)), kept at `plan/reader-tests/key.md`, and brought up to date whenever the notes change. The writer reads it before it is used. Each entry is one question a reader could ask about how the world works or what it is, in one of four kinds:

| Kind | The text alone should return | Scored as a fault when |
|---|---|---|
| **Plain** | what it is, though the page never names it | it comes back blank: **missing** (shown too thinly) |
| **Hidden** | the world's own explanation, or nothing; never the truth | it comes back **sure** as the truth: **leak** |
| **Unknown** | unknown; the book never resolves it | any firm answer: **leak** |
| **Forbidden** | the question does not arise | it is raised at all, or raised unprompted in the open run: **leak** |

Each entry's fields are in the [template](../templates/reader-key.md).

## 2. The story questions

*Refinement. Add this when the book holds a secret across chapters.*

The key asks how the world works. The story questions ask what the **story** holds back. Kept at `plan/reader-tests/questions.md` ([template](../templates/reader-questions.md)). Each question has an expected answer **by chapter range**, so one list scores any stretch of the book:

| Kind | Before it turns | From the chapter it turns |
|---|---|---|
| **Secret** | unknown, or guessed | sure |
| **Misdirection** | wrong: the reader believes the false thing | sure of the truth |
| **Irony** | (none) | sure, though the narrator misses it |
| **Trope** | no, or unknown, throughout | no, or unknown |

**Scoring:**

- **Leak:** sure before the range says sure.
- **Miss:** anything short of sure after the turn.
- **Weak setup:** a misdirection not believed.
- **Trope:** the reader concluded the stock outcome the book is built to avoid.

The chapter at the edge of each range is where to look for the cause.

## 3. The blind probe

A fresh agent, with no notes, reads only the prose of the stretch, in two runs.

1. **The open run** ([prompt](reader-tests/probe-open.md)): unprompted. "Name every device, power, process, institution and being the story relies on; say how each works and what it really is, as far as the text lets you; then say what world this is, when, and anything about the narrator the text implies but does not say." **The open run counts most,** because nothing in it prompted the answer.
2. **The asked run** ([prompt](reader-tests/probe-asked.md)): the same reader (continue that agent by message, not a new launch), then given the key's questions and the story questions whose ranges cover this stretch, **shuffled among as many decoys** (questions the book has no stake in), so the list itself gives nothing away.

Every answer quotes the passages it rests on, and is marked **sure**, **guessed** or **unknown**.

**A guess is not a leak.** A *guessed* answer is the suspicion the genre allows a sharp reader. It is logged, and watched across runs, but only a **sure** answer to a hidden question is scored as a leak.

**Scoring,** per question, against the key: **as meant**, **leak**, **missing**, or **wrong**. A wrong answer quotes the passage that misled; that passage goes to the writer.

## 4. The reread test

*Refinement. Add this when a payoff is drafted.*

The probe checks the first read. The reread test checks the second: a reader **told the truth** reads the same scenes again ([prompt](reader-tests/informed-reader.md)).

A fresh agent is given one truth, from the key or the story questions (a Hidden or Secret answer, quoted from its source), then the prose up to and including the scenes that should hold its plants. It answers: knowing this, how do you read these scenes? Which lines change meaning? Which lines were planted for it? Does anything now contradict it?

**Scoring, per scene and truth:**

| Result | Means |
|---|---|
| **Pays off** | lines turn, and the turn is fair (the blind probe did not get it sure before its range) |
| **Flat** | knowing the truth changes nothing: the scene carries no plant |
| **Contradicts** | a line no longer fits the truth: a discontinuity |
| **Too obvious** | the informed reading is so plain the blind probe should have got it; check it against the probe's result |

**Walking the line.** Run the reread test with the blind probe on the same range. A truth that is **unknown or guessed** blind and **pays off** informed is on the line: working. **Sure** blind is a leak. **Flat** informed is a missed plant.

## 5. The closed-book quiz

*Refinement. Add this after a trim or revision.*

Per chapter, run with the interest check's readers ([prompt to write it](reader-tests/quiz-writer.md); [prompt to grade it](reader-tests/quiz-grader.md)). One agent writes the quiz from the prose, the clue register and the chapters' plants, kept at `plan/reader-tests/quiz-<stretch>.md` with its key:

- **Should know:** two or three questions per chapter on what the page must land, each keyed to the line that lands it.
- **Guess:** where a hook is planted, one question keyed to the true answer, with what counts as too plain, on target, off, or too faint.

Each reader answers from memory in its own session, after reading, marking sure or guess. A grader marks both.

| Result | Means |
|---|---|
| **Confident wrong** on a should-know | a **misread**: the page says it unclearly or misleads |
| **Confident right** on a guess | the hook is **too readable** |
| **Blank** on a guess | the plant is **too faint** |

## How failures route back

| Failure | Goes to | As |
|---|---|---|
| **Leak** (a hidden, unknown or forbidden answer sure; a secret sure too early) | the **mechanism critic** and the **voice critic**, with the passage the reader quoted | the line that gives it away; the fix is usually order, distance or restraint, not removal |
| **Missing** (a plain answer blank; a secret not sure after its turn) | the **drafter**, through the chapter's Next pass list | shown too thinly; the beat needs one more visible step |
| **Weak setup** (a misdirection not believed) | the **outline**, then the drafter | the false trail needs a cause the reader can see |
| **Trope** concluded | the **writer** | a structural note |
| **Flat** in the reread | the **outline** and the clue register | a missing plant |
| **Contradicts** in the reread | the **facts critic** and the writer | a discontinuity |
| **Misread** in the quiz | the **reviser** | the line that misleads |
| **Too readable / too faint** | the **writer**, with both the blind and informed results | where the hook sits on the line |

**No fix may cut a clue.** A leak is fixed by moving, delaying or quieting what gives the truth away, never by removing a line a reader needs to solve it later. A plant flagged as too obvious is quieted, not deleted. Every fix is checked against the clue register before it lands.

## Checks

- Every reader quote resolves in the prose (`tools/quotes.py`).
- Every key entry's **True** quote resolves in the notes.
- The decoys outnumber or equal the real questions in the asked run.
- The open run is scored before the asked run is read.

## Outputs

- `plan/reader-tests/key.md`, `questions.md`, `quiz-<stretch>.md` (the spec; living files).
- Per run, in the task folder: the probe's two runs, the informed readers' reports, the quiz answers and grades, and the **scored table**: one row per question, with the expected answer for this stretch, each run's answer and mark, the score, and where the fault routes.

## Lessons and failure modes

- **Write the spec before the prose,** from the notes. A key written after reading the draft drifts toward what the draft does.
- **The open run is the real test.** The asked run tells you what a reader *can* get when prompted; the open run tells you what the page *gives*. A leak only in the asked run is weaker than one in the open run.
- **Decoys are not optional.** Without them, the questions themselves tell the reader what matters, and every hidden truth leaks.
- **Score by sure, not by guessed.** Readers of a genre suspect. A book that leaves no room to suspect is no puzzle; a book whose secrets come back sure is no secret. Guesses are logged and watched, not scored.
- **Expect old drift to show up as fact.** A detail left in an early draft that the notes have since changed comes back from the reader as a confident answer. That is a drift row, not a leak.
- **A reader's wrong answer is often the most useful result.** Quote the passage that misled; it is usually a sentence that does two jobs.
