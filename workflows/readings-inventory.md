# Readings inventory: settle the open readings in batches

*Refinement. Add this when readings pile up.*

## Purpose

List every open reading in the notes and outlines, so the writer can settle or cut them in batches. A reading is where Claude read the writer's shorthand or filled a gap the writer likely already has an answer to, so each is a place the page may differ from the story in the writer's head.

## When to run it

Whenever the readings have piled up (a grep for *(My reading* returns more than a screenful), and before any sweep that relies on the notes.

## Scope

Every mark that calls itself a reading: *(My reading, to confirm.)* and its variants, and first-person flags ("I read X as Y", "I assume"). In drafted chapters, match only the notes, since the prose may be first person. Proposals are inventions, not readings, and are a separate inventory.

## Steps

1. **Open a task** with the start hash.
2. **Extract mechanically:**
   ```bash
   grep -rn -i -E "my reading|I read .* as|I assume|reading, to confirm" world story/outline story/notes > $SCRATCH/readings.txt
   ```
   Split into groups of roughly equal size by subject.
3. **One agent per group,** at most two ([prompt](#prompt)), each writing one file to the task folder.
4. **Verify:** every quote resolves; every "possibly settled" item quotes its settling text and file.
5. **Assemble the index:** counts per group and topic; the possibly settled items first (quick wins); then the batches.
6. **Clear what the notes already answer:** a reading whose answer already carries a settled mark is deleted from the note; a reading that disagrees with a settled line is fixed on the reading's side. Agents for this are split **by note file**, so no two edit one file.
7. **Present the rest to the writer one batch at a time.** Confirmed: the mark becomes settled, with a ledger row. Corrected: the fact is rewritten in its one home, and dependents are grepped. Cut: removed.

## Item form

`### ID · title`, then `- **Where:** file:line`; `- **Quote:** "…"`; `- **Reads:**` what the note assumes, in one plain sentence; `- **Ask:**` the question, as yes or no or a pick between named options; `- **Rides on it:**` other passages that depend on it, quoted, or "nothing found"; `- **Status:**` open, possibly settled (with the settling text), or not a reading; `- **Topic:**` a short tag.

## Prompt

> You are inventorying the open readings in a novel's notes for the writer to settle, in the folder {REPO}. Read `plan/README.md` and `plan/workflows/readings-inventory.md`, then the extraction at {EXTRACT}. For each item, read its paragraph, and grep `world/` and `story/` for its key terms to find what depends on it and whether a later settled line already answers it. Write `{OUTPUT}` in the item form, one item per reading, grouped by topic, with a short header of topics and counts. Quotes verbatim. Run no git commands; do not launch agents; edit no other file. Phrase each Ask so the writer can answer in a word or a line; read back the shorthand rather than settling it.

## Lessons

- **Match the variants too.** Patterns that catch only the standard mark miss the first-person forms.
