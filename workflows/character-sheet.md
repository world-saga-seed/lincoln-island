# Character sheet

*Basic.*

One agent gathers everything the notes and outlines say about one character into a single sheet, and proposes what the notes leave open, marked. Run it when a character recurs and needs one place to check against. The blank form is `plan/templates/character-sheet.md`.

**Grade.** A judgment. Settled facts carry their source; everything new is a proposal.

## The loop

1. **Open a task** naming the character, the scope (the arcs they live in) and the start hash.
2. **One fresh agent** writes the sheet ([prompt](#prompt)), marked *(Proposal.)* at its top.
3. **Verify:** quotes resolve; nothing marked settled lacks a source.
4. **Review** against the setup check: nothing in the backstory above the character's station or reach, and nothing outside the scope.
5. **Put the open questions to the writer** one at a time. Fold each answer as it comes; answers open new causes, so budget for the review to outrun the list.
6. **Make canon** what the writer settles; log the run.

## Prompt

> You are writing a reference sheet for **{NAME}**, a character in a novel in progress, in the folder {REPO}. Scope: {SCOPE}. Read `README.md`, the voice sheet, the main characters' sheets, the cards their life touches, and every outline that names them ({FILES}). Write only `story/notes/characters/{FILE}`. Run no git commands; do not launch agents. Mark every point: *(Settled …)* with its source; *(Proposal.)* for what you add; *(My reading, to confirm.)* for inferences. The writer has a long-developed design in mind: where the notes are silent on something important, prefer a question to an invention. Sections: At a glance (a few lines, each linking its section); What the notes settle; Backstory (proposed, within the setting's rules and the character's station); Personality and voice (how they talk, what they find funny, what they fear; **voice them from the whole person, never from their job**); Habits (grounded in their trade or life, with "Not:" lines); Their arc within the scope; Relationships; Rules for writing them (what they must never become); Conflicts and gaps in the notes, quoted; Open questions, each with your recommendation. A reference, not prose.
