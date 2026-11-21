#!/usr/bin/env python3
"""Card the final 01950 (R1121-132; redone for R1121-134, -135). Paragraph numbers are found from the quotes, so they cannot drift; the "¶" given by hand is ignored. Card's new facts (R1121-132), each cited (XIX bis ¶N), in one section per card,
"- **In XIX bis.**", so that the chapter's facts come out cleanly: delete that section and "XIX bis"
from "Appears in". ¶1 is "On the 1st of June". Every quote is checked against its paragraph. Run from the repo root."""
import glob, re, sys
PROSE = sys.argv[1] if len(sys.argv) > 1 else glob.glob('story/prose/01950-*.md')[0]
lines = open(PROSE, encoding='utf-8').read().split('\n')[1:]
paras, cur = [], []
for l in lines:
    if l.strip(): cur.append(l)
    elif cur: paras.append(' '.join(cur)); cur = []
if cur: paras.append(' '.join(cur))
paras = paras[2:]  # drop the chapter number and the heading
P = lambda n: paras[n - 1]
assert P(1).startswith('On the 1st of June')

F = {}  # card path -> list of (fact, paras, [quotes])
def add(card, fact, ps, *quotes):
    F.setdefault(card, []).append((fact, ps, quotes))

pl, th, pe, an = 'world/places/', 'world/things/', 'world/people/', 'world/animals/'
# places
add(pl+'baie-de-l-union.md', 'On 1 June, after a night of squalls, the wind is dropping but the sea still runs high in the bay and breaks in long rolls on the islet, under a low grey sky', '1', 'the sea still ran high in Union Bay and broke in long rolls upon the islet')
add(pl+'baie-de-l-union.md', 'On 2 June a cold rain comes on an east-north-east wind blowing straight into the bay; a squall comes out of the east across the bay with the flood, about an hour after low water', '21, 58', 'a wind which had gone round to the east-north-east and blew straight into the bay', 'It came out of the east, across the bay, a grey wall of rain and wind.')
add(pl+'baie-de-l-union.md', 'On 3 June the day is grey and still, the wind gone round to the south-west, the sea down', '71', 'in the night the wind had gone round to the south-west, and the sea was down')
add(pl+'the-channel.md', 'A sand bar lies off the mouth of the Mercy, on the coast side of the gut, a cable or two from the beach; at low water it is reached over the bared sands without crossing the gut', '4, 26', 'on the coast side of this gut, a bar of sand lay bare, a cable or two from the beach', 'There was no need to cross the gut')
add(pl+'the-channel.md', 'The squalls at the end of May reshape the shore near the Mercy: sand cut from the foot of a rock, a bank where there was none', '3', 'Here the sand had been cut away from the foot of a rock, there a bank showed where there had been none before.')
add(pl+'the-channel.md', 'The tides of 1 to 3 June: low water near first light on 1 June, toward eight on 2 June, mid-morning on 3 June; the evening ebb of 1 June falls after dark', '3, 7, 20, 23, 71', 'The tide was near its lowest', 'The evening ebb fell after dark', "Toward eight o'clock the ebb began to near its lowest.", 'Toward the middle of the morning, at low water')
add(pl+'the-channel.md', 'On 2 June, as they rise to go, Herbert\'s foot goes through the old net\'s meshes under the bar\'s sand, and the sand closes on it and holds it fast while the flood comes on; Pencroff digs it free with his knife', '0', 'His foot had gone through the old meshes where they lay under the sand, and the sand had closed upon it.', 'but the sand held the foot fast, and ran back as fast as he dug')
add(pl+'the-channel.md', "On 2 June the backwash draws the freed float off the bar into the gut, and the flood in the channel carries it in toward the mouth of the river (R1121-136)", '0', 'The backwash drew the freed ball off the bar into the gut, and the flood in the channel carried it in toward the mouth of the river.')
add(pl+'the-channel.md', 'On 3 June the bar has moved; where the float lay, the sand runs smooth and level to the gut, and not a thread of the net shows', '72, 73', 'The bar had moved.', 'the sand ran smooth and level to the gut, and of the net not a thread showed')
add(pl+'mercy-river.md', "On 2 June the glass float, carried in by the flood, breaks on the rocks at the river's mouth in the spray: a flash, seen from under the granite wall; no piece is ever found (R1121-136)", '0', "Out on the rocks at the river's mouth, in the spray, something flashed, once, and flew apart.", 'They both knew that glass thrown upon those rocks by such a sea was in pieces.')
add(pl+'the-granite-wall.md', 'Close under the wall near the foot of the ladder is a shelter from the worst of an east wind, with the bar and the islet in view; the shoes are left under a rock at its foot', '24, 61', 'They went up it to the granite wall and stood close under it, near the foot of the ladder, out of the worst of the wind.', 'set them under the rock')
add(pl+'mercy-river.md', "Pencroff's lines are set near the Chimneys, on the left bank at the river's mouth", '1', 'toward the mouth of the Mercy, where, near the Chimneys, on the left bank of the river, he had set his lines')
add(pl+'the-chimneys.md', "Pencroff's lines are set near the Chimneys, on the left bank of the Mercy's mouth", '1', 'near the Chimneys, on the left bank of the river, he had set his lines')
add(pl+'granite-house.md', 'On 2 June, in the east-north-east wind, the shutters are kept closed from first light, the house is lit only by the kitchen fire, and the kitchen chimney smokes', '21', 'Granite House was lit only by the fire of the kitchen, and the chimney smoked.')
add(pl+'granite-house.md', 'Picks and shovels are kept in the storeroom', '22', 'There were picks and shovels in the storeroom')
add(pl+'pacific-ocean.md', "The narrator: in the South Pacific the waters turn in a great round, north up the coasts of Chile and Peru, west below the line, south, and east under the westerlies, carrying what falls into it for months and years", '37', 'In the South Pacific the waters turn in a great round: up the coasts of Chile and Peru, westward below the line, then south, and back to the east under the westerly winds')
# things
add(th+'bottom-lines.md', "In June 1865 the lines are set at the mouth of the Mercy, armed with iron hooks from the forge; they are Pencroff's own affair, and he visits them every morning (R1121-60)", '1, 2', 'These lines were his own affair; he had armed them with iron hooks from the forge, and he went every morning to visit them')
add(th+'bottom-lines.md', 'On 2 June the hooks come up with their bait untouched; the lines are the pretext for going out to the bar on 2 and 3 June', '24, 71', 'the hooks came up with their bait untouched', 'the two went down once more to the lines')
add(th+'the-shutters.md', 'On 2 June the shutters are kept closed from first light against the rain on an east-north-east wind', '21', 'from first light the thick shutters were kept closed')
add(th+'hearth.md', 'The kitchen chimney smokes in the east-north-east wind of 2 June', '21', 'and the chimney smoked')
add(th+'the-furniture.md', 'On 2 June Smith, Spilett and Neb are at work indoors on the furnishing of the rooms', '21', 'The engineer, the reporter and Neb were at work within, upon the furnishing of the rooms')
add(th+'iron-tools.md', "Picks and shovels are kept in Granite House's storeroom; on 2 June Pencroff leaves them, since a man does not carry a pick to lift his lines", '22', 'But a man does not carry a pick down a ladder to lift his lines')
add(th+'knife-blades.md', 'Pencroff carries one of the two blades on 2 June; he saws blind with it at the cord under the float, and digs Herbert\'s foot free of the sand with it', '0', "the sailor had his knife, one of the two blades made from Top's collar", 'sawed at it blindly a long while', 'Then Pencroff dug with the blade of his knife')
add(th+'pencroff-jacket.md', 'On 2 June he turns up the collar of his jacket against the rain', '23', 'Pencroff turned up the collar of his jacket')
add(th+'pottery.md', "Neb's pots are in use in the kitchen of Granite House in June 1865", '23', 'went back to his pots')
add(th+'the-colonists-clothes.md', 'By June their shoes are much worn; on the sands they go barefoot, trousers rolled to the knee, and dry their wet clothes on their backs by the fire', '24, 69', 'took off their shoes, which were much worn', 'dried their clothes upon their backs')
add(th+'seaweed.md', 'On 2 June a tangle of wrack, torn loose by the squalls, lies over the float on the bar', '27', 'A tangle of wrack, torn loose by the squalls, lay over it')
add(th+'window-glass.md', "Pencroff's unspoken reckoning on 2 June: the glass float might make a window for the shuttered house, since Smith has not yet had the time to make glass", '39', 'because the engineer had not yet had the time to make glass for its windows')
add(th+'lens.md', "Pencroff saw the lens, and on 2 June thinks Smith could make a window of the glass float", '39', 'he had seen the lens he made of two watch glasses, and he was sure that he could make a window of a ball')
add(th+'the-rope-ladder.md', 'On 2 June it streams with water on the climb home', '0', 'The ladder streamed with water')
# Not on mobilis-in-mobili.md: linking the float's letters to the motto is the outline's truth (R1121-27), not the page's.
# people
add(pe+'pencroff.md', 'He crossed the channel on the first day and knows its current; a seaman, he does not go out alone on the bar with the flood making', '7', 'he had crossed that channel on the first day', 'Pencroff was bold, but he was a seaman, and he did not go out alone.')
add(pe+'pencroff.md', 'On 1 June he sees the float, keeps it from the others so as not to raise their hopes, and takes Herbert aside: "If it is worth the telling, we tell it"', '9–19', "I'll not have Mr. Smith and Mr. Spilett and Neb all hoping", "If it is worth the telling, we tell it.")
add(pe+'pencroff.md', 'He has put in at many good ports and never seen a glass float; he has scraped barnacles off many a ship\'s bottom', '34, 42', 'I have put in at many good ports, my boy, and I have never seen the like.', "I have scraped them off many a ship's bottom.")
add(pe+'pencroff.md', 'Under the wall, when Herbert says they must tell Mr. Smith: "And so we shall, my boy, when we have something to show him"; they would be giving the others only a hope', '0', 'And so we shall, my boy, when we have something to show him', 'What should we be giving them now but a hope?')
add(pe+'pencroff.md', 'His unspoken reckoning: a window of the ball for the shuttered house, or the finest float for his lines', '39', 'it would be the finest float for his lines that a fisherman ever had; but he kept all this to himself')
add(pe+'pencroff.md', 'On 2 June, where they reach the ball, he sets the boy a limit from old habit, back before the turn; over the letters he misjudges the half hour; when Herbert\'s foot is held by the net and the sand he digs it free with his knife; he does not laugh after; on 3 June he keeps the lad on his landward side', '0', '"Back before the turn, my boy," said Pencroff, from old habit, with a look at the gut.', 'judged they had the half hour yet', 'Then Pencroff dug with the blade of his knife, and at last drew the foot free.', 'Pencroff did not laugh.', 'This time Pencroff kept the lad on his landward side')
add(pe+'pencroff.md', 'On 3 June: "Five of us and the picks, and we\'d have had it"; then, to the lad, "the sea will give us something else"', '0', "Five of us and the picks, and we'd have had it", 'The sea has taken, and the sea will give us something else.')
add(pe+'harbert.md', 'He knows barnacles and goose barnacles by name: goose barnacles hang by a stalk, fasten on anything afloat and live near the surface; from them he reads that the float floated long and came from far off', '41–45', 'these are goose barnacles', 'They fasten upon anything that floats')
add(pe+'harbert.md', 'He reads the letters as "Latin, I think", too few to choose a word among', '0', 'here there are not letters enough to choose among them')
add(pe+'harbert.md', 'On 2 June his foot is caught in the old net under the sand, and Pencroff digs it free as a sea breaks over them; under the wall he coughs up the sea water and laughs; at the ladder he says they must tell Mr. Smith, and owns Pencroff is right that they would be giving the others only a hope', '0', 'Herbert rose, and fell again.', 'Herbert coughed up the sea water he had swallowed, and laughed', 'We must tell Mr. Smith, Pencroff.', 'Herbert thought a moment, and owned that he was right')
add(pe+'harbert.md', 'He keeps Pencroff\'s secret from 1 June; on 3 June, at the smooth sand, he answers: "and it lay under our hands the whole time the sea was out"', '0', 'Herbert promised', 'and it lay under our hands the whole time the sea was out')
add(pe+'nab.md', 'On 2 June he calls after Pencroff that he is a madman for going out in the rain, and laughs at Pencroff\'s joke when they come home wet', '0', 'Neb called after the sailor that he was a madman', 'Neb laughed loudly')
add(pe+'gedeon-spilett.md', 'On 2 June he asks the wet pair "what has the sea given you this morning?"', '67', 'what has the sea given you this morning?')
add(pe+'cyrus-smith.md', 'On 2 June he works indoors at the furnishing, Top at his feet, and smiles at Pencroff\'s joke', '21, 69', "Top lay at his master's feet", 'the engineer smiled')
add(an+'top.md', 'On 1 to 3 June he stays with his master; on 2 June he lies at Smith\'s feet indoors', '21', "Top lay at his master's feet")
# new cards
add(th+'the-glass-float.md', 'A ball of glass about a foot across, half buried in the bar off the Mercy, a third of it showing above the sand like the back of a turtle', '5, 6, 28', 'Something lay on the bar, half buried, and it was round.', 'The thing might measure a foot across', 'so that it showed above the sand as the back of a turtle shows above the sea')
add(th+'the-glass-float.md', 'Dark green glass, like a bottle\'s, under a crust of dead grey-white barnacles over the part that shows, with a few dead goose barnacles among them', '27, 28, 41, 43', 'there the glass showed through, dark green, like the glass of a bottle', 'these are goose barnacles')
add(th+'the-glass-float.md', 'A rotten, sand-choked net cord runs from it into the bar on the gut side, and a second cord passes under it on the hidden side; it cannot be turned, and the dug sand refills with water', '28, 30', 'a dark cord came out of the sand, rotten and swollen with water, with the meshes of a net choked with sand along it', 'A cord of the same kind as the other passed under it, on the hidden side')
add(th+'the-glass-float.md', 'Pencroff calls it a float for a net, no cork and never made in America. The narrator: glass net floats are a late thing, new still and rare, which an American sailor might never have seen', '32, 36', "It's a float,\" said he at last. \"A float for a net.", 'Only in late years had fishermen begun to buoy their great nets with globes of blown glass')
add(th+'the-glass-float.md', 'A round seal a palm across is moulded in the glass on the gut side, mostly below toward the sand, with raised capitals inside its rim: B, a place the crust holds, L, I; then the ring goes into the sand', '50, 52', 'the rim of a round seal about a palm across, which had been moulded in the glass itself', 'Beyond the I, the ring went down into the sand.')
add(th+'the-glass-float.md', 'Lost on 2 June: the squall and flood loosen it, the cord gives, the backwash and the channel current take it to the islet, and it breaks on the rocks; on 3 June the bar is smooth. That day the two tell the others nothing of it', '0', 'At last it gave way', 'something flashed, once, and flew apart', 'of the net not a thread showed', 'That was all they told, and it was true, as far as it went.')
add(an+'barnacles.md', 'A grey-white crust of dead acorn barnacles, cemented one against another over the part of the glass float that shows; Pencroff knows them from ships\' bottoms. Acorn barnacles grow only where the float rode under water, never on a dry top (R1121-134)', '0', 'Over all its upper part lay a crust of grey-white shells, dead and empty, packed one against another.', "I have scraped them off many a ship's bottom.")
add(an+'barnacles.md', 'Goose barnacles, as Herbert tells them: they hang by a stalk, fasten on anything afloat (driftwood, a buoy, a ship), and live only near the surface where the sea brings their food; on the float only their shells and dried stalk stumps are left', '43, 45', 'that hang by a stalk', 'they live only near the surface, where the sea brings them their food', 'a stump of the stalk, dried hard among the others')

