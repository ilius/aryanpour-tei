#!/usr/bin/env python3
import argparse
import os
import re
import unicodedata

ENGLISH = "abcdefghijklmnopqrstuvwxyz"
PERSIAN = [
    ("\u0622", "28-fa-aa"),
    ("\u0627", "29-fa-alef"),
    ("\u0628", "30-fa-b"),
    ("\u067e", "31-fa-p"),
    ("\u062a", "32-fa-t"),
    ("\u062b", "33-fa-se"),
    ("\u062c", "34-fa-j"),
    ("\u0686", "35-fa-ch"),
    ("\u062d", "36-fa-h"),
    ("\u062e", "37-fa-kh"),
    ("\u062f", "38-fa-d"),
    ("\u0630", "39-fa-zal"),
    ("\u0631", "40-fa-r"),
    ("\u0632", "41-fa-z"),
    ("\u0698", "42-fa-zh"),
    ("\u0633", "43-fa-s"),
    ("\u0634", "44-fa-sh"),
    ("\u0635", "45-fa-sad"),
    ("\u0636", "46-fa-zad"),
    ("\u0637", "47-fa-ta"),
    ("\u0638", "48-fa-za"),
    ("\u0639", "49-fa-eyn"),
    ("\u063a", "50-fa-gh"),
    ("\u0641", "51-fa-f"),
    ("\u0642", "52-fa-ghaf"),
    ("\u06a9", "53-fa-k"),
    ("\u06af", "54-fa-g"),
    ("\u0644", "55-fa-l"),
    ("\u0645", "56-fa-m"),
    ("\u0646", "57-fa-n"),
    ("\u0648", "58-fa-v"),
    ("\u0647", "59-fa-he"),
    ("\u06cc", "60-fa-ye"),
]
PERSIAN_MAP = dict(PERSIAN)
PERSIAN_RANK = {ch: i for i, (ch, _) in enumerate(PERSIAN)}
ARABIC_VARIANTS = {
    "\u0623": "\u0627",
    "\u0625": "\u0627",
    "\u0624": "\u0648",
    "\u0626": "\u06cc",
    "\u0629": "\u0647",
    "\u064a": "\u06cc",
    "\u0643": "\u06a9",
}
LATIN_VARIANTS = {
    "\u00e6": "ae",
    "\u0153": "oe",
}
ENGLISH_MAP = {chr(ord("a") + i): f"{i + 2:02d}-{chr(ord('a') + i)}" for i in range(26)}
PUNC_FILE = "01-puncs-digits"
HEADER_FILE = "00-header"
ENTRY_RE = re.compile(r"<entry>.*?</entry>", re.S)


def fold_latin(ch):
    decomposed = unicodedata.normalize("NFKD", ch)
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    for c in stripped:
        if c.isalpha():
            return c.lower()
    return None


def sort_key(headword):
    primary = []
    for ch in headword:
        ch = ARABIC_VARIANTS.get(ch, ch)
        if ch in PERSIAN_RANK:
            primary.append((1, PERSIAN_RANK[ch]))
            continue
        for c in LATIN_VARIANTS.get(ch, ch):
            if not c.isalnum():
                continue
            folded = fold_latin(c)
            primary.append((2, folded if folded else c.casefold()))
    return tuple(primary), headword.casefold()


def entry_file(headword):
    for ch in headword:
        if not ch.isalpha():
            continue
        if "\u0600" <= ch <= "\u06ff":
            return PERSIAN_MAP.get(ch, PUNC_FILE)
        base = fold_latin(ch)
        if base in ENGLISH_MAP:
            return ENGLISH_MAP[base]
        return PUNC_FILE
    return PUNC_FILE


def all_filenames():
    names = [HEADER_FILE, PUNC_FILE]
    names.extend(ENGLISH_MAP[c] for c in ENGLISH)
    seen = set()
    for _, name in PERSIAN:
        if name not in seen:
            names.append(name)
            seen.add(name)
    return names


def dedent_entry(text):
    lines = text.split("\n")
    prefixes = []
    for line in lines[1:]:
        if line.strip():
            prefixes.append(line[: len(line) - len(line.lstrip(" \t"))])
    if not prefixes:
        return text
    base = os.path.commonprefix(prefixes)
    if not base:
        return text
    return "\n".join(
        [lines[0]]
        + [line[len(base):] if line.startswith(base) else line for line in lines[1:]]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="aryanpour.tei")
    parser.add_argument("--outdir", default="aryanpour.parts")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        data = f.read()

    matches = list(ENTRY_RE.finditer(data))
    if not matches:
        raise SystemExit("no entries found")

    header = data[: matches[0].start()]
    footer = data[matches[-1].end():]

    outputs = {name: [] for name in all_filenames()}
    last_file = None

    for match in matches:
        entry = match.group(0)
        orth = re.search(r"<orth>(.*?)</orth>", entry, re.S)
        headword = orth.group(1) if orth else ""
        last_file = entry_file(headword)
        outputs[last_file].append((headword, dedent_entry(entry)))

    os.makedirs(args.outdir, exist_ok=True)

    for name in all_filenames():
        path = os.path.join(args.outdir, name + ".xml")
        if name == HEADER_FILE:
            content = header.rstrip() + "\n"
        else:
            entries = sorted(outputs[name], key=lambda item: sort_key(item[0]))
            content = "\n".join(entry for _, entry in entries)
            if content:
                content += "\n"
            if name == last_file:
                content += footer.lstrip("\n")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)

    print(f"wrote {len(outputs)} files to {args.outdir}")
    print(f"header + {len(matches)} entries")


if __name__ == "__main__":
    main()
