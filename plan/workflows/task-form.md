# The task form

*Basic.*

Every task file opens with the form; the steps below it are the task's own flow, adjusted to what the discussion settled. The blank form is [`plan/templates/task.md`](../templates/task.md).

- The steps are plan, study, revise the plan, execute, check, report.
- The Log is written as the work goes: at every step boundary, every agent launch and result, every decision. A session can end without warning; the next one resumes from the log alone.
- A step the discussion made moot is dropped, with one line saying why.
- Name: `plan/tasks/task-YYYYMMDD-NN-slug.md`, by the day it was opened. Its working papers go in a folder of the same name.
- **A wave** is a task file that only orders other tasks: each task's name and one line of why it sits there, with the retrospective last. It waits for the writer's "next wave".
- Get hashes with `git rev-parse HEAD`. Never write one from memory.
