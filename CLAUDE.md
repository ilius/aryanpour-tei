# Project instructions

## Source of truth

- `aryanpour.parts/NN-*.xml` are the editable source files.
- `aryanpour.tei` in the project root is a manual build artifact for conversion and testing. Agents must always ignore it: never read, modify, compare against, or regenerate it unless explicitly asked.
- After any change to `aryanpour.parts/`, automatically update the dates in `00-header.xml` to the current date: `<title>Aryanpour [YYYY-MM]</title>`, `<edition>YYYY.MM.DD</edition>`, and `<publicationStmt><date>YYYY-MM-DD</date></publicationStmt>`.
- Record applied work in `changelog/YYYY-MM-DD.md`.
- Keep `review.md` for remaining issues only; remove items once fixed.
- Do not renumber remaining issues in `review.md` after removing fixed issues; keep their original numbers.

## Reference code

- Read `~/pyglossary` for the FreeDict reader and related code/docs.
- Do not modify or commit anything in `~/pyglossary` unless explicitly asked.

## FreeDict reader structure

`~/pyglossary/pyglossary/plugins/freedict/reader.py` reads TEI in the
`http://www.tei-c.org/ns/1.0` namespace. Keep `aryanpour.parts/` within this
structure:

- `TEI/text/body/entry`.
- `entry` children: `form` (`orth`, `pron`, `usg`), `usg`, `sense`.
- `sense` (nestable): `cit`, `def`, `note`, `ref`, `usg`, `lang`, `xr`,
  `form`, `gramGrp`, nested `sense`.
- `cit`: `type="trans"` for translations, `type="example"` for examples, and
  `type="idiom"` (treated as a translation). A translation `cit` may contain
  `quote`, `gramGrp`, `usg`, and `note` (nested `cit` is skipped); an example
  `cit` may contain `quote`, `usg`, and nested translation `cit`.
- `gramGrp`: `pos`, `gen`, `number`/`num`, `subc`, `gram`, `note`, `colloc`.
- `usg`: text or inline content. TEI allows it under `entry`, `form`, `sense`,
  `cit`, `gramGrp`, `etym`, or `xr`; the FreeDict reader renders it as a tag
  under `entry`, `form`, `sense`, and `cit`, so keep it in those parents. TEI
  sample `type` values are `geo`, `time`, `dom`, `register`, `style`, `plev`,
  `lang`, `gram`, `syn`, `hyper`, `colloc`, `comp`, `obj`, `subj`, `verb`,
  `hint`; FreeDict also uses `reg`, and TEI examples use `domain` and
  `category` (the attribute is an open enumeration).
- `note`: no `type` renders as a note; `type="pos"`/`"gram"` renders as grammar;
  the recognized note types below render as notes; unknown types warn but are
  still rendered. Recognized types: `sense`, `stagr`, `stagk`, `def`, `usage`,
  `hint`, `status`, `editor`, `dom`, `infl`, `obj`, `lbl`, `gloss`, `idarex`.
- Inline content: `ref` is linked. `quote`/`note`/`xr` use the rich-text writer
  and support `br`, `p`, `div`, `span`; `def` handles `ref` specially and
  recurses other inline elements as text.
- `xml:lang` on `form`/`sense`/`cit`/`quote` controls language, RTL, and
  direction.

Re-read the reader and update this summary/check only when explicitly asked or
when the reader itself changes. Do not re-audit `~/pyglossary` on every content
change; routine content changes only need the checks below.

## Validation

Run before finishing:

```bash
python3 combine_tei.py --output /tmp/combined.tei
python3 - <<'PY'
import re, xml.etree.ElementTree as ET
text = open('/tmp/combined.tei', encoding='utf-8').read()
ET.fromstring(text)
print('entries:', len(re.findall(r'<entry>', text)))
print('ZWNJ before punctuation:', len(re.findall(r'\u200c[-–(\)!؟;.,:&/"]', text)))
PY
```

Then check the content structure against the summary above:

```bash
python3 check_structure.py /tmp/combined.tei
```

Expected: 181,144 entries, valid XML, no ZWNJ before punctuation, and
`structure problems: 0`.

Whenever `aryanpour.parts/` changes, run both checks automatically; if a check
fails, fix the content before finishing. Do not re-check `~/pyglossary` unless
asked.
