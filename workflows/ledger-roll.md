# Ledger roll: split a ledger file that ran past its day

*Refinement. Add this when a ledger file runs past its day.*

The ledger keeps one file per date, and a row's ID carries its file's date (`R0302-01` is in `2027-03-02.md`). A long session that crosses midnight, or a helper that keeps appending to the last file, makes one file run on across days. Split it.

**Prevent it:** run `date` before the first ruling of every session and after any session crosses midnight; write to that day's file, creating it with the header if it is missing.

## The split

1. **Open a task** naming the file and the start hash.
2. **Split** by the Date column: rows go, in order, to `plan/settled/ledger/<Date>.md`, each new file headed like the others. **IDs never change**, even when a row lands in a file whose date does not match its prefix; the README notes the range.
3. **Repoint** every link to the split file: each goes to the file holding the ID that link cites (the ID nearest the link on the same line). A link with no ID on its line stays, and is logged.
4. **Check:** `python3 tools/links.py` at 0; every ID in exactly one file; row count before equals after; each file's rows all carry its date.
5. **Review:** a second agent samples twenty repointed links and confirms the cited ID is in the target file.
6. **Note** in `plan/settled/ledger/README.md` where the run-on series went, and that new rows follow the day rule.
