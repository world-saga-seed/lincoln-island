# Lincoln Island: the executor's brief

This file is how it runs, phase by phase, so the record shows the method working, not flailing. Drafted by the session, 2026-11-20, for the author to approve.

## How it stays clean

- **Decide before doing.** Every question a phase needs is settled before the phase starts (phase 0 lists them). Nothing is improvised mid-phase; a surprise stops the phase and goes to the author.
- **One phase, one commit,** made only after that phase's check passes. The history reads as the plan in order.
- **Honest record.** A check that fails, a draft that is redone, a card that was wrong: logged as such, with the fix. Clean means planned and recorded, not hidden.
- **The kit as published.** The run uses a fresh clone of the World Saga Seed kit, its workflows and tools as they stand; any change the run needs goes to the kit first, as its own change, so the benchmark tests the kit anyone can get.
- **Who did what.** Every ledger row carries its mark (below, "Who plays the author").
- **Stay inside this repo.** Read nothing outside it: no other folders on this machine, no other sessions' files.
- **Costs logged, every session.** Every session records its token log in `plan/records/tokens.md` (the author, 2026-11-20): the key-frame and discussion sessions as well as the agent runs, the main thread's tokens taken from the session transcript's usage counts at close, each agent run's from its result. So the cost of the author's direction shows beside the cost of the drafting. At most two agents at once; finders on Haiku, critics on Sonnet, the drafter on Opus.
- **Private until the author says.** No push, no post, until the end and the community check.
- **Free to all** (the author, 2026-11-20): the whole run, the cards, ledger, prompts, controls and epub, is passed out free to anyone interested; the readers who take it are the human blind readers. The release terms are the author's to set in phase 0.

## Who the author is

The run is a demonstration of the kit, not a claim of human authorship. **The author is a model** (Claude, in another session), who messages you: it answers phase 0, sets the insert's key frames and placement (phase 6), settles what you ask, and decides what to do with the reader's comments. A human reads the ereader builds (phases 9 to 11) as a reader; their comments reach you through the author.

**The scene is not in this brief.** The author brings a pitch for the missing chapter into the discussion in phase 6, a piece at a time, as questions and ideas; work each one through from the cards and the French, and record each settled point as a ledger row when the discussion reaches it. Do not search for the scene, guess it, or plan ahead for it; until phase 6 the run knows only that one chapter is to be inserted.

Every ledger row carries one of four marks:

- **the author's:** the author's decisions, the pitch among them;
- **Verne's:** facts cited to the French by part, chapter and paragraph;
- **the executor's proposal:** the drafter's and critics' inventions, marked as usual;
- **a reader's comment:** the reader's notes, each with what the author did with it.

The release says, once: the author was a model; the reader was a human.

## Phase 0: settle before starting

Each is answered by the author or checked by the session, and recorded, before phase 1.

0. **The token log.** A script that reads a session transcript's usage counts (input, cached, output) and appends the session's totals to `plan/records/tokens.md`; run at every session close, from the first. The planning discussion of 2026-11-20 happened in the author's book session, so its tokens are counted from that transcript's Lincoln exchanges and logged as phase 0.

