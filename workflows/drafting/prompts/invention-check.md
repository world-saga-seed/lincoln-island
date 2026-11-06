# Prompt: invention check (v1)

*A small standalone run, after a pass, on one inventions log. Never run by an agent on the main path. It edits nothing.*

```text
You are checking a list of small inventions for a novel in progress, in the folder {REPO}.
Every file is read-only except your one output file. Run no git commands. Do not launch
agents.

Read: {LOG} (the inventions, one row each: the new fact, file:line, the cards it touches,
who made it); for each row, the cited line in its file; the cards the row names; and the
setting's core rules, {RULES}. Read nothing else.

For each row:
1. Against the canon: does the fact clash with any card it touches? Quote the card line.
2. Against what is to hand: could a person in that place, time and trade reach it with the
   tools, materials and knowledge they have? Would they think of it? For a custom or an
   institution: what pressure made it, and what came of the same pressure in real history?
3. Verdict: stands; reword (consistent in substance, a word or a part wrong; give the
   fix); break (a canon clash; give the canon line); or to the writer (it touches a
   settled line or a key frame, or it has no pressure and no precedent).

The question is whether each invention is consistent, not whether it is the best choice.
People in a story pick what they would think of, not the optimum.

Write a table to {OUT}: row number, the fact in a few words, verdict, the card line or fix,
one line of why. Finish with the counts by verdict.
```
