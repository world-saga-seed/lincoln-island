# Actor logs: the timelines behind the narrator's view

*The three critics' [light pass](#the-light-pass-basic) is Basic. The full log is a Refinement: add it when an offstage actor drives a beat.*

The outline is the narrator's view, so anyone else's work shows only where it crosses theirs. Between crossings nothing tracks them: a character can be in two places, know what they could not, act on no motive, or sit idle while the plot needs them. An actor log is the writer-side record of one actor's doing, knowing and wanting across a horizon, checked against the outline.

**Who gets one.** Anyone whose offstage work crosses the narrator's view and drives a beat. A group (a family, a firm, a faction) gets one by the same test. The writer chooses the list per horizon.

## When it runs

The check runs on outlines, so it runs **every time a horizon's outlines change in bulk, before anything is drafted from them**: after a restructure, an [outline clean](outline-clean.md) or a consistency batch that moves beats, and at each new horizon. The drafting gate waits on it.

- **Rerun, not patched.** A log is rebuilt by the loop below from the current outlines, not mended row by row; spot fixes between runs do not count as a run.
- **Each log's head records its last run:** `Last run: <commit> <date>`. The log is stale once any outline in its horizon changes after that commit.
- **The extraction reads the current outlines, notes, cards and ledger only, never a retired draft,** so a superseded beat cannot come back through the log.
- **Then the cross-log check.** Once every log of the horizon is rebuilt, two agents read the logs against each other **at the scenes where two actors meet** (from each log's Where and Trace columns), not every pair in full, for conflicts of time, place, knowledge, event and want.

## The three critics

The audit asks three questions of every row and every beat the actor drives, one critic each:

- **Logistics and physics.** Can they get there in the time (*presence*, *timing*: travel, work hours, the calendar)? Do they have the supplies, tools, money and hands the act needs (*means*)? How long does the act itself take, and does the calendar hold it (*duration*)? Are they idle where they would act, or carrying more threads than one person could (*load*)?
- **Causal chain.** What started them on the path that leads here (*trigger*)? Do they know what the act needs, from an earlier row that says when and from whom (*knowledge*; for a group, through a channel its Knows column names)? Do they know how to do it, by training or trade (*know-how*)? Does a want drive the beat (*motive*)?
- **Character invariant.** Is the act consistent with the person's [sheet](character-sheet.md): their center, goals and habits? The critic names the sheet line the act breaks or stretches. **It flags, it does not block:** an act out of character can be deliberate (a mask, a breaking point), so the writer rules, and a stretch ruled deliberate goes on the sheet so it is not raised again. It runs only on people with a sheet.

**The interview is forced.** Every finding of rank (a) (step 5) is written to the task's `interview.md`: both sides quoted, the plain fix first, and a recommendation. The [drafting gate](drafting/README.md#the-gate) refuses "draft" while any item there is open. **The interview is where the human creativity comes in.** A finding is not just a fault to patch: each item asks the writer why the person did it, what moved them, and how they thought it through. The recommendation is there to accept or overrule, never a substitute for that answer, and the answer goes into the log's Wants and Knows rows and the sheet, so the drafter writes from it.

## The light pass (Basic)

Without full logs, one critic pass per chapter outline asks the three questions of each offstage move the chapter's beats rest on: who must have gone somewhere, carried something, learned something or decided something off the page for this beat to happen. Its findings that change an outline line go into `interview.md` as the full audit's do. When offstage actors drive many beats, move up to the full log.

## The log

`story/calendar/<actor>/<arc>.md`, a table in date order, one row per event or span:

| Column | Holds |
|---|---|
| **When** | the date or span, and the chapter the narrator's thread is in |
| **Where / doing** | where they are and what they do |
| **Knows** | what they know that bears on the plot, and from whom (new knowledge in bold). For a group, the channel: their own eyes, an agent, a witness |
| **Wants** | what they are after, and what they fear |
| **Trace** | what the narrator could see of it, or "none" |
| **Source** | the outline, note, draft or ruling it rests on, quoted |

A row with no source is a tween, marked *(Proposal.)*.

## The loop

1. **Extract** (one agent per actor, read-only): every line in the horizon's outlines, notes, drafts and cards that says or implies where they are, what they do, know or want, with its quote and date.
2. **Check** every quote; drop what does not resolve.
3. **Build** the log in date order.
4. **Audit** with [the three critics](#the-three-critics), and for **no trace** (a long run the narrator could have glimpsed and did not).
5. **Fill the gaps** with proposed rows, and rank every fault and fix by page impact:
   - (a) a fault whose fix changes an outline line, or who knows what, when, or who is present;
   - (b) a stale line that a newer ruling already overrules;
   - (c) a tween that changes no line.

   Only (a) goes to the writer, through `interview.md`, with the character critic's flags. Strike (b) at once by the newer ruling. Write (c) into the log as a reading, listed in the task but not asked, since a drafter never sees it.
6. **Check acceptance:** every beat the actor drives on the page traces to a row; nothing left open in `interview.md` without the writer's ruling.

**The log is never on the page.** The narrator sees only its traces. A reader is never put inside a character the narrator only watches.
