#!/usr/bin/env python3
"""A voice critic's prompt for a batch of chapters of White made unabridged.
Usage: python3 make_voice.py OUT.md NN NN NN   (run from the root)"""
import csv, glob, re, subprocess, sys
T = 'plan/tasks/task-20261121-15-white-unabridged'; R = '.'
out, nns = sys.argv[1], [int(x) for x in sys.argv[2:]]
act = {r['nn']: r['action'] for r in csv.DictReader(open(T + '/chapters.tsv'), delimiter='\t')}
def cite(n): return ('I.%d' % n) if n <= 22 else ('II.%d' % (n - 22)) if n <= 42 else ('III.%d' % (n - 42))
files, desc = [], []
for n in nns:
    code = '%05d' % (n * 100); f = [p for p in glob.glob('%s/ch/%s/%s-*.md' % (T, code, code))][0]
    files.append(f)
    desc.append('%s (%s) is %s' % (code, cite(n), "White's own chapter patched where he departs from the French" if act['%02d' % n] == 'patch' else 'rendered anew from the French in his voice'))
s = open(T + '/pilot/prompt-critic-voice.md', encoding='utf-8').read()
i = s.index('\n---\n'); j = s.index('Read first story/voice/pov.md')
intro = ("\n---\n\nYou are a critic for a novel in progress, in the folder %s: Jules Verne's *L'Île mystérieuse* in English, in the voice of Stephen W. White's translation (1876). %d chapters, from the work of making White whole: %s. Run no git commands of any kind. Do not launch agents. Work alone. Write nothing in the repository; your answer is your final message.\n\nThe chapters: %s.\n\n"
         % (R, len(nns), '; '.join(desc), ' and '.join('%s/%s' % (R, f) for f in files)))
s = intro + s[j:]
s = s.replace('4. Patch seams (00500 only).', '4. Patch seams (the patched chapters only).')
nums = subprocess.run(['python3', 'tools/tells.py'] + files + ['--banned', 'story/voice/banned.txt'], capture_output=True, text=True).stdout
nums = '\n'.join(l for l in nums.splitlines() if ' w=' in l)
a = s.index("The drafts' numbers:\n"); b = s.index('Flag, with the paragraph', a)
s = s[:a] + "The drafts' numbers:\n" + nums + "\n" + s[b:]
s = s.replace('Head your answer "# Critic: voice, the pilot (00500, 05600)"', 'Head your answer "# Critic: voice, %s"' % ', '.join('%05d' % (n * 100) for n in nns))
s = s.replace("White's names and forms", "White's names and forms")
s += "\nWhite's names and forms of address (story/voice/names.md; \"Mr. Smith\") are the house rule, never a finding. Verne's own explanations, repeats and exclamations are the text: in a patched or rendered chapter, flag a line only for how it is said, never for saying what the French says.\n"
assert '00500' not in s and '05600' not in s
open(out, 'w', encoding='utf-8').write('# The voice critic for %s (from the pilot\'s voice prompt)\n%s' % (', '.join(cite(n) for n in nns), s))
print('ok', files)
