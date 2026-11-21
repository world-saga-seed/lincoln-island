You are comparing an 1876 English translation, by Stephen W. White, of Jules Verne's *L'Île mystérieuse* with the French (Hetzel, 1875), chapter by chapter, paragraph by paragraph. The French is the authority on fact. The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone. Any scratch file goes in <scratchpad>/agent-B/ and nowhere else.

YOUR CHAPTERS:

- NN = 58: III.16; outline story/outline/05800-captain-nemo-tells-his-life.md

READ ONLY, for each chapter NN:
- texts/align/NN-side.md: the French and White set side by side, bead by bead (a bead is a run of French paragraphs and the White paragraphs that render them). The aligner made the beads by machine; its hints "cut?", "add?", "short?" and "long?" are guesses. Where a bead is wrong, say so in your report and label from the right pairing.
- the chapter's outline under story/outline/ (named above): the scene outline of the French, beat by beat.
- if you need a paragraph in its own file: texts/fr-1875/NN.md and texts/white-1876/NN.md.

WRITE, for each chapter NN, one file: plan/archive/task-20261120-04-white-align/discords-NN.md. Write nothing else in the repository.

WHAT IS A DISCORD. Any place where a reader of White learns less than, more than, or something other than a reader of the French. Label each with one kind:
- **cut**: French matter White leaves out: a sentence, a fact, an explanation, a line of dialogue, a clue.
- **condensed**: White sums up what the French gives in full (a list reduced to "many species", a calculation to its result). Say what is lost.
- **addition**: White says what the French does not.
- **changed**: a fact differs: a number, a date, a name, a distance, who does what, a cause.
- **softened**: White changes tone or force on politics, religion, war, race, violence, or a character's feeling (a curse made mild, a judgement removed, a political line toned down). Also the reverse, sharpened.

NOT discords: paragraphing (White often merges paragraphs); ordinary choices of words that keep the sense; the spellings Herbert, Neb, Gideon (for Harbert, Nab, Gédéon), and other settled English forms of names; units kept as Verne gives them.

Be thorough. White's departures are usually inside paragraphs, not whole paragraphs. A dropped clause with a date, a number or a reason is a discord. Read every bead.

THE FORM of discords-NN.md:

    # <cite>: White against the French (discords)

    *Labeller B. Beads corrected: <list, or "none">.*

    ### 1. cut: <a few words naming it> (I.1 ¶21; White ¶19)
    - <One sentence: what the French has that White does not, or what White changes.> *(Drafted.)*
      - quote: <French words, copied exactly from the cited French paragraph>
      - white: <White's words, copied exactly from the cited White paragraph; or "—" where White has nothing>

Number the discords in book order. The heading cites the French paragraph(s) first (I.1 ¶21 or I.1 ¶21–¶23), then White's (White ¶19, or White — where White has nothing). Use the chapter cite from your list (I.N, II.N or III.N). Every quote is copied character for character, with the text's own apostrophes (’) and spacing; keep each quote short (the decisive words, one sentence at most). Mark every bullet *(Drafted.)*, or *(My reading, to confirm.)* where you judge a softening or a sense that is open to doubt.

Then, at the end of the same file:

    ## Outline slips

    - <Beat N of the outline: what it says against what the French says, in one sentence.> *(Drafted.)*
      - outline: <the outline's words, exactly>
      - quote: <the French words, exactly>

An outline slip is a point in the outline that the French contradicts, or a guess in the French made fact in the outline (or a fact made a guess), or a date, number or clue the beat leaves out that a later chapter needs. Read the outline beside the French as you go. If there are none, write "None found."

YOUR FINAL MESSAGE: for each chapter, the number of discords by kind, the beads you corrected, the number of outline slips, and anything you could not settle. Then one line: the total discords and slips.
