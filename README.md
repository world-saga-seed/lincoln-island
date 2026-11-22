# Lincoln Island

*The Mysterious Island*, by Jules Verne: the whole novel of 1875, unabridged, in Stephen W. White's English of 1876, with one chapter added. Byline: "Jules Verne; the missing chapter by a model, by the World Saga Seed method".

## What the book is

White's translation of 1876 is the one English voice, but White cut and changed Verne as he went. Here every chapter has been put back to Verne's French (Hetzel, 1875): what White left out is restored in his manner, what he changed is set right, and where White's chapter was too far from Verne to mend, it was rendered anew from the French in his voice. Names, spellings and forms of address stay White's. Verne's own slips are listed in [the errata](texts/errata.md), with how each was handled. White's glossary of 1876 follows the last chapter as back matter, marked as his.

## What was added, and how to take it out

One chapter: **XIX bis, "The Float in the Bar"**, [story/prose/01950-the-float-in-the-bar.md](story/prose/01950-the-float-in-the-bar.md), set between Verne's chapters XIX and XX (1 to 3 June 1865). It has no French original and is marked so. Nothing else in the book was written for it: its neighbours, XIX and XX, are Verne's chapters as the rest are, and later chapters carry no line of its making.

To read Verne alone, leave that one file out: delete it, or build without it (`tools/epub.py --prose story/prose --from 100 --to 6200 --skip 1950`). The book is then Verne's unabridged, in White's English.

## Where to start

Read the chapters in order in [story/prose/](story/prose/), from [00100, "The Balloon in the Hurricane"](story/prose/00100-the-balloon-in-the-hurricane.md) to 06200, then the [glossary](story/backmatter/white-1876-glossary.md). A file's number is its place: 00100 is chapter I, in steps of 100, and 01950 is the inserted chapter.

## The builds

Two books, each as an EPUB and a Kobo kepub, under one name each, overwritten at every build: `build/lincoln-island` is the novel (the forewords, the map, the chapters with the scholar's notes, White's glossary), made by `python3 plan/tasks/task-20261121-16-the-book/build_book.py build/lincoln-island`; `build/lincoln-island-run` is the run's book (XIX, XIX bis and XX at every stage, the controls, the cards, the ledger and the blind scores), made by `build_run.py` beside it. `build/` is not tracked.

## Clearance

Every source is in the public domain: Verne's French (Hetzel, 1875, from fr.wikisource), White's English (1876, from Project Gutenberg), and, for measurement only, Kingston's (1875). The working texts in `texts/` carry none of Gutenberg's or Wikisource's own additions. The raw downloads are not in the public repository; each source's `SOURCE.md` and checksums say where to fetch them. Every published text was measured for runs of eight or more words shared with White and with Kingston (`tools/overlap.py`; the report is [the clearance task](plan/tasks/task-20261121-17-clearance.md)): the chapters written anew lean on Kingston's translation, about three words in ten. **No modern translation was checked.** Due diligence, not a legal opinion.

## How it was made

With the [World Saga Seed](https://github.com/world-saga-seed/world-saga-seed) kit, whose method is in [kit/](kit/pipeline/README.md); the run, phase by phase, is in [BRIEF.md](BRIEF.md), and the working rules in [CLAUDE.md](CLAUDE.md).

## The folders

| Folder | Holds |
|---|---|
| [BRIEF.md](BRIEF.md) | The run, phase by phase: who plays the author, the checks and gates. |
| [existing/](existing/README.md) | The sources as handed over, read-only, each with its SOURCE.md and checksums: [the French, Hetzel 1875](existing/hetzel-1875/SOURCE.md); [White's translation, 1876](existing/white-1876/SOURCE.md); [*Vingt mille lieues*, Hetzel 1870](existing/vingt-mille-hetzel-1870/SOURCE.md); Kingston's translation (closed until phase 12b). |
| texts/ | The French and White, paragraph by paragraph, the alignments, and the [errata](texts/errata.md). |
| world/ | The cards: [people](world/people/README.md), [places](world/places/README.md), [things](world/things/README.md). Each fact is cited to the French. |
| story/ | `prose/` (the book), `backmatter/` (White's 1876 glossary), `outline/`, `notes/` (with `characters/`), `voice/` (with `samples/`), `calendar/`. |
| [plan/](plan/README.md) | The [roadmap](plan/roadmap.md), the [state](plan/state.md), the [ledger](plan/settled/ledger/), tasks, the [token log](plan/records/tokens.md), and the kit's [workflows](plan/workflows/README.md) and [templates](plan/templates/README.md). |
| [tools/](tools/README.md) | The kit's scripts. |
| [kit/](kit/pipeline/README.md) | The kit's method: the pipeline, the interview, the reasons. |
