# Apply terms: carry a settled name through the notes

*Refinement. Add this when a placeholder name is settled.*

## Purpose

When the writer settles a name or term that replaces a placeholder (a town called "Town A", a renamed office, a retired word), agents apply it across the notes.

**Grade.** Mechanical in intent but not in practice: a placeholder like "A" is also an article, so every hit is read in context. The diff is the check.

## When to run it

When a placeholder is settled, or a term is renamed or retired.

## Steps

1. **Open a task** naming the term, its replacement and the start hash. Record the term in the setting's list of terms first (a `world/terms.md` with one meaning per term), so that list is the authority.
2. **Rename headings centrally,** before any agent runs: change each heading that carries the old term, work out its new anchor, and update every link to it in one script. Agents never rename headings, so no two fight over an anchor.
3. **Split by file and skip** as [ripple](ripple.md#the-loop) does (step 2) ([prompt](#prompt)).
4. **Also skip** task papers an agent is still reading; change drafted prose only if the writer wants it.
5. **Check:** grep for leftover hits of the old term and read each; `tools/links.py` at 0; the diff stat for files that changed more than expected.
6. **Show the writer** the diff summary and the leftovers.

## Prompt

> Apply the settled names in {FILES} only; edit nothing else. Names: {NAMES}. Run no git commands; do not launch agents. Read every hit in context: change a placeholder only where it means the thing renamed, never an article, a list label, an option letter or a quoted line of drafted prose. Keep each sentence's meaning, marks and links; change link text, never link targets (the headings are already done). Where a mechanical swap reads badly, rephrase minimally. Do not revert other unsaved edits. Report per file: the number of changes, and every hit you left alone that a reviewer might question, with line and reason.

## Lessons

- **Placeholders collide with ordinary words.** Read every hit; never run a blind replace.
- **A term means one thing.** If the new name already means something else in the notes, stop and put it to the writer.
