# The reviser's prompt for 01900 (from prompts/reviser.md v3, filled; R1121-116)

---

You are revising one chapter of a novel in progress, in the current folder, on verified critic findings: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. Every file is read-only except this one: story/prose/01900-the-facade-the-ladder-and-the-warren.md. Run no git commands of any kind. Do not launch agents. Work alone.

Read: story/voice/pov.md; story/voice/white.md, story/voice/names.md, story/voice/spelling.md and story/voice/banned.txt; plan/workflows/drafting/rulings.md (the rules; every line binds you); story/voice/samples/white-I.5.md (the voice); the French, texts/fr-1875/19.md (the authority: check every split against it); and the verified findings with their dispositions, plan/tasks/task-20261121-11-render-v1/findings-v1.md. Read nothing else.

YOUR FIXES, and only these (the findings file gives their sources):
1. (N1) Spelling, White's forms: "fibers" (twice) to "fibres", "leveled" to "levelled", "marvelous" to "marvellous".
2. (N2) "Prospect Heights" to "Prospect Plateau".
3. (N4, R1121-108) Split Verne's long sentences toward White's lengths, as White splits them, adding and dropping nothing: the median sentence is 22 words and 42% are long, against White's about 18 and about a quarter. Start with the paragraphs beginning "The facade of Granite House was then to be lighted" and those the tells.py "knot" lines name. Split at a semicolon, a colon or an "and" that joins two main clauses; keep lists whole; keep White's semicolons where they join closely.

Rules:
- Change wording only. Add no fact, object, person, name or event; drop none; move no beat. Every sentence of the French stays rendered, and nothing that is not in it is added (R1121-103). Where you split a sentence, the French decides where its clauses fall.
- Keep every line of dialogue unless a fix names it.
- Keep every line on the keep list below exactly.
- Keep the chapter inside White's texture, measured with python3 tools/tells.py story/prose/01900-the-facade-the-ladder-and-the-warren.md. Do not chop.
- Everything in the rules holds.
- Change the title line's "(draft 1)" to "(draft 2)".
- When done, run python3 tools/tells.py story/prose/01900-the-facade-the-ladder-and-the-warren.md --banned story/voice/banned.txt and python3 tools/spelling.py check story/voice/spelling.md story/prose/01900-the-facade-the-ladder-and-the-warren.md, and fix any hit in narration. Those two commands are the only ones you may run.

Finish with a short report (your final message): each fix by number and what you did (or why you left it); the word count and the tells.py line, before and after; then an Inventions list of any fact you added that the notes lack (expected: none), one line each.
