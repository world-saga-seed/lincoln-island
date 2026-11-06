# Distill: one version of each card

*Refinement. Add this when a card collects restatements.*

A card holds one tight version of each concept. The versions it grew through are in git. Run this on any card that has collected restatements, revision notes or quoted discussion; and on every card a task touched, before the task closes.

## Per card

1. **The head stays** (lines 1 to 5: name and what it is, the summary, the keywords). The summary may be tightened, never given a new fact. Then a blank line, `*(Distilled from <commit>.)*`, a blank line, the body.
2. **Each concept once.** Where a point is stated, restated in a quote, and again in a reading, keep one sentence in the card's own voice, with the link to where it came from.
3. **Rulings, not words.** Remove the writer's quoted discussion words. If the line already states what the quote says, delete the quote; if the quote holds something the line does not, write it into the line as a plain sentence, no new content. Keep quotes of the page (drafted prose, in-world speech) where the wording is the point.
4. **One mark per point,** the strongest that applies. A ledger ID is kept exactly. Drop revision chatter inside marks ("first marked…", "revised by…").
5. **Drop the empty and the spent:** "none recorded" fields, revision notes, reading chains, a reading a later ruling answers.
6. **Readings still open stay,** as one *(My reading, to confirm.)* sentence, or under **Open**.
7. **Two versions that disagree:** the ledger-marked or later one wins; if neither wins, keep both under Open and log the pair. Never resolve a contradiction silently.
8. **Gaps:** fill one only where the card's own Open asks a question its linked lore answers outright, marked *(Resolved by judgment, overturnable.)*. No new names, numbers or relations.
9. **Keep what links in:** every heading other files link to stays.
10. **Tight:** every word is read by every agent that opens the card.

## Run

- At most two agents, each with a fixed list of cards. Each logs contradictions kept, gaps filled and what it could not place.
- **Compare by script against the commit:** the head and the distilled line present; every ledger ID kept (`grep -o 'R[0-9]\{4\}-[0-9]*'` before and after); size before and after. Then `tools/cards.py check` and `tools/links.py`.
- The supervisor reads a sample of changed cards against `git show <commit>:<card>`: no ruling lost, no fact added.
- A card that reads wrong to the writer later is redrafted from the writer's reason, not reverted.

## Lessons

- **Agents merge and reword marks freely.** Count marks by ID against the commit; the few that moved show at once.
- **Agents carry task papers forward.** Grep each batch for citations into `plan/tasks/`.
