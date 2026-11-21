# The reviser's prompt for 01950 (from prompts/reviser.md v3, filled; R1121-116)

---

You are revising one chapter of a novel in progress, in the current folder, on verified critic findings: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. Every file is read-only except this one: story/prose/01950-the-float-in-the-bar.md. Run no git commands of any kind. Do not launch agents. Work alone.

Read: story/voice/pov.md; story/voice/white.md, story/voice/names.md, story/voice/spelling.md and story/voice/banned.txt; plan/workflows/drafting/rulings.md (the rules; every line binds you); story/voice/samples/white-I.5.md (the voice); the chapter's outline and notes in its bundle, plan/tasks/task-20261121-11-render-v1/bundle-01950.md (the facts; read them only to place the fixes); and the verified findings with their dispositions, plan/tasks/task-20261121-11-render-v1/findings-v1.md. Read nothing else.

YOUR FIXES, and only these (the findings file gives their sources):
1. (I1, R1121-109) Herbert's cry "Then men have been here!" becomes "Then a ship—!" Pencroff's answer stands.
2. (I2, R1121-110, R1121-65) At the loss, one clause, in the narrator's plain words, before the flash: what was left of the rotten cord gives way, the backwash draws the freed ball off the bar into the gut, and the channel's current carries it toward the islet's point. Then the flash on the islet's rocks, as now.
3. (I3, R1121-115) "upon the rooms which the long days of winter were to finish" becomes "upon the rooms that were still unfinished".
4. (I4, R1121-115) "crossed dry-shod" becomes "crossed dry".
5. (I5, R1121-111) Outside the squall, lengthen the narration toward White's lengths, joining clauses as he does, with semicolons and "and", adding no matter: the median sentence is 11 words and 32% are short, against White's about 18 and about 14%. Above all the first morning (from "On the 1st of June" to Pencroff's talk with Herbert), the walk out over the sands to the float, and the smooth sand of 3 June. Leave the squall's short sentences, the one-line paragraphs, and the dialogue as they are.
6. (I6) Cut "and, besides, it was the truth" (the errand line); keep "it was true, as far as it went" at home.
7. (I7) Pencroff's speech to Herbert: trim his retelling of the sighting to a line, and change or cut his "it sits up like a buoy", since the narrator has the buoy already. Keep his request and his reason for telling no one.
8. (I8) Split two long sentences, every word kept: "…ribbed by the ebb and shining with water; and on the coast side of the gut…", and "…which had been moulded in the glass itself; but the greater part of the seal lay below, toward the sand…".
9. (I9) Make plain the second "telescope": "searched its rocks with his telescope eyes from one end to the other" becomes "searched its rocks from one end to the other".
10. (I10) Cut "ribbed by the ebb" at the smooth sand of 3 June; keep it on 2 June.
11. (I12, R1121-116) In the paragraph beginning "Pencroff might have told the rest then", cut only its last sentence, "That would be a surprise worth the keeping."

Rules:
- Change wording only. Add no fact, object, person, name or event, and move no beat, except the one clause fix 2 asks for, which the author ruled.
- Keep every line of dialogue unless a fix names it.
- Keep every line on the keep list below exactly.
- Keep the chapter inside White's texture, measured with python3 tools/tells.py story/prose/01950-the-float-in-the-bar.md. Do not chop.
- Everything in the rules holds.
- Change the title line's "(draft 1)" to "(draft 2)".
- When done, run python3 tools/tells.py story/prose/01950-the-float-in-the-bar.md --banned story/voice/banned.txt and python3 tools/spelling.py check story/voice/spelling.md story/prose/01950-the-float-in-the-bar.md, and fix any hit in narration. Those two commands are the only ones you may run.

THE KEEP LIST, word for word:
- "The lines took nothing, and the sea took the pair of us."
- "Five of us and the picks, and we'd have had it,"
- "We had it, Pencroff. For an hour."
- "Latin, I think,"
- every line naming the letters (the B, the place where the crust holds fast, the L, the I) and the seal's hidden part toward the sand;
- "Pencroff was bold, but he was a seaman, and he did not go out alone."
- the paragraph of the house on 2 June (shutters closed, the fire), save the fix 3 phrase;
- "They both knew that glass thrown upon those rocks by such a sea was in pieces."

Finish with a short report (your final message): each fix by number and what you did (or why you left it); the word count and the tells.py line, before and after; then an Inventions list of any fact you added that the notes lack (expected: none), one line each.
