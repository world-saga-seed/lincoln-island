#!/usr/bin/env python3
"""Derive the paragraph-numbered working text of a French Wikisource chapter set.

Reads existing/<src>/raw/NN.html and manifest.json (never changes them) and writes
texts/<out>/NN.md, one paragraph a line:

  hd [p.1] a heading (the part's, the chapter's number and title; ' / ' a line break)
  ¶0 [p.1] the chapter's summary (the argument under the heading)
  ¶1 [p.1] « Remontons-nous ?
  ...
  ## Notes
  n1 [¶12] the footnote's text

¶N is the citation number: part I, chapter 1, paragraph 12 is cited "I.1 ¶12".
[p.N] is the djvu page the paragraph starts on (Wikisource's pagenum anchor).
A footnote's marker in the text reads [n1]. Kept as Wikisource gives it: the
corrected reading of a printer's error (class "coquille"), each one listed in
texts/<out>/corrections.tsv with the print's reading. Kept apart, under "Plates and loose lines": text outside any paragraph,
Férat's plate captions (pl) and lines such as a part's end (ln), each with the
paragraph it follows. Dropped: Wikisource's own
additions (ws-noexport blocks, headers, footers, styles), the figures, the
footnote back-links, the page anchors themselves. Changed: U+00A0, U+202F and
U+2009 become a plain space and runs of spaces become one; nothing else.

Usage: python3 texts/derive_fr.py SRC OUT PARTS
  SRC    folder under existing/, e.g. hetzel-1875
  OUT    folder under texts/, e.g. fr-1875
  PARTS  chapters per part, comma-separated, e.g. 22,20,20
"""
import html.parser, json, os, re, sys

ROMAN = ['I', 'II', 'III', 'IV']
SPACES = re.compile(r'[    \t\r\n]+')


class Chapter(html.parser.HTMLParser):
    VOID = {'br', 'img', 'hr', 'link', 'meta', 'wbr', 'input', 'source'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, skip, role)
        self.blocks = []         # (kind, page, text)
        self.notes = []
        self.cur = None          # list of text pieces of the open block
        self.kind = None
        self.page = None
        self.cur_page = None
        self.corrections = []
        self.coq = None
        self.loose = []          # (kind, after_paragraph_count, page, text)
        self.last_fig = False
        self.brk = False
        self.newitem = False

    def skipping(self):
        return any(s for _, s, _ in self.stack)

    def role(self, r):
        return any(x == r for _, _, x in self.stack)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '') or ''
        if 'pagenum' in cls:
            self.page = a.get('id')
            if self.cur is not None and not ''.join(self.cur).strip():
                self.cur_page = self.page
        if tag in self.VOID:
            if tag == 'br' and self.cur is not None:
                self.cur.append(' / ' if self.role('poem') else ' ')
            return
        if tag in ('div', 'p', 'br', 'li', 'tr', 'td', 'table', 'figure', 'hr', 'dd', 'dl'):
            self.brk = True
        if tag == 'figure':
            self.newitem = True
        if tag in ('div', 'li', 'td', 'dd') and self.cur is not None:
            self.cur.append(' / ' if self.kind == 'heading' else ' ')
        if tag == 'figure':
            self.last_fig = True
        elif tag == 'p':
            self.last_fig = False
        skip = ('ws-noexport' in cls or tag in ('style', 'script', 'figure')
                or 'mw-cite-backlink' in cls or 'cite-bracket' in cls)
        role = None
        if tag == 'ol' and 'references' in cls:
            role = 'refs'
        elif tag == 'li' and self.role('refs'):
            role = 'note'
            self.open_block('note')
        elif 'reference-text' in cls:
            role = 'reftext'
        elif tag == 'sup' and 'reference' in cls:
            role = 'marker'
        elif 'coquille' in cls:
            role = 'coquille'
            self.coq = [a.get('title', ''), []]
        elif 'poem' in cls:
            role = 'poem'
        elif tag in ('h2', 'h3'):
            role = 'heading'
            self.close_block()
            self.cur, self.kind, self.cur_page = [], 'heading', self.page
        elif tag == 'p' and not self.role('refs') and not self.role('poem'):
            self.open_block('p')
        elif tag == 'div' and 'alineanegatif' in cls:
            self.open_block('summary')
        elif tag == 'tr' and not self.skipping():
            self.open_block('row')
        elif tag == 'div' and 'poem' in cls:
            self.open_block('poem')
        self.stack.append((tag, skip, role))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if tag in ('div', 'p', 'li', 'tr', 'td', 'table', 'figure', 'dd', 'dl'):
            self.brk = True
        while self.stack:
            t, _, role = self.stack.pop()
            if role == 'coquille' and self.coq:
                self.corrections.append((self.coq[0], ''.join(self.coq[1])))
                self.coq = None
            if role == 'poem' or (t == tag and role == 'note'):
                self.close_block()
            if t == tag:
                break
        if tag in ('p', 'tr', 'h2', 'h3') or (tag == 'div' and self.kind == 'summary'):
            self.close_block()

    def handle_data(self, data):
        if self.skipping():
            return
        if self.role('marker'):
            d = data.strip()
            if d and self.cur is not None:
                self.cur.append(f'[n{d}]')
            return
        if self.coq is not None:
            self.coq[1].append(data)
        if self.cur is not None:
            if self.role('refs') and not self.role('reftext'):
                return
            self.cur.append(data)
        elif data.strip() and not self.role('refs'):
            n = len(self.blocks)
            kind = 'plate' if self.last_fig else 'line'
            if self.loose and self.loose[-1][1] == n and self.loose[-1][0] == kind and not self.newitem:
                k, a, pg, t = self.loose[-1]
                self.loose[-1] = (k, a, pg, t + (' / ' if self.brk else '') + data)
            else:
                self.loose.append((kind, n, self.page, data))
            self.brk = self.newitem = False

    def open_block(self, kind):
        if self.cur is not None and kind == 'p' and self.kind == 'poem':
            return
        self.close_block()
        self.cur, self.kind, self.cur_page = [], kind, self.page

    def close_block(self):
        if self.cur is None:
            return
        text = SPACES.sub(' ', ''.join(self.cur)).strip()
        if text:
            if self.kind == 'note':
                self.notes.append(text)
            else:
                self.blocks.append((self.kind, self.cur_page, text))
        self.cur, self.kind = None, None


