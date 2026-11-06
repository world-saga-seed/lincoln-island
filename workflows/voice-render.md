# Voice render (optional): a chapter as audio

*Refinement. Add this when the writer wants to listen.*

## Purpose and when

A drafted chapter rendered to speech, so a read can be a listen. Rhythm faults (a run of short kicker lines, a sentence that never ends) are often easier to hear than to see. Only if the writer wants it, after a chapter is refined; a short pilot first.

## Setup (once)

- Use a local, open-source text-to-speech engine, installed in its own Python environment outside the book's folder, so nothing leaves the machine. A recent consumer graphics card is enough for most; check the engine's own requirements.
- Write a small script that reads a prose file and writes a WAV or MP3 (keep it in `tools/`, with a `--help`). The kit does not ship one, because it depends on the engine you choose.

## What the script should do

- Speak the title without the draft tag; drop markdown.
- **Split paragraphs into pieces of a few hundred characters at sentence ends:** many engines drift on long inputs.
- Put short pauses between paragraphs and longer ones at `---`.
- **Deliver flat by default,** with a fixed random seed, so the narrator does not drift between pieces. A restrained narrator is broken by a reading that oversells.
- Offer `--words N` to render only the opening, for a pilot.
- Write to `build/voice/`, out of git.

## Not built by default, worth adding

- **A pronunciation table** for invented or unusual names, applied before rendering, settled by the writer.
- **More voices,** one per narrator, so a shift of point of view is audible (most engines take a short reference recording).
- **A sparse direction pass:** tags only where the text says how a line is said ("under her breath").

## Rules

- Never render text you have no right to render: only the writer's own book.
