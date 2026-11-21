# French kept in the English (R1120-39)

The sweep of the outlines, notes and timeline for French outside the cited quotes. The run's rule (R1120-29) is English throughout, with French only in quotes. These are the exceptions it keeps.

## Terms the book keeps in French
- **Cheminées**, also written Les Cheminées: the castaways' name for their first shelter. In running English it is "the Chimneys".
- **pan coupé**: the sheer cut face of the granite wall.
- **tétras**: the grouse the castaways fish for in I.6.
- **échidné**: the animal named in the summary of I.15.
- **déodars**, **poivrière**, **précintes** and **ptéropode**: the text's own words for a tree, a turret, a ship's wales and a sea creature, kept where a line names them.

## Proper names
Places, people, ships and books keep the text's form: Granite-house, Port-Ballon, la pointe de l’Épave (also Flotson-point), le golfe du Requin, cap Mandibule, Creek-Rouge, Tippo-Saïb, and the place names given in I.11. Where a line uses an English form already (the Chimneys, Lake Grant, Mount Franklin, Wreck Point), it is left as it stands.

## French the line is about
Where a line sets two of the text's wordings side by side, or the argument turns on the exact French ("la veille", "le 30 novembre", the ladder "retirée et relevée jusqu’au seuil" against "replacer l’échelle"), the French stays, in backticks or quotation marks. The sorters marked 32 such spans "wording".

## How it was done
- `find_french.py` found 928 distinct spans in 1,102 places (`french-candidates.tsv`).
- Two Haiku sorters binned them (`french-sorted-s1.tsv`, `french-sorted-s2.tsv`): 858 translate, 25 name, 9 term, 32 wording and 4 skip, which is all 928.
- `apply_french.py` put the English in at 1,000 places; 5 missed and were fixed by hand.
- Two Haiku reviewers read every changed line, before and after (`french-reviewed-r1.tsv`, `french-reviewed-r2.tsv`). The main session applied 27 fixes. It held back 149 (`french-rejected.tsv`), nearly all of them the first reviewer putting the French back; it then fixed the half-replaced lines in notes 01700, 02800, 02900 and 03100 by hand.
- A last pass, by French spacing before ! ? ; :, put 20 short exclamations into English. Very short French with no accent, no function word and no spaced punctuation can still hide; a reader who finds one puts it into English.
