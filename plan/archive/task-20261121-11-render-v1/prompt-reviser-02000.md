# The reviser's prompt for 02000 (from prompts/reviser.md v3, filled; R1121-116)

---

You are revising one chapter of a novel in progress, in the current folder, on verified critic findings: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. Every file is read-only except this one: story/prose/02000-candles-and-the-grain-of-wheat.md. Run no git commands of any kind. Do not launch agents. Work alone.

Read: story/voice/pov.md; story/voice/white.md, story/voice/names.md, story/voice/spelling.md and story/voice/banned.txt; plan/workflows/drafting/rulings.md (the rules; every line binds you); story/voice/samples/white-I.5.md (the voice); the French, texts/fr-1875/20.md (the authority: check every change against it); and the verified findings with their dispositions, plan/tasks/task-20261121-11-render-v1/findings-v1.md. Read nothing else.

YOUR FIXES, and only these (the findings file gives their sources):
1. (N1) Spelling, White's forms: "fiber" to "fibre", "fibers" (twice) to "fibres".
2. (N3) "gave them an acid drink" becomes "gave them an acidulated drink" (Verne's "une boisson acidulée").
3. (N5) Leave the sentence lengths as they are: the earlier splits were ruled, and the chapter is near White's range. Split only a tells.py "knot" that runs two main clauses through a semicolon.

Rules:
- Change wording only. Add no fact, object, person, name or event; drop none; move no beat. Every sentence of the French stays rendered, and nothing that is not in it is added (R1121-103). Where you split a sentence, the French decides where its clauses fall.
- Keep every line of dialogue unless a fix names it.
- Keep every line on the keep list below exactly.
- Keep the chapter inside White's texture, measured with python3 tools/tells.py story/prose/02000-candles-and-the-grain-of-wheat.md. Do not chop.
- Everything in the rules holds.
- Change the title line's "(draft 1)" to "(draft 2)".
- When done, run python3 tools/tells.py story/prose/02000-candles-and-the-grain-of-wheat.md --banned story/voice/banned.txt and python3 tools/spelling.py check story/voice/spelling.md story/prose/02000-candles-and-the-grain-of-wheat.md, and fix any hit in narration. Those two commands are the only ones you may run.

Finish with a short report (your final message): each fix by number and what you did (or why you left it); the word count and the tells.py line, before and after; then an Inventions list of any fact you added that the notes lack (expected: none), one line each.
