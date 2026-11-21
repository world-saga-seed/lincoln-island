# Wave 4, role B (I.15 to I.18): report

## Cards made (31; 16 are stubs)

Full cards, places: `places/the-old-outlet.md`, `places/the-well.md`, `places/the-new-fall.md`, `places/lake-east-bank.md`, `places/lake-south-beach.md`.
Full cards, things: `things/seal-bellows.md`, `things/iron.md`, `things/steel.md`, `things/iron-tools.md`, `things/iron-shod-spears.md`, `things/fibre-rope.md`, `things/refractory-pottery.md`, `things/nitro-glycerine.md`, `things/nitric-acid.md`, `things/briquet.md`.
Stubs: `places/the-talus.md`, `places/the-upper-cave.md`, `things/the-branch-hut.md`, `things/granite-anvil.md`, `things/dragon-trees.md`, `things/the-pyrite-heap.md`, `things/soda.md`, `things/glycerine.md`, `things/soap.md`, `things/dugong-fat.md`, `things/iron-sulphate.md`, `things/sulphate-furnace.md`, `things/sulphuric-acid.md`, `things/mine-hole.md`, `things/firing-device.md`, `things/torches.md`.

## Cards extended (26)

Places: `ilot-du-salut`, `the-channel`, `cap-mandibule-sud`, `golfe-du-requin`, `the-dunes`, `pomotou`, `pacific-ocean`, `jacamar-wood`, `red-creek`, `mont-franklin`, `lake-grant`, `grande-vue-plateau`, `mercy-river`, `the-granite-wall`, `the-chimneys`, `lincoln-island`, `granite-house`.
Things: `iron-ore`, `coal`, `pyrite`, `saltpetre`, `hurdle`, `seaweed`, `knife-blades`, `pottery`, `guns`.
Also `things/tool-chain.md`: 23 lines added, I.15 to I.18, in book order.
`world/*/README.md` tables rebuilt with `cards.py build` (all four folders, since the tool does them together).

Pruned (R1121-06): `things/knife-blades.md`, 3 lines (Smith's eye lit up at the dog; "here are two knives, Pencroff"; the sailor's two cheers), all I.13 scene logs, on no Clues list I could see (I read the notes of I.10 to I.13 for those words). No other card needed pruning that I could tell; "when in doubt, keep".
Renames: none (I.15 to I.18 give no new name to a described subject; "Granite-house" was already a card, and I.18 names it).
One head edit: `places/granite-house.md`'s summary said "Named only in the last chapter", now false; I changed it to say it is named in I.18 (rule 9). Its Open line is untouched, though I.18 partly answers it (where, how big, how the well opens).

## Crowd figures (no card)

The basin of water for the iron sulphate (I.17 ¶50); the plain of sand under the talus (I.16 ¶23); the "forests of the south" (I.16 ¶29); Sicily and Greece (I.16 ¶1, a climate comparison, carded on the island); Corsica (I.15 ¶41), Sweden and Norway (I.15 ¶9), the United Kingdom (I.15 ¶9), Bohemia and Nordhausen (I.17 ¶52), New South Wales (I.16 ¶29), Malaysia (I.17 ¶2), London (I.18 n1), "Tubal-Cain" (I.15 ¶42); dynamite and fulminate (named only as not made); the thermometer (I.16 ¶1).
Also not carded: the coot, kangaroos, boars, sloth and snake (animals are A's).

## The text's own disagreements put on Open lines

- `things/iron-ore.md`: the deposits "in the north-west part of the island" (I.15 ¶7) against "at the foot of the north-east spurs of Mount Franklin" (¶31).
- `things/coal.md`: the coal "towards the mouth of the Red Creek" (I.13 ¶46) against the coal "not far" from ore found "almost at the very sources of the creek" (I.15 ¶41, ¶43).
- `places/lake-grant.md`: the lake to fall by "trois pieds" (I.17 ¶17) against "deux pieds, au moins" (I.18 ¶3).
- `places/lake-south-beach.md`: "angle sud" (I.16 ¶63), "pointe sud" (I.17 ¶2), "angle sud-est" (I.16 ¶47): not said to be one place.
- Gaps recorded: `things/fibre-rope.md` (the plant), `things/briquet.md` (what it is made of), `places/the-old-outlet.md` (the passage's length is not totalled), `places/the-well.md` (whether it is the "puits intérieur" of III.16 ¶64).
- Not put on an Open line but for the I.19 wave: I.16 ¶12 says the east coast is "not exposed like the other to the trade winds, which blow from the north-west"; I.19 differs (per the I.16 notes). It is carded on `lincoln-island.md` as I.16 ¶12 only.
- The time of day on 21 May (I.17 ¶68, the hole done "about four in the evening", the blast 25 minutes after the fibre is lit; I.18 ¶83, out of the outlet "a little before four o'clock"): not carded, because I dated none of the I.18 events; I wrote "after the blast", not "21 May", on the I.18 facts. A dated disagreement belongs in the outlines.

## Questions for the author

1. The ore and the coal: should the Open lines above stay open until I.19 and later chapters place them again? Recommendation: leave them open; no later quote resolves them yet.
2. Subjects in A's folders met in my chapters that carry Clues: the echidna (I.15 ¶34, the summary names it, the body does not), the dugong and Top's mystery (I.16 ¶44 to ¶65), Smith's rescue and the "bras puissant" (I.17 ¶8, ¶9), Top's knowledge (I.18 ¶56). I carded none of these (A's folders); I put only the Top line on Granite-house as a clue. Recommendation: A's cards for Top, the dugong and Smith carry them.
3. Stubs for I.17's acid chain (sulphuric acid, soda, glycerine, soap, iron sulphate) are thin because each appears in one chapter and on no Clues list. Recommendation: leave them stubs; the tool-chain lines hold the process.
4. `cap-mandibule-sud.md`: I.15 ¶5 says only "la pointe du cap Mandibule", seven miles from the Chimneys; I carded it as the south cape, marked as a reading, because I.14 ¶38 describes the same walk. Recommendation: confirm in the I.14 re-read.

## Totals

31 cards made (16 stubs), 26 cards extended, about 210 facts added (including the Open lines), 23 tool-chain lines, 3 lines pruned. `cards.py check` prints 0 card problems and `links.py` 0 broken; every quote was asserted against its cited paragraph when written and resolves under `tools/quotes.py`.
