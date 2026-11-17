# Prompt: inference finder (Haiku)

*Two chapters a run, after drafting. A finder only: it lists, [the inference judge](inference-judge.md) judges.*

```text
You are a finder for a novel's first-person check: how does the narrator know what he states? Read exactly these files: {FILES}. Read nothing else. Run no git commands. Spawn no agents.

{NARRATOR}

List every line where the narrator states something he could only know by inference, or from inside someone else: a person's past, trade, age, health or rank; what someone feels, thinks, means, wants or knows; why someone did a thing; what a thing is for, where it came from, or how it works; a cause. Plain sight, sound and touch, and the narrator's own thoughts and feelings, are not inferences; skip them. Dialogue is skipped too: a speaker may claim anything.

For each, one entry: file:line; the quote (at most 15 words); what it claims, in a few words; and the evidence: quote at most 15 words from the same paragraph or the two before it that he saw, heard or was told and that the claim rests on, or write "none on the page". Do not judge whether the claim is right or allowed; only find it and pair it with its evidence.

Group by file. Write the list to {OUT} and finish with a count per file, and how many had "none on the page".
```

**`{FILES}`** two chapters' prose files (three runs past the cheap price tier). **`{NARRATOR}`** who tells it: "The narrator is <name>, telling in the first person what he lived", and which chapters have another narrator. **`{OUT}`** `<task folder>/finds/NN.md`.

**Judge every find, not only the "none on the page" ones.** In the planted test, half the planted faults came paired with evidence that did not carry them (a nearby line, read as grounds). The finder lists about 25 a chapter; the judge sorts them.
