# Kit patch: tools/overlap.py, the overlap check for the clearance

*Generic; no book content. Apply by copying `tools/overlap.py` into the kit's `tools/`, and adding the line below to the kit's `tools/README.md` and the step to `plan/workflows/publication.md`.*

## The file

`tools/overlap.py` (standard library only). It lists every run of N or more words (default 8) that a published text shares with one or more reference texts, after normalizing case, quotes, dashes and punctuation. Per file it reports the words, the share covered by shared runs, the number of runs and the longest; `--show K` prints the K longest runs; `--between START END` strips a distributor's header and footer from the references; `--tsv` writes the table.

## tools/README.md line

- `overlap.py`: runs of N+ words a text shares with reference texts (the clearance before release; also a measure of how much a render leans on an existing translation).

## publication.md step (after section 1)

**The overlap check.** Run `tools/overlap.py` with every published text against each reference translation: the public-domain ones (overlap is legal and measures dependence) and any modern one the writer owns (kept on their machine, never committed). Give, for scale, the overlap of two independent translations with each other. Review every long run against a modern translation; a passage that reproduces one is rewritten from the source and logged. If no modern translation is checked, the release says so. Due diligence, not a legal opinion.