NEW = {
 th+'the-glass-float.md': ('# The glass float: the ball of glass on the bar off the Mercy, lost on 2 June 1865',
   '*The glass net float Pencroff finds half buried in the bar on 1 June 1865 and loses in the squall of the 2nd, as the inserted chapter shows it. What it truly is lives in [the outline](../../story/outline/01950-the-float-in-the-bar.md#the-find), never on this card.*',
   'Keywords: float, flotteur, glass ball, boule de verre, net, filet, seal, letters, B L I, barnacles'),
 an+'barnacles.md': ('# The barnacles: acorn and goose barnacles on the glass float',
   '*The dead barnacles crusting the glass float, which Herbert names and reads (the inserted chapter only).*',
   'Keywords: barnacles, anatifes, balanes, goose barnacles, stalk, Lepas, crust, shells'),
}

def quote_ok(ps, q):
    nums = [int(x) for x in re.findall(r'\d+', ps)]
    if '–' in ps:
        a, b = map(int, re.findall(r'\d+', ps)[:2]); nums = range(a, b + 1)
    return any(q in P(n) for n in nums)

def where(q):
    hits = [i + 1 for i, p in enumerate(paras) if q in p]
    return hits
bad = []
for c, fs in F.items():
    for k, (fact, ps, qs) in enumerate(fs):
        found = []
        for q in qs:
            h = where(q)
            if len(h) != 1: bad.append((c, fact[:40], q, h))
            else: found += h
        fs[k] = (fact, ', '.join(str(n) for n in sorted(set(found))), qs)
