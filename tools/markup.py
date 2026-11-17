"""The markup page for one chapter: whose beat each passage carries, and the clues, as local HTML.

    python3 tools/markup.py items CHAPTER [--author-written 00100,00200]   what the locators look for
    python3 tools/markup.py render CHAPTER                                 the page, from the locators' finds

Run from the book's top folder. The items and finds go under tmp/markup/, the page to build/markup/; keep
both out of git, and keep the page on your machine. The workflow is plan/workflows/markup.md.

The prose is a placeholder for whoever writes it last; what the page marks is the beat each passage carries
and who gave it. Text colour: a **keyframe** (its source is the writer's: a ledger row of kind
settled-author, an outline or notes bullet marked as settled by the writer, the writer's key frames), an
**assisted** beat (a recommendation, a judgment, a proposal), or a **tween** (no source: the model's own,
between frames). Highlights from the clue register (plan/reread-hooks.md): pink a red herring (an ID
starting FP, or "herring" in the row), blue foreshadowing, green a structural puzzle (by a Kind or Colour
column if the register has one: body, motif, word or foreshadow are blue; anything else green). Lore, a card
the outline or notes link, is a dotted underline. Every marked span carries a tooltip with its source.

--author-written lists chapters the writer wrote whole before their outlines were taken from them: every
beat in their outline and notes counts as a keyframe unless the bullet says it is a proposal.
"""
import collections, glob, html, json, os, re, subprocess, sys

TMP, OUT = 'tmp/markup', 'build/markup'
ID = re.compile(r'\b[A-Z]\d{4}-\d+\b')
HOOK_COLOUR = {'body': 'foreshadow', 'motif': 'foreshadow', 'word': 'foreshadow', 'foreshadow': 'foreshadow', 'herring': 'herring',
               'rule': 'puzzle', 'count': 'puzzle', 'name': 'puzzle'}
AUTHOR = re.compile(r'settled by the (?:author|writer)|the (?:author|writer)\'s (?:key ?frames?|frames|word|ruling|pitch|dictation)|confirmed by the (?:author|writer)|dictated', re.I)
AUTHOR_WRITTEN = set()  # set by --author-written
ASSIST = re.compile(r'proposal|my reading|on the recommendation|settled in discussion|settled by judgment|recommend', re.I)


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()


def plain(s):
    return re.sub(r'\*+', '', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s))


# ---- the sources -----------------------------------------------------------------------------------

def chapter_files(ch):
    prose = sorted(p for p in glob.glob(f'story/prose/{ch}-*.md') if not re.match(rf'{ch}-F\d', os.path.basename(p)))
    if not prose:
        sys.exit(f'no prose for {ch}')
    outline = sorted(glob.glob(f'story/outline/{ch}-*.md'))
    notes = sorted(glob.glob(f'story/notes/{ch}-*.md'))
    return prose[0], (outline[0] if outline else None), (notes[0] if notes else None)


