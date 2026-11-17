# Prompt: inference judge (Sonnet)

*About 60 to 70 finds a run (two chapters' worth). Judges [the inference finder](inference-finder.md)'s list from the prose itself.*

```text
You judge a novel's first-person inferences, in the repo {REPO}. Read-only except your one output file. Run no git commands. Spawn no agents except at most 2 cheap assistants at a time for lookups (each writing nothing, spawning none).

{NARRATOR} He may state only what he saw, heard, touched or was told, or his own thoughts; anything else needs its grounds.

Read the finder's list {FINDS}. Its lines point at {PROSE}. For each entry, judge from the prose itself (open it at the line, read the paragraph and the two before), never the finder's gloss, which can be wrong or backwards. **The grounds must come first.** The telling is contemporaneous, so what grounds a claim must come before it or in its own sentence: a motive, feeling or past stated first and borne out later in the scene is still a break, since he could not know it when he said it.

**Check the plot before any break or question.** A line that looks unplanted, a slip or a contradiction is checked first against the chapter's notes and outline, the person's character sheet, the cards the notes link, the clue register, and a search of the ledger for the person or thing. A beat settled there passes, with its citation: an age on paper against an age by body may be the plot, and one object may go by two names. Only what the plot does not settle is a break or a question.

Sort each into one of:

1. **Grounded:** what he saw, heard or was told in the same beat supports it (a sign shown: a look, a callus, a word said). Pass silently.
2. **Known from before:** he could know it from an earlier chapter: something he was told, saw, or learned there. Before calling any break, search the earlier prose and the person's sheet for when he learned it. If found, pass it, citing file:line in one line.
3. **Common knowledge:** what any local knows (a trade's tools, a custom, what the town says). Pass silently.
4. **A verdict with no evidence** (a break): a person's past, trade or rank, a motive, what a thing is for, or a cause, stated with no grounds on the page and none from before.
5. **Someone else's inside as fact** (a break): another's feeling, thought or intent stated with no sign shown and none from before.
6. **Left to the reader on purpose** (a question for the writer): the page shows the signs and the narrator does not draw the conclusion, or draws one the reader may doubt; detail can be a red herring that follows the narrator's eye.

Write to {OUT}, headed "# Judge, inference", with:
- **Breaks** (4 and 5): file:line, the quote, which kind, why in one sentence (what you searched for grounds, and where), and a fix that gives the missing lead before the claim (a sign he saw, a word someone says, or his own read marked as his), in a few words. A cut only when the claim is incidental and nothing he could have seen would carry it.
- **Known from before** (2): one line each with the citation.
- **Questions** (6): file:line, the quote, both readings.
Then a tally. Do not rewrite any file. Inventing a finding is worse than missing one.

{NOTES}
```

**`{NARRATOR}`** as for the finder. **`{FINDS}`** one or two finder lists. **`{PROSE}`** their chapters. **`{NOTES}`** anything run-specific: chapters with another narrator, and chapters the writer wrote whole, where every break is a question only, never a fix.

**After the judge: the supervisor checks every break against the page and the plot** before it goes to the writer. On the first full run, three of ten called breaks were grounded a few lines earlier or settled in the notes. The questions get the same check; four the writer saw unchecked were all settled canon.
