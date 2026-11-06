# Ereader: the writer reads the volume as a reader would

*Refinement. Add this when a stretch is long enough to read as a book.*

## Purpose and when

Drafted volumes go to the writer as EPUB books. The writer reads them on an ereader, as a reader would meet them, not as files, and comes back with comments. This is how a volume reaches the writer's markup.

**Grade.** The build is mechanical: it reproduces the prose files or it does not. Filing the comments is a judgment.

Run it when a volume (or any stretch the writer wants to read) is refined. Build once; while the writer is reading and sending notes, do not rebuild after each fix. Rebuild when the notes stop, and say so.

## Build

```bash
python3 tools/epub.py --title "Volume 1" --author "Your Name" --series "Your Series" --index 1 \
    --front story/volume/front-matter.md \
    --prose story/prose --outline story/outline --from 100 --to 2000 \
    --out build/volume-1.epub
```

- **What goes in:** each prose file's text only. The draft tag in the title and `<!-- comments -->` are dropped; `---` becomes a scene break.
- **Gaps show:** with `--outline`, a chapter that has an outline and no prose gets a "[Not yet drafted.]" page under its title, so the gaps fall where they will be.
- **Front matter:** `--front` sets a page before the first chapter (only what follows its first `---`, so the top of the file can hold writer-side notes). **A later volume opens on the story so far** (the interest check's recap), so a reader who comes back after a break is not lost.
- **Series metadata** groups the books on readers that support it.
- **Tracing a comment back:** each chapter is its own page, and every paragraph carries its source line as an id (`p87` is line 87). A highlight names its page; its quoted text finds the line.
- **Kobo readers:** `--kepub` also runs kepubify if it is installed; send the `.kepub.epub`, which the device's own renderer reads with the reader's settings. Put only one of the two files on the device.
- Keep `build/` out of git.
- Check a build with epubcheck if you have it.

## Comments back

1. Export the highlights and notes from the device (most readers store them in a database or an export file: the book, the page, the highlighted text, any typed note).
2. File each comment against its chapter: a **reading** item on the chapter's Next pass list, a question for the writer, or a drift row in `plan/state.md`.
3. Rebuild once the chapters change.

## Lessons and failure modes

- **Set an explicit base font size** in the stylesheet (`html` 100%, `body` 1em). Without one, some readers render a sideloaded book at a very different size from their other books.
- **A copy on the device may not appear until the device imports it,** usually on disconnect.
- **Keep comments traceable** to page and paragraph, or filing them becomes guesswork.
