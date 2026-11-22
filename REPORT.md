# Lincoln Island: the report

*Phase 13 of [BRIEF.md](BRIEF.md). A draft for the author: every figure is from the files named beside it. (Proposal.)*

## What was made

Two books, from plain files in this repository:

- **The novel.** Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) in Stephen W. White's English of 1876, made unabridged against the French. Then it was "vandalized": an Iowa scholar's footnotes on where the story disagrees with itself, and one chapter Verne never wrote, XIX bis, "The Float in the Bar", set on 1 to 3 June 1865.
- **The run's book.** XIX, XIX bis and XX at every stage:
  - White;
  - two prompt-only controls;
  - version 1;
  - the stages after the human's read-aloud and after the character check;
  - the final.

  Then the cards, the ledger, the blind scores and the read-aloud.

Language models did the work. One model played the author, and its session directed this one, which drafted, checked and built with fresh agents. A human read the builds as a reader and gave the parts the foreword names: the read-aloud of XIX bis, two later turns of its plot, the fact its glass float turns on, the idea of the additions, and the scholar's conception and the title note on XIX bis.

## The method, as run

The [World Saga Seed](kit/pipeline/README.md) kit keeps the story's facts as notes ("cards") and checks every chapter against them. Every ruling goes on a ledger before any file changes ([plan/settled/ledger/](plan/settled/ledger/)). The phases, in BRIEF's order:

1. The sources.
2. A scene outline of every chapter from the French.
3. White aligned to the French, with every departure listed.
4. The cards.
5. A calibration render.
6. The insert's brainstorm.
7. The controls.
8. Version 1.
9. The ereader read.
10. The read-aloud of XIX bis.
11. The refine.
12. The book.
12b. The clearance.