def main():
    src, out, parts = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
    raw = os.path.join('existing', src, 'raw')
    man = json.load(open(os.path.join(raw, 'manifest.json'), encoding='utf-8'))
    od = os.path.join('texts', out)
    os.makedirs(od, exist_ok=True)
    cites, n = [], 0
    for p, k in enumerate(parts):
        for c in range(1, k + 1):
            cites.append((ROMAN[p], c))
    corr = ['file\tcite\tprint\twikisource']
    index = []
    for e in man:
        part, ch = cites[e['n'] - 1]
        ch_ = Chapter()
        ch_.feed(open(os.path.join(raw, e['file']), encoding='utf-8').read())
        ch_.close_block()
        lines, num, rows = [], 0, []
        pmap = [0]                      # pmap[i]: the paragraph number reached after block i-1
        for kind, page, text in ch_.blocks:
            pmap.append(num + (1 if kind not in ('summary', 'heading') and not (kind == 'row' and rows) else 0))
            if kind == 'row':           # a table, kept as one paragraph, rows joined by " | "
                rows.append(text)
                continue
            if rows:
                num += 1
                lines.append(f'¶{num} [p.{rows_page}] ' + ' | '.join(rows))
                rows = []
            if kind == 'heading':
                lines.append(f'hd [p.{page}] {text}')
                continue
            if kind == 'summary':
                lines.append(f'¶0 [p.{page}] {text}')
                continue
            num += 1
            lines.append(f'¶{num} [p.{page}] {text}')
            rows_page = page
        if rows:
            num += 1
            lines.append(f'¶{num} [p.{rows_page}] ' + ' | '.join(rows))
        # a row block's page: the page of the paragraph before it is good enough
        notes = []
        for i, t in enumerate(ch_.notes, 1):
            where = next((ln.split(' ', 1)[0] for ln in lines if f'[n{i}]' in ln), '?')
            notes.append(f'n{i} [{where}] {t}')
        # loose text outside any paragraph: Férat's plate captions, and lines such as a part's end.
        # "after" counts blocks; turn it into the paragraph number it follows.
        loose = []
        for i, (kind, after, page, t) in enumerate(ch_.loose, 1):
            after = pmap[after]
            t = SPACES.sub(' ', t).strip()
            if t:
                loose.append(f'{"pl" if kind == "plate" else "ln"}{i} [after ¶{after}, p.{page}] {t}')
        name = e['file'].replace('.html', '.md')
        head = (f'# {e["title"]}\n\n'
                f'*Cited as {part}.{ch} ¶N. From `existing/{src}/raw/{e["file"]}`, revid {e["revid"]}, '
                f'by `texts/derive_fr.py`; vetted by `texts/vet_fr.py`. [p.N] is the djvu page.*\n\n')
        body = '\n'.join(lines) + '\n'
        if notes:
            body += '\n## Notes\n\n' + '\n'.join(notes) + '\n'
        if loose:
            body += '\n## Plates and loose lines\n\n' + '\n'.join(loose) + '\n'
        open(os.path.join(od, name), 'w', encoding='utf-8').write(head + body)
        for pr, ws in ch_.corrections:
            corr.append(f'{name}\t{part}.{ch}\t{pr}\t{SPACES.sub(" ", ws).strip()}')
        index.append(f'| [{part}.{ch}]({name}) | {num} | {len(notes)} |')
    open(os.path.join(od, 'corrections.tsv'), 'w', encoding='utf-8').write('\n'.join(corr) + '\n')
    open(os.path.join(od, 'INDEX.md'), 'w', encoding='utf-8').write(
        '| Chapter | Paragraphs | Notes |\n|---|---|---|\n' + '\n'.join(index) + '\n')
    print(len(man), 'chapters;', len(corr) - 1, 'corrections')


if __name__ == '__main__':
    main()
