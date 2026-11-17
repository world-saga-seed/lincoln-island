# The critics

*Basic.*

One dimension each. Each is a fresh agent, a full prompt, the strongest model available, and one output file. The prompt templates are in [prompts/](prompts/).

**The Basic pair** is the facts critic and the voice-and-mechanism critic (run last). The others are Refinements, each added when its trigger shows up.

## The table

| Critic | Tier | The question | Gets | Never gets | Runs |
|---|---|---|---|---|---|
| **Facts** ([prompt](prompts/facts.md)) | Basic | "Where does this contradict the notes?" | the chapter; its notes for drafting; the settled lines of its outline and arc outline; the cards and sheets of everyone and everything in it; the rulings; the drafts before it | the outline's proposals; later outlines | each chapter |
| **Coverage and slip** ([prompt](prompts/coverage-slip.md)) | Refinement: beats go missing, or someone knows too early | "Which beats are missing, out of order or added? Where does someone use what they do not have yet, or the narrator know what they could not?" | the chapter; its outline's numbered beats; the drafts before it; the voice sheet; the rulings | the notes for drafting; later outlines | each chapter |
| **Setup and belief** ([prompt](prompts/setup-belief.md)) | Refinement: help arrives on cue, or the chapter has a big event | "Where does help arrive on cue with no cause? Given only what each person has lived and believes, where would they not do or say this?" | the chapter; the drafts before it; the setting's topic files; the sheets of the people in it | this chapter's outline and notes; anything later | each chapter (or only those with a big event) |
| **Procedures** ([prompt](prompts/procedures.md)) | Refinement: the book has trades, rites, fights or paperwork carded step by step, and the writer's read finds steps missing | "Is every process on the page done as its card sets it? What step is skipped, out of order, or done by the wrong hand?" | the chapter; the cards of each process on the page (by the book's own index of them); the drafts before it, or the digest; the rulings | the outline's proposals; later outlines | each chapter |
| **Continuity** ([prompt](prompts/continuity.md)) | Refinement: chapters are drafted side by side | "Where do these chapters disagree with the chapters before them, and with each other?" | the batch's chapters; the drafts before | the outlines; the notes | each batch |
| **Out-of-world phrases** ([prompt](prompts/idioms.md)) | Refinement: out-of-world phrases survive the banned list | "Which phrases only make sense to someone outside the narrator's world?" | the batch's narration only | everything else | each batch |
| **Habits** ([prompt](prompts/habits.md)) | Refinement: one character's tic shows up on another | "Where does someone do a habit that is not theirs, break one of theirs, or repeat one until it is filler?" | the batch; the Habits sections of every sheet and card for who appears; the voice sheet for the narrator; from the second batch of a volume, `refrains.py` | the outlines; the notes for drafting | each batch |
| **Attribution** ([prompt](prompts/attribution.md)) | Refinement: the book has two or more viewpoint heads | "Whose head is each of these unlabeled paragraphs in, and how could you tell?" | the batch's paragraphs, shuffled, with labels and breaks removed (`tools/attribution.py`) | everything else, the key above all | each batch with more than one head |
| **How the narrator knows** ([finder](prompts/inference-finder.md), [judge](prompts/inference-judge.md)) | Refinement: a first-person or close narrator, and readers who ask "how does he know that?" | "Where does the narrator state a past, motive, feeling, purpose or cause he could not know when he says it?" | the chapter; earlier chapters by search; the chapter's notes and outline, the sheets, cards, clue register and ledger, for the plot check | the writer's reasons and the conversation | two chapters a run, after drafting: a cheap finder, then a stronger judge |
| **Voice and mechanism** ([prompt](prompts/voice-mechanism.md)) | Basic | "I think these chapters are poorly matched with the voice. Can you tell me where?" plus mechanism, model tells, hindsight, register and measures | the batch; the voice sheet; the banned list; the style samples; the setting's topic files only to recognize a true cause when it leaks; `tells.py` output | the outlines; the notes for drafting | each batch, **last** |

