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
