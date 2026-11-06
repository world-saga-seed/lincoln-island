# Restructure: move the notes without losing a fact

*Refinement. Add this when a topic file passes about 5,000 words with two subjects.*

## Purpose

Move notes into a better structure (split a file that holds two kinds of text, move files to new homes, merge topic files) so that nothing is reworded by accident, every block lands exactly once, and every link still points at the right place.

**Grade.** Mechanical where it can be: the moves are scripts, verbatim, and coverage is checked by script. Judgment only in the design and the clean-up, and both are logged.

## When to run it

When the folders no longer fit how the work reads them: a topic file past about 5,000 words with two subjects, a folder that mixes kinds, a card audit's settled splits.

## Steps

1. **Inventory:** the files and sections in scope, their sizes, and the links into each heading (`grep -rn "file.md#" --include=*.md .`).
2. **Design** (one agent): the target tree, each new file's outline, and a **map**: one line per block (a heading's section, or a paragraph) saying where it goes. Loop until every block is placed exactly once.
3. **Dry run** on a copy in the scratchpad: build the new tree from the map verbatim; check **coverage** (every non-blank source line is in exactly one output); check links in the copy against the real folder's baseline.
4. **Move** for real: `git mv` for every whole-file move, so history follows; build splits from the map; repoint every link to a moved heading.
5. **Clean** (agents by target group, at most two): delete struck and superseded text, merge restatements into their home, smooth the seams. Headings are frozen. Every change in a log.
6. **Review:** coverage again; a stronger agent reads each clean diff for changed facts. Fix or restore.
7. **Check:** `tools/links.py` at 0; update `README.md`'s index.

## Lessons and failure modes

- **Bulk moves go to a small, cheap model,** checked by script and reviewed by a stronger one. The work is verbatim and high-volume; the risk is a silent reword or a dropped block.
- **Dated records keep their old paths.** Task logs, ledger rows and settled decisions are history: do not rewrite the paths inside them.
- **Write quoted links inside a report as code,** or they count as broken links.
- **Never move and reword in one step.** Move verbatim first; clean after, with its own diff.
