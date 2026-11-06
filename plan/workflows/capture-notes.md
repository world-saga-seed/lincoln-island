# Capture notes: land an outside document before it is removed

*Refinement. Add this when the writer brings an outside document.*

The writer often brings material from elsewhere: notes from another chat, a page of ideas from a notebook, an old plan. Before such a document is set aside, every item in it is put on a ledger: **captured** (where it landed), **rejected** (by the writer's word or a settled line), or **open**.

**Grade.** Mechanical for the quotes (each landing quote resolves); a judgment for what counts as one item and whether a landing says the same thing.

**Relayed notes reword the lore, and can swap a pair** (which of two clocks is which; who sent whom). A different wording of the same idea is a restatement, not a conflict. A swapped pair is a slip unless the document gives a reason. Canon wins on a slip; note where the new wording is clearer.

## The loop

1. **Ledger** (one agent per document or half, read-only, [prompt](#prompt)).
2. **Merge:** the open items as questions in batches of five, recommendation first; the rest counted.
3. **Settle** the open items with the writer: land each, or reject it.
4. **Remove** the document only when its ledger has no open row, and only at the writer's word.

## Prompt

> You are checking whether a document has been fully captured in the notes of a novel, in the folder {REPO}. Every file is read-only except your report, {REPORT}. Run no git commands; do not launch agents. Read `README.md` and `plan/README.md` (the marks). Your document: {DOC}. Break it into items: one claim, rule, beat or direction each. For each item, search `world/`, `story/` and `plan/settled/` and decide: **captured** (give `file:line` and a short exact quote; note any correction); **rejected** (quote the ruling or line that replaces it); **open** (not landed, not refused). An item landed only as a proposal or reading is captured, "as proposal". Where the notes say something different, canon wins: the item is captured-corrected or rejected, not open. Write one table (item, the document's line, the item in a few words, verdict, `file:line` and quote, note), then a summary under 150 words: counts by verdict, and every open item in one line.
