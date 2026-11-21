#!/usr/bin/env python3
"""A session's token totals, from its Claude Code transcript, for the token log.

Usage:
  python3 tools/tokens.py TRANSCRIPT.jsonl [MORE.jsonl ...] [--step "session close"]
                          [--since 2026-11-20T09:00] [--until 2026-11-20T18:00]
                          [--log plan/tokens.md] [--append]

Reads each transcript (one JSON object a line, as Claude Code writes them under
~/.claude/projects/) and sums the usage of every model call in it: input,
cache written, cache read and output tokens. A call written as several lines
(one per content block) is counted once, by its message id. Calls made inside
the session by its agents (sidechain lines) are summed apart and shown on
their own line; an agent whose calls live in a transcript of its own is added
by naming that file too. --since and --until (ISO times; a time with no zone
is read as local) keep only the calls between them: to count part of a session,
such as the turns on one book. Minutes run from the first kept call to the last.

Prints the totals, by model, and the row for the token log. With --append, adds
that row to the end of --log (it must exist, from plan/templates/tokens.md).
Nothing else is changed. Exit 0; exit 1 when no call was found.
"""
import argparse, json, os, sys
from datetime import datetime

FIELDS = ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens', 'output_tokens')
SHORT = ('in', 'cache write', 'cache read', 'out')


def parse_time(s):
    """An aware datetime, or None; a time with no zone is local."""
    try:
        t = datetime.fromisoformat(s.replace('Z', '+00:00'))
    except (AttributeError, TypeError, ValueError):
        return None
    return t if t.tzinfo else t.astimezone()


def calls(paths, since=None, until=None):
    """Yield (id, model, sidechain, timestamp, usage) once per model call."""
    seen = set()
    for p in paths:
        with open(p, encoding='utf-8') as f:
            for n, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                except ValueError:
                    print(f'{p}:{n}: not JSON, skipped', file=sys.stderr)
                    continue
                if d.get('type') != 'assistant':
                    continue
                m = d.get('message') or {}
                u = m.get('usage')
                if not u:
                    continue
                key = m.get('id') or d.get('requestId') or d.get('uuid')
                if key in seen:
                    continue
                ts = parse_time(d.get('timestamp'))
                if (since or until) and ts is None:
                    continue
                if since and ts < since:
                    continue
                if until and ts > until:
                    continue
                seen.add(key)
                yield key, m.get('model', '?'), bool(d.get('isSidechain')), ts, u


def total(rows):
    t = dict.fromkeys(FIELDS, 0)
    for u in rows:
        for k in FIELDS:
            t[k] += u.get(k) or 0
    return t


def fmt(t):
    parts = ' · '.join(f'{s} {t[k]:,}' for k, s in zip(FIELDS, SHORT))
    return f'{sum(t.values()):,} ({parts})'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('transcripts', nargs='+')
    ap.add_argument('--step', default='session', help='the Step cell of the row')
    ap.add_argument('--chapter', default='', help='the Chapter cell of the row')
    ap.add_argument('--since', help='keep calls at or after this ISO time')
    ap.add_argument('--until', help='keep calls at or before this ISO time')
    ap.add_argument('--log', default='plan/tokens.md')
    ap.add_argument('--append', action='store_true', help='add the row to --log')
    a = ap.parse_args()

    since, until = parse_time(a.since), parse_time(a.until)
    for given, t in ((a.since, since), (a.until, until)):
        if given and t is None:
            ap.error(f'not an ISO time: {given}')
    found = list(calls(a.transcripts, since, until))
    if not found:
        print('no model calls found')
        return 1
    main_rows = [c[4] for c in found if not c[2]]
    side_rows = [c[4] for c in found if c[2]]
    everything = total(c[4] for c in found)
    times = [c[3] for c in found if c[3]]
    minutes = round((max(times) - min(times)).total_seconds() / 60) if times else ''
    date = min(times).astimezone().date().isoformat() if times else ''

    print(f'calls: {len(found)} ({len(main_rows)} main thread, {len(side_rows)} agents in the thread)')
    print(f'main thread: {fmt(total(main_rows))}')
    if side_rows:
        print(f'agents:      {fmt(total(side_rows))}')
    print(f'all:         {fmt(everything)}')
    for model in sorted({c[1] for c in found}):
        print(f'  {model}: {fmt(total(c[4] for c in found if c[1] == model))}')
    print(f'minutes: {minutes}')

    reading = 'transcript ' + ', '.join(os.path.basename(p) for p in a.transcripts)
    if a.since or a.until:
        reading += f" ({a.since or ''} to {a.until or ''})"
    row = (f'| {date} | session | {a.step} | {a.chapter} |  | {reading} | '
           f'{fmt(everything)} | {len(found)} | {minutes} |')
    print(row)
    if a.append:
        if not os.path.exists(a.log):
            print(f'{a.log}: not found; copy plan/templates/tokens.md there first', file=sys.stderr)
            return 1
        with open(a.log, encoding='utf-8') as f:
            text = f.read()
        with open(a.log, 'a', encoding='utf-8') as f:
            f.write(('' if text.endswith('\n') else '\n') + row + '\n')
        print(f'appended to {a.log}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
