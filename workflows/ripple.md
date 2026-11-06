# Ripple: carry a settled change through the notes

*Refinement. Add this when a settled change contradicts earlier notes.*

When the writer settles a change that earlier notes assumed the opposite of (a homecoming moved, an ending changed, a scene relocated), agents find every line downstream that still assumes the old version and shift it.

**Grade.** A judgment with a mechanical core. Where a line simply contradicts the change, the agent revises it in place, marked. Where matching it needs a new decision, the agent writes a held question instead. The diff is the check.

## The loop

1. **Open a task** naming the change (quoted, with its ledger ID), the start hash, and the file groups.
2. **Split by file,** one agent per group, at most two at once, no file in two groups, the largest file alone. Agents never rename headings. Skip `plan/archive/` and `plan/settled/` (history) and drafted prose (log drift instead). Stay inside the horizon; a ripple past it goes on a list for the writer.
3. **Agents** ([prompt](#prompt)), each editing only its own files.
4. **Check:** links resolve; every revision marked; the diff stat for files that changed more than expected; grep for leftovers of the old version.
5. **Present:** the diff summary, then the held questions a few at a time, each with a recommendation.
6. **Fold the answers;** log drift in `plan/state.md`.

## Prompt

> A settled change in a novel's notes, in the folder {REPO}: {CHANGE}, recorded as {ID}. Read `README.md`, `plan/README.md`, the ledger row and your files: {FILES}. Edit only those; write your report to {REPORT}. Run no git commands; do not launch agents. Never revert or reformat anything you did not change; edit by small exact replacements. Cite a ruling by its ledger ID and a fact by its card, never a task paper. Find every line in your files that still assumes the old version, directly or by consequence, and sort each: (a) **contradicts** the change: revise it in place, deleting the old text rather than striking it, and marking new text by what it is; (b) **needs a decision** the change does not make: leave it, and write a held question with context, the plain option first and a recommendation; (c) **drift** in files you may not edit: list it. Never invent lore; never present an invention as settled. Verify every link you write. Report: revisions by file, held questions, drift.

## Lessons

- **Dedupe across groups** before presenting: agents on different files reach the same question from different ends.
- **Hold the writer's new points until the file's agent finishes,** or one side's edit is lost.
