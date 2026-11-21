#!/usr/bin/env python3
"""Derive the paragraph-numbered working text of White's 1876 translation.

Reads existing/white-1876/8misl10h.htm (never changes it) and writes
texts/white-1876/NN.md for its 62 chapters, in the same form as the French:

  hd PART I / SHIPWRECKED IN THE AIR      a heading (a part's, the chapter's)
  ¶0 THE HURRICANE OF 1865—CRIES ...      the chapter's summary (its first paragraph, in capitals)
  ¶1 “Are we going up again?”

Cited as "White XII ¶N" (the chapter's number as White prints it, I to LXII).
The text runs from the heading "THE MYSTERIOUS ISLAND." after the contents to
"END OF TRANSLATION OF THE MYSTERIOUS ISLAND"; Gutenberg's header and footer,
the redactor's note, the title page and the contents are left out. A chapter's
first paragraph is taken as its summary only when it has no lower-case letter.
Changed: &nbsp; becomes a plain space and runs of spaces become one; nothing else.
White has no page numbers in this file, so there is no [p.N].

Usage: python3 texts/derive_white.py
"""
import html.parser, os, re

SRC = 'existing/white-1876/8misl10h.htm'
OUT = 'texts/white-1876'
SPACES = re.compile(r'[  \t\r\n]+')
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50}


def roman(s):
    n = 0
    for a, b in zip(s, s[1:] + ' '):
        v = ROMAN[a]
        n += -v if b in ROMAN and ROMAN[b] > v else v
    return n


class White(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.on = False
        self.done = False
        self.blocks = []        # (kind, text)
        self.cur = None
        self.kind = None

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'h4', 'h3', 'td'):
            self.close()
            self.cur, self.kind = [], 'hd' if tag in ('h4', 'h3') else 'p'
        elif tag == 'br' and self.cur is not None:
            self.cur.append(' / ')

    def handle_endtag(self, tag):
        if tag in ('p', 'h4', 'h3', 'td'):
            self.close()

    def handle_data(self, data):
        if self.cur is not None:
            self.cur.append(data)

    def close(self):
        if self.cur is None:
            return
        t = SPACES.sub(' ', ''.join(self.cur)).strip()
        self.cur = None
        if not t:
            return
        if self.kind == 'hd' and t == 'THE MYSTERIOUS ISLAND.':
            self.on = True
        if self.on and not self.done:
            self.blocks.append((self.kind, t))
        if self.kind == 'hd' and t.startswith('END OF TRANSLATION'):
            self.done = True


def main():
    w = White()
    w.feed(open(SRC, encoding='utf-8').read())
    w.close()
    os.makedirs(OUT, exist_ok=True)
    chapters, pending_hd, front = [], [], []
    for kind, t in w.blocks:
        m = re.fullmatch(r'CHAPTER ([IVXL]+)\.?', t) if kind == 'hd' else None
        if m:
            chapters.append({'n': roman(m.group(1)), 'roman': m.group(1), 'hd': pending_hd + [t], 'p': []})
            pending_hd = []
        elif kind == 'hd':
            if t.startswith('END OF TRANSLATION'):
                chapters[-1]['end'] = t
            else:
                pending_hd.append(t)
        elif chapters:
            chapters[-1]['p'].append(t)
        else:
            front.append(t)
    assert [c['n'] for c in chapters] == list(range(1, 63)), [c['n'] for c in chapters]
    index = ['| Chapter | Paragraphs | Summary |', '|---|---|---|']
    for c in chapters:
        lines = []
        # a part's heading met before this chapter's own: "PART I", then its title
        hds = c['hd']
        heads = [h for h in hds if h not in ('THE MYSTERIOUS ISLAND.', 'By JULES VERNE.')]
        for h in hds:
            if h in ('THE MYSTERIOUS ISLAND.', 'By JULES VERNE.'):
                lines.append(f'hd {h}')
        part = [h for h in heads[:-1]]
        if part:
            lines.append('hd ' + ' / '.join(part))
        lines.append('hd ' + heads[-1])
        ps = c['p']
        summary = bool(ps) and not re.search(r'[a-z]', ps[0])
        k = 0
        for i, t in enumerate(ps):
            if i == 0 and summary:
                lines.append(f'¶0 {t}')
            else:
                k += 1
                lines.append(f'¶{k} {t}')
        if 'end' in c:
            lines.append(f'hd {c["end"]}')
        name = f'{c["n"]:02d}.md'
        head = (f'# White, chapter {c["roman"]}\n\n*Cited as White {c["roman"]} ¶N. From `{SRC}` '
                f'by `texts/derive_white.py`; vetted by `texts/vet_white.py`.*\n\n')
        open(os.path.join(OUT, name), 'w', encoding='utf-8').write(head + '\n'.join(lines) + '\n')
        index.append(f'| [{c["roman"]}]({name}) | {k} | {"yes" if summary else "no"} |')
    open(os.path.join(OUT, 'INDEX.md'), 'w', encoding='utf-8').write('\n'.join(index) + '\n')
    print(len(chapters), 'chapters,', sum(len(c['p']) for c in chapters), 'paragraphs; front matter kept out:', len(front))


if __name__ == '__main__':
    main()
