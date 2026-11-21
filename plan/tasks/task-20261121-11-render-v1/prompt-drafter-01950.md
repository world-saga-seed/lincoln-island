# The drafter's prompt for 01950 (from prompts/drafter.md v3, filled)

---

You are drafting one chapter of a novel in progress, in the current folder. The novel is Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. This is the inserted chapter, "XIX bis", between Verne's I.19 and I.20. It has no French: you write it from its outline, in Verne's manner and White's English. Every file is read-only except your one output file. Run no git commands of any kind (not even status or log): another session may be editing this folder. Do not launch agents. Work alone.

Read, in this order, and nothing else:
1. story/voice/pov.md (how the chapter is told; where it and the voice sheet differ, it wins); then story/voice/white.md (the voice sheet), story/voice/names.md (White's forms of every name: use these and no others) and story/voice/banned.txt (words the narration never uses);
2. plan/workflows/drafting/rulings.md (the rules of the page; every line binds you);
3. world/false-assumptions.md (what is not true in June 1865);
4. story/voice/samples/white-I.5.md, a whole chapter of White's translation: the voice. Match it; never copy its sentences;
5. your bundle, plan/tasks/task-20261121-11-render-v1/bundle-01950.md: the chapter's outline (the numbered beats: what the page shows) and its notes for drafting, the world's rules, and the facts of the cards it needs, cut to what is known by 31 May 1865. The cards keep the French names; the page uses White's;
6. the draft before it, story/prose/01900-the-facade-the-ladder-and-the-warren.md, read closely for the join: your chapter opens on 1 June, the morning after it ends.
Do not read any other file, and no outline after this chapter. Do not look for White's chapters besides I.5.

Write the chapter as prose into story/prose/01950-the-float-in-the-bar.md, with the title line "# The Float in the Bar (draft 1)". Under it, the chapter's heading as White sets his: "CHAPTER XIX bis." and a summary line in his manner, phrases in capitals set off by dashes. Then the chapter. Every settled beat, in order; the proposal beats too, unless one contradicts a settled beat. The outline's "The find" says whose the float is: that is for you, never for the page. The page never says or hints whose it is, and explains nothing of where it came from beyond what Pencroff and Herbert can see and guess. Length: about 2,500 words, a target, not a cap.

Keep to the texture in the rules: measure with
  python3 tools/tells.py story/prose/01950-the-float-in-the-bar.md --banned story/voice/banned.txt
and fix every banned-word hit that is narration. Running that one command is the only command you may run.

No notes, marks or comments inside the prose file. Where a beat cannot be written without inventing a fact the notes lack, write around it and list it. If the tool refuses the file, do not work around it: put the whole chapter in your final message, headed by its path.

Finish with a short report (your final message):
- the word count and the tells.py line;
- the beats covered; any beat skipped or changed, and why;
- Inventions: the small things you made up (names, objects, staging, sayings), one line each: the fact, its line, the cards it touches. Do not check them yourself; a separate run does;
- the facts you had to leave open;
- the banned-word hits you fixed.
