# Contributing an improvement

The kit is a cooperative tool: it gets better from what writers find while using it. A critic that catches more, a voice rule, a step that costs fewer tokens, a script, a failure mode and its fix: all welcome, big or small.

## The easy way: tell us

Open an issue that describes the improvement in general terms: what went wrong or could be better, what you changed, and what it did. No names, scenes or lines from your book are needed; "the facts critic kept flagging my narrator's dialect as errors, so I added a line to its brief" is enough. It will be ported into the kit for you.

## Sending the change yourself

Your book is never the place to send a change from: it is full of your work, and the kit carries none of it. So a change goes through a second copy, and you look at it there before anyone else does. Claude runs each step below for you; you say what you want and read what it shows you.

1. **Once: make your fork.** Say to Claude: "Fork the World Saga Seed kit on GitHub, clone the fork into a folder beside my book, and add the kit as its upstream." Your book stays as it is; the fork is a clean copy of the kit. During the alpha both the kit and your fork are private.
2. **Port the change on a branch.** Ask Claude to bring the fork up to date, start a branch, and carry the improvement from your book into the fork's copy of the same workflow, prompt or script, written for any book. Where it needs an example, use the toy novel in `example/`.
3. **Open a pull request to your own fork,** from the branch to your fork's main branch. This is your review: Claude runs the leak check on it and reads the whole change for anything of your book, and you look it over. The leak check, from the fork's folder:

   ```bash
   git diff upstream/master | python3 tools/check_leak.py --book ../my-book
   ```

   It lists any line of the change holding a name from your cards or character sheets, a run of eight or more words that also appears in your prose, notes or manuscripts, or an email address. It catches only exact matches, so Claude's read and yours are the real check: a plot point retold, a coined word, a character's habit. When you are satisfied, say so: that is your approval. (GitHub does not let you approve your own pull request, so there is no Approve button to look for.) Claude then closes this review request without merging it, so your fork's main stays a clean copy of the kit, and sends the same branch on.
4. **Submit it to the kit:** a pull request from the same branch to the kit, saying what it fixes and what it did for you. If you measured it (a critic's catch on planted faults before and after, or the token log's rows), include the numbers; numbers from your book are fine without quoting it. If not, say so, and it can be measured on the example.

## What a change keeps

- The kit's rules ([plan/workflows/README.md](plan/workflows/README.md)): the marks, the ledger first, the agent limits, every finding quoting the text, no git commands in an agent.
- No personal information: no email addresses or account names, and no names of real people beyond the kit's credit line.
- No text from published books, yours or anyone's, beyond a short phrase.

**The license.** Every contribution is given under the same licenses as the rest of the kit: [CC BY 4.0](LICENSE) for the docs, [MIT](tools/LICENSE) for the scripts. A pull request to the kit opens with a short form whose first box says so; ticking it is your consent, and a change is not taken without it. Give only what you wrote or have the right to give. An idea told in an issue is ported under the same licenses.
