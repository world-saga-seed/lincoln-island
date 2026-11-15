# Prompt: attribution test (v1)

*One batch, in a book with two or more viewpoint heads. Refinement: add it when the POV file gives a chapter more than one head, or a book has several narrators. A cold reader is given paragraphs with their labels and breaks removed, and names whose head each is in from the voice alone. A paragraph it gives to the wrong head, or calls "could be either", is voice bleed: the drafters copied each other, or a fix flattened one head into the other.*

**Build the test by script, then run the reader.** Take the batch's narration paragraphs of 40 words or more, shuffle them, and write them unlabeled to the task's folder as `attribution-<range>.md`, headed `## P1`, `## P2` and so on, with no section breaks, titles or names of chapters. Keep the key (each P's file, line and head) in a file the reader is not given. Fifteen paragraphs is enough for two heads; take at least five from each.

```text
You are a cold reader for a test of a novel's prose, in the folder {REPO}. Read only one
file: {FILE}. Read nothing else. Write only {OUT}. Run no git commands and launch no agents.

The file holds paragraphs taken out of order from {WHAT}, told in {PERSON}, from inside the
heads of these people: {HEADS}, one line each on who they are. Each paragraph is from inside
one head.

For each paragraph, say whose head it is in, how sure you are (sure, likely, guess), and in
one sentence what in the prose itself told you: the diction, the rhythm, what the
narration notices or cares about. Do not rely on who is named in it; say whether you could
tell from the voice alone. Then, in a short paragraph, say how distinct the voices are
overall, and name any paragraph whose voice seemed wrong for its head or could belong to
either.
```

**Score it against the key.** A paragraph given to the wrong head, or called wrong for its head, is a finding of kind voice, severity weak, direction: "rewrite in <head>'s voice". A run of neutral paragraphs (procedure, a crowd, a room) that carry neither voice is a taste finding: give each such stretch one thing only its head would notice.

**Where it came from.** In a test of five narrations of one chapter, the voice critic missed a paragraph planted in the wrong head's voice and read the second head's real voice as a fault to cut. A cold reader with unlabeled paragraphs put all fifteen in the right head, named the planted one as "wrong for its head" by voice alone, and found a slip the drafter had made, for about a fifth of a critic run's cost.

**Calibrate it first,** as any critic ([principles](../principles.md#5-calibrated-before-it-is-trusted)): plant one paragraph rewritten in the other head's voice, and trust the test only once it is named.
