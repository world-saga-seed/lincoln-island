# Consistency check: the outlined book against itself

*Refinement. Add this when an arc of several chapters is about to be outlined.*

The logic check runs on one arc before it is outlined. This runs on everything already outlined, by chapter range, before drafting: it catches what drifted as later work settled things the earlier outlines did not know.

**Grade.** A judgment. Agents find; the writer decides. Nothing here edits a note.

## Dimensions

The first three of the [logic check's](logic-check.md#dimensions): time (checked against `story/calendar/`); knowledge and causality (nobody uses what they do not have yet); the setting's rules (including the banned words in what the page shows). Then two of its own:

- **Continuity:** each chapter against those before it: names, objects, injuries, who is present, what was promised.
- **Settled against settled:** two settled lines that cannot both hold. The newer usually wins; say which is newer.

## The loop

1. **Split the outlined chapters into ranges** an agent can read whole, plus one agent for the spine: the arc outlines and the seams between ranges.
2. **At most two fresh agents at a time,** each owning one range across every dimension.
3. **Verify** every finding; merge duplicates across ranges; drop what is held or logged.
4. **Present to the writer** in batches, most severe first, each with context and a recommendation.
5. **Fold back;** log the run.

## Prompt

> You are checking a novel's outlines for consistency, in the folder {REPO}. Every file is read-only except your output file. Run no git commands; do not launch agents. Read `README.md` and `plan/README.md` (the marks). Your range: {RANGE}. Read every outline and notes file for those chapter numbers, and the arc outlines {ARCS}. Check them against each other, the calendar, and the cards they link, in five dimensions: time; knowledge and causality; the setting's rules; continuity; settled against settled. Write only {OUTPUT}. For each finding: a title; severity (**breaks**, **strains**, **nit**); both sides quoted with file, line and mark, and which is newer (by the file dates in {DATES}, or the dates in the marks); why, in two or three sentences; two or three fixes, the plain one first, with your recommendation. Skip what is held, open, superseded or logged as drift, and anything that is only wording. Do not invent lore. At most twenty findings. Verify every quote with `grep -F`.

**`{DATES}`** is supplied by the supervisor, who runs the git command itself (agents run no git): each file's last commit date, from `git log -1 --format=%cs -- <file>`.
