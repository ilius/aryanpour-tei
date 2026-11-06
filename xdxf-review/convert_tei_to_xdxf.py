#!/usr/bin/env python3
"""Select 100 entries from aryanpour.parts and convert them to XDXF.

English-headword entries (en -> fa) and Persian-headword entries (fa -> en)
are written to separate XDXF files because XDXF allows only one language pair
per dictionary.
"""

from __future__ import annotations

import argparse
import collections
import glob
import html
import os
import re
import xml.etree.ElementTree as ET

TEI_NS = "http://www.tei-c.org/ns/1.0"
NS = f"{{{TEI_NS}}}"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
ENTRY_RE = re.compile(r"<entry(?:\s[^>]*)?>.*?</entry>", re.S)
WS_RE = re.compile(r"[ \t\r\n]+")


def tag_name(el: ET.Element) -> str:
	return el.tag.replace(NS, "")


def local_name(tag: str) -> str:
	return tag.rsplit("}", 1)[-1]


def entry_info(raw: str) -> dict:
	"""Cheap string-based metadata used for sampling."""
	form = re.search(r"<form([^>]*)>\s*<orth", raw, re.S)
	lang_match = re.search(r'xml:lang="([^"]+)"', form.group(1)) if form else None
	direction = lang_match.group(1) if lang_match and lang_match.group(1) in ("en", "fa") else "en"
	orth = re.search(r"<orth>(.*?)</orth>", raw, re.S)
	headword = html.unescape(re.sub(r"<[^>]+>", "", orth.group(1))).strip() if orth else ""
	n_sense = raw.count("<sense")
	n_cit = raw.count("<cit")
	n_ex = raw.count('type="example"')
	n_usg = raw.count("<usg")
	n_gram = raw.count("<gramGrp")
	n_ref = raw.count("<ref")
	n_xr = raw.count("<xr")
	n_def = raw.count("<def")
	n_note = raw.count("<note")
	n_br = raw.count("<br")
	n_form = raw.count("<form")
	rare = bool(n_xr or n_def or n_note or n_br)
	if direction == "en":
		score = (
			3 * n_sense
			+ 2 * n_ex
			+ 2 * n_usg
			+ n_gram
			+ n_ref
			+ 4 * n_xr
			+ 6 * n_def
			+ 6 * n_note
			+ 2 * max(0, n_form - 1)
		)
	else:
		score = n_cit + n_ref + len(headword) // 12
	return {
		"direction": direction,
		"headword": headword,
		"score": score,
		"rare": rare,
		"features": {
			"senses": n_sense,
			"cits": n_cit,
			"examples": n_ex,
			"usg": n_usg,
			"gramGrp": n_gram,
			"ref": n_ref,
			"xr": n_xr,
			"def": n_def,
			"note": n_note,
			"br": n_br,
			"forms": n_form,
		},
	}


def scan(indir: str) -> list[dict]:
	records = []
	for path in sorted(glob.glob(os.path.join(indir, "*.xml"))):
		name = os.path.basename(path)
		if name.startswith("00-"):
			continue
		text = open(path, encoding="utf-8").read()
		for index, match in enumerate(ENTRY_RE.finditer(text)):
			info = entry_info(match.group(0))
			info.update(path=path, index=index, raw=match.group(0), part=name)
			records.append(info)
	return records


def pick_even(candidates: list[dict], count: int, part_order: list[str]) -> list[dict]:
	"""Pick `count` candidates spread round-robin across part files."""
	by_part = collections.defaultdict(list)
	for rec in candidates:
		by_part[rec["part"]].append(rec)
	for part in by_part:
		by_part[part].sort(key=lambda r: (r["score"], r["headword"], r["index"]))
	queues = [by_part[p] for p in part_order if p in by_part]
	picked = []
	pos = 0
	while len(picked) < count:
		added = False
		for queue in queues:
			if pos < len(queue):
				picked.append(queue[pos])
				added = True
				if len(picked) == count:
					break
		if not added:
			break
		pos += 1
	return picked


