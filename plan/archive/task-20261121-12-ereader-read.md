# Task: phase 9, the ereader read

- **Objective:** the human reads the stretch as a reader; their comments reach this session through the author, and each comment and what the author did with it is a ledger row (BRIEF phase 9).
- **Context:** R1121-121. The build: `build/lincoln-island-xix-xx-v1.epub` (out of git), from commit 45bdeb0, by `plan/tasks/task-20261121-11-render-v1/ereader/build_epub.py`. Its checksum: 4e390a66b185a7ed19cf90d2967eaa507e5359362b370c9ea587156b877ce060.
- **Reading order:** White XIX; v1 XIX; XIX bis (marked as having no French original and no translation by White); v1 XX; White XX.
- **Region:** writes this task, the ledger, and the chapters' Next pass lists. No prose changes during the read (`plan/workflows/ereader.md`).
- **Start hash:** 45bdeb0 2026-11-21.
- **Status:** Closed, 2026-11-21 (R1121-132).

## Log

- 2026-11-21 Built: 7 pages (title, front, five chapters), about 13,400 words. Checked: the spine and contents are in the order above; the paragraph counts match the sources; no draft tags; the note on XIX bis is present; mimetype first and stored.

## Comments

(Filed as they arrive, by chapter and kind.)

1. **01950, line.** `"We had it, Pencroff," said Herbert. "For an hour."` It does not read as Verne; it is a line White would add. Now that the hour is on the page, the answer can be plainer. Filed: R1121-122, and the Next pass list of 01950 (item 3). The author chose try A (R1121-123): "Yes," answered Herbert; "and it lay under our hands the whole time the sea was out." Prose at the refine.

- 2026-11-21 The Kobo would not open the epub. The author made `build/lincoln-island-xix-xx-v1.kepub.epub` with kepubify (sha256 3cf1275a…bef), from the same epub (4e390a66…e060), so the text is the one built at 45bdeb0. From now on every build makes the kepub too (R1121-126). The v1 epub is not rebuilt, since the read is under way.

## Resolution

The human read the v1 build on a Kobo, from the kepub the author made (the plain epub would not open; every build now makes a kepub, R1121-126). Their comments came through the author: one on Herbert's line (R1121-122, -123), a Gemini read's chimney (R1121-127, -128), and the author's read-aloud of XIX bis in thirteen places (R1121-129 to -131), which stood in for phase 10's voice reading of the insert. Every comment went into draft 3 of the refine as a patch, beside v1, as asked (R1121-124). No prose in `story/prose/` changed during the read. Not done: the recorder of phase 10 (BRIEF phase 0 item 8) was not used; the read-aloud came as the author's cleaned-up text, so there are no recordings or transcripts to keep. epubcheck was not run, on the author's hold.
