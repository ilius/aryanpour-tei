#!/usr/bin/env python3
"""Check aryanpour TEI structure against the FreeDict reader expectations."""

import argparse
import xml.etree.ElementTree as ET

NS = "{http://www.tei-c.org/ns/1.0}"

ALLOWED_TAGS = {
	"body", "entry", "form", "orth", "pron", "usg", "sense", "cit",
	"quote", "gramGrp", "pos", "gen", "number", "num", "subc", "gram",
	"note", "def", "lang", "xr", "ref", "br", "div", "span", "re",
	"etym", "lbl",
}
USG_TYPES = {
	"dom", "domain", "reg", "register", "geo", "gram", "time", "lang",
	"style", "plev", "hint", "syn", "hyper", "colloc", "comp", "obj",
	"subj", "verb", "category",
}
NOTE_TYPES = {
	"sense", "stagr", "stagk", "def", "usage", "hint", "status",
	"editor", "dom", "infl", "obj", "lbl", "gloss", "idarex",
}
CIT_TYPES = {None, "trans", "example", "idiom"}
USG_PARENTS = {"entry", "form", "sense", "cit"}


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", nargs="?", default="/tmp/combined.tei")
	args = parser.parse_args()

	root = ET.parse(args.input).getroot()
	body = root.find(f".//{NS}body")
	if body is None:
		raise SystemExit("no TEI body found")

	parents = {child: parent for parent in body.iter() for child in parent}
	problems = []
	for el in body.iter():
		tag = el.tag.replace(NS, "")
		if tag not in ALLOWED_TAGS:
			problems.append(f"unexpected tag: {tag}")
		if tag == "usg":
			if not "".join(el.itertext()).strip():
				problems.append("empty usg")
			if el.get("type") not in USG_TYPES:
				problems.append(f"unknown usg type: {el.get('type')!r}")
			parent = parents.get(el)
			if parent is None or parent.tag.replace(NS, "") not in USG_PARENTS:
				problems.append("bad usg parent")
		if tag == "cit" and el.get("type") not in CIT_TYPES:
			problems.append(f"unknown cit type: {el.get('type')!r}")
		if tag == "note":
			type_ = el.get("type")
			if type_ and type_ not in NOTE_TYPES:
				problems.append(f"unknown note type: {type_!r}")

	print("structure problems:", len(problems))
	for problem in problems[:20]:
		print(" ", problem)
	if problems:
		raise SystemExit(1)


if __name__ == "__main__":
	main()
