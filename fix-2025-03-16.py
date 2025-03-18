with open("Aryanpour.tei", encoding="utf-8") as _file:
	text = _file.read()


print(len(text), hash(text))

text = text.replace("خوراک پردازی", "خوراک‌پردازی")
text = text.replace("خوراکپردازی", "خوراک‌پردازی")
text = text.replace("خوراکپزی", "خوراک‌پزی")
text = text.replace("خوراک پزی", "خوراک‌پزی")
text = text.replace("امریکا", "آمریکا")
text = text.replace("آمریکا –", "آمریکا -")
text = text.replace("آمریکا-جانورشناسی", "آمریکا - جانورشناسی")
text = text.replace("آمریکا -خودمانی", "آمریکا - خودمانی")
text = text.replace("آمریکا-خودمانی", "آمریکا - خودمانی")
text = text.replace("آمریکا- عامیانه", "آمریکا- عامیانه")

print(len(text), hash(text))


with open("Aryanpour.tei", "w", encoding="utf-8") as _file:
	_file.write(text)