Two more run on outlines, before drafting: see [Outline critics](#outline-critics).

## The POV file, and the lists every critic reads

**Every critic reads the POV file** ([the template](../../templates/pov.md)): `story/voice/pov.md` for the book, `story/voice/pov-NNNNN.md` for a chapter told another way. It says whose head the narration is in, its distance, what each head may know, what is never told, and what the narrator cannot witness. Where it and the voice sheet differ, it wins. Without it, every critic judges every chapter against the main narrator's rules: in a test of five narrations of one chapter, the critics flagged close third and omniscient narration as faults in themselves, and an omniscient narrator's allowed visits into other heads as breaks, while the same critics on the first-person control raised no such findings.

**A narrator's wrong beliefs are guarded** ([the template](../../templates/knowledge.md)). The facts critic judges every line against the cards, so an unreliable narrator, or any head that believes something wrong, reads to it as a run of errors, and the reviser would correct each one. A knowledge guard per head, `story/voice/knowledge/<head>.md`, lists what the head knows, believes wrongly and does not know, each entry with the chapter it starts and ends; `tools/knowledge.py N` prints the entries in force at chapter N for the briefs, so a narrator whose beliefs change needs no file per chapter. The drafter voices the beliefs; facts, coverage-slip and setup-belief spare a line that matches a listed belief, flag a wrong line listed nowhere for the writer to rule (a slip, or a new belief), and break a line that states what the head does not know or contradicts what it knows; the reviser never corrects a listed belief. In a test on a first-person chapter with three planted beliefs, two unlisted errors and one thing the narrator could not know, the critics without a guard flagged all three beliefs as errors, one as a break; with the guard they spared all three, caught the other three, and with the head's knowledge on paper also caught a reversal of the narrator's eyesight the unguarded runs had missed, at no added cost.

**Two lists reach the critics as well as the reviser:**
- **The clue register** (`plan/reread-hooks.md`), for every critic that proposes cutting or varying a detail. In the same test a voice critic asked to vary a repeated phrase that was the clue matching two characters; only the reviser's never-cut rule stood in its way.
- **The held facts:** the reader key's hidden and forbidden entries, and the outline's author-side lines, for the facts, coverage and voice critics. A line that states a held fact, or lets a reader state it, is a break whoever narrates. Without the list, a leak is caught only where a chapter's notes happen to say what is kept.

**By narration:**
- **First person, another narrator** (a letter, a fragment, a witness): covered by the voice critic's narrators question, given that narrator's voice sheet.
- **Close third:** the POV file's head and distance; coverage and slip judge knowledge per head.
- **Several heads:** a voice sheet and samples per head, coverage and slip per head, and the attribution test each batch.
- **Omniscient:** the POV file says who may be entered, how wide the narrator ranges and what it never tells; the voice critic asks whether each move is marked, not whether it happens. A drafter left to choose stays close to the main character, so a book that wants real omniscience must say so.
- **A narrator who cannot witness a beat:** the beat is not missing, but a clue it carried must reach the page another way, or be listed as lost.

## Why each excludes what it excludes

- **Continuity, voice and setup never read the outline.** They judge the page as a reader meets it. A critic who has read the outline sees what the scene meant to do, and forgives what it fails to do.
- **Facts reads only settled lines.** A draft that departs from a proposal is not wrong; a draft that departs from a settled line is.
- **Coverage never reads the notes for drafting.** Its question is only the beats.
- **Out-of-world gets only the narration.** It must read cold, with no setting notes to explain away a phrase.
- **Nobody reads later outlines.** What has not happened yet cannot be a fault, and knowing the payoff makes a critic flag the plant.

## Order

1. **Per chapter, as each draft lands:** facts; coverage and slip; setup and belief (with `firstuse.py`); procedures. Resolve these before the batch critics, so the batch critics read a chapter whose facts are right.
2. **Per batch,** after the [volume checks](mechanical.md#volume-checks-before-the-batch-critics): continuity across the two or three chapters; out-of-world phrases; habits.
3. **Voice and mechanism last,** because it reads the joins the others left and the fixes they made.

Run independent critics in parallel, two at a time.

## The voice and mechanism critic

The broadest critic, with six numbered questions (voice, mechanism, model tells, hindsight, register, measures and narrators): see [its prompt](prompts/voice-mechanism.md).

## The report form

Every critic writes the same form ([plan/templates/critic-report.md](../../templates/critic-report.md)), so one checker reads them all. Written to the batch's scratch folder, one file per critic: `critic-<dimension>-<chapters>.md`.

## The idiom bank grows from the out-of-world critic

Each confirmed out-of-world phrase becomes a line in the banned list, so next time the grep catches it for free. Its shifted phrasing ("what the narrator could say instead, built from their world") goes into the voice sheet's idiom list, once the writer has approved it. The banned list finds only what is already on it; the critic finds what should be. Run both.

## Cheap finders for detail checks

For a detail check (scale, counts, names, repeats), run a cheap model as a finder first: it lists every candidate line and never judges, and a script or the stronger critic judges the list. It almost always pays: one real catch tells the stronger agent where to look, and the fix is a grep away. Never trust the finder's gloss over its quote; a cheap reader can read a line backwards. Second case: [the inference finder](prompts/inference-finder.md) and [its judge](prompts/inference-judge.md). In a planted test (eight reads with no evidence put into three chapters: two pasts, two feelings, a motive, a purpose, a cause, and a grounded line stripped of its grounds) the finder found all eight and the judge, once told that grounds must come before the claim, called all eight. On the first full run over about forty chapters, it found seven firm breaks in about 1,550 candidates, most in the newest drafts, and caught two lines cold readers had stumbled on; it does not catch a cause simply missing from the page. About 75k tokens a finder run and 70k a judge run, two chapters each. First case: [the scale finder](prompts/scale-finder.md), which in a planted test found all fifteen warped sizes, the five shown only by action among them, and three times the lines the pattern script finds, for about 18k tokens a chapter.

## Outline critics

*Refinement. Add these when an arc of several chapters is outlined.*

Two run on outlines, before drafting, where a fault is cheapest to fix ([prompt](prompts/outline-critic.md)):

- **The outline critic.** The question: "Where does this outline contradict the notes, or give a beat no cause?" It gets the chapter outlines in the range, their notes, the arc outline, the cards and sheets they link, and the rulings. It never gets drafted prose of these chapters, later outlines, or the conversation.
- **The setup check** on outline beats: the setup question of the [setup and belief prompt](prompts/setup-belief.md), asked of the beats instead of the page.

## Tracing findings to their source

Every finding's `against:` line names the file it rests on, by its path from the book's top (`world/beast/selkie.md, Size`), or says "the outline" or "the notes". A finding with no file can't be traced.

After the critics, run `tools/gaps.py` on their reports with the chapter's bundle manifest. It sorts each break and weak finding:
- **a drafter slip:** the fact was in the bundle, the chapter, or the rules;
- **a source gap:** the card was not included, its field was not given, or the fact sits only on an earlier page the drafter did not read.

It ends with the list of fixes to the source: the includes and fields to add. Make those, so the next chapter that uses the card gets it. Save the trace next to the manifest. A finding is a lead: check it against the page before changing anything.

When a card changes later, `tools/uses.py` lists the drafted chapters whose bundle gave the changed field, and the lines of their pages that name the card. Those are the places to recheck.

## Running a test of the critics

When you test the chain itself (a new narration, a new critic), give the test's folder and files neutral names. In the narration test two critics guessed what was being tested from the folder's name and adjusted their findings.

## Adding a critic

When a fault keeps reaching the writer's read that no critic catches, add a critic for it:

1. Write its one question.
2. Decide what it gets and never gets.
3. Write its prompt from the closest template.
4. Calibrate it ([principles](principles.md#5-calibrated-before-it-is-trusted)).
5. Add its row here.

A **method critic** is a common addition for books with fights or crafts: "Where does this fight, hunt or repair run by stock convention instead of the setting's own rules? Who is doing it, and does it follow their culture's way?" Give it the setting's card on how that work is done and the cards of whatever is in the scene. Where the cards set a process step by step, the [procedures critic](prompts/procedures.md) is the narrower form: it walks each step against the page.

**Reading lists and lookups.** From the second volume, each critic gets its share of the chapter's reading list (`tools/reading.py N --step <critic>`) and the volume digest in place of the earlier chapters ([the reading list](drafter.md#the-reading-list)). A fact the list lacks is a lookup for [the librarian](prompts/librarian.md).
