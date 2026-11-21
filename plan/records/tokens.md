# Token log

*Every agent run, one row each, and every session, one row at its close, so the cost per step can be watched as the book grows and the cost of the discussion shows beside the cost of the drafting. For an agent, tokens, calls and minutes are Claude Code's figures for it; words are the chapter's (or the batch's); "Reading" says how it read: whole files, a reading list, the digest. For a session, the row is `tools/tokens.py`'s, from the session's transcript: its tokens include the agents run inside it, so do not add the session rows and the agent rows together. Flat per step is fine; growth from volume to volume is the warning.*

| Date | Run | Step | Chapter | Words | Reading | Tokens | Calls | Minutes |
|---|---|---|---|---|---|---|---|---|
| 2026-11-20 | the author's session, 17:47Z to 20:25Z | phase 0 planning (upper bound; out 39,394) | | | | 7,876,544 | 61 | 150 |
| 2026-11-20 | the author's session, 2026-11-21 04:17Z on | phase 0 answers (upper bound; out 40,043) | | | | 20,044,050 | 65 | 34 |
| 2026-11-20 | agent, Sonnet: carder, people | budget sample (card-existing) | I.1, I.13, III.16 | 10,234 | whole files: the three chapters, the card form, texts/README, CLAUDE.md | 112,859 | 17 | 5.2 |
| 2026-11-20 | agent, Sonnet: carder, places and things | budget sample (card-existing) | I.1, I.13, III.16 | 10,234 | whole files: the three chapters, the card form, texts/README, CLAUDE.md | 138,953 | 16 | 8.3 |
| 2026-11-20 | agent, Sonnet: outliner a | phase 2 pilot (scene-outlines D) | 00100, 00200 | 5,586 | whole files: the two chapters, the workflow, the forms, texts/README, CLAUDE.md | 98,247 | 12 | 4.5 |
| 2026-11-20 | agent, Sonnet: outliner b | phase 2 pilot (scene-outlines D) | 00300 | 2,630 | whole files: the chapter, the workflow, the forms, texts/README, CLAUDE.md | 58,889 | 8 | 1.3 |
| 2026-11-20 | agent, Sonnet: outliner c | phase 2 (scene-outlines D) | 00400 to 00700 | 11,986 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 120,658 | 33 | 5.0 |
| 2026-11-20 | agent, Sonnet: outliner d | phase 2 (scene-outlines D) | 00800 to 01100 | 13,357 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 154,607 | 23 | 7.8 |
| 2026-11-20 | agent, Sonnet: outliner e | phase 2 (scene-outlines D) | 01200 to 01500 | 12,946 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 149,080 | 24 | 7.4 |
| 2026-11-20 | agent, Sonnet: outliner f | phase 2 (scene-outlines D) | 01600 to 01900 | 12,421 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 129,204 | 22 | 5.7 |
| 2026-11-20 | agent, Sonnet: outliner g | phase 2 (scene-outlines D) | 02000 to 02300 | 12,812 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 146,523 | 27 | 7.3 |
| 2026-11-20 | agent, Sonnet: outliner h | phase 2 (scene-outlines D) | 02400 to 02700 | 13,522 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 151,157 | 23 | 6.2 |
| 2026-11-20 | agent, Sonnet: outliner i | phase 2 (scene-outlines D) | 02800 to 03100 | 13,686 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 134,984 | 24 | 5.8 |
| 2026-11-20 | agent, Sonnet: outliner j | phase 2 (scene-outlines D) | 03200 to 03500 | 14,524 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 142,412 | 21 | 6.6 |
| 2026-11-20 | agent, Sonnet: outliner k | phase 2 (scene-outlines D) | 03600 to 03900 | 13,685 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 147,776 | 22 | 7.0 |
| 2026-11-20 | agent, Sonnet: outliner l | phase 2 (scene-outlines D) | 04000 to 04300 | 13,900 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 147,653 | 27 | 6.8 |
| 2026-11-20 | agent, Sonnet: outliner m | phase 2 (scene-outlines D) | 04400 to 04700 | 14,070 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 141,320 | 21 | 6.5 |
| 2026-11-20 | agent, Sonnet: outliner n | phase 2 (scene-outlines D) | 04800 to 05100 | 10,367 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 116,158 | 18 | 4.8 |
| 2026-11-20 | agent, Sonnet: outliner o | phase 2 (scene-outlines D) | 05200 to 05500 | 11,921 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md | 130,173 | 20 | 5.6 |
| 2026-11-20 | agent, Sonnet: outliner p | phase 2 (scene-outlines D) | 05600 to 05900 | 13,539 | whole files: the four chapters, the workflow, the forms, texts/README, CLAUDE.md; also ran check_outlines.py, not on its list | 134,206 | 22 | 5.6 |
| 2026-11-20 | agent, Sonnet: outliner q | phase 2 (scene-outlines D) | 06000 to 06200 | 11,026 | whole files: the three chapters, the workflow, the forms, texts/README, CLAUDE.md | 114,643 | 23 | 4.8 |
| 2026-11-20 | agent, Haiku: French sorter s1 | phase 2 (French sweep, R1120-39) | all 62 | — | french-sort-s1.tsv | 138,608 | 9 | 3.5 |
| 2026-11-20 | agent, Haiku: French sorter s2 | phase 2 (French sweep, R1120-39) | all 62 | — | french-sort-s2.tsv | 125,973 | 3 | 2.7 |
| 2026-11-20 | agent, Haiku: French reviewer r1 | phase 2 (French sweep, R1120-39) | all 62 | — | french-review-r1.tsv | 234,115 | 5 | 7.4 |
| 2026-11-20 | agent, Haiku: French reviewer r2 | phase 2 (French sweep, R1120-39) | all 62 | — | french-review-r2.tsv | 167,286 | 5 | 3.6 |
| 2026-11-20 | agent, Haiku: finder f1 | phase 2 (the check) | 31 beats, 00100 to 03100 | — | the sampled beats and their cited French | 149,481 | 13 | 2.6 |
| 2026-11-20 | agent, Haiku: finder f2 | phase 2 (the check) | 31 beats, 03200 to 06200 | — | the sampled beats and their cited French | 162,513 | 23 | 3.4 |
| 2026-11-20 | agent, Sonnet: critic | phase 2 (the check) | 3 findings, 12 beats re-read | — | report-f2, critic-recheck, the outlines and cited French | 78,290 | 19 | 1.3 |
| 2026-11-20 | agent, Sonnet: labeller A | phase 3 (pilot) | 00100, 03900 | 13,239 (side-by-side) | the two side-by-side files and outlines | 104,506 | 14 | 2.7 |
| 2026-11-20 | agent, Sonnet: labeller B | phase 3 (pilot) | 05800 | 7,397 (side-by-side) | the side-by-side file and outline | 72,791 | 6 | 1.4 |
| 2026-11-20 | agent, Sonnet: labeller d | phase 3 (White discords) | 00600 to 00900 | 27017 (side-by-side) | the four side-by-side files and outlines | 162,072 | 25 | 4.0 |
| 2026-11-20 | agent, Sonnet: labeller c | phase 3 (White discords) | 00200 to 00500 | 25694 (side-by-side) | the four side-by-side files and outlines | 171,210 | 20 | 5.1 |
| 2026-11-20 | agent, Sonnet: labeller e | phase 3 (White discords) | 01000 to 01300 | 28134 (side-by-side) | the four side-by-side files and outlines | 188,947 | 21 | 5.2 |
| 2026-11-20 | agent, Sonnet: labeller f | phase 3 (White discords) | 01400 to 01700 | 25876 (side-by-side) | the four side-by-side files and outlines | 174,427 | 14 | 5.0 |
| 2026-11-20 | agent, Sonnet: labeller g | phase 3 (White discords) | 01800 to 02100 | 24373 (side-by-side) | the four side-by-side files and outlines | 161,961 | 23 | 4.2 |
| 2026-11-20 | agent, Sonnet: labeller h | phase 3 (White discords) | 02200 to 02500 | 29044 (side-by-side) | the four side-by-side files and outlines | 187,170 | 19 | 5.2 |
| 2026-11-20 | agent, Sonnet: labeller i | phase 3 (White discords) | 02600 to 02900 | 29131 (side-by-side) | the four side-by-side files and outlines | 173,089 | 22 | 4.7 |
| 2026-11-20 | agent, Sonnet: labeller j | phase 3 (White discords) | 03000 to 03300 | 27446 (side-by-side) | the four side-by-side files and outlines; also ran git log and git diff, against its prompt | 187,155 | 23 | 6.3 |
| 2026-11-20 | agent, Sonnet: labeller k | phase 3 (White discords) | 03400 to 03700 | 29716 (side-by-side) | the four side-by-side files and outlines | 183,656 | 21 | 5.6 |
| 2026-11-20 | agent, Sonnet: labeller l | phase 3 (White discords) | 03800 | 8363 (side-by-side) | the side-by-side file and outline | 80,771 | 5 | 1.9 |
| 2026-11-20 | agent, Sonnet: labeller m | phase 3 (White discords) | 04000 to 04300 | 28236 (side-by-side) | the four side-by-side files and outlines | 171,226 | 24 | 4.5 |
| 2026-11-20 | agent, Sonnet: labeller n | phase 3 (White discords) | 04400 to 04700 | 28090 (side-by-side) | the four side-by-side files and outlines | 190,035 | 21 | 5.6 |
| 2026-11-20 | agent, Sonnet: labeller o | phase 3 (White discords) | 04800 to 05100 | 21375 (side-by-side) | the four side-by-side files and outlines | 153,726 | 14 | 4.2 |
