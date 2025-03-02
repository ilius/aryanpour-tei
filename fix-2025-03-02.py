with open("Aryanpour.tei", encoding="utf-8") as _file:
	text = _file.read()


text = text.replace("\u200c</orth>", "</orth>")
text = text.replace("\u200c</pron>", "</pron>")
text = text.replace(" </orth>", "</orth>")
text = text.replace(" </pron>", "</pron>")
text = text.replace("\u200c ", " ")
text = text.replace(" \u200c", " ")


with open("Aryanpour.tei", "w", encoding="utf-8") as _file:
	_file.write(text)
