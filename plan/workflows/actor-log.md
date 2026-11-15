# Actor logs: the timelines behind the narrator's view

*Refinement. Add this when an offstage actor drives a beat.*

The outline is the narrator's view, so anyone else's work shows only where it crosses theirs. Between crossings nothing tracks them: a character can be in two places, know what they could not, act on no motive, or sit idle while the plot needs them. An actor log is the writer-side record of one actor's doing, knowing and wanting across a horizon, checked against the outline.

**Who gets one.** Anyone whose offstage work crosses the narrator's view and drives a beat. A group (a family, a firm, a faction) gets one by the same test. The writer chooses the list per horizon.

## When it runs

The check runs on outlines, so it runs **every time a horizon's outlines change in bulk, before anything is drafted from them**: after a restructure, an [outline clean](outline-clean.md) or a consistency batch that moves beats, and at each new horizon. The drafting gate waits on it.

- **Rerun, not patched.** A log is rebuilt by the loop below from the current outlines, not mended row by row; spot fixes between runs do not count as a run.
- **Each log's head records its last run:** `Last run: <commit> <date>`. The log is stale once any outline in its horizon changes after that commit.
- **The extraction reads the current outlines, notes, cards and ledger only, never a retired draft,** so a superseded beat cannot come back through the log.
- **Then the cross-log check.** Once every log of the horizon is rebuilt, two agents read the logs against each other **at the scenes where two actors meet** (from each log's Where and Trace columns), not every pair in full, for conflicts of time, place, knowledge, event and want.

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
4. **Audit** for the faults: **idle spans** (long stretches with nothing to do while the plot needs them); **overload** (too many threads at once); **knowledge leaks** (they act on what has not reached them); **two places at once**; **no motive** (an act no Wants row explains); **no trace** (a long run the narrator could have glimpsed and did not).
5. **Fill the gaps** with proposed rows, and rank every fault and fix by page impact:
   - (a) a fault whose fix changes an outline line, or who knows what, when, or who is present;
   - (b) a stale line that a newer ruling already overrules;
   - (c) a tween that changes no line.

   Only (a) goes to the writer. Strike (b) at once by the newer ruling. Write (c) into the log as a reading, listed in the task but not asked, since a drafter never sees it.
6. **Check acceptance:** every beat the actor drives on the page traces to a row; no fault left open without the writer's ruling.

**The log is never on the page.** The narrator sees only its traces. A reader is never put inside a character the narrator only watches.
