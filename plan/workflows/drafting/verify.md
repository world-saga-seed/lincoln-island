# Verify, merge, dispose

*Basic.*

Before the writer or the reviser sees anything, every finding is checked mechanically. Then the findings are merged into one list in text order, and each gets a disposition.

## Verify

For every critic report:

1. **The quote exists.** Run `python3 tools/quotes.py <report> --in <the chapter file>`. A quote that does not resolve is dropped. Count the drops per critic: a critic that drops often is inventing, and its precision goes down in the calibration table.
   - Quotes from a chapter that has since been changed (a facts fix applied before the voice critic read it) are checked against the snapshot the critic read, and then looked for in the current file.
2. **The rule exists.** The cited heading is in the cited file. A finding that cites a rule nobody wrote is dropped.
3. **The quote is not the writer's.** `grep -F` each voice finding's quote in the style samples. A hit is dropped: the samples are the reference.
4. **The finding is not a clue.** Check each quote against the clue register and the chapter's clue notes. A finding that asks to cut or reword a clue is kept as a finding but its direction is changed: the clue stays, the passage around it may change.
5. **The finding survives a fair reading.** The supervisor reads the line in context. A line of dialogue flagged as narration, or a phrase used in another sense, is dropped with a note.

## Merge

- **One list per batch,** in text order (chapter, then line).
- **Findings on the same quote from different critics become one,** listing each critic.
- **Duplicates across chapters** (the same tic in three chapters) become one finding with every location, because the fix is one decision.

## Dispositions

Every verified finding gets exactly one:

| Disposition | When | Goes to |
|---|---|---|
| **Fix** | a break, or a weak finding with a clear fix that touches no settled line | the reviser's list |
| **Fix now** | a mechanical fix (a banned word, a spelling, a number against a card) | applied by the supervisor at once, logged |
| **Hold** | right, but the fix needs a later chapter, a card change, or the next pass | the chapter's Next pass list, with why |
| **To the writer** | it touches a settled line or a key frame, or two settled lines conflict | the next batch of questions, with a recommendation |
| **Keep** | taste, or the line is the writer's voice, or the line is a clue | logged with the reason; nothing changes |
| **Resolved by judgment** | the writer asked Claude to decide | applied, marked overturnable in the paper |

**Resolve on story judgment,** checked against the notes. Each judgment is marked overturnable in the batch paper, so the writer can reverse it.

## The batch paper

One file per batch in the task's folder: `batch-<first>-<last>.md`. It holds, in order:

1. the drafters' reports (choices, inventions, gaps);
2. the mechanical results per chapter;
3. each critic's run: prompt version, chapter and its hash, findings raw and verified, drops;
4. the merged list with dispositions;
5. **To the reviser:** the findings marked Fix, with their directions;
6. **To the writer:** the questions, each with context and a recommendation;
7. the reviser's report and the re-check;
8. the inventions, and the invention check's verdicts.

This paper is what the fold-back and the next drafting pass read. Write it as you go.
