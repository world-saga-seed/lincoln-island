# The drafter

*Basic.*

Turns one outlined chapter into a first draft in the narrator's voice. The prompt template is [prompts/drafter.md](prompts/drafter.md).

**Grade.** A judgment. A draft is checked by the chain after it, and is not done until the writer says so.

## What the drafter gets

The POV file comes first ([the template](../../templates/pov.md)): whose head, what each head may know, what is never told. Then the voice sheet (and each head's, where there are several), the banned list, the rulings and the style samples, because the first things read set the voice; then the chapter's outline and notes, the arc outline, the drafts before it, and the cards and sheets (with the **Habits**) of everyone in it. The full list, in order, with `{FRAME}` and `{EXTRA}`, is in [the prompt](prompts/drafter.md).

## The reading list

*Refinement: add it when a run's tokens grow with the book (the [token log](../../templates/tokens.md) shows it), usually from the second volume.* "The drafts before it" and "the cards of everyone in it" grow with every chapter. Past the first volume, give each agent a list instead:

- **Build it by script:** `python3 tools/reading.py N --step drafter --digest story/volume/<volume>-digest.md > plan/tasks/<task>/reading-N.md`. It resolves every link in the chapter's outline and notes to its file, and to a line range where the link names a heading in a large file. It adds any card the outline names without linking, the sheets of the people it names, and the chapter before. For each critic, use the matching `--step` (facts, setup, procedures, habits, continuity), so each reads only its own share.
- **The knowledge in force:** where any head has a knowledge guard, `python3 tools/knowledge.py N --out plan/tasks/<task>/knowledge-N.md` writes what each head knows, believes wrongly and does not know at this chapter. It fills `{KNOWLEDGE}` for the drafter and every critic and the reviser. It is built from one guard per head, so it is needed from the first chapter, not only past the first volume.
- **Tell the agent:** "read these and nothing else, unless a fact you need is missing; then follow one link and say so in your report." A fact the list does not carry is a lookup for [the librarian](prompts/librarian.md), not a reason to open whole files.
- **The volume digest** stands in for the volume's earlier chapters ([the template](../../templates/volume-digest.md)). It holds what the pages have set: who has met whom, what each knows, what objects are where, the names and terms in use, the routines already shown in full, and the asks still open. A small agent writes one block per batch as the batch closes; the supervisor checks its quotes. A critic reads the digest and the chapter before, not the volume.
- **What it saves:** the cost of a run follows the chapter's length and the number of passes over it, not the reading around it. That is the point: the reading stops growing as the book does.

## What the drafter must not get

- **Later outlines.** Nothing past this chapter. A drafter who knows the payoff writes toward it, and the plant becomes a signpost.
- **Anything past the horizon.**
- **The outline's author-side lists** (reference detail, the truth behind a secret) as things to put on the page. The outline marks them; the drafter leaves them off.
- **The conversation** with the writer. The drafter is a fresh agent with a complete prompt.
- **The critics' prompts.** A drafter who writes to pass a critic writes to the critic.
- **The chapter's old draft, on a redraft.** A drafter given the draft it replaces keeps its sentences, and the old book comes back. It gets the cleaned outline ([outline clean](../outline-clean.md)), the voice files and the accepted volumes instead.

## The rules it works under

- Every settled beat in order. The proposal beats too, unless they contradict a settled one.
- **Lore stays in the notes.** A card holds far more than the scene needs. The page shows only what the narrator sees and what the scene calls for.
- **Where a beat cannot be written without a fact the notes lack, write around it and list it.** Do not invent a fact to fill a hole in the outline.
- **Small inventions are fine, and logged:** names of minor things, staging, sayings. They go on the Inventions list. The drafter does not check them; a separate run does ([the invention check](principles.md#the-invention-check)).
- Measure the texture with `tools/tells.py` and keep near the rulings' numbers. Run the banned list and fix every hit in narration before reporting.
- No notes, marks or comments inside the prose file. Title line: `# {TITLE} (draft N)`.
- **Run no git commands. Do not launch agents.** Write only the one prose file.

## The drafter's report

Short, ending with the **Inventions** list, in the form [the prompt](prompts/drafter.md) gives. The supervisor copies the report into the batch paper.

## Batches

- **Basic: one chapter at a time, in story order,** one fresh agent, so each drafter reads the finished draft of the chapter before.
- **Refinement: two or three chapters side by side,** in story order, one fresh agent each, at most two agents running at once. Drafters running side by side cannot see each other's new text. So each gets the outline (not the draft) of the chapter before if that chapter is in the same batch, and the continuity critic checks the seams afterward.
- **The main narrator's thread first.** Pieces in another voice (letters, interludes, other narrators) have their own register and come after, with their own `{EXTRA}` saying which rules of the voice sheet are the main narrator's alone and do not apply.

## Style samples

The writer's own pages set the voice. The intake lists candidates; the writer picks them in the interview: the two or three passages most like the writer at their best, not the most polished. Stage 03 copies them, unchanged, to `story/voice/samples/` (copies, with the source file and line). Every drafter reads them. Every critic is told: these are the writer's own lines; never flag a line because it resembles them.

When the writer's existing scenes are rewritten from new outlines, the samples stay as they were. They are the reference, not the book.

## Lessons the method learned

- **Side-by-side batches need the continuity critic.** Parallel drafters drift at the seams: a day counted twice, an object in two places. One chapter at a time, in order, does not.
- **Drafters do not invent staging for a device.** Extra machinery (pipes, gauges, drains) pushes a reader toward a picture the book never meant.
- **A drafted chapter with no key frame reads flat.** If the gate let one through, stop and write its brief.
- **A setting that works by its own rules needs a staging sheet.** A drafter left alone reaches for the stock picture: a smithy with a fire, a print shop that clatters. For a place that works by the setting's own rules, write one sheet (what stands where, what each tool does, what only the narrator sees) and give it to every drafter and reviser of the chapters set there. Walk the shop on paper with the writer before drafting: writers often know the trades. The [procedures critic](prompts/procedures.md) is the backstop.
- **Anyone in two chapters or more gets a sheet before drafting,** named or not. A drafter who meets the same unnamed clerk twice invents two clerks.
