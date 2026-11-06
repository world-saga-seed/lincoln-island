# Prompt: the blind probe, asked run (v1)

*The same agent, after the open run is written: in Claude Code, continue the agent that did the open run by sending it a message, so it keeps what it read; do not launch a new one. The supervisor shuffles the real questions (the key's entries and the story questions whose ranges cover this stretch) among at least as many decoys: questions about the setting the book has no stake in ("What do people here eat in winter?", "Who owns the inn?").*

```text
Now answer these questions about the same book, from what you read. The list is mixed:
some questions matter to the story and some do not, and nothing in the order or wording
is a clue.

{SHUFFLED QUESTIONS, NUMBERED}

For each: your answer; the passages it rests on, quoted exactly (25 words at most each),
each on its own line as "- quote: the exact words"; and sure, guessed or unknown. "Unknown" is a good answer when the text does not say. Do not
reread anything except {PROSE}.

Write your answers to {OUT}, headed "# Probe, asked run: {LABEL}".
```

**Score the open run before reading the asked run.**
