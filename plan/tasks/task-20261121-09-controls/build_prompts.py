#!/usr/bin/env python3
"""Build the three phase 7 control prompts from the fixed texts below and the
working texts (White's chapters, Verne's French), as plain text a prompter
would paste: paragraph numbers, page marks and plate captions stripped;
Verne's footnotes kept at the end of the French. Run from the repo root:
  python3 plan/tasks/task-20261121-09-controls/build_prompts.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
LINE = re.compile(r'^(hd|¶\d+|n\d+)(?: \[[^\]]*\])? (.*)$')


def plain(path):
    body, notes = [], []
    for line in open(path, encoding='utf-8'):
        m = LINE.match(line.rstrip('\n'))
        if not m:
            continue
        tag, text = m.groups()
        (notes if tag.startswith('n') else body).append(text)
    out = '\n\n'.join(body)
    if notes:
        out += '\n\n' + '\n'.join('[Note: %s]' % n for n in notes)
    return out


def white(n):
    return plain('texts/white-1876/%02d.md' % n)


def french(n):
    return plain('texts/fr-1875/%02d.md' % n)


NEIGHBOUR = """I'm preparing an edition of Jules Verne's *The Mysterious Island* in the voice of Stephen W. White's 1876 English translation. White's chapter {roman} cuts and softens parts of Verne's text, so I want it done again.

Below is Verne's French for Part I, chapter {n} (Hetzel, 1875), and, for White's voice, his translations of the chapters on either side, {before} and {after}.

Translate chapter {roman} into English as White would have written it: his diction and rhythm, his American spelling (color, honor, harbor), and his forms of the names (Herbert, Neb, Gideon Spilett, Granite House, Union Bay, Safety Islet). But make it complete and faithful to the French: nothing cut, nothing added, nothing softened. Begin with the chapter heading and its summary line, in White's style. Give only the chapter.

=== Verne, Part I, chapter {n} (French) ===

{fr}

=== White, chapter {before} ===

{w_before}

=== White, chapter {after} ===

{w_after}
"""

INSERT = """I'm adding one chapter to Jules Verne's *The Mysterious Island*. It sits between chapters XIX and XX of Stephen W. White's 1876 English translation, as "Chapter XIX bis". White's chapters XIX and XX are below, for his voice and for where the story stands. Write the new chapter in White's English, in Verne's manner: his narrator, the past tense, kept with Pencroff and Herbert. Use White's American spelling and his forms of the names. Make it about 2,500 words, beginning with the heading and a summary line in White's style. Give only the chapter.

The scene. It is the first days of June 1865, the start of the island's first winter: the colonists have just moved into Granite House, and Whit Sunday (4 June) is still to come. On the morning of 1 June, Pencroff goes down at low water to his fishing lines in the Mercy. Reading the waterline as a sailor does, he sees something on a sandbar in the channel between the shore and Safety Islet: a round thing, about a foot across, half buried. The flood is already making. Not wanting to raise hopes he can't keep, he tells no one but Herbert, out of doors, and asks the boy to help him with the lines at the next morning's low water. That morning dawns in rain. The shutters of Granite House are closed, and the others are at work indoors. The two lift the lines and find them empty. Then they cross the bared sand to the bar with no tools but Pencroff's knife, one of the colony's only two, made from the halves of Top's collar; picks carried out of the house would have been asked about. The thing is a ball of dark green glass, thick with dead barnacles, still lashed to the remains of an old net buried in the sand. It is too fast to turn or pull free, and the lashing runs out of reach under it. Pencroff knows it for a net float, but not cork and not American: he has never seen its like. Herbert reads the barnacles: long dead, of the kind that grow on things kept at the surface. So it has been in the sea a long time and, he thinks, came from far off, which dims their hope of a ship nearby. Chipping the crust away with a stone, they bare part of a moulded seal: a broken run of capital letters, a B, an L, an I. "Latin, I think," Herbert says, and no more. While he chips, Pencroff counts silently what the glass would be worth, light for the shuttered house and a float for his lines, but he never says it. They spend the hour of low water reading it instead of freeing it. Five men with picks could have had it out; two cannot.

Then the squall comes in with the flood. They shelter under the granite wall near the foot of the ladder, where they can still see the float in the surf. The surge breaks what is left of the rotten mooring, and in a rift of light they see a flash on the rocks of the islet, in the spray, and it is gone. They are home by early afternoon, wet through. Pencroff makes a joke of it ("The lines took nothing, and the sea took the pair of us") and says no more, because he still means to bring something home himself and lay it on the table, a surprise. At the next low water, on 3 June, the bar has shifted, and there is nothing to find, not even the net. Pencroff: "Five of us and the picks, and we'd have had it." Herbert: "We had it, Pencroff. For an hour." The two never speak of it again, to anyone. The point of the chapter is the cost of not acting quickly, of keeping a find to themselves. For you, not for the page: the float is from Captain Nemo's Nautilus, from a net her crew lost there years before. The chapter must never say or hint whose it is, and it explains nothing.

=== White, chapter XIX ===

{w19}

=== White, chapter XX ===

{w20}
"""

prompts = {
    'prompt-01900.md': NEIGHBOUR.format(roman='XIX', n=19, before='XVIII', after='XX',
                                        fr=french(19), w_before=white(18), w_after=white(20)),
    'prompt-01950.md': INSERT.format(w19=white(19), w20=white(20)),
    'prompt-02000.md': NEIGHBOUR.format(roman='XX', n=20, before='XIX', after='XXI',
                                        fr=french(20), w_before=white(19), w_after=white(21)),
}
for name, text in prompts.items():
    with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
        f.write(text)
    print(name, len(text.split()), 'words')
