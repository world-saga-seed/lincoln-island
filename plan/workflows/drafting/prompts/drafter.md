# Prompt: drafter (v1)

*Fill every `{PLACEHOLDER}`. One chapter per agent. A fresh agent, never a fork.*

```text
You are drafting one chapter of a novel in progress, in the folder {REPO}. Every file is
read-only except your one output file. Run no git commands of any kind (not even status or
stash): another session may be editing this folder. Do not launch agents.

Read, in this order:
1. story/voice/voice.md (the voice sheet) and story/voice/banned.txt (the words the
   narration never uses);
2. plan/workflows/drafting/rulings.md (the rulings of the page; every line binds you);
3. the style samples in story/voice/samples/: the voice as the writer set
   it. Match it; do not copy it;
4. the chapter's outline, story/outline/{N}-*.md (the numbered beats: what the page shows),
   and its notes for drafting, story/notes/{N}-*.md;
5. the arc outline {ARC}, for context only;
6. the draft before it, {PREV}, read closely for the join; and skim {SKIM} for the people,
   places and objects already set;
7. the cards for every person, place and thing in the chapter, through the indexes in
   world/*/README.md, and the sheets in story/notes/characters/. Read the Habits section of
   everyone who appears, and give each person only their own.
Read nothing else. Do not read any outline after this chapter.

Follow a link in the outline only as far as you need to get a fact right. The notes are the
facts; the page shows only what the narrator sees and what the scene needs. Lore stays in
the notes.

Write the chapter as prose into story/prose/{N}-{SLUG}.md, replacing any earlier draft,
with the title line "# {TITLE} (draft {D})". Every settled beat, in order; the proposal
beats too, unless one contradicts a settled beat; nothing the outline marks author-side or
reference. The chapter falls after {FRAME}. Length: {WORDS}, a target, not a cap.

Keep to the texture in the rulings: measure with
  python3 tools/tells.py story/prose/{N}-{SLUG}.md --banned story/voice/banned.txt
and fix every banned-word hit that is narration.

No notes, marks or comments inside the prose file. Where a beat cannot be written without
inventing a fact the notes lack, write around it and list it.

{EXTRA}

Finish with a short report:
- the word count and the tells.py line;
- the beats covered; any beat skipped or changed, and why;
- Inventions: the small things you made up (names, objects, staging, sayings), one line
  each: the fact, its line, the cards it touches. Do not check them yourself; a separate
  run does;
- the facts you had to leave open;
- the banned-word hits you fixed.
```

**`{EXTRA}`** is where the supervisor puts what this chapter's outline gets wrong against the rulings, and what the neighboring chapters drafted at the same time will have done ("00300 ends with the narrator at the gate at midday; open there"). For a piece in another narrator's voice, `{EXTRA}` also says which rules of the voice sheet belong to the main narrator only and do not apply, and gives the piece's own voice line.
