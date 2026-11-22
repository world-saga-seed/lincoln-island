# Roadmap

*Rewritten at the end of every session. Delete what is done; git keeps the history.*

## Now

Phases 0 to 12b are done, and phase 13 is drafted.
- **The novel:** all 63 chapters are final in `story/prose/`. Verne's 62 are White made unabridged; 01950 is XIX bis.
- **The forewords and the map** are in `story/front/`, and the scholar's 38 notes are in `story/scholar/`.
- **The two books** build from `plan/tasks/task-20261121-16-the-book/`: `build_book.py` makes `build/lincoln-island.*` and `build_run.py` makes `build/lincoln-island-run.*`. `build/` is not tracked.
- **The clearance** is done, and no modern translation was checked (R1121-180). The raw sources listed in `plan/tasks/task-20261121-17-clearance/release-exclude.txt` stay out of the public repo.
- **The report** is `REPORT.md`, and the post draft is in `plan/tasks/task-20261121-18-close/post-draft.md`.

## Next

1. **The community check** (BRIEF phase 13), at the author's word.
2. **The post**, at the author's word (BRIEF: "No push, no post, until the end and the community check").

## Waiting

- **On the author:**
  - The raw sources are to come out of the git history before the repository is made public. The author does this (R1121-180); this session leaves the history alone.
  - If a modern translation file is placed outside the repo, the overlap runs against it.
- Carried:
  - epubcheck has not been run on any build. None is installed; the XHTML is checked as well-formed.
  - The phase 4 scene lines on the large cards (length, not truth).
  - The text's discords are ruled when a draft leans on them (R1121-07).
- **Tasks left open on purpose:** 16, 17 and 18 stay in `plan/tasks/`. The README, REPORT and the build commands link into their folders, and the builders live there. Moving the builders to `tools/` and archiving the tasks is a step for the close, after the post.