The widened horizon (R1121-148, the human's own word) added a second piece of work. All 62 of Verne's chapters were made unabridged: 38 by patches to White's text (3,224 patches) and 24 rendered anew from the French in White's English.

## The measures

### The voice against the old translation, at the seams

These are `tools/tells.py` measures. White's own range across these chapters is: "and" per sentence 0.47 to 0.70, median sentence 18 words, short sentences 6 to 18%, long 27 to 30%, spread (sd) 11.4 to 13.0.

| Final | and/s | median | short% | long% | sd | banned words |
|---|---|---|---|---|---|---|
| XIX (Verne's, rendered) | 0.49 | 18 | 8 | 29 | 11.2 | 0 |
| XIX bis (the insert) | 0.70 | 16 | 14 | 26 | 10.4 | 0 |
| XX (Verne's, rendered) | 0.42 | 19 | 16 | 31 | 10.6 | 0 |

The seams critic ran on v1 and on the final. Its one finding on the final was a matter of taste, and it was settled (R1121-132).

### Version 1 against the two prompt-only controls

The controls had the same chapters and the same scene, with no cards, no ledger and no checks. Fresh critics checked them blind. The figures are from [the controls' batch paper](plan/tasks/task-20261121-09-controls/checks/batch-paper.md) and [v1's findings](plan/archive/task-20261121-11-render-v1/findings-v1.md).

- **Verne's chapters, XIX and XX.**
  - **The controls:** both rendered close to the French. Gemini had 3 fact findings, Opus 3 standing, with 0 to 1 omissions. Their faults were of voice: long sentences above White's (41 to 43% against 27 to 30), house spelling (13 and 6 forms), and names from other translations.
  - **Version 1:** one fact finding ("an acid drink" for "une boisson acidulée"). Its voice findings were seven spellings, one name, and XIX's long sentences.
- **The insert, XIX bis.**
  - **The controls:** canon breaks against Verne and their own neighbouring chapters, Gemini 7 and Opus 2. Voice breaks, Gemini 5 and Opus 4, on the same four rules: the narrator settles the float's origin, looks ahead, names the silence, and names its cause. In the blind probe, Gemini leaked two of the hidden questions and got one wrong; Opus held them all but lost the chapter's point to half.
  - **Version 1:** 4 fact findings, against the notes. In the probe it leaked none of the hidden questions, but, like Opus, it lost the point to half. The probe on the final read 15 of 15 as meant, with no leaks (`plan/tasks/task-20261121-14-refine-2/probe/score.md`).

### The final on top of v1: the blind scores

The human put each version to Gemini cold, with one judge per text and the rubrics frozen at phase 7. These are one reader's view, not a measurement ([the scores](plan/tasks/task-20261121-16-the-book/blind-scores.md)).

| XIX bis | Gemini control | v1 | after read-aloud | after character check | final |
|---|---|---|---|---|---|
| Fidelity to spec | 9 | 8 | 6 | 7.5 | 7 |
| Restraint | 7 | 9 | 4 | 7 | 7 |
| Period voice | 8.5 | 8 | 8 | 8.5 | 8 |
| Character | 8 | 8 | 6 | 7.5 | 8 |
| Prose | 8 | 7 | 7 | 7.5 | 7.5 |
| Modern-model habits | 6.5 | 8 | 5 | 6.5 | 6.5 |

The read-aloud added beats the frozen one-paragraph scene does not hold, so fidelity counts them against the chapter. The character check won most of the read's cost back. On the translations, every version scored 10 for completeness, with accuracy from 8.5 to 9.5.

**No human blind-reader ranking was run.**

### The clearance

These figures come from `tools/overlap.py`, counting runs of 8 or more words ([the report](plan/tasks/task-20261121-17-clearance.md)):

- The 24 rendered chapters share 28.9% of their words with Kingston's 1875 translation. White's own text over the same chapters shares 6.1%. The prompt-only controls share 16 to 26%. The models remember Kingston. It is in the public domain, and the foreword says so.
- XIX bis shares one 8-word run with Kingston and none with White.
- The famous-phrase check found nothing.
- **No modern translation was checked.**

## The cost

The token log is [plan/records/tokens.md](plan/records/tokens.md). It counts every model call; most of the tokens are cached context read again.

| Work | Tokens |
|---|---|
| Phase 0 (the author's sessions; upper bounds) | 27.9M |
| Phases 3 to 5 (main session) | 165.7M |
| Phases 7 to 11 (main session and 35 agents) | 169.9M |
| White made unabridged, the end pass (main session and its agents) | 415.2M |
| Phases 12 and 12b (main session and 6 agents) | 58.6M |
| Agents logged by row (phases 1 to 5) | 14.4M |

Carding was done once, for the whole book. The insert's three chapters, from the controls to the final (phases 7 to 11), cost about as much as the outlining, alignment and calibration together (phases 3 to 5). Making the whole of White unabridged cost about two and a half times either.

## What worked

- **The ledger first.** 181 rulings on the second day, each one sentence, each written before the edit. A later reader can see why every line is as it is.
- **Fresh critics, quoting the text.** Every finding had to quote words that resolve by search. Two fresh critics on the scholar's notes and the forewords caught false claims the drafters were sure of: 15 of 37 notes needed fixing, and the foreword had several claims wrong, among them who had made which change.
- **The controls.** They showed where the method pays. It made little difference on Verne's chapters, where the French holds a model to the facts. On the invented chapter it made a large one: the controls broke canon and told what the chapter is built to withhold.
- **Patches, not redrafts.** In the refine and in the unabridged work, each change was a row with its old and new text. That made every change reviewable, and the map is drawn from those rows.

## What failed, and how it was fixed

- **The departure lists undercounted.** The phase 3 alignment listed 7 departures in I.5; the patcher and its critic found at least 31. From the pilot on, patchers read for departures and did not just patch the list.
- **The read-aloud cost restraint.** The read's beats dropped the insert's restraint score from 9 to 4. A character check, which asked whether these men would do each beat, brought it back to 7.
- **Over-correction in the joins.** Joining XIX bis's short sentences pushed "and" per sentence to 0.81 and semicolons to 36; nine splits brought it back to White's range.
- **Build bugs:** a heading taken from White's end line; a quote pass that opened quotes after dashes. Both were caught by reading the output.
- **The executor reported a commit hash before git showed it,** once. It sent a correction. The rule since is to report a hash only after `git log` shows it.

## Limits

- One judge, one run per text, for the scores.
- No human blind readers.
- No modern translation checked.
- The French was checked against the scan only in spots.
- The rendered chapters' English leans on Kingston.
- The scholar's notes are the papers against themselves, settled by one critic's check.

## Still to do

- The community check.
- The post, which the author decides on.
- The author's removal of the raw sources from the history before the repository is made public (R1121-180).
