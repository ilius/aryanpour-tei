
# What is the difference between (انگلیس - سابقا) and (انگلیس - قدیمی)

with open("Aryanpour.tei", encoding="utf-8") as _file:
	text = _file.read()


print(len(text), hash(text))

text = text.replace("اسب سواری", "اسب‌سواری")
text = text.replace("اسطوره یونان", "اسطورهٔ یونان")
text = text.replace("(هندسه و ریاضی)", "(هندسه و ریاضیات)")
text = text.replace(" آمیز)", "\u200cآمیز)")
text = text.replace("(انگلیس‌-عامیانه)", "(انگلیس - عامیانه)")


print(len(text), hash(text))


with open("Aryanpour.tei", "w", encoding="utf-8") as _file:
	_file.write(text)



"""
domain name in sense.sense.cit.quote
grep -P '<quote>\(.{3,20}\)</quote>' Aryanpour.tei | sort | uniq | less

<entry>
    <form xml:lang="en">
        <orth>sparrow</orth>
        <pron>spar´ō</pron>
    </form>
    <sense n="1" xml:lang="fa">
        <gramGrp>
            <pos norm="noun">اسم</pos>
        </gramGrp>
        <sense xml:lang="fa">
            <cit type="trans">
                <quote>(جانورشناسی)</quote>
            </cit>
        </sense>
		...
    </sense>
</entry>
"""



# Domain and Register
# https://github.com/freedict/fd-dictionaries/blob/master/freedict-editor/src/values.c
# https://tei-c.org/release/doc/tei-p5-doc/en/html/examples-usg.html
# https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-domain.html
# Domain:
# 	TEI 12.3.5.2 Usage Information and Other Labels
# 	Encoded as <usg type="dom">agr</usg> inside <sense>
# Register:
# 	Encoded as <usg type="reg">official</usg> inside <sense>
# Examples:
# <usg type="dom">zoology</usg>
# <usg type="dom">Zoology</usg>
# <usg norm="nautical" type="dom">naut.</usg>

# Source: https://github.com/freedict/fd-dictionaries/blob/master/freedict-editor/src/values.c
# taken from fdicts.com
domainByDesc = {
	"Agriculture": "agr",
	"Astronomy": "astr",
	"Automobile": "aut",
	"Biology": "bio",
	"Botany": "bot",
	"Chemistry": "chem",
	"Electrotechnics": "el",
	"Finance": "fin",
	"Geography": "geo",
	"Geology": "geol",
	"Grammar": "gram",
	"History": "hist",
	"Information Technology": "it",
	"Law": "law",
	"Mathematics": "math",
	"Medicine": "med",
	"Military": "mil",
	"Music": "mus",
	"Mythology": "myt",
	"Physics": "phy",
	"Politics": "pol",
	"Religion": "rel",
	"Sexual": "sex",
	"Sport": "sport",
	"Technology": "tech",
	# the rest are added by Saeed Rasooli
	"Zoology": "zoo",

	"Education": "edu",
	"Literary": "lit",
	"Ski": "ski",
	"Economy": "econ",
	"Academic": "academic",
	"Business": "business",
	"Mechanics": "mechanics",
	"Geometry", "geom",

	"Islam": "islam",
	"Christian": "christ",
	"Judaism": "judaism",
	"Hinduism": "hinduism",
	"Buddhism": "buddhism",
	"Carpentry": "carpentry",
	"Masonry": "masonry",
}
registerByDesc = {
	"Official": "official", # used in official communication
	"Formal": "formal", # same as official, maybe a bit less, suggested by TEI 12.3.5.2
	"Children Speech": "chil", # used to communicate with small children and by them
	"Colloquial": "col", # used in informal context, like at home
	"Slang": "slang", # used by certain groups of society only, suggested by TEI 12.3.5.2
	"Vulgar": "vulg", # used by uneducated people
	"Taboo": "taboo", # should not be used?, suggested by TEI 12.3.5.2
	"Ironic": "ironic", # used mainly in ironic remarks? suggested by TEI 12.3.5.2
	"Facetious": "facetious", # used mainly in funny context eg. jokes? suggested by TEI 12.3.5.2

	# the rest are added by Saeed Rasooli
	"Old": "old",
}

fa2en = {
	"کشاورزی": "Agriculture",
	"نجوم": "Astronomy",
	"انومبیل": "Automobile",
	"زیست‌شناسی": "Biology",
	"درخت آرایی": "Botany",
	"شیمی": "Chemistry",
	"برق‌افزارگان‌شناسی": "Electrotechnics",
	"برق": "Electrotechnics",
	"الکترونیک": "Electrotechnics",
	"امور مالی": "Finance",
	"جغرافی": "Geography",
	"زمین‌شناسی": "Geology",
	"دستور زبان": "Grammar",
	"تاریخ": "History",
	"فناوری اطلاعات": "Information Technology",
	"قانون": "Law",
	"حقوق": "Law",
	"ریاضیات": "Mathematics",
	"پزشکی": "Medicine",
	"نظامی": "Military",
	"ارتش": "Military",
	"موسیقی": "Music",
	"اسطوره‌شناسی": "Mythology",
	"اساطیر": "Mythology",
	"اسطوره": "Mythology",
	"اسطورهٔ": "Mythology",
	"افسانهٔ": "Mythology",
	"اسطوره‌های": "Mythology",
	"فیزیک": "Physics",
	"سیاست": "Politics",
	"دین": "Religion",
	"مذهب": "Religion",
	"جنسی": "Sexual",
	"ورزش": "Sport",
	"فناوری": "Technology",
	"رسمی/دفتری": "Official",
	"رسمی/جدی": "Formal",
	"زبان کودکان": "Children Speech",
	"عامیانه": "Colloquial",
	"خودمانی": "Slang",
	"ناپسند": "Vulgar",
	"بی‌ادبانه": "Vulgar",
	"تابو": "Taboo",
	"طعنه‌آمیز": "Ironic",
	"شوخ‌طبعانه": "Facetious",

	"جانور‌شناسی": "Zoology",
	"جانورشناسی": "Zoology",

	"آموزش": "Education"
	"ادبی": "Literary",
	"اسکی": "Ski",
	"اقتصاد": "Economy"
	"دانشگاهی": "Academic",
	"دانشگاه": "Academic",
	"بازرگانی": "Business",
	"مکانیک": "Mechanics",
	"هندسه": "Geometry",

	"اسلام": "Islam",
	"اسلامی": "Islam",
	"مسیحیت": "Christian",
	"مسیحی": "Christian",
	"انجیلی": "Christian",
	"انجیل": "Christian",
	"یهودیت": "Judaism",
	"هندو": "Hinduism",
	"هندوها": "Hinduism",
	"بودا": "Buddhism",
	"بودایی": "Buddhism",

	"نجاری": "Carpentry",
	"بنایی": "Masonry",


	"قدیمی": "Old",

}