def select(records: list[dict]) -> dict[str, list[dict]]:
	by_direction = {"en": [], "fa": []}
	for rec in records:
		by_direction[rec["direction"]].append(rec)

	result = {"en": [], "fa": []}
	for direction, quota, distribution in (
		("en", 50, (("rare", None), ("simple", 0), ("medium", 0), ("complex", 0))),
		("fa", 50, (("simple", 25), ("medium", 15), ("complex", 10))),
	):
		pool = by_direction[direction]
		part_order = sorted({r["part"] for r in pool})
		chosen = []
		chosen_keys = set()

		def add(rec):
			key = (rec["part"], rec["index"])
			if key not in chosen_keys:
				chosen_keys.add(key)
				chosen.append(rec)

		if direction == "en":
			# One simple entry from every part file.
			for part in part_order:
				candidates = [
					r for r in pool
					if r["part"] == part and not r["rare"] and r["score"] <= 10
				]
				candidates.sort(key=lambda r: (r["score"], r["index"]))
				if candidates:
					add(candidates[0])
			# Every entry with a construct that is rare in the dictionary.
			for rec in sorted((r for r in pool if r["rare"]), key=lambda r: (r["part"], r["index"])):
				add(rec)
			# One representative for every <usg> type and the only <gen>.
			for usg_type in ("dom", "reg", "time", "plev", "hint", "gram", "geo", "style", "lang"):
				match = [r for r in pool if f'<usg type="{usg_type}"' in r["raw"]]
				match.sort(key=lambda r: (r["score"], r["headword"], r["part"], r["index"]))
				if match:
					add(match[0])
			for rec in sorted((r for r in pool if "<gen" in r["raw"]), key=lambda r: (r["score"], r["part"], r["index"])):
				add(rec)
			forced = set(chosen_keys)
			medium = [r for r in pool if (r["part"], r["index"]) not in forced and 7 <= r["score"] <= 40]
			complex_ = [r for r in pool if (r["part"], r["index"]) not in forced and r["score"] > 40]
			remaining = quota - len(chosen)
			giants = sorted(complex_, key=lambda r: r["score"], reverse=True)[:3]
			complex_rest = [r for r in complex_ if r not in giants]
			for rec in giants:
				add(rec)
			for rec in pick_even(medium, max(0, remaining - len(giants)), part_order):
				add(rec)
			remaining = quota - len(chosen)
			for rec in pick_even(complex_rest, remaining, part_order):
				add(rec)
		else:
			# One simple entry from every part file.
			for part in part_order:
				candidates = [r for r in pool if r["part"] == part and r["score"] <= 2]
				candidates.sort(key=lambda r: (abs(r["score"] - 2), r["index"]))
				if candidates:
					add(candidates[0])
			forced = set(chosen_keys)
			medium = [r for r in pool if (r["part"], r["index"]) not in forced and 3 <= r["score"] <= 10]
			complex_ = [r for r in pool if (r["part"], r["index"]) not in forced and r["score"] > 10]
			remaining = quota - len(chosen)
			offset = len(part_order) // 2
			rotated = part_order[offset:] + part_order[:offset]
			complex_count = (remaining + 1) // 2
			for rec in pick_even(complex_, complex_count, rotated):
				add(rec)
			remaining = quota - len(chosen)
			for rec in pick_even(medium, remaining, rotated):
				add(rec)

		if len(chosen) != quota:
			raise SystemExit(f"{direction}: selected {len(chosen)} entries, expected {quota}")
		result[direction] = sorted(chosen, key=lambda r: (r["part"], r["index"]))
	return result


def normalize_text(value: str | None) -> str:
	if not value:
		return ""
	return WS_RE.sub(" ", value)


def append_text(parent: ET.Element, value: str | None) -> None:
	value = normalize_text(value)
	if not value:
		return
	if len(parent):
		last = parent[-1]
		last.tail = (last.tail or "") + value
	else:
		parent.text = (parent.text or "") + value


def set_text(el: ET.Element, value: str | None) -> None:
	value = normalize_text(value)
	if value:
		el.text = value


def trim_block(el: ET.Element) -> None:
	if el.text:
		el.text = el.text.lstrip()
	if len(el):
		last = el[-1]
		if last.tail:
			last.tail = last.tail.rstrip()
	elif el.text:
		el.text = el.text.rstrip()


def copy_inline(el: ET.Element, parent: ET.Element) -> None:
	append_text(parent, el.text)
	for child in el:
		name = tag_name(child)
		if name == "ref":
			target = child.get("target")
			if target:
				node = ET.SubElement(parent, "iref", {"href": target})
			else:
				node = ET.SubElement(parent, "kref")
			copy_inline(child, node)
		elif name == "br":
			ET.SubElement(parent, "br")
		elif name in ("i", "b", "sup", "sub"):
			node = ET.SubElement(parent, name)
			copy_inline(child, node)
		else:
			copy_inline(child, parent)
		append_text(parent, child.tail)


def lang_attr(el: ET.Element) -> dict[str, str]:
	value = el.get(XML_LANG)
	return {XML_LANG: value} if value else {}


