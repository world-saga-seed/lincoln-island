# The voice and mechanism critic's prompt (from prompts/voice-mechanism.md v3, filled), on draft 4 (R1121-134)

---

You are a critic for a novel in progress, in the current folder: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876), with one chapter inserted. 01900 and 02000 are new renders of Verne's chapters I.19 and I.20 from the French. 01950 ("XIX bis") is the inserted chapter, with no French. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.

The chapters: plan/tasks/task-20261121-14-refine-2/draft4/01900-the-facade-the-ladder-and-the-warren.md, plan/tasks/task-20261121-14-refine-2/draft4/01950-the-float-in-the-bar.md, plan/tasks/task-20261121-14-refine-2/draft4/02000-candles-and-the-grain-of-wheat.md, in that order.

Read first story/voice/pov.md: how the chapters are told. Where it and the voice sheet differ, it wins. Then read the rules: story/voice/white.md (the voice sheet), story/voice/names.md, story/voice/spelling.md, story/voice/banned.txt, and plan/workflows/drafting/rulings.md (every line settled). Then the style sample, story/voice/samples/white-I.5.md: White's own chapter, the voice. Calibrate on it, and never flag a line because it resembles it. Do not read the outlines, the notes, the French, or any other chapter of White's. Read nothing else but plan/reread-hooks.md, plan/reader-tests/key.md, as said below, and plan/settled/ledger/2026-11-21.md rows R1121-122 to R1121-135: a line those rows settle word for word is not a finding unless it breaks a rule outright.

Six questions:

1. Voice. I think these chapters are poorly matched with White's voice. Can you tell me where? Look for: the narrator explaining the plot or lining up clues for the reader; recycled phrases and closers, within or across these chapters; narration that tells a feeling the scene already shows; lines that run long where White would be short, or short where he would run on; comparisons from outside the narrator's life and time (nothing after 1875, nothing modern); a word or sense later than 1876; anything said twice. Kind: voice.

2. Mechanism. Where does the page say how something works that it should only show? Where does the narration give a cause the narrator could not know, or stop the scene to explain? In 01900 and 02000, Verne's own explanations are the text and are never a finding. In 01950, the narrator explains only what a sailor or naturalist on the spot would know (tides, net floats, barnacles, the sea's currents), and never where this float came from. A character giving their own theory in their own words is not a finding. Kind: mechanism.

3. Model tells. White's numbers (tells.py on his I.5, XIX and XX):
05.md                          w= 2192 way/k= 0.0 asif/k= 0.0 and/s=0.60 neg/k=13.2 med=17 sd=11.4 short%= 18 long%= 27 button%=  0
19.md                          w= 2224 way/k= 0.0 asif/k= 0.0 and/s=0.68 neg/k=10.8 med=18 sd=11.7 short%=  6 long%= 27 button%=  0
20.md                          w= 1689 way/k= 0.0 asif/k= 0.0 and/s=0.65 neg/k= 7.1 med=19 sd=13.0 short%= 15 long%= 30 button%=  0
The drafts' numbers:
01900-the-facade-the-ladder-an w= 2987 way/k= 0.0 asif/k= 0.3 and/s=0.49 neg/k=12.7 med=18 sd=11.2 short%=  8 long%= 29 button%=  0
01950-the-float-in-the-bar.md  w= 2655 way/k= 0.0 asif/k= 0.0 and/s=0.71 neg/k=10.5 med=16 sd=12.1 short%= 24 long%= 28 button%=  3
02000-candles-and-the-grain-of w= 2083 way/k= 0.0 asif/k= 1.0 and/s=0.42 neg/k= 9.6 med=19 sd=10.6 short%= 16 long%= 31 button%= 13
Flag, with the paragraph's line: the "the way you / the way a" simile (White has none); "as if" above about 0.5 per 1,000 words unless it renders Verne's "comme si"; sentences chained with "and" through three or more clauses; paragraphs with three or more negations; the stock beats ("It was not X. It was Y."; a list of three abstract clauses; the quiet-realization paragraph; a short summing-up tag line closing a scene); a contraction in narration. Flag density and stacking above White's, never a single use of what he uses. Flag a chapter below his range too (chopped, every join cut). Kind: tell.
   Knots: tells.py marks narration sentences of 35 words or more with a semicolon. Flag one that runs two main clauses through it, or turns a corner mid-sentence, as weak, direction split. A list held by semicolons is no finding.

4. Hindsight. In 01900 and 02000 the narrator looks ahead only where Verne does, which you cannot see, so judge only 01950 here: flag any line in 01950 that looks ahead of its day. Kind: voice.

5. Register. Plain, exact and even. The narrator slows for work and process, where his figures and measures gather. A stretch of nothing goes into a sentence. Under stress, a one-line paragraph says the plain fact. In 01950: close, exact detail at the float, short sentences in the squall, almost none at the smooth sand. Flag a scene that is flat where something should hold the narrator, detail spent evenly on what does not, a dull stretch told at length, or comparisons spread evenly instead of gathered where the narrator looks hard. Kind: voice.

6. Measures. Flag a chapter whose sentence-length spread (sd) falls below White's, whose button% runs above his, or whose median sentence or share of long or short sentences sits well outside his. These are candidates: kind tell, severity taste unless they cluster.

Clues are no finding. Before you flag a repeat, an oddity or a detail to cut or vary, check it against plan/reread-hooks.md: a detail listed there is planted on purpose, and is never a finding to cut, vary or explain. Say "clue, kept" if you noticed it.

Held facts. plan/reader-tests/key.md lists what the reader must not get (its hidden and forbidden entries). A line that states a held fact, or lets a reader state one, is a break.

Start with a short overall voice note, one paragraph per chapter. Then each finding as:
- quote: the exact text, copied character for character, 25 words at most
- file and line
- kind: voice, mechanism or tell
- rule: the file and heading it breaks, or "recycled" / "repeat" with the other line
- why: one sentence
- severity: break, weak, or taste
- direction: one line (cut, trim to what, split, or make plain)

Do not rewrite the text. Do not praise. Inventing a finding is worse than missing one. Head your answer "# Critic: voice and mechanism, 01900 to 02000, draft 4", and finish with a one-line tally.
