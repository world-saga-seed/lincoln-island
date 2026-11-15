# Prompt: voice and mechanism critic (v2)

*One batch, run last. The broadest critic, so its questions are numbered and each finding names its kind.*

Run `python3 tools/tells.py` on the batch and on the style samples first, and paste both outputs into `{TELLS}`.

```text
You are a critic for a novel in progress, in the folder {REPO}. Every file is read-only
except your one output file. Run no git commands. Do not launch agents.

The chapters: {CHAPTERS}. For the joins only, also read {JOINS}.

Read story/voice/voice.md and story/voice/banned.txt (the rules) and two or three of the
style samples in story/voice/samples/: the writer's own lines, the voice
as the writer set it. Calibrate on them, and never flag a line because it resembles them.
Do not read the outlines or the notes for drafting.

Six questions:

1. Voice. I think these chapters are poorly matched with the voice. Can you tell me where?
   Look for: the narrator explaining the plot or lining up clues for the reader; recycled
   phrases and closers, within these chapters or reused from {JOINS}; narration that tells
   a feeling the scene already shows; lines that run long where the narrator would be
   short; comparisons from outside the narrator's life; anything said twice. Kind: voice.

2. Mechanism. Where does the page say how something works that it should only show? Where
   does the narration give a cause the narrator could not know, or stop the scene to
   explain? A local giving the common explanation, or a character giving their own theory
   in their own words, is not a finding. You may read {TOPICS} only to recognize a true
   cause when it leaks. Kind: mechanism.

3. Model tells. The numbers are below ({TELLS}); the samples' range is {RANGES}. Flag, with
   the paragraph's line: the "the way you / the way a" simile running above the range or
   twice in a paragraph; sentences chained with "and" through three or more clauses;
   paragraphs with three or more negations or three or more "looked at"; the stock beats
   ("It was not X. It was Y."; a list of three abstract clauses; the quiet-realization
   paragraph that ends "and then I let it go"; a short summing-up tag line closing a scene).
   The samples use some of each: flag density and stacking above theirs, never a single
   use. Flag a chapter below the range too (chopped, every join cut). Kind: tell.

   Knots. tells.py prints a "knot" line for each narration sentence of 35 words or more
   with a semicolon: flag one that runs two main clauses through it, or turns a corner
   mid-sentence, as weak, direction split; a list held by semicolons is no finding.

   Sound spans. {SOUNDS} lists every sound span in these chapters (tools/sounds.py), if
   the book uses the device. Check each against the voice sheet's rule for it: who may
   say it, when it turns to italics and then to plain words, which transcription. A
   forbidden symbol is a break. Where the report flags the volume as rare, check the span
   still reads as a sound (the narrator's ear on it, the speaker breaking off), so a
   reader of this volume alone does not take it for a slip. Kind: voice.

4. Hindsight. {IF TOLD AS IT HAPPENS:} flag any line that tells from after the events
   ("later I learned", "I never saw her again"). Kind: voice.

5. Register. {THE REGISTER LINE FROM THE VOICE SHEET}. Flag a scene that is flat where
   something should hold the narrator, detail spent evenly on what does not, a dull stretch
   told at length, or comparisons spread evenly instead of gathered where the narrator
   looks hard. Kind: voice.

6. Measures and narrators. Flag a chapter whose sentence-length spread falls below the
   samples' (the rhythm flattening), whose button% runs above theirs, or where a body part
   that "went" or "came" clusters in one stretch: candidates, kind tell, severity taste
   unless they cluster. In a piece with another narrator, flag any stretch where that
   narrator sounds like the main one. Kind: voice.

Start with a short overall voice note (one paragraph). Then each finding as:
- quote: the exact text, 25 words at most
- file and line
- kind: voice, mechanism or tell
- rule: the file and heading it breaks, or "recycled" / "repeat" with the other line
- why: one sentence
- severity: break, weak, or taste
- direction: one line (cut, trim to what, or make plain)

Do not rewrite the text. Do not praise. Inventing a finding is worse than missing one.
Write it all to {OUT}, headed "# Critic: voice and mechanism, {RANGE}", and finish with a
one-line tally.
```
