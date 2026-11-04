#!/usr/bin/env python3
import argparse
import os
import re

ENTRY_RE = re.compile(r"<entry>.*?</entry>", re.S)
INDENT = "\t\t\t"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default="aryanpour.parts")
    parser.add_argument("--output", default="aryanpour.tei")
    args = parser.parse_args()

    files = [n for n in os.listdir(args.indir) if re.fullmatch(r"\d+-.*\.xml", n)]
    files.sort(key=lambda n: int(n.split("-", 1)[0]))
    if not files:
        raise SystemExit(f"no part files found in {args.indir}")

    with open(os.path.join(args.indir, files[0]), encoding="utf-8") as f:
        header = f.read().rstrip()

    chunks = []
    for name in files[1:]:
        with open(os.path.join(args.indir, name), encoding="utf-8") as f:
            chunks.append(f.read())
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

    print(f"combined {len(files)} files, {len(matches)} entries into {args.output}")


if __name__ == "__main__":
    main()
