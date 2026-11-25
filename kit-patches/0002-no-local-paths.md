# Kit patch: no local paths in the files, and tools/check_paths.py

*Generic; no book content. Apply by copying `tools/check_paths.py` into the kit's `tools/`, adding rule 17 below to the kit's `CLAUDE.md`, the lines below to `tools/README.md`, and the step to `plan/workflows/publication.md` (R1124-04).*

## Why

Lincoln Island's saved agent prompts named the repository by its absolute path, and the agents' scratchpads by theirs: 1,436 lines in 360 files under `plan/archive/` and `plan/tasks/`, every one carrying the home folder and the user name. They were committed, so they are in the history as well as the tree. A path written from the repository's root works on every machine and names no one.

## CLAUDE.md rule

17. **No local paths in the files.** A tracked file names every path relative to the repository's root: never a home folder, a user name or a session scratchpad. Agents run in the repository's folder; a saved prompt names a scratchpad as `<scratchpad>`, and the real path is given only at run time. Run `python3 tools/check_paths.py` before committing an agent's prompt or report, and before a release.

## The file

`tools/check_paths.py` (standard library only). It scans the files git tracks for `/home/<name>/`, `/Users/<name>/`, `C:\Users\<name>`, `/tmp/claude-<n>/` and the root user's home folder, skips binaries and itself, lists each hit as `file:line`, exits 1 on any hit and prints `clean` otherwise.

## tools/README.md lines

In the table, after `check_clean.py`:

| `check_paths.py` | checks that no tracked file holds an absolute local path (a home folder, a user name, a session scratchpad); prompts and reports name paths from the repository's root | `python3 tools/check_paths.py` |

In the notes: **check_paths.py.** Run it before committing a saved prompt or report, and before a release. It scans the files git tracks (every file but `.git/` outside a checkout), skips binaries and itself, and lists each hit as `file:line` with the path; exits 1 on any hit, prints `clean` otherwise. `--root DIR` checks another folder.

## publication.md step (before section 1)

**First, the paths.** Run `python3 tools/check_paths.py`; it must print `clean`. An absolute local path in a saved prompt or report names the machine and the person who ran the work, and it survives in the history once committed, so clean it before the repository is made public.

## Also in the kit

The kit's own prompt templates and workflow examples, if any write "The repository is /path/...", should say "The repository is the current folder; every path below is relative to it." Run `check_paths.py` on the kit itself after applying.
