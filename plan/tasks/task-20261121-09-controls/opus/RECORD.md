# The Opus controls: the record

*Run by the main session, 2026-11-21, one try each, by `run.sh` (in this folder). Each reply is kept verbatim in `opus-NNNNN.json`, the CLI's whole result with its usage. `opus-NNNNN.md` is that JSON's `result` field, extracted unchanged.*

- **Model:** claude-opus-5-5, through the Claude Code CLI in print mode (`claude -p`).
- **Context:** fresh. An empty scratch folder, so no project files and no CLAUDE.md; `--tools ""` (no tools); `--setting-sources ""`; `--strict-mcp-config` (no MCP servers); `--no-session-persistence`.
- **System prompt:** "You are a helpful assistant."
- **User message:** the frozen prompt file, whole, on stdin (`../prompt-NNNNN.md`, checksums in `../SHA256SUMS`, commit 7b645a5).
- **Tries:** one each. No retry and no edit.

| Chapter | Started (UTC) | Finished (UTC) | Stop | Output tokens | Words | Cost (USD) |
|---|---|---|---|---|---|---|
| 01900 | 2026-11-21 15:31:27 | 15:32:37 | end_turn | 7,972 | 3,200 | 0.30 |
| 01950 | 15:32:37 | 15:34:05 | end_turn | 7,650 | 3,153 | 0.24 |
| 02000 | 15:34:05 | 15:35:03 | end_turn | 6,597 | 2,620 | 0.27 |
