# Task: the book (phase 12)

- **Objective:** the novel as a book: our foreword, the scholar's preface, the restoration map, the 62 chapters with XIX bis, the scholar's notes at each chapter's back (linked both ways in the epub, pop-ups in the kepub), White's glossary, "THE END." after LXII; and the run's book beside it (R1121-162 to -166, R1121-158, R1121-160).
- **Every addition in its own file,** so a fork takes it out by deleting the file (R1121-163): the forewords and the map in `story/front/`, the notes in `story/scholar/`, XIX bis in `story/prose/01950-*.md`. *(Proposal, put to the author.)*
- **Steps:**
  1. The map's data from the patches made: `task-20261121-16-the-book/map_data.py` writes `map.tsv`, one mark per French paragraph (kept, patched, restored; rendered chapters whole). *(Done.)*
  2. The notes inventory: the papers' discords against themselves (timelines, directions), from the timeline's flags and its "Across the chapters" list, the place cards, and the errata rows that are internal; each with both quotes, from the final English text and the French; a discord the restoration removed from the page is not noted.
  3. The forewords and the notes drafted; a facts critic (quotes resolve; each note settles from the papers or leaves open; the narrator rule R1121-156 untouched; no held fact told).
  4. The builder: notes at each chapter's back with links both ways (epub); pop-up notes (kepub); the sample chapter to the author's Kobo first (R1121-166).
  5. The full builds, `build/lincoln-island` and `build/lincoln-island-run` (R1121-160).

- **Status:** Closed (left in place: its builders and copies are what the build commands use).

## Log

- 2026-11-21 R1121-162 to -166 on the ledger. Four questions to the author (the map's form, the note marks, the files, the sample). The map's data: 3,224 patches; of the 38 patched chapters' French paragraphs, 945 kept, 1,554 patched, 754 restored; 24 chapters rendered.
- 2026-11-21 R1121-167 on the ledger (the author's answers). Map drawn per Part as SVG and PNG (`draw_map.py`), with the table in the build. Our foreword, the scholar's preface and the map page in `story/front/`; sample notes in `story/scholar/05800.md` and `01950.md` *(Proposal.)*. Builder `build_book.py`: endnotes linked both ways (epub), asides as pop-ups (kepub). Sample book (front matter, XIX bis, LVIII) built to `build/lincoln-island-sample.*`, well-formed; no epubcheck on this machine. Sent to the human's device. Open: 05800's note (b) points to notes on chapter XXXIX not yet written; the full inventory waits on the sample's verdict.
- 2026-11-21 R1121-168, -169. XIX bis's tide notes cut (no two same-phase clock readings in the papers to give a rate). The map redrawn in the draft's form from the patches; map page and foreword updated; sample rebuilt.
- 2026-11-21 R1121-170: a rule before the notes. The run's book: `build_run.py` and `run-front.md` *(Proposal.)*: XIX, XIX bis and XX each as White, the Opus and Gemini controls, v1 and the final, then the cards and the ledger; built to `build/lincoln-island-run.*`, 22 pages well-formed. A trial build of the novel (69 pages) is well-formed, ends with THE END. and White's 91 glossary entries. The notes drafter is out (one fresh agent).
- 2026-11-21 R1121-171, -172. The run's book: XIX bis at every stage (v1 = the render-v1 snapshot; after the read-aloud = b4d375a, draft 3 final; after the character check = 7b10525, after R1121-143 (R1121-173); the final), copies in `stages/`; the blind scores copied from tmp/scores into `blind-scores.md`; the read-aloud as sent, from the session transcript, in `read-aloud.md`. 01900's "hydraulic lift" is "hydraulic elevator" (the only one in the prose). 26 pages well-formed.
- 2026-11-21 The notes drafter: 36 notes in 26 new files *(Proposal.)*, anchors unique, inventory in `notes-inventory.md`; the trial build passes. A fresh facts critic is checking every claim.
- 2026-11-21 The critic: 22 stand, 15 fixed (`findings-notes.md`). The full builds: `build/lincoln-island.*` (69 pages, 38 notes) and `build/lincoln-island-run.*`; sent. Open for the author: the numbered notes' wording, XXXIII's "winter of 1866-67", a check of the two forewords.

## Resolution

The two books are built: the novel with the forewords, the map, 38 scholar's notes, THE END and the glossary; the run's book at every stage with the cards, the ledger, the scores and the read-aloud (R1121-162 to -178, -181).
