# The working texts

The texts every outline, card and ledger row cites, made from the sources in `existing/` (never changed) by the scripts here and vetted word for word against them (phase 1 of `BRIEF.md`). One file per chapter, one paragraph per line.

| Folder | From | Chapters | Cited as | Vetted |
|---|---|---|---|---|
| [fr-1875/](fr-1875/INDEX.md) | `existing/hetzel-1875/raw/` (R1120-04) | 62: I.1 to I.22, II.1 to II.20, III.1 to III.20 | `II.15 ¶30` | `python3 texts/vet_fr.py hetzel-1875 fr-1875`: 205,324 words, 0 differences |
| [vml-1870/](vml-1870/INDEX.md) | `existing/vingt-mille-hetzel-1870/raw/` (R1120-05) | 47: I.1 to I.24, II.1 to II.23 | `VML II.6 ¶64` | `python3 texts/vet_fr.py vingt-mille-hetzel-1870 vml-1870`: 143,200 words, 0 differences |
| [white-1876/](white-1876/INDEX.md) | `existing/white-1876/8misl10h.htm` (R1120-06) | 62: I to LXII, numbered straight through | `White XXXVII ¶30` | `python3 texts/vet_white.py`: 162,755 words, 0 differences |

To rebuild: `python3 texts/derive_fr.py hetzel-1875 fr-1875 22,20,20`; `python3 texts/derive_fr.py vingt-mille-hetzel-1870 vml-1870 24,23`; `python3 texts/derive_white.py`. Then run the three vets.

## The form of a line

- `hd [p.N] ...` is a heading: the part's title, or the chapter's number and title. ` / ` marks a line break. A heading line takes no number.
- `¶0 [p.N] ...` is the chapter's summary, the argument printed under its heading. Every chapter of *L'Île* has one in both the French and White; *Vingt mille* has none.
- `¶N [p.N] ...` is paragraph N, the citation number. `[p.N]` is the DjVu page the paragraph starts on, from Wikisource's page anchors (White's file has no pages). A table is one paragraph, its rows joined by ` | `.
- `[nN]` in a paragraph marks a footnote. The note itself is under **Notes** as `nN [¶N] ...`. These are Hetzel's footnotes, Verne's own or marked "(Avis de l'Éditeur.)", and are part of the text.
- Under **Plates and loose lines**: `plN [after ¶N, p.N]` is a caption of one of Férat's plates, and `lnN [after ¶N, p.N]` is text set outside any paragraph (a document, an inscription, a part's end line).

## What was changed, what was dropped

- **Changed:** no-break, narrow no-break and thin spaces become plain spaces, and runs of spaces become one. Nothing else is changed.
- **Kept as Wikisource reads them:** its corrections of printer's errors. Each is listed with the print's reading in `corrections.tsv` (8 in the French *L'Île*, 9 in *Vingt mille*). Three in *L'Île* change a fact, and a citation resting on any of them should say so:
  - I.12: the print's "basse" is read "haute" (the island's latitude "sans doute trop haute" for the coconut palm);
  - II.20: note n1's "106" is read "83" ("Environ 83 kilomètres à l'heure");
  - III.10: "novembre" is read "décembre" (¶52, "cette journée du 7 décembre").
- **Dropped:** Wikisource's own additions (its headers, footers, navigation, `ws-noexport` blocks and styles), the figures themselves, the footnote back-links and the page anchors. From White: Gutenberg's header and footer, the redactor's note, the title page and the contents. These are CC BY-SA or Gutenberg's, not Verne's, and are not shipped (R1120-23).

## The scan check

Ten pages were read by eye, without OCR (R1120-31), and one more later (R1120-40), from the Commons DjVu of the Gallica scan (`File:Jules Verne - L'Île mystérieuse.djvu`, credited to Gallica `bpt6k1033380`, 620 pages, sha1 `2360ed184643a54ca4b8a607cc6cc3eb3f87b6e1`). Gallica itself refused the automated fetch (HTTP 403). The DjVu page number is the printed page number on every page read, so `[p.N]` is also the page of the 1875 book. The images were kept in the session's scratch folder and not committed.

| Page | Read against | Result |
|---|---|---|
| 2 | I.1 ¶4 to ¶17, note n1 | matches |
| 108 | I.12 ¶41 (end) to ¶46 | matches, except Wikisource's correction: the print reads "trop basse" |
| 126 | I.14 ¶22 to ¶25, the table, note n1 | matches, except one slip: the print's "très-exactement" (¶25) lost its hyphen on Wikisource. The other 237 cases of "très-" keep it. |
| 223 | II.2 ¶52, the start of ¶53 | matches |
| 300 | II.9 ¶80 to ¶84, ln4, ln5 | matches |
| 358 | II.15 ¶27 to ¶32 | matches |
| 406 | II.20 heading, ¶0, the start of ¶1 | matches |
| 407 | II.20 ¶1 (end), note n1 | matches, except Wikisource's correction: the print's note reads "Environ 106 kilomètres à l'heure" |
| 508 | III.10 ¶48 to ¶53 | matches, except Wikisource's correction: the print reads "7 novembre" |
| 566 | III.16 ¶30 to ¶36, note n1 | matches |
| 460 | III.4 ¶80 to ¶93 (read later, R1120-40) | matches: the print itself reads "le 30 novembre" for the torpedo's finding, so the date before III.5's "8 novembre" is Verne's, not Wikisource's |

**What it shows.** The transcription is faithful: one slip of a hyphen in ten pages, and no word wrong. All three of Wikisource's corrections that change a fact are confirmed as changes to what Hetzel printed. Two of them are editors' judgments rather than misreads:

- **II.20 n1, "106" read as "83".** Forty-five nautical miles an hour is about 83 km; forty-five land miles is about 72. The print's 106 fits neither, and the emendation is Wikisource's arithmetic. *(My reading, to confirm.)*
- **III.10 ¶52, "novembre" read as "décembre".** The paragraphs around it are dated in December ("le 6 décembre", ¶34; "8 décembre", ¶56), so the print's November is a slip that Wikisource mended.

A card resting on any of these cites the paragraph and gives both readings.

## White and the French

White's chapters are numbered I to LXII straight through. The French restarts its numbering in each part, so the French II.1 is White XXIII and the French III.1 is White XLIII. Phase 3 aligns them paragraph by paragraph.

## The alignment (phase 3)

`texts/align/NN.tsv` pairs White's paragraphs with the French: one row a bead (a run of French paragraphs and the White ones that render them), made by `texts/align_white.py`. Its kinds "cut?", "add?", "short?" and "long?" are hints. `texts/align/NN-side.md` sets each bead's two texts side by side (`texts/side_white.py`). `texts/align/NN-discords.md` lists every place White departs from the French, with its kind (cut, condensed, addition, changed, softened) and both texts quoted (R1120-43); `plan/tasks/task-20261120-04-white-align/check_white.py` checks them. White's III.20 ends with a glossary of 92 entries after "THE END.", the edition's own; it is not aligned. White's II.17 ¶80 and I.19 ¶31 break mid-sentence ("two or four years of"; "head-cook Neb was not particular"), as the Gutenberg HTML does; and White's I.2 ¶25 repeats ¶23's question where the French has ¶29, again as the HTML has it.
