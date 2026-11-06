# Draft cards: card what the drafters made up

*Refinement. Add this when a second chapter meets people a drafter made up.*

After each drafting batch's fixes, agents read the drafted prose and card every person, object and place a drafter made up, so the next drafter meets the same clerk, the same counter and the same stair.

**Grade.** Mechanical for the quotes; a judgment for what counts as invented. A drafted fact is a proposal until the writer settles it: *(Proposal, from the draft, NNNNN.)* with the quote. A later drafter follows it; the writer can strike it, and then the prose is fixed to match.

**The threshold.** A person gets a card if the prose names them, gives them a line, or gives them a detail a later scene could contradict. Crowd figures stay off. A thing gets one if it has a detail beyond its plain name. A place gets one if it has a layout, contents or a route.

## The loop

1. **Extract** (agents of about 15,000 words of prose each, read-only): every person, object and place, with its exact quote, chapter and line, and its status: **carded** (give the card), **noted** (the notes name it, no card), or **invented** (grep the notes for the name and a key word first). For carded and noted: what the prose adds. Contradictions with a card in their own list, both sides quoted. Pairs that may be one thing under two descriptions.
2. **Check the quotes:** `python3 tools/quotes.py <extract> --in story/prose/*.md --backticks`.
3. **Merge** (one agent): one row per thing across the extracts, each with its action: new card, add to a card, a sheet item for the writer, or none. The supervisor resolves the same-thing calls before the writers run. Where an outline line marks the fact settled, the merge carries that mark, not the draft's.
4. **Write** (one agent per kind, at most two at once): new cards in the form, drafted details added to existing cards, `tools/cards.py build` for the indexes.
5. **Check:** quotes on every card touched; `tools/links.py` at 0; `tools/cards.py check`.
6. **Review** (a stronger model): nothing on a card the prose or notes do not say; marks right; no card for a crowd figure.

## Lessons

- **Settled lines get lost between the extract and the card,** so the merge lists a fact's settled line beside it, and writers check the outline themselves.
