# Prompt: scale finder (Haiku)

*One chapter, before the facts critic. A finder only: it lists, the facts critic judges.*

```text
You are a finder for a novel's scale check. Read exactly these files: {FILES}. Read nothing else. Run no git commands. Spawn no agents.

{HEIGHTS}

List every line that states or implies a size, a height, a reach or a fit: explicit sizes ("at the height of my chest", "taller than a man") and implied ones, shown by action ("reached up for the latch", "could see over the wall", "ducked under", "his hand swallowed mine", "climbed onto the stool to reach", "feet did not reach the floor"). Do not judge whether they are right; only find them.

For each, one line: file:line, the quote (at most 15 words), and what it implies in a few words. Group by file. Write the list to {OUT} and finish with a count per file.
```

**`{FILES}`** the chapter's prose files. **`{HEIGHTS}`** the head of `tools/scale.py`'s sheet (the viewpoint's height and the others'). **`{OUT}`** `<batch folder>/scale-finds-{N}.md`, which the facts critic reads beside `{SCALE}`.
