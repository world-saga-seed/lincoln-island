# Prompt: the blind probe, open run (v1)

*A fresh agent. The prose only. This run counts most.*

Make `{PROSE}` first: the stretch's chapters in reading order in one scratch file, with no notes, titles of drafts, or marks.

```text
You are a careful reader of a novel. Read only {PROSE}; do not read anything else. Run no
git commands. Do not launch agents.

When you have read it all:
1. Name every device, power, process, institution and being the story relies on. For each,
   say how it works and what it really is, as far as the text lets you.
2. Say what world this is, and when, and anything about the narrator or the people close
   to them that the text implies but does not say.
3. Say what you think the story is holding back, and what you expect to turn out true.

For every answer: quote the passages it rests on (exact, 25 words at most each), and mark
it sure, guessed or unknown. Guess boldly where the text invites it, and mark the guess as
a guess. Do not invent quotes.

Write it all to {OUT}, headed "# Probe, open run: {LABEL}". Then stop and wait: you will be
asked more questions in this same session.
```
