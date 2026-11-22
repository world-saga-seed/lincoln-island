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
subprocess.run(['python3', T + '/make_critics.py', str(nn), str(draft), str(d)], check=True, capture_output=True)
for k in ['facts']:
    p = d / ('prompt-critic-%s-%s.md' % (k, code)); s = p.read_text(encoding='utf-8')
    s = s.replace("(White often cuts or changes; that is known and listed, and is not your question)",
        "(the version you check is this chapter patched to the French; where White's words still stand against the French, say so: \"white does the same: yes\")" if act == 'patch' else
        "(the version you check is a new render of the French, not White's; \"white does the same\" asks only whether White departs there too)")
    p.write_text(s, encoding='utf-8')
print(act, code, title, draft, sep='\n')
