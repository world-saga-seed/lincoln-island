# Report of the Vingt mille carder (step 4; R1120-25, R1121-02)

The tool refused the report file, so this is the report; it is not saved at plan/archive/task-20261121-05-carding/report-vml.md.

Scope: what L'Île (III.15 ¶100 on, III.16, III.17) draws on from Vingt mille, carded with a VML cite. Every quote resolves (`tools/quotes.py` on each card, against `texts/fr-1875/*.md` and `texts/vml-1870/[0-9]*.md`). `tools/links.py` prints 0 broken. `tools/cards.py check` reports only the three stale index tables, since I did not run build. I ran no git.

## Cards made (5), all under world/
- `people/the-french-professor-his-servant-and-a-canadian-fisherman.md`. L'Île gives no names, so VML's Aronnax, Conseil and Ned Land are carded as VML facts.
- `things/frigate-abraham-lincoln.md`. This is the frigate, not the statesman of `people/abraham-lincoln.md`.
- `things/the-frigate-rammed-by-the-nautilus.md` (III.16 ¶70 to ¶73; VML II.21).
- `things/vingt-mille-lieues-sous-les-mers.md`, the book itself (III.16 ¶24, ¶25, ¶58, n1).
- `people/the-candiotes.md` (III.16 n2; VML II.6, II.8).

## Cards extended (10)
- `people/captain-nemo.md`
- `things/nautilus.md`
- `places/nautilus-engine-room.md`
- `places/nautilus-platform.md`
- `places/nautilus-saloon.md`
- `places/nautilus-library.md`
- `things/the-nautilus-light.md`
- `places/crypte-dakkar.md`
- `things/mobilis-in-mobili.md`
- `things/the-nautilus-boat.md`

The engine-room and mobilis cards were stubs. The L'Île fact is now a bullet with the VML bullet under it, and the stub line is kept.

`places/bundelkund.md` is untouched, because VML never names Bundelkund.

Four gap lines deleted, each answered by VML or made false by it:
- On captain-nemo.md: "The method of producing his electricity is unrevealed" is answered by VML I.12 ¶19 to ¶25.
- On captain-nemo.md: "The fate of his father, mother, wife and children is not stated" is answered by VML II.21 ¶57 ("j'ai vu tout périr").
- On captain-nemo.md: "III.16 refers throughout to the earlier book… the card holds only what III.16 states" is no longer true.
- On nautilus.md: "nothing from it is drawn on here" is no longer true.

## L'Île statements traced
- **Submarine built on a desert island of the Pacific (III.16 ¶53):**
  - VML I.13 ¶47: "un îlot désert, en plein Océan", and fire destroyed every trace.
  - VML I.13 ¶45: parts from Le Creusot, Prussia and Motala.
  - VML I.13 ¶39: captain, builder and engineer.
- **Electricity as motive force, light and heat, and "des moyens qui seront connus un jour":**
  - VML I.12 ¶9, ¶13, ¶19, ¶21, ¶23, ¶25, ¶27: sodium and mercury cells, "charbon de mer".
  - VML I.13 ¶39.
- **"Capitaine Nemo", and English (III.16 ¶5, ¶2):** VML I.10 ¶56 and ¶5 (he speaks French, English, German and Latin).
- **Vigo treasure (¶54):**
  - VML II.8 ¶58, ¶63, ¶64, ¶67.
  - Gift to peoples in revolt: VML II.8 ¶73, ¶75.
  - Candiotes (n2): VML II.8 ¶75; II.6 ¶76, ¶82, ¶83.
- **Three men thrown aboard 6 November (¶55):**
  - VML I.6 ¶95, ¶104; I.7 ¶15, ¶58, ¶84, ¶86, ¶90; I.8 ¶1.
  - Names: VML I.2 ¶1; I.3 ¶6; I.4 ¶7, ¶10; I.10 ¶5.
