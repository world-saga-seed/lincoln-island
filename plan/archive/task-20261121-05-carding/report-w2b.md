# Report, wave 2, role B (I.6 to I.9)

**Cards made (40).**
Places, full (8): the-dunes.md, the-grotto.md, the-reef-line.md, the-northern-shore.md, the-forest-marsh.md, the-bend.md, pacific-ocean.md, micronesian-archipelago.md.
Places, stubs (8): mendana-archipelago.md, pomotou.md, new-zealand.md, juan-fernandez.md, auckland-islands.md, the-pond.md, dead-wood-clearings.md, grotto-stream.md.
Things, full (8): burnt-linen.md, clubs.md, seaweed.md, shell-cups.md, footprints.md, pine-nuts.md, palms.md, firs.md.
Things, stubs (16): tetras-lines.md, dwarf-acacia.md, tetras-jelly.md, litter.md, maritime-pine.md, spilett-watch.md, smith-watch.md, salt.md, harbert-handkerchief.md, smith-shoes.md, pencroff-jacket.md, douglas-firs.md, fire-sticks.md, spark-pebbles.md, chemical-matches.md, signal-faggot.md.
Also: 8 lines added to world/things/tool-chain.md (burnt linen, clubs, tétras lines, tétras jelly, litter, seaweed bed, sticks of young fir, second raft).

**Cards extended (16).** Places: the-chimneys.md, the-islet.md, mercy-river.md, the-snow-capped-mountain.md, the-evergreen-forest.md, the-granite-wall.md, grande-vue-plateau.md, lincoln-island.md. Things: tinder.md, hearth.md, first-fire.md, firewood.md, raft-of-logs.md, pines.md, deodars.md, spilett-notebook.md. No line was deleted or reworded; only the Appears-in lines were rewritten to add chapters. The READMEs of world/places and world/things were rebuilt by `tools/cards.py build`.

**Renaming.** None. My chapters name nothing: the islet, the mountain, the bay and the plateau keep their descriptive files until the wave that reaches I.11 renames them.

**Crowd figures (no card).** Carolinas (North and South), Georgia, the Gulf of Mexico, Mexico (the route Smith reckons, I.9 ¶70, in the Pacific card); "l'Union" (I.9 ¶14); Asian shores (I.9 ¶18, in the seaweed card); the junipers (I.6 ¶37, in the forest card); the thicket where the capybara was met (I.9 ¶103); the companions' jackets laid over Smith (I.9 ¶17); the heap of dry moss and two sticks beside the Chimneys' hearth, none named. Not carded, for A: the couroucous strings (I.6 ¶35, I.7 ¶21, I.9 ¶15), the tétras, jacamar, capybara, mussels and pigeon eggs (animals). Not on the tool chain: the failed fire-sticks and spark pebbles (I.9), the signal faggot (I.7 ¶57), the strings of couroucous.

**The text's own disagreements put on Open lines.**
- the-grotto.md: distance from the coast, "à plus d’un mille de la côte" (I.8 ¶31) against Pencroff's "À un demi-mille environ" from the reefs (I.8 ¶64).
- the-grotto.md: distance from the Chimneys, "à six milles environ" (I.7 ¶81) against "À huit mille du premier campement" (I.7 ¶0) and "huit milles à franchir" (I.8 ¶86).
- pine-nuts.md: "pin pigeon" (I.9 ¶97) against "Le pin pignon" (I.9 ¶0).
- the-snow-capped-mountain.md: direction, north-west (I.3 ¶54) against "dans l’ouest" (I.9 ¶60).

**Questions for the author.**
1. Full card or stub? Three cards are full on my reading of "on a Clues section", which is a stretch, and may be overturned: footprints.md (the I.8 clue that it is evident Smith came alone rests on the prints), pine-nuts.md (kept full to hold the pin pigeon / pin pignon disagreement) and palms.md (the I.6 latitude clue). Recommendation: keep them full.
2. smith-shoes.md and the fire-sticks, spark-pebbles and chemical-matches are stubs (one chapter, no Clues line). The shoes carry the I.8 proof that the prints are Smith's, and that fact is on footprints.md, not on the stub. Recommendation: leave as stubs; the outline has the scene.
3. I joined the river's "coude" (I.6 ¶18, I.9 ¶82) to I.4 ¶29's sharp bend in the-bend.md, and the "cône central"/"montagne dans l’ouest" to the snow-capped mountain, each marked *(My reading, to confirm.)*. I did not join the "pointe de roc" smoke (I.6 ¶17) to anything. Recommendation: confirm both links.
4. The I.4 reefs on the-bay.md and the reef line of I.7 and I.8 may be one line; left apart, with an Open line. Recommendation: leave apart.
5. Open gaps now partly answered, left in place: the-chimneys.md "how many corridors or chambers", mercy-river.md "source or mouth" (I.6 ¶35 gives a surmised source). Recommendation: delete in a clean-up pass.
6. seaweed.md also holds the sargasses (I.9 ¶18) rather than a separate stub, since the text calls them algae of that kind.

**Slip.** I ran one read-only `git status` against the prompt, to see which files showed as changed. No git command changed anything.

**Checks.** `cards.py build` rebuilt both folders and `check` prints 0 card problems; `links.py` prints 0 broken. Every quote was checked in code against its cited paragraph before writing.

**Totals.** 40 cards made (16 places, 24 things; 16 of them full, 24 stubs), 16 extended, 151 facts added (75 on new cards, 76 on extended), 8 tool-chain lines, 5 Open entries added (4 on new cards, 1 on extended).
