# The reviser, and the re-check

*Basic.*

The reviser makes the fixes. It works from a snapshot, on the verified findings only, and changes wording, never the story. The prompt template is [prompts/reviser.md](prompts/reviser.md).

## Before it runs

1. **Snapshot** the batch's chapters to the scratchpad (`snap/`). The re-check and any restore work from the snapshot.
2. Apply the **Fix now** items yourself, and log them.
3. Write the reviser's list: every **Fix** finding with its direction, and any "to the reviser" items from the batch paper.
4. Write the **keep list:** every clue line in the chapters (from the register and the clue notes), every line the writer has asked to keep, and every fix already made by an earlier critic that the reviser must not undo.

## What it gets, and its rules

What it reads, its rules (wording only, every finding addressed, the keep list and every clue kept, the texture held) and its report are in [the prompt](prompts/reviser.md). It does **not** get the critics' raw reports (only the verified list), the outlines (only the settled lines if a finding needs one), or the conversation.

## Re-check

The re-check is the mechanical half of trusting a revision. In order:

1. **Diff** each chapter against its snapshot. Read the diff. A change that is not tied to a finding is a stray edit: restore it, or put it to the writer.
2. **The keep list is still on the page.** Write it as `- quote:` lines and run `python3 tools/quotes.py keep.md --in <the revised chapters>`. Every keep line must resolve. A miss is restored from the snapshot.
3. **The mechanical checks again:** `tells.py` with the banned list, the rule greps, `links.py`.
4. **Check the fix, not only the finding.** For each finding, read the new text: is the fault gone, or only the quoted words? A finding "resolved" by deleting its line, where the fault was the scene's, is not resolved.
5. **A facts check over the changed passages only,** against the snapshot. A reviser who rewords can still slip a fact. One small critic run, given the diff and the cards it touches.
6. **The invention check** on the reviser's Inventions list, as its own small run.

Then the chapter's stage in `plan/state.md` moves to **refined**.

## When to run a second reviser

Only when the re-check finds more than a handful of problems. A third pass on the same batch is a sign the outline or the rulings are wrong, not the prose. Stop and look there.
