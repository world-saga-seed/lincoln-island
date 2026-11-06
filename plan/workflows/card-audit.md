# Card audit: size, common causes, and lore left outside the cards

*Refinement. Add this when cards pass about 1,500 words.*

Audits the cards on three counts: which are too long and should split; which causes several cards share and want one home; and which settled lore lives only in outlines, notes or task papers and belongs on a card.

**Grade.** Mechanical for the sizes and the candidates; a judgment for the rest. The audit proposes; it edits no card. The writer settles; then moves run verbatim ([restructure](restructure.md)).

## Thresholds

A card over about 1,500 words, a topic file over about 5,000, or any section over about 1,500 is reviewed for a split (sizes from another book: set your own). A split is proposed only where the text holds two topics each looked up on its own.

## The loop

1. **Inventory.** Words by section for every file in `world/`:
   ```bash
   for f in $(find world -name '*.md'); do echo "$(wc -w < $f) $f"; done | sort -rn | head -30
   ```
   And the candidates: every *(Settled …)* line in `story/` whose ruling no card in `world/` states (grep each ledger ID in `world/`).
2. **Audit** (agents by group of cards, read-only, at most two): **splits** (the new files, which headings go where, words each; or "keep" and why); **common causes** (each mechanism two or more cards lean on: its home, or "no home"; every place that states it without linking the home; any place that states it differently, both quoted); **overfill** (scene detail on a card; a rule restated at length when its home is another card).
3. **Sort the candidates:** each is **lore** (which card), **carried** (already on a card in other words; quote it), **story** (a beat or page rule; no action), or **mixed** (split it).
4. **Merge** into one report with recommendations; questions to the writer in batches of five, most consequential first.
5. **Settle, then move and link.** `tools/links.py` at its baseline; `tools/cards.py build`. A card too long to read whole gets an **At a glance** index (`kit/method/cards.md`).
