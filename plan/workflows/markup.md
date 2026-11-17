# Markup: a chapter's beats, marked by their source

*Speciality, for a book that needs it. Add it when you want to see, or show, whose beats a chapter carries: for yourself, for a writer who may take on the prose, or as the record behind a statement of authorship.*

An HTML page of one chapter that colours each passage by the source of its beat. The prose a model drafts is a placeholder for whoever writes it last; what the writer provides is the beat, so the measure is **keyframe against tween**, never verbatim words. Between the outline and the notes almost every piece has a source, so a passage the locators cannot tie to one is a **tween**: the model's own, between frames.

The page is local: `build/markup/<chapter>.html`. Keep `tmp/` and `build/` out of git, and keep the page on your machine; it is the prose.

## What the page shows

- **Text colour, by beat:** blue a **keyframe** (its source is the writer's: a ledger row of kind settled-author, an outline or notes bullet marked as the writer's, the writer's key frames), brown an **assisted** beat (a recommendation, a judgment, a proposal, or a bullet with no mark), gray a **tween** (no source).
- **Highlights, from the clue register** (`plan/reread-hooks.md`): pink a red herring, blue foreshadowing, green a structural puzzle. Give the register a Kind or Colour column to choose; without one, a row is green unless its ID starts FP or it says "herring". Lore, a card the outline or notes link, is a dotted underline.
- **Tooltips:** every marked span names its source (the ID, the bullet's section and text, or the ruling), whether it is a keyframe or assisted, and how to find it. Line numbers in the margin link to each paragraph.
- **The shares** of keyframe, assisted and tween, by characters of narrative, in the legend.

## Steps

1. **The items** (no tokens): `python3 tools/markup.py items CHAPTER` writes `tmp/markup/CHAPTER/items.md`: the chapter's clue rows, every outline and notes bullet (a retired outline is read from the tag it names), the cards they link, and the ledger rows they cite or that name the chapter. If you wrote a chapter whole before its outline was taken from it, add `--author-written CHAPTER`: every beat in its outline then counts as yours.
2. **Locate** (Haiku, at most 2 at a time): one locator ([locator.md](markup/locator.md)) per hundred items or so, each with its line range of the items file, output `tmp/markup/CHAPTER/finds-1.md`, `finds-2.md`. Keep each locator's reading under about 100,000 tokens. Log tokens in the token log.
3. **Render** (no tokens): `python3 tools/markup.py render CHAPTER` places every find whose quote is on the page and lists the rest at the foot as dropped.
4. **Read the misses.** A locator's `none` and its notes on near matches are a free consistency check: a beat the outline has and the page lost, or a page that says what a note says it must not.

## Limits

- **An unmarked bullet counts as assisted.** The cure is the mark on the bullet, not a guess on the page.
- **A locator finds, it does not judge.** A find says where a source lands, not that the page does it well.

## Lessons

- *(First runs, on the series the kit came from.)* Verbatim matching against the writer's own messages was tried and dropped: re-rendering left 0 to 1% of the writer's words on the page, and pasted reviews and manuscripts in the messages showed as the writer's. The beat is the honest measure.
- *(The same.)* A chapter the writer wrote whole showed 40% keyframe and a chapter built from five key frames 18%: the page tells the two ways a chapter is made apart. The locators' misses turned up a lost beat and a page breaking an outline's note.
- *(The same.)* A locator that cannot find an item's exact words calls the beat missing, and items often quote a character sheet, not the page (a sheet's "teased as a dumb blond" was on the page as "A blond."). So the locator quotes the passage that carries the beat in other words and marks it `reworded:`; only `none` is a loss to check.
