# Task: phase 1, the sources (intake and working texts)

- **Objective:** know the sources before outlining, and make the paragraph-numbered texts every later row cites.
- **Context:** `BRIEF.md` phase 1; R1120-04 to -08, R1120-23, R1120-28 to -31.
- **Related study:** none.
- **Region:** writes `texts/` (new) and this task. Reads `existing/hetzel-1875/`, `existing/vingt-mille-hetzel-1870/` and `existing/white-1876/`. `existing/kingston-1875/` is closed (R1120-07) and not read.
- **Wave:** none.
- **Start hash:** 3faf270, 2026-11-20 21:18 -0800.
- **End hash:** (on close)
- **Status:** Done, awaiting commit.

## Steps

1. **Plan.** Verify the checksums. Derive each text with a script, and vet it with a second script written another way (regex, not the deriver's parser), word for word. Spot-check the French against the scan. Produce the intake (kit/interview/intake.md, adapted: the sources are a published novel and its translation, not a writer's drafts).
2. **Execute.** Done by hand in the main session. No agents.
3. **Check.** See Acceptance.

## The file table

| File | Words | Kind | What it is |
|---|---|---|---|
| `existing/hetzel-1875/raw/01.html` to `62.html` | 205,324 (derived text) | manuscript: the ground truth | *L'Île mystérieuse*, Hetzel 1875, fr.wikisource "Textes validés", 62 chapters |
| `existing/hetzel-1875/raw/manifest.json`, `SHA256SUMS`, `SOURCE.md` | | other | revids, checksums, provenance |
| `existing/vingt-mille-hetzel-1870/raw/01.html` to `47.html` | 143,200 | other: the earlier book, carded only where *L'Île* draws on it (R1120-25) | *Vingt mille lieues sous les mers*, Hetzel 1870, 47 chapters |
| `existing/vingt-mille-hetzel-1870/raw/manifest.json`, `SHA256SUMS`, `SOURCE.md` | | other | revids, checksums, provenance |
| `existing/white-1876/8misl10h.htm` (and the `.zip` it came in) | 162,755 (body) | manuscript: the one English voice (R1120-06) | White's 1876 translation, 62 chapters |
| `existing/white-1876/pg8993.rdf`, `SOURCE.md` | | other | Gutenberg's record, provenance |
| `existing/kingston-1875/` | not read | other: closed until 12b (R1120-07) | Kingston's 1875 translation |
| `existing/README.md` | | other | the kit's placeholder line |

## The checksums

All of them match: `sha256sum -c ../SHA256SUMS` run inside each French `raw/` folder, and White's three files against the sha256 values in its SOURCE.md.

## The manuscripts

**The French.** Third person, past tense (passé simple). The narrator is outside the story and sometimes addresses the reader in footnotes "(Avis de l'Éditeur.)". There are three parts: I.1 to I.22 (*Les Naufragés de l'air*), II.1 to II.20 (*L'Abandonné*), III.1 to III.20 (*Le Secret de l'île*). Every chapter opens with a summary (¶0). The cast, places and things are left to phase 4's cards; listing them here would only be a summary of the book.

**White.** The same person and tense, in English. Its 62 chapters are numbered straight through; the parts begin at XXIII and XLIII. Every chapter has its capitals summary (¶0). It has 4,345 numbered paragraphs against the French's 5,242 (5,304 lines less the 62 summaries). That is a first sign of where it merges or cuts, which phase 3's alignment will show.

## Facts to carry

**The French draws on two earlier books, not one.** R1120-25 sets the scope for *Vingt mille lieues* only. II.17 n1 names *Les Enfants du capitaine Grant* as the source of Ayrton's story:

- quote: sont tirés d’un ouvrage que quelques-uns de nos lecteurs ont sans doute lu et qui est intitulé Les Enfants du capitaine Grant

Both notes warn that the dates do not agree with the earlier books:

- quote: une certaine discordance dans les dates
- quote: Ici se place donc la même observation qui a été faite à propos des aventures d’Ayrton, sur la discordance de quelques dates.

That is Verne's own word that the calendars disagree. The cards should cite the French date and record the earlier book's date beside it, never reconcile them. *(Proposal.)*

**Three of Wikisource's corrections change a fact** (`texts/README.md`, "What was changed"). In I.12, a latitude "trop haute" where the print reads "basse"; in II.20 n1, "83" kilometres an hour where the print has "106"; in III.10, "décembre" where the print has "novembre". The scan check (R1120-31) confirms that the print reads otherwise in all three (`texts/README.md`, "The scan check").

- quote: Environ 83 kilomètres à l’heure.
- quote: pendant cette journée du 7 décembre

## Style samples

None are picked here. Phase 5 chooses the voice chapter: White's chapter least cut or changed against the French.

## The shape

The book is fixed: it is Verne's, whole. The only loose thing is where the one inserted chapter goes, and that is set in phase 6, which this run does not anticipate.

## Questions for the author

1. ***Les Enfants du capitaine Grant*:** fetch it and card what *L'Île* draws on from it, under the same rule as R1120-25? Rec: yes. Fetch the Hetzel text from fr.wikisource the same way, into `existing/`, and card only what *L'Île* uses (Ayrton, the *Duncan*, Tabor, Glenarvan's party), each card citing the earlier book. The other way: card from *L'Île* alone, and treat the II.17 account as all the run needs.

## Acceptance

1. Every file in `existing/` (outside the closed folder) is in the table. **Yes.**
2. Every quote resolves: `python3 tools/quotes.py plan/archive/task-20261120-01-sources/intake.md --in texts/fr-1875/*.md`. **Yes.**
3. Nothing in `existing/` changed: `git status existing/` is clean. **Yes.**
4. The three vets print 0 differences. **Yes.**
5. `tools/links.py` and `tools/cards.py check` print 0. **Yes.**

## Log

- 2026-11-20 Opened.
- 2026-11-20 The first vet found real deriver faults: Férat's plate captions and part-end lines were dropped, and a block inside a footnote ran two words together ("égard.(Avis"). It also found faults in the vet itself, which put spaces at inline tags and put loose lines back in reverse order. All were fixed and both scripts re-run, until 0 differences. *Vingt mille* then showed its chapter titles sit in headings, which the deriver had dropped. Headings are now kept as `hd` lines in all three texts.
- 2026-11-20 The scan check: Gallica refused (HTTP 403, Cloudflare). The author ruled first to skip the check (R1120-30), then to read the same scan from Commons (R1120-31). Ten pages were read; the results are in `texts/README.md`. The transcription is faithful: one hyphen lost (I.14 ¶25), and Wikisource's three corrections that change a fact are confirmed against the print. Page 407 was read in place of 612, so that II.20's note could be seen.

## Resolution

The working texts are in `texts/`, all three vetted clean. One question is put to the author (above). Next: the budget sample (R1120-27).
