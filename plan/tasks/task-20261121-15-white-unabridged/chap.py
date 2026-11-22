#!/usr/bin/env python3
"""Set up one chapter of White made unabridged: its folder, prompts and title.
Usage: python3 chap.py NN        -> prints the chapter's paths
       python3 chap.py NN apply  -> applies the chapter's patches into its draft
Run from the root."""
import csv, pathlib, re, subprocess, sys
T = 'plan/tasks/task-20261121-15-white-unabridged'
nn = int(sys.argv[1]); code = '%05d' % (nn * 100)
act = {r['nn']: r['action'] for r in csv.DictReader(open(T + '/chapters.tsv'), delimiter='\t')}['%02d' % nn]
outline = next(pathlib.Path('story/outline').glob(code + '-*.md'))
slug = outline.name
h1 = outline.read_text(encoding='utf-8').splitlines()[0][2:].replace(' (outline)', '')
small = {'a', 'an', 'and', 'the', 'of', 'in', 'on', 'at', 'to', 'by', 'for', 'or', 'from', 'with'}
title = ' '.join(w if (i and w.lower() in small) else w[:1].upper() + w[1:] for i, w in enumerate(h1.split()))
d = pathlib.Path(T) / 'ch' / code; d.mkdir(parents=True, exist_ok=True)
draft = d / slug; tsv = d / ('patches-%s.tsv' % code)
if len(sys.argv) > 2 and sys.argv[2] == 'apply':
    r = subprocess.run(['python3', T + '/apply.py', str(nn), str(tsv), str(draft), title + ' (draft 1)'], capture_output=True, text=True)
    print(r.stdout.replace('ok ', '').replace('\n', ' ')[:0] + ('ALL OK' if r.returncode == 0 else r.stdout))
    sys.exit(r.returncode)
if act == 'patch':
    s = open(T + '/patcher-v2.md', encoding='utf-8').read()
    s = s.replace('{NN}', '%02d' % nn).replace('{OUT}', str(tsv))
    (d / 'prompt-patch.md').write_text(s, encoding='utf-8')
if act == 'render':
    def roman(n):
        out = ''
        for v, r in [(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]:
            while n >= v: out += r; n -= v
        return out
    subprocess.run(['python3', T + '/build_bundle.py', str(nn), str(d)], check=True, capture_output=True)
    s = open(T + '/pilot/prompt-render-05600.md', encoding='utf-8').read()
    fr = open('texts/fr-1875/%02d.md' % nn, encoding='utf-8').read()
    fw = len(re.findall(r'\w+', re.sub(r'^\S+ ', '', fr, flags=re.M)))
    part, ch = ('I', nn) if nn <= 22 else ('II', nn - 22) if nn <= 42 else ('III', nn - 42)
    s = (s.replace('III.14', '%s.%d' % (part, ch)).replace(T + '/pilot/bundle-05600.md', str(d / ('bundle-%s.md' % code)))
          .replace(T + '/pilot/05600-the-new-ship-and-the-third-winter.md', str(draft))
          .replace('# The New Ship and the Third Winter (draft 1)', '# %s (draft 1)' % title)
          .replace('CHAPTER LVI.', 'CHAPTER %s.' % roman(nn)).replace('about 3,800 words', 'about {:,} words'.format(round(fw, -2)))
          .replace('(the pilot, R1121-147; from the phase 8 drafter\'s prompt)', '(R1121-149; from the pilot\'s)'))
    s = s.replace('story/voice/names.md (White\'s forms of the names)', 'story/voice/names.md (White\'s forms of every name in the book: use his usual form; never a form from another translation; where it says "none in White", use its proposal)')
    s = s.replace('Running that one command is the only command you may run.', 'Running that one command is the only command you may run: no other command, no script, no python. Make every change with your editing tool.')
    import re as _re
    s = _re.sub(r'Keep to the texture in the rules: measure with\n.*?\n.*?may run[^\n]*\n', 'Keep to the texture in the rules and avoid every word in story/voice/banned.txt that is narration. Run no command at all: the main session measures the draft with tools/tells.py after you finish.\n', s, flags=_re.S)
    s = s.replace('- the word count and the tells.py line;', '- the word count, estimated;').replace('marked as the French marks it.', 'marked (1), (2) in the order of the French notes.')
    s = s.replace('Use White\'s forms of the names and White\'s American spelling.', 'Use White\'s forms of the names and White\'s American spelling. Where the French names Nab, write Neb; where it has "le nègre", write "the negro" (R1121-150). "Grain de plomb" is "pellet" or "leaden pellet"; "amandes de pin pignon" are "pine kernels" (R1121-152). Verne\'s "onaggas" are "onaggas", never "onagers" (R1121-154). Verne\'s "ascenseur" is White\'s "elevator". Verne\'s boat is "the Bonadventure", never "Good Luck" (R1121-155).')
    assert 'pellet' in s, 'render prompt rulings'
    assert 'tells.py line' not in s and 'measure with' not in s, 'render prompt tells'
    assert '05600' not in s and 'LVI' not in s, 'render prompt'
    (d / 'prompt-render.md').write_text(s, encoding='utf-8')
subprocess.run(['python3', T + '/make_critics.py', str(nn), str(draft), str(d)], check=True, capture_output=True)
for k in ['facts']:
    p = d / ('prompt-critic-%s-%s.md' % (k, code)); s = p.read_text(encoding='utf-8')
    s = s.replace("(White often cuts or changes; that is known and listed, and is not your question)",
        "(the version you check is this chapter patched to the French; where White's words still stand against the French, say so: \"white does the same: yes\")" if act == 'patch' else
        "(the version you check is a new render of the French, not White's; \"white does the same\" asks only whether White departs there too)")
    p.write_text(s, encoding='utf-8')
print(act, code, title, draft, sep='\n')
