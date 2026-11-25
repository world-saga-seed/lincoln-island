# Publication: before a volume goes to readers

*Refinement. Add this when a volume is about to be released (once per volume).*

## Purpose and when

Checks run once per volume, before release, after the writer's read is folded back and the volume is final. Not part of drafting.

**First, the paths.** Run `python3 tools/check_paths.py`; it must print `clean`. An absolute local path in a saved prompt or report names the machine and the person who ran the work, and it survives in the history once committed, so clean it before the repository is made public (R1124-04).

## 1. The famous-phrase check

A model can, rarely, reproduce a memorable published line nearly word for word. A narrow, period- or world-bound narrator is low risk; the risk sits wherever outside text can come in: songs, sayings, prayers, quoted verse, a character from our world quoting it.

1. **Candidates (script):** rank each chapter's sentences for quotability: short present-tense generalizations, figurative lines, kicker paragraphs, rare five-word runs. Keep the top 10 to 15 per chapter. **Always include** the high-risk lines: anything quoted from songs, sayings, scripture or verse, and any narrator whose register is not the main one's.
2. **A first look** (one read-only agent): flags candidates that sound like a known line and names the source it suspects. A filter only.
3. **The judge:** an exact-phrase web search on every flagged line and the top candidates, and on each line's most distinctive run of eight or more words.
4. **Severity:** **break**: ten or more words verbatim from a copyrighted work, or any song lyric. **Weak:** a close paraphrase of a famous line that is not a deliberate allusion. **Fine:** common idioms and proverbs; public-domain text. Deliberate allusions are listed by the writer and pass.
5. **Report** each match with the quote, the source, the severity and a rewrite; record the cleared lines so a later volume does not search them again.

## 2. The writer's-voice clarity check

Anything in the writer's own voice (front matter, an afterword, a blurb, a note to readers) is checked by a **cold reader** before it is final. The critics judge the narrator; this is the writer's plain voice for a reader who knows nothing.

1. **One agent** gets only the text and is told: "You are an intelligent reader who has never heard of this book."
2. It lists, quoting each: every pronoun or "this", "that", "it" whose referent is unclear; every term or name the text assumes; every sentence that needs the writer's own logic to follow, said back as what it seems to mean; any paragraph that circles back.
3. **The rewrite stays the writer's.** Claude proposes the smallest fix for each (a noun for the pronoun, a gloss or a cut for the term); the writer settles; the writer's words are kept wherever they are clear.
4. **Run it again** on the revision, until the cold reader's account matches what the writer meant.

## 3. The release plan (for a serial)

If the book is released in parts: a pattern of drops (a launch bunch, then a steady rate, faster toward a volume's end), published to readers so a change of pace reads as design. A secondary piece placed in a slot goes out in that slot; it is never moved for the schedule.

## 4. The retailer's questions

If a retailer asks how the book was made, the answer agrees with the front matter.

## Outputs

- The famous-phrase report with cleared lines; the final front matter; the release plan.

## Lessons (Lincoln Island, 2026-11-21)

- **Run the overlap against the public-domain translations too.** Renders "in one translator's voice" shared 29% of their words, in runs of eight or more, with another translation that no agent was given (White's own text: 6%). The models remembered it. The figure goes in the front matter, said plainly.
- **Check the front matter's credits against the ledger** with a fresh critic. A foreword said two plot turns came from a reading they did not come from; who made what is a fact like any other.
- **The cold reader's smallest fixes are glosses at first use:** the method, the patch, the added chapter's label. Its "what I understood" paragraph is the test that the page works.
