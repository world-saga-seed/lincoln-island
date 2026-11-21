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

## 01950, facts critic, clean run

A fresh Sonnet agent, `prompt-critic-facts-01950.md`, 2026-11-21, 106,401 tokens. **0 breaks, 2 weak, 2 taste.** All four quotes resolve (checked by grep).
1. Weak: the path and the mooring's parting are not on the page ("Where the bar had been there was only broken water, and the flood ran over it.", l.127). **Disposition:** fix, by R1121-110, with the cord giving way (R1121-65).
2. Weak: "Then men have been here!" (l.39) against K5, K6 and R1121-100. **Disposition:** fix, by R1121-109.
3. Taste: "upon the rooms which the long days of winter were to finish" (l.47), a forward glance against R1121-91. **Disposition:** fix, to "upon the rooms that were still unfinished" (R1121-115).
4. Taste: "the sands they had crossed dry-shod an hour before" (l.117), when they are barefoot (gap item 13). **Disposition:** fix, to "dry" (R1121-115).
Its other checks were all clear: dates, tides, wind, names, the float's look and letters, the tools, the shoes, the pretext, the joke, the cast at home, the two settled lines, and the unspoken sum.

## 02000, facts critic

A fresh Sonnet agent, `prompt-critic-facts-02000.md`, 2026-11-21, 57,837 tokens. **1 finding**, both quotes resolving:
- ¶31, changed: "gave them an acid drink" for "leur donnaient une boisson acidulée" (acidulated, slightly acid). **Disposition:** fix ("an acidulated drink").
It checked every figure in the wheat arithmetic, the seals, the fat, the bridges and the dates. It judged "monsieur Cyrus" as "Mr. Smith" ordinary (R1121-96). Calibrated on 01900 (4 of 5, weak on losses); the omission critic covers losses.

## 01900, omission critic

Calibrated 5 of 5 (`cal/plants-01900-lost.md`). The clean run is running.
- Clean run (fresh Sonnet, `prompt-critic-omission-01900.md`, 52,457 tokens): **No losses.** It went through ¶1 to ¶48 sentence by sentence, the dialogue and n1. One borderline case it did not count: "assez semblables à leurs congénères d'Europe" as "much like their European fellows" (¶41).
- 02000, omission critic, clean run (fresh Sonnet, `prompt-critic-omission-02000.md`, 49,953 tokens): **No losses** in ¶0 to ¶68, with the qualifications and every figure checked.

## The voice critic

- Calibrated on a copy of 01950 with six planted faults: 6 of 6 caught (`cal/plants-01950-voice.md`).
- The batch run (fresh Sonnet, `prompt-critic-voice.md`, 87,124 tokens): 9 findings (5 weak, 4 taste), merged with the calibration run's real findings into `findings-v1.md`.

## The revision

### 01900, draft 2

- **Reviser:** a fresh Opus agent, `prompt-reviser-01900.md`, 2026-11-21, 81,540 tokens. Fixes N1, N2, N4 made: four spellings, Prospect Plateau, about 30 splits checked against the French. Inventions: none.
- **The main session's re-check:**
  - It restored one connective the reviser reported dropping: Verne's "car" at ¶22, given back as ", for the distance from Lincoln Island", the draft 1 wording.
  - tells.py: `and/s=0.49 med=18 sd=11.2 short%=8 long%=29` (draft 1: 0.70, 22, 13.2, 7, 42). The median and the long share now sit at White's.
  - Banned 0; spelling.py 0; Prospect Heights 0; lengths.py 48 to 48; every line of dialogue identical to the snapshot.
  - The prompt named a keep list "below" and gave none for the neighbours. The reviser reported it; no line was cut, so nothing was lost. The omission critic runs again on draft 2.
- **Omission re-check on draft 2** (fresh Sonnet, the same prompt), 2026-11-21: **No losses** in ¶1 to ¶48, with the qualifications, figures, names and n1 checked.

### 01950, draft 2

