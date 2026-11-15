# Outline clean: the old drafts out of the outlines before a redraft

*Refinement. Add it when outlines written before a restructure are about to be redrafted from.*

A consistency check reads outlines against outlines, so it cannot see old text inside them: beats lifted from a draft written before a restructure, and proposals older than the rulings around them. A redraft from such an outline blends the old book back in. This pass ages every beat before a full redraft, so the drafter renders only the current book.

**Grade.** A judgment, in two layers: the script finds, agents propose, the supervisor verifies, the writer decides the real choices. Agents edit no story file; their proposals go to the task's folder.

## The loop

1. **List the aged lines** by script: `python3 tools/aged.py story/outline/NNN*.md --cutoff YYYY-MM-DD --retired story/prose/NNN*.md --proposals --tsv plan/tasks/<task>/aged.tsv`. The cutoff is the day the current outline was accepted; the retired drafts are the ones being replaced. A line is flagged when it says it comes "from the draft", links a retired draft, carries only date marks and rulings older than the cutoff, or is a proposal with no date or ruling.
2. **Split the chapters into two ranges** and give each to one fresh agent, each with its named file list.
3. **Each agent rules every flagged line** in its range, one line each:
   - **keep:** it agrees with every current settled line; mark it current.
   - **rewrite:** give the new beat, with the rulings it now rests on.
   - **strike:** it is superseded; name what supersedes it.
   - **ask:** it is a real choice between settled lines; give a recommendation.

   It also lists any unflagged line it finds stale on the way.
4. **Verify** every rewrite and strike against the rulings it names (`grep -F` the quotes); drop what does not hold.
5. **Apply** the verified keeps, rewrites and strikes in place, superseded text deleted, not kept beside the new; put the asks to the writer, most severe first.
6. **Check:** links clean; the script again shows no from-draft or cites-retired line left unruled.
7. **Rerun the actor logs** for the horizon, if the book keeps them ([actor-log](actor-log.md#when-it-runs)): the clean changes the outlines, so the logs are stale until rerun, and drafting waits on them.

## The prompt

```text
You are cleaning a novel's chapter outlines before a full redraft, in the folder {REPO}.
Every file is read-only except your output file; run no git commands and launch no agents.
Read README.md and plan/README.md first (the marks: settled, proposal, reading). Your range:
{RANGE}; your files: {FILES}. The old drafts of these chapters were written before the
restructure and are out of date: do not read story/prose/ except to see what a flagged
line quotes. The flagged lines are in {TSV}.

For every flagged line in your range, against the current settled lines (the outline
itself, its notes, the arc outline, the ledger rows it cites in plan/settled/ledger/, and
the cards it links), rule one of: keep, rewrite, strike, ask. Give each ruling as one line:
the file and the line's first words; the ruling; for rewrite the new beat in the outline's
style, with the rulings it rests on; for strike what supersedes it; for ask the two sides
and your recommendation. Quote exactly. Add any unflagged line you find stale. Write only
{OUT}.
```

## Notes and cards

**The clean is not done until the notes and cards are clean too.** Character sheets, chapter notes and cards quote the old drafts as freely as the outlines did, and the drafters read them. So the same loop runs on them after the outlines: `python3 tools/aged.py story/notes/**/*.md world/**/*.md --retired story/prose/NNN*.md --tsv OUT` lists every line linking a retired draft; then two agents by file list, verify, apply, ask.

**The prompt, cards form.** The prompt above, with "chapter outlines" read as "notes and cards", and these rules added:

```text
Each flagged line links or quotes a retired draft. Rule it against the cleaned outlines and
the ledger: keep when what it says still agrees with the current outline (the link to the
draft is removed and the line stands on the outline or ruling instead, cited); rewrite
when the fact stands but the draft's detail does not; strike when the outline or a newer
ruling supersedes it; ask when two settled lines conflict. A draft's wording is never a
source: a quoted phrase the outline does not carry is struck, or marked as a proposal for
the redraft. Links to accepted prose stay. A card's "On the page" line cites the outline,
not the retired page.
```

## Lessons

- **The old book comes back through the notes, not only the outlines.** After the outlines were cleaned, the sheets and cards still quoted the retired drafts, and the drafters read them. Clean both before any drafter launches.
- **No drafter gets its chapter's old draft.** Give it the voice files and the accepted volumes instead ([the drafter](drafting/drafter.md#what-the-drafter-must-not-get)).
