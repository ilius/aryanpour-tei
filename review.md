# Review of `aryanpour.parts`

Scope: all 61 files in `aryanpour.parts/` (181,144 entries).

## Code review: `split_tei.py` / `combine_tei.py`

- Entry regexes use `<entry>...</entry>`. They would silently skip `<entry attr="...">`; prefer `<entry(?:\s[^>]*)?>...</entry>`.
- `split_tei.py` attaches the footer to the file containing the last *entry*, not the numerically last filename. If the last entry ever sorts into another file, the closing `</body></text></TEI>` lands mid-set. Attach the footer to `all_filenames()[-1]` instead.
- `dedent_entry()` normalizes entry bodies but not the footer or trailing whitespace. Normalize the footer in the script so manual fixes are not needed.
- `entry_file()` silently routes unmapped Persian characters (hamza, diacritics, Arabic variants at word start) to the `01-puncs-digits.xml` placeholder. Add an assertion or explicit fallback so entries cannot disappear silently.
- `combine_tei.py` re-indents entries and depends on every part ending with a newline; add a validation step.
- There is no XML validation or test target. A small check using `xmllint` or `ElementTree` would catch malformed parts before publishing.

## Recommended order of work

4. Add XML validation to the split/combine workflow.