def outline_text(path):
    """The outline; a retired one is read from the tag it names."""
    if not path:
        return ''
    t = open(path, encoding='utf-8').read()
    m = re.search(r'`git show ([\w.-]+):([\w/.-]+)`', t)
    if 'retired' in t.split('\n', 1)[0] and m:
        r = subprocess.run(['git', 'show', f'{m.group(1)}:{m.group(2)}'], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
    return t


def ledger():
    rows = {}
    for f in sorted(glob.glob('plan/settled/ledger/*.md')):
        for line in open(f, encoding='utf-8'):
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(c) >= 3 and ID.fullmatch(c[0]):
                rows[c[0]] = (c[1], plain(c[2]), os.path.basename(f))
    return rows


def origin(text, ids, rows, head=''):
    """keyframe when the author gave it, assisted when it came from a recommendation, discussion or proposal."""
    if AUTHOR.search(text) or 'author' in head.lower() and 'key' in head.lower():
        return 'keyframe'
    kinds = [rows[i][0] for i in ids if i in rows]
    if any(k == 'settled-author' for k in kinds):
        return 'keyframe'
    return 'assisted'


def hooks(ch, rows):
    """The clue register's rows that name the chapter: (id, colour, text, origin)."""
    out, col = [], None
    if not os.path.exists('plan/reread-hooks.md'):
        return out
    for line in open('plan/reread-hooks.md', encoding='utf-8'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if c and c[0] == 'ID':
            heads = [x.lower() for x in c]
            col = next((i for i, h in enumerate(heads) if h in ('kind', 'colour', 'color')), None)
            continue
        if len(c) < 3 or not re.fullmatch(r'[A-Z]+-?\d+', c[0]) or ch not in line:
            continue
        kind = c[col].lower() if col is not None and col < len(c) else ''
        colour = 'herring' if c[0].startswith('FP') or 'herring' in c[1].lower() else HOOK_COLOUR.get(kind, 'puzzle')
        out.append((c[0], colour, plain(c[1])[:400], origin(line, ID.findall(line), rows)))
    return out


def items(ch):
    prose, outline, notes = chapter_files(ch)
    ot = outline_text(outline)
    nt = open(notes, encoding='utf-8').read() if notes else ''
    rows = ledger()
    src = {}  # item id -> {head, text, ids, origin}
    lines = [f'# Items for {ch}', '', f'Chapter: {prose}. Find each item on the page; give the exact words that carry it.', '',
             '## Puzzle box (hooks)', '']
    hk = hooks(ch, rows)
    for hid, colour, text, org in hk:
        src[hid] = {'head': 'the clue ledger', 'text': text, 'ids': [], 'origin': org}
        lines.append(f'- {hid} [{colour}]: {text}')
    for label, text in (('outline', ot), ('notes', nt)):
        lines += ['', f'## Plot and background ({label} bullets; each is a source)', '']
        head = ''
        for n, l in enumerate(text.split('\n'), 1):
            if l.startswith('#'):
                head = plain(l.lstrip('#').strip())
                continue
            m = re.match(r'^\s*(?:[-*]|\d+\.)\s+(.*)', l)
            if not m or len(m.group(1)) < 30:
                continue
            t = plain(m.group(1))
            ids = sorted(set(ID.findall(l)))
            k = f'{label}:{n}'
            org = 'keyframe' if ch in AUTHOR_WRITTEN and not ASSIST.search(l) else origin(l, ids, rows, head)
            src[k] = {'head': head, 'text': t[:500], 'ids': ids, 'origin': org}
            lines.append(f'- {k} [{"plot" if label == "outline" else "decision"}] ({head[:60]}){" " + ",".join(ids) if ids else ""}: {t[:300]}')
    lines += ['', '## Lore (cards the outline and notes link)', '']
    seen = set()
    for link in re.findall(r'\]\(((?:\.\./)+world/[^)#]+\.md)', ot + nt):
        p = os.path.normpath(os.path.join('story/outline', link))
        if p in seen or not os.path.exists(p):
            continue
        seen.add(p)
        L = open(p, encoding='utf-8').read().split('\n') + ['', '', '']
        what = f'{plain(L[0].lstrip("# "))}. {plain(L[2].strip("*"))}'
        src[f'card {p}'] = {'head': 'card', 'text': what, 'ids': [], 'origin': None}
        lines.append(f'- card {p} [lore]: {what}')
    lines += ['', '## Decisions (ledger rows)', '']
    keys = set(ID.findall(ot + nt)) | {k for k, (_, t, _) in rows.items() if ch in t}
    for k in sorted(keys & set(rows)):
        src[k] = {'head': f'ledger {rows[k][2]}', 'text': rows[k][1][:500], 'ids': [k],
                  'origin': 'keyframe' if rows[k][0] == 'settled-author' else 'assisted'}
        lines.append(f'- {k} [decision]: {rows[k][1][:400]}')
    os.makedirs(f'{TMP}/{ch}', exist_ok=True)
    json.dump(src, open(f'{TMP}/{ch}/sources.json', 'w'))
    p = f'{TMP}/{ch}/items.md'
    open(p, 'w').write('\n'.join(lines) + '\n')
    orgs = collections.Counter(v['origin'] for v in src.values() if v['origin'])
    print(f'{p}: {len(src)} items ({len(hk)} hooks, {len(seen)} cards, {len(keys & set(rows))} ledger rows); '
          f'{orgs["keyframe"]} keyframe sources, {orgs["assisted"]} assisted')


# ---- the page ---------------------------------------------------------------------------------

FIND = re.compile(r'^\s*-\s*(?:id:\s*)?(?P<id>[^|]+?)\s*\|\s*(?:layer:\s*)?(?P<layer>\w+)\s*\|\s*(?:quote:\s*)?(?P<quote>.+?)\s*(?:\|\s*(?:note:\s*)?(?P<note>.*))?$')
LAYERS = ('decision', 'plot', 'lore', 'herring', 'foreshadow', 'puzzle')


def finds(ch):
    out = []
    for f in sorted(glob.glob(f'{TMP}/{ch}/finds-*.md')):
        for line in open(f, encoding='utf-8'):
            m = FIND.match(line)
            if m and m.group('layer').lower() in LAYERS and m.group('quote').strip().strip('`').lower() not in ('none', 'not on the page'):
                q = m.group('quote').strip().strip('`').strip('"“”')
                out.append((m.group('id').strip(), m.group('layer').lower(), q, (m.group('note') or '').strip()))
    return out


def paragraphs(path):
    """(line no, kind, text, italic flags), the markdown emphasis taken out and kept as flags."""
    out = []
    for n, l in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if l.startswith('## Notes'):
            break
        if not l.strip() or l.startswith('<!--') or (l.startswith('*(') and l.endswith(')*')):
            continue
        kind = 'h1' if l.startswith('# ') else 'h2' if l.startswith('## ') else 'p'
        t = l.lstrip('#').strip() if kind != 'p' else l
        text, ital, on = [], [], False
        for c in t:
            if c == '*':
                on = not on
                continue
            text.append(c); ital.append(on)
        out.append((n, kind, ''.join(text), ital))
    return out


def place(q, paras):
    """(paragraph, start, end) of the quote, matched with spaces and quote marks normalized."""
    nq = norm(q.replace('*', '')).lower()
    for pi, (_, _, text, _) in enumerate(paras):
        idx, buf = [], []
        for i, c in enumerate(text):
            if c.isspace() and buf and buf[-1] == ' ':
                continue
            buf.append(' ' if c.isspace() else c); idx.append(i)
        k = norm(''.join(buf)).lower().find(nq)
        if k >= 0:
            lead = len(''.join(buf)) - len(''.join(buf).lstrip())
            k += lead
            return pi, idx[k], idx[min(k + len(nq), len(idx)) - 1] + 1
    return None


def render(ch):
    prose, _, _ = chapter_files(ch)
    sp = f'{TMP}/{ch}/sources.json'
    srcs = json.load(open(sp)) if os.path.exists(sp) else {}
    paras = paragraphs(prose)
    anns, marks, missing = finds(ch), collections.defaultdict(list), []
    for ai, (aid, layer, q, note) in enumerate(anns):
        at = place(q, paras)
        if at:
            marks[at[0]].append((at[1], at[2], ai))
        else:
            missing.append((aid, layer, q))
    counts, body = collections.Counter(), []
    for pi, (n, kind, text, ital) in enumerate(paras):
        L = len(text)
        on = [set() for _ in range(L)]
        for s, e, ai in marks.get(pi, []):
            for j in range(s, min(e, L)):
                on[j].add(ai)
        out, j = [], 0
        while j < L:
            key = (frozenset(on[j]), ital[j])
            k = j
            while k < L and (frozenset(on[k]), ital[k]) == key:
                k += 1
            ais, it = key
            seg = html.escape(text[j:k], quote=False)
            if it:
                seg = f'<em>{seg}</em>'
            layers = {anns[a][1] for a in ais}
            orgs = {srcs.get(anns[a][0], {}).get('origin') for a in ais if anns[a][1] not in ('lore',)}
            beat = 'keyframe' if 'keyframe' in orgs else 'assisted' if orgs - {None} or layers & {'decision', 'plot'} else 'tween'
            if kind == 'p':
                counts[beat] += k - j
            cls = ([beat] if beat != 'tween' else []) + [x for x in ('herring', 'foreshadow', 'puzzle') if x in layers] + (['lore'] if 'lore' in layers else [])
            tips = []
            for a in sorted(ais):
                aid, layer, q, note = anns[a]
                s = srcs.get(aid, {})
                where = (f'{aid.split(":")[0]} file, line {aid.split(":")[1]}' if ':' in aid and not aid.startswith('card')
                         else aid[5:] if aid.startswith('card ') else f'grep -n "{aid}" plan/settled/ledger/*.md plan/reread-hooks.md')
                ids = f' ({", ".join(s["ids"])})' if s.get('ids') and s['ids'] != [aid] else ''
                tips.append(f'{aid} · {layer}{" · " + s["origin"] if s.get("origin") else ""}\n'
                            f'{("[" + s["head"] + "] ") if s.get("head") else ""}{s.get("text", "")[:280]}{ids}'
                            f'{chr(10) + "on the page: " + note if note else ""}\nfind: {where}')
            if cls or tips:
                attr = f' data-tip="{html.escape(chr(10).join(tips))}" tabindex="0"' if tips else ''
                seg = f'<span class="{" ".join(cls)}"{attr}>{seg}</span>'
            out.append(seg)
            j = k
        body.append(f'<{kind} id="L{n}"><a class="ln" href="#L{n}">{n}</a>{"".join(out)}</{kind}>')
    total = sum(counts.values()) or 1
    share = ' · '.join(f'{k} {100 * counts[k] / total:.0f}%' for k in ('keyframe', 'assisted', 'tween'))
    miss = ''.join(f'<li><code>{html.escape(a)}</code> ({l}): “{html.escape(q[:120])}”</li>' for a, l, q in missing)
    page = PAGE.format(ch=ch, share=share, n=len(anns) - len(missing), body='\n'.join(body),
                       missing=f'<details><summary>{len(missing)} finds not on the page (dropped)</summary><ul>{miss}</ul></details>' if missing else '')
    os.makedirs(OUT, exist_ok=True)
    p = f'{OUT}/{ch}.html'
    open(p, 'w', encoding='utf-8').write(page)
    print(f'{p}: {len(anns) - len(missing)} finds placed, {len(missing)} dropped; {share}')


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Markup {ch}</title><style>
:root {{ --bg:#fbfaf7; --fg:#2b2b2b; --muted:#888; --tween:#8a8a8a; --keyframe:#1d4ed8; --assisted:#7a5418;
  --herring:#fbd3e9; --foreshadow:#cfe3ff; --puzzle:#cdeccf; --tipbg:#222; --tipfg:#f4f4f4; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#161616; --fg:#e6e6e6; --muted:#888; --tween:#9a9a9a;
  --keyframe:#8ab4ff; --assisted:#e0c48a; --herring:#5a2440; --foreshadow:#1e3a5f; --puzzle:#1f4a2a; --tipbg:#f0f0f0; --tipfg:#111; }} }}
:root[data-theme="dark"] {{ --bg:#161616; --fg:#e6e6e6; --muted:#888; --tween:#9a9a9a; --keyframe:#8ab4ff; --assisted:#e0c48a;
  --herring:#5a2440; --foreshadow:#1e3a5f; --puzzle:#1f4a2a; --tipbg:#f0f0f0; --tipfg:#111; }}
body {{ background:var(--bg); color:var(--tween); font:17px/1.6 Georgia, serif; max-width:42em; margin:0 auto; padding:1em 16px 4em; }}
h1,h2 {{ color:var(--fg); font-weight:normal; }}
p {{ margin:0 0 .9em; position:relative; }}
.ln {{ position:absolute; left:-3em; width:2.5em; text-align:right; color:var(--muted); font:11px/2 sans-serif; text-decoration:none; }}
@media (max-width:52em) {{ .ln {{ position:static; display:inline-block; width:auto; margin-right:.5em; }} }}
.keyframe {{ color:var(--keyframe); }} .assisted {{ color:var(--assisted); }}
.herring {{ background:var(--herring); }} .foreshadow {{ background:var(--foreshadow); }} .puzzle {{ background:var(--puzzle); }}
.lore {{ text-decoration:underline dotted; text-underline-offset:3px; }}
[data-tip] {{ position:relative; cursor:help; }}
[data-tip]:hover::after, [data-tip]:focus::after {{ content:attr(data-tip); position:absolute; left:0; top:1.6em; z-index:9; width:min(30em,80vw);
  white-space:pre-line; background:var(--tipbg); color:var(--tipfg); font:13px/1.4 sans-serif; padding:.6em .8em; border-radius:6px; }}
.legend {{ font:13px/1.8 sans-serif; color:var(--fg); border-bottom:1px solid var(--muted); padding-bottom:.6em; margin-bottom:1.5em; }}
.legend span {{ padding:0 .3em; margin-right:.6em; }}
details {{ font:13px sans-serif; color:var(--muted); margin-top:3em; }}
</style></head><body>
<div class="legend"><b>Markup {ch}</b> · beats: {share} · {n} finds<br>
<span class="keyframe">keyframe (the writer's beat)</span><span class="assisted">assisted beat</span><span style="color:var(--tween)">tween</span>
<span class="herring">red herring</span><span class="foreshadow">foreshadowing</span><span class="puzzle">structural puzzle</span><span class="lore">lore</span><br>
The prose is a placeholder for whoever writes it last; the colours show whose beat each passage carries.</div>
{body}
{missing}
</body></html>
"""

if __name__ == '__main__':
    a = sys.argv[1:]
    if '--author-written' in a:
        i = a.index('--author-written')
        AUTHOR_WRITTEN.update(x.strip() for x in a[i + 1].split(',') if x.strip())
        del a[i:i + 2]
    if len(a) < 2 or a[0] not in ('items', 'render') or a[0] == '--help':
        sys.exit(__doc__)
    (items if a[0] == 'items' else render)(a[1])
