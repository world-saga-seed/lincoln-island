# Prompt: grade the closed-book quiz (v1)

```text
You are grading a reader's answers to a closed-book quiz on a novel. Read only {KEY} and
{ANSWERS}. Run no git commands. Do not launch agents.

For each question, mark:
- should know: right, wrong, or blank; and sure or guess as the reader marked it;
- guess: too plain (right and sure), on target (right, guessed), off (wrong), or too faint
  (blank).

Then list: every confident wrong answer to a should-know question (a misread), every
confident right answer to a guess question (a hook too readable), and every blank guess
(a plant too faint), each with the key's line.

Write it to {OUT}, headed "# Quiz grades: {READER}, {LABEL}".
```

The reader answers in its own session, after reading, from memory: "Answer from what you remember; do not reread. Mark each answer sure or guess."
