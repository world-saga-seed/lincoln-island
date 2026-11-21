# *Vingt mille lieues sous les mers*, the French (Hetzel, 1870): where it came from

*Written into `existing/` by the executor at the author's request, 2026-11-20 (R1120-05). After this commit it is read-only, like the rest of `existing/`.*

- **Edition:** J. Hetzel, Paris, 1870, illustrated by Alphonse de Neuville and Édouard Riou. These details come from Wikisource's scan index, `Livre:Verne - Vingt mille lieues sous les mers.djvu` ("Annee=1870"). The author had approved the folder name as 1871; the scan's date was used instead, and the author confirmed 1870.
- **Scan:** the Internet Archive, `vingtmillelieue00vern`, the scan the transcription was made from.
- **Transcription:** fr.wikisource, `Vingt mille lieues sous les mers`, marked "Textes validés". It has 47 chapter pages: Partie 1 has chapters 1 to 24, Partie 2 has chapters 1 to 23. Files `01` to `24` are Partie 1, and `25` to `47` are Partie 2.
- **Fetched:** 2026-11-20, by the MediaWiki API (`action=parse`, `prop=text|revid`), one call per chapter. Wikisource rate-limited the fetch (HTTP 429), so it was re-run slowly from the start, and only the complete run is kept. Each page's revision id is in `raw/manifest.json`, so every page can be fetched again exactly at `https://fr.wikisource.org/w/index.php?oldid=REVID`.
- **Files:** `raw/01.html` to `raw/47.html` are the rendered chapter HTML exactly as the API returned it. `SHA256SUMS` holds the sha256 of each; run `sha256sum -c ../SHA256SUMS` from inside `raw/`, the same layout as `hetzel-1875/`.
- **Size:** about 142,400 words in paragraphs.

## Scope (R1120-25)

Only what *L'Île mystérieuse* itself draws on from this book is carded, and each of those cards cites the earlier book. Anything more is carded only if the run needs it, with the reason logged.

## Licence, for the clearance (phase 12b)

- Verne's text and the plates are in the public domain.
- Wikisource's own additions (the `ws-noexport` blocks, the headers and the page numbers) are CC BY-SA. They are stripped, not shipped (R1120-23).

## Not yet done

- A spot check of sample paragraphs against the scan.
