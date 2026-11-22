# Task: phase 12b, the clearance

- **Objective:** BRIEF phase 12b: (1) every input's licence checked and recorded; (2) the overlap of every published text with White's and Kingston's translations, and with any modern translation the human owns; every long run against a modern one reviewed.
- **Context:** R1121-178 opens it; `existing/kingston-1875` opens with it (the author's ruling of 2026-11-20).
- **Region:** writes this task and its folder, `tools/overlap.py`, `kit-patches/0001-tools-overlap.md`. Reads `existing/` (read-only), `texts/`, `story/prose/`, the run's versions.
- **Start hash:** 95d7739 2026-11-21.
- **Status:** executing; waits on the human for any modern translation.

## (1) Inputs

| Source | Licence | In the derived texts | In the repo as handed over |
|---|---|---|---|
| Verne's French, Hetzel 1875 (fr.wikisource, Gallica scan) | public domain; Wikisource's own additions CC BY-SA | stripped (`texts/derive_fr.py`: ws-noexport, headers, footers, styles); the edition's page numbers kept as `[p.N]` (a fact of the print) | `existing/hetzel-1875/raw/*.html`, Wikisource's pages whole, with their additions |
| White 1876 (Gutenberg #8993) | public domain in the USA; Gutenberg's "Small Print!" licence on the wrapper | header, footer, redactor's note, title page and contents left out (`texts/derive_white.py`) | `existing/white-1876/`, the release whole, wrapper and Wolcott's note included |
| Kingston 1875 (Gutenberg #1268) | public domain; Gutenberg wrapper | not derived; measurement only | `existing/kingston-1875/milnd11.txt`, whole |
| *Vingt mille lieues*, Hetzel 1870 (fr.wikisource) | public domain; Wikisource additions CC BY-SA | carded facts only | `existing/vingt-mille-hetzel-1870/raw/*.html`, whole |
| Webster 1864 (Internet Archive OCR) | public domain | none (a word check) | `existing/webster-1864/`, the OCR whole |

**For the public repository** (R1121-180): the raw files listed in `release-exclude.txt` (116 paths under `existing/`) stay out; each `SOURCE.md` and `SHA256SUMS` stays. The author removes them from the history at the close; this session leaves the history alone.

No derived or story file carries Gutenberg's wrapper, Wolcott's note or Wikisource's additions (grep of every tracked file outside `existing/`). The raw files in `existing/` do.

## (2) Overlap, runs of 8+ words (`tools/overlap.py`)

| Text | words | shares with White | shares with Kingston |
|---|---|---|---|
| The novel, all 63 chapters | 205,694 | 43.6% | 19.2% |
| the 38 patched chapters | 121,466 | 69.4% | 13.3% |
| the 24 rendered chapters | 81,033 | 6.7% | 28.9% |
| XIX bis | 3,195 | 0.0% | 0.3% (longest run 8) |
| *For scale:* White's own text, against Kingston | 170,584 | — | 7.1% (6.1% in the rendered chapters' span, 7.6% in the patched) |
| The controls, XIX and XX (Opus, Gemini) | | 4.7–7.6% | 15.5–25.5% |
| Ours, XIX and XX (v1 and final) | | 4.6–5.5% | 24.7–26.4% |

**Modern translations:** none checked (R1121-180); the README says so. If the author places one outside the repo, the overlap is run against it and every long run reviewed.

Per-file tables: `novel-vs-white.tsv`, `novel-vs-kingston.tsv`, `white-vs-kingston.tsv`, `run-vs-white.tsv`, `run-vs-kingston.tsv`.

**Finding.** The rendered chapters, written "in White's English", share four to five times as much with Kingston as White's own text does (28.9% against 6.1%), in runs up to 62 words (XXXIII, the albatross's message) and 36 (XIV, the latitude). No agent was given Kingston (it stayed closed); the models remember it. The prompt-only controls lean on it as much. Kingston is in the public domain, so this is a question of voice and of what the release claims, not of law. The patched chapters' restored passages lean on it too (13.3% against White's 7.6%). **Said plainly** in our foreword (R1121-179): "Those chapters lean on W. H. G. Kingston’s translation of 1875, which the models evidently remember: about three words in ten are in runs of eight or more shared with his, where White’s own text shares fewer than one in ten."

## Log

- 2026-11-21 R1121-179: the lean said plainly; the famous-phrase and clarity checks run; modern translations and existing/ wait on the author.
- 2026-11-21 Opened. Inputs audited. `tools/overlap.py` and its kit patch written. Overlaps run. Questions to the author.
- 2026-11-21 The famous-phrase check: 27 lines, none found (`famous-phrase.md`). The cold reader of the two forewords: the smallest fixes applied (glosses for the method, the patch, XIX bis, the controls, the cards and ledger; "now given to" made "usually credited to … though the edition names no translator"; referents named); the author may overturn (R1121-130).