def add_gram_grp(gram: ET.Element, parent: ET.Element) -> None:
	for child in gram:
		name = tag_name(child)
		text = "".join(child.itertext()).strip()
		if not text:
			text = child.get("norm", "")
		if name == "pos":
			node = ET.SubElement(parent, "pos")
			set_text(node, text)
		elif name in ("gen", "number", "num", "subc", "gram", "colloc"):
			node = ET.SubElement(parent, "gr")
			set_text(node, text)
		elif name == "note":
			node = ET.SubElement(parent, "c", {"c": "gray"})
			copy_inline(child, node)
		else:
			node = ET.SubElement(parent, "gr")
			set_text(node, text)


def add_cit(cit: ET.Element, parent: ET.Element) -> None:
	cit_type = cit.get("type")
	if cit_type == "trans":
		node = ET.SubElement(parent, "dtrn", lang_attr(cit))
		for child in cit:
			name = tag_name(child)
			if name == "quote":
				copy_inline(child, node)
				append_text(node, child.tail)
			elif name == "gramGrp":
				add_gram_grp(child, node)
				append_text(node, child.tail)
			elif name == "usg":
				usg = ET.SubElement(node, "categ", {"type": child.get("type", "")})
				set_text(usg, "".join(child.itertext()))
				append_text(node, child.tail)
			elif name == "note":
				note = ET.SubElement(node, "c", {"c": "gray"})
				copy_inline(child, note)
				append_text(node, child.tail)
			elif name != "cit":
				copy_inline(child, node)
				append_text(node, child.tail)
		trim_block(node)
	elif cit_type == "example":
		node = ET.SubElement(parent, "ex", lang_attr(cit))
		for child in cit:
			name = tag_name(child)
			if name == "quote":
				orig = ET.SubElement(node, "ex_orig", lang_attr(child))
				copy_inline(child, orig)
				trim_block(orig)
				append_text(node, child.tail)
			elif name == "cit" and child.get("type") == "trans":
				tran = ET.SubElement(node, "ex_tran", lang_attr(child))
				for grandchild in child:
					if tag_name(grandchild) == "quote":
						copy_inline(grandchild, tran)
						append_text(tran, grandchild.tail)
					elif tag_name(grandchild) == "gramGrp":
						add_gram_grp(grandchild, tran)
				trim_block(tran)
				append_text(node, child.tail)
			elif name in ("usg", "note"):
				inline = ET.SubElement(node, "c", {"c": "gray"})
				copy_inline(child, inline)
				append_text(node, child.tail)
		trim_block(node)
	else:
		copy_inline(cit, parent)


def add_sense(sense: ET.Element, parent: ET.Element) -> None:
	attrs = {}
	if sense.get("n"):
		attrs["n"] = sense.get("n")
	attrs.update(lang_attr(sense))
	node = ET.SubElement(parent, "def", attrs)
	for child in sense:
		name = tag_name(child)
		if name == "sense":
			add_sense(child, node)
			append_text(node, child.tail)
		elif name == "gramGrp":
			add_gram_grp(child, node)
			append_text(node, child.tail)
		elif name == "usg":
			usg = ET.SubElement(node, "categ", {"type": child.get("type", "")})
			set_text(usg, "".join(child.itertext()))
			append_text(node, child.tail)
		elif name == "cit":
			add_cit(child, node)
			append_text(node, child.tail)
		elif name == "note":
			note = ET.SubElement(node, "c", {"c": "gray", **lang_attr(child)})
			copy_inline(child, note)
			trim_block(note)
			append_text(node, child.tail)
		elif name == "def":
			dtrn = ET.SubElement(node, "dtrn", lang_attr(child))
			copy_inline(child, dtrn)
			trim_block(dtrn)
			append_text(node, child.tail)
		elif name == "xr":
			dtrn = ET.SubElement(node, "dtrn", lang_attr(child))
			copy_inline(child, dtrn)
			trim_block(dtrn)
			append_text(node, child.tail)
		else:
			copy_inline(child, node)
			append_text(node, child.tail)
	trim_block(node)


