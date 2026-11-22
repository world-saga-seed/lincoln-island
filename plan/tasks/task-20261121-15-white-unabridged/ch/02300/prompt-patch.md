# The patcher's prompt, v2 (R1121-149: a full reading, not only the list)

---

You are patching one chapter of Stephen W. White's 1876 English translation of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) so that it renders the whole of Verne's French, in White's own voice. The repository is the current folder; every path below is relative to it. Every file is read-only except your one output file. Run no git commands of any kind (not even status or log): another session may be editing this folder. Do not launch agents. Work alone. Run no command.

Read, and nothing else:
1. the French: texts/fr-1875/23.md (paragraph-numbered, ¶0 the summary, n lines the footnotes, pl lines plate captions, not rendered);
2. White's chapter: texts/white-1876/23.md (paragraph-numbered; the "¶N " at each line's head is not part of his text; "hd" lines are headings);
3. a list of some of the places where White departs from the French: texts/align/23-discords.md. It is incomplete: in the pilot it held 7 of about 60 departures.
4. story/voice/white.md (the voice sheet), story/voice/spelling.md, story/voice/banned.txt, and plan/workflows/drafting/rulings.md (the rules of the page).

YOUR TASK: read the chapter sentence by sentence against the French, and patch every place where White's English says something other than the French: a word, a clause or a sentence cut; a passage condensed; a fact, figure, name, number, tense or person changed; a feeling, force or qualifier softened or raised (including "très", "extrême", "peut-être", "du moins"). The list is a start, not the whole. Ordinary English choices that keep the sense are not departures.

THE RULE (R1121-146), by kind:
- cut or condensed: restore what the French says, in White's voice, at the place White would have said it;
- changed or softened: correct White's words to the French;
- an addition of White's: remove it only where it adds a fact the French lacks; keep a stylistic addition;
- keep White's names and forms of address (Herbert, Neb, Mr. Smith), his spelling and his sentences everywhere else. Change no more of his text than each departure needs. Restored English must sound like White: plain, period, no word later than 1876;
- where the French names Nab and White writes "the negro" (or "the black"), write "Neb": the label is White's, not Verne's. Where the French has "le nègre", keep White's word. Where the French has "l'esclave", say "the slave".
- fix White's print slips where you see them (a stray capital, a full stop for a comma, a stray quotation mark).

Write your patches to plan/tasks/task-20261121-15-white-unabridged/ch/02300/patches-02300.tsv, one per line, tab-separated, with a header line "id	discord	old	new":
- id: P1, P2, … in the order they fall in the chapter;
- discord: the list's number, as "23.3", or "new" for a departure the list lacks, or "slip";
- old: White's exact words to replace, copied unbroken from texts/white-1876/23.md without the "¶N " prefix, with the file's own quotation marks and apostrophes; long enough to occur only once in the chapter; no two olds may overlap;
- new: the replacement. Use "¶" for a paragraph break inside new. White prints none of Verne's footnotes: restore each one by writing {fn: the note's English} in new, right after the word the French marks; it becomes "(1)" there and the note goes after the paragraph, as the renders set them. Never a tab or a line break inside a field. To replace or delete a whole paragraph of White's (a stray repeat, or a note set as a paragraph), write old as "@¶N" with White's paragraph number; an empty new deletes it.

Finish with a short report (your final message): the number of patches (from the list, new, slips); each listed discord you did not patch, and why; every French phrase you were unsure how to render.