- **Frigate Abraham-Lincoln and the shock (¶55):** VML I.6 ¶102 to ¶104; I.7 ¶20, ¶22; I.10 ¶10; I.13 ¶37.
- **Taken for a cetacean or pirates, hunted on all seas (¶56):** VML I.1 ¶7; I.2 ¶5; I.8 ¶1; I.10 ¶12; I.14 ¶9; II.21 ¶30.
- **Kept prisoners; twenty thousand leagues (¶57):** VML I.10 ¶24, ¶42; II.23 ¶4. "Seven months" is a discord, below.
- **Escape by boat and the Maelstrom (¶58):**
  - VML II.22 ¶22, ¶52, ¶56, ¶58, ¶61.
  - Cast ashore at the Lofoten and the book: VML II.23 ¶1, ¶3, ¶5.
- **Coral cemetery (¶59):** VML I.24 ¶56 to ¶59, ¶72, ¶74; II.19 ¶2.
- **"Ports sous-marins" (¶60):** VML II.10 ¶23, ¶26 (the volcano lagoon, "son port d'attache"), carded on crypte-dakkar.md.
- **Diving dress (¶62, ¶64):** VML I.15 ¶67 (Rouquayrol-Denayrouze, improved by Nemo).
- **Electric bullets (¶65):** VML I.15 ¶81, ¶83; I.16 ¶13.
- **Family perished (¶49), and "dans la justice et dans le droit" (¶75):** VML II.21 ¶57.
- **The rammed frigate (¶71, ¶73):** VML II.21 ¶15 to ¶17, ¶22, ¶41, ¶46, ¶50, ¶51, ¶57, ¶78, ¶81, ¶84.
- **Mobilis in mobili (III.17 ¶13):** VML I.8 ¶59, ¶60; II.6 ¶79.
- **Saloon, library, dining room, organ, pearls (III.15 ¶142 to ¶144; III.17 ¶13, ¶40):**
  - VML I.10 ¶64.
  - VML I.11 ¶1, ¶2, ¶6, ¶10, ¶21, ¶22, ¶23, ¶27, ¶31, ¶32, ¶35.
  - VML I.12 ¶36.
- **Lenticular eye, helm cage, light (III.17 ¶42):** VML I.13 ¶29, ¶31, ¶33; I.14 ¶8, ¶10; I.8 ¶10; I.12 ¶31.
- **Its boat (III.16 ¶58), and the tanks and taps (III.17 ¶32):** VML I.12 ¶40, ¶42; I.13 ¶8, ¶18.
- **Crew "une vingtaine" (¶51):** VML I.18 ¶4; I.12 ¶50; II.21 ¶51.
- **"D'un pôle à l'autre" (¶54):** only the south pole is in VML (II.14 ¶87, ¶93). I found no north pole there.
- **Not found:**
  - The "appareil alphabétique" (III.16 ¶66). I searched `alphabét` in all 47 chapters. The nearest is the electric wire and "télégramme" between boat and ship (I.12 ¶46), which is not the same.
  - Dakkar, Bundelkund, Tippoo-Saïb, the 1857 revolt. I searched `Bundel`, `Dakkar`, `Tippo` and `cipaye`; VML says nothing of them.

## Discords put on Open lines (both readings quoted and cited; carded neither)

