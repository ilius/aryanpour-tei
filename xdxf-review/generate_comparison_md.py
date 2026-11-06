#!/usr/bin/env python3
"""Build side-by-side TEI/XDXF comparison sheets for the sampled entries."""

from __future__ import annotations

import csv
import glob
import html
import os
import re
import xml.etree.ElementTree as ET

ENTRY_RE = re.compile(r"<entry(?:\s[^>]*)?>.*?</entry>", re.S)

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
PARTS = os.path.join(ROOT, "aryanpour.parts")


def load_entries() -> dict[str, list[str]]:
	by_file: dict[str, list[str]] = {}
	for path in sorted(glob.glob(os.path.join(PARTS, "*.xml"))):
		name = os.path.basename(path)
		if name.startswith("00-"):
			continue
		text = open(path, encoding="utf-8").read()
		by_file[name] = [m.group(0) for m in ENTRY_RE.finditer(text)]
	return by_file


def load_articles(filename: str) -> list[ET.Element]:
	root = ET.parse(os.path.join(BASE, filename)).getroot()
	lexicon = root.find("lexicon")
	return list(lexicon) if lexicon is not None else []


def pretty(elem: ET.Element) -> str:
	clone = ET.fromstring(ET.tostring(elem, encoding="unicode"))
	ET.indent(clone)
	return ET.tostring(clone, encoding="unicode")


def code(lang: str, body: str) -> str:
	return f"```{lang}\n{body}\n```"


def tag(el: ET.Element) -> str:
	return el.tag.rsplit("}", 1)[-1]


def serialize(children: list[ET.Element]) -> str:
	return "\n".join(pretty(child) for child in children)


def build(direction: str, xdxf_file: str, out_file: str) -> None:
	entries = load_entries()
	articles = load_articles(xdxf_file)

	rows = []
	with open(os.path.join(BASE, "selected-entries.tsv"), encoding="utf-8") as src:
		for row in csv.DictReader(src, delimiter="\t"):
			if row["direction"] == direction:
				rows.append(row)

	if len(rows) != len(articles):
		raise SystemExit(
			f"{direction}: {len(rows)} rows but {len(articles)} XDXF articles"
		)

	out = [
		f"# {xdxf_file} TEI vs XDXF comparison (sense by sense)",
		"",
		f"Direction: `{direction}`. Each entry shows the source TEI from "
		f"`aryanpour.parts/` and the converted XDXF article from `{xdxf_file}`, "
		"split so that each TEI `<sense>` is paired with its XDXF `<def>`.",
		"",
	]

	for i, (row, article) in enumerate(zip(rows, articles), 1):
		tei = ET.fromstring(entries[row["file"]][int(row["index"])])
		tei_header = [c for c in tei if tag(c) in ("form", "usg")]
		xdxf_header = [c for c in article if tag(c) in ("k", "tr", "categ")]
		tei_senses = [c for c in tei if tag(c) == "sense"]
		xdxf_defs = [c for c in article if tag(c) == "def"]

		out.append(f"## {i}. {row['headword']}")
		out.append("")
		out.append(
			f"TEI source: `{row['file']}` entry {row['index']} "
			f"(score {row['score']}, rare {row['rare']})  "
		)
		out.append(
			f"XDXF article: `{xdxf_file}` # {i} "
			f"(key `{html.unescape(''.join(article.find('k').itertext()).strip())}`, "
			f"{len(xdxf_defs)} senses)"
		)
		out.append("")
		out.append("### Headword / form")
		out.append("")
		out.append("TEI:")
		out.append("")
		out.append(code("xml", serialize(tei_header) or "(none)"))
		out.append("")
		out.append("XDXF:")
		out.append("")
		out.append(code("xml", serialize(xdxf_header) or "(none)"))
		out.append("")

		if len(tei_senses) != len(xdxf_defs):
			out.append(
				f"> Sense count differs: {len(tei_senses)} TEI senses vs "
				f"{len(xdxf_defs)} XDXF defs."
			)
			out.append("")

		for j, (sense, definition) in enumerate(
			zip(tei_senses, xdxf_defs), 1
		):
			n = sense.get("n") or definition.get("n") or str(j)
			out.append(f"### Sense {j} (n={n})")
			out.append("")
			out.append("TEI:")
			out.append("")
			out.append(code("xml", pretty(sense)))
			out.append("")
			out.append("XDXF:")
			out.append("")
			out.append(code("xml", pretty(definition)))
			out.append("")

	with open(os.path.join(BASE, out_file), "w", encoding="utf-8") as dst:
		dst.write("\n".join(out))
	print(f"wrote {out_file}: {len(rows)} entries")


def main() -> None:
	build("en", "en-fa.xdxf", "en-fa.md")
	build("fa", "fa-en.xdxf", "fa-en.md")


if __name__ == "__main__":
	main()
