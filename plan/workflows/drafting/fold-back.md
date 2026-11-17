# Fold-back: the draft back into the outline and notes

*Refinement. Add this when a chapter will be redrafted or the writer's comments arrive.*

After a stretch is drafted and refined, each chapter's outline and notes are brought up to what the draft made, and every place the prose must change at the next drafting pass is listed in the chapter's notes. The writer's reading comments join the same list. The second drafting pass drafts from it. The prompt template is [prompts/fold-back.md](prompts/fold-back.md).

**Grade.** A judgment with a mechanical check: every quote in a Next pass list must resolve in the prose (`tools/quotes.py --backticks`), every link must resolve, and every added line must carry a mark. Whether a draft's choice stands is a story judgment, made overturnable.

## Two directions

- **The draft into the outline.** What the drafter chose and the critics kept (the batch paper's drafter reports, fixes that changed a beat, inventions that stood) goes into the outline beat it belongs to, in one line, marked *(Proposal, from the draft, NNNNN.)*. Outline text the draft and its batch settled otherwise is **deleted**, not struck. An open question in the notes the draft answered is replaced by the answer, marked *(Answered by the draft, NNNNN; overturnable.)*. **A choice that contradicts a settled line is never folded:** it is drift, and goes on the list below.
- **The notes into the prose.** Where the prose no longer matches the notes, cards or rulings, it goes on the chapter's **Next pass** list.

## The Next pass list

The last section of each chapter's notes file, `## Next pass`, headed by one italic line: *(Proposal, from the fold-back: where the prose changes at the next drafting pass. The writer's reading comments join this list.)* Each item:

> N. **kind.** `exact quote from the prose` (line L). What changes, in one line, never rewritten prose. Source: link. *(mark)*

The kinds:

- **drift:** the notes, a card or a ruling moved after the draft. Look hardest at what changed since the facts critic ran.
- **held:** a batch left the item for later.
- **beat:** an outline beat is missing, out of order or changed without the batch keeping it.
- **voice:** the default register buries what the narrator feels, or fails to show what holds them; or a conversation they are listening hard to gives only what was said, never how it was said (a pause, a voice gone careful, a word leaned on). At most eight a chapter, the strongest.
- **length:** the chapter is outside its notes' range (`wc -w`).
- **reading:** the writer's comments from the ereader read, added later.

The quote goes in backticks, since dialogue uses double quotes. Line numbers move when the prose is revised; the quote is what identifies the place.

## The loop

1. **Groups by batch.** One agent per drafting batch, editing only its chapters' outlines and notes. It never edits prose, cards, sheets, arc outlines or `plan/state.md`: it writes what those need to its report. At most two agents.
2. **Check each group as it lands:** every Next pass quote resolves (`python3 tools/quotes.py next-pass.md --in story/prose/NNNNN-*.md --backticks`, run on the `## Next pass` section copied to a scratch file, since `--backticks` checks every backticked span, commands included); links resolve; every added line carries a mark; read the outline diff for folded text that contradicts a settled line.
3. **Fold the reports.** Shared-file items go to the cards and sheets. Drift rows in `plan/state.md` are deleted where the current prose no longer has the quote, and carried as pointers where it does. Questions for the writer are deduplicated across groups and asked a few at a time, each with a recommendation.
4. **Later, the reading comments** are filed into the same lists as **reading** items.

## Reflow: the approved page back into its notes

*(Proposal: from one book's redraft test.)*

A page the writer has read and approved holds beats nothing written down holds. A drafter invented them, the writer kept them, and the fold-back carried only what the batch papers listed. A redraft from the outline cannot reproduce them, and in the test it didn't. So before an approved chapter is redrafted, reflow it.

1. **Trace the page** (a cheap finder, checked by script). Split the page into beats: a turn in a scene, a line of dialogue that changes something, an image used again later, a slip or a cover. Give each a quote and its place in the outline or notes: supported, partly, or absent. `tools/quotes.py` checks the quotes.
2. **Mark the strength.** A strength critic reads the page alone, never beside another draft, and marks its strongest and weakest beats with quotes. Run it on two models. A comparing reader is no use here: it praises or damns the same beat according to which draft it picked.
3. **Judge each absent or partly supported beat:**
   - **keep the words:** both critics marked it strong, or it is load-bearing. A beat is load-bearing if it carries a clue, plants something a later chapter pays off, or is a line later pages refer back to. Find these by the trace, the clue register and a grep of the later pages, never by taste.
   - **a proposal:** one critic marked it strong;
   - **stays in the draft:** weak or unmarked;
   - **drop:** it conflicts with a settled line, and goes on the Next pass list.
4. **Write it back.**
   - A beat whose words are kept goes into the notes with the exact quote, marked *(Reflowed: the approved page, NNNNN; keep the words.)*. The drafter's bundle gives it verbatim.
   - A proposal goes into the outline beat, marked *(Proposal: reflowed from the page, NNNNN.)*, with its words free.

   Choose a mark your book doesn't already use. If "kept" means held off the page in your notes, a "kept" beat meant for the page will collide with it.

**Revise approved chapters in place.** Where a card or the canon changed, revise the lines `tools/uses.py` lists. Redraft only where the outline itself changed, and only after reflow. A redraft replaces the approved page only if it passes the compare gate ([reader tests](../reader-tests.md#comparing-two-drafts)).

## The second pass

The next drafting pass gives the drafter the chapter's outline, notes and **Next pass list**, and the previous draft as reference for what to keep. The list is the brief for what changes. Everything not on it should survive, so the second-pass critics compare against the first draft as well as the notes.