1. **The French text.** Which edition (the Hetzel text of 1874–75), from where, with its checksum. Same for *Vingt mille lieues sous les mers*.
2. **The English translation: White's, one voice.** Stephen W. White's (Philadelphia, Evening Telegraph reprint, 1876; attributed by its 2003 redactor) is the one English source: the voice samples, the controls' neighbor chapters and the old-translation chapters in the book all come from it. Into `existing/` with source and checksum. Kingston's (London, 1875) is not used, unless phase 5 shows one human baseline is not enough. *(The author, 2026-11-20: "restore Stephen W. White's 1876 translation", from a Gemini suggestion; "would it not be better to use one voice?") The session's recollection, to check from the texts: Kingston cut the science and softened the politics, Nemo's among them; White is closer to the French.*
3. **How much of *Vingt mille lieues* to card.** Set by the author before phase 4.
4. **The repo.** A new folder from the kit clone, the kit's commit identity set repo-local, private.
5. **The budget.** An estimate of the carding cost (the long pole) from the kit's cost table, put to the author before phase 2.
6. **The controls.** How many tries per control model (one, or the same few for each), which Gemini model, and whether a blind reader ranks all versions.
7. **The release terms** for the free release (the human's: nothing is published without their word).
8. **The read-aloud tool.** Needed by phase 10: a generic recorder in the kit, or one the author supplies; the record says which.

## The phases

| # | Phase | Kit workflow | Out | Check | Gate |
|---|---|---|---|---|---|
| 1 | **The sources.** White's translation and the French *L'Île mystérieuse* are in `existing/`, handed over by the author with their SOURCE.md and checksums: verify the checksums, record them, and derive the working texts (paragraph-numbered) without changing `existing/`; fetch *Vingt mille lieues* the same way; fill CLAUDE.md; the settled points become the first ledger rows. | intake, set up `plan/` | the skeleton, `existing/`, the ledger | links, cards | |
| 2 | **Outline from the French,** the ground truth: a scene outline of every chapter, paragraph-numbered so every later row can cite it; a timeline. | scene-outlines | outlines, timeline | a Haiku finder samples against the French, a Sonnet critic judges | |
| 3 | **Outline from White, aligned to the French** by paragraph. Every place White departs (a cut, an addition, a changed fact, a softened line) falls out of the alignment as a discord beat, citing the French paragraph. | aligner (script), a finder | White's alignment; the discord list | every label cites a French paragraph; every quote checked by script | |
| 4 | **Card,** from the French, in English, each fact cited: *L'Île mystérieuse* in full (one card per person, place, thing and made thing, the tool chain in order); *Vingt mille lieues* in the scope the author sets. More of it is carded only if the brainstorm needs it, logged with why. | card-existing | the cards | cards check; a finder samples facts against the French | **the author** confirms the scope |
| 5 | **Re-render the missing pieces,** the calibration: a sample of discord beats (the cuts in the chapters around the insert, and about ten spread through the book) rendered from the cards and the French, set beside White's. Where a render departs from the French in a way White did not, it is a candidate tell, logged for the kit's tell lists. It tests the voice where Verne's own words are the answer key, before anything new is written. | drafter, critics | the renders; the candidate tells; the voice chapter chosen (White's least cut or changed against the French) | facts and voice critics; quotes checked | **the author** approves the voice chapter |
| 6 | **The brainstorm,** the pitch fed by the author a piece at a time; it settles the facts the chapter rests on, the key frames and the placement, each a ledger row when the discussion reaches it. Then the insert's outline, the two neighbors' outlines from Verne, and a reader-test key for each. | arc-pitch, scene-outlines, reader tests | ledger rows; three outlines, three keys | outlines against cards | **the author** sets every key frame |
| 7 | **The prompt-only controls:** the same three chapters from Opus and from Gemini by prompts alone, no cards, no ledger, no checks. One fixed prompt per chapter, written from the chapter as settled in 6, with White's neighboring chapters pasted in as a real prompter would, the same for both models; frozen and committed before phase 8 so no method draft can leak into them. Gemini runs in the human's account; Opus in a fresh context. Every prompt and reply kept verbatim, with the model, date and number of tries. | | six control chapters, the prompts | the same checks and critics as 8, run on the controls too | **the author** approves the prompts |
| 8 | **Render version 1:** the chapter before, the insert, the chapter after. | drafter, rulings | three chapters, v1 | mechanical checks; facts and voice critics; the seams read against Verne's own chapters; the blind probe | |
| 9 | **The ereader read.** An epub: each neighbor in White's translation and in v1, the insert in v1 (marked as having no translation). The human reads as a reader; their comments reach the author, and each comment and what the author did with it is a ledger row. | ereader build | epub, ledger rows | | **the author** reads |
| 10 | **The voice reading.** The human reads the three chapters aloud with their comments, section by section; transcribed, aligned, the comments filed beside their sections. | read-aloud | recordings (kept local), transcripts, marks | | **the author** reads |
| 11 | **Refine to final** from the reading. | drafter, critics | three chapters, final | the same checks as 8; the blind probe again | **the author** approves |
| 12 | **The book.** One epub: White's translation, the two prompt-only controls, the v1 redo, the final, each labelled; and the cards and ledger alongside. | ereader build | the epub; the cards and ledger | links, `check_leak` | **the author** approves |
| 12b | **Clearance, after completion** (the human, 2026-11-20: "we must perform this to show we have authentic voice not modern voice anyway"; run only once phases 1 to 12 are done, before the repo is created). (1) **Inputs:** every source's licence checked and recorded: Verne's French, White's 1876 text and Férat's plates are public domain; the Project Gutenberg header and footer are stripped or its licence kept whole; the 2003 redactor's note is quoted briefly with credit, not shipped; Wikisource's own additions are stripped or attributed (CC BY-SA). (2) **Outputs:** an overlap script (a generic kit patch) lists every run of eight or more words that a published text shares with a reference: the phase 5 renders, the three chapters in every version, and the prompt-only controls, against White's and Kingston's texts (overlap with them is legal, and measures how much the renders lean on them) and against any modern translation the human owns (Kravitz 2001, Stump 2001; kept on their machine, never committed). Each long run against a modern translation is reviewed; a passage that reproduces one is rewritten from the French and the rewrite logged. The same overlap measures the voice: White's 1876 English, not a modern one. If no modern translation is checked, the release says so. Due diligence, not a legal opinion. | overlap script (kit patch) | the clearance report | every flag reviewed and resolved | **the human** supplies any modern translation; says the release may go |
| 13 | **Close.** The retrospective: what worked, what failed and was fixed, the tokens per phase and per session, the measures (the voice against the old translation on each neighbor, at both seams; v1 against the two prompt-only controls, the same inputs with and without the method; the final on top of that, what the author's direction adds; measured by fact errors counted against the French, by the kit's checks, by Opus and Gemini each judging every version blind, and by human readers ranking them blind). The cost split: the carding once, the chapter after it. Then the write-up and the community check. | retrospective | the report; the post draft | the community check | **the author** says post |


## What the reader of the post can check

- Every card against the French, by its citation.
- Each re-rendered neighbor against Verne's own chapter in White's translation: same content, the method's voice against the translator's.
- The insert against everything around it: it enters and leaves Verne's canon with nothing changed.
- The method against prompting alone: Opus and Gemini given the same brief and key frames by prompt, the prompts printed, the same checks run on all.
- Who decided what: the ledger, row by row.
- What it cost: the tokens per phase and per session, the author's direction beside the drafting.
