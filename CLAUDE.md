# Project instructions

## Source of truth

- `aryanpour.parts/NN-*.xml` are the editable source files.
- `aryanpour.tei` is generated/git-ignored; regenerate only when needed.
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

Expected: 181,160 entries, valid XML, and no ZWNJ before punctuation.
