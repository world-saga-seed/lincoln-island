#!/usr/bin/env python3
"""Check that no file holds an absolute local path.

A path like /home/<name>/..., /Users/<name>/..., C:\\Users\\<name>\\... or a
session scratchpad under /tmp/claude-<n>/ names the machine and the person who
ran the work, and breaks on every other machine. Inside the repository a path
is written relative to its root; a scratchpad is named "<scratchpad>".

This check lists each hit as file:line with the path found, and exits 1 on any
hit; otherwise it prints "clean" and exits 0. Run it before every commit that
saves an agent's prompt or report, and before a release.

Usage:
  python3 tools/check_paths.py [--root DIR]

  --root DIR   the book's top folder (default: the current folder)

It scans the files git tracks (or, outside a git checkout, every file under
the root but .git/), skips binary files, and does not scan itself.
"""
import argparse, os, re, subprocess, sys

PATTERNS = [
    re.compile(r'/home/[A-Za-z0-9._-]+/'),
    re.compile(r'/Users/[A-Za-z0-9._-]+/'),
    re.compile(r'[A-Za-z]:[\\/]+Users[\\/]+[A-Za-z0-9._ -]+'),
    re.compile(r'/tmp/claude-[0-9]+/'),
    re.compile(r'/root/'),
]


def files(root):
    try:
        out = subprocess.run(['git', '-C', root, 'ls-files', '-z'], capture_output=True,
                             check=True).stdout.decode('utf-8', 'replace')
        return [f for f in out.split('\0') if f]
    except (subprocess.CalledProcessError, FileNotFoundError):
        found = []
        for d, dirs, names in os.walk(root):
            dirs[:] = [x for x in dirs if x != '.git']
            found += [os.path.relpath(os.path.join(d, n), root) for n in names]
        return found


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', default='.')
    args = ap.parse_args()
    me = os.path.realpath(__file__)
    hits = 0
    for rel in files(args.root):
        path = os.path.join(args.root, rel)
        if os.path.realpath(path) == me or not os.path.isfile(path):
            continue
        with open(path, 'rb') as fh:
            data = fh.read()
        if b'\0' in data[:8192]:
            continue
        for n, line in enumerate(data.decode('utf-8', 'replace').splitlines(), 1):
            for p in PATTERNS:
                for m in p.finditer(line):
                    print(f'{rel}:{n}: {m.group(0)}')
                    hits += 1
    if hits:
        print(f'{hits} absolute local path(s) found', file=sys.stderr)
        sys.exit(1)
    print('clean')


if __name__ == '__main__':
    main()
