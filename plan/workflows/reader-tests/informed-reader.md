# Prompt: the reread test, informed reader (v1)

*A fresh agent per truth. Never the probe's agent.*

```text
You are rereading part of a novel, knowing one thing a first reader does not. Read only
the files named here. Run no git commands. Do not launch agents.

The truth: {TRUTH, quoted from its source in the notes}.

Now read, in order: {CHAPTERS}.

Knowing this truth:
1. How do you read each scene now? A line or two per scene.
2. Which lines change meaning? Quote each exactly (25 words at most) and say what it
   meant before and what it means now.
3. Which lines look planted for this truth? Quote them.
4. Does anything now contradict the truth? Quote it.
5. Per scene, one word: pays off (lines turn), flat (nothing changes), contradicts, or too
   obvious (a first reader would surely have got it).

Write it to {OUT}, headed "# Reread: {TRUTH ID}".
```
