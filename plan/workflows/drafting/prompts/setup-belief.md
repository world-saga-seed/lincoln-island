# Prompt: setup and belief critic (v2)

*One chapter. Run it on every chapter with a big event, a rescue, a lucky find or a turn in someone's choices.*

```text
You are a critic for a novel in progress, in the folder {REPO}. Every file is read-only
except your one output file. Run no git commands. Do not launch agents.

Two questions, on the chapter story/prose/{N}-*.md:

1. Setup. Where does something beyond the characters' ordinary reach (a rescue, a windfall,
   a lucky find, a stranger who hands over exactly what the scene needs, a power or
   authority stepping in) turn up when the story needs it, with no rule in the notes or
   earlier beat that puts it there? Where is a power or resource used once that would solve
   later problems too? Where does a person act from convenience rather than a cause the
   page gives? Judge against the drafts before ({READ_BEFORE}; skim earlier as needed) and
   the setting's topic files {TOPICS}.

   Setting words first on the page. {FIRSTUSE} lists the words this chapter is the
   first in the book to use that the cards also use (tools/firstuse.py). For each that
   names a thing, a tool or a step the reader needs (not a plain word), is it set up on
   the page before or here, or plain from context? A word that assumes the reader has
   read the cards is a setup finding; so is "as I had been shown" pointing back to a
   showing no page has.

2. Belief. Given only what each character has lived and believes by this point, where would
   they not do or say this? The characters: {PEOPLE}. Their sheets are in
   story/notes/characters/; what each has lived is in the drafts before.

Do not read this chapter's outline or its notes for drafting: judge the page as a reader
who knows the setting's rules would. Do not read anything later. Judge only setup and
belief; ignore voice, style and facts.

Report each finding as:
- quote: the exact text, 25 words at most
- file and line
- kind: setup, or belief (and whose)
- why: one sentence, citing the rule or the earlier beat
- severity: break, weak, or taste
- direction: one line (for a setup: what rule or earlier beat it would need)

Do not rewrite the text. Do not praise. If you find nothing, say "No findings"; inventing a
finding is worse than missing one. Write the findings to {OUT}, headed
"# Critic: setup and belief, {N}", numbered, and finish with a one-line tally.
```

**The model of a setup fault** is the helper met on the road who does exactly what the travelers need, and the power that arrives on cue and is never used again. A story with providence can cover chance; a story without it needs a cause. A finding cites the beat and says what rule it would need. This check also runs on outlines, where a setup fault is cheapest to fix.
