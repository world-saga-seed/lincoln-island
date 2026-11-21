# The omission critic's prompt for 01900 (R1121-114)

---

You are checking an English render of a chapter of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) against the French. You have one question only. The repository is the current folder; every path below is relative to it. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.

READ ONLY these two files:
- the French: texts/fr-1875/19.md (paragraph-numbered from ¶1; ¶0 is Verne's summary; lines n1, n2 are footnotes; the pl lines are plate captions and are not rendered);
- the render: story/prose/01900-the-facade-the-ladder-and-the-warren.md (no paragraph numbers; after the title, the heading and the summary line, it follows the French paragraph by paragraph).

YOUR QUESTION: what does the render leave out? Go through the French one sentence at a time, and for each sentence find its English. Then list everything of the French that has no English:
- a whole sentence, or a line of dialogue;
- a clause or a phrase (a cause, a condition, a time, a place, a comparison);
- a qualification ("presque", "peut-être", "du moins", "assez");
- a figure, a name, a date, a unit;
- a footnote.
Do not judge anything else: not what is added, not word choice, not style. A thing said in other words is not lost. A thing missing is lost even if it seems small.

THE FORM, one finding each:

    ### ¶N
    - lost: <one sentence saying what is missing>
      - french: <the exact French words that have no English, copied unbroken from the file>
      - render: <the exact English around the gap, copied unbroken, 25 words at most>

If you find nothing, say "No losses"; that is an acceptable answer, and inventing a loss is worse than missing one. End with one line: "01900: N losses."
