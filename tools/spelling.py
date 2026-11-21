#!/usr/bin/env python3
"""Build a spelling list from a reference text, and check drafts against it both ways.

For each British/American pair (with its inflections), count both forms in the
reference text. The form it uses is the house form; the other is wrong. A pair the
text never uses is left out (no evidence either way).

  spelling.py build REF... --out LIST.md          write the table
  spelling.py check LIST.md DRAFT...              print every wrong form in the drafts
"""
import argparse, re, sys, pathlib

# (British stem, American stem, endings)
PAIRS = [
 ('centre','center','s|d'), ('fibre','fiber','s'), ('metre','meter','s'), ('litre','liter','s'),
 ('theatre','theater','s'), ('lustre','luster',''), ('sombre','somber',''), ('spectre','specter','s'),
 ('calibre','caliber','s'), ('sabre','saber','s'),
 ('grey','gray','s|ed|ish|ness'), ('mould','mold','s|ed|ing|y|er|ers'), ('sulphur','sulfur','|ous|ic|ate|ated'),
 ('travelled','traveled',''), ('travelling','traveling',''), ('traveller','traveler','s'),
 ('labelled','labeled',''), ('levelled','leveled',''), ('signalled','signaled',''),
 ('cancelled','canceled',''), ('marvellous','marvelous','|ly'), ('jewellery','jewelry',''),
 ('woollen','woolen','s'), ('quarrelled','quarreled',''), ('channelled','channeled',''),
 ('colour','color','s|ed|ing|less|ful'), ('honour','honor','s|ed|ing|able|ably'), ('labour','labor','s|ed|ing|er|ers'),
 ('favour','favor','s|ed|ing|able|ably|ite|ites'), ('harbour','harbor','s|ed|ing'), ('neighbour','neighbor','s|ing|hood|ly'),
 ('vigour','vigor',''), ('odour','odor','s|less'), ('rigour','rigor','s'), ('humour','humor','s|ed'),
 ('endeavour','endeavor','s|ed|ing'), ('behaviour','behavior',''), ('armour','armor','|ed|y'),
 ('clamour','clamor','s|ed|ing'), ('ardour','ardor',''), ('rumour','rumor','s|ed'), ('splendour','splendor','s'),
 ('vapour','vapor','s'), ('tumour','tumor','s'), ('parlour','parlor','s'),
 ('defence','defense','s|less'), ('offence','offense','s'), ('pretence','pretense','s'),
 ('plough','plow','s|ed|ing|share|shares'), ('waggon','wagon','s'), ('draught','draft','s'),
 ('cheque','check','s'), ('grey','gray',''), ('storey','story',''), ('connexion','connection','s'),
 ('programme','program','s'), ('kilogramme','kilogram','s'), ('gramme','gram','s'),
 ('manoeuvre','maneuver','s|d'), ('aluminium','aluminum',''), ('sceptic','skeptic','s|al|ism'),
 ('ploughed','plowed',''), ('catalogue','catalog','s'), ('analyse','analyze','s|d'), ('paralyse','paralyze','s|d'),
 ('realise','realize','s|d'), ('organise','organize','s|d|r'), ('recognise','recognize','s|d'),
 ('civilise','civilize','s|d'), ('apologise','apologize','s|d'), ('criticise','criticize','s|d'),
 ('utilise','utilize','s|d'), ('surprize','surprise','s|d'), ('enquire','inquire','s|d|y'),
 ('gaol','jail','s|er|ers'), ('mustache','moustache','s'),
]

def rx(stem, ends):
    alts = [e for e in ends.split('|')] if ends else ['']
    if '' not in alts: alts.append('')
    return re.compile(r'\b' + re.escape(stem) + '(' + '|'.join(re.escape(a) for a in alts) + r')\b', re.I)

def count(text, stem, ends): return len(rx(stem, ends).findall(text))

def build(refs, out):
    text = ''.join(pathlib.Path(p).read_text(encoding='utf-8') for p in refs)
    rows, seen = [], set()
    for a, b, e in PAIRS:
        if (a, b) in seen: continue
        seen.add((a, b))
        na, nb = count(text, a, e), count(text, b, e)
        if na == nb == 0: continue
        house, wrong = (a, b) if na >= nb else (b, a)
        rows.append(f'| {house} | {wrong} | {max(na,nb)} | {min(na,nb)} | {e} |')
    head = ('# The house spelling\n\n*Built by `tools/spelling.py build` from the reference text. For each British/American pair the text uses, '
            'its form is the house form and the other is wrong, with the counts of each. A pair it never uses is not listed.*\n\n'
            '| House form | Wrong form | House count | Wrong count | Endings |\n|---|---|---|---|---|\n')
    pathlib.Path(out).write_text(head + '\n'.join(rows) + '\n', encoding='utf-8')
    print(f'{len(rows)} pairs written to {out}')

def check(lst, drafts):
    rows = [l.split('|')[1:6] for l in pathlib.Path(lst).read_text(encoding='utf-8').splitlines() if l.startswith('| ') and not l.startswith('| House')]
    hits = 0
    for d in drafts:
        for i, line in enumerate(pathlib.Path(d).read_text(encoding='utf-8').splitlines(), 1):
            if line.startswith("#"): continue
            for house, wrong, nh, nw, ends in rows:
                for m in rx(wrong.strip(), ends.strip()).finditer(line):
                    hits += 1
                    print(f'{d}:{i}: "{m.group(0)}" (house form: {house.strip()}{m.group(1)}; reference {nh.strip()} to {nw.strip()})')
    print(f'{hits} wrong forms')
    return hits

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('build'); b.add_argument('refs', nargs='+'); b.add_argument('--out', required=True)
    c = sub.add_parser('check'); c.add_argument('list'); c.add_argument('drafts', nargs='+')
    a = ap.parse_args()
    if a.cmd == 'build': build(a.refs, a.out)
    else: sys.exit(1 if check(a.list, a.drafts) else 0)
