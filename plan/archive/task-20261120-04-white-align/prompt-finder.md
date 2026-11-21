# The phase 3 finder's prompt

*Filled in for each finder: {AGENT} (f1, f2) and {ROWS} (its half of `sample.md`).*

---

You are checking a sample of "discords": places where an 1876 English translation (Stephen W. White's) of Jules Verne's *L'Île mystérieuse* is said to depart from the French (Hetzel, 1875). The French is the authority. The repository is the current folder; every path below is relative to it. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; any scratch file goes in <scratchpad>/agent-{AGENT}/.

READ ONLY:
- each list named below (texts/align/NN-discords.md): find the discord by its number and heading;
- the French chapter texts/fr-1875/NN.md and White's texts/white-1876/NN.md: read the paragraphs the heading cites, with a few around them (White often moves a sentence to the next paragraph).

YOUR DISCORDS:

| NN | List | Discord |
|---|---|---|
{ROWS}

FOR EACH DISCORD, answer:
1. **Real?** Does the French say what the bullet says it says, and does White say (or leave out) what the bullet says? Look in the neighbouring White paragraphs before agreeing that White leaves something out: a "cut" is wrong if White renders the matter a paragraph away.
2. **Kind?** Is the kind right (cut: White leaves French matter out; condensed: White sums it up; addition: White adds; changed: a fact differs; softened: tone or force on politics, religion, war, race, violence or feeling is lowered or raised)?
3. **Fair?** Is it a departure in sense, not a mere choice of words that keeps the sense?

THE FORM of your final message, one block per discord:

    ## NN, discord N: <heading words>
    - verdict: sound | finding
    - finding: <one sentence: what is wrong>
      - french: <French words, copied exactly, that show it>
      - white: <White words, copied exactly, that show it>
      - at: <II.4 ¶12; White ¶10>

Give a finding only where you can quote the text that shows it. End with one line: discords checked, sound, findings.
