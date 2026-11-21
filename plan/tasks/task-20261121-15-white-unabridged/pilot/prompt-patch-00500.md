# The patcher's prompt, I.5 (the pilot, R1121-147)

---

You are patching one chapter of Stephen W. White's 1876 English translation of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) so that it renders the whole of Verne's French, in White's own voice. The repository is the current folder; every path below is relative to it. Every file is read-only except your one output file. Run no git commands of any kind (not even status or log): another session may be editing this folder. Do not launch agents. Work alone.

Read, and nothing else:
1. the French: texts/fr-1875/05.md (paragraph-numbered, ¶0 the summary, n lines the footnotes, pl lines plate captions, not rendered);
2. White's chapter: texts/white-1876/05.md (paragraph-numbered; the "¶N " at each line's head is not part of his text);
3. the list of where White departs from the French in this chapter: texts/align/05-discords.md (each discord gives its kind, the French paragraph, the French quote and White's words);
4. story/voice/white.md (the voice sheet), story/voice/names.md, story/voice/spelling.md, story/voice/banned.txt, and plan/workflows/drafting/rulings.md (the rules of the page).

THE RULE (R1121-146), discord by discord:
- **cut** or **condensed:** restore what the French says, in White's voice, at the place White would have said it;
- **changed** or **softened:** correct White's words to the French;
- **addition:** remove White's words only where they add a fact the French lacks; keep a stylistic addition;
- keep White's names and forms of address (Herbert, Neb, Mr. Smith), his spelling and his sentences everywhere else. Change no more of his text than the discord needs.
If in reading you find a departure the list does not hold, do not patch it: report it.

Write your patches to plan/tasks/task-20261121-15-white-unabridged/pilot/patches-00500.tsv, one per line, tab-separated, with a header line "id	discord	old	new":
- id: P1, P2, …;
- discord: the list's number, as "5.3" for I.5's discord 3;
- old: White's exact words to replace, copied unbroken from texts/white-1876/05.md without the "¶N " prefix; long enough to occur only once in the chapter;
- new: the replacement, which must keep the old words wherever they stand, and add or change only what the discord needs. Use "¶" for a paragraph break inside new. Never use a tab or a line break inside a field. Use straight quotes as White's file has them, or the exact characters his file has.
For a removal, new is old without the added words.

Finish with a short report (your final message): the number of patches; each discord you did not patch, and why; any departure you found that the list lacks, quoted (French and White); and every French phrase you were unsure how to render.