def convert_entry(raw: str, direction: str) -> ET.Element:
	root = ET.fromstring(f'<TEI xmlns="{TEI_NS}">{raw}</TEI>')
	entry = root[0]
	ar = ET.Element("ar")

	for form in entry:
		if tag_name(form) != "form":
			continue
		for child in form:
			if tag_name(child) == "orth":
				k = ET.SubElement(ar, "k")
				copy_inline(child, k)
				trim_block(k)
	if not len(ar):
		raise SystemExit("entry has no orth")

	for form in entry:
		if tag_name(form) != "form":
			continue
		for child in form:
			if tag_name(child) == "pron":
				tr = ET.SubElement(ar, "tr")
				copy_inline(child, tr)
				trim_block(tr)
		for child in form:
			if tag_name(child) == "usg":
				usg = ET.SubElement(ar, "categ", {"type": child.get("type", "")})
				set_text(usg, "".join(child.itertext()))

	for child in entry:
		name = tag_name(child)
		if name == "usg":
			usg = ET.SubElement(ar, "categ", {"type": child.get("type", "")})
			set_text(usg, "".join(child.itertext()))
		elif name == "sense":
			add_sense(child, ar)

	return ar


def build_xdxf(records: list[dict], direction: str, title: str) -> ET.ElementTree:
	from_code, to_code = ("ENG", "PER") if direction == "en" else ("PER", "ENG")
	root = ET.Element(
		"xdxf",
		{"lang_from": from_code, "lang_to": to_code, "format": "visual"},
	)
	name = ET.SubElement(root, "full_name")
	name.text = title
	desc = ET.SubElement(root, "description")
	desc.text = (
		f"Manual-review sample of {len(records)} Aryanpour entries. "
		"Converted directly from aryanpour.parts TEI. "
		"Entries were sampled across the alphabet and complexity levels."
	)
	lexicon = ET.SubElement(root, "lexicon")
	for rec in records:
		lexicon.append(convert_entry(rec["raw"], direction))
	return root


def serialize_xdxf(root: ET.Element) -> str:
	"""Serialize with one <ar> per line.

	Whitespace inside <ar> or <def> would become part of the rendered article,
	so only element-only containers (<xdxf>, <lexicon>) get indentation.
	"""
	lines = ['<?xml version="1.0" encoding="UTF-8"?>']
	lines.append(
		"<!-- Pragmatic XDXF sample for manual review: TEI sense -> def, "
		"cit trans -> dtrn, cit example -> ex/ex_orig/ex_tran, usg -> categ, "
		"gramGrp -> pos/gr, note -> c, xr/def -> dtrn, ref -> kref/iref. -->"
	)
	attrs = " ".join(f'{key}="{value}"' for key, value in root.attrib.items())
	lines.append(f"<xdxf {attrs}>")
	for child in root:
		if child.tag == "lexicon":
			lines.append("\t<lexicon>")
			for article in child:
				lines.append("\t\t" + ET.tostring(article, encoding="unicode"))
			lines.append("\t</lexicon>")
		else:
			lines.append("\t" + ET.tostring(child, encoding="unicode"))
	lines.append("</xdxf>")
	return "\n".join(lines) + "\n"


def write_manifest(path: str, records: dict[str, list[dict]]) -> None:
	with open(path, "w", encoding="utf-8") as out:
		out.write("direction\tfile\tindex\theadword\tscore\trare\tsenses\tcits\texamples\tusg\tgramGrp\tref\txr\tdef\tnote\tbr\tforms\n")
		for direction in ("en", "fa"):
			for rec in records[direction]:
				f = rec["features"]
				out.write(
					"\t".join(
						map(
							str,
							(
								direction,
								rec["part"],
								rec["index"],
								rec["headword"],
								rec["score"],
								int(rec["rare"]),
								f["senses"],
								f["cits"],
								f["examples"],
								f["usg"],
								f["gramGrp"],
								f["ref"],
								f["xr"],
								f["def"],
								f["note"],
								f["br"],
								f["forms"],
							),
						)
					)
					+ "\n"
				)


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--indir", default="aryanpour.parts")
	parser.add_argument("--outdir", default="xdxf-review")
	args = parser.parse_args()

	os.makedirs(args.outdir, exist_ok=True)
	records = scan(args.indir)
	print(f"scanned {len(records)} entries")
	selected = select(records)
	for direction, title, filename in (
		("en", "Aryanpour sample (English -> Persian)", "en-fa.xdxf"),
		("fa", "Aryanpour sample (Persian -> English)", "fa-en.xdxf"),
	):
		root = build_xdxf(selected[direction], direction, title)
		with open(os.path.join(args.outdir, filename), "w", encoding="utf-8") as out:
			out.write(serialize_xdxf(root))
		print(f"wrote {filename}: {len(selected[direction])} entries")
	write_manifest(os.path.join(args.outdir, "selected-entries.tsv"), selected)


if __name__ == "__main__":
	main()
