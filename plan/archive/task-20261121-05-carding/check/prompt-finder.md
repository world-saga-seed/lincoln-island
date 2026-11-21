# The phase 4 finder's prompt

*Filled in for each finder: {AGENT} (f1, f2), {CHAPTER} and {REPORTS}.*

---

You are checking a sample of "cards": English notes on Jules Verne's *L'Île mystérieuse* (Hetzel, 1875), each fact cited by part, chapter and paragraph and resting on French words quoted under it. The French is the authority. The repository is the current folder; every path below is relative to it. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.

READ ONLY:
- plan/archive/task-20261121-05-carding/check/sample.md, your section (## {AGENT}): thirty fact lines, each with its card and line number;
- each card named, at the line given (read the quote under it and the card's head);
- the "What a card holds" section of plan/archive/task-20261121-05-carding.md;
- texts/README.md (how the French is cited);
- the French: texts/fr-1875/NN.md (I.n is NN = n; II.n is 22 + n; III.n is 42 + n), and for a "VML" cite texts/vml-1870/NN.md (VML I.n is n; VML II.n is 24 + n): the cited paragraphs, with a few around them;
- for TASK 2: the chapter {CHAPTER}, the folder index tables world/*/README.md, and the carders' reports {REPORTS} (their crowd-figure lists). To find a card by a word: `python3 tools/cards.py find WORD`, run from the repository's folder.

TASK 1. For each of your thirty facts, answer:
1. **True?** Does the French at the cite say what the English line says? Not more, not less, not other. A line that adds an inference without the mark *(My reading, to confirm.)*, or that takes one side where the text gives two, is a finding.
2. **Cited?** Is the cite the paragraph the quote is in, and does the quote hold the words the fact rests on?
3. **Placed?** Is it a fact about its card's subject (not a scene of the story only, not another subject's fact)?

TASK 2. Read chapter {CHAPTER} through. List every named or described person, animal, place and thing in it that the colonists meet, own, make or use. For each, say whether it has a card (give the file) or is listed as a crowd figure in the reports (give which). Anything with neither is a finding.

THE FORM of your final message:

    ## Task 1
    ### N. <card file>, line L
    - verdict: sound | finding
    - finding: <one sentence: what is wrong>
      - card: <the card's words, copied exactly>
      - french: <the French words, copied exactly, that show it>
      - at: <II.4 ¶12>

    ## Task 2
    - <subject>: <card file> | crowd figure (<report>) | finding: no card and not listed
      - french: <the words naming it, copied exactly> (<¶>)

Give a finding only where you can quote the text that shows it. End with two lines: "Task 1: 30 facts, N sound, N findings." and "Task 2: N subjects, N carded, N crowd figures, N findings."
