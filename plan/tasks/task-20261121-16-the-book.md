# Task: the book (phase 12)

- **Objective:** the novel as a book: our foreword, the scholar's preface, the restoration map, the 62 chapters with XIX bis, the scholar's notes at each chapter's back (linked both ways in the epub, pop-ups in the kepub), White's glossary, "THE END." after LXII; and the run's book beside it (R1121-162 to -166, R1121-158, R1121-160).
- **Every addition in its own file,** so a fork takes it out by deleting the file (R1121-163): the forewords and the map in `story/front/`, the notes in `story/scholar/`, XIX bis in `story/prose/01950-*.md`. *(Proposal, put to the author.)*
- **Steps:**
  1. The map's data from the patches made: `task-20261121-16-the-book/map_data.py` writes `map.tsv`, one mark per French paragraph (kept, patched, restored; rendered chapters whole). *(Done.)*
  2. The notes inventory: the papers' discords against themselves (timelines, directions), from the timeline's flags and its "Across the chapters" list, the place cards, and the errata rows that are internal; each with both quotes, from the final English text and the French; a discord the restoration removed from the page is not noted.
  3. The forewords and the notes drafted; a facts critic (quotes resolve; each note settles from the papers or leaves open; the narrator rule R1121-156 untouched; no held fact told).
  4. The builder: notes at each chapter's back with links both ways (epub); pop-up notes (kepub); the sample chapter to the author's Kobo first (R1121-166).
  5. The full builds, `build/lincoln-island` and `build/lincoln-island-run` (R1121-160).

## Log

- 2026-11-21 R1121-162 to -166 on the ledger. Four questions to the author (the map's form, the note marks, the files, the sample). The map's data: 3,224 patches; of the 38 patched chapters' French paragraphs, 945 kept, 1,554 patched, 754 restored; 24 chapters rendered.
