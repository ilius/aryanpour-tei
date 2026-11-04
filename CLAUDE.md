# Project instructions

## Source of truth

- `aryanpour.parts/NN-*.xml` are the editable source files.
- `aryanpour.tei` in the project root is a manual build artifact for conversion and testing. Agents must always ignore it: never read, modify, compare against, or regenerate it unless explicitly asked.
- After any change to `aryanpour.parts/`, automatically update the dates in `00-header.xml` to the current date: `<title>Aryanpour [YYYY-MM]</title>`, `<edition>YYYY.MM.DD</edition>`, and `<publicationStmt><date>YYYY-MM-DD</date></publicationStmt>`.
- Record applied work in `changelog/YYYY-MM-DD.md`.
- Keep `review.md` for remaining issues only; remove items once fixed.
- Do not renumber remaining issues in `review.md` after removing fixed issues; keep their original numbers.

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

Expected: 181,144 entries, valid XML, and no ZWNJ before punctuation.
