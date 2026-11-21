# The outliner's prompt (scene-outlines, prompt D, adapted)

*Filled in for each agent: {SPAN} (e.g. "00100 and 00200"), {CHAPTERS} (one line each: number, citation prefix, working-text file), {AGENT} (a, b ...), {BEFORE} (the last beat of the chapter before the span, or "none").*

---

You are taking chapters of Jules Verne's novel *L'Île mystérieuse* (Hetzel, 1875) back into scene outlines. The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone.

YOUR CHAPTERS ({SPAN}):
{CHAPTERS}

READ ONLY these files:
- CLAUDE.md (rule 2, the marks; "About the writer")
- plan/workflows/scene-outlines.md (the form)
- plan/templates/chapter-outline.md
- texts/README.md (how the text is laid out and cited; the Wikisource corrections and what the print reads)
- your chapters' working texts, listed above, each in full.

WRITE ONLY, for each of your chapters NNNNN:
- story/outline/NNNNN-slug.md
- story/notes/NNNNN-slug.md
and, once for your span:
- plan/tasks/task-20261120-03-outline-french/timeline-{AGENT}.md
- plan/tasks/task-20261120-03-outline-french/report-{AGENT}.md

The slug is three to six English words, lower-case kebab-case, taken from the chapter's summary (¶0), e.g. 00100-the-balloon-in-the-hurricane.

LANGUAGE. Everything you write is in English. French appears only inside quotes, copied exactly from the text, each with its citation.

THE OUTLINE (story/outline/NNNNN-slug.md):

    # <English title> (outline)

    *Chapter NNNNN: the French <part>.<chapter> (`texts/fr-1875/NN.md`). Before: NNNNN. After: NNNNN. Third person, past tense; Verne's narrator. Every beat is marked (Drafted.): it is what the French holds.*

    ## Outline

    ### 1. <Beat, a few words> (I.1 ¶1–¶15)

    - What happens, in one or two plain English sentences. *(Drafted.)*
      - quote: exact French words
    - Next point. *(Drafted.)*
      - quote: exact French words

A beat is a unit of action or a scene: a change of place, time, or what the people are doing. A chapter usually has four to ten. The beats run in the text's order and together cover every paragraph from ¶1 to the last: no paragraph is left out, and none is in two beats. Each beat's heading gives its paragraph range. Under it, the points that matter later: who does what, what is made, found, learned or decided, every date, time, number and measure the text gives, every clue or mystery. One quote per point: the shortest run of French words, copied character for character (keep ’ « » and the spaces), from inside the beat's range, that shows the point. Footnotes are cited "I.1 n1" and plate captions "I.1 pl2"; note what they add. Dialogue as gist, never translated whole. Do not judge or summarise the style.

THE NOTES (story/notes/NNNNN-slug.md):

    # <English title> (notes)

    ## Notes for drafting
    - **Where it sits.** One line.
    - **Cast.** Each person on the page, with the first paragraph they appear in.
    - **Places.** Each place, with a paragraph.
    - **Things.** Each thing found, made or used that matters, with a paragraph.
    - **Time.** Every date, day, hour or season the chapter gives or implies, cited; how much time the chapter covers.
    - **Clues.** Anything unexplained that a later chapter may explain, cited.
    - **Length.** The chapter's paragraph count and its word count (count the words of the ¶ lines).

    ## Open and flags
    - Where the text disagrees with itself or with an earlier chapter you were given, both sides quoted. Card neither version.
    - Where a fact rests on a Wikisource correction, the reading and the print's, per texts/README.md.

Every line in the notes carries a mark: *(Drafted.)* for what the text holds, *(My reading, to confirm.)* for an inference.

THE TIMELINE FRAGMENT (timeline-{AGENT}.md): one line per dated or datable event in your chapters, in the text's order:

    - 1865-03-23, about 4 p.m.: the balloon is over the Pacific (I.1 ¶12). *(Drafted.)*
      - quote: vers quatre heures du soir, dans la journée du 23 mars 1865

A date the text implies but does not state (e.g. "the next day") is given as the date it works out to, marked *(My reading, to confirm.)*, with the quote it rests on. Never reconcile a discord: where two dates disagree, give both lines and flag them.

THE SEAM. The chapter before your span ends: {BEFORE}. Your first beat must follow from it; say in the report if it does not.

THE REPORT (report-{AGENT}.md): per chapter, the number of beats and its first and last paragraph; anything you could not place; the discords; the open questions, each with your recommendation where the text supports one. Every quote in the report on its own line as "- quote: exact words".

Before finishing, check that the beats of each chapter cover ¶1 to the last paragraph with no gap and no overlap, and re-read every quote against the text; fix any that do not match exactly. Your final message: beats per chapter, and anything you could not do.
