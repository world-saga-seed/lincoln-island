# Dictation: key frames for a chapter that has none

*Refinement. Add this when a chapter is graded thin or none.*

The writer dictates the scene a chapter needs, and Claude cards it as key frames. Claude's work is the brief before the dictation and the carding after it; neither may invent a beat.

**When.** For every chapter graded **thin** or **none** for key frames, in story order, up to the horizon. In conversation, with the writer at the keyboard. No agents.

## The loop

1. **Gather what is already settled for the chapter** before writing the brief: its outline and notes, and every paper that settled something for it without landing it in the outline. `grep` the chapter number in `plan/settled/ledger/`, the actor logs and the task papers. A settled beat found there goes into the outline now, under its ID.
2. **The brief,** under 250 words:
   - where the chapter sits: time, place, ages;
   - the state at the start and at the end;
   - the reveals: what may be learned and what is held;
   - the writer's beats already in the outline;
   - what is only proposed, so the writer knows what is not theirs;
   - **three or four questions, each aimed at a character's goal in the scene and how far they push** ("what is she after?", "how far would she push him?"). A recommendation only where the canon supports one.
3. **The writer dictates.** Read it as key frames, in the writer's words. Where a line has two readings, take the one that fits the canon and mark it *(My reading, to confirm.)*.
4. **Answer the writer's questions from canon.** "Does that fit her?" is answered from her sheet and the settled lines, with each source named. When the writer asks how something would be done, give the plain, obvious way first.
5. **Card it, in order:**
   1. the ledger row, written as the ruling;
   2. the outline: the writer's lines as *(Settled R….)* bullets; Claude's fills as proposals; delete any reading the dictation supersedes; if the scene's order changes, renumber and fix inbound links;
   3. any rule the dictation states, at its home: a setting rule on its card, a drive on the sheet, a voice rule in the voice sheet; forward threads on the chapter that pays them off;
   4. the notes' drift line: what a redraft needs that the existing draft lacks;
   5. `python3 tools/links.py`;
   6. the task log: the chapter, its IDs, one line of what it settled, and the next chapter.
6. **Report in a few lines,** then **give the next brief in the same message,** so the loop keeps moving.

## Lessons

- **Dictations reach past the chapter.** Grep the thread before carding, and card each rule at its home.
- **The writer's asides are key frames too.** An aside about where a beat lands later is its own ledger row.
- **After a run of dictations, run a ripple scan** before drafting ([ripple](ripple.md)).
