# 03 Set up plan/

*Basic.*

**When:** after the interview.

**Uses:** the kit's [templates/](../templates/README.md); [task-form](../workflows/task-form.md); the scaffolding in [method/tasks-and-waves.md](../method/tasks-and-waves.md).

**What happens:** Claude makes the layout and fills the plan files:

```
your-book/
  CLAUDE.md  README.md            the instructions, and the index of every folder
  existing/                       read-only
  world/                          cards: people/, places/, things/, and topic files
  story/  outline/ notes/ notes/characters/ prose/ voice/ voice/samples/ calendar/
  plan/   README.md roadmap.md state.md reread-hooks.md
          settled/ settled/ledger/ tasks/ archive/ reader-tests/
          workflows/ (from the kit, with drafting/)   templates/ (from the kit)
  tools/                          from the kit
```

`CLAUDE.md` from the kit's template, with the horizon; `plan/README.md`, `roadmap.md` and `state.md` from the templates; the card folders' indexes in place (`tools/cards.py build`); git set up, one repository for the whole folder.

**Done when:** a fresh session given only "read CLAUDE.md and continue" can say where the work stands; `tools/links.py` and `tools/cards.py check` print 0.
