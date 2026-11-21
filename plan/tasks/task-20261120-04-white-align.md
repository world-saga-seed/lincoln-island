# Task: phase 3, White aligned to the French

- **Objective:** White's 1876 translation aligned to the French by paragraph, and every place White departs (a cut, a condensation, an addition, a changed fact, a softened line) listed as a discord beat citing the French paragraph.
- **Context:** `BRIEF.md` phase 3; R1120-29, R1120-33, R1120-41 (the labellers also note slips in the phase 2 outlines).
- **Region:** writes `texts/align/` (the aligner's beads and the side-by-side files), the discord lists, `texts/align/NN-discords.md` (R1120-43), and this task's folder. Reads `texts/fr-1875/`, `texts/white-1876/`, `story/outline/`.
- **Wave:** none.
- **Start hash:** fdb14c1, 2026-11-20.
- **End hash:** (on close)
- **Status:** Running: four chapters a labeller, two at a time, cap 4.5 M (R1120-42).

## Steps

1. **Align** (script): `texts/align_white.py all` writes `texts/align/NN.tsv`, the beads; `texts/side_white.py all` writes `texts/align/NN-side.md`, each bead with both texts. The beads are hints; the labeller corrects them.
2. **Pilot:** two Sonnet labellers, A on I.1 and II.17, B on III.16. Measure; project to 62; put the cost and the place for the discord lists to the author.
3. **Run** the rest, two agents at a time, in contiguous spans.
4. **Check:** `check_white.py`: every discord cites a French paragraph; every French quote resolves in its chapter and every White quote in White's; every bullet is marked. Then a finder samples discords against both texts (the brief's check).
5. **Close:** the discord list summed (counts by kind, by chapter); the outline slips folded back; commit.

## Acceptance

1. 62 discord lists; every discord cites a French paragraph and quotes the French and White (or marks White's silence).
2. Every quote resolves by script.
3. The finder's sample and its findings are logged.
4. The token rows are in `plan/records/tokens.md`.

## Log

- 2026-11-20 Opened. The aligner: monotone dynamic programming over beads (1-1, n-1, 1-n to 5, 1-0, 0-1), scored on length against the chapter's ratio and on shared anchors (figures, names with White's spellings mapped, number words). White's III.20 ends with a glossary of 92 entries after "THE END." (White ¶54 to ¶145), the edition's own; it is not aligned, and stands as one addition. On I.1 the beads were read by eye and are right; White condenses inside paragraphs more than it cuts whole ones (White ¶19 drops "Dès le début de cette journée du 24 mars", I.1 ¶21). With the skip cost at 1.6 the aligner proposes 7 whole cuts and 1 addition over the book, 55 short beads and 18 long; two cuts checked by eye were condensations (II.5 ¶41 is White ¶33's "enumerated many species").
- 2026-11-20 The pilot. A (I.1, II.17): 104,506 tokens, 14 calls, 2.7 min; 16 and 24 discords, 3 outline slips in 00100. B (III.16): 72,791 tokens, 6 calls, 1.4 min; 30 discords, no slips. No bead needed correcting. `check_white.py` passes all three lists (widened to take footnote cites, "III.16 ¶34 n1", and paragraph lists). White departs often and on facts: II.17 has 1854 printed 1861, Grant's 1852 printed 1832, "plus de quatre-vingts têtes" printed "twenty-four"; III.16 drops "il y a seize ans" and the Publisher's note on dates, and turns "au ban de l'humanité" into "a scourge to humanity". A source quirk, kept: White ¶80 of II.17 breaks mid-sentence ("two or four years of" / "abandonment"), as the Gutenberg HTML has it.
- 2026-11-20 The projection: about 33 k tokens a labeller plus 5.4 per word of the side-by-side text (420,646 words for the book): 2.8 M at four chapters a labeller, 3.0 M at three, 3.6 M by flat scaling; with a finder's check, about 3.1 to 3.9 M. Put to the author with the place for the lists.
- 2026-11-20 d back (I.6 to I.9): 54 discords, 1 outline slip (00800 beat 1: "Vivant !" is a cry, not a question); 162,072 tokens, 25 calls, 4.0 min; passes the checker. For the clue lists, when `plan/reread-hooks.md` is made: White cuts I.9 ¶105, "Peut-être voyait-il des hommes pour la première fois" (the capybara), a hint that the island is unvisited.
- 2026-11-20 c back (I.2 to I.5): 66 discords, 5 outline slips; 171,210 tokens, 20 calls, 5.1 min; passes the checker after one heading was recited (I.2 ¶57 n1). c corrected three beads in I.2 and one run in I.5 (¶60 to ¶63). A source quirk, confirmed in the Gutenberg HTML: White's I.2 ¶25 repeats ¶23's "Mr. Smith, do you want to escape?" where the French has ¶29 (Smith reads Pencroff's face), and the next line opens with a doubled quote mark; the French asks once. Logged as White's, not the derivation's.
- 2026-11-20 e back (I.10 to I.13): 81 discords, then 80 (the main session removed I.12 ¶41's "trop haute"/"too low", which is Wikisource's correction; White follows the print's "basse"), 3 outline slips; 188,947 tokens, 21 calls, 5.2 min; passes the checker. White cuts I.11 ¶91 to ¶92, the war's cause and Lincoln's death foretold.
- 2026-11-20 f back (I.14 to I.17): 96 discords, 1 outline slip (01700 beat 4: "sledge" for the French "claie", a hurdle); 174,427 tokens, 14 calls, 5.0 min; passes the checker (fixed to accept "None found."). f corrected beads in I.14 (White ¶11 to ¶17, one step off) and I.17 (an exchange one speech off).
- 2026-11-20 g back (I.18 to I.21): 69 discords, 1 outline slip (02100 beat 5: "alive" added to Cyrus's claim); 161,961 tokens, 23 calls, 4.2 min; passes the checker. Beads corrected in I.18, I.20 and I.21. White's I.19 ¶31 ends without its full stop ("head-cook Neb was not particular"), as the Gutenberg HTML has it; logged in texts/README.
- 2026-11-20 h back (I.22 to II.3): 88 discords, 3 outline slips (02200 beats 9 and 11; 02500 beat 10, "some hundred paces" for "quelques cents pas"); 187,170 tokens, 19 calls, 5.2 min; passes the checker. h's tallies by kind for I.22 did not add up; counts by kind are taken from the headings at close. Misprints in the Gutenberg White ("l5 pounds", "I adzes") are logged as discords, marked as readings.
- 2026-11-20 i back (II.4 to II.7): 72 discords, 4 outline slips; 173,089 tokens, 22 calls, 4.7 min; passes the checker. Of the slips, 02900 beat 5's "three weeks" against seventeen days is already flagged in the 02900 notes, so it is no slip; 02900 beat 4's "three sides" is checked at the fold-back.

## Resolution

(On close.)