if bad:
    for b in bad: print('QUOTE NOT UNIQUE OR NOT FOUND', b)
    sys.exit(1)

def section(facts):
    out = ['- **In XIX bis.** *(The inserted chapter, 01950; R1121-132.)*']
    for fact, ps, qs in facts:
        out.append(f'  - {fact} (XIX bis ¶{ps}). *(Drafted.)*')
        out += [f'    - quote: {q}' for q in qs]
    return out

# Strip every card's old section first, so a card that has lost all its facts is cleaned too.
for c in glob.glob('world/*/*.md'):
    t = open(c, encoding='utf-8').read()
    if '- **In XIX bis.**' in t and c not in NEW:
        i0 = t.index('- **In XIX bis.**'); i1 = t.index('- **Appears in:**', i0)
        t = t[:i0] + t[i1:]
        t = re.sub(r'(- \*\*Appears in:\*\*.*?), XIX bis', r'\1', t)
        open(c, 'w', encoding='utf-8').write(t)
for card, facts in F.items():
    if card in NEW:
        h, d, k = NEW[card]
        body = [h, '', d, '', k, ''] + section(facts) + ['- **Appears in:** XIX bis']
        open(card, 'w', encoding='utf-8').write('\n'.join(body) + '\n'); continue
    s = open(card, encoding='utf-8').read()
    if '- **In XIX bis.**' in s:
        i0 = s.index('- **In XIX bis.**'); i1 = s.index('- **Appears in:**', i0)
        s = s[:i0] + s[i1:]
        s = re.sub(r'(- \*\*Appears in:\*\*.*?), XIX bis', r'\1', s)
    L = s.split('\n')
    i = next(k for k, l in enumerate(L) if l.startswith('- **Appears in:**'))
    L[i:i] = section(facts)
    L[i + len(section(facts))] += ', XIX bis'
    open(card, 'w', encoding='utf-8').write('\n'.join(L))
print(len(F), 'cards;', sum(len(v) for v in F.values()), 'facts')