- **Reviser:** a fresh Opus agent, `prompt-reviser-01950.md`, 2026-11-21, 108,309 tokens. All eleven fixes were made. Its only invention is the ruled clause of fix 2: "At last what was left of the rotten cord gave way; the backwash drew the freed ball off the bar into the gut, and the current of the channel carried it toward the point of the islet."
- tells.py, draft 1 to draft 2: `and/s` 0.55 to 0.66, `med` 11 to 16, `short%` 32 to 28, `long%` 25 to 31. The short sentences left are dialogue, the one-line paragraphs and the squall.
- **The main session's re-check:**
  - Every keep-list line is word for word.
  - Each fixed phrase is gone ("men have been here", "telescope eyes", "surprise worth the keeping", "dry-shod", "besides, it was the truth", "were to finish"), and each new one is present.
  - There is no Nemo, Nautilus, MOBILIS or N, no contraction in narration, and spelling.py and the banned list are both 0.
- **One join to watch:** under fix 5 the reviser joined "He did not." into "…by the fire, but he did not." That plain one-line beat was R1121-95's kind of sentence. It is put to the author.

### 02000, draft 2

- **Reviser:** a fresh Opus agent, `prompt-reviser-02000.md`, 2026-11-21, 62,500 tokens. Fixes: three spellings, "an acidulated drink", and four knots split at semicolons joining main clauses, each where the French has ";" or ", et". Inventions: none.
- **The main session's re-check:**
  - spelling.py 0; banned 0; lengths.py 68 to 68 (¶42 low, as in draft 1); every line of dialogue identical to the snapshot.
  - tells.py: `and/s` 0.43 to 0.42, `long%` 35 to 31, knots 5 to 1.
  - **Omission re-check on draft 2** (fresh Sonnet), 2026-11-21: **No losses** in ¶1 to ¶68.

## Triplets (R1121-117)

`triplets.py` counts series of three short items (one to four words each, the last two joined by and/or) in the narration, against the aligned French. A series the French paragraph also has is Verne's list; one beyond the French count is for rhythm, or the render's own. Speech is left out.

