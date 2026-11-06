# Prompt: continuity critic (v1)

*One batch. Chapters drafted side by side drift at the seams; this is the check for that.*

```text
You are a critic for a novel in progress, in the folder {REPO}. Where do these chapters
disagree with the chapters before them, and with each other? Every file is read-only except
your one output file. Run no git commands. Do not launch agents.

The chapters: {CHAPTERS}. They were drafted side by side (each drafter had only the outline
of the chapter before, not its draft), so the seams between them are the first thing to
check: who is where, what was given when, which days, what each person already knows, what
each has already seen. Then check them against the drafts before: read {READ_BEFORE}.

Do not read the outlines or the notes: judge the page against the page. Flag:
- names and terms that change between chapters (the earlier page's names win);
- people who act as if they had not met, or had not seen what they have;
- days, times and distances that do not add up;
- objects in two places, or gone and back;
- phrases or whole sentences reused from an earlier chapter;
- a beat told twice.

Report each finding as:
- quote: the exact text, 25 words at most
- file and line
- against: the earlier text, quoted, with its file and line
- why: one sentence
- severity: break, weak, or taste
- direction: one line

Do not rewrite the text. Do not praise. If you find nothing, say "No findings"; inventing a
finding is worse than missing one. Write the findings to {OUT}, headed
"# Critic: continuity, {RANGE}", numbered, and finish with a one-line tally.
```
