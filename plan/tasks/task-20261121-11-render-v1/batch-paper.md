# Batch paper: phase 8, v1

## 01900, draft 1

- **Drafter:** a fresh Opus agent, 2026-11-21, 91,127 tokens, 11 tool uses, about 98 seconds. Prompt: `prompt-drafter-01900.md`. One try.
- **The drafter's report**, as given (summarized from its final message; the full text is in the session transcript):
  - 3,007 words. All 48 French paragraphs and the footnote rendered. Banned list: 0 hits.
  - tells.py: `w= 3007 way/k= 0.0 asif/k= 0.3 and/s=0.70 neg/k=12.6 med=22 sd=13.2 short%= 7 long%= 42 button%= 0`. The drafter left the long sentences as Verne's.
  - Unsure renderings, quoted with its choices: "dégauchirent" (trued), "le dessin ogival" (the ogival outline), "courtine" and "saillant" (curtain, salient), "mouffle" (tackle), "tressées au moyen d'un moulinet" (twisted by means of a winch), "curry-jonc" (curry-rush), "se tutoyer" ("thee" and "thou"), "maître Nab" (Master Neb), "au cinquième au-dessus de l'entresol" (kept "entresol"), "Si le marin fut fier de son élève, cela ne peut se dire" (taken literally), "secouru" (relieved), and others.
  - Departures it knew of: the plate captions left out; "se développait" softened to "lay"; the place names from memory of White, unchecked.
- **Mechanical checks (main session):**
  - Banned list 0; links 0 broken; no "-our" form.
  - Texture against the bounds (R1121-94): "and" per sentence 0.70, at the top of White's range; median sentence 22 against about 18; long sentences 42% against about a quarter. Flagged, not forced. White's own XIX, on its paragraphs: and/s 0.68, median 18, long 27%.
  - Names against White's text (R1121-20): "Prospect Heights" (1) is not White's, who has "Prospect Plateau" 60 times and "Prospect Heights" never. Jacamar Wood, Mandible Cape, Claw Cape, Union Bay and Granite House are his.
- **Facts critic** (fresh Sonnet, the phase 5 calibrated prompt, `prompt-critic-facts-01900.md`), 2026-11-21: **0 findings** (added 0, lost 0, changed 0, softened 0). It checked ¶0 to ¶48 and n1: every figure, name, plant list and the force of the precautions and of Cyrus's fear kept. Three choices it judged ordinary English: "not in the least jealous" (n'en était point jaloux), "much easier" (notablement plus facile), "in the circus" (dans les cirques).
  - **Main session's note on the critic:** it did not flag the one departure the drafter itself reported, "se développait" rendered "lay" (¶2), and it passed "Prospect Heights" as matching Grande-Vue (a names question, not its own; caught by the mechanical check, T7). A zero on 3,000 words is held as "nothing found", not "nothing there".

## 01950, draft 1

- **Drafter:** a fresh Opus agent, 2026-11-21, 119,514 tokens, 26 tool uses, about 263 seconds. Prompt: `prompt-drafter-01950.md`. One try.
- **The drafter's report** (summarized; the full text is in the session transcript):
  - About 2,254 words against a 2,500 target. tells.py: `w= 2254 way/k= 0.0 asif/k= 0.0 and/s=0.55 neg/k=10.2 med=11 sd=11.6 short%= 32 long%= 25 button%= 0`.
  - All beats 1 to 7 in order. The settled lines are word for word. The word "neap" is not used. The wait is shown as the evening ebb after dark. The pride is shown, not stated.
  - Inventions: 22 listed (staging, sayings, Pencroff's thoughts, the indoor work of 2 June, the shoes, "The fish have more sense than we have, my boy", Herbert's "Then men have been here!", the turtle-back comparison, "as wet glass flashes in the sun", Spilett's question at home). They go to the invention check (step 9).
  - Left open: why Herbert is on the beach on 1 June; the 3 June pretext; how the float reaches the islet's rocks against an onshore wind; how the ladder is managed.
- **Mechanical checks (main session):**
  - Banned list 0; no contraction in narration; names all White's ("grey" is White's spelling, 10 to 0).
  - No Nemo, Nautilus, MOBILIS or N on the page.
  - Texture (R1121-94): median sentence 11 against about 18; short sentences 32% against about 14%. The squall's short sentences are ruled (R1121-95), but the gap runs through the whole chapter.
  - Key watch: "Then men have been here!" (Herbert) points at people near the island, where K6 must not return "set close by" and K8 leans no.
  - Physics, from the drafter's open list: the outline has the surge throw the float on the islet's rocks (R1121-66, -68), but the wind of 2 June is onshore (gap item 9) and the bar lies on the coast side of the gut, so the islet is to windward.
- **Facts critic, calibration** (R1121-112): 4 of 5 plants caught in a copy of 01900; it missed the lost clause. See `cal/plants-01900.md`. A "lost: 0" from this critic is not trusted.

## 01950, facts critic, calibration

- All 5 plants caught in a copy of 01950, with 2 real weak findings (the mooring's parting not on the page; the path, already ruled R1121-110) and no false finding. See `cal/plants-01950.md`. The clean run on draft 1 is running.

## 02000, draft 1

- **Drafter:** a fresh Opus agent, 2026-11-21, 101,383 tokens, 21 tool uses, about 166 seconds. Prompt: `prompt-drafter-02000.md`. One try.
- **The drafter's report** (summarized; the full text is in the session transcript):
  - 2,750 words (tells.py counts 2,083 of narration). All 68 French paragraphs rendered. Six long sentences split under R1121-108; five knots left where the French runs as one sentence.
  - tells.py: `and/s=0.43 asif/k=1.0 med=19 short%=17 long%=35 button%=13`. The two "as if" are Verne's ("comme s'il", ¶28; "Ne semblait-il pas que", ¶68).
  - Unsure renderings, quoted with its choices: "chandelle"/"bougie" (tallow candles / stearine candles), "égohines" (fox-tail saws, to check), "acérinées" (acerineæ), "quatre cents milliards" (four hundred thousand millions), "olein, margarin and stearin", "boracic acid", "monsieur Cyrus" as "Mr. Smith".
  - Departures it knew of: the plate caption left out; "mont Frankin" (a misprint) given as Mount Franklin; two sentences restructured; Verne's own slips kept (the "arithmetic" progression, the 800 grains, Pencroff's match).
- **Mechanical checks (main session):** banned list 0; names all White's; `lengths.py` aligns 68 to 68, one paragraph low (¶42, ratio 0.79, French 29 words against English 23), for the critic to look at.
- **"and" per sentence 0.43** is under White's lowest chapter (0.47), and the button rate (13%) is high. Both are flagged for the voice critic.

## Spelling, both ways (R1121-113)

`tools/spelling.py check story/voice/spelling.md story/prose/0*.md`, 2026-11-21: 7 wrong forms. 01900 has "fibers" twice, "leveled" and "marvelous" (White 3 to 1). 02000 has "fiber" once and "fibers" twice. 01950 has none. All go to the revision.
