# The finder's prompt (the phase 2 check, BRIEF.md: "a Haiku finder samples against the French")

*Filled in for each finder: {AGENT} (f1, f2) and {ROWS} (its half of `sample.md`).*

---

You are checking a sample of scene-outline beats against the French text they summarise. The book is Jules Verne's *L'Île mystérieuse* (Hetzel, 1875). The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-{AGENT}/ and nowhere else.

READ ONLY:
- texts/README.md (how the French is laid out and cited: one paragraph a line, "¶N [p.N] text"; footnotes "nN", plate captions "plN")
- for each row below, the outline file it names, and the French chapter it cites: chapter NNNNN is texts/fr-1875/NN.md, where NN is NNNNN ÷ 100 (00100 is 01.md, 04300 is 43.md). Read only the cited paragraphs of the French, with a few around them for context.

WRITE NOTHING. Your findings are your final message.

YOUR BEATS:

| Chapter | Outline | Beat | Heading |
|---|---|---|---|
{ROWS}

FOR EACH BEAT: read the beat (its heading, its points, its quotes) and the French paragraphs its heading cites. Then answer four questions:

1. **True?** Does every English point say what the French says? A point is wrong if it changes who did something, what, when, where, how many or why, or turns a guess in the text into a fact.
2. **Complete?** Is anything in the cited paragraphs that a later chapter depends on missing from the beat: a thing made or found, a date, a number, a decision, a clue?
3. **Placed?** Does each quote come from inside the beat's range (or the note or plate its "at:" line names)?
4. **Marked?** Does every point carry a mark?

THE FORM of your final message, one block per beat:

    ## NNNNN, beat N: <heading>
    - verdict: clean | finding
    - finding: <one sentence: what is wrong or missing>
      - outline: <the outline's words, copied exactly>
      - quote: <the French words, copied exactly, that show it>
      - at: <I.1 ¶12>

Give a finding only where you can quote the French that shows it. A beat with no finding says "verdict: clean" and nothing more. Do not judge style. Do not suggest rewrites. Do not report a discord the outline already flags. End with one line: beats checked, beats clean, findings.
