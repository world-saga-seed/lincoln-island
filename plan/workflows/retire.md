# Retire: archive and tombstones

*Refinement. Add this when closed tasks pile up.*

How finished work leaves the working set, so a closed task or an accepted chapter's papers stop being pulled back in.

## What gets retired

- **A finished task** moves from `plan/tasks/` to `plan/archive/` under its own name. Every link to it is repointed in the same commit.
- **A task that is only noise** (a run log, a scan, a superseded proposal) is tombstoned.
- **An accepted chapter's working papers** (critic runs, batch papers) are tombstoned once the writer accepts the chapter.
- **A procedure that grew inside a task** becomes a workflow, so later tasks cite the workflow, not the task.

## The procedure

1. **Promote first.** Every live fact goes to its card, every decision to the ledger or `plan/settled/`, every working rule to its workflow. A file whose outcome cannot be said in a few lines is not ready to retire: the knowledge is still only there.
2. **Repoint citations.** A card that cites the task for a fact now cites the card or ledger row the fact went to. Canon never cites a task paper; only the ledger's "Asked in" column and task logs may.
3. **Write the tombstone** in place of the file, at the same path: its title; a line `*Tombstone, <date>: the full text is at <sha>, git show <sha>:<path>.*`; a short summary of what it settled and where each result now lives; and every heading another file links to, each with a line saying where that went, so links still land.
4. **A paper nothing links to is removed**, not tombstoned; the task's own tombstone lists it with the sha. To find links into a task: `grep -rn "task-<id>" --include=*.md .`
5. **Check:** `python3 tools/links.py` at 0.
6. **Log** the files and the sha in the commit message or the task log.

## Rules

- The sha is the last commit holding the full text.
- A tombstone is never edited back into a working file. If its subject reopens, a new task cites it.
- Nothing is tombstoned while a live task, open question or unaccepted chapter still works from it.
