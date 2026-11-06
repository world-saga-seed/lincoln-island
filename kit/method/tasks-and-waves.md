# Tasks and waves: the project scaffolding

This part is plain project management, nothing more. Everything else in the kit (the ledger, cards, horizons, the interview, key frames, the drafting and critic chain, the reader tests, the interest check) is the fiction method that sits on top of it.

## How it fits together

- **The plan makes tasks.** `plan/roadmap.md` says what is now, next and waiting; `plan/state.md` says what stage each chapter is at. From those, each piece of work becomes a task file in `plan/tasks/`.
- **Each task has its own flow:** plan, study, revise the plan, execute, check, report.
- **Every step is written to the task file as it happens.** A session can end without warning. The next one resumes from the task's log alone.
- **Tasks are grouped into waves.** A wave is a task file that only orders other tasks, with a retrospective last. A wave waits for the writer to say "next wave".
- **A retrospective closes each wave and each session** ([retrospective](../../plan/workflows/retrospective.md); the reasons are in [session-close.md](session-close.md)).

## The task form

Every task file opens with the form in [plan/templates/task.md](../../plan/templates/task.md); [task-form](../../plan/workflows/task-form.md) says how it is used.

A step the discussion made moot is dropped, with one line saying why ("Study: none; the count was taken in discussion").

Get hashes with `git rev-parse HEAD`; never write one from memory. The task's name is `task-YYYYMMDD-NN-slug.md`, by the day it was opened, and it keeps that name when it moves to `plan/archive/`.

## The rhythm

1. **Discuss** with the writer.
2. When the discussion settles some work, **draft the tasks and a wave** that orders them, retrospective last. Put the wave on the roadmap's Next.
3. **Wait for "next wave".** Do not start work in the middle of a discussion. A step that needs the writer (a commit, a ruling) is a stop line in the wave.
4. **Run the wave:** each task through its flow, logging as it goes.
5. **The retrospective** closes the wave: every task closed or carried by name into the next wave, and a line on why the order held or changed.
