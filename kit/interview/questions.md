# The interview script

*Sections 1 to 9 are the first interview, in this order, a few questions at a time. Section 10 (the world) and 12 (the cast's voices) follow once the existing work is carded, so the questions can start from the cards; 11 (ambiance) goes with 10; 13 (assumed elements) runs after the carding and again before each horizon is outlined. Ask in this order, a few at a time. Skip what the existing work already answers. Each question says why it is asked and where the answer lands. "Lands" means: a ledger row, plus the file named.*

## 1. The existing work

| Question | Why it is asked | Lands in |
|---|---|---|
| Which of these files are live, and which are old versions you have moved past? | The intake cannot tell; building on a dead draft wastes everything after it | `plan/interview.md`; old versions noted in the intake table |
| Which passages sound most like you? (offer the intake's candidates) | They become the style samples every drafter reads and every critic respects | the voice sheet's samples line; stage 03 copies them to `story/voice/samples/` |
| What in the existing work is fixed, and what is free to change? | Fixed points are key frames; free parts are where Claude may propose | the arc outline (frames marked settled) |
| Where the files disagree (show each pair), which is current? | Only the writer knows; the answer becomes one card line | the card for that fact |

## 2. Scope

| Question | Why it is asked | Lands in |
|---|---|---|
| How long, roughly? One book, or a series? | Sets the horizon size and how much machinery is worth it | `plan/roadmap.md`; `plan/state.md` targets |
| If a series: how many books, and does each close, or is it one story cut into volumes? | Decides whether every volume needs its own ending and its own recap | the arc outline; `plan/roadmap.md` |
| Will it be released all at once, or as a serial? At what pace? | A serial is judged chapter by chapter; it changes the interest check and the release plan | `plan/roadmap.md`; `plan/workflows/publication.md` settings |
| What is the first horizon: where should the first outline stop and be drafted and read? | Outlining too far ahead breaks when drafting shifts the story | `CLAUDE.md` rule 8; `plan/roadmap.md` |

## 3. Direction

| Question | Why it is asked | Lands in |
|---|---|---|
| The premise in one breath? | A test of whether the shape is clear; the line heads the arc outline | the arc outline's head |
| How does it end? (Or: what must be true at the end?) | Every outline is checked against the ending; an open ending blocks only the stretches that lead to it | the arc outline, The ending |
| What must it never become? | Names the average answer the model will drift toward, so it can be refused | a settled decision file, "what it rejects" |
| What does the book promise its reader? | The promise is what the interest check guards and what a plot turn must keep | `plan/README.md` rules; the arc outline |
| What are the big secrets, and when should a careful reader be able to guess each? | Becomes the reveal ladder and the clue register | `plan/reread-hooks.md`; `plan/workflows/reveal-pacing.md` |

## 4. Voice and point of view

| Question | Why it is asked | Lands in |
|---|---|---|
| Who tells it? First person, close third, several viewpoints? | The single biggest rule for every drafter and critic | the voice sheet, The rule |
| Past or present tense? Told as it happens, or from after? | "Told as it happens" bans hindsight lines; the critics need to know | the voice sheet |
| What does the narrator notice, and what bores them? | Attention sets the register: close detail where something holds them, a line where it does not | the voice sheet, The register |
| What words, phrases or ideas could the narrator never use? (period, place, age, world) | The first lines of the banned list | `story/voice/banned.txt` |
| Are there characters whose voice you already hear? Who? | Their sheets get a voice section first, from your words | the character sheets |
| Is there anything the page must never explain? | Keeps the mechanism on the notes' side of the line | the voice sheet; question 2 (mechanism) of the voice-and-mechanism critic, `plan/workflows/drafting/prompts/voice-mechanism.md` |

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
| Who is it for? Age, and what else they read? | Sets the reader personas for the interest check, and the content line | `plan/workflows/interest-check.md` personas; `plan/README.md` |
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
| How do you want to read drafts: on screen, an ereader, as audio? | Sets up the ereader build and, if wanted, the voice render | `plan/roadmap.md`; `plan/workflows/ereader.md` |
| Would you comment from your phone as you read (a Remote Control session), or highlight on the device? | Sets up the read: comments filed as they come, or exported after | `plan/workflows/ereader.md`, The read |
| Is anything hard for you when reading? (for example, unmarked jumps in time or point of view, long blocks of text) | A working preference becomes a page rule, such as "every chapter opens on a day" | the voice sheet; `CLAUDE.md` About the writer |
| How do you like questions put to you? | Some writers want options; some want one recommendation; some want to talk it through | `CLAUDE.md` About the writer |

## 10. The world

*Ask once the existing work is carded (stage 04), when the cards show what is already written. Skip it for a book set in the reader's own world, except for whatever the book changes.*

| Question | Why it is asked | Lands in |
|---|---|---|
| What is different here from the reader's world, and what follows from it? | Each difference is a rule with consequences; the consequences are where the world gets its depth and where drift begins | a rules card (`world/rules/`, one card per rule), each consequence on it |
| Why has the world settled the way it has? Why does nobody fix the obvious problem? | A world that stands still needs a reason that makes standing still the sensible choice, or it reads as everyone being foolish | the rules card; a settled decision file if it binds many cards |
| How do people make a living, and what is scarce? What is cheap that we find dear, and dear that we find cheap? | Economy and ecology tie together; prices and scarcities give every scene its ordinary details | `world/` cards for the trades and goods; the daily-life study |
| What is dangerous, and how do ordinary people live with it? | Danger handled by routine is the setting's texture; danger met fresh every time reads as a game | the rules card; the cards of the dangers |
| What do you know about the world that the page never says? | The truth beneath is kept on the notes' side of the line; drafters must not leak it | a writer-side card marked never on the page; the voice sheet's "never explain" |
| Which of your world's pieces come from somewhere you'd rather not show (another book, a game, a real place)? | Borrowed pieces need their own causes in this world, so nothing reads as lifted | the card, with its cause; the source stays writer-side |

## 11. Ambiance

| Question | Why it is asked | Lands in |
|---|---|---|
| What does an ordinary day feel like here: the light, the weather, the smells, the sounds, the cold? | Drafters fill silence with the stock picture; a palette written once gives every scene its own | the voice sheet, The register; the place card's **On the page** line |
| How have the conditions shaped the people: their houses, clothes, food, habits, manners? | People shaped by their environment are what make a setting lived in, not described | the place and people cards; the daily-life study |
| Is there a film, a painter or a book whose feel is close? (by premise is fine) | A precedent says in one line what a page of description cannot | `CLAUDE.md` About the writer; the voice sheet |
| Where should the book feel warm, and where cold or strange? | Ambiance is not even: it gathers where the narrator looks hard | the arc outline, Density |

## 12. The cast's voices

| Question | Why it is asked | Lands in |
|---|---|---|
| For each person who recurs: who are they, beyond their job? What do they want, fear, hide, love? | A voice built from a role (the gruff guard, the kind teacher) is a stock character; one built from the whole person is not | the character sheet, Who they are; What they want, and what they fear |
| How do they talk: long or short, plain or ornate, what they never say, what they say too often? | Drafters copy each other's speech; a sheet with the person's own speech stops it | the character sheet, Voice |
| What do they do with their hands, from their life and trade? | Habits from the work ground a character on the page; a habit borrowed from another character is a finding | the character sheet, Habits |
| Who else recurs, even unnamed (a clerk, a gatekeeper, a neighbor)? | Anyone in two chapters or more gets a sheet before drafting, or drafters invent a new one each time | a sheet for each |
| Are any two of them told together (a pair, a family, a rivalry)? | A pair is voiced together, so the contrast holds | both sheets, cross-linked |

## 13. Assumed elements

*Run after the carding (stage 04) and again before each horizon is outlined. Claude goes first: it reads the cards and outlines and lists what they take for granted.*

| Question | Why it is asked | Lands in |
|---|---|---|
| (Claude lists) Where do the cards assume something from the reader's world that this world may not share: money, time, distance, families, law, religion, food, what children may do? | Each unstated default is a place the model fills with its own world | the rule's card, or a ledger row that the default holds |
| (Claude lists) Which things does every scene use that no card describes: how people travel, light a room, pay, write, get water? | The things nobody thought to write down are the ones drafters invent differently every time | a card for each, from the writer's answer |
| (Claude lists) Which beats depend on someone knowing something, with no line saying how they learned it? | Assumed knowledge is the commonest slip in an outline | the outline, a beat that shows it; or the actor log |
| What do you see in these scenes that you have never written down? | A long-held story has answers the writer has not said; this is where they come out | the cards and outlines they touch |

## Closing the interview

1. Read back each section in three lines. Correct.
2. List the open questions. Each goes to `plan/state.md`, under "Questions held".
3. Propose the first horizon and the first wave of tasks (usually: set up plan, card the existing work, the checks). Wait for the writer's word.
