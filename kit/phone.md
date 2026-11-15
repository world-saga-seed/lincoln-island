# Working from a phone

Set up once on the computer; then the writing loop can run from a phone. Everything still runs on the computer, in the book's folder: the files, the scripts, the agents. The phone is a window onto that session through Claude Code's Remote Control, so you can dictate a key frame on a walk, rule on a critic's finding from the couch, or comment while you read on an ereader.

**Once, at the computer:** do the setup in the [README's How to start](../README.md#how-to-start). Then, in the book's folder, start a Remote Control session by typing `claude remote-control --name "My book"` (the one command you type yourself), and open it from the Claude app on your phone. If it drops, `claude remote-control --continue` in the same folder reattaches to it, for about four hours after it was last used; after that, start a new one. These commands come from Claude Code's own help (`claude remote-control --help`), which is the place to check if they have changed.

**What works well from the phone:** the interview and the key-frame walk (answer by voice or by typing); dictating a scene; ruling on questions, which Claude puts a few at a time, each with a recommendation; starting a render and coming back when it is done; commenting while you read ([the ereader read](../plan/workflows/ereader.md#the-read-comments-from-the-phone)).

## The gotchas

- **The computer must stay on, awake and online,** with the session open. If it sleeps, the phone loses the session; set its power settings so it does not.
- **Don't read diffs or long critic reports on the phone.** Ask Claude for the verdict in a few lines, then the findings one at a time with its recommendation. The kit's `CLAUDE.md` already tells Claude to answer a phone in a few lines.
- **Permission prompts come to the phone.** Read what you approve, as you would at the desk; an agent run or a push is worth a second look.
- **The ereader book has to reach the reader.** Copy it over at the computer, or put the build folder in a cloud folder the reader syncs.
- **Autocorrect and voice typing swap words.** Claude reads each message by the scene it points at, and asks only when a misread word could change a ruling.
- **Long runs cost tokens whether you watch or not.** Each run is logged in the token log (`plan/templates/tokens.md` is its form); check it at the computer now and then.

## An always-on host

For daily work, a small machine that never sleeps is better than a laptop: a Raspberry Pi 5 (8 GB) or a mini PC running Linux, with the book on an SSD rather than an SD card, on a wired network. Claude Code runs on it as on any Linux machine (check Claude Code's install page for the current list of supported systems before buying), and you reach it only through the phone. Ask Claude to push the book to a private remote each day, so a dead card or drive loses nothing.
