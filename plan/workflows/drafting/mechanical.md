# Mechanical checks: the greps and scripts

*Basic.*

Run these on every draft before any critic sees it. They are cheap, they give verdicts nobody argues with, and they clear away what a critic would otherwise spend its attention on.

**A hit is a candidate, not a failure.** A grep cannot tell narration from a line of dialogue, or a lamp in a memory from a lamp in the room. Every hit is read in context, by the supervisor, before it becomes a fix.

## The checks

| Check | Command | What a hit means |
|---|---|---|
| Banned words and phrases | `python3 tools/tells.py story/prose/NNNNN-*.md --banned story/voice/banned.txt` | A word the narrator never uses. Fix in narration; in dialogue, read whether the speaker would say it (`--all-text` scans dialogue too) |
| Texture numbers | `python3 tools/tells.py story/prose/NNNNN-*.md story/voice/samples/*.md` | A chapter well outside the samples' range on a measure: a candidate for the voice critic. A **knot** line under it is a sentence of 35 words or more with a semicolon: the reviser splits any that runs two main clauses through one |
| Setting words first on the page (per chapter, Refinement) | `python3 tools/firstuse.py story/prose/*.md --batch 1` | A word the cards use that no earlier page has: the setup critic's `{FIRSTUSE}` |
| Links | `python3 tools/links.py` | A note or card points at nothing |
| Cards in form | `python3 tools/cards.py check` | A card head out of form, or an index stale |
| Repeated phrases (per batch) | `python3 tools/repeats.py story/prose/0*.md --min-files 3 --narration` | A phrase the reader meets chapter after chapter |
| Your own rules | one grep per rule that has one (below) | A rule broken on the page |

## Reading the texture numbers

`tells.py` gives, per file: narration words; "the way you / the way a" similes per 1,000 words; "as if" per 1,000; "and" per sentence; negations per 1,000; median and spread of sentence length; short and long sentence shares; and **button%**, the share of paragraphs that end on a sentence of five words or fewer.

These are the rhythms that give model prose away. A reader who knows model fiction spots it by:

- the same simile frame again and again ("the way a dog shakes off water");
- sentences chained with "and" through three or more clauses;
- paragraphs that report what did not happen (three or more negations);
- the short kicker paragraph after every beat ("That was all.");
- the flattening of sentence length (a low spread).

**There is no universal good value.** Run `tells.py` on the writer's style samples and on the writer's existing chapters. Their range is the target. Write it into [rulings.md](rulings.md#texture). Flag a chapter well above the range, and well below it too: a chapter chopped to pass the caps (every join cut) reads worse than one slightly over.

**Density, never a single use.** One "the way she had" is the writer's voice. Five in a chapter is the machine's. A single hit is never a finding.

## Add a grep for every rule that has one

When a rule in the rulings turns out to have a mechanical form, add a row. Examples:

```bash
f=story/prose/00400-*.md
# Hindsight (a told-as-it-happens narrator)
grep -niE "later I (learned|knew|found)|I never saw (him|her|them) again|for what came after|would (later|one day)" "$f"
# British spellings, if the book is American
grep -nwE 'colour|grey|recognise|realise|favour|centre|metre|travell(ing|ed|er)' "$f"
# Contractions in narration (lines with no quotation mark: a rough cut)
grep -niE "\b([a-z]+n't|[a-z]+'(re|ll|ve|d|m))\b" "$f" | grep -v '"'
# Negation then correction: "It was not X. It was Y." / "not X but Y"
grep -nE "\b(was|is) not [^.]{1,40}\. [A-Z]|\bnot [a-z]+ but\b" "$f"
```

## First appearances

A name on the page before the chapter where the story first meets it is a slip or a leak. Each card's **Appears in** line lists its chapters. For each card name, grep the drafted chapters before the first one listed:

```bash
grep -ln "Hollis" story/prose/00[1-5]*.md   # the inspector's card says: appears from 00600
```

A hit is either the page too early or the card's list out of date. Read it: a common word used in another sense is no finding.

## Plant a case first

**A check is trusted only after it has caught a planted case,** as a critic is calibrated on planted faults. A grep that has never matched a planted line proves nothing when it finds nothing. Before relying on a new rule's grep, put one line that breaks it in a scratch copy, and see the grep find it. The same goes for the banned list: add a test word, run it, remove it.

## Volume checks before the batch critics

*Refinement: add them from the second batch of a volume.* A batch critic sees two or three chapters, so it cannot count what builds up across a volume: a detail shown in full at every appearance, a description repeated near word for word, a device so rare in one volume that it reads as a slip. Run these on the volume so far before the batch critics, and paste each into its critic's prompt:

| Check | Command | Goes to |
|---|---|---|
| Refrains | `python3 tools/refrains.py story/prose/<volume's chapters so far> --list story/voice/refrains.txt --batch K` | the habits critic's `{REFRAINS}` |
| Sound spans, if the book writes sounds the narrator cannot spell | `python3 tools/sounds.py story/prose/*.md --batch K --volume V --forbid "<symbols>"` | the voice critic's `{SOUNDS}` |
| Routines shown in full, open asks | the digest's Standing lines, brought up to the batch before ([the digest](../../templates/volume-digest.md)) | the procedures critic's and continuity critic's `{DIGEST}` |

- **Refrains list.** Start `story/voice/refrains.txt` from [the template](../../templates/refrains.txt). Add every refrain a critic, reader or the writer names, so the next count catches it for free. The script flags a refrain shown more than 8 times in a volume or more than 3 in a chapter. A refrain the writer keeps on purpose past the count goes in the digest's "Refrains, full showings kept" line, and the critic leaves it alone.
- **Sound spans.** Write the convention into the voice sheet first: who may say a sound, when it turns to italics and then to plain words, and which accent it is transcribed in. Mixed accents in a transcription are an easy slip for a model.

Across a drafted volume, for the register pass ([register-pass.md](register-pass.md)), add:

- `tools/repeats.py` over the whole volume, narration only;
- the first-appearance greps for every card;
- `tools/links.py` and `tools/cards.py check` at 0.

## Log

Write each chapter's numbers into the batch paper: the texture line from `tells.py`, the banned hits found and fixed, any rule grep's hits and what was done. The register pass and the second drafting pass compare against these.
