# Prompt: build the key (v1)

*One agent that may read all the notes. Its output is the spec; the writer reads it before it is used. It is never given to a reader.*

```text
You are building the answer key for a test of a novel, in the folder {REPO}. Every file is
read-only except your output, {OUTPUT}. Run no git commands. Do not launch agents.

Read README.md, the voice sheet story/voice/voice.md, the clue register
plan/reread-hooks.md, the arc outlines {ARCS}, and the cards and topic files they link.

List every question a reader of the prose could ask about how the world works or what it
is: every device, power, process, institution and being the story relies on, and the big
ones (what is really going on, who the narrator is, what the place is). For each entry:
- ID and the question, plainly;
- kind: plain (the reader should work it out, though the page never names it), hidden
  (the reader must not come back sure of the truth), unknown (the book never resolves it),
  or forbidden (nothing on the page should raise it, or not before a stated chapter);
- text returns: what the prose alone should let a reader conclude, and what it must not;
- true: the answer from the notes, quoted, with file and heading;
- planted in: the chapters where the page first touches it, and where it turns, if the
  outlines say.

Group the entries by subject, with a short index at the top. Mark every entry
"(Proposal.)": the writer settles the key. Quote exactly; verify every quote with grep -F.
```
