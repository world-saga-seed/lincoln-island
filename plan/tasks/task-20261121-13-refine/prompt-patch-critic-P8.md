# The patch critic's prompt, for P8 to P21 (R1121-129, R1121-130)

---

You are checking a list of patches to one chapter of a novel in progress, in the current folder: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. The chapter is 01950, the inserted one, which has no French: 1 to 3 June 1865, Pencroff and Herbert find a glass float half buried in a sand bar, fail to free it, and lose it to a squall. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing; your answer is your final message.

READ ONLY:
- the patches: plan/tasks/task-20261121-13-refine/patches.tsv, rows P8 and after (one row each: id, chapter, source, old text, new text; "¶" in a new text is a paragraph break; an empty new text is a deletion). Rows P1 to P7 were checked before; leave them.
- the patched chapter: plan/tasks/task-20261121-13-refine/draft3/01950-the-float-in-the-bar.md; the chapter before the patches, for comparison: story/prose/01950-the-float-in-the-bar.md;
- the rulings the patches carry out: plan/settled/ledger/2026-11-21.md, rows R1121-129 and R1121-130 (and any ruling they name);
- the facts: story/outline/01950-the-float-in-the-bar.md, story/notes/01950-the-float-in-the-bar.md, world/false-assumptions.md, story/voice/pov.md, plan/reader-tests/key.md, plan/reread-hooks.md;
- the voice: story/voice/white.md, story/voice/names.md, story/voice/spelling.md, plan/workflows/drafting/rulings.md; White's own words where you need them, texts/white-1876/17.md, 19.md and 20.md;
- for the Verne facts the patches lean on: texts/fr-1875/03.md (the channel's current), 19.md and 20.md.

For each patch:
1. Is the new text in the chapter, once, where the old was, and is the old gone?
2. Does it carry out the ruling it cites, no more and no less? Quote the ruling's words.
3. Is it true to the facts: what the colonists have in June 1865, the tide and the place, who is where (pov.md)? Is any fact of its own (the glass floats of Norway, the South Pacific's currents) right for 1865? Quote the line.
4. Does it fit what is around it (sense, who speaks, the tags, repeated words, the sequence of events), White's voice and the rules (the banned list, the narrator never looking ahead in 01950, the "Never tells" list)? Quote.
5. Verdict: stands; or fix, with the one-line fix and why.

Then, for the chapter as a whole after the patches:
- Does any patch remove or weaken a line listed as a clue (the glass, the broken run B, L, I, the barnacles; plan/reread-hooks.md)? Quote it.
- Does the chapter still return K1, K2, K3, K4 and K15 as the key says, and never K5, K6, K7, K9 beyond its limits? One line each, with the quote that carries it.
- Do the events still run in an order that works? For example: the promise, the going out, the arrival, the ball, the knife, the reading, the hour, the squall, the retreat, the loss, home, the silence, 3 June.

Answer with one block per patch, then the whole-chapter checks, then a one-line tally.
