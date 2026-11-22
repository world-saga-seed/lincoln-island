# Post draft (for the author; nothing is posted without the author's word)

**Lincoln Island: Verne's *Mysterious Island*, restored and then vandalized, by language models**

We used Claude to make Stephen W. White's 1876 English translation of *L'Île mystérieuse* unabridged against the French. It made 3,224 patches to 38 chapters and rendered the other 24 anew in White's voice. A map in the book shows every patch.

Then we vandalized it, on purpose and in files you can delete. We added a dry Iowa scholar who footnotes the places where the story disagrees with itself. We also added one chapter Verne never wrote, XIX bis, "The Float in the Bar". It was written by the World Saga Seed method: the story's facts are kept as notes, every ruling goes on a ledger, and fresh critics have to quote the text they fault.

What we measured:
- **Against prompt-only controls** (Opus and Gemini given the same scene): on Verne's own chapters the method made little difference in facts, where the French holds a model to them, and a clear one in voice: the controls ran to long sentences and house spellings that White's English doesn't have. On the invented chapter it made a large one. The controls broke canon (7 and 2 breaks) and told what the chapter is built to withhold. Version 1 had 4 fact findings against its own notes, and the final reads 15 of 15 as meant in a blind probe.
- **What we didn't expect:** the chapters rendered "in White's English" share 29% of their words, in runs of eight or more, with Kingston's 1875 translation, which no agent was given. The models remember it. White's own text shares 6%.
- **What a human added:** reading the new chapter aloud changed it in thirteen places. In blind scores, restraint fell from 9 to 4 after the read-aloud and came only part way back, to 7, after a character check. The final scores below version 1 on fidelity to the scene, restraint and modern-model habits.

Everything is in the repository: the ebooks, the cards, the ledger, the prompts, the controls, the scores, and a report with what worked and what failed. No human blind-reader ranking was run, and no modern translation was checked.

[link]
