# Review of `aryanpour.parts`

Scope: all 61 files in `aryanpour.parts/` (181,160 entries).

## Remaining issues (not auto-fixed)

### 1. Ambiguous ZWNJ-before-hyphen/parenthesis conversions

The applied fix converted `\u200c-`, `\u200c–`, and `\u200c(` to a normal space. This produces forms such as:

- `(گیاه - شناسی)` from `(گیاه‌- شناسی)`
- `آب پرده (کالبد‌شناسی)` from `آب پرده‌(کالبد‌شناسی‌)`

These are much cleaner than the stray ZWNJ forms, but the exact desired wording (e.g. `گیاه‌شناسی` vs `گیاه - شناسی`) should be checked manually for the 328 hyphen and 351 parenthesis cases.

### 2. Remaining space-before-punctuation edge cases

- 9 remaining `space + )` cases have a non-alphanumeric predecessor and were intentionally skipped:
  - `aryanpour.parts/02-a.xml:7857` — `(بدین شکل: ' )`
  - `aryanpour.parts/02-a.xml:99405` — `(این شکل: * )`
  - `aryanpour.parts/04-c.xml:83726` — `(به اندازهٔ ) ...`
  - similar cases in `10-i.xml`, `14-m.xml`
- 23 remaining `space + !` cases are mostly intentional English examples or symbol labels:
  - `aryanpour.parts/03-b.xml:58021` — `... جهنم! !go to blazes`
  - `aryanpour.parts/06-e.xml:60801` — `(این نشان: !)`
  These should stay as-is.

### 3. Inline-markup whitespace

A few rare structural elements put text on a new line with indentation, which becomes whitespace in the text content:

- `<br/>` inside `<quote>`:
  - `aryanpour.parts/04-c.xml:87857`
  - `aryanpour.parts/04-c.xml:96392`
  - `aryanpour.parts/04-c.xml:110154`
  - `aryanpour.parts/05-d.xml:32077`
- `<xr>` content on its own line:
  - `aryanpour.parts/08-g.xml:3020`
  - `aryanpour.parts/08-g.xml:40995`
  - `aryanpour.parts/22-u.xml:10152`
- `<note>`:
  - `aryanpour.parts/02-a.xml:12`
  - `aryanpour.parts/08-g.xml:40996`

Recommendation: either keep mixed content on one line or accept the extra whitespace intentionally. If `<br/>` is not wanted in the target schema, replace it with separate `<quote>`/`<cit>` elements.

### 4. Duplicate headwords

After normalization, 404 `<orth>` values are duplicated within the same part file (410 globally). Most are legitimate English homographs or abbreviations (`a`, `A`, `B`, `s`, `y`, …). The Persian duplicates should be reviewed:

- `28-fa-aa.xml`: `آدم (خودمانی)`, `آلاله (گیاه شناسی)`, `آهسته (موسیقی)`, `آهسته و آرام (موسیقی)`, `آهنگ (موسیقی)`, `آهنگین (موسیقی)`
- `29-fa-alef.xml`: `احساس گرمی کردن (عامیانه)`, `اه!`
- `30-fa-b.xml`: `بهداشت`, `بی -`
- `31-fa-p.xml`: `پیش (در و پنجره)`
- `32-fa-t.xml`: `تشت`
- `35-fa-ch.xml`: `چراغ خوراک‌پزی`
- `37-fa-kh.xml`: `خوب (خودمانی)`
- `38-fa-d.xml`: `دب اصغر (نجوم)`
- `53-fa-k.xml`: `کامیون کوچک`

The count rose from 392 to 404 within-file duplicates because punctuation/ZWNJ normalization made some headwords identical. Confirm whether these are intentional homographs or accidental duplicates.

### 5. Empty punctuation/digit part

`aryanpour.parts/01-puncs-digits.xml` is 0 bytes but is still counted as one of the 61 files by `combine_tei.py` (“combined 61 files”). Options:

- remove it from the set and from `all_filenames()`, or
- keep it with a placeholder/comment explaining that no entries currently sort there.

### 6. Working file is out of sync

`aryanpour.tei` is git-ignored and still has the pre-sort entry order. Running `combine_tei.py` now produces the sorted part order, so its output will not be byte-identical to the current working `aryanpour.tei` (all entries/header/footer are preserved, only order differs). Regenerate it deliberately if needed.

### 7. Metadata date consistency

`00-header.xml` currently has:

- title `Aryanpour [2025-03]`
- edition `2025.03.02`
- publication date `2023-01-14`

The publication date may be intentional (original source date), but it is worth confirming.

## Code review: `split_tei.py` / `combine_tei.py`

- Entry regexes use `<entry>...</entry>`. They would silently skip `<entry attr="...">`; prefer `<entry(?:\s[^>]*)?>...</entry>`.
- `split_tei.py` attaches the footer to the file containing the last *entry*, not the numerically last filename. If the last entry ever sorts into another file, the closing `</body></text></TEI>` lands mid-set. Attach the footer to `all_filenames()[-1]` instead.
- `dedent_entry()` normalizes entry bodies but not the footer or trailing whitespace. Normalize the footer in the script so manual fixes are not needed.
- `entry_file()` silently routes unmapped Persian characters (hamza, diacritics, Arabic variants at word start) to the empty `01-puncs-digits.xml`. Add an assertion or explicit fallback so entries cannot disappear silently.
- `combine_tei.py` re-indents entries and depends on every part ending with a newline; add a validation step.
- There is no XML validation or test target. A small check using `xmllint` or `ElementTree` would catch malformed parts before publishing.

## Recommended order of work

1. Manually spot-check the ZWNJ-before-hyphen/parenthesis conversions.
2. Review the Persian duplicate headwords.
3. Clean up the rare `<br/>`/`<xr>` whitespace cases.
4. Add XML validation to the split/combine workflow.
