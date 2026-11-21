# The drafter's prompt for 01900 (from prompts/drafter.md v3, filled)

---

You are drafting one chapter of a novel in progress, in the current folder. The novel is Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) in English, in the voice of Stephen W. White's translation (1876). This chapter is Verne's own chapter I.19, rendered anew from the French. Every file is read-only except your one output file. Run no git commands of any kind (not even status or log): another session may be editing this folder. Do not launch agents. Work alone.

Read, in this order, and nothing else:
1. story/voice/pov.md (how the chapter is told; where it and the voice sheet differ, it wins); then story/voice/white.md (the voice sheet) and story/voice/banned.txt (words the narration never uses);
2. plan/workflows/drafting/rulings.md (the rules of the page; every line binds you);
3. world/false-assumptions.md (what is not true in June 1865);
4. story/voice/samples/white-I.5.md, a whole chapter of White's translation: the voice. Match it; never copy its sentences;
5. your bundle, plan/tasks/task-20261121-11-render-v1/bundle-01900.md. It holds Verne's French of the chapter (paragraph-numbered; render every paragraph, including the footnote), the chapter's outline and notes, and the facts of the cards that cite this chapter, each with its French quote. The French is the authority; where a card and the French differ, follow the French.
Do not read any other file. Do not look for White's own version of this chapter, nor any other chapter of his besides I.5.

Write the chapter as prose into story/prose/01900-the-facade-the-ladder-and-the-warren.md, with the title line "# The Facade, the Ladder and the Warren (draft 1)". Under it, the chapter's heading as White sets his: "CHAPTER XIX." and a summary line in his manner, phrases in capitals set off by dashes, drawn from Verne's own summary at the head of the French. Then the chapter.

Render every sentence of the French and nothing that is not in it: do not add, explain, soften, sum up or leave out. Where Verne is technical, be technical as he is; where he gives a figure, give it as he does. Render the footnote as a footnote at the paragraph's end, marked as the French marks it. Use White's forms of the names (Herbert, Neb, Gideon Spilett, the Granite House) and White's American spelling. Length: as long as the French requires (it runs about 3,100 words of French).

Keep to the texture in the rules: measure with
  python3 tools/tells.py story/prose/01900-the-facade-the-ladder-and-the-warren.md --banned story/voice/banned.txt
and fix every banned-word hit that is narration. Running that one command is the only command you may run.

No notes, marks, paragraph numbers or comments inside the prose file. If the tool refuses the file, do not work around it: put the whole chapter in your final message, headed by its path.

Finish with a short report (your final message):
- the word count and the tells.py line;
- every French word or sentence you were unsure how to render, quoted, with what you chose and why;
- any place where you knew you departed from the French, quoted;
- the banned-word hits you fixed.
