# The prune reviewer's prompt (wave 3, R1121-05, R1121-06)

You are reviewing lines that were deleted from the cards of a study of Jules Verne's *L'Île mystérieuse*. The repository is the current folder; every path below is relative to it. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.

READ ONLY: plan/tasks/task-20261121-05-carding/pruned-w3.tsv (each row: an id, the card's file name, and the deleted line) and the section "What a card holds" of plan/tasks/task-20261121-05-carding.md.

THE RULE (the author's, R1121-05): a card holds what is true of its subject, not the story's events. A carder deleted these lines as scene logs. Some were scenes; some were not. For each line, decide:
- **keep**: the line states, or shows by a single telling act, something true of the subject: a trait, temper, belief, skill, knowledge, possession, relation, look, habit, a capacity or limit ("he cannot manage a balloon", "he becomes a skilful archer", "he is not a man to let an occasion slip", "he knows the couroucous are good to eat"), or a change in the subject (wounded, freed, named, first sight of a place, what a thing is made of);
- **scene**: the line only records what the subject said or did at a moment of the story, and tells nothing lasting about it ("he asks whether the engineer can swim", "he offers Nab shellfish", "at the balloon he detaches the ballast bags").
When in doubt, keep.

YOUR ANSWER: one line per id, in id order, tab-separated, with one header line and nothing else:

    id	verdict
    1	keep
    2	scene

Then one line: the counts of keep and scene.
