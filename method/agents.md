# Agents: few, narrow, named, fresh

Claude Code can launch other agents to do pieces of work in parallel. Used well, they are fast. Used loosely, they blow through a usage limit and finish nothing.

## The limits

- **At most two agents at a time.** More agents with wide scope means each one reads half the repo, some launch their own agents, and the run fails.
- **No agent spawns its own.** Every prompt says so: "Do not launch agents or forks."
- **Every agent gets a named file list:** what it may read beyond the method files, and the one or few files it may write. Never "the whole arc" or "grep the repo".
- **No git commands in any agent.** Not even `status` or `stash`. A stash in a shared folder can remove other sessions' unsaved work. Where a prompt needs history (what changed since a date, a file's last commit date), the supervisor runs the git command and passes its output in as an input, such as `{CHANGES}` or `{DATES}`.
- **Small work is done directly.** Do not delegate what takes two minutes.

## Fresh, not forked

A fork inherits the whole conversation, including the writer's reasoning. A critic or a reader must not see that, or it judges what the writer meant instead of what the page says. So critics, readers and checkers are always fresh agents with a complete prompt.

## Strong models for judgment, small models for bulk

- **Critics and readers:** the strongest model available. Their job is to find what a reader would.
- **Mechanical bulk work** (moving text, splitting files, applying a rename): a small, cheap model does it, a script checks it (coverage, links), and a stronger agent reviews a sample.

## Inventions: logged by the writer of the text, checked by someone else

Invention is allowed; the agent that invents logs each new fact on an **Inventions** list and does not check it, because checking pulls in many cards and dilutes the main task. A small separate agent checks the list against the cards, asking whether each is consistent, not whether it is the best choice ([the invention check](../workflows/drafting/principles.md#the-invention-check)).

## Briefs

A good brief for an agent:

1. Says what the book is, in one line, and where the repo is.
2. Names the files to read, in order, and says to read nothing else.
3. Names the one file to write.
4. Asks one question, or gives one job.
5. Says what form the report takes, with every claim quoting the text.
6. Says: run no git commands; do not launch agents; inventing a finding is worse than missing one.
7. Asks for a short final message: counts, and the one finding that matters most.

**Scope each agent to a few chapters and a named card list.** An agent given a whole arc reads too much, runs out of room, and finishes nothing. If a job does not fit, split it into two agents with two file lists.

## Supervise

While agents run, Claude's job is to supervise: check what comes back (quotes, links, counts, a read of the rows), fix or drop what fails, resolve conflicts by story judgment (marked overturnable), and collect only the real questions for the writer.

## Log as you go

Write each agent launch, each result and each decision into the task's log as it happens. A session can end without warning when a usage limit is hit. The next session resumes from the log alone.
