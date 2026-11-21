#!/bin/bash
# The Opus controls: one try each, a fresh context, no tools, no project files.
S="$1"; OUT="$2"
cd "$S" || exit 1
for n in 01900 01950 02000; do
  date -u +%FT%TZ > "$OUT/opus-$n.started"
  claude -p --model claude-opus-5-5 --tools "" --system-prompt "You are a helpful assistant." \
    --strict-mcp-config --setting-sources "" --no-session-persistence --output-format json \
    < "$S/prompt-$n.md" > "$OUT/opus-$n.json" 2> "$OUT/opus-$n.stderr"
  date -u +%FT%TZ > "$OUT/opus-$n.finished"
done
