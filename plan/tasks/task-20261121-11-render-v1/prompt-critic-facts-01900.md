# The facts critic's prompt for 01900 (from the phase 5 calibrated facts critic)

---

You are checking an English render of a chapter of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875) against the French. The French is the authority. The repository is the current folder; every path below is relative to it. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.

READ ONLY these three files:
- the French: texts/fr-1875/19.md (paragraph-numbered ¶0 to ¶48, with a footnote n1; the pl lines are plate captions and are not rendered);
- the render: story/prose/01900-the-facade-the-ladder-and-the-warren.md (it has no paragraph numbers; it follows the French paragraph by paragraph, the heading and summary line first);
- Stephen W. White's 1876 translation of the same chapter: texts/white-1876/19.md (White often cuts or changes; that is known and listed, and is not your question).

YOUR QUESTION, paragraph by paragraph: where does the render say something other than the French?
- **added:** the render says what the French does not (an explanation, a figure, a cause, a feeling, a modern idea);
- **lost:** the French says what the render leaves out (a clause, a figure, a name, a qualification, a note);
- **changed:** a fact, figure, date, name or relation differs;
- **softened:** the render lowers (or raises) the force of the French on politics, war, nation, race, religion, violence or feeling.
For each finding, say also whether White does the same thing at that point (yes, no, or partly), quoting White.

Ordinary choices of English that keep the sense are not findings. Give a finding only where you can quote both the render and the French that show it, each quote copied exactly, unbroken, from its file.

THE FORM:

    ### ¶N: <kind>
    - finding: <one sentence>
      - render: <exact words>
      - french: <exact words>
      - white: <exact words, or "—" if White has nothing there>
      - white does the same: yes | no | partly

End with one line, "01900: N findings.", and the totals by kind and by "white does the same".