On captain-nemo.md, eight:
1. **Year of the night of 6 November.** III.16 ¶55 says 1866. VML dates the hunt to 13 April 1867 and "le 2 juillet", then the 6 November (I.1 ¶19, I.2 ¶30, I.6 ¶95), so VML's year is 1867. That year is my reckoning, marked *(My reading, to confirm.)*, because VML gives none for the night.
2. **The escape.** III.16 ¶58 says 22 June 1867, and ¶71 says "quelques jours" after the sinking. VML has the sinking on 2 June, dated 1 June 1868, then "quinze ou vingt jours" before the Maelstrom, and gives no date for the escape (II.20 ¶52, II.21 ¶72, II.22 ¶9). Hetzel's III.16 n1 is quoted there too.
3. **Seven months** (III.16 ¶57) against "en moins de dix mois" and "dix mois" (VML II.23 ¶4, ¶6).
4. **England.** III.16 ¶41, ¶42 say he would never set foot there. VML I.13 ¶43 has him say "j'ai étudié à Londres, à Paris, à New York".
5. **The sunk ship.** III.16 ¶71, ¶73 say a frigate, English, in a narrow shallow bay. VML II.21 ¶17, ¶50, ¶55 and II.20 ¶52 have an ironclad two-decker of unnamed nationality met in the open sea. This is also on the-frigate-rammed card.
6. **Ocean of the coral cemetery.** III.16 ¶59 says "au fond du Pacifique". VML I.24 ¶46, ¶49 say "cette portion de l'océan indien".
7. **The crew.** III.16 ¶51 has companions gathered in Bundelkund. VML I.18 ¶4 has sailors "de nations différentes". This is also on nautilus.md.
8. **His age.** III.16 ¶60 says sixty. VML I.8 ¶21 says "trente-cinq ou cinquante ans".

On the other cards:
- **nautilus.md:**
  - Length: "deux cent cinquante pieds" (III.15 ¶132) against "soixante-dix mètres" (VML I.13 ¶2). The professor's own estimate of the animal in VML I.6 ¶43 was also 250 feet.
  - Platform height: "quatre-vingts centimètres" (VML I.14 ¶9) against seven or eight feet and ten to twelve feet.
  - Engine room: "à l'avant" (III.17 ¶40) against "à l'arrière" (VML I.12 ¶35, ¶36, ¶51). This is also on the engine-room, library and platform cards.
- **nautilus-platform.md:** the helm cabin "derrière cet œil" (III.17 ¶42) against the reflector "en arrière de la cage du timonier" (VML I.13 ¶33).
- **mobilis-in-mobili.md:** "Mobilis in mobili" (III.17 ln1) against "Mobilis in mobile" (VML II.6 ¶79; the title of I.8).
- **the-nautilus-boat.md:** VML's boat is "entièrement ponté" and entered by a man-hole, where the colonists' iron boat has benches. Whether they are one boat is not said.
- **three-men card:**
  - Conseil followed his master rather than being thrown (VML I.7 ¶14, ¶15), against "précipités" (III.16 ¶55).
  - "Pendant la nuit… jetés à son bord" against a night on the hull and boarding at day (VML I.7 ¶84, ¶86, ¶90).
- **crypte-dakkar.md:** none put on Open. Its only addition is VML II.10 ¶26, the volcano lagoon as "port d'attache".

## Questions for the author, with my recommendation
1. **Cards not on my list that VML bears on.** The L'Île facts sit on `places/maelstrom.md`, `places/coral-cemetery.md`, `things/vigo-treasure.md`, `things/diving-suit.md`, `things/electric-bullets.md` and `things/nemos-casket.md`. The electric-bullets Open line ("does not say what the bullets are made of") is answered by VML I.15 ¶83. The casket is related to the chest of gold bearing the cipher and motto (VML II.6 ¶79), though that is a different chest. I put those facts on `captain-nemo.md` and `nautilus.md` instead, where the L'Île fact also sits, with links to each card. Recommend one short pass to copy the VML bullets onto those six cards.
2. **Whether to rule on the discords** (250 feet, seven months, 22 June 1867). Recommend no ruling now: the notes say "both readings", and the insert does not need them.
3. **The crew's nationality** (VML I.18 ¶4) may matter if the insert shows the Nautilus's dead companions. Recommend leaving the Open line and asking only if the insert touches the crew.

## Totals
Cards made 5; cards extended 10; facts added about 122 VML-cited bullets. About 28 of those are Open-line discords or answers, and the rest are *(Drafted.)* facts with quotes. Two are marked *(My reading, to confirm.)*: the Candiotes chest, and the year of 6 November in VML. Four stale gap lines deleted. The three world/ index tables are stale and need the main session's build.
