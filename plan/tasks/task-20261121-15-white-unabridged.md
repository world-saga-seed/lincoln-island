# Task: White made unabridged (R1121-144 to R1121-147), the pilot

- **Objective:** White's translation made whole: each chapter patched by its departures from the French, or rendered whole from the French in White's voice where he departs too far (R1121-144, R1121-145); first a pilot of one patch (I.5) and one re-render (III.14), measured before any more (R1121-147).
- **Context:** the author, 2026-11-21. The measure (R1121-145): the missing share, 1 − (White's words ÷ French words) ÷ 0.885, and discords per 1,000 French words; re-render at 20% or 8. The patch rule (R1121-146). Every chapter passes the critics before it counts as done.
- **Horizon:** widened by the human to the whole book for this phase, at about 17M tokens (R1121-148). The pilot's chapters go to `story/prose/` once they pass the critics (R1121-146).
- **Region:** writes this task and its folder. Reads `texts/fr-1875/`, `texts/white-1876/`, `texts/align/`, `story/voice/`, `plan/workflows/drafting/rulings.md`, the chapters' outlines and notes, and `world/`.
- **Wave:** none.
- **Start hash:** (at the first commit)
- **End hash:** (on close)
- **Status:** Executing: the pilot's patcher and drafter are running.

## Steps

1. **Patch I.5:** a fresh Opus patcher writes `pilot/patches-00500.tsv` from the French, White and `texts/align/05-discords.md`; `apply.py` applies it to White's text (every old text found once) into `pilot/00500-the-last-match-and-the-fire.md`.
2. **Re-render III.14:** a fresh Opus drafter, from `pilot/bundle-05600.md` (built by `build_bundle.py`), into `pilot/05600-the-new-ship-and-the-third-winter.md`.
3. **Mechanical checks:** tells.py with the banned list; spelling.py.
4. **Critics** (fresh Sonnet, the phase 8 prompts pointed at the files): facts and omission on each; voice on the two together.
5. **Measure:** tokens and time per chapter, by step; findings per chapter; the projection to the 60; put to the author.

## Acceptance

1. Each pilot chapter passes the critics (no break left standing) or its faults are listed for the author.
2. The measured cost and the projection are put to the author before any other chapter starts.

## Log

- 2026-11-21 Opened (R1121-144 to R1121-147). The bundle for III.14: 56 cards, 12,570 words. The prompts written.
- 2026-11-21 R1121-148: the human widens the horizon. The controls' checks in. The pilot launched: the I.5 patcher and the III.14 drafter, fresh Opus agents.
- 2026-11-21 I.5 patched: 7 patches from the list, then 12 the patcher found ("new") and one more (P20, the raft moored, not built; added by the main session); P14 reworded on the main session's call ("he could not, or would not, live any longer"). 20 patches apply; banned 0, spelling 0; tells: med 17, sd 11.6, short 20, long 25 (White's own I.5: 17, 11.3, 17, 26). **The lesson:** the phase 3 list holds 7 of at least 20 departures in the chapter with the fewest, so the lists undercount and the patcher must read for departures, not only patch the list. The facts critic runs.
- 2026-11-21 III.14 drafted: 3,570 words (0.94 of the French's 3,803); tells med 20, sd 12.0, short 7, long 35, banned 0, spelling 0. The drafter broke its prompt: it ran a python script (it failed before writing; the same splits then made by hand). Names set to White's on the main session's call (rulings.md): Balloon Harbor, Jetsam Point, Good Luck (White's boat), Mr. Smith for "monsieur Cyrus". **Lesson:** story/voice/names.md covers I.19 and I.20; the whole book needs White's names list first, from texts/white-1876 and the French.
- 2026-11-21 The I.5 facts critic, round 1: 11 more departures where White still stands. So I.5 holds at least 31, against 7 listed. Patcher's third pass running; then the omission critic.
- 2026-11-21 III.14 facts critic: faithful; 4 findings, all the rulings' "Mr. Smith"; 0 standing. The omission critic runs.
- 2026-11-21 III.14 omission critic: 0 losses. III.14 waits only for the voice critic.
- 2026-11-21 The patcher's third pass: P21 to P31 for the critic's 11, and P32 to P46 for 15 more it found; P46 smoothed on the main session's call ("Herbert soon fell asleep."). 46 patches apply. The patched I.5 keeps 2,623 of White's 2,711 words (96.8%) and runs 2,828 words, 0.87 of the French (the measure's 0.885). Four places the patcher judged close enough are left for the critics (¶4, ¶26, ¶43, ¶84). The voice critic (both chapters) and a second facts critic on I.5 run.
- 2026-11-21 The second I.5 facts critic: 12 more, all where White's words stand ("scratching" for rubbing; Neb's hope held out, reversed by White; "je vous en prie"; "Non"; "je ne veux pas"; "chargea"; the bluish flame; into the cone; "fort bien"; Verne's "Ah ! si…"; the one incident; "veillant"). Patched by the main session (P47 to P57, and P36 to "scratching"): 57 patches apply. Round 1 found 11 and round 2 found 12: the tail is long, so a patched chapter needs about three passes of patcher and critic.
- 2026-11-21 Voice critic on the pilot: no standing break (the "&" is Verne's). I.5: White's print slips patched (P58 to P61) and two seams smoothed; 61 patches. III.14: two knots and repeated connectives, weak. I.5's omission critic: 0 losses. A third facts round on I.5 runs, to see whether the tail has ended.
- 2026-11-21 The third facts round on I.5: 3 (lost, extreme, "Poor fellow!"). Two patched (P62, P63); "Poor fellow!" kept as a stylistic addition (R1121-146). The tail: 11, 12, 3. **Both pilot chapters pass** (no break standing) and go to `story/prose/` as final (R1121-146).

## The pilot's measure

| | I.5, patched | III.14, re-rendered |
|---|---|---|
| Departures found | 7 listed; 63 patches in all (7 from the list, 39 from the patcher's own reading and the first facts round, 13 from the second and third facts rounds, 4 White's print slips) | — |
| Rounds to pass | patcher ×3, facts ×3, omission, voice | drafter, facts, omission, voice |
| Tokens (agents) | about 490k (patcher 207k; facts 63k + 63k + about 60k; omission 52k; voice 47k) | 263k (drafter 105k; facts 58k; omission 53k; voice 47k) |
| White's words kept | 2,623 of 2,711 (96.8%) | none (new render) |
| Length against the French | 0.87 | 0.94 |
| Standing findings | taste only | weak: two knots, repeated connectives |

Lessons: (1) the phase 3 lists undercount White's departures by a factor of about eight (7 listed, 59 departures patched), so a patcher must read for departures, not only patch the list; (2) story/voice/names.md covers I.19 and I.20 only, and later names (Balloon Harbor, Jetsam Point, Good Luck, Tabor Island) must come from White's own text; the book needs White's names list first; (3) a drafter broke its one-command rule.
- 2026-11-21 R1121-149 (option A). `chapters.tsv`: 37 to patch, 21 to re-render, 4 done (I.5, I.19, I.20, III.14). `patcher-v2.md` (a full reading against the French), `chap.py` (a chapter's folder, prompts and title; `apply`). The names builder runs (`names/`), for the re-renders. The patches start in book order with I.1, since a patch keeps White's names.

## The loop, per chapter

Patch: patcher v2 (Opus) → apply → facts critic → patcher's second pass on the findings → apply → facts critic 2 → the last findings patched by the main session → omission critic → voice critic by threes → into `story/prose/` as final. Re-render: drafter (Opus, a bundle by `build_bundle.py`, the names list) → facts → omission → voice → final.
- 2026-11-21 I.1: patcher v2, 75 patches (16 listed, 57 new, 2 slips); all apply. Verne's footnotes: `{fn: …}` in a patch becomes "(1)" and a note paragraph after, as 01900 sets them (apply.py; patcher v2 told). "metres" follows White's one "kilometres". Facts critic 1 runs.
- 2026-11-21 I.1 facts critic 1: 2 (one the rulings' "Mr. Smith"; "désert d'eau" patched, P76). Patcher v2 works: the first critic found 1 departure, against 11 in the pilot. Facts critic 2 runs.
- 2026-11-21 I.1 facts critic 2: 3 ("Mr. Smith"; the summary's "LAND AHEAD!" and the pockets' "menus ustensiles", patched P77, P78). The omission critic runs.
- 2026-11-21 I.1 omission: 0 losses. I.1 waits for the voice critic (by threes). I.2's patcher runs.
- 2026-11-21 White's names list for the whole book (`names/names-book.md`, 241 rows, every form found in texts/white-1876 by search; a Sonnet agent, 205k tokens) replaces `story/voice/names.md`, which it extends (the earlier rows recounted; its Safety Island note corrected: White prints both forms in both halves, "the islet" most often). Names White never prints carry a plain-English *(Proposal.)*. I.2: patcher v2, 70 patches; apply.py takes a whole paragraph as "@¶N" (White's stray repeat of ¶23 at ¶25 deleted; his bracketed note ¶48 set as Verne's footnote, corrected to the French); patcher v2 told.
- 2026-11-21 I.2 facts critic 1: 4 (the heading's "Rebellion"; the motto; "disputée"; "Bien"), all patched (P34 corrected, P73 to P75). Facts critic 2 runs.
- 2026-11-21 I.2 facts critic 2: 6 small (the Union; the hurricane's force twice; "hommes" and "en plein ouragan"; "se débattait"; "rafales déchaînées"), all patched (P76 to P81). The omission critic runs.
- 2026-11-21 I.2 omission: 1 ("Ce jour-là"), patched (P82). I.2 waits for the voice critic.
- 2026-11-21 I.6 re-rendered (the first under R1121-149): footnote set as (1); the drafter kept to its one command. Facts critic runs.
- 2026-11-21 I.6 facts critic: 0 findings. The omission critic runs.
- 2026-11-21 I.6 omission: 0 losses. The voice critic for I.1, I.2 and I.6 (`make_voice.py`, by threes).
- 2026-11-21 Voice on I.1, I.2, I.6: no break; the weak findings are Verne's or White's own sentences, untouched. **I.1, I.2 and I.6 final** in story/prose. Quotation marks differ between files (straight in the renders, curly in White): a matter for the build.
- 2026-11-21 I.3: patcher v2, 67 patches (23 listed, 42 new, 2 slips; îlot as "islet" throughout); "pôle austral du monde" set as "the south pole of the heavens" on the main session's call. Facts 1 on I.3 and I.4's patcher run.
- 2026-11-21 I.3 facts 1: 1 ("la partie nord du nouveau continent", P68); facts 2: 3 (the surf's rattle, "devaient penser", "plutonien", P69 to P71). The omission critic runs.
- 2026-11-21 I.3 omission: 0. I.3 waits for voice. I.7's patcher runs.
- 2026-11-21 I.4: patcher v2, 78 patches (18 listed, 56 new, 4 slips); all apply. "the negro Neb" for "le nègre Nab" checked: it is White's own form (his I.2 heading, and 14 times elsewhere). Facts 1 runs.
- 2026-11-21 I.4 facts 1: 4; three patched (the road that walks by itself, with Herbert's echo; "pointe aiguë"; "agréable dans ses aspects"); "amphibious monsters" kept as White's stylistic addition (R1121-146). Facts 2 runs.
- 2026-11-21 I.7: patcher v2, 69 patches (10 listed, 57 new, 2 slips); all apply. The summary's "huit mille" against ¶79's five and ¶81's six miles is Verne's own (rendered as printed). Facts 1 runs.
- 2026-11-21 I.4 facts 2: 2 ("reconnut … à basse mer"; the long fringe of whimsical rocks), patched. The omission critic runs.
- 2026-11-21 I.7 facts 1: 3 ("bois sec", "se laissait faire", "devaient souffrir"), patched. Facts 2 runs.
- 2026-11-21 I.4 omission: 0. I.4 waits for voice. I.8's patcher runs.
- 2026-11-21 I.7 facts 2: 6 small, patched (the ebbing sea; eyes opened again; "par excellence"; the three named; Herbert's question; the cut face). The omission critic runs.
- 2026-11-21 I.7 omission: 1 ("des premières roches, au large du littoral"), patched. The voice critic for I.3, I.4, I.7 runs.
- 2026-11-21 I.8: patcher v2, 67 patches (11 listed, 47 new, 9 slips), and "regardait sans voir" (main session). Facts 1 runs.
- 2026-11-21 Voice on I.3, I.4, I.7: no break; two patch seams mended. **I.3, I.4, I.7 final.** I.8 facts 1: 4 ("rachitiques"; Smith's hallucination; the litter, not a carriage; the cut face), patched. Next: I.8 facts 2, and I.9's patcher.
- 2026-11-21 I.8 facts 2: 5; four patched ("à quoi avait tenu la vie"; "accidents de terrain … se grava"; the cut face; the islet); "nord-nord" (Verne's truncation) left as White's "due north". The omission critic runs.
- 2026-11-21 I.8 omission: 1 ("trois"), patched. I.8 waits for voice.
- 2026-11-21 I.9: patcher v2, 91 patches (15 listed, 63 new, 13 slips); all apply. "maître Pencroff" kept bare, as names.md has it (no "Master" in White). "pin pigeon" read as Verne's slip for the "pin pignon" of his own summary: "pignon pine". Facts 1 runs.
- 2026-11-21 I.9 facts 1: 6; patched: the heading's cabiai, "le tonnerre en personne", Nab named, the tracks of Top. Kept: White's Marquesas and Low Archipelago (names.md), his "water-hog" gloss. **Neb named, book-wide (main session's call under R1121-146, overturnable):** where the French names Nab and White writes "the negro", the render says "Neb"; where the French has "le nègre", White's word stays. Applied to I.2 ("L'esclave, devenu libre": "The slave, once free"), I.7 (three), I.8 (one), I.9 (one); I.2 and I.7 finals rebuilt; patcher-v2 carries the line for the chapters to come. Facts 2 on I.9 runs.
- 2026-11-21 I.9 facts 2: 3; patched "pouvait avoir des conséquences fort graves" and the confidence "en Cyrus Smith"; White's "water-hog" gloss kept (French ¶103 has "espèce de porc"). Author confirmed the Neb rule and the three smaller calls (R1121-150, R1121-151); texts/errata.md started. The omission critic runs.
- 2026-11-21 I.10: patcher v2, 90 patches (23 listed, 63 new, 4 slips); all apply. "pin pignon" set as "pignon pine", as in I.9 (R1121-151). No "the negro" left for Nab. Facts 1 runs.
- 2026-11-21 I.9 omission: 1 ("assez mauvaises"), patched. I.9 waits for voice (with I.8 and I.10). I.11's patcher runs.
- 2026-11-21 I.10 facts 1: 2 (the summary's question; "on s'élevait peu à peu"), patched. Facts 2 runs.
- 2026-11-21 I.10 facts 2: 0; of its set-asides, the four named laughers restored (main session); "to dine" at noon kept (the period's midday dinner). The omission critic runs.
- 2026-11-21 I.10 omission: 0. The voice critic for I.8, I.9, I.10 runs.
- 2026-11-21 Voice on I.8, I.9, I.10: no break; three print slips mended in I.9. **I.8, I.9, I.10 final.**
- 2026-11-21 I.11: patcher v2, 87 patches (16 listed, 60 new, 11 slips); all apply. "Cochalot Point" kept as White's name (names.md, 3 times); "trajopan" mended (White prints "tragopan" twice). Facts 1 on I.11 and I.12's patcher run.
- 2026-11-21 I.11 facts 1: 7; five patched (the telescopes under his brows; "animal"; "s'échancrait"; "cap"; "admise"). Kept: "Cochalot Point" (White's name, R1121-146) and "cue" (White's word, the period's spelling of queue). Facts 2 runs.
- 2026-11-21 I.11 facts 2: 4; three patched ("périmètre", "devait", "déjà reconnue"); "Cochalot" kept (White's form, as before). The omission critic runs.
- 2026-11-21 I.11 omission: 2 ("à mesure", "précis"), patched. I.11 waits for voice.
- 2026-11-21 I.12: patcher v2, 66 patches (21 listed, 40 new, 5 slips); all apply. "maître Pencroff": White's "Professor Pencroff" made plain "Pencroff" (R1121-151); "amandes" as "pine kernels", as in I.9 and I.10. Facts 1 runs.
- 2026-11-21 I.12 facts 1: 4; three patched (the latitude "trop haute", White's error reversed; "smooth" and "constantly" removed). "pine kernels" kept: the "amandes" are the pignon kernels of I.9 and I.10. Facts 2 runs.
- 2026-11-21 I.12 facts 2: 2; "indigène dangereux" patched (White's "savage" an added judgment, R1121-150's measure); "pine kernels" kept again ("amandes" here are the kernels of the pignon pine, I.9 ¶97, I.10). The omission critic runs.
- 2026-11-21 I.12 omission: 2 ("pittoresquement relevé", "tout à fait"), patched. I.12 waits for voice.
- 2026-11-21 I.13: patcher v2, 81 patches (19 listed, 57 new, 5 slips); all apply. Verne's hours in ¶34 and n1 do not agree: rendered as printed, logged in texts/errata.md. Facts 1 on I.13 and the I.14 drafter (render) run.
- 2026-11-21 I.13 facts 1: 3 ("immédiatement utilisable", the fibres' tenacity, "pot-au-feu" as boiled agouti), patched. Facts 2 runs.
- 2026-11-21 I.13 facts 2: 5; four patched (the heading's pottery kiln; the "commencement"; the wind that cast them ashore; "sanctifier"); "THE FIRST BOILED MEAT" kept, agreeing with the body's boiled agouti. The omission critic runs.
- 2026-11-21 I.13 omission: 1 ("un simple pot-au-feu"), patched. I.13 waits for voice.
- 2026-11-21 I.14 rendered (Opus): about 3,220 words against the French's 3,330; tells.py run by the main session (0 banned hits; long% 43, sd 14.7, three knots: for the voice critic). The drafter could not run its one allowed command (the classifier refused it), so render prompts now allow none: chap.py strips the tells line, and footnotes are asked as (1). The footnote's "[1]" set as "(1)". Voice on I.11, I.12, I.13 and facts 1 on I.14 run.
- 2026-11-21 I.14 facts: 0. The omission critic runs.
- 2026-11-21 I.14 omission: 0. I.14 waits for voice. I.15's patcher runs.
- 2026-11-21 Voice on I.11, I.12, I.13: no break; four patch seams mended. **I.11, I.12, I.13 final.**
- 2026-11-21 The author confirmed the five calls of the last report (R1121-152).
- 2026-11-21 I.16: patcher v2, 71 patches (12 listed, 54 new, 5 slips). The summary follows Verne's (White's added "—THE DUGONG" removed, as in the headings patched before). Facts 1 runs.
- 2026-11-21 I.15: patcher v2, 74 patches (30 for the 26 listed, 43 new, 1 slip); all apply. "koula" restored for White's "ai" (Verne's name for the beast, glossed as the sloth in the same sentence); the clay gloss removed as an added fact. Facts 1 runs.
- 2026-11-21 I.16 facts 1: 3 ("du large", "veiller", "s'échouer sur une petite grève"), patched. Facts 2 runs.
- 2026-11-21 I.15 facts 1: 7; six patched ("le lendemain", "mauvaise saison", the added "magnetic ore", the charcoal-burner's wood, the tool list, iron and steel); "Low Archipelago" kept (White's name). Facts 2 runs.
- 2026-11-21 I.16 facts 2: 7 small, all patched ("considérable"; the reporter's statement; "devait laisser à désirer"; "quêtant"; "l'énorme animal"; "devait peser"; "personne n'eût pu le dire"). The omission critic runs.
- 2026-11-21 I.15 facts 2: 1 ("Low Archipelago": White's name, kept). The omission critic runs.
- 2026-11-21 I.15 omission: 0. I.16 omission: 3 ("en réalité", "en cet endroit", "en somme"), patched. The voice critic for I.14, I.15, I.16 and I.17's patcher run.
- 2026-11-21 Voice on I.14, I.15, I.16: no break; two long sentences of the render split. **I.14, I.15, I.16 final.**
- 2026-11-21 I.17: patcher v2, 69 patches (20 carrying all 25 listed, 42 new, 7 slips). Facts 1 runs.
- 2026-11-21 I.17 facts 1: 8, all patched ("le courant indicateur"; "n'insistons pas"; "rive"; "acharnement"; varechs and goëmons; "en fin de compte"; the waterfall White added; "le but final"). Facts 2 runs.
- 2026-11-21 I.18: patcher v2, 73 patches (15 listed, 52 new, 6 slips); all apply; Nab named (R1121-150); White's "pulp" read as "poulp". Facts 1 runs.
- 2026-11-21 I.18 facts 1: 2 ("assez approximativement", "romane"), patched. Facts 2 runs.
- 2026-11-21 I.17 facts 2: 3, patched ("ce granit"; "le but à atteindre" as its own sentence; "cadre" as frame, three times). The omission critic runs.
- 2026-11-21 I.18 facts 2: 3 ("faite au lac", "c'est-à-dire", "plus frais"), patched. The omission critic runs.
- 2026-11-21 I.17 omission: 1 ("ensuite"); I.18 omission: 1 ("C'est ce qui fut fait"); both patched. Voice on I.17, I.18 (a batch of two) and I.21's patcher run.
- 2026-11-21 Voice on I.17, I.18: no break; one restored sentence split. **I.17, I.18 final.** Part I wants only I.21 and I.22.
- 2026-11-21 I.21: patcher v2, 69 patches (13 listed, 47 new, 9 slips), and Herbert's Atlantis made a statement again (main session); all apply. Facts 1 runs.
- 2026-11-21 I.21 facts 1: 8, all patched ("bien employée", "conifères", the added "majestically", "milliards de milliards", "infusoires du corail", "animaux microscopiques", "des Colombs", "le secret de Dieu"). Facts 2 runs.
- 2026-11-21 I.22: patcher v2, 92 patches (22 listed, 62 new, 8 slips); all apply. "amandes de pin-pignon" as "pine kernels" (R1121-152). Facts 1 runs.
- 2026-11-21 I.21 facts 2: 4, patched ("infusoires", "astre", the added "from its changes", "ressusciter"). The omission critic runs.
- 2026-11-21 I.21 omission: 0. I.21 waits for voice (with I.22). II.1's patcher runs.
- 2026-11-21 I.22 facts 1: 9; seven patched (culpeux; "à revers"; "féliens"; the lid; "en quelque point"; "désir"; "pas seulement trois mois"). Kept: White's "tajassans" and "dragon-tree wine" (his forms). Facts 2 runs.
- 2026-11-21 I.22 facts 2: 1 ("tajassans", White's form, kept). The omission critic runs. II.1's patcher failed on a login timeout (it left a patch file of unknown completeness; set aside as patches-02300.partial.tsv) and is relaunched.
- 2026-11-21 I.22 omission: 0. Voice on I.21, I.22 runs.
- 2026-11-21 Voice on I.21, I.22: no break; one seam split; headings XVII and XXI given their full stop in the finals. **I.21, I.22 final: Part I complete (22 chapters).**
- 2026-11-21 I.21, I.22 calls confirmed by the author (R1121-153). II.1: patcher v2 (retry), 70 patches (17 listed, 46 new, 5 slips), all apply; "grain de plomb" as "pellet" throughout, to agree with I.22's "leaden pellet" (H5) (main session; White has "bullet"). Facts 1 runs.
- 2026-11-21 II.1 facts 1: 9, all patched ("Puis :"; "trop directement"; "au plus"; "à plusieurs reprises"; "avec leur adhérence"; "Je ne dis pas non"; "des chélonées"; "bien embarrassé"; the future perfect of conjecture). Facts 2 runs.
- 2026-11-21 II.1 facts 2: 6, patched ("ouragan"; the natives of New Zealand; "légère fumée", White's "thin film"; Nab's general remark; "sur le sable"; "maladroits"). The omission critic runs.
- 2026-11-21 II.1 omission: 0. II.1 waits for voice. II.3 (render) is drafted.
- 2026-11-21 II.2: patcher v2, 79 patches (24 listed, 48 new, 7 slips); all apply; "bullet" made "pellet" (the patcher began before the line was in patcher-v2). Verne's "comme un nègre" restored under R1121-150. Facts 1 runs.
- 2026-11-21 II.2 facts 1: 6, patched (the added "low"; this part of the domain; "provenance"; "pas admissible"; "paraissait … feuilleté"; "plusieurs planisphères"). Facts 2 runs.
- 2026-11-21 II.3 rendered (Opus): 3,430 words against the French's 3,576; tells.py: 0 banned hits, long% 42, five knots (for voice). Facts runs.
- 2026-11-21 II.2 facts 2: 4, patched ("la côte"; "l'épave" as jetsam, not prize; "J'espère bien que non"; the added "pocket"). The omission critic runs.
- 2026-11-21 II.3 facts: 0. The omission critic on II.2 and II.3 run.
- 2026-11-21 II.3 omission: 0. II.3 waits for voice. II.4 (render) is drafted.
- 2026-11-21 II.2 omission: 3 ("assez bien", "en somme", "maintenant"), patched. II.2 waits for voice.
- 2026-11-21 Voice on II.1, II.2, II.3 runs.
- 2026-11-21 II.4 rendered (Opus): 3,213 words against the French's 3,430; tells.py: 0 banned hits, but long% 45, neg/k 17.2 and 15 knots, the most of any render (for voice, which may split at the joins under R1121-108); "dut donc être très-étonné" made a conjecture again (main session). Facts runs.
- 2026-11-21 Voice on II.1, II.2, II.3: no break; three seams in II.2 and four lines of the render mended. **II.1, II.2, II.3 final.** II.4 facts: 0; its omission critic and II.5's patcher run.
- 2026-11-21 II.4 omission: 0. II.4 waits for voice. II.6's patcher runs.
- 2026-11-21 II.5: patcher v2, 93 patches (21 listed, 68 new, 4 slips); all apply. Checked against plan/reread-hooks.md: P90 brings H16 to the French ("hantée par un être surnaturel"), P92-P93 bring H9 to it ("Il n'y avait plus d'échelle."); no clue line lost. Facts 1 runs.
- 2026-11-21 II.6: patcher v2, 82 patches (14 listed, 57 new, 11 slips); all apply. The patcher broke its no-command rule (one shell call: a heredoc to write its file and a read-only python check of the olds); logged, and its output kept, since apply.py rebuilds from White and checks every old. 28.6 "le brave nègre", White's "the brave fellow": restored as "the brave negro" under R1121-150 (Verne's own word kept, White's softening undone). Facts 1 runs.
- 2026-11-21 II.5 facts 1: 2 ("évasion", "ne pouvaient l'être"), patched. Facts 2 runs.
- 2026-11-21 II.6 facts 1: 5; four patched ("macaque" twice, White's "macauco" a lemur; the added "trained"; "Il paraît jeune"). Open, put to the author: Pencroff's "ce moricaud" (¶93, said of the orang), White's "this black ape"; kept as White's until ruled. Facts 2 runs.
- 2026-11-21 II.5 facts 2: 3, patched ("avec l'aide du temps"; "une fortune"; "habitude professionnelle"). The omission critic runs.
- 2026-11-21 II.5 omission: 2 ("de l'extrémité de la presqu'île"; the cloth, ropes and cordage), patched. II.5 waits for voice. II.7's patcher runs.
- 2026-11-21 II.6 facts 2: 6; five patched (the Chimneys and the day; down the bank at full speed; "ils virent que"; "comme tel"; "boire le vin"); "moricaud" waits for the author. The omission critic runs.
- 2026-11-21 II.6 omission: 2 ("rapidement", "On sait que"), patched. II.6 waits for "moricaud" and voice.
- 2026-11-21 Voice on II.4, II.5, II.6 runs (the "moricaud" line may change after it, by the author's ruling).
- 2026-11-21 II.7: patcher v2, 72 patches (13 listed, 55 new, 4 slips), and three by the main session ("indiginous", "unwieldly" as slips; "la première quinzaine de décembre" as the first half, not White's middle); all apply. 29.12 "onaggas": White's "onagers" kept, as his word for the beast (24 times in his text); for the author's next report. Facts 1 runs.
- 2026-11-21 Voice on II.4, II.5, II.6: no break; three splits in the render, one seam in II.5. **II.4, II.5 final.** II.6 waits for the "moricaud" ruling.
- 2026-11-21 II.7 facts 1: 5; three patched ("les volatiles" without White's quoted "chickens"; "renvoyée"; the added "canal"). Onaggas (the heading and ¶54, and White's "onagers" book-wide) put to the author. Facts 2 runs.
- 2026-11-21 R1121-154: onaggas everywhere. "Moricaud" is with the human. patcher-v2 and the render prompts carry the onagga line; II.8 (rendering now) is checked for it on its return.
- 2026-11-21 II.7 facts 2: 8, all patched; onaggas throughout the chapter and its heading (R1121-154); "traînait des charges"; "esprit pratique"; the engineer had the stable built; the echoes; "rassurante pour l'alimentation". The omission critic runs.
- 2026-11-21 II.7 omission: 1 ("définitivement"), patched. II.7 waits for voice.
- 2026-11-21 II.8: rendered (Opus, no command); 3,531 words against the French 3,604; 0 banned; "onagas" made "onaggas" (R1121-154); three knots split at voice-sheet seams by the main session; the plate captions left out, as in every final. Facts 1 runs.
- 2026-11-21 II.8 facts 1: 1 ("charbon" ¶14, coal or charcoal); left as "coal", White's own reading, since the word is ambiguous and the colonists have coal from Part I. Facts 2 runs.
- 2026-11-21 II.8 facts 2: 0. The omission critic runs.
- 2026-11-21 II.8 omission: 0. II.8 waits for voice, with II.7 and II.9.
- 2026-11-21 II.9: rendered (Opus, no command); 3,578 words against the French 3,840; 0 banned. The main session put White's "elevator" for "ascenseur" (White XXXI ¶15-¶25) and his "Tabor Island" (names.md) in the title, and split two knots. Plate captions left out.
- 2026-11-21 II.9 facts 1: 0. Facts 2 runs.
- 2026-11-21 II.9 facts 2: 0. The omission critic runs.
- 2026-11-21 II.9 omission: 0. Voice on II.7, II.8, II.9 runs.
- 2026-11-21 II.10: rendered (Opus, no command); 3,389 words against the French 3,660; 0 banned. The main session dropped Verne's n1 ("Champ des baleines"), which glosses his English "whale-field" for French readers and says nothing in English *(Resolved by judgment, overturnable.)*; n2 renumbered (1), and its Vineyard-in-New-York put in the errata; two knots split. Facts 1 runs.
- 2026-11-21 II.10 facts 1: 1, the dropped n1, which is the main session's own call above (left; for the author's next report). Facts 2 runs.
- 2026-11-21 II.10 facts 2: 1, the dropped n1 again; left, for the author. The omission critic runs.
- 2026-11-21 II.10 omission: 2; "maître Pencroff" is plain Pencroff (R1121-151), and n1 is the main session's call; nothing patched. II.10 waits for voice.
- 2026-11-21 Voice on II.7, II.8, II.9: no break; renders and one seam mended (voice/findings-29-30-31.md). **II.7, II.8, II.9 final.**
- 2026-11-21 II.11: rendered; 3,840 words against 4,006; 0 banned; "lift" made White's "elevator" (the render prompt now says so). II.12: rendered; 4,356 against 4,683; 0 banned; "lift" made "elevator"; ln3 (the bottle's document, French in the French edition) given in English, as II.13 ¶6 says it is English *(Resolved by judgment, overturnable.)*. The boat's name (Verne's "Bonadventure", Pencroff's baptismal name; White's "Good Luck") put to the author; II.12 waits for it. Facts 1 runs on both.
- 2026-11-21 R1121-155: the Bonadventure everywhere; names.md, patcher-v2 and the render prompts carry it; II.12 made so (8 names). Drift logged in plan/state.md: the pilot final 05600 has "Good Luck" once; not edited. II.11 facts 1: 3; "SMITH ALONE" (White's form) in the heading, "éléments constitutifs" made "constituent"; White's "Bennett" kept as his form of the name. II.12 facts 1: 8, all the boat's name, already met by R1121-155. Facts 2 runs on both.