| Text | Narration words | Series not in the French | Per 1,000 |
|---|---|---|---|
| White XIX | 2,154 | 1 ("Neb was courage, zeal, and self-denial in person") | 0.46 |
| White XX | 1,598 | 1 real ("This spot was cleared, weeded, and even dug"), plus 1 false match ("somehow or other") | 0.63 |
| 01900 draft 2 | 2,945 | 0 | 0.00 |
| 02000 draft 2 | 2,053 | 1 ("The spot was cleared, carefully weeded, and even dug over"), but it is the French's: "nettoyé, sarclé avec soin, fouillé même" (¶67), with no "et", which the matcher misses | 0.00 |
| 01950 draft 2 (no French; against White's rate) | 2,275 | 1 ("dead and empty", within "a crust of grey-white shells, dead and empty") | 0.44 |

**Result:** none of ours runs over White's rate. The one in 02000 is Verne's. 01950's 0.44 is at White's XIX rate, and its one series is the settled detail of the shells (gap item 4). **No flags.**
- **Facts re-check on 01950 draft 2** (fresh Sonnet), 2026-11-21: 1 weak finding, and its quote resolves. "upon the rooms that were still unfinished" (l.47) strains 01900, "the partitions were finished. Nothing remained but to furnish the rooms, which would be the work of the long days of winter." **The wording was the main session's own** (sent as the corrected pick for I3 and ruled in R1121-115), so the error is ours, not the reviser's. Put to the author. Everything else checks, including the new path clause and no held fact.
- **Two edits by the main session (R1121-118):** "upon the furnishing of the rooms", and "He did not." restored as its own sentence. Re-check: banned 0, spelling 0, tells.py `and/s=0.66 med=16`.

## The seams (BRIEF phase 8)

A fresh Sonnet critic, `prompt-critic-seams.md`, 2026-11-21: **0 breaks, 2 weak, 1 taste.** Both seams join cleanly, and nothing in 01950 is presented as new by I.20.
1. Weak: "on the coast side of the gut, where the current still ran deep and fast" (01950 l.55), against Verne's knee-deep ford at the lowest ebb (I.15 ¶15) and the ford of 5 June (I.20 ¶20). Put to the author.
2. Weak: 3 June "grey and still" (01950 l.139) against I.20 ¶1, June's "averses et des rafales qui se succédèrent sans relâche". Put to the author.
3. Taste: "took off their shoes, which were nearly worn through" (01950 l.51) against I.20 ¶3, the clothes "chauds et solides", to be replaced "bientôt". Put to the author.

## The blind probe

See `probe/score.md`: no leaks; 11 of 15 key questions as meant; K3 (the point) and K2 half-missed; K4 thin.

## 01950, draft 2, after the probe and the seams (R1121-119)

Four edits by the main session; two findings left as they stand:
- "The hour of low water went by in this way." added after "for a while even Pencroff forgot to watch the water." (K3: the hour is on the page before Herbert names it).
- "something flashed, once, and flew apart." (K4).
- "where the current still ran fast" (seams 1).
- "which were much worn" (seams 3).
- Left: the tools' reason (K2, stated at l.49), and the still 3 June (seams 2).
- **Facts re-check on the edited 01950** (fresh Sonnet), 2026-11-21: 1 weak finding. It held "something flashed, once, and flew apart." against the outline's "a flash in the spray, and it is gone" and the POV file's "No one sees it break up close". **Disposition:** the draft stands. R1121-68 itself says "The two see the float break", and the author ruled "flew apart" (R1121-119). The outline's and the POV file's wording lagged the ruling, and both are now brought up to it. This was a notes fix, not a prose fix.
- **Probe re-ask:** K3 and K4 now as meant (see `probe/score.md`).

## The invention check (01950)

A fresh Sonnet agent, `prompt-invention-check.md`, on `inventions.md` (22 rows), 2026-11-21: **19 stand, 3 reword, 0 break, 0 to the writer.**
- Row 9, reword: "the hooks came up as clean as they had gone down" can read as the bait gone, against the joke that the fish "keep indoors". Fix: "with their bait untouched".
- Row 14, reword: "he had seen him make a lens of two watch glasses". By the lens card (I.10), Smith made it away from the camp ("mais j'en ai fait une"). Fix: "he had seen the lens he made of two watch glasses".
- Row 16, reword: "The stalks have rotted away, and only the shells are left." A goose barnacle holds by its stalk, so with the stalks gone the crust would fall away, yet the page keeps the shells "packed" on the ball. **This touches settled gap item 4** ("a grey-white crust of dead shells, the stalks long gone", R1121-80), so it goes to the author.
All three are prose changes, and the author asked to see any before it is made.
- **Applied (R1121-120):** "with their bait untouched"; "he had seen the lens he made of two watch glasses"; and the barnacles as two kinds. Herbert now says: "Barnacles," then "And look here, among them: these are goose barnacles." His next line has "these few are of another kind, that hang by a stalk" and ends "nothing left but the shells, and a stump of the stalk, dried hard among the others." Gap item 4 and the outline are amended to match, and the bundles rebuilt. Re-check: banned 0, spelling 0, links 0. The clue (the barnacles; Herbert's "long in the sea, from far off") is kept word for word.

## The fold-back

Two fresh Opus agents, run together (their write sets did not overlap): `prompt-fold-back-neighbours.md` and `prompt-fold-back-01950.md`, 2026-11-21.
- **01900:** three lines of the draft's terms and name forms folded into the notes. Next pass: 2 drift ("lay" for "se développait", ¶2; Cyrus's own fear, "n'être jamais secouru", given as "they would never be relieved", ¶22) and 1 voice (the ¶29 idiom).
- **02000:** four lines folded into the notes; the "mont Frankin" flag answered; the outline's "Prospect Heights" corrected. Next pass: 1 drift ("vest" for "veste"; White has "waistcoat").
- **01950:** the 22 inventions folded into the beats as proposals from the draft (21 lines), with two lore lines in the notes, and the R1121-109 line added to the outline. Next pass: 2 voice.
- **The main session's check:** every Next pass quote resolves (3/3, 2/2, 1/1); links 0 broken; every added line is marked. It fixed the 01950 notes' names line ("Granite House", the islet) against `story/voice/names.md`, marked the 01900 seam line it found unmarked *(Proposal.)*, and marked R1121-109 and -115 applied.
- **Length:** 01950 runs 2,719 words (`wc -w`) against about 2,500, a target. 01900 runs 3,274 and 02000 2,750.
