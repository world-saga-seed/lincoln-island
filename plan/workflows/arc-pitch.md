# Arc pitch: key frames and tweens

*Refinement. Add this when an arc has enough frames to lay out.*

The writer supplies an arc's **key frames**; agents propose the frames still missing and pitch the **tweens**: the passage that places the frames on one timeline and sets the pacing. Run it when an arc has gathered enough frames to lay out.

**Grade.** A judgment. The writer's frames stay exactly as settled; every tween and proposed frame is marked *(Proposal.)*.

## The loop

1. **Open a task** naming the arc, its span, the frames settled and the frames missing.
2. **Two fresh agents:** **missing frames** (prompt A) and **the pitch** (prompt B), each writing only to the task folder.
3. **Verify:** quotes resolve; headings exist; nothing marked settled lacks a source.
4. **The interview** ([below](#the-interview)): the missing frames first, since the pitch's slots depend on them, then the gaps the pitch leaves.
5. **Fold back:** settled frames into the notes; the pitch revised around them and moved to the arc outline.

**Pace against the setting's clock.** Before placing frames, read the calendar, the ages, the travel the notes require, and who besides the main characters carries a thread offstage. A pitch that skips them crams a year into a season.

**The writer's list is not an order** (`kit/method/key-frames.md`).

## The interview

After the pitch, and after any dictation, Claude scans what is now on paper and puts the gaps to the writer. It is the step where the writer's judgment enters: each question asks why a person acts, not only what fills a slot.

**What it scans for,** in this order, since each answer can settle the ones after it:

1. **A missing key frame:** a slot in the pitch, or a chapter graded none. Asked open, with no recommendation: the frame is the writer's to give, and without it nothing below is asked.
2. **Motive:** a person who drives a beat with nothing they are after, or with no sense of how far they push.
3. **Cause:** a beat with nothing to start it. The plain, obvious means comes first.
4. **Knowledge:** a person acting on what they could not know: from whom, and when.
5. **The end state:** a scene that does not leave things where the next frame starts.
6. **A conflict:** the new text against a settled line, both quoted.
7. **What is held:** a fact the reader must not yet learn, at risk here.

The [actor-log critics](actor-log.md#the-three-critics) ask the same questions (logistics, the causal chain, the character invariant), so a horizon whose logs are current brings their open findings here too.

**Each question,** short enough to read on a phone:

- a number;
- one line of context, with the source named (the card, sheet, outline line or ruling);
- the question;
- **Recommended:** the answer and why, from canon, or "open" where canon holds nothing;
- the alternative, when there is a real one.

**Three or four at a time.** Questions canon can answer are not asked: Claude answers them, marks them *(Proposal.)*, and lists them in one line after the questions, so the writer can overturn any.

**The answers the writer can give:**

| The writer says | What happens |
|---|---|
| **as recommended** | every open recommendation is accepted, recorded as settled on the recommendation |
| **2 and 3 as recommended, 4: …** | mixed: the writer's words win where given |
| **override: …** (or just the answer) | the writer's line replaces the recommendation, recorded as the writer's |
| **discuss 4** | that question opens a back-and-forth; the rest wait |
| **leave it** | it stays a marked proposal, open for later |
| **next chapter** (or **next arc**) | what is settled is carded; anything unanswered stays a marked proposal; then the next brief |
| **stop** | carded, and the session closes by [the retrospective](retrospective.md) |

**The loop.** Card each round's answers before the next round (the ledger row first, then the outline, cards and sheets), then scan again: an answer often opens a new gap or closes several. Repeat until nothing is open, or the writer moves on. Claude ends each round by offering the next step ("next chapter?"); it never starts the next chapter's brief unasked.

**Wording slips.** A typed or dictated answer is read by the scene it points at. Claude asks again only when a misread word would change the ruling.

## Prompt A: missing frames

> You are proposing missing key frames for {ARC} of a novel, in the folder {REPO}. Read `README.md`, `plan/README.md`, the arc outline, the main characters' sheets, the voice sheet, and the cards the frames touch. Write only {FILE}; run no git commands; do not launch agents. The missing frames: {FRAMES}. For each: (1) what the notes already settle about it, quoted; (2) two or three options, each a short beat sequence, with what it sets up and pays off, what it costs, and which settled lines it leans on; (3) your recommendation and why; (4) open questions. Combine what the notes hold before inventing; where the notes are silent on something important, prefer a question. Hold to the book's rules: the narrator's reach; chance with a cause; the setup check. Outline only.

## Prompt B: the pitch

> Same files. (1) **The key frames,** each quoted with its source, and the missing ones as marked slots. (2) **The timeline:** frames in order, with what fixes the order and what is free. (3) **The tweens,** each a proposal: the ordinary days, short scenes and aftermath that let the frames land. (4) **Density:** scene by scene, quiet against set piece, so jokes do not stack and each set piece has room; name any stretch overfull or empty; say what each quiet stretch sets up. (5) **What should move,** with the reason. (6) **Conflicts** between settled lines, quoted. (7) **Open questions,** each with a recommendation. Outline only.

## Prompt C: the chapter list

> Once frames, tweens and the logic check are settled: one row per chapter in story order, numbered {NUMBERING}, with the date or season; the chapter's main beat; what the narrator sees and does; the aftermath it carries; quiet or set piece; what it plants; a working title. Mark each chapter settled or proposal. Count the chapters against the budget {BUDGET}; name what is overfull, thin or stacked. Say what the first chapter takes from before and what the last hands on.

**Lesson:** ask the writer the span's shared setting question (where everyone lives and works, season by season) before the agents run, because every agent hits it.
