# The interview script

*Ask in this order, a few at a time. Skip what the existing work already answers. Each question says why it is asked and where the answer lands. "Lands" means: a ledger row, plus the file named.*

## 1. The existing work

| Question | Why it is asked | Lands in |
|---|---|---|
| Which of these files are live, and which are old versions you have moved past? | The intake cannot tell; building on a dead draft wastes everything after it | `plan/interview.md`; old versions noted in the intake table |
| Which passages sound most like you? (offer the intake's candidates) | They become the style samples every drafter reads and every critic respects | the voice sheet's samples line |
| What in the existing work is fixed, and what is free to change? | Fixed points are key frames; free parts are where Claude may propose | the arc outline (frames marked settled) |
| Where the files disagree (show each pair), which is current? | Only the writer knows; the answer becomes one card line | the card for that fact |

## 2. Scope

| Question | Why it is asked | Lands in |
|---|---|---|
| How long, roughly? One book, or a series? | Sets the horizon size and how much machinery is worth it | `plan/roadmap.md`; `plan/state.md` targets |
| If a series: how many books, and does each close, or is it one story cut into volumes? | Decides whether every volume needs its own ending and its own recap | the arc outline; `plan/roadmap.md` |
| Will it be released all at once, or as a serial? At what pace? | A serial is judged chapter by chapter; it changes the interest check and the release plan | `plan/roadmap.md`; `workflows/publication.md` settings |
| What is the first horizon: where should the first outline stop and be drafted and read? | Outlining too far ahead breaks when drafting shifts the story | `CLAUDE.md` rule 8; `plan/roadmap.md` |

## 3. Direction

| Question | Why it is asked | Lands in |
|---|---|---|
| The premise in one breath? | A test of whether the shape is clear; the line heads the arc outline | the arc outline's head |
| How does it end? (Or: what must be true at the end?) | Every outline is checked against the ending; an open ending blocks only the stretches that lead to it | the arc outline, The ending |
| What must it never become? | Names the average answer the model will drift toward, so it can be refused | a settled decision file, "what it rejects" |
| What does the book promise its reader? | The promise is what the interest check guards and what a plot turn must keep | `plan/README.md` rules; the arc outline |
| What are the big secrets, and when should a careful reader be able to guess each? | Becomes the reveal ladder and the clue register | `plan/reread-hooks.md`; `workflows/reveal-pacing.md` scope |

## 4. Voice and point of view

| Question | Why it is asked | Lands in |
|---|---|---|
| Who tells it? First person, close third, several viewpoints? | The single biggest rule for every drafter and critic | the voice sheet, The rule |
| Past or present tense? Told as it happens, or from after? | "Told as it happens" bans hindsight lines; the critics need to know | the voice sheet |
| What does the narrator notice, and what bores them? | Attention sets the register: close detail where something holds them, a line where it does not | the voice sheet, The register |
| What words, phrases or ideas could the narrator never use? (period, place, age, world) | The first lines of the banned list | `story/voice/banned.txt` |
| Are there characters whose voice you already hear? Who? | Their sheets get a voice section first, from your words | the character sheets |
| Is there anything the page must never explain? | Keeps the mechanism on the notes' side of the line | the voice sheet; the mechanism critic's rules |

## 5. Pacing

| Question | Why it is asked | Lands in |
|---|---|---|
| Where are the quiet stretches, and do you want them? | Quiet is often the book's texture; the interest check must not flatten it | the arc outline, Density |
| What does each quiet stretch set up? | A lull that pays off later is kept; one that sets up nothing is a finding | the arc outline, Density; the clue register |
| What is the outside pressure in each stretch? | Stretches that score low usually lack outside pressure or a widening cast | the arc outline |
| How long should a chapter be, roughly? | A target, not a cap; it flags drift, never forces a cut | `plan/state.md` targets |

## 6. Audience

| Question | Why it is asked | Lands in |
|---|---|---|
| Who is it for? Age, and what else they read? | Sets the reader personas for the interest check, and the content line | `workflows/interest-check.md` personas; `plan/README.md` |
| Is there any content line (for age, for taste) the book keeps? | A guardrail every drafter reads | the voice sheet, or a settled decision file |

## 7. What you dislike

| Question | Why it is asked | Lands in |
|---|---|---|
| What in books like this makes you put them down? | Each dislike becomes a critic question or a banned pattern | `CLAUDE.md` About the writer; the critics' rules |
| What do you detest in prose you suspect a model wrote? | Seeds the tells list and the banned list | `story/voice/banned.txt`; `tools/tells.py` reading |

## 8. Reading roots

| Question | Why it is asked | Lands in |
|---|---|---|
| What books or kinds of story shaped how you think about this one? (by premise is fine if titles do not come) | When you ask "has this been done?", Claude can look in the right shelf; precedents by premise help name a half-remembered story | `CLAUDE.md` About the writer |
| Where does your own experience run deep (a trade, a place, a craft)? | Your calls there are taken as fact, and proposals are built around them | `CLAUDE.md` About the writer |

## 9. How you read

| Question | Why it is asked | Lands in |
|---|---|---|
| How do you want to read drafts: on screen, an ereader, as audio? | Sets up the ereader build and, if wanted, the voice render | `plan/roadmap.md`; `workflows/ereader.md` |
| Is anything hard for you when reading? (for example, unmarked jumps in time or point of view, long blocks of text) | A working preference becomes a page rule, such as "every chapter opens on a day" | the voice sheet; `CLAUDE.md` About the writer |
| How do you like questions put to you? | Some writers want options; some want one recommendation; some want to talk it through | `CLAUDE.md` About the writer |

## Closing the interview

1. Read back each section in three lines. Correct.
2. List the open questions. Each goes to `plan/state.md`, under "Questions held".
3. Propose the first horizon and the first wave of tasks (usually: set up plan, card the existing work, the checks). Wait for the writer's word.
