# The patch critic's prompt (R1121-124)

---

You are checking a list of small patches to three chapters of a novel in progress, in the current folder: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. 01900 and 02000 render Verne's I.19 and I.20 from the French. 01950 is the inserted chapter, which has no French. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing; your answer is your final message.

READ ONLY:
- the patches: plan/tasks/task-20261121-13-refine/patches.tsv (one row each: id, chapter, source, old text, new text);
- the patched chapters: plan/tasks/task-20261121-13-refine/draft3/*.md;
- for 01900 and 02000, the French: texts/fr-1875/19.md and 20.md, and White's own chapters, texts/white-1876/19.md and 20.md (for his words only);
- for 01950, P7 rests on the French of I.19 ¶46 (texts/fr-1875/19.md, the sentence "Peut-être, sans doute même, par les grands vents d’est…") and must not refer back to it; also story/outline/01950-the-float-in-the-bar.md and story/notes/01950-the-float-in-the-bar.md (the settled lines), and plan/reader-tests/key.md (its K3 entry);
- the rules: plan/workflows/drafting/rulings.md, story/voice/names.md and story/voice/spelling.md.

Check only patch P7 (the last row); P1 to P6 were checked before. For each patch, answer four questions:
1. Is the new text in the chapter, once, where the old text was, and is the old text gone?
2. In 01900 and 02000: is the new text truer to the French than the old, with nothing added and nothing lost? Quote the French. In 01950: does it match the settled line it cites, word for word?
3. Does it fit the sentence and paragraph around it (grammar, sense, who speaks, the tag), and White's voice and the rules?
4. Verdict: stands; or fix, with the one-line fix and why.

Then one more question: does any patch break a line the outline marks as a clue, or change what a reader would take from K3? Quote the line.

Answer with one block per patch: id, the quotes, the verdict. Finish with a one-line tally.
