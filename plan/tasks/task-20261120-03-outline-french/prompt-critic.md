# The phase 2 critic's prompt

You are the critic for the phase 2 check of a set of scene outlines of Jules Verne's *L'Île mystérieuse* (Hetzel, 1875), checked against the French. The repository is the current folder; every path below is relative to it. Run no git commands. Do not launch agents. Work alone. Write nothing: your answer is your final message. Any scratch file goes in <scratchpad>/agent-critic/ and nowhere else.

READ ONLY:
- texts/README.md (how the French is laid out and cited)
- plan/tasks/task-20261120-03-outline-french/report-f2.md (the three findings, in its "finding" blocks)
- plan/tasks/task-20261120-03-outline-french/critic-recheck.md (twelve beats to re-read)
- the outline files those two name, under story/outline/
- the French chapters they cite: chapter NNNNN is texts/fr-1875/NN.md, NN = NNNNN ÷ 100. Read the cited paragraphs, with a few around them.

TASK 1. JUDGE THE THREE FINDINGS. For each, read the beat and the French. Say:
- confirmed: the outline is wrong or short as the finding says, and the fix is plain;
- partial: there is something, but less than the finding says (say what);
- rejected: the outline is right (say why).
Quote the French that decides it, and the outline's words, exactly.

TASK 2. RE-READ TWELVE BEATS the first readers called clean. For each, check every point against the cited French:
1. True? Does every point say what the French says (who, what, when, where, how many, why), without turning a guess into a fact or a fact into a guess?
2. Complete? Is anything in the cited paragraphs that a later chapter depends on missing (a thing made or found, a date, a number, a decision, a clue)?
3. Placed? Does each quote come from inside the beat's range?
4. Marked? Does every point carry a mark like *(Drafted.)*?

Report a finding only where you can quote the French that shows it. Do not judge style. Do not report a discord the outline already flags.

THE FORM:

    ## Task 1
    ### 03200, beat 7
    - judgement: confirmed | partial | rejected
    - reason: <one or two sentences>
      - outline: <exact>
      - quote: <exact French>
      - at: <II.10 ¶51>

    ## Task 2
    ### NNNNN, beat N: <heading>
    - verdict: clean | finding
    - finding: <one sentence>
      - outline: <exact>
      - quote: <exact French>
      - at: <cite>

End with two lines: "Task 1: N confirmed, N partial, N rejected." and "Task 2: 12 beats, N clean, N findings."
