#!/usr/bin/env python3
import argparse
import os
import re
import xml.etree.ElementTree as ET

ENTRY_RE = re.compile(r"<entry(?:\s[^>]*)?>.*?</entry>", re.S)
INDENT = "\t\t\t"


def read_part(path, name):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if text and not text.endswith("\n"):
        raise SystemExit(f"{name} does not end with a newline")
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default="aryanpour.parts")
    parser.add_argument("--output", default="aryanpour.tei")
    args = parser.parse_args()

    files = [n for n in os.listdir(args.indir) if re.fullmatch(r"\d+-.*\.xml", n)]
    files.sort(key=lambda n: int(n.split("-", 1)[0]))
    if not files:
        raise SystemExit(f"no part files found in {args.indir}")

    header = read_part(os.path.join(args.indir, files[0]), files[0]).rstrip()

    chunks = []
    for name in files[1:]:
        chunks.append(read_part(os.path.join(args.indir, name), name))
    body = "".join(chunks)

    matches = list(ENTRY_RE.finditer(body))
    footer = body[matches[-1].end():] if matches else body

    with open(args.output, "w", encoding="utf-8", newline="") as out:
        out.write(header)
        for match in matches:
            entry = match.group(0).replace("\n", "\n" + INDENT)
            out.write("\n" + INDENT + entry)
        if footer.strip():
            out.write("\n" + footer.lstrip("\n"))

    with open(args.output, encoding="utf-8") as f:
        combined = f.read()
    try:
        ET.fromstring(combined)
    except ET.ParseError as exc:
        raise SystemExit(f"combined output is not well-formed XML: {exc}")

    print(f"combined {len(files)} files, {len(matches)} entries into {args.output}")


if __name__ == "__main__":
    main()
