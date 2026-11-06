# en-fa.xdxf TEI vs XDXF comparison (sense by sense)

Direction: `en`. Each entry shows the source TEI from `aryanpour.parts/` and the converted XDXF article from `en-fa.xdxf`, split so that each TEI `<sense>` is paired with its XDXF `<def>`.

## 1. a

TEI source: `02-a.xml` entry 0 (score 47, rare 1)  
XDXF article: `en-fa.xdxf` # 1 (key `a`, 2 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>a</orth>
  <pron>ə</pron>
</form>
```

XDXF:

```xml
<k>a</k>
<tr>ə</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="adjective">صفت</pos>
    <pos norm="indefinite article">indefinite article</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <note>(پیش از واژه‌هایی که با حرف صدادار آغاز می‌شوند تبدیل به an می‌شود)</note>
    <cit type="trans">
      <quote>یک، یک عدد، – ی (یای نکره یا وحدت)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I see a man</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مردی را می‌بینم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">once a day</quote>
      <cit type="trans" xml:lang="fa">
        <quote>روزی یکبار</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a Mr. Smith called you yesterday</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مردی به نام آقای اسمیت دیروز به شما تلفن زد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">an apple</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یک سیب</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a city</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یک شهر</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a hundred and fifty thousand</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یکصد و پنجاه هزار</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>هر، هر یک</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* a few</quote>
      <cit type="trans" xml:lang="fa">
        <quote>معدودی، چندتا، چند عدد</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* a good (or great) many</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بسیار، خیلی، زیاد</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a good many of them were sick</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تعداد کثیری از آنها بیمار بودند.</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>صفت</pos>
  <pos>indefinite article</pos>
  <def xml:lang="fa">
    <c c="gray">(پیش از واژه‌هایی که با حرف صدادار آغاز می‌شوند تبدیل به an می‌شود)</c>
    <dtrn>یک، یک عدد، – ی (یای نکره یا وحدت)</dtrn>
    <ex>
      <ex_orig xml:lang="en">I see a man</ex_orig>
      <ex_tran xml:lang="fa">مردی را می‌بینم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">once a day</ex_orig>
      <ex_tran xml:lang="fa">روزی یکبار</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a Mr. Smith called you yesterday</ex_orig>
      <ex_tran xml:lang="fa">مردی به نام آقای اسمیت دیروز به شما تلفن زد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">an apple</ex_orig>
      <ex_tran xml:lang="fa">یک سیب</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a city</ex_orig>
      <ex_tran xml:lang="fa">یک شهر</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a hundred and fifty thousand</ex_orig>
      <ex_tran xml:lang="fa">یکصد و پنجاه هزار</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>هر، هر یک</dtrn>
    <ex>
      <ex_orig xml:lang="en">* a few</ex_orig>
      <ex_tran xml:lang="fa">معدودی، چندتا، چند عدد</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* a good (or great) many</ex_orig>
      <ex_tran xml:lang="fa">بسیار، خیلی، زیاد</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a good many of them were sick</ex_orig>
      <ex_tran xml:lang="fa">تعداد کثیری از آنها بیمار بودند.</ex_tran>
    </ex>
  </def>
</def>
```

### Sense 2 (n=2)

TEI:

```xml
<sense n="2" xml:lang="fa">
  <gramGrp>
    <pos norm="prefix">پیشوند</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>در، به، درون</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>در حال، مشغول</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>بدون، فاقد، ابی -، بی -، نا [amoral]</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="2" xml:lang="fa">
  <pos>پیشوند</pos>
  <def xml:lang="fa">
    <dtrn>در، به، درون</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>در حال، مشغول</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>بدون، فاقد، ابی -، بی -، نا [amoral]</dtrn>
  </def>
</def>
```

## 2. AAU

TEI source: `02-a.xml` entry 15 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 2 (key `AAU`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>AAU</orth>
</form>
```

XDXF:

```xml
<k>AAU</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>اتحادیهٔ ورزشکاران آماتور</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>اتحادیهٔ ورزشکاران آماتور</dtrn>
  </def>
</def>
```

## 3. ablative absolute

TEI source: `02-a.xml` entry 91 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 3 (key `ablative absolute`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>ablative absolute</orth>
</form>
```

XDXF:

```xml
<k>ablative absolute</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="gram">دستور زبان</usg>
    <cit type="trans">
      <quote>مفعول به مطلق، ازی مطلق</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="gram">دستور زبان</categ>
    <dtrn>مفعول به مطلق، ازی مطلق</dtrn>
  </def>
</def>
```

## 4. Acta Sanctorum

TEI source: `02-a.xml` entry 586 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 4 (key `Acta Sanctorum`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Acta Sanctorum</orth>
  <pron>äk´tä säŋk tō´room</pron>
</form>
```

XDXF:

```xml
<k>Acta Sanctorum</k>
<tr>äk´tä säŋk tō´room</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="lang">لاتین</usg>
    <cit type="trans">
      <quote>مجموعهٔ زندگینامه‌های مقدسین و شهدای کلیسای کاتولیک</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="lang">لاتین</categ>
    <dtrn>مجموعهٔ زندگینامه‌های مقدسین و شهدای کلیسای کاتولیک</dtrn>
  </def>
</def>
```

## 5. Aegospotami

TEI source: `02-a.xml` entry 955 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 5 (key `Aegospotami`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Aegospotami</orth>
  <pron>ē´gäs´pät´ə mī´</pron>
</form>
```

XDXF:

```xml
<k>Aegospotami</k>
<tr>ē´gäs´pät´ə mī´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="geo">یونان کهن</usg>
    <cit type="trans">
      <quote>رود ایجوس (ایجوس پوتامی)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="geo">یونان کهن</categ>
    <dtrn>رود ایجوس (ایجوس پوتامی)</dtrn>
  </def>
</def>
```

## 6. AIDS-related complex

TEI source: `02-a.xml` entry 1355 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 6 (key `AIDS-related complex`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>AIDS-related complex</orth>
</form>
```

XDXF:

```xml
<k>AIDS-related complex</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="dom">پزشکی</usg>
    <cit type="trans">
      <quote>بیماری وابسته به ایدز که نشانهٔ آن بزرگ شدن غدد لنفاوی است و می‌تواند تبدیل به ایدز شود</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="dom">پزشکی</categ>
    <dtrn>بیماری وابسته به ایدز که نشانهٔ آن بزرگ شدن غدد لنفاوی است و می‌تواند تبدیل به ایدز شود</dtrn>
  </def>
</def>
```

## 7. A level

TEI source: `02-a.xml` entry 1654 (score 7, rare 0)  
XDXF article: `en-fa.xdxf` # 7 (key `A level`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>A level</orth>
</form>
```

XDXF:

```xml
<k>A level</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(انگلیس) مرحلهٔ دوم و پیشرفته‌تر امتحانات دورهٔ متوسطه (که معمولا دو سال بعد از امتحان اول انجام می‌شود) (رجوع شود به: <ref>O level</ref>)، قبولی در این امتحانات (A-level هم می‌نویسند)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(انگلیس) مرحلهٔ دوم و پیشرفته‌تر امتحانات دورهٔ متوسطه (که معمولا دو سال بعد از امتحان اول انجام می‌شود) (رجوع شود به: <kref>O level</kref>)، قبولی در این امتحانات (A-level هم می‌نویسند)</dtrn>
  </def>
</def>
```

## 8. Alkoran

TEI source: `02-a.xml` entry 1775 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 8 (key `Alkoran`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Alkoran</orth>
  <pron>al´kō rän´</pron>
</form>
```

XDXF:

```xml
<k>Alkoran</k>
<tr>al´kō rän´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="time">قدیمی</usg>
    <cit type="trans">
      <quote>قرآن</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="time">قدیمی</categ>
    <dtrn>قرآن</dtrn>
  </def>
</def>
```

## 9. Baalbek

TEI source: `03-b.xml` entry 10 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 9 (key `Baalbek`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Baalbek</orth>
  <pron>bäl´bek´</pron>
</form>
```

XDXF:

```xml
<k>Baalbek</k>
<tr>bäl´bek´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شهر بعلبک در لبنان (محل ویرانه‌های یک شهر باستانی رومی)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>شهر بعلبک در لبنان (محل ویرانه‌های یک شهر باستانی رومی)</dtrn>
  </def>
</def>
```

## 10. Big Daddy

TEI source: `03-b.xml` entry 1780 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 10 (key `Big Daddy`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Big Daddy</orth>
</form>
```

XDXF:

```xml
<k>Big Daddy</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="reg">عامیانه</usg>
    <cit type="trans">
      <quote>شخص یا چیز نیرومند و غنی (و اغلب سلطه‌گرای)، آقابالاسر</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="reg">عامیانه</categ>
    <dtrn>شخص یا چیز نیرومند و غنی (و اغلب سلطه‌گرای)، آقابالاسر</dtrn>
  </def>
</def>
```

## 11. CAB

TEI source: `04-c.xml` entry 9 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 11 (key `CAB`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>CAB</orth>
</form>
```

XDXF:

```xml
<k>CAB</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>مخفف : (آمریکا) ادارهٔ هواپیمایی کشوری</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>مخفف : (آمریکا) ادارهٔ هواپیمایی کشوری</dtrn>
  </def>
</def>
```

## 12. Caledonia

TEI source: `04-c.xml` entry 253 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 12 (key `Caledonia`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Caledonia</orth>
  <pron>kal´ə dōn´yə</pron>
  <pron>-dō´nē ə</pron>
</form>
```

XDXF:

```xml
<k>Caledonia</k>
<tr>kal´ə dōn´yə</tr>
<tr>-dō´nē ə</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="style">شاعرانه</usg>
    <cit type="trans">
      <quote>اسکاتلند</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="style">شاعرانه</categ>
    <dtrn>اسکاتلند</dtrn>
  </def>
</def>
```

## 13. coed

TEI source: `04-c.xml` entry 3637 (score 19, rare 1)  
XDXF article: `en-fa.xdxf` # 13 (key `coed`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>coed</orth>
  <pron>kō´ed´</pron>
</form>
<form>
  <orth>co-ed</orth>
</form>
```

XDXF:

```xml
<k>coed</k>
<k>co-ed</k>
<tr>kō´ed´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <pos norm="adjective">صفت</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>وابسته به آموزش توام پسران و دختران، مختلط، هم‌آموزی<br />رجوع شود به: coeducational</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a coed school</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مدرسهٔ مختلط</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote />
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(دانشجو) دختر، دانشجوی زن، هم‌آموز</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">two of the coeds were from Egypt</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دوتا از دانشجویان دختر اهل مصر بودند.</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <pos>صفت</pos>
  <def xml:lang="fa">
    <dtrn>وابسته به آموزش توام پسران و دختران، مختلط، هم‌آموزی<br />رجوع شود به: coeducational</dtrn>
    <ex>
      <ex_orig xml:lang="en">a coed school</ex_orig>
      <ex_tran xml:lang="fa">مدرسهٔ مختلط</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn />
  </def>
  <def xml:lang="fa">
    <dtrn>(دانشجو) دختر، دانشجوی زن، هم‌آموز</dtrn>
    <ex>
      <ex_orig xml:lang="en">two of the coeds were from Egypt</ex_orig>
      <ex_tran xml:lang="fa">دوتا از دانشجویان دختر اهل مصر بودند.</ex_tran>
    </ex>
  </def>
</def>
```

## 14. comatulid

TEI source: `04-c.xml` entry 3978 (score 13, rare 1)  
XDXF article: `en-fa.xdxf` # 14 (key `comatulid`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>comatulid</orth>
  <pron>kō mach´ōō lid´</pron>
</form>
<form>
  <orth>feather star</orth>
</form>
<form>
  <orth>comatula</orth>
</form>
<form>
  <orth>comatulida</orth>
</form>
```

XDXF:

```xml
<k>comatulid</k>
<k>feather star</k>
<k>comatula</k>
<k>comatulida</k>
<tr>kō mach´ōō lid´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>لاله‌وشان، نام یک راسته از رده زنبق دریایی است.<br />نام علمی: Comatulida</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <def xml:lang="fa">
    <dtrn>لاله‌وشان، نام یک راسته از رده زنبق دریایی است.<br />نام علمی: Comatulida</dtrn>
  </def>
</def>
```

## 15. concrete music

TEI source: `04-c.xml` entry 4432 (score 10, rare 1)  
XDXF article: `en-fa.xdxf` # 15 (key `concrete music`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>concrete music</orth>
</form>
<form>
  <orth>musique concrète</orth>
</form>
<form>
  <orth>musique concrete</orth>
</form>
```

XDXF:

```xml
<k>concrete music</k>
<k>musique concrète</k>
<k>musique concrete</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>موسیقی کانکریت، سبکی از موسیقی است که مشتق شده از صداهای ضبط شده‌است.<br />امروزه این نام اشاره به گونه‌ای از موسیقی الکتروآکوستیک دارد که بخش‌های مختلف آن از صداهای آکوسماتیک ساخته شده‌است.</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>موسیقی کانکریت، سبکی از موسیقی است که مشتق شده از صداهای ضبط شده‌است.<br />امروزه این نام اشاره به گونه‌ای از موسیقی الکتروآکوستیک دارد که بخش‌های مختلف آن از صداهای آکوسماتیک ساخته شده‌است.</dtrn>
  </def>
</def>
```

## 16. dab hand

TEI source: `05-d.xml` entry 14 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 16 (key `dab hand`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>dab hand</orth>
</form>
```

XDXF:

```xml
<k>dab hand</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(انگلیس – عامیانه) ماهر، دارای ید طولی (در کاری)، صد مرده حلاج</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(انگلیس – عامیانه) ماهر، دارای ید طولی (در کاری)، صد مرده حلاج</dtrn>
  </def>
</def>
```

## 17. depository

TEI source: `05-d.xml` entry 1143 (score 11, rare 1)  
XDXF article: `en-fa.xdxf` # 17 (key `depository`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>depository</orth>
  <pron>dē päz´ə tôr´ē</pron>
  <pron>di-</pron>
</form>
```

XDXF:

```xml
<k>depository</k>
<tr>dē päz´ə tôr´ē</tr>
<tr>di-</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <number norm="plural">جمع</number>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>انبار (که در آن اشیا را به امانت می‌سپارند)، سپارشگاه، ودیعه‌گاه، گروگاه</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>حالت دیگری از <ref>depositary</ref>
        <br />گنجور، امین، ودیعه نگهدار، سپارش‌دار</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <gr>جمع</gr>
  <def xml:lang="fa">
    <dtrn>انبار (که در آن اشیا را به امانت می‌سپارند)، سپارشگاه، ودیعه‌گاه، گروگاه</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>حالت دیگری از <kref>depositary</kref>
      <br />گنجور، امین، ودیعه نگهدار، سپارش‌دار</dtrn>
  </def>
</def>
```

## 18. Dutch East Indies

TEI source: `05-d.xml` entry 3659 (score 18, rare 1)  
XDXF article: `en-fa.xdxf` # 18 (key `Dutch East Indies`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Dutch East Indies</orth>
</form>
<form xml:lang="en">
  <orth>Netherlands East Indies</orth>
</form>
<form xml:lang="en">
  <orth>Netherlands Indies</orth>
</form>
<form xml:lang="en">
  <orth>Netherlands East-Indies</orth>
</form>
```

XDXF:

```xml
<k>Dutch East Indies</k>
<k>Netherlands East Indies</k>
<k>Netherlands Indies</k>
<k>Netherlands East-Indies</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>هند شرقی هلند</quote>
    </cit>
    <def>هند شرقی هلند، بخشی از مستعمرات هلند بود که پس از جنگ جهانی دوم به استقلال رسید و به اندونزی مدرن کنونی تبدیل شد.</def>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>هند شرقی هلند</dtrn>
    <dtrn>هند شرقی هلند، بخشی از مستعمرات هلند بود که پس از جنگ جهانی دوم به استقلال رسید و به اندونزی مدرن کنونی تبدیل شد.</dtrn>
  </def>
</def>
```

## 19. e-

TEI source: `06-e.xml` entry 2 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 19 (key `e-`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>e-</orth>
</form>
```

XDXF:

```xml
<k>e-</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پیشوند برابر با: ex- (پیش از حروف b و d و g و j و l و m و n و r و v به کار می‌رود) [eject]</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>پیشوند برابر با: ex- (پیش از حروف b و d و g و j و l و m و n و r و v به کار می‌رود) [eject]</dtrn>
  </def>
</def>
```

## 20. Englander

TEI source: `06-e.xml` entry 1189 (score 9, rare 0)  
XDXF article: `en-fa.xdxf` # 20 (key `Englander`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Englander</orth>
  <pron>-ər</pron>
</form>
```

XDXF:

```xml
<k>Englander</k>
<tr>-ər</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <usg type="plev">نادر</usg>
    <cit type="trans">
      <quote>انگلیسی، بومی انگلیس</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <def xml:lang="fa">
    <categ type="plev">نادر</categ>
    <dtrn>انگلیسی، بومی انگلیس</dtrn>
  </def>
</def>
```

## 21. furmenty

TEI source: `07-f.xml` entry 2942 (score 4, rare 0)  
XDXF article: `en-fa.xdxf` # 21 (key `furmenty`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>furmenty</orth>
  <pron>fu_r´mən tē</pron>
</form>
```

XDXF:

```xml
<k>furmenty</k>
<tr>fu_r´mən tē</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
</def>
```

## 22. Gable

TEI source: `08-g.xml` entry 17 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 22 (key `Gable`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Gable</orth>
  <pron>gā´bəl</pron>
</form>
```

XDXF:

```xml
<k>Gable</k>
<tr>gā´bəl</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>کلارک گیبل (هنرپیشهٔ آمریکایی سینما)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>کلارک گیبل (هنرپیشهٔ آمریکایی سینما)</dtrn>
  </def>
</def>
```

## 23. Galla

TEI source: `08-g.xml` entry 129 (score 19, rare 1)  
XDXF article: `en-fa.xdxf` # 23 (key `Galla`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Galla</orth>
  <pron>gal´ə</pron>
</form>
```

XDXF:

```xml
<k>Galla</k>
<tr>gal´ə</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <pos norm="adjective">صفت</pos>
    <number norm="plural">جمع</number>
  </gramGrp>
  <sense xml:lang="fa">
    <def>واژهٔ قدیمی و زننده برای زبان اورومو یا مردم اورومو</def>
    <xr>رجوع شود به: <ref target="https://en.wikipedia.org/wiki/Oromo_language">Oromo language</ref> و <ref target="https://en.wikipedia.org/wiki/Oromo_people">Oromo people</ref>
    </xr>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <pos>صفت</pos>
  <gr>جمع</gr>
  <def xml:lang="fa">
    <dtrn>واژهٔ قدیمی و زننده برای زبان اورومو یا مردم اورومو</dtrn>
    <dtrn>رجوع شود به: <iref href="https://en.wikipedia.org/wiki/Oromo_language">Oromo language</iref> و <iref href="https://en.wikipedia.org/wiki/Oromo_people">Oromo people</iref>
    </dtrn>
  </def>
</def>
```

## 24. gradation

TEI source: `08-g.xml` entry 1745 (score 36, rare 1)  
XDXF article: `en-fa.xdxf` # 24 (key `gradation`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>gradation</orth>
  <pron>grā dā´shən</pron>
  <pron>grə-</pron>
</form>
```

XDXF:

```xml
<k>gradation</k>
<tr>grā dā´shən</tr>
<tr>grə-</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>درجه بندی، مدرج سازی، طبقه بندی، پایه، رتبه، پله‌پله سازی، زینه بندی، درجه، زینه</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the many gradations between absolute good and bad</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مدارج مختلف بین خوبی و بدی مطلق</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دگرگونی تدریجی، (رفتن تدریجی) از مرحله‌ای به مرحله دیگر</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to go from a lower to a higher gradation</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از مرحلهٔ پایین‌تر به مرحلهٔ بالاتری رسیدن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تبدیل تدریجی از یک رنگ به رنگ دیگر، حد فاصل دو رنگ</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <usg type="dom">زمین‌شناسی</usg>
    <cit type="trans">
      <quote>مسطح شدگی (در اثر فرسایش بلندی‌ها و رسوب در گودی‌ها)، همواری، ترازسازی</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <xr>(زبان‌شناسی) رجوع شود به: <ref>ablaut</ref>
    </xr>
    <note>(vowel gradation هم می‌گویند)</note>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <def xml:lang="fa">
    <dtrn>درجه بندی، مدرج سازی، طبقه بندی، پایه، رتبه، پله‌پله سازی، زینه بندی، درجه، زینه</dtrn>
    <ex>
      <ex_orig xml:lang="en">the many gradations between absolute good and bad</ex_orig>
      <ex_tran xml:lang="fa">مدارج مختلف بین خوبی و بدی مطلق</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>دگرگونی تدریجی، (رفتن تدریجی) از مرحله‌ای به مرحله دیگر</dtrn>
    <ex>
      <ex_orig xml:lang="en">to go from a lower to a higher gradation</ex_orig>
      <ex_tran xml:lang="fa">از مرحلهٔ پایین‌تر به مرحلهٔ بالاتری رسیدن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>تبدیل تدریجی از یک رنگ به رنگ دیگر، حد فاصل دو رنگ</dtrn>
  </def>
  <def xml:lang="fa">
    <categ type="dom">زمین‌شناسی</categ>
    <dtrn>مسطح شدگی (در اثر فرسایش بلندی‌ها و رسوب در گودی‌ها)، همواری، ترازسازی</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>(زبان‌شناسی) رجوع شود به: <kref>ablaut</kref>
    </dtrn>
    <c c="gray">(vowel gradation هم می‌گویند)</c>
  </def>
</def>
```

## 25. Haakon VII

TEI source: `09-h.xml` entry 5 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 25 (key `Haakon VII`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Haakon VII</orth>
  <pron>hô´koon</pron>
</form>
```

XDXF:

```xml
<k>Haakon VII</k>
<tr>hô´koon</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>هاکون (پادشاه کشور نروژ)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>هاکون (پادشاه کشور نروژ)</dtrn>
  </def>
</def>
```

## 26. Iago

TEI source: `10-i.xml` entry 8 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 26 (key `Iago`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Iago</orth>
  <pron>ē ä´gō</pron>
</form>
```

XDXF:

```xml
<k>Iago</k>
<tr>ē ä´gō</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>ایاگو (نام مردی بد طینت در نمایشنامهٔ ((اتللو)) از شکسپیر)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>ایاگو (نام مردی بد طینت در نمایشنامهٔ ((اتللو)) از شکسپیر)</dtrn>
  </def>
</def>
```

## 27. Jabalpur

TEI source: `11-j.xml` entry 7 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 27 (key `Jabalpur`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Jabalpur</orth>
  <pron>jub´əl poor´</pron>
</form>
```

XDXF:

```xml
<k>Jabalpur</k>
<tr>jub´əl poor´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شهر جبل پور (در ناحیهٔ مرکزی هندوستان)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>شهر جبل پور (در ناحیهٔ مرکزی هندوستان)</dtrn>
  </def>
</def>
```

## 28. jellaba

TEI source: `11-j.xml` entry 267 (score 19, rare 1)  
XDXF article: `en-fa.xdxf` # 28 (key `jellaba`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>jellaba</orth>
  <pron>jə lä´bä</pron>
</form>
<form xml:lang="en">
  <orth>jillaba</orth>
</form>
<form xml:lang="en">
  <orth>djellaba</orth>
</form>
<form xml:lang="en">
  <orth>galabia</orth>
  <pron>gal´ə bē´ə</pron>
</form>
```

XDXF:

```xml
<k>jellaba</k>
<k>jillaba</k>
<k>djellaba</k>
<k>galabia</k>
<tr>jə lä´bä</tr>
<tr>gal´ə bē´ə</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جیلابا</quote>
    </cit>
    <def>روپوش تک‌جنسیتی، بلند، گشاد و آستین‌بلند است که در منطقه مغرب در آفریقای شمالی پوشیده می شود.</def>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <def xml:lang="fa">
    <dtrn>جیلابا</dtrn>
    <dtrn>روپوش تک‌جنسیتی، بلند، گشاد و آستین‌بلند است که در منطقه مغرب در آفریقای شمالی پوشیده می شود.</dtrn>
  </def>
</def>
```

## 29. Kaaba

TEI source: `12-k.xml` entry 6 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 29 (key `Kaaba`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Kaaba</orth>
  <pron>kä´bə</pron>
  <pron>kä´ə bə</pron>
</form>
```

XDXF:

```xml
<k>Kaaba</k>
<tr>kä´bə</tr>
<tr>kä´ə bə</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(عربی) کعبه</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(عربی) کعبه</dtrn>
  </def>
</def>
```

## 30. Labanotation

TEI source: `13-l.xml` entry 13 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 30 (key `Labanotation`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Labanotation</orth>
</form>
```

XDXF:

```xml
<k>Labanotation</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به‌ویژه در باله: روش نگارش حرکات رقصگران به کمک علامات و غیره) رقص‌نگاری، رامش‌نگاری</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(به‌ویژه در باله: روش نگارش حرکات رقصگران به کمک علامات و غیره) رقص‌نگاری، رامش‌نگاری</dtrn>
  </def>
</def>
```

## 31. M'

TEI source: `14-m.xml` entry 4 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 31 (key `M'`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>M'</orth>
</form>
```

XDXF:

```xml
<k>M'</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>برابر است با: M'Donald) Mac-)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>برابر است با: M'Donald) Mac-)</dtrn>
  </def>
</def>
```

## 32. Nablus

TEI source: `15-n.xml` entry 13 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 32 (key `Nablus`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Nablus</orth>
  <pron>nab´ləs</pron>
  <pron>näb´-</pron>
</form>
```

XDXF:

```xml
<k>Nablus</k>
<tr>nab´ləs</tr>
<tr>näb´-</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شهر نابلس (در غرب کشور اردن)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>شهر نابلس (در غرب کشور اردن)</dtrn>
  </def>
</def>
```

## 33. newspaperwoman

TEI source: `15-n.xml` entry 687 (score 13, rare 0)  
XDXF article: `en-fa.xdxf` # 33 (key `newspaperwoman`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>newspaperwoman</orth>
  <pron>-woom´ən</pron>
</form>
```

XDXF:

```xml
<k>newspaperwoman</k>
<tr>-woom´ən</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <gen norm="feminine">مونث</gen>
    <number norm="plural">جمع</number>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(زن)</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>روزنامه نویس، گزارشگر، خبرنگار، نودادنگار</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>صاحب روزنامه، روزنامه دار، صاحب امتیاز روزنامه</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <gr>مونث</gr>
  <gr>جمع</gr>
  <def xml:lang="fa">
    <dtrn>(زن)</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>روزنامه نویس، گزارشگر، خبرنگار، نودادنگار</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>صاحب روزنامه، روزنامه دار، صاحب امتیاز روزنامه</dtrn>
  </def>
</def>
```

## 34. Oahu

TEI source: `16-o.xml` entry 7 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 34 (key `Oahu`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Oahu</orth>
  <pron>ō ä´hōō</pron>
</form>
```

XDXF:

```xml
<k>Oahu</k>
<tr>ō ä´hōō</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جزیرهٔ اواهو (در آبخست گروه هاوایی – پایتخت: 1526 Honolulu کیلومتر مربع)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>جزیرهٔ اواهو (در آبخست گروه هاوایی – پایتخت: 1526 Honolulu کیلومتر مربع)</dtrn>
  </def>
</def>
```

## 35. old hand

TEI source: `16-o.xml` entry 458 (score 8, rare 0)  
XDXF article: `en-fa.xdxf` # 35 (key `old hand`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>old hand</orth>
</form>
```

XDXF:

```xml
<k>old hand</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <usg type="hint">آدم</usg>
    <cit type="trans">
      <quote>کار کشته، کهنه کار، ماهر، پر تجربه</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <categ type="hint">آدم</categ>
    <dtrn>کار کشته، کهنه کار، ماهر، پر تجربه</dtrn>
  </def>
</def>
```

## 36. Pacific

TEI source: `17-p.xml` entry 23 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 36 (key `Pacific`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Pacific</orth>
  <pron>pə sif´ik</pron>
</form>
```

XDXF:

```xml
<k>Pacific</k>
<tr>pə sif´ik</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>اقیانوس آرام (نام کامل: the Pacific Ocean)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>اقیانوس آرام (نام کامل: the Pacific Ocean)</dtrn>
  </def>
</def>
```

## 37. Qatar

TEI source: `18-q.xml` entry 6 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 37 (key `Qatar`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Qatar</orth>
  <pron>ke tär´</pron>
  <pron>kä´tär´</pron>
</form>
```

XDXF:

```xml
<k>Qatar</k>
<tr>ke tär´</tr>
<tr>kä´tär´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>کشور قطر (در خلیج فارس – پایتخت: دوحه 15540 – Doha کیلومتر مربع)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>کشور قطر (در خلیج فارس – پایتخت: دوحه 15540 – Doha کیلومتر مربع)</dtrn>
  </def>
</def>
```

## 38. Ra

TEI source: `19-r.xml` entry 2 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 38 (key `Ra`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Ra</orth>
  <pron>rä</pron>
</form>
```

XDXF:

```xml
<k>Ra</k>
<tr>rä</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(اسطورهٔ مصر) رآ (خدای خورشید)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(اسطورهٔ مصر) رآ (خدای خورشید)</dtrn>
  </def>
</def>
```

## 39. run

TEI source: `19-r.xml` entry 2903 (score 397, rare 0)  
XDXF article: `en-fa.xdxf` # 39 (key `run`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>run</orth>
  <pron>run</pron>
</form>
```

XDXF:

```xml
<k>run</k>
<tr>run</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <pos norm="adjective">صفت</pos>
    <pos norm="transitive verb">فعل متعدی</pos>
    <pos norm="intransitive verb">فعل لازم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دویدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the child ran to her mother</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کودک به سوی مادرش دوید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I ran and I ran; to a mountain top I came ...</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دویدم و دویدم سرکوهی رسیدم ....</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a running race</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مسابقه دو</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>به سرعت حرکت کردن، تند رفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a ship running before the wind</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یک کشتی که در جلو باد به تندی حرکت می‌کند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(معمولا با: to) مراجعه کردن(به)، (پیش کسی یا چیزی) رفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she is always running to the police</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او مرتبا به پلیس مراجعه می‌کند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">as soon as anything happens he runs to his mother's lap</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تا چیزی می‌شود به دامن مادرش پناه می‌برد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(معمولا با: with) معاشر بودن (با)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he runs around with a bunch of hoodlums</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او با یک دسته اراذل و اوباش دوستی می‌کند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(آزادانه) آمدن، رفتن، رستن، جنبیدن، گشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">deer used to run free in these woods</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در این بیشه‌ها آهوان آزادانه می‌گشتند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>فرار کردن، به چاک زدن، ورمالیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">our dog ran away</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سگ ما فرار کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(با: up to یا down to یا over to و غیره) سفر تند و کوتاه کردن، زود رفتن و آمدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">run over to the store and get me some sugar</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تند برو به مغازه و برایم قدری شکر بگیر.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در مسابقه یا انتخابات و غیره) شرکت کردن، نامزد (انتخابات و غیره) بودن یا کردن، شرکت دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he is going to run as an independent candidate</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او به عنوان نامزد مستقل (در انتخابات) شرکت خواهد کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run a race</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در مسابقه شرکت کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در مسابقات – اول یا دوم و غیره) شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run last</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آخر شدن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(ماهی – در جهت معینی) شنا کردن، مهاجرت کردن، مهاجرت، کوچ</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">salmons run upstream for spawning</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ماهی آزاد برای تخم‌گذاری به بالای رودخانه شنا می‌کند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(طبق برنامه مرتبا) رفت و آمد کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a bus that runs between Tehran and Tabriz</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اتوبوسی که میان تهران و تبریز رفت و آمد می‌کند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به سرعت از روی چیزی) رد شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his eyes ran over the page</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به سرعت صفحه را از مد نظر گذراند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شایع بودن، زبانزد بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a rumor running through the town</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شایعه‌ای که در شهر زبانزد شده است</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>بالا رفتن، خزیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a vine running over the wall</quote>
      <cit type="trans" xml:lang="fa">
        <quote>درخت مو که از دیوار بالا می‌رود</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(دائما) کار کردن یا جنبیدن، بند نیامدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his tongue ran on and on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زبانش بند آمدنی نبود.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(اداره یا موتور و غیره) کار کردن، به کار افتادن یا انداختن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I don't know how to run this motor</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نمی‌دانم این موتور را چگونه به کار بیاندازم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a machine that is running</quote>
      <cit type="trans" xml:lang="fa">
        <quote>موتوری که دارد کار می‌کند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به فکر) خطور کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the memory of that accident keeps running through my mind</quote>
      <cit type="trans" xml:lang="fa">
        <quote>خاطرهٔ آن حادثه مرتبا در فکرم خطور می‌کند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>روان بودن، جریان داشتن، جاری کردن یا بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">running water</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آب روان</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">at the foot of the hill, the river runs more slowly</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در پای تپه (جریان) رودخانه آهسته‌تر می‌شود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">let the water run through the pipe</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بگذار آب در لوله جاری شود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">gutters running blood</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جوی‌هایی که خون در آن جاری است</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>آب شدن و جاری شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the vax ran</quote>
      <cit type="trans" xml:lang="fa">
        <quote>موم آب شد و جاری شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the butter was beginning to run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کره داشت آب می‌شد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(پارچه) رنگ پس دادن، (رنگ) دواندن، سرایت کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">colors guaranteed not to run or fade</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رنگ‌هایی که تضمین شده است سرایت نمی‌کنند و نمی‌پرند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پر بودن، سرشار بودن، لبریز بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">her eyes were running with tears</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چشمانش از اشک لبریز بودند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>چکه کردن، (آب یا چرک و غیره) پس دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a running sore</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زخمی که از آن چرک یا خون می‌آید</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(زمان) کشیدن، گذشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the days ran into weeks</quote>
      <cit type="trans" xml:lang="fa">
        <quote>روزها به هفته‌ها کشید.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در روزنامه یا صحنهٔ تئاتر و غیره) ظاهر شدن، چاپ کردن، نمایش(دهی)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a film that had a long run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فیلمی که مدت زیادی نمایش داده می‌شد</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a play that ran for a full year</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نمایشی که یک سال تمام روی صحنه آورده می‌شد</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">several newspapers run his articles</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چندین روزنامه مقاله‌های او را چاپ می‌کنند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(قانون و غیره) اعتبار داشتن، به قوت قانونی باقی ماندن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a law running for 25 years</quote>
      <cit type="trans" xml:lang="fa">
        <quote>قانونی که 25 سال است به قوت خود باقیست</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به طور موروثی) وجود داشتن، فراوان بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">musical talent runs in this family</quote>
      <cit type="trans" xml:lang="fa">
        <quote>استعداد موسیقی در این خانواده فراوان است.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>گرایش داشتن، تمایل داشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">their taste runs more to exotic foods</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سلیقهٔ آنان به خوراک‌های عجیب و غریب گرایش بیشتری دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به صورت خط یا راه و غیره) ادامه داشتن، گذشتن، رد شدن، کشیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run lines on a sheet of paper</quote>
      <cit type="trans" xml:lang="fa">
        <quote>روی یک صفحه کاغذ خط کشیدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this railway runs through a forest</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این راه‌آهن از میان جنگل می‌گذرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a fence that runs through the middle of our land</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نرده‌ای که از میان زمین ما رد می‌شود</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(با: from و to) شامل بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his plays run from tragedies to comedies</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نمایشنامه‌های او شامل سوگمایش و شادمایش (تراژدی و کمدی) می‌شود.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به وضع خاصی) رسیدن، برخوردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run into trouble</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به اشکال برخوردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(کشتی یا اتومبیل و غیره) خوردن به</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the boat ran aground</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کشتی به گل نشست</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the car ran into a tree</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اتومبیل به درخت خورد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(خبر یا داستان و غیره) بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the story runs like this</quote>
      <cit type="trans" xml:lang="fa">
        <quote>داستان بدین قرار است</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(قیمت یا اندازه و غیره) بودن، داشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">boots that run $40</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پوتین‌هایی که 40 دلار قیمت دارند</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">apples running 7 to a kilo</quote>
      <cit type="trans" xml:lang="fa">
        <quote>هر 7 تا سیب یک کیلو وزن دارد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">prices are running high</quote>
      <cit type="trans" xml:lang="fa">
        <quote>قیمت‌ها بالا هستند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(قرض) بالا آوردن، (ریسک یا خطر) کردن، به خود هموار کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the free-spending man ran up a heavy debt</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مرد ولخرج قرض سنگینی به بار آورد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">if you go,you run the risk of being shot</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اگر بروی خطر تیر خوردن را به خود هموار می‌کنی.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(محاصره وغیره را) شکستن، عبور کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run a naval blockade</quote>
      <cit type="trans" xml:lang="fa">
        <quote>محاصرهٔ دریایی را شکستن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run a red light</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از چراغ قرمز عبور کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(موتور اتومبیل و غیره را) درجا به کار انداختن (to idle هم می‌گویند)، هرز کار کردن، خلاص کار کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">let the engine run for five minutes so that it warms up</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بگذار موتور (اتومبیل) پنج دقیقه در جا کار کند تا گرم شود.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(جوراب بلند زنانه) نخ‌کش، دررفتگی، نخ‌کش شدن، دررفتگی پیدا کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">these stockings run easily</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این جوراب‌ها زود نخ‌کش می‌شوند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">there is a big run in your stocking</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جورابت دررفتگی بزرگی دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(کشتی و اتوبوس و غیره) حمل کردن، بردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">our ships run passengers as well as cargo</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کشتی‌های ما هم مسافر و هم محموله می‌برند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>قاچاق کردن، قاچاق حمل کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run whiskey</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ویسکی قاچاق کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>چپاندن، با فشار وارد کردن یا عبور دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">run the rod in and out of the hole to make it bigger</quote>
      <cit type="trans" xml:lang="fa">
        <quote>میله را چند بار بکن توی سوراخ و در بیاور تا گشادتر شود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he run his sword through the middle of Goodarz' neck</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شمشیرش را از وسط گردن گودرز رد کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>اداره کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to run a household</quote>
      <cit type="trans" xml:lang="fa">
        <quote>خانواده‌ای را اداره کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">they ran the country on a tight budget</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آنها کشور را با بودجهٔ محدودی اداره کردند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(آزمایش و غیره) کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the doctors decided to run another test</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دکترها تصمیم گرفتند یک آزمایش دیگر هم بکنند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(تب) داشتن، کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she has been running a fever for three days</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سه روز است تب دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>عمل دویدن، دو، گام‌های تند</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>مسابقهٔ دو</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(اتوبوس و کشتی و غیره) یک رفت (یا یک برگشت)، سفر</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this train runs between Tehran and Ghom and each run takes two hours</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این ترن میان تهران و قم رفت و برگشت می‌کند و هر سفر دو ساعت طول می‌کشد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جریان، روانی</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the run of events</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جریان امور</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the run of the tide</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جریان کشند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رخ دادن پی‌درپی، سلسله، دوره</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a run of good luck</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چند بار شانس خوب</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به ویژه مشتریان) هجوم بردن (به)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">customers made a run on the banks</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مشتریان (برای مطالبهٔ پول خود) به بانک‌ها هجوم بردند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-50 (به شرطی که تند باشد) نهر، جوی، رودچه -51 مدت کار کردن موتور و غیره، بازده ماشین (در این مدت) -52 (کالا یا مردم و غیره) نوع معمولی، نوع</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">ordinary run of people</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مردم عادی</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-53 (اسکی) پیست</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a ski run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیست اسکی</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-54 (جانوران) مسیر، راه</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a buffalo run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مسیر گاوهای وحشی</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-55 آزادی رفت و آمد یا ورود و خروج یا استفاده</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">my brothers have the run of my house</quote>
      <cit type="trans" xml:lang="fa">
        <quote>برادران من می‌توانند هر وقت بخواهند به منزل من بیایند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-56 (بیس‌بال – یک امتیاز در اثر یک بار دور زمین گشتن) ران -57 (هواپیما – برای تیراندازی یا بمباران) شیرجه رفتن، از ارتفاع کاستن، به هدف نزدیک شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">despite enemy fire, we made three runs and left the target in flames</quote>
      <cit type="trans" xml:lang="fa">
        <quote>با وجود آتش دشمن سه بار شیرجه رفتیم و هدف را به حریق کشاندیم.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>-58 (کامپیوتر) رانش، اجرا، رانیدن، اجرا کردن (برنامه) -59 ذوب شده، آب شده -60 (فلز) قالب گیری شده، ریخته، ریخته‌گری شده، ریختن، ریخته‌گری</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">run metal</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فلز ریخته‌گری شده</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* a run for one's money</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- رقابت شدید 2- بهره وری (از سرمایه‌گذاری یا صرف وقت و غیره)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* in the long run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بالاخره، در دراز مدت، نتیجهٔ نهایی</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* in the short run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در آغاز، در ابتدا، در کوتاه مدت</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* on the run</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- درحال دویدن 2- در تکاپو، سخت مشغول 3- در حال فرار، درحال عقب نشینی</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run across</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(اتفاقا) برخوردن (به کسی یا چیزی)، ملاقات کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run after</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تعقیب کردن، دنبال کسی یا چیزی دویدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run along</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رفتن، عزیمت کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I must run along now</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اکنون باید بروم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run around with</quote>
      <cit type="trans" xml:lang="fa">
        <quote>با کسی دیگر رابطه داشتن یا معاشر بودن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">her husband was running around with another woman</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شوهرش با یک زن دیگر رابطه داشت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run away</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- فرار کردن، گریختن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the prisoner ran away</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زندانی فرار کرد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- ترک خانواده (یا وطن) کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run away with</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- رفتن و با خود بردن، دزدیدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he ran away with my purse</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کیف پولم را زد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- مهار نکردنی شدن، از کنترل خارج شدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">her enthusiasm ran away with her</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اشتیاق او لجام گسیخته شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run back</quote>
      <usg type="dom">فوتبال آمریکایی</usg>
      <cit type="trans" xml:lang="fa">
        <quote>با توپ به سوی دروازهٔ حریف دویدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run down</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (به خاطر کمبود سوخت یا برق و غیره) از کار ایستادن 2- (با ماشین و غیره به کسی یا چیزی) زدن و افکندن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the truck ran down two large trees</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کامیون دو درخت بزرگ را انداخت.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>3- تعقیب کردن و گرفتن (یا کشتن)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run for it</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(به منظور فرار یا احتراز) دویدن، دو زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run idle</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(موتور اتومبیل و غیره) خلاص کار کردن، هرزکارکردن، درجا کار کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run in</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (به عنوان چیز اضافی) افزودن، شامل کردن، گنجاندن 2- (عامیانه) توقف کوتاه کردن 3- (عامیانه) بازداشت کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run into</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (اتفاقا) برخوردن به، ملاقات کردن 2- تصادم کردن با، خوردن به، زدن به</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he again ran into the telephone pole with his car</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دوباره با ماشین زد به تیر تلفن.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>run to) -3 هم می‌گویند) بالغ شدن بر، رسیدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the two cars ran into each other</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دو اتومبیل با هم شاخ به شاخ شدند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">their debts run into several millions</quote>
      <cit type="trans" xml:lang="fa">
        <quote>قروض آنان به چندین میلیون می‌رسد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run off</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (متن را) تکثیر کردن، چاپ کردن، پلی‌کپی کردن، تایپ کردن 2- تاراندن، دور کردن 3- هرز رفتن 4- به خارج جاری شدن یا ریختن 5- فرار کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- ادامه دادن، ادامه یافتن 2- به آخر چیزی اضافه کردن 3- دائما حرف زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run out</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- منقضی شدن، به پایان رسیدن، تمام شدن، مصرف شدن 2- بیرون کردن، بیرون راندن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run out of</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(موجودی چیزی را) به اتمام رساندن، دیگر نداشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run out on</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>تنها گذاشتن و رفتن، قال گذاشتن، رها کردن، ترک کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run out the clock</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(فوتبال و بسکتبال و غیره – در اواخر مسابقه) توپ را کنترل کردن، وقت کشی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run over</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- لبریز شدن 2- (با اتومبیل و غیره) زیر گرفتن، زیر ماشین رفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Pooran was run over by a car</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پوران زیر ماشین رفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run scared</quote>
      <usg type="reg">خودمانی</usg>
      <cit type="trans" xml:lang="fa">
        <quote>از خطر یا احتمال شکست ترسیدن، روش ترس‌آمیز داشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run through</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (با بی‌فکری یا سرعت) خرج کردن، مصرف کردن، لوطی خور کردن 2- (با چیز تیز) سوراخ کردن 3- (باسرعت) بررسی کردن، دوره‌کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* run up</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (با سرعت) ساختن، بنا کردن 2- (قرض و غیره) ایجاد کردن، به بار آوردن</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <pos>صفت</pos>
  <pos>فعل متعدی</pos>
  <pos>فعل لازم</pos>
  <def xml:lang="fa">
    <dtrn>دویدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the child ran to her mother</ex_orig>
      <ex_tran xml:lang="fa">کودک به سوی مادرش دوید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I ran and I ran; to a mountain top I came ...</ex_orig>
      <ex_tran xml:lang="fa">دویدم و دویدم سرکوهی رسیدم ....</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a running race</ex_orig>
      <ex_tran xml:lang="fa">مسابقه دو</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>به سرعت حرکت کردن، تند رفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a ship running before the wind</ex_orig>
      <ex_tran xml:lang="fa">یک کشتی که در جلو باد به تندی حرکت می‌کند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(معمولا با: to) مراجعه کردن(به)، (پیش کسی یا چیزی) رفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she is always running to the police</ex_orig>
      <ex_tran xml:lang="fa">او مرتبا به پلیس مراجعه می‌کند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">as soon as anything happens he runs to his mother's lap</ex_orig>
      <ex_tran xml:lang="fa">تا چیزی می‌شود به دامن مادرش پناه می‌برد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(معمولا با: with) معاشر بودن (با)</dtrn>
    <ex>
      <ex_orig xml:lang="en">he runs around with a bunch of hoodlums</ex_orig>
      <ex_tran xml:lang="fa">او با یک دسته اراذل و اوباش دوستی می‌کند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(آزادانه) آمدن، رفتن، رستن، جنبیدن، گشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">deer used to run free in these woods</ex_orig>
      <ex_tran xml:lang="fa">در این بیشه‌ها آهوان آزادانه می‌گشتند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>فرار کردن، به چاک زدن، ورمالیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">our dog ran away</ex_orig>
      <ex_tran xml:lang="fa">سگ ما فرار کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(با: up to یا down to یا over to و غیره) سفر تند و کوتاه کردن، زود رفتن و آمدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">run over to the store and get me some sugar</ex_orig>
      <ex_tran xml:lang="fa">تند برو به مغازه و برایم قدری شکر بگیر.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در مسابقه یا انتخابات و غیره) شرکت کردن، نامزد (انتخابات و غیره) بودن یا کردن، شرکت دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">he is going to run as an independent candidate</ex_orig>
      <ex_tran xml:lang="fa">او به عنوان نامزد مستقل (در انتخابات) شرکت خواهد کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to run a race</ex_orig>
      <ex_tran xml:lang="fa">در مسابقه شرکت کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در مسابقات – اول یا دوم و غیره) شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run last</ex_orig>
      <ex_tran xml:lang="fa">آخر شدن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(ماهی – در جهت معینی) شنا کردن، مهاجرت کردن، مهاجرت، کوچ</dtrn>
    <ex>
      <ex_orig xml:lang="en">salmons run upstream for spawning</ex_orig>
      <ex_tran xml:lang="fa">ماهی آزاد برای تخم‌گذاری به بالای رودخانه شنا می‌کند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(طبق برنامه مرتبا) رفت و آمد کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a bus that runs between Tehran and Tabriz</ex_orig>
      <ex_tran xml:lang="fa">اتوبوسی که میان تهران و تبریز رفت و آمد می‌کند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به سرعت از روی چیزی) رد شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">his eyes ran over the page</ex_orig>
      <ex_tran xml:lang="fa">به سرعت صفحه را از مد نظر گذراند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>شایع بودن، زبانزد بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a rumor running through the town</ex_orig>
      <ex_tran xml:lang="fa">شایعه‌ای که در شهر زبانزد شده است</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>بالا رفتن، خزیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a vine running over the wall</ex_orig>
      <ex_tran xml:lang="fa">درخت مو که از دیوار بالا می‌رود</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(دائما) کار کردن یا جنبیدن، بند نیامدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">his tongue ran on and on</ex_orig>
      <ex_tran xml:lang="fa">زبانش بند آمدنی نبود.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(اداره یا موتور و غیره) کار کردن، به کار افتادن یا انداختن</dtrn>
    <ex>
      <ex_orig xml:lang="en">I don't know how to run this motor</ex_orig>
      <ex_tran xml:lang="fa">نمی‌دانم این موتور را چگونه به کار بیاندازم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a machine that is running</ex_orig>
      <ex_tran xml:lang="fa">موتوری که دارد کار می‌کند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به فکر) خطور کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the memory of that accident keeps running through my mind</ex_orig>
      <ex_tran xml:lang="fa">خاطرهٔ آن حادثه مرتبا در فکرم خطور می‌کند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>روان بودن، جریان داشتن، جاری کردن یا بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">running water</ex_orig>
      <ex_tran xml:lang="fa">آب روان</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">at the foot of the hill, the river runs more slowly</ex_orig>
      <ex_tran xml:lang="fa">در پای تپه (جریان) رودخانه آهسته‌تر می‌شود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">let the water run through the pipe</ex_orig>
      <ex_tran xml:lang="fa">بگذار آب در لوله جاری شود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">gutters running blood</ex_orig>
      <ex_tran xml:lang="fa">جوی‌هایی که خون در آن جاری است</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>آب شدن و جاری شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the vax ran</ex_orig>
      <ex_tran xml:lang="fa">موم آب شد و جاری شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the butter was beginning to run</ex_orig>
      <ex_tran xml:lang="fa">کره داشت آب می‌شد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(پارچه) رنگ پس دادن، (رنگ) دواندن، سرایت کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">colors guaranteed not to run or fade</ex_orig>
      <ex_tran xml:lang="fa">رنگ‌هایی که تضمین شده است سرایت نمی‌کنند و نمی‌پرند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پر بودن، سرشار بودن، لبریز بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">her eyes were running with tears</ex_orig>
      <ex_tran xml:lang="fa">چشمانش از اشک لبریز بودند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>چکه کردن، (آب یا چرک و غیره) پس دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a running sore</ex_orig>
      <ex_tran xml:lang="fa">زخمی که از آن چرک یا خون می‌آید</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(زمان) کشیدن، گذشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the days ran into weeks</ex_orig>
      <ex_tran xml:lang="fa">روزها به هفته‌ها کشید.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در روزنامه یا صحنهٔ تئاتر و غیره) ظاهر شدن، چاپ کردن، نمایش(دهی)</dtrn>
    <ex>
      <ex_orig xml:lang="en">a film that had a long run</ex_orig>
      <ex_tran xml:lang="fa">فیلمی که مدت زیادی نمایش داده می‌شد</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a play that ran for a full year</ex_orig>
      <ex_tran xml:lang="fa">نمایشی که یک سال تمام روی صحنه آورده می‌شد</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">several newspapers run his articles</ex_orig>
      <ex_tran xml:lang="fa">چندین روزنامه مقاله‌های او را چاپ می‌کنند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(قانون و غیره) اعتبار داشتن، به قوت قانونی باقی ماندن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a law running for 25 years</ex_orig>
      <ex_tran xml:lang="fa">قانونی که 25 سال است به قوت خود باقیست</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به طور موروثی) وجود داشتن، فراوان بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">musical talent runs in this family</ex_orig>
      <ex_tran xml:lang="fa">استعداد موسیقی در این خانواده فراوان است.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>گرایش داشتن، تمایل داشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">their taste runs more to exotic foods</ex_orig>
      <ex_tran xml:lang="fa">سلیقهٔ آنان به خوراک‌های عجیب و غریب گرایش بیشتری دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به صورت خط یا راه و غیره) ادامه داشتن، گذشتن، رد شدن، کشیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run lines on a sheet of paper</ex_orig>
      <ex_tran xml:lang="fa">روی یک صفحه کاغذ خط کشیدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">this railway runs through a forest</ex_orig>
      <ex_tran xml:lang="fa">این راه‌آهن از میان جنگل می‌گذرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a fence that runs through the middle of our land</ex_orig>
      <ex_tran xml:lang="fa">نرده‌ای که از میان زمین ما رد می‌شود</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(با: from و to) شامل بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">his plays run from tragedies to comedies</ex_orig>
      <ex_tran xml:lang="fa">نمایشنامه‌های او شامل سوگمایش و شادمایش (تراژدی و کمدی) می‌شود.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به وضع خاصی) رسیدن، برخوردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run into trouble</ex_orig>
      <ex_tran xml:lang="fa">به اشکال برخوردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(کشتی یا اتومبیل و غیره) خوردن به</dtrn>
    <ex>
      <ex_orig xml:lang="en">the boat ran aground</ex_orig>
      <ex_tran xml:lang="fa">کشتی به گل نشست</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the car ran into a tree</ex_orig>
      <ex_tran xml:lang="fa">اتومبیل به درخت خورد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(خبر یا داستان و غیره) بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the story runs like this</ex_orig>
      <ex_tran xml:lang="fa">داستان بدین قرار است</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(قیمت یا اندازه و غیره) بودن، داشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">boots that run $40</ex_orig>
      <ex_tran xml:lang="fa">پوتین‌هایی که 40 دلار قیمت دارند</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">apples running 7 to a kilo</ex_orig>
      <ex_tran xml:lang="fa">هر 7 تا سیب یک کیلو وزن دارد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">prices are running high</ex_orig>
      <ex_tran xml:lang="fa">قیمت‌ها بالا هستند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(قرض) بالا آوردن، (ریسک یا خطر) کردن، به خود هموار کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the free-spending man ran up a heavy debt</ex_orig>
      <ex_tran xml:lang="fa">مرد ولخرج قرض سنگینی به بار آورد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">if you go,you run the risk of being shot</ex_orig>
      <ex_tran xml:lang="fa">اگر بروی خطر تیر خوردن را به خود هموار می‌کنی.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(محاصره وغیره را) شکستن، عبور کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run a naval blockade</ex_orig>
      <ex_tran xml:lang="fa">محاصرهٔ دریایی را شکستن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to run a red light</ex_orig>
      <ex_tran xml:lang="fa">از چراغ قرمز عبور کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(موتور اتومبیل و غیره را) درجا به کار انداختن (to idle هم می‌گویند)، هرز کار کردن، خلاص کار کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">let the engine run for five minutes so that it warms up</ex_orig>
      <ex_tran xml:lang="fa">بگذار موتور (اتومبیل) پنج دقیقه در جا کار کند تا گرم شود.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(جوراب بلند زنانه) نخ‌کش، دررفتگی، نخ‌کش شدن، دررفتگی پیدا کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">these stockings run easily</ex_orig>
      <ex_tran xml:lang="fa">این جوراب‌ها زود نخ‌کش می‌شوند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">there is a big run in your stocking</ex_orig>
      <ex_tran xml:lang="fa">جورابت دررفتگی بزرگی دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(کشتی و اتوبوس و غیره) حمل کردن، بردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">our ships run passengers as well as cargo</ex_orig>
      <ex_tran xml:lang="fa">کشتی‌های ما هم مسافر و هم محموله می‌برند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>قاچاق کردن، قاچاق حمل کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run whiskey</ex_orig>
      <ex_tran xml:lang="fa">ویسکی قاچاق کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>چپاندن، با فشار وارد کردن یا عبور دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">run the rod in and out of the hole to make it bigger</ex_orig>
      <ex_tran xml:lang="fa">میله را چند بار بکن توی سوراخ و در بیاور تا گشادتر شود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he run his sword through the middle of Goodarz' neck</ex_orig>
      <ex_tran xml:lang="fa">شمشیرش را از وسط گردن گودرز رد کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>اداره کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to run a household</ex_orig>
      <ex_tran xml:lang="fa">خانواده‌ای را اداره کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">they ran the country on a tight budget</ex_orig>
      <ex_tran xml:lang="fa">آنها کشور را با بودجهٔ محدودی اداره کردند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(آزمایش و غیره) کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the doctors decided to run another test</ex_orig>
      <ex_tran xml:lang="fa">دکترها تصمیم گرفتند یک آزمایش دیگر هم بکنند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(تب) داشتن، کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she has been running a fever for three days</ex_orig>
      <ex_tran xml:lang="fa">سه روز است تب دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>عمل دویدن، دو، گام‌های تند</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>مسابقهٔ دو</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>(اتوبوس و کشتی و غیره) یک رفت (یا یک برگشت)، سفر</dtrn>
    <ex>
      <ex_orig xml:lang="en">this train runs between Tehran and Ghom and each run takes two hours</ex_orig>
      <ex_tran xml:lang="fa">این ترن میان تهران و قم رفت و برگشت می‌کند و هر سفر دو ساعت طول می‌کشد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>جریان، روانی</dtrn>
    <ex>
      <ex_orig xml:lang="en">the run of events</ex_orig>
      <ex_tran xml:lang="fa">جریان امور</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the run of the tide</ex_orig>
      <ex_tran xml:lang="fa">جریان کشند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>رخ دادن پی‌درپی، سلسله، دوره</dtrn>
    <ex>
      <ex_orig xml:lang="en">a run of good luck</ex_orig>
      <ex_tran xml:lang="fa">چند بار شانس خوب</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به ویژه مشتریان) هجوم بردن (به)</dtrn>
    <ex>
      <ex_orig xml:lang="en">customers made a run on the banks</ex_orig>
      <ex_tran xml:lang="fa">مشتریان (برای مطالبهٔ پول خود) به بانک‌ها هجوم بردند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-50 (به شرطی که تند باشد) نهر، جوی، رودچه -51 مدت کار کردن موتور و غیره، بازده ماشین (در این مدت) -52 (کالا یا مردم و غیره) نوع معمولی، نوع</dtrn>
    <ex>
      <ex_orig xml:lang="en">ordinary run of people</ex_orig>
      <ex_tran xml:lang="fa">مردم عادی</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-53 (اسکی) پیست</dtrn>
    <ex>
      <ex_orig xml:lang="en">a ski run</ex_orig>
      <ex_tran xml:lang="fa">پیست اسکی</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-54 (جانوران) مسیر، راه</dtrn>
    <ex>
      <ex_orig xml:lang="en">a buffalo run</ex_orig>
      <ex_tran xml:lang="fa">مسیر گاوهای وحشی</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-55 آزادی رفت و آمد یا ورود و خروج یا استفاده</dtrn>
    <ex>
      <ex_orig xml:lang="en">my brothers have the run of my house</ex_orig>
      <ex_tran xml:lang="fa">برادران من می‌توانند هر وقت بخواهند به منزل من بیایند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-56 (بیس‌بال – یک امتیاز در اثر یک بار دور زمین گشتن) ران -57 (هواپیما – برای تیراندازی یا بمباران) شیرجه رفتن، از ارتفاع کاستن، به هدف نزدیک شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">despite enemy fire, we made three runs and left the target in flames</ex_orig>
      <ex_tran xml:lang="fa">با وجود آتش دشمن سه بار شیرجه رفتیم و هدف را به حریق کشاندیم.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>-58 (کامپیوتر) رانش، اجرا، رانیدن، اجرا کردن (برنامه) -59 ذوب شده، آب شده -60 (فلز) قالب گیری شده، ریخته، ریخته‌گری شده، ریختن، ریخته‌گری</dtrn>
    <ex>
      <ex_orig xml:lang="en">run metal</ex_orig>
      <ex_tran xml:lang="fa">فلز ریخته‌گری شده</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* a run for one's money</ex_orig>
      <ex_tran xml:lang="fa">1- رقابت شدید 2- بهره وری (از سرمایه‌گذاری یا صرف وقت و غیره)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* in the long run</ex_orig>
      <ex_tran xml:lang="fa">بالاخره، در دراز مدت، نتیجهٔ نهایی</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* in the short run</ex_orig>
      <ex_tran xml:lang="fa">در آغاز، در ابتدا، در کوتاه مدت</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* on the run</ex_orig>
      <ex_tran xml:lang="fa">1- درحال دویدن 2- در تکاپو، سخت مشغول 3- در حال فرار، درحال عقب نشینی</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run across</ex_orig>
      <ex_tran xml:lang="fa">(اتفاقا) برخوردن (به کسی یا چیزی)، ملاقات کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run after</ex_orig>
      <ex_tran xml:lang="fa">تعقیب کردن، دنبال کسی یا چیزی دویدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run along</ex_orig>
      <ex_tran xml:lang="fa">رفتن، عزیمت کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I must run along now</ex_orig>
      <ex_tran xml:lang="fa">اکنون باید بروم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run around with</ex_orig>
      <ex_tran xml:lang="fa">با کسی دیگر رابطه داشتن یا معاشر بودن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">her husband was running around with another woman</ex_orig>
      <ex_tran xml:lang="fa">شوهرش با یک زن دیگر رابطه داشت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run away</ex_orig>
      <ex_tran xml:lang="fa">1- فرار کردن، گریختن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the prisoner ran away</ex_orig>
      <ex_tran xml:lang="fa">زندانی فرار کرد.</ex_tran>
      <ex_tran xml:lang="fa">2- ترک خانواده (یا وطن) کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run away with</ex_orig>
      <ex_tran xml:lang="fa">1- رفتن و با خود بردن، دزدیدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he ran away with my purse</ex_orig>
      <ex_tran xml:lang="fa">کیف پولم را زد.</ex_tran>
      <ex_tran xml:lang="fa">2- مهار نکردنی شدن، از کنترل خارج شدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">her enthusiasm ran away with her</ex_orig>
      <ex_tran xml:lang="fa">اشتیاق او لجام گسیخته شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run back</ex_orig>
      <c c="gray">فوتبال آمریکایی</c>
      <ex_tran xml:lang="fa">با توپ به سوی دروازهٔ حریف دویدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run down</ex_orig>
      <ex_tran xml:lang="fa">1- (به خاطر کمبود سوخت یا برق و غیره) از کار ایستادن 2- (با ماشین و غیره به کسی یا چیزی) زدن و افکندن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the truck ran down two large trees</ex_orig>
      <ex_tran xml:lang="fa">کامیون دو درخت بزرگ را انداخت.</ex_tran>
      <ex_tran xml:lang="fa">3- تعقیب کردن و گرفتن (یا کشتن)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run for it</ex_orig>
      <ex_tran xml:lang="fa">(به منظور فرار یا احتراز) دویدن، دو زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run idle</ex_orig>
      <ex_tran xml:lang="fa">(موتور اتومبیل و غیره) خلاص کار کردن، هرزکارکردن، درجا کار کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run in</ex_orig>
      <ex_tran xml:lang="fa">1- (به عنوان چیز اضافی) افزودن، شامل کردن، گنجاندن 2- (عامیانه) توقف کوتاه کردن 3- (عامیانه) بازداشت کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run into</ex_orig>
      <ex_tran xml:lang="fa">1- (اتفاقا) برخوردن به، ملاقات کردن 2- تصادم کردن با، خوردن به، زدن به</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he again ran into the telephone pole with his car</ex_orig>
      <ex_tran xml:lang="fa">دوباره با ماشین زد به تیر تلفن.</ex_tran>
      <ex_tran xml:lang="fa">run to) -3 هم می‌گویند) بالغ شدن بر، رسیدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the two cars ran into each other</ex_orig>
      <ex_tran xml:lang="fa">دو اتومبیل با هم شاخ به شاخ شدند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">their debts run into several millions</ex_orig>
      <ex_tran xml:lang="fa">قروض آنان به چندین میلیون می‌رسد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run off</ex_orig>
      <ex_tran xml:lang="fa">1- (متن را) تکثیر کردن، چاپ کردن، پلی‌کپی کردن، تایپ کردن 2- تاراندن، دور کردن 3- هرز رفتن 4- به خارج جاری شدن یا ریختن 5- فرار کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run on</ex_orig>
      <ex_tran xml:lang="fa">1- ادامه دادن، ادامه یافتن 2- به آخر چیزی اضافه کردن 3- دائما حرف زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run out</ex_orig>
      <ex_tran xml:lang="fa">1- منقضی شدن، به پایان رسیدن، تمام شدن، مصرف شدن 2- بیرون کردن، بیرون راندن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run out of</ex_orig>
      <ex_tran xml:lang="fa">(موجودی چیزی را) به اتمام رساندن، دیگر نداشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run out on</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">تنها گذاشتن و رفتن، قال گذاشتن، رها کردن، ترک کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run out the clock</ex_orig>
      <ex_tran xml:lang="fa">(فوتبال و بسکتبال و غیره – در اواخر مسابقه) توپ را کنترل کردن، وقت کشی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run over</ex_orig>
      <ex_tran xml:lang="fa">1- لبریز شدن 2- (با اتومبیل و غیره) زیر گرفتن، زیر ماشین رفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Pooran was run over by a car</ex_orig>
      <ex_tran xml:lang="fa">پوران زیر ماشین رفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run scared</ex_orig>
      <c c="gray">خودمانی</c>
      <ex_tran xml:lang="fa">از خطر یا احتمال شکست ترسیدن، روش ترس‌آمیز داشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run through</ex_orig>
      <ex_tran xml:lang="fa">1- (با بی‌فکری یا سرعت) خرج کردن، مصرف کردن، لوطی خور کردن 2- (با چیز تیز) سوراخ کردن 3- (باسرعت) بررسی کردن، دوره‌کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* run up</ex_orig>
      <ex_tran xml:lang="fa">1- (با سرعت) ساختن، بنا کردن 2- (قرض و غیره) ایجاد کردن، به بار آوردن</ex_tran>
    </ex>
  </def>
</def>
```

## 40. Saarbrücken

TEI source: `20-s.xml` entry 9 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 40 (key `Saarbrücken`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Saarbrücken</orth>
  <pron>sär´brook´ən</pron>
</form>
```

XDXF:

```xml
<k>Saarbrücken</k>
<tr>sär´brook´ən</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شهر ساربروکن (پایتخت سارلند در غرب آلمان)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>شهر ساربروکن (پایتخت سارلند در غرب آلمان)</dtrn>
  </def>
</def>
```

## 41. Ta

TEI source: `21-t.xml` entry 6 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 41 (key `Ta`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Ta</orth>
</form>
```

XDXF:

```xml
<k>Ta</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(شیمی – مخفف) نشان تانتال (tantalum)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>(شیمی – مخفف) نشان تانتال (tantalum)</dtrn>
  </def>
</def>
```

## 42. take

TEI source: `21-t.xml` entry 165 (score 447, rare 0)  
XDXF article: `en-fa.xdxf` # 42 (key `take`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>take</orth>
  <pron>tāk</pron>
</form>
```

XDXF:

```xml
<k>take</k>
<tr>tāk</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
    <pos norm="transitive verb">فعل متعدی</pos>
    <pos norm="intransitive verb">فعل لازم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>گرفتن، تسخیر کردن، مسخر کردن، تصاحب کردن، فتح کردن، استاندن، یازیدن، دست اندازی کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">they took the fort in two days</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دو روزه دژ را تسخیر کردند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the town and carried its people into captivity</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او شهر را فتح کرد و مردم آن را به اسارت برد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">...give or else a tyrant will take by force</quote>
      <cit type="trans" xml:lang="fa">
        <quote>...بده ورنه ستمگر به زور بستاند</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>ماهی (و غیره) گرفتن، صید کردن، شکار کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">eighty percent of the whales today are taken in the Antarctic</quote>
      <cit type="trans" xml:lang="fa">
        <quote>امروزه هشتاد درصد نهنگ‌ها در جنوبگان صید می‌شوند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the taking of birds and deer</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شکار پرندگان و آهو</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در دست یا با دست) گرفتن، در دست نگهداشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">take the pen in your right hand</quote>
      <cit type="trans" xml:lang="fa">
        <quote>قلم را در دست راست خود بگیر.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took the child in my arms</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کودک را در بغل گرفتم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the hammer firmly by the handle</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دستهٔ چکش را محکم گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took my hand and guided me step by step...</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دستم بگرفت و پابپا برد...</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(چیزی را از کسی) گرفتن، به دست آوردن، ستدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">if you can play better, take it and play!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گر تو بهتر می‌زنی بستان بزن!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took my watch and never gave it back</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ساعتم را گرفت و هرگز پس نداد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she would not take money from the poor</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او از مسکینان پول نمی‌گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Akram takes bribes</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اکرم رشوه می‌گیرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>برداشتن، ورداشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">take anything you want</quote>
      <cit type="trans" xml:lang="fa">
        <quote>هرچه دلت می‌خواهد بردار.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she accused me of taking his camera</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مرا متهم کرد که دوربین عکاسی او را برداشته‌ام.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">don't take things that do not belong to you!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چیزهایی را که به تو تعلق ندارند بر ندار!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took his hat and overcoat and left</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کلاه و پالتو خود را برداشت و رفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took the book off the shelf</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کتاب را از تاقچه برداشتم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">who took the money I had left here?</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پولی را که این‌جا گذاشته بودم کی برداشت؟</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(شطرنج و نرد و غیره) کشتن، برنده بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">my rook took his horse</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رخ من اسب او را کشت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">ace takes the king</quote>
      <cit type="trans" xml:lang="fa">
        <quote>خال آس از شاه می‌برد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به بخشی از بدن) زدن، خوردن (به)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his punch took me right on the chin</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مشت او درست خورد به چانهٔ من.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دچار کردن، دستخوش کردن یا شدن، (بیماری) گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she was taken with a fit of laughing</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ناگهان دستخوش خندهٔ شدید شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to be taken ill</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دچار بیماری شدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Asghar was taken with pneumonia</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اصغر سینه پهلو گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the child took the measles</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بچه سرخک گرفت.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در حین ارتکاب و غیره) مچ کسی را گرفتن، غافلگیر کردن، دستگیر کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the thieves were taken by the police</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پلیس دزدان را دستگیر کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the officer took the sentinel napping</quote>
      <cit type="trans" xml:lang="fa">
        <quote>افسر مچ نگهبانی را که چرت می‌زد گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take someone in the very act</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در حین ارتکاب کسی را غافگیر کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">taken in adultry</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گرفتار شده هنگام انجام زنا</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>مفتون کردن، مجذوب کردن، جلب کردن، خرسند کردن، (از کسی یا چیزی) خوش آمدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his performance seemed to have taken the fancy of the crowd</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چنین به نظر می‌رسد که بازیگری او آن جماعت را مسحور کرده بود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the parents of the girl were much taken with Ali</quote>
      <cit type="trans" xml:lang="fa">
        <quote>والدین آن دختر خیلی از علی خوششان آمده بود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">her eyes took my attention momentarily</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چشمانش برای لحظه‌ای توجه مرا جلب کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>خوردن، نوشیدن، لب زدن، فرودادن، فرو بردن، استنشاق کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take poison</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زهر خوردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she has taken no food for three days</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سه روز است خوراک نخورده است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the medicine with a glass of water</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دارو را با یک لیوان آب خورد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">don't take the smoke into your lungs!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دود را به ریه‌ات فرو نبر!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this drug is not to be taken internally</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این دارو را نباید خورد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took her breakfast alone</quote>
      <cit type="trans" xml:lang="fa">
        <quote>صبحانه را تنها صرف کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(زن یا معشوق وغیره) گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took her to wife</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او را به زنی گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his wife took a lover</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زنش فاسق گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she has started taking private students</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او شروع کرده است به گرفتن شاگردان خصوصی.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به شغل یا مقام و غیره) رسیدن، به عهده گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a job</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کار گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took office last year</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سال پیش به این شغل رسید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took service under a foreign flag</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او زیر یک پرچم خارجی خدمت می‌کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the responsibility for keeping order</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مسئولیت حفظ نظم را به عهده گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Ahmad took the role of a fool</quote>
      <cit type="trans" xml:lang="fa">
        <quote>احمد نقش دلقک را به عهده گرفت.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(سوگند) خوردن، (قول و غیره) دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took a vow never to gamble again</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او عهدکرد که دیگر هرگز قمار نکند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take an oath</quote>
      <cit type="trans" xml:lang="fa">
        <quote>قسم خوردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(مسابقه یا جایزه و غیره) بردن، شکست دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took the first prize</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او جایزهٔ اول را برد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the fight by a knockout</quote>
      <cit type="trans" xml:lang="fa">
        <quote>با ضربهٔ فنی در مسابقهٔ مشت زنی برنده شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took the first place in the broad jump</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در پرش طول مقام اول را به دست آورد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>برگزیدن، گزیدن، انتخاب کردن، خریدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the first suit he tried on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اولین لباسی را که پرو کرد خرید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">take any number from one to ten</quote>
      <cit type="trans" xml:lang="fa">
        <quote>هر شماره‌ای را که می‌خواهی از یک تا ده انتخاب کن.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">let him take his pick</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بگذار به میل خودش انتخاب کند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">always take the straight road!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>همیشه صراط مستقیم را برگزین!</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>اتخاذ کردن، دست زدن (به)، متوسل شدن (به)، استفاده کردن (از)</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the government had to take severe measures</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دولت مجبور شد دست به اقدام شدید بزند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">we took any means we could think of</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به هر وسیله‌ای که به فکرمان رسید متوصل شدیم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took the first opportunity</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از اولین فرصت استفاده کردم.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>گنجایش داشتن، جا داشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this bus takes 40 passengers</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این اتوبوس برای 40 مسافر جا دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>اجاره کردن، آبونه شدن یا بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a summer house</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یک خانهٔ تابستانی اجاره کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a daily newspaper</quote>
      <cit type="trans" xml:lang="fa">
        <quote>روزنامهٔ روزانه را آبونه بودن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <usg type="reg">خودمانی</usg>
    <cit type="trans">
      <quote>گول زدن، گوش کسی را بریدن</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <usg type="gram">دستور زبان</usg>
    <cit type="trans">
      <quote>حالت بخصوص گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a transitive verb takes an object</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فعل متعدی مفعول می‌گیرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the word "book" takes an "s" in the plural</quote>
      <cit type="trans" xml:lang="fa">
        <quote>واژهٔ "book" در جمع "s" می‌گیرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(وسیلهٔ نقلیه) گرفتن، سوار شدن، با... رفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a bus</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اتوبوس گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">you can take the subway</quote>
      <cit type="trans" xml:lang="fa">
        <quote>می‌توانی با مترو بروی</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جستن، (پناه) بردن، (بست) نشستن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take shelter</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پناه جستن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take sanctuary</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بست نشستن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">as soon as he saw the bear, he took to the nearest tree</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تا خرس را دید به نزدیک‌ترین درخت پناه برد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جای گرفتن، مستقر شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a seat in the rear</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در عقب (یک محل) جای گرفتن (نشستن)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the president took the chair</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رییس جمهور بر مسند نشست.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she is always ready to take the spotlight</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او برای این‌که مرکز توجه باشد همیشه آمادگی دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(وقت و غیره) صرف کردن، گرفتن، طول کشیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">writing this dictionary will take six years</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نگارش این فرهنگ شش سال طول خواهد کشید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">it takes a lot of time</quote>
      <cit type="trans" xml:lang="fa">
        <quote>خیلی وقت می‌گیرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>نیاز داشتن، لازم داشتن، مستلزم بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">it takes money to travel</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سفر کردن پول لازم دارد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">it takes courage to do what he did</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کاری که او کرد به شجاعت نیاز دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(به ارث) بردن، (به کسی) رفتن، (اسم یا لقب و غیره) گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he takes after his father</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او به پدرش رفته است.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>نقل کردن، نقل قول کردن، گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a verse from the Bible</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سوره‌ای از انجیل را نقل کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>- کردن، – برداشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a poll</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نظر خواهی عمومی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a vote</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رای گیری کردن، رای گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take notes</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نت برداشتن، یادداشت کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take attendance</quote>
      <cit type="trans" xml:lang="fa">
        <quote>حاضر غایب کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take inventory</quote>
      <cit type="trans" xml:lang="fa">
        <quote>صورت موجودی برداشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a copy of a will</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از وصیت نامه نسخه برداشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take pictures</quote>
      <cit type="trans" xml:lang="fa">
        <quote>عکس برداشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a person's fingerprints</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کسی را انگشت نگاری کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take part in an activity</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در کاری شرکت کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a leave of absence</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مرخصی گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a walk</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیاده‌روی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a music course</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کلاس موسیقی گرفتن (انتخاب کردن)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a rest</quote>
      <cit type="trans" xml:lang="fa">
        <quote>استراحت کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take the room's measurements</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اتاق را اندازه گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take notice</quote>
      <cit type="trans" xml:lang="fa">
        <quote>توجه کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پذیرفتن، پذیرا بودن، قبول کردن، تحمل کردن، تاب داشتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">take my advice!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پند مرا بپذیر!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take a bet</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شرط بندی (قبول) کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took my joke seriously</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او شوخی مرا جدی گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took his punishment like a man</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مثل مرد تنبیه خود را قبول کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this plant takes cold weather beautifully</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این گیاه در هوای سرد خوب تاب می‌آورد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>فهمیدن، درک کردن، پی بردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his hearers were slow to take his meaning</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شنودگان زود به منظور او پی نبردند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she took my hint immediately</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فورا به اشارهٔ من پی برد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(با خود یا به محلی) بردن، حمل کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">God will take the ship where he pleases ...</quote>
      <cit type="trans" xml:lang="fa">
        <quote>برد کشتی آنجا که خواهد خدای ...</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took his wife to a doctor</quote>
      <cit type="trans" xml:lang="fa">
        <quote>زنش را پیش دکتر برد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">will you take me to a movie?</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مرا به سینما می‌بری؟</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took the whole family to dinner</quote>
      <cit type="trans" xml:lang="fa">
        <quote>همهٔ خانواده را برد به شام.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took them to London</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آنها را به لندن بردم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">this road will take you to the center of the city</quote>
      <cit type="trans" xml:lang="fa">
        <quote>این راه شما را به مرکز شهر خواهد برد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>کشتن، تباه کردن، نابود کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">cruel fate took him from us</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سرنوشت قدار او را از ما گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">cancer takes many lives</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سرطان خیلی‌ها را می‌کشد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>کسر کردن، کاستن، منها کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">nothing took from the scene's beauty</quote>
      <cit type="trans" xml:lang="fa">
        <quote>هیچ‌چیز از زیبایی آن صحنه نمی‌کاست.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">take three from five</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سه را از پنج کسر کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(قلمه یا پیوند یا آتش و غیره) گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">most of this surgeon's grafts take</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اکثر پیوندهایی که این جراح می‌زند می‌گیرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the wick was wet and the sparks didn't take</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فتیله تر بود و جرقه‌ها نگرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the fire took rapidly</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آتش به سرعت گرفت (روشن شد).</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the vaccination took</quote>
      <cit type="trans" xml:lang="fa">
        <quote>واکسن گرفت.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پنداشتن، به جای کسی یا چیزی دیگر گرفتن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took her to be a teacher</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فکر کردم که او معلم است.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>عمل گرفتن، در دست گیری، تسخیر، تصاحب، گرفت، گیرش</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>میزان گرفته شده یا صید شده یا بدست آوری شده</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a day's take of fish</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مقدار ماهی صید شده در یک روز</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دریافتی (ها)، مبالغ واریز شده، کسب، سود، درآمد</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to increase the city's take from gambling</quote>
      <cit type="trans" xml:lang="fa">
        <quote>درآمد شهر از محل قماربازی را بیشتر کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>واکسنی که می‌گیرد (اثر می‌کند)</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(عکسبرداری و فیلمبرداری) برداشت</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* on the take</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>رشوه گیر، دارای درآمد غیر مشروع</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a cop who is on the take</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پاسبانی که درآمد نامشروع دارد</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take after</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (به کسی) رفتن، شباهت داشتن 2- (کسی را) تعقیب کردن، دنبال کسی راه افتادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take a meeting</quote>
      <usg type="reg">خودمانی</usg>
      <cit type="trans" xml:lang="fa">
        <quote>در کنفرانس حضور یافتن، به جلسه رفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take a miss</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (در اصل) اشتباه کردن، عوضی گرفتن 2- درست درک نکردن، سو تفاهم پیدا کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take back</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- پس گرفتن (چیزی یا حرفی یا ادعایی) 2- پس دادن (چیزی خریداری شده)، پس بردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take down</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- یادداشت کردن 2- در جای پایین‌تر قرار دادن، تنزل دادن، پایین بردن 3- (شلوار و غیره) پایین کشیدن 4- خوار کردن، خفیف کردن، پست کردن 5- از هم باز کردن، پیاده کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take five (or ten, etc)</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(آمریکا- عامیانه) استراحت پنج دقیقه‌ای (یا ده دقیقه‌ای و غیره) کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take for</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- پنداشتن، تصور کردن، پذیرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I took him for an American</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فکر کردم که آمریکایی است.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- عوضی (به جای کس دیگر) گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take in</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- راه دادن، پذیرفتن، پذیرا شدن 2- (لباس یا بادبان کشتی و غیره) تو گرفتن، کوچک کردن 3- شامل بودن، حاوی بودن 4- درک‌کردن، فهمیدن 5- گول زدن، فریب دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">don't be taken in by his tempting promises!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گول وعده‌های وسوسه انگیز او را نخور!</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>6- دیدار کردن، بازدید کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to take in all the historical sights</quote>
      <cit type="trans" xml:lang="fa">
        <quote>همهٔ جاهای تاریخی را بازدید کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- فکر کردن، پنداشتن، تصور کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I take it he is her brother</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فکر می‌کنم او برادرش باشد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- تحمل کردن، تاب آوردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I am tired of this job; I can't take it any more!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از این شغل بیزارم و دیگر تاب تحمل آن را ندارم!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it easy!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سخت نگیر</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it from me</quote>
      <cit type="trans" xml:lang="fa">
        <quote>باور کن، به حرفم اعتماد کن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it or leave it</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>می‌خواهی بخواه و نمی‌خواهی نخواه، همین است که هست</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it out of</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>1- خسته کردن، فرسودن 2- تقاص گرفتن، پول در کشیدن (از)، غرامت گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take it out on</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>تلافی کاری را سر شخص ثالث درآوردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I know you've been fired from your office but don't take it out on the children!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>می‌دانم که از اداره اخراجت کرده‌اند ولی تلافی‌اش را سربچه‌ها در نیاور!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take off</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (جامه) در آوردن، کندن 2- (کلاه و عینک و غیره) برداشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">please take off your hat</quote>
      <cit type="trans" xml:lang="fa">
        <quote>لطفا کلاه خود را بردارید.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>3- عزیمت کردن، رفتن 4- (کار یا مدرسه) غیبت کردن، غایب شدن 5- کشتن 6- کسر کردن، کاستن، تخفیف دادن 7- کپی کردن، نسخه‌برداشتن 8- پرزدن، پرواز کردن 9- شروع کردن، آغاز کردن 10- (هواپیما) بلند شدن از زمین 11- (با: on) تقلید کردن، تقلید در آوردن 12- (عامیانه) موفق شدن، گل کردن، (کار و بار) گرفتن 13- (خودمانی) دزدیدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- به خود گرفتن، شکل گرفتن، رنگ گرفتن، قوام گرفتن 2- استخدام کردن، به کار گرفتن 3- به عهده گرفتن، تقبل کردن 4- به مبارزه‌طلبیدن، از پس کسی یا چیزی برآمدن، مقابله کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take one's time</quote>
      <cit type="trans" xml:lang="fa">
        <quote>باتانی کار کردن، وقت کافی صرف کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take out</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- کسر کردن، کاستن 2- درآوردن، کشیدن (بیرون) 3- (با پر کردن درخواست و غیره وام و غیره) گرفتن، به دست آوردن 4-(عامیانه) همراهی کردن، (به محلی) بردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take over</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به عهده گرفتن، تصدی چیزی را قبول کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take place</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به وقوع پیوستن، روی دادن، رخ دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take sides</quote>
      <cit type="trans" xml:lang="fa">
        <quote>طرفداری کردن، یک طرف را گرفتن، سوگیری کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take something easy</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سخت نگرفتن، سخت‌گیری نکردن، آسان گرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take to</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- عادت کردن، خوگرفتن 2- پناه بردن به، (به محلی) رفتن 3- (به کار یا مطالعه و غیره) پرداختن 4- (از کسی) خوش آمدن، به دل راه‌دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take up</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- افراشتن، بلند کردن، بالابردن 2- (لباس و غیره) تو گرفتن، کوتاه کردن، تنگ کردن 3- جذب کردن، در آشامیدن 4- پذیرفتن، به عهده‌گرفتن 5- ادامه دادن 6- علاقمند شدن به 7- جاگرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take upon (or on) oneself</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- مسئولیت کاری را پذیرفتن، به عهده گرفتن، تقبل کردن 2- انجام کاری را آغاز کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take up with</quote>
      <usg type="reg">عامیانه</usg>
      <cit type="trans" xml:lang="fa">
        <quote>دوست کسی شدن، همدم شدن، هم‌نشینی کردن</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <pos>فعل متعدی</pos>
  <pos>فعل لازم</pos>
  <def xml:lang="fa">
    <dtrn>گرفتن، تسخیر کردن، مسخر کردن، تصاحب کردن، فتح کردن، استاندن، یازیدن، دست اندازی کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">they took the fort in two days</ex_orig>
      <ex_tran xml:lang="fa">دو روزه دژ را تسخیر کردند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the town and carried its people into captivity</ex_orig>
      <ex_tran xml:lang="fa">او شهر را فتح کرد و مردم آن را به اسارت برد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">...give or else a tyrant will take by force</ex_orig>
      <ex_tran xml:lang="fa">...بده ورنه ستمگر به زور بستاند</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>ماهی (و غیره) گرفتن، صید کردن، شکار کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">eighty percent of the whales today are taken in the Antarctic</ex_orig>
      <ex_tran xml:lang="fa">امروزه هشتاد درصد نهنگ‌ها در جنوبگان صید می‌شوند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the taking of birds and deer</ex_orig>
      <ex_tran xml:lang="fa">شکار پرندگان و آهو</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در دست یا با دست) گرفتن، در دست نگهداشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">take the pen in your right hand</ex_orig>
      <ex_tran xml:lang="fa">قلم را در دست راست خود بگیر.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I took the child in my arms</ex_orig>
      <ex_tran xml:lang="fa">کودک را در بغل گرفتم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the hammer firmly by the handle</ex_orig>
      <ex_tran xml:lang="fa">دستهٔ چکش را محکم گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she took my hand and guided me step by step...</ex_orig>
      <ex_tran xml:lang="fa">دستم بگرفت و پابپا برد...</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(چیزی را از کسی) گرفتن، به دست آوردن، ستدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">if you can play better, take it and play!</ex_orig>
      <ex_tran xml:lang="fa">گر تو بهتر می‌زنی بستان بزن!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took my watch and never gave it back</ex_orig>
      <ex_tran xml:lang="fa">ساعتم را گرفت و هرگز پس نداد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she would not take money from the poor</ex_orig>
      <ex_tran xml:lang="fa">او از مسکینان پول نمی‌گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Akram takes bribes</ex_orig>
      <ex_tran xml:lang="fa">اکرم رشوه می‌گیرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>برداشتن، ورداشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">take anything you want</ex_orig>
      <ex_tran xml:lang="fa">هرچه دلت می‌خواهد بردار.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she accused me of taking his camera</ex_orig>
      <ex_tran xml:lang="fa">مرا متهم کرد که دوربین عکاسی او را برداشته‌ام.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">don't take things that do not belong to you!</ex_orig>
      <ex_tran xml:lang="fa">چیزهایی را که به تو تعلق ندارند بر ندار!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took his hat and overcoat and left</ex_orig>
      <ex_tran xml:lang="fa">کلاه و پالتو خود را برداشت و رفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I took the book off the shelf</ex_orig>
      <ex_tran xml:lang="fa">کتاب را از تاقچه برداشتم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">who took the money I had left here?</ex_orig>
      <ex_tran xml:lang="fa">پولی را که این‌جا گذاشته بودم کی برداشت؟</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(شطرنج و نرد و غیره) کشتن، برنده بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">my rook took his horse</ex_orig>
      <ex_tran xml:lang="fa">رخ من اسب او را کشت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">ace takes the king</ex_orig>
      <ex_tran xml:lang="fa">خال آس از شاه می‌برد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به بخشی از بدن) زدن، خوردن (به)</dtrn>
    <ex>
      <ex_orig xml:lang="en">his punch took me right on the chin</ex_orig>
      <ex_tran xml:lang="fa">مشت او درست خورد به چانهٔ من.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>دچار کردن، دستخوش کردن یا شدن، (بیماری) گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she was taken with a fit of laughing</ex_orig>
      <ex_tran xml:lang="fa">ناگهان دستخوش خندهٔ شدید شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to be taken ill</ex_orig>
      <ex_tran xml:lang="fa">دچار بیماری شدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Asghar was taken with pneumonia</ex_orig>
      <ex_tran xml:lang="fa">اصغر سینه پهلو گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the child took the measles</ex_orig>
      <ex_tran xml:lang="fa">بچه سرخک گرفت.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در حین ارتکاب و غیره) مچ کسی را گرفتن، غافلگیر کردن، دستگیر کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the thieves were taken by the police</ex_orig>
      <ex_tran xml:lang="fa">پلیس دزدان را دستگیر کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the officer took the sentinel napping</ex_orig>
      <ex_tran xml:lang="fa">افسر مچ نگهبانی را که چرت می‌زد گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take someone in the very act</ex_orig>
      <ex_tran xml:lang="fa">در حین ارتکاب کسی را غافگیر کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">taken in adultry</ex_orig>
      <ex_tran xml:lang="fa">گرفتار شده هنگام انجام زنا</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>مفتون کردن، مجذوب کردن، جلب کردن، خرسند کردن، (از کسی یا چیزی) خوش آمدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">his performance seemed to have taken the fancy of the crowd</ex_orig>
      <ex_tran xml:lang="fa">چنین به نظر می‌رسد که بازیگری او آن جماعت را مسحور کرده بود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the parents of the girl were much taken with Ali</ex_orig>
      <ex_tran xml:lang="fa">والدین آن دختر خیلی از علی خوششان آمده بود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">her eyes took my attention momentarily</ex_orig>
      <ex_tran xml:lang="fa">چشمانش برای لحظه‌ای توجه مرا جلب کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>خوردن، نوشیدن، لب زدن، فرودادن، فرو بردن، استنشاق کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take poison</ex_orig>
      <ex_tran xml:lang="fa">زهر خوردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she has taken no food for three days</ex_orig>
      <ex_tran xml:lang="fa">سه روز است خوراک نخورده است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the medicine with a glass of water</ex_orig>
      <ex_tran xml:lang="fa">دارو را با یک لیوان آب خورد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">don't take the smoke into your lungs!</ex_orig>
      <ex_tran xml:lang="fa">دود را به ریه‌ات فرو نبر!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">this drug is not to be taken internally</ex_orig>
      <ex_tran xml:lang="fa">این دارو را نباید خورد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she took her breakfast alone</ex_orig>
      <ex_tran xml:lang="fa">صبحانه را تنها صرف کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(زن یا معشوق وغیره) گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">he took her to wife</ex_orig>
      <ex_tran xml:lang="fa">او را به زنی گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">his wife took a lover</ex_orig>
      <ex_tran xml:lang="fa">زنش فاسق گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she has started taking private students</ex_orig>
      <ex_tran xml:lang="fa">او شروع کرده است به گرفتن شاگردان خصوصی.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به شغل یا مقام و غیره) رسیدن، به عهده گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a job</ex_orig>
      <ex_tran xml:lang="fa">کار گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took office last year</ex_orig>
      <ex_tran xml:lang="fa">سال پیش به این شغل رسید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took service under a foreign flag</ex_orig>
      <ex_tran xml:lang="fa">او زیر یک پرچم خارجی خدمت می‌کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the responsibility for keeping order</ex_orig>
      <ex_tran xml:lang="fa">مسئولیت حفظ نظم را به عهده گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Ahmad took the role of a fool</ex_orig>
      <ex_tran xml:lang="fa">احمد نقش دلقک را به عهده گرفت.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(سوگند) خوردن، (قول و غیره) دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she took a vow never to gamble again</ex_orig>
      <ex_tran xml:lang="fa">او عهدکرد که دیگر هرگز قمار نکند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take an oath</ex_orig>
      <ex_tran xml:lang="fa">قسم خوردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(مسابقه یا جایزه و غیره) بردن، شکست دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she took the first prize</ex_orig>
      <ex_tran xml:lang="fa">او جایزهٔ اول را برد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the fight by a knockout</ex_orig>
      <ex_tran xml:lang="fa">با ضربهٔ فنی در مسابقهٔ مشت زنی برنده شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she took the first place in the broad jump</ex_orig>
      <ex_tran xml:lang="fa">در پرش طول مقام اول را به دست آورد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>برگزیدن، گزیدن، انتخاب کردن، خریدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">he took the first suit he tried on</ex_orig>
      <ex_tran xml:lang="fa">اولین لباسی را که پرو کرد خرید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">take any number from one to ten</ex_orig>
      <ex_tran xml:lang="fa">هر شماره‌ای را که می‌خواهی از یک تا ده انتخاب کن.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">let him take his pick</ex_orig>
      <ex_tran xml:lang="fa">بگذار به میل خودش انتخاب کند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">always take the straight road!</ex_orig>
      <ex_tran xml:lang="fa">همیشه صراط مستقیم را برگزین!</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>اتخاذ کردن، دست زدن (به)، متوسل شدن (به)، استفاده کردن (از)</dtrn>
    <ex>
      <ex_orig xml:lang="en">the government had to take severe measures</ex_orig>
      <ex_tran xml:lang="fa">دولت مجبور شد دست به اقدام شدید بزند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">we took any means we could think of</ex_orig>
      <ex_tran xml:lang="fa">به هر وسیله‌ای که به فکرمان رسید متوصل شدیم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I took the first opportunity</ex_orig>
      <ex_tran xml:lang="fa">از اولین فرصت استفاده کردم.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>گنجایش داشتن، جا داشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">this bus takes 40 passengers</ex_orig>
      <ex_tran xml:lang="fa">این اتوبوس برای 40 مسافر جا دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>اجاره کردن، آبونه شدن یا بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a summer house</ex_orig>
      <ex_tran xml:lang="fa">یک خانهٔ تابستانی اجاره کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a daily newspaper</ex_orig>
      <ex_tran xml:lang="fa">روزنامهٔ روزانه را آبونه بودن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <categ type="reg">خودمانی</categ>
    <dtrn>گول زدن، گوش کسی را بریدن</dtrn>
  </def>
  <def xml:lang="fa">
    <categ type="gram">دستور زبان</categ>
    <dtrn>حالت بخصوص گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">a transitive verb takes an object</ex_orig>
      <ex_tran xml:lang="fa">فعل متعدی مفعول می‌گیرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the word "book" takes an "s" in the plural</ex_orig>
      <ex_tran xml:lang="fa">واژهٔ "book" در جمع "s" می‌گیرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(وسیلهٔ نقلیه) گرفتن، سوار شدن، با... رفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a bus</ex_orig>
      <ex_tran xml:lang="fa">اتوبوس گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">you can take the subway</ex_orig>
      <ex_tran xml:lang="fa">می‌توانی با مترو بروی</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>جستن، (پناه) بردن، (بست) نشستن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take shelter</ex_orig>
      <ex_tran xml:lang="fa">پناه جستن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take sanctuary</ex_orig>
      <ex_tran xml:lang="fa">بست نشستن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">as soon as he saw the bear, he took to the nearest tree</ex_orig>
      <ex_tran xml:lang="fa">تا خرس را دید به نزدیک‌ترین درخت پناه برد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>جای گرفتن، مستقر شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a seat in the rear</ex_orig>
      <ex_tran xml:lang="fa">در عقب (یک محل) جای گرفتن (نشستن)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the president took the chair</ex_orig>
      <ex_tran xml:lang="fa">رییس جمهور بر مسند نشست.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she is always ready to take the spotlight</ex_orig>
      <ex_tran xml:lang="fa">او برای این‌که مرکز توجه باشد همیشه آمادگی دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(وقت و غیره) صرف کردن، گرفتن، طول کشیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">writing this dictionary will take six years</ex_orig>
      <ex_tran xml:lang="fa">نگارش این فرهنگ شش سال طول خواهد کشید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">it takes a lot of time</ex_orig>
      <ex_tran xml:lang="fa">خیلی وقت می‌گیرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>نیاز داشتن، لازم داشتن، مستلزم بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">it takes money to travel</ex_orig>
      <ex_tran xml:lang="fa">سفر کردن پول لازم دارد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">it takes courage to do what he did</ex_orig>
      <ex_tran xml:lang="fa">کاری که او کرد به شجاعت نیاز دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(به ارث) بردن، (به کسی) رفتن، (اسم یا لقب و غیره) گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">he takes after his father</ex_orig>
      <ex_tran xml:lang="fa">او به پدرش رفته است.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>نقل کردن، نقل قول کردن، گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a verse from the Bible</ex_orig>
      <ex_tran xml:lang="fa">سوره‌ای از انجیل را نقل کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>- کردن، – برداشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to take a poll</ex_orig>
      <ex_tran xml:lang="fa">نظر خواهی عمومی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a vote</ex_orig>
      <ex_tran xml:lang="fa">رای گیری کردن، رای گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take notes</ex_orig>
      <ex_tran xml:lang="fa">نت برداشتن، یادداشت کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take attendance</ex_orig>
      <ex_tran xml:lang="fa">حاضر غایب کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take inventory</ex_orig>
      <ex_tran xml:lang="fa">صورت موجودی برداشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a copy of a will</ex_orig>
      <ex_tran xml:lang="fa">از وصیت نامه نسخه برداشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take pictures</ex_orig>
      <ex_tran xml:lang="fa">عکس برداشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a person's fingerprints</ex_orig>
      <ex_tran xml:lang="fa">کسی را انگشت نگاری کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take part in an activity</ex_orig>
      <ex_tran xml:lang="fa">در کاری شرکت کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a leave of absence</ex_orig>
      <ex_tran xml:lang="fa">مرخصی گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a walk</ex_orig>
      <ex_tran xml:lang="fa">پیاده‌روی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a music course</ex_orig>
      <ex_tran xml:lang="fa">کلاس موسیقی گرفتن (انتخاب کردن)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a rest</ex_orig>
      <ex_tran xml:lang="fa">استراحت کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take the room's measurements</ex_orig>
      <ex_tran xml:lang="fa">اتاق را اندازه گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take notice</ex_orig>
      <ex_tran xml:lang="fa">توجه کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پذیرفتن، پذیرا بودن، قبول کردن، تحمل کردن، تاب داشتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">take my advice!</ex_orig>
      <ex_tran xml:lang="fa">پند مرا بپذیر!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take a bet</ex_orig>
      <ex_tran xml:lang="fa">شرط بندی (قبول) کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took my joke seriously</ex_orig>
      <ex_tran xml:lang="fa">او شوخی مرا جدی گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took his punishment like a man</ex_orig>
      <ex_tran xml:lang="fa">مثل مرد تنبیه خود را قبول کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">this plant takes cold weather beautifully</ex_orig>
      <ex_tran xml:lang="fa">این گیاه در هوای سرد خوب تاب می‌آورد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>فهمیدن، درک کردن، پی بردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">his hearers were slow to take his meaning</ex_orig>
      <ex_tran xml:lang="fa">شنودگان زود به منظور او پی نبردند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she took my hint immediately</ex_orig>
      <ex_tran xml:lang="fa">فورا به اشارهٔ من پی برد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(با خود یا به محلی) بردن، حمل کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">God will take the ship where he pleases ...</ex_orig>
      <ex_tran xml:lang="fa">برد کشتی آنجا که خواهد خدای ...</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took his wife to a doctor</ex_orig>
      <ex_tran xml:lang="fa">زنش را پیش دکتر برد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">will you take me to a movie?</ex_orig>
      <ex_tran xml:lang="fa">مرا به سینما می‌بری؟</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">he took the whole family to dinner</ex_orig>
      <ex_tran xml:lang="fa">همهٔ خانواده را برد به شام.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I took them to London</ex_orig>
      <ex_tran xml:lang="fa">آنها را به لندن بردم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">this road will take you to the center of the city</ex_orig>
      <ex_tran xml:lang="fa">این راه شما را به مرکز شهر خواهد برد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>کشتن، تباه کردن، نابود کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">cruel fate took him from us</ex_orig>
      <ex_tran xml:lang="fa">سرنوشت قدار او را از ما گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">cancer takes many lives</ex_orig>
      <ex_tran xml:lang="fa">سرطان خیلی‌ها را می‌کشد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>کسر کردن، کاستن، منها کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">nothing took from the scene's beauty</ex_orig>
      <ex_tran xml:lang="fa">هیچ‌چیز از زیبایی آن صحنه نمی‌کاست.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">take three from five</ex_orig>
      <ex_tran xml:lang="fa">سه را از پنج کسر کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(قلمه یا پیوند یا آتش و غیره) گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">most of this surgeon's grafts take</ex_orig>
      <ex_tran xml:lang="fa">اکثر پیوندهایی که این جراح می‌زند می‌گیرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the wick was wet and the sparks didn't take</ex_orig>
      <ex_tran xml:lang="fa">فتیله تر بود و جرقه‌ها نگرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the fire took rapidly</ex_orig>
      <ex_tran xml:lang="fa">آتش به سرعت گرفت (روشن شد).</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the vaccination took</ex_orig>
      <ex_tran xml:lang="fa">واکسن گرفت.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پنداشتن، به جای کسی یا چیزی دیگر گرفتن</dtrn>
    <ex>
      <ex_orig xml:lang="en">I took her to be a teacher</ex_orig>
      <ex_tran xml:lang="fa">فکر کردم که او معلم است.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>عمل گرفتن، در دست گیری، تسخیر، تصاحب، گرفت، گیرش</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>میزان گرفته شده یا صید شده یا بدست آوری شده</dtrn>
    <ex>
      <ex_orig xml:lang="en">a day's take of fish</ex_orig>
      <ex_tran xml:lang="fa">مقدار ماهی صید شده در یک روز</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>دریافتی (ها)، مبالغ واریز شده، کسب، سود، درآمد</dtrn>
    <ex>
      <ex_orig xml:lang="en">to increase the city's take from gambling</ex_orig>
      <ex_tran xml:lang="fa">درآمد شهر از محل قماربازی را بیشتر کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>واکسنی که می‌گیرد (اثر می‌کند)</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>(عکسبرداری و فیلمبرداری) برداشت</dtrn>
    <ex>
      <ex_orig xml:lang="en">* on the take</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">رشوه گیر، دارای درآمد غیر مشروع</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a cop who is on the take</ex_orig>
      <ex_tran xml:lang="fa">پاسبانی که درآمد نامشروع دارد</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take after</ex_orig>
      <ex_tran xml:lang="fa">1- (به کسی) رفتن، شباهت داشتن 2- (کسی را) تعقیب کردن، دنبال کسی راه افتادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take a meeting</ex_orig>
      <c c="gray">خودمانی</c>
      <ex_tran xml:lang="fa">در کنفرانس حضور یافتن، به جلسه رفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take a miss</ex_orig>
      <ex_tran xml:lang="fa">1- (در اصل) اشتباه کردن، عوضی گرفتن 2- درست درک نکردن، سو تفاهم پیدا کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take back</ex_orig>
      <ex_tran xml:lang="fa">1- پس گرفتن (چیزی یا حرفی یا ادعایی) 2- پس دادن (چیزی خریداری شده)، پس بردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take down</ex_orig>
      <ex_tran xml:lang="fa">1- یادداشت کردن 2- در جای پایین‌تر قرار دادن، تنزل دادن، پایین بردن 3- (شلوار و غیره) پایین کشیدن 4- خوار کردن، خفیف کردن، پست کردن 5- از هم باز کردن، پیاده کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take five (or ten, etc)</ex_orig>
      <ex_tran xml:lang="fa">(آمریکا- عامیانه) استراحت پنج دقیقه‌ای (یا ده دقیقه‌ای و غیره) کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take for</ex_orig>
      <ex_tran xml:lang="fa">1- پنداشتن، تصور کردن، پذیرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I took him for an American</ex_orig>
      <ex_tran xml:lang="fa">فکر کردم که آمریکایی است.</ex_tran>
      <ex_tran xml:lang="fa">2- عوضی (به جای کس دیگر) گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take in</ex_orig>
      <ex_tran xml:lang="fa">1- راه دادن، پذیرفتن، پذیرا شدن 2- (لباس یا بادبان کشتی و غیره) تو گرفتن، کوچک کردن 3- شامل بودن، حاوی بودن 4- درک‌کردن، فهمیدن 5- گول زدن، فریب دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">don't be taken in by his tempting promises!</ex_orig>
      <ex_tran xml:lang="fa">گول وعده‌های وسوسه انگیز او را نخور!</ex_tran>
      <ex_tran xml:lang="fa">6- دیدار کردن، بازدید کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to take in all the historical sights</ex_orig>
      <ex_tran xml:lang="fa">همهٔ جاهای تاریخی را بازدید کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it</ex_orig>
      <ex_tran xml:lang="fa">1- فکر کردن، پنداشتن، تصور کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I take it he is her brother</ex_orig>
      <ex_tran xml:lang="fa">فکر می‌کنم او برادرش باشد.</ex_tran>
      <ex_tran xml:lang="fa">2- تحمل کردن، تاب آوردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I am tired of this job; I can't take it any more!</ex_orig>
      <ex_tran xml:lang="fa">از این شغل بیزارم و دیگر تاب تحمل آن را ندارم!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it easy!</ex_orig>
      <ex_tran xml:lang="fa">سخت نگیر</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it from me</ex_orig>
      <ex_tran xml:lang="fa">باور کن، به حرفم اعتماد کن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it or leave it</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">می‌خواهی بخواه و نمی‌خواهی نخواه، همین است که هست</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it out of</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">1- خسته کردن، فرسودن 2- تقاص گرفتن، پول در کشیدن (از)، غرامت گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take it out on</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">تلافی کاری را سر شخص ثالث درآوردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I know you've been fired from your office but don't take it out on the children!</ex_orig>
      <ex_tran xml:lang="fa">می‌دانم که از اداره اخراجت کرده‌اند ولی تلافی‌اش را سربچه‌ها در نیاور!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take off</ex_orig>
      <ex_tran xml:lang="fa">1- (جامه) در آوردن، کندن 2- (کلاه و عینک و غیره) برداشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">please take off your hat</ex_orig>
      <ex_tran xml:lang="fa">لطفا کلاه خود را بردارید.</ex_tran>
      <ex_tran xml:lang="fa">3- عزیمت کردن، رفتن 4- (کار یا مدرسه) غیبت کردن، غایب شدن 5- کشتن 6- کسر کردن، کاستن، تخفیف دادن 7- کپی کردن، نسخه‌برداشتن 8- پرزدن، پرواز کردن 9- شروع کردن، آغاز کردن 10- (هواپیما) بلند شدن از زمین 11- (با: on) تقلید کردن، تقلید در آوردن 12- (عامیانه) موفق شدن، گل کردن، (کار و بار) گرفتن 13- (خودمانی) دزدیدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take on</ex_orig>
      <ex_tran xml:lang="fa">1- به خود گرفتن، شکل گرفتن، رنگ گرفتن، قوام گرفتن 2- استخدام کردن، به کار گرفتن 3- به عهده گرفتن، تقبل کردن 4- به مبارزه‌طلبیدن، از پس کسی یا چیزی برآمدن، مقابله کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take one's time</ex_orig>
      <ex_tran xml:lang="fa">باتانی کار کردن، وقت کافی صرف کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take out</ex_orig>
      <ex_tran xml:lang="fa">1- کسر کردن، کاستن 2- درآوردن، کشیدن (بیرون) 3- (با پر کردن درخواست و غیره وام و غیره) گرفتن، به دست آوردن 4-(عامیانه) همراهی کردن، (به محلی) بردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take over</ex_orig>
      <ex_tran xml:lang="fa">به عهده گرفتن، تصدی چیزی را قبول کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take place</ex_orig>
      <ex_tran xml:lang="fa">به وقوع پیوستن، روی دادن، رخ دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take sides</ex_orig>
      <ex_tran xml:lang="fa">طرفداری کردن، یک طرف را گرفتن، سوگیری کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take something easy</ex_orig>
      <ex_tran xml:lang="fa">سخت نگرفتن، سخت‌گیری نکردن، آسان گرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take to</ex_orig>
      <ex_tran xml:lang="fa">1- عادت کردن، خوگرفتن 2- پناه بردن به، (به محلی) رفتن 3- (به کار یا مطالعه و غیره) پرداختن 4- (از کسی) خوش آمدن، به دل راه‌دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take up</ex_orig>
      <ex_tran xml:lang="fa">1- افراشتن، بلند کردن، بالابردن 2- (لباس و غیره) تو گرفتن، کوتاه کردن، تنگ کردن 3- جذب کردن، در آشامیدن 4- پذیرفتن، به عهده‌گرفتن 5- ادامه دادن 6- علاقمند شدن به 7- جاگرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take upon (or on) oneself</ex_orig>
      <ex_tran xml:lang="fa">1- مسئولیت کاری را پذیرفتن، به عهده گرفتن، تقبل کردن 2- انجام کاری را آغاز کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take up with</ex_orig>
      <c c="gray">عامیانه</c>
      <ex_tran xml:lang="fa">دوست کسی شدن، همدم شدن، هم‌نشینی کردن</ex_tran>
    </ex>
  </def>
</def>
```

## 43. turn

TEI source: `21-t.xml` entry 3685 (score 350, rare 0)  
XDXF article: `en-fa.xdxf` # 43 (key `turn`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>turn</orth>
  <pron>tu_rn</pron>
</form>
```

XDXF:

```xml
<k>turn</k>
<tr>tu_rn</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="transitive verb">فعل متعدی</pos>
    <pos norm="intransitive verb">فعل لازم</pos>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>چرخاندن، گرداندن، به گردش درآوردن، به چرخش درآوردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn the key in a lock</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کلید را در قفل چرخاندن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the motor turns the wheel</quote>
      <cit type="trans" xml:lang="fa">
        <quote>موتور چرخ را به گردش درمی‌آورد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she turned her eyes in my direction</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چشمان خود را به سوی من چرخاند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Mahmood turned his back on me</quote>
      <cit type="trans" xml:lang="fa">
        <quote>محمود پشتش را به من کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn the door handle</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دستهٔ در را چرخاندن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تراش دادن، خراطی کردن، (با چرخاندن) ساختن، شکل دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn several table legs</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چندین پایهٔ میز خراطی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn a pretty phrase</quote>
      <cit type="trans" xml:lang="fa">
        <quote>عبارت زیبایی را تصنیف کردن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پیچاندن، پیچ دادن، تاباندن، تاب دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn a screw</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیچ را پیچاندن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Amjadi turns the ends of his mustache up</quote>
      <cit type="trans" xml:lang="fa">
        <quote>امجدی انتهای سبیل خود را به بالا تاب می‌دهد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>ورق زدن، (صفحه و غیره) برگرداندن، پشت و رو کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn the pages of a book</quote>
      <cit type="trans" xml:lang="fa">
        <quote>صفحات یک کتاب را ورق زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn a phonograph record</quote>
      <cit type="trans" xml:lang="fa">
        <quote>صفحهٔ گرامافون را پشت و رو کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">before planting we must turn over the soil with a shovel</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیش از کشت باید خاک را با بیل پشت و رو کنیم (شخم بزنیم).</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">fry the fish for three minutes, then turn it and fry the other side</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ماهی را سه دقیقه سرخ بکن و سپس آن را پشت و رو کرده و طرف دیگر را سرخ کن.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>وارونه کردن یا شدن، معکوس کردن یا شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she turned the bottle upside down</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بطری را وارونه کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(معده را) به هم زدن، به حال تهوع درآوردن یا درآمدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">when I saw the putrid food my stomach turned</quote>
      <cit type="trans" xml:lang="fa">
        <quote>وقتی که آن خوراک متعفن را دیدم دلم به هم خورد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(در مقابل ضربه و غیره) جاخالی دادن، منحرف کردن یا شدن، منصرف کردن یا شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn a blow</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در مقابل ضربه جاخالی دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn someone from his purpose</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کسی را از هدف خود منصرف کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">do not turn from the path of righteousness!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>از مسیر تقوا منحرف نشوید!</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تا کردن، خماندن، تو گذاشتن، دولا کردن یا شدن</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دور زدن</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(مبلغ یا سن و غیره) رسیدن، (بالغ) شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">tomorrow he is going to turn fifty</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فردا پنجاه ساله خواهد شد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پس زدن، متوقف کردن، برگرداندن، دفع کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn an attack</quote>
      <cit type="trans" xml:lang="fa">
        <quote>حمله را پس زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the criticism turned against the critic himself</quote>
      <cit type="trans" xml:lang="fa">
        <quote>انتقاد متوجه خود انتقاد کننده شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">we turned back an enemy attack</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ما حملهٔ دشمن را دفع کردیم.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(رها یا آزاد و غیره) کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the rebels turned the political prisoners loose</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شورشیان، زندانیان سیاسی را آزاد کردند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>معطوف کردن، متوجه کردن، برگشت دادن، به کار زدن، پرداختن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Ali turned his gun on us</quote>
      <cit type="trans" xml:lang="fa">
        <quote>علی تپانچه‌اش را به طرف ما گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn one's thoughts to monetary matters</quote>
      <cit type="trans" xml:lang="fa">
        <quote>افکار خود را به امور پولی معطوف کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn one's hand to writing</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به نگارش دست زدن (پرداختن)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">later on he turned his attention to music</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بعدا توجه خود را به موسیقی معطوف کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn knowledge to good account</quote>
      <cit type="trans" xml:lang="fa">
        <quote>علم را در امور خیر بکار زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">as his debts increased, he turned to crime</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چون بدهی‌های او زیاد شد دست به تبهکاری زد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تبدیل کردن یا شدن، – شدن، – کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn bitter with age</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در اثر کهنگی تلخ شدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn cream into butter</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سرشیر را تبدیل به کره کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn produce into hard cash</quote>
      <cit type="trans" xml:lang="fa">
        <quote>محصول کشاورزی را تبدیل به پول نقد کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a writer turned actor</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نویسنده‌ای که هنرپیشه شده است</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">turned sick by the sight</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دچار حالت تهوع در اثر دیدن آن منظره</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">water turns into ice</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آب تبدیل به یخ می‌شود.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn Hassan's remarks to ridicule</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گفته‌های حسن را مورد تمسخر قرار دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Asghar turned against his former friends</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اصغر با دوستان سابق خود ضدیت کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>ترجمه کردن یا شدن، (به زبان یا بیان دیگری) برگرداندن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">my father turned Hafez' poems into English</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پدرم اشعار حافظ را به انگلیسی ترجمه کرد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Attar turned that story into a poem</quote>
      <cit type="trans" xml:lang="fa">
        <quote>عطار آن داستان را به شعر برگرداند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دیوانه کردن، مجنون کردن، مفتون کردن، شیفته کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">too much success has turned his head</quote>
      <cit type="trans" xml:lang="fa">
        <quote>موفقیت زیاد به سرش زده است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">her mind has been turned by grief</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اندوه او را دیوانه کرده است.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(شیر و کره و غیره) ترشیدن، ترشاندن، ترش شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">after a while, the milk started turning</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پس از مدتی شیر شروع به ترشیدگی کرد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رنگ (چیزی را) عوض کردن، رنگ پریده کردن یا شدن، رنگ به رنگ کردن یا شدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">leaves turn in the fall</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در پاییز برگ‌ها رنگ عوض می‌کنند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>چرخیدن، دور زدن، گشتن، گردیدن، به گردش درآمدن، پیچیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the key won't turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کلید نمی‌چرخد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the car turned left and then right</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اتومبیل به سمت چپ و سپس به سمت راست پیچید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">my head ached and the room was turning around my head</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سرم درد می‌کرد و اتاق دور سرم می‌چرخید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">turn right at the end of the street</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در انتهای خیابان به دست راست بپیچید.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the teacher's head turned toward me</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سر معلم به سوی من چرخید.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>خم شدن، خمیدن، انحنا پیدا کردن، قوسدار شدن، پیچیدن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">turn left at the next intersection</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در چهار راه بعدی به طرف چپ بپیچید.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>غلت زدن، تریدن، قل خوردن، قل دادن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the child tossed and turned all night</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کودک تمام شب تکان می‌خورد و غلت می‌زد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>برگشتن، عقبگرد کردن، تغییر جهت دادن، عوض شدن، دگرگون شدن یا کردن، عوض کردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the tide has turned</quote>
      <cit type="trans" xml:lang="fa">
        <quote>کشند برگشته است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the situation has turned in his favor</quote>
      <cit type="trans" xml:lang="fa">
        <quote>اوضاع به سود او تغییر کرده است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the wind turned</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جهت باد عوض شد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his luck has turned</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بخت از او برگشته است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn on one's heels</quote>
      <cit type="trans" xml:lang="fa">
        <quote>ناگهان عقبگرد کردن (بازگشتن)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">an event that turned the course of history</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رویدادی که مسیر تاریخ را عوض کرد</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رجوع کردن به، مراجعه کردن، پناه بردن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">she has no one to turn to</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او پشت و پناهی ندارد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">they turn to the government for help</quote>
      <cit type="trans" xml:lang="fa">
        <quote>آنان برای کمک به دولت متوسل می‌شوند.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(ناگهان) حمله کردن، پریدن به</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the dog turned on him</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سگ پرید به او.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(با: on یا upon) بستگی داشتن به، منوط بودن</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">our fate turned on the whims of the captain</quote>
      <cit type="trans" xml:lang="fa">
        <quote>سرنوشت ما به هوس‌های ناخدا بستگی داشت.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>چرخش، گردش</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">no left turn (is allowed)</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گردش به چپ ممنوع (است)</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">don't pull the handle; give it a turn!</quote>
      <cit type="trans" xml:lang="fa">
        <quote>دسته را نکش؛ آن را یک چرخ بده!</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">make a left turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به سمت چپ بچرخ (برو).</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پیچش، پیچ، تاب</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a sharp turn in the road</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیچ تند جاده</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the story has many twists and turns</quote>
      <cit type="trans" xml:lang="fa">
        <quote>داستان پیچ و تاب فراوان دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>قوس‌داری، انحنا، خمش، کژی، خم</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he went around the turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او پیچ را دور زد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the river has many turns</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رودخانه پیچ و خم زیاد دارد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جهت چرخش یا انحنا</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تغییر جهت، انحراف</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the turn of the tide</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تغییر جهت کشند (یا موج)</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(پیاده‌روی و غیره) دور، دورزنی، گشت، گلگشت</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">he took another turn around the garden</quote>
      <cit type="trans" xml:lang="fa">
        <quote>او یک بار دیگر دور باغ گشت زد.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دگرگونی، تغییر</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">at the turn of this century</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در آغاز این قرن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a turn for the better</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تغییر در جهت خوب</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رجوع شود به: <ref>turning point</ref>
      </quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>تکان، یکه، شوک</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>عمل، کار</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to do someone a good turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>برای کسی عمل خیر انجام دادن</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(سرگیجه یا خشم یا بیماری) حمله، بروز</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دوره، نوبت</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">it is not your turn yet</quote>
      <cit type="trans" xml:lang="fa">
        <quote>هنوز نوبت تو نیست.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">it is my turn to sing</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نوبت آواز خواندن من است.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">you missed your turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نوبت خود را از دست دادی.</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>نمایش کوتاه</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>(بورس سهام) خرید و فروش، دست به دست گشتن</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>لحن، فحوا، نحوه، طرز</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a quaint turn to her speech</quote>
      <cit type="trans" xml:lang="fa">
        <quote>لحن عجیب و غریب حرف زدن او</quote>
      </cit>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>گرایش، تمایل، استعداد، جهت، سوی</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">an inquisitive turn of mind</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تمایل (تفکری) به کنجکاوی</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the discussion took a new turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بحث مسیر تازه‌ای را به خود گرفت.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to give an old story a new turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به یک داستان قدیمی سر و صورت تازه‌ای دادن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">turn of events</quote>
      <cit type="trans" xml:lang="fa">
        <quote>گرایش رویدادها</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* at every turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>در همهٔ حالات، در کلیهٔ آزمایش‌ها، دائما، همیشه</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* by turns</quote>
      <cit type="trans" xml:lang="fa">
        <quote>یکی پس از دیگری، به نوبت، متناوبا</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* call the turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>درست پیش‌بینی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* in turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به نوبت، به ترتیب، به طور منظم</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* out of turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- خارج از نوبت، به طور غیر مرتب 2- نابهنگام، بی‌موقع، نسنجیده</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to talk out of turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نسنجیده حرف زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take a turn for the better (or worse)</quote>
      <cit type="trans" xml:lang="fa">
        <quote>(به ویژه بیماری) رو به بهبود (یا وخامت) گذاشتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* take turns</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به نوبت (کاری را) انجام دادن، نوبتی کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* to a turn</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به نحو احسن، به بهترین طریق، عالی، بسیار خوب</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn and turn about (or turn about)</quote>
      <cit type="trans" xml:lang="fa">
        <quote>به نوبت، به طور مرتب و منظم</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn down</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- رد کردن، قبول نکردن، نپذیرفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">our offer was turned down</quote>
      <cit type="trans" xml:lang="fa">
        <quote>پیشنهاد ما رد شد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- (صدای رادیو و غیره یا نور چراغ و غیره را) کم کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I turned down the radio</quote>
      <cit type="trans" xml:lang="fa">
        <quote>صدای رادیو را کم کردم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn in</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- وارد شدن، داخل شدن 2- تحویل دادن، سپردن، دادن 3- پس دادن، اعاده کردن 4- تا کردن، دولا کردن، تو گذاشتن 5- (عامیانه) به‌بستر رفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">Farhad turned in his resignation</quote>
      <cit type="trans" xml:lang="fa">
        <quote>فرهاد استعفای خود را داد.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">our children turned in earlier</quote>
      <cit type="trans" xml:lang="fa">
        <quote>بچه‌های ما زودتر به رختخواب رفتند.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn off</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (از جادهٔ اصلی به جادهٔ فرعی) پیچیدن 2- (راه و غیره) منشعب شدن 3- (جریان چیزی را) بند آوردن، قطع کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn off the electricity</quote>
      <cit type="trans" xml:lang="fa">
        <quote>برق را قطع کردن</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>4- (موتور و غیره) خاموش کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn off the television</quote>
      <cit type="trans" xml:lang="fa">
        <quote>تلویزیون را خاموش کردن</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>5- منحرف کردن، کنار زدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">his angry tone turned us off</quote>
      <cit type="trans" xml:lang="fa">
        <quote>لحن خشم‌آلود او ما را دلزده کرد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>6- (آمریکا – خودمانی) دلسرد کردن، دلزده کردن، بی‌علاقه کردن، ملول کردن، خسته کردن 7- (انگلیس – کارمند را) اخراج کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- (جریان آب یا گاز و غیره را) باز کردن 2- (رادیو یا تلویزیون و غیره را) روشن کردن 3- (خودمانی) نشئه کردن، (با مواد مخدر) سرکیف آوردن 4- شهوتی کردن، تحریک جنسی کردن 5- سرشوق آوردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn on the faucet</quote>
      <cit type="trans" xml:lang="fa">
        <quote>شیر آب را باز کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">I tarned the lights on</quote>
      <cit type="trans" xml:lang="fa">
        <quote>چراغ‌ها را روشن کردم.</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn out</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- انجامیدن، شدن، از آب در آمدن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">how did the meeting turn out?</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جلسهٔ ملاقات به کجا انجامید؟</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">the servant turned out to be a thief</quote>
      <cit type="trans" xml:lang="fa">
        <quote>نوکر دزد از آب درآمد.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>2- (چراغ) خاموش کردن 3- خارج گذاشتن، در بیرون قرار دادن 4- بیرون کردن، اخراج کردن، مرخص کردن 5- پشت و رو کردن 6-خارج شدن، رفتن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">a huge crowd turned out to welcome him</quote>
      <cit type="trans" xml:lang="fa">
        <quote>جمعیت عظیمی به پیشواز او رفتند.</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>7- تولید کردن 8- (از بستر) خارج شدن، برخاستن 9- مجهز کردن، ملبس کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn over</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- غلت زدن، جابجا کردن یا شدن، دفتی زدن 2- وارونه کردن، بالا و پایین کردن، پشت و رو کردن 3- (موتور و غیره) روشن کردن، به‌کار انداختن 4- مورد تفکر قرار دادن، سبک و سنگین کردن 5- مسترد کردن، دادن 6- احاله کردن، صرفنظر کردن 7- تبدیل کردن 8-خرید و فروش کردن، داد و ستد کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn to</quote>
      <cit type="trans" xml:lang="fa">
        <quote>مشغول شدن، دست به کار شدن، (به کاری) پرداختن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">* turn up</quote>
      <cit type="trans" xml:lang="fa">
        <quote>1- دولا کردن، بالا زدن و دوختن، تو گرفتن، کوتاه کردن (لباس) 2- نمودار کردن، کشف کردن، پدیدار کردن 3- (جریان یا صدای‌چیزی را) زیاد کردن، بلند کردن</quote>
      </cit>
    </cit>
    <cit type="example">
      <quote xml:lang="en">to turn up the radio</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رادیو را بلند کردن</quote>
      </cit>
      <cit type="trans" xml:lang="fa">
        <quote>4- (در جادهٔ فرعی) پیچیدن 5- سیر صعودی داشتن، بالا رفتن 6- روی دادن 7- یافت شدن 8- پدیدار شدن، سررسیدن</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>فعل متعدی</pos>
  <pos>فعل لازم</pos>
  <pos>اسم</pos>
  <def xml:lang="fa">
    <dtrn>چرخاندن، گرداندن، به گردش درآوردن، به چرخش درآوردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn the key in a lock</ex_orig>
      <ex_tran xml:lang="fa">کلید را در قفل چرخاندن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the motor turns the wheel</ex_orig>
      <ex_tran xml:lang="fa">موتور چرخ را به گردش درمی‌آورد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">she turned her eyes in my direction</ex_orig>
      <ex_tran xml:lang="fa">چشمان خود را به سوی من چرخاند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Mahmood turned his back on me</ex_orig>
      <ex_tran xml:lang="fa">محمود پشتش را به من کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn the door handle</ex_orig>
      <ex_tran xml:lang="fa">دستهٔ در را چرخاندن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>تراش دادن، خراطی کردن، (با چرخاندن) ساختن، شکل دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn several table legs</ex_orig>
      <ex_tran xml:lang="fa">چندین پایهٔ میز خراطی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn a pretty phrase</ex_orig>
      <ex_tran xml:lang="fa">عبارت زیبایی را تصنیف کردن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پیچاندن، پیچ دادن، تاباندن، تاب دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn a screw</ex_orig>
      <ex_tran xml:lang="fa">پیچ را پیچاندن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Amjadi turns the ends of his mustache up</ex_orig>
      <ex_tran xml:lang="fa">امجدی انتهای سبیل خود را به بالا تاب می‌دهد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>ورق زدن، (صفحه و غیره) برگرداندن، پشت و رو کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn the pages of a book</ex_orig>
      <ex_tran xml:lang="fa">صفحات یک کتاب را ورق زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn a phonograph record</ex_orig>
      <ex_tran xml:lang="fa">صفحهٔ گرامافون را پشت و رو کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">before planting we must turn over the soil with a shovel</ex_orig>
      <ex_tran xml:lang="fa">پیش از کشت باید خاک را با بیل پشت و رو کنیم (شخم بزنیم).</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">fry the fish for three minutes, then turn it and fry the other side</ex_orig>
      <ex_tran xml:lang="fa">ماهی را سه دقیقه سرخ بکن و سپس آن را پشت و رو کرده و طرف دیگر را سرخ کن.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>وارونه کردن یا شدن، معکوس کردن یا شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she turned the bottle upside down</ex_orig>
      <ex_tran xml:lang="fa">بطری را وارونه کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(معده را) به هم زدن، به حال تهوع درآوردن یا درآمدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">when I saw the putrid food my stomach turned</ex_orig>
      <ex_tran xml:lang="fa">وقتی که آن خوراک متعفن را دیدم دلم به هم خورد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(در مقابل ضربه و غیره) جاخالی دادن، منحرف کردن یا شدن، منصرف کردن یا شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn a blow</ex_orig>
      <ex_tran xml:lang="fa">در مقابل ضربه جاخالی دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn someone from his purpose</ex_orig>
      <ex_tran xml:lang="fa">کسی را از هدف خود منصرف کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">do not turn from the path of righteousness!</ex_orig>
      <ex_tran xml:lang="fa">از مسیر تقوا منحرف نشوید!</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>تا کردن، خماندن، تو گذاشتن، دولا کردن یا شدن</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>دور زدن</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>(مبلغ یا سن و غیره) رسیدن، (بالغ) شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">tomorrow he is going to turn fifty</ex_orig>
      <ex_tran xml:lang="fa">فردا پنجاه ساله خواهد شد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پس زدن، متوقف کردن، برگرداندن، دفع کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn an attack</ex_orig>
      <ex_tran xml:lang="fa">حمله را پس زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the criticism turned against the critic himself</ex_orig>
      <ex_tran xml:lang="fa">انتقاد متوجه خود انتقاد کننده شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">we turned back an enemy attack</ex_orig>
      <ex_tran xml:lang="fa">ما حملهٔ دشمن را دفع کردیم.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(رها یا آزاد و غیره) کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the rebels turned the political prisoners loose</ex_orig>
      <ex_tran xml:lang="fa">شورشیان، زندانیان سیاسی را آزاد کردند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>معطوف کردن، متوجه کردن، برگشت دادن، به کار زدن، پرداختن</dtrn>
    <ex>
      <ex_orig xml:lang="en">Ali turned his gun on us</ex_orig>
      <ex_tran xml:lang="fa">علی تپانچه‌اش را به طرف ما گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn one's thoughts to monetary matters</ex_orig>
      <ex_tran xml:lang="fa">افکار خود را به امور پولی معطوف کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn one's hand to writing</ex_orig>
      <ex_tran xml:lang="fa">به نگارش دست زدن (پرداختن)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">later on he turned his attention to music</ex_orig>
      <ex_tran xml:lang="fa">بعدا توجه خود را به موسیقی معطوف کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn knowledge to good account</ex_orig>
      <ex_tran xml:lang="fa">علم را در امور خیر بکار زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">as his debts increased, he turned to crime</ex_orig>
      <ex_tran xml:lang="fa">چون بدهی‌های او زیاد شد دست به تبهکاری زد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>تبدیل کردن یا شدن، – شدن، – کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">to turn bitter with age</ex_orig>
      <ex_tran xml:lang="fa">در اثر کهنگی تلخ شدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn cream into butter</ex_orig>
      <ex_tran xml:lang="fa">سرشیر را تبدیل به کره کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn produce into hard cash</ex_orig>
      <ex_tran xml:lang="fa">محصول کشاورزی را تبدیل به پول نقد کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a writer turned actor</ex_orig>
      <ex_tran xml:lang="fa">نویسنده‌ای که هنرپیشه شده است</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">turned sick by the sight</ex_orig>
      <ex_tran xml:lang="fa">دچار حالت تهوع در اثر دیدن آن منظره</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">water turns into ice</ex_orig>
      <ex_tran xml:lang="fa">آب تبدیل به یخ می‌شود.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn Hassan's remarks to ridicule</ex_orig>
      <ex_tran xml:lang="fa">گفته‌های حسن را مورد تمسخر قرار دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Asghar turned against his former friends</ex_orig>
      <ex_tran xml:lang="fa">اصغر با دوستان سابق خود ضدیت کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>ترجمه کردن یا شدن، (به زبان یا بیان دیگری) برگرداندن</dtrn>
    <ex>
      <ex_orig xml:lang="en">my father turned Hafez' poems into English</ex_orig>
      <ex_tran xml:lang="fa">پدرم اشعار حافظ را به انگلیسی ترجمه کرد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Attar turned that story into a poem</ex_orig>
      <ex_tran xml:lang="fa">عطار آن داستان را به شعر برگرداند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>دیوانه کردن، مجنون کردن، مفتون کردن، شیفته کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">too much success has turned his head</ex_orig>
      <ex_tran xml:lang="fa">موفقیت زیاد به سرش زده است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">her mind has been turned by grief</ex_orig>
      <ex_tran xml:lang="fa">اندوه او را دیوانه کرده است.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(شیر و کره و غیره) ترشیدن، ترشاندن، ترش شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">after a while, the milk started turning</ex_orig>
      <ex_tran xml:lang="fa">پس از مدتی شیر شروع به ترشیدگی کرد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>رنگ (چیزی را) عوض کردن، رنگ پریده کردن یا شدن، رنگ به رنگ کردن یا شدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">leaves turn in the fall</ex_orig>
      <ex_tran xml:lang="fa">در پاییز برگ‌ها رنگ عوض می‌کنند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>چرخیدن، دور زدن، گشتن، گردیدن، به گردش درآمدن، پیچیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the key won't turn</ex_orig>
      <ex_tran xml:lang="fa">کلید نمی‌چرخد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the car turned left and then right</ex_orig>
      <ex_tran xml:lang="fa">اتومبیل به سمت چپ و سپس به سمت راست پیچید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">my head ached and the room was turning around my head</ex_orig>
      <ex_tran xml:lang="fa">سرم درد می‌کرد و اتاق دور سرم می‌چرخید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">turn right at the end of the street</ex_orig>
      <ex_tran xml:lang="fa">در انتهای خیابان به دست راست بپیچید.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the teacher's head turned toward me</ex_orig>
      <ex_tran xml:lang="fa">سر معلم به سوی من چرخید.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>خم شدن، خمیدن، انحنا پیدا کردن، قوسدار شدن، پیچیدن</dtrn>
    <ex>
      <ex_orig xml:lang="en">turn left at the next intersection</ex_orig>
      <ex_tran xml:lang="fa">در چهار راه بعدی به طرف چپ بپیچید.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>غلت زدن، تریدن، قل خوردن، قل دادن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the child tossed and turned all night</ex_orig>
      <ex_tran xml:lang="fa">کودک تمام شب تکان می‌خورد و غلت می‌زد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>برگشتن، عقبگرد کردن، تغییر جهت دادن، عوض شدن، دگرگون شدن یا کردن، عوض کردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">the tide has turned</ex_orig>
      <ex_tran xml:lang="fa">کشند برگشته است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the situation has turned in his favor</ex_orig>
      <ex_tran xml:lang="fa">اوضاع به سود او تغییر کرده است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the wind turned</ex_orig>
      <ex_tran xml:lang="fa">جهت باد عوض شد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">his luck has turned</ex_orig>
      <ex_tran xml:lang="fa">بخت از او برگشته است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn on one's heels</ex_orig>
      <ex_tran xml:lang="fa">ناگهان عقبگرد کردن (بازگشتن)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">an event that turned the course of history</ex_orig>
      <ex_tran xml:lang="fa">رویدادی که مسیر تاریخ را عوض کرد</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>رجوع کردن به، مراجعه کردن، پناه بردن</dtrn>
    <ex>
      <ex_orig xml:lang="en">she has no one to turn to</ex_orig>
      <ex_tran xml:lang="fa">او پشت و پناهی ندارد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">they turn to the government for help</ex_orig>
      <ex_tran xml:lang="fa">آنان برای کمک به دولت متوسل می‌شوند.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(ناگهان) حمله کردن، پریدن به</dtrn>
    <ex>
      <ex_orig xml:lang="en">the dog turned on him</ex_orig>
      <ex_tran xml:lang="fa">سگ پرید به او.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(با: on یا upon) بستگی داشتن به، منوط بودن</dtrn>
    <ex>
      <ex_orig xml:lang="en">our fate turned on the whims of the captain</ex_orig>
      <ex_tran xml:lang="fa">سرنوشت ما به هوس‌های ناخدا بستگی داشت.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>چرخش، گردش</dtrn>
    <ex>
      <ex_orig xml:lang="en">no left turn (is allowed)</ex_orig>
      <ex_tran xml:lang="fa">گردش به چپ ممنوع (است)</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">don't pull the handle; give it a turn!</ex_orig>
      <ex_tran xml:lang="fa">دسته را نکش؛ آن را یک چرخ بده!</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">make a left turn</ex_orig>
      <ex_tran xml:lang="fa">به سمت چپ بچرخ (برو).</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>پیچش، پیچ، تاب</dtrn>
    <ex>
      <ex_orig xml:lang="en">a sharp turn in the road</ex_orig>
      <ex_tran xml:lang="fa">پیچ تند جاده</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the story has many twists and turns</ex_orig>
      <ex_tran xml:lang="fa">داستان پیچ و تاب فراوان دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>قوس‌داری، انحنا، خمش، کژی، خم</dtrn>
    <ex>
      <ex_orig xml:lang="en">he went around the turn</ex_orig>
      <ex_tran xml:lang="fa">او پیچ را دور زد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the river has many turns</ex_orig>
      <ex_tran xml:lang="fa">رودخانه پیچ و خم زیاد دارد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>جهت چرخش یا انحنا</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>تغییر جهت، انحراف</dtrn>
    <ex>
      <ex_orig xml:lang="en">the turn of the tide</ex_orig>
      <ex_tran xml:lang="fa">تغییر جهت کشند (یا موج)</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(پیاده‌روی و غیره) دور، دورزنی، گشت، گلگشت</dtrn>
    <ex>
      <ex_orig xml:lang="en">he took another turn around the garden</ex_orig>
      <ex_tran xml:lang="fa">او یک بار دیگر دور باغ گشت زد.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>دگرگونی، تغییر</dtrn>
    <ex>
      <ex_orig xml:lang="en">at the turn of this century</ex_orig>
      <ex_tran xml:lang="fa">در آغاز این قرن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a turn for the better</ex_orig>
      <ex_tran xml:lang="fa">تغییر در جهت خوب</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>رجوع شود به: <kref>turning point</kref>
    </dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>تکان، یکه، شوک</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>عمل، کار</dtrn>
    <ex>
      <ex_orig xml:lang="en">to do someone a good turn</ex_orig>
      <ex_tran xml:lang="fa">برای کسی عمل خیر انجام دادن</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>(سرگیجه یا خشم یا بیماری) حمله، بروز</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>دوره، نوبت</dtrn>
    <ex>
      <ex_orig xml:lang="en">it is not your turn yet</ex_orig>
      <ex_tran xml:lang="fa">هنوز نوبت تو نیست.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">it is my turn to sing</ex_orig>
      <ex_tran xml:lang="fa">نوبت آواز خواندن من است.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">you missed your turn</ex_orig>
      <ex_tran xml:lang="fa">نوبت خود را از دست دادی.</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>نمایش کوتاه</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>(بورس سهام) خرید و فروش، دست به دست گشتن</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>لحن، فحوا، نحوه، طرز</dtrn>
    <ex>
      <ex_orig xml:lang="en">a quaint turn to her speech</ex_orig>
      <ex_tran xml:lang="fa">لحن عجیب و غریب حرف زدن او</ex_tran>
    </ex>
  </def>
  <def xml:lang="fa">
    <dtrn>گرایش، تمایل، استعداد، جهت، سوی</dtrn>
    <ex>
      <ex_orig xml:lang="en">an inquisitive turn of mind</ex_orig>
      <ex_tran xml:lang="fa">تمایل (تفکری) به کنجکاوی</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the discussion took a new turn</ex_orig>
      <ex_tran xml:lang="fa">بحث مسیر تازه‌ای را به خود گرفت.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to give an old story a new turn</ex_orig>
      <ex_tran xml:lang="fa">به یک داستان قدیمی سر و صورت تازه‌ای دادن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">turn of events</ex_orig>
      <ex_tran xml:lang="fa">گرایش رویدادها</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* at every turn</ex_orig>
      <ex_tran xml:lang="fa">در همهٔ حالات، در کلیهٔ آزمایش‌ها، دائما، همیشه</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* by turns</ex_orig>
      <ex_tran xml:lang="fa">یکی پس از دیگری، به نوبت، متناوبا</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* call the turn</ex_orig>
      <ex_tran xml:lang="fa">درست پیش‌بینی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* in turn</ex_orig>
      <ex_tran xml:lang="fa">به نوبت، به ترتیب، به طور منظم</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* out of turn</ex_orig>
      <ex_tran xml:lang="fa">1- خارج از نوبت، به طور غیر مرتب 2- نابهنگام، بی‌موقع، نسنجیده</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to talk out of turn</ex_orig>
      <ex_tran xml:lang="fa">نسنجیده حرف زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take a turn for the better (or worse)</ex_orig>
      <ex_tran xml:lang="fa">(به ویژه بیماری) رو به بهبود (یا وخامت) گذاشتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* take turns</ex_orig>
      <ex_tran xml:lang="fa">به نوبت (کاری را) انجام دادن، نوبتی کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* to a turn</ex_orig>
      <ex_tran xml:lang="fa">به نحو احسن، به بهترین طریق، عالی، بسیار خوب</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn and turn about (or turn about)</ex_orig>
      <ex_tran xml:lang="fa">به نوبت، به طور مرتب و منظم</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn down</ex_orig>
      <ex_tran xml:lang="fa">1- رد کردن، قبول نکردن، نپذیرفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">our offer was turned down</ex_orig>
      <ex_tran xml:lang="fa">پیشنهاد ما رد شد.</ex_tran>
      <ex_tran xml:lang="fa">2- (صدای رادیو و غیره یا نور چراغ و غیره را) کم کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I turned down the radio</ex_orig>
      <ex_tran xml:lang="fa">صدای رادیو را کم کردم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn in</ex_orig>
      <ex_tran xml:lang="fa">1- وارد شدن، داخل شدن 2- تحویل دادن، سپردن، دادن 3- پس دادن، اعاده کردن 4- تا کردن، دولا کردن، تو گذاشتن 5- (عامیانه) به‌بستر رفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">Farhad turned in his resignation</ex_orig>
      <ex_tran xml:lang="fa">فرهاد استعفای خود را داد.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">our children turned in earlier</ex_orig>
      <ex_tran xml:lang="fa">بچه‌های ما زودتر به رختخواب رفتند.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn off</ex_orig>
      <ex_tran xml:lang="fa">1- (از جادهٔ اصلی به جادهٔ فرعی) پیچیدن 2- (راه و غیره) منشعب شدن 3- (جریان چیزی را) بند آوردن، قطع کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn off the electricity</ex_orig>
      <ex_tran xml:lang="fa">برق را قطع کردن</ex_tran>
      <ex_tran xml:lang="fa">4- (موتور و غیره) خاموش کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn off the television</ex_orig>
      <ex_tran xml:lang="fa">تلویزیون را خاموش کردن</ex_tran>
      <ex_tran xml:lang="fa">5- منحرف کردن، کنار زدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">his angry tone turned us off</ex_orig>
      <ex_tran xml:lang="fa">لحن خشم‌آلود او ما را دلزده کرد.</ex_tran>
      <ex_tran xml:lang="fa">6- (آمریکا – خودمانی) دلسرد کردن، دلزده کردن، بی‌علاقه کردن، ملول کردن، خسته کردن 7- (انگلیس – کارمند را) اخراج کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn on</ex_orig>
      <ex_tran xml:lang="fa">1- (جریان آب یا گاز و غیره را) باز کردن 2- (رادیو یا تلویزیون و غیره را) روشن کردن 3- (خودمانی) نشئه کردن، (با مواد مخدر) سرکیف آوردن 4- شهوتی کردن، تحریک جنسی کردن 5- سرشوق آوردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn on the faucet</ex_orig>
      <ex_tran xml:lang="fa">شیر آب را باز کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">I tarned the lights on</ex_orig>
      <ex_tran xml:lang="fa">چراغ‌ها را روشن کردم.</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn out</ex_orig>
      <ex_tran xml:lang="fa">1- انجامیدن، شدن، از آب در آمدن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">how did the meeting turn out?</ex_orig>
      <ex_tran xml:lang="fa">جلسهٔ ملاقات به کجا انجامید؟</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">the servant turned out to be a thief</ex_orig>
      <ex_tran xml:lang="fa">نوکر دزد از آب درآمد.</ex_tran>
      <ex_tran xml:lang="fa">2- (چراغ) خاموش کردن 3- خارج گذاشتن، در بیرون قرار دادن 4- بیرون کردن، اخراج کردن، مرخص کردن 5- پشت و رو کردن 6-خارج شدن، رفتن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">a huge crowd turned out to welcome him</ex_orig>
      <ex_tran xml:lang="fa">جمعیت عظیمی به پیشواز او رفتند.</ex_tran>
      <ex_tran xml:lang="fa">7- تولید کردن 8- (از بستر) خارج شدن، برخاستن 9- مجهز کردن، ملبس کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn over</ex_orig>
      <ex_tran xml:lang="fa">1- غلت زدن، جابجا کردن یا شدن، دفتی زدن 2- وارونه کردن، بالا و پایین کردن، پشت و رو کردن 3- (موتور و غیره) روشن کردن، به‌کار انداختن 4- مورد تفکر قرار دادن، سبک و سنگین کردن 5- مسترد کردن، دادن 6- احاله کردن، صرفنظر کردن 7- تبدیل کردن 8-خرید و فروش کردن، داد و ستد کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn to</ex_orig>
      <ex_tran xml:lang="fa">مشغول شدن، دست به کار شدن، (به کاری) پرداختن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">* turn up</ex_orig>
      <ex_tran xml:lang="fa">1- دولا کردن، بالا زدن و دوختن، تو گرفتن، کوتاه کردن (لباس) 2- نمودار کردن، کشف کردن، پدیدار کردن 3- (جریان یا صدای‌چیزی را) زیاد کردن، بلند کردن</ex_tran>
    </ex>
    <ex>
      <ex_orig xml:lang="en">to turn up the radio</ex_orig>
      <ex_tran xml:lang="fa">رادیو را بلند کردن</ex_tran>
      <ex_tran xml:lang="fa">4- (در جادهٔ فرعی) پیچیدن 5- سیر صعودی داشتن، بالا رفتن 6- روی دادن 7- یافت شدن 8- پدیدار شدن، سررسیدن</ex_tran>
    </ex>
  </def>
</def>
```

## 44. U bolt

TEI source: `22-u.xml` entry 11 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 44 (key `U bolt`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>U bolt</orth>
</form>
```

XDXF:

```xml
<k>U bolt</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>پیچ رکابی، کرپی</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>پیچ رکابی، کرپی</dtrn>
  </def>
</def>
```

## 45. underworld

TEI source: `22-u.xml` entry 431 (score 26, rare 1)  
XDXF article: `en-fa.xdxf` # 45 (key `underworld`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>underworld</orth>
  <pron>-wu_rld´</pron>
</form>
```

XDXF:

```xml
<k>underworld</k>
<tr>-wu_rld´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <gramGrp>
    <pos norm="noun">اسم</pos>
  </gramGrp>
  <sense xml:lang="fa">
    <usg type="time">قدیمی</usg>
    <cit type="trans">
      <quote>کرهٔ زمین، جهان خاکی</quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>جهان زیرین، سرزمین مردگان</quote>
    </cit>
    <xr>رجوع شود به: <ref>Hades</ref>
    </xr>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رجوع شود به: <ref>antipodes</ref>
      </quote>
    </cit>
  </sense>
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>دنیای تبهکاران، محیط جنایتکاران حرفه‌ای</quote>
    </cit>
    <cit type="example">
      <quote xml:lang="en">boss of the New York underworld</quote>
      <cit type="trans" xml:lang="fa">
        <quote>رئیس تبهکاران نیویورک</quote>
      </cit>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <pos>اسم</pos>
  <def xml:lang="fa">
    <categ type="time">قدیمی</categ>
    <dtrn>کرهٔ زمین، جهان خاکی</dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>جهان زیرین، سرزمین مردگان</dtrn>
    <dtrn>رجوع شود به: <kref>Hades</kref>
    </dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>رجوع شود به: <kref>antipodes</kref>
    </dtrn>
  </def>
  <def xml:lang="fa">
    <dtrn>دنیای تبهکاران، محیط جنایتکاران حرفه‌ای</dtrn>
    <ex>
      <ex_orig xml:lang="en">boss of the New York underworld</ex_orig>
      <ex_tran xml:lang="fa">رئیس تبهکاران نیویورک</ex_tran>
    </ex>
  </def>
</def>
```

## 46. Vaal

TEI source: `23-v.xml` entry 5 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 46 (key `Vaal`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Vaal</orth>
  <pron>väl</pron>
</form>
```

XDXF:

```xml
<k>Vaal</k>
<tr>väl</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رودخانهٔ وال (در جمهوری افریقای جنوبی)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>رودخانهٔ وال (در جمهوری افریقای جنوبی)</dtrn>
  </def>
</def>
```

## 47. Waal

TEI source: `24-w.xml` entry 3 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 47 (key `Waal`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Waal</orth>
  <pron>väl</pron>
</form>
```

XDXF:

```xml
<k>Waal</k>
<tr>väl</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رودخانهٔ وال (در هلند)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>رودخانهٔ وال (در هلند)</dtrn>
  </def>
</def>
```

## 48. xanthene dye

TEI source: `25-x.xml` entry 7 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 48 (key `xanthene dye`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>xanthene dye</orth>
</form>
```

XDXF:

```xml
<k>xanthene dye</k>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>انواع رنگ‌ها و رنگیزه‌هایی که ملکول آنها دارای زانتین است</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>انواع رنگ‌ها و رنگیزه‌هایی که ملکول آنها دارای زانتین است</dtrn>
  </def>
</def>
```

## 49. Yadkin

TEI source: `26-y.xml` entry 13 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 49 (key `Yadkin`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Yadkin</orth>
  <pron>yad´kin</pron>
</form>
```

XDXF:

```xml
<k>Yadkin</k>
<tr>yad´kin</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>رودخانهٔ یدکین (در ایالت کارولینای شمالی – آمریکا)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>رودخانهٔ یدکین (در ایالت کارولینای شمالی – آمریکا)</dtrn>
  </def>
</def>
```

## 50. Zaanstad

TEI source: `27-z.xml` entry 3 (score 6, rare 0)  
XDXF article: `en-fa.xdxf` # 50 (key `Zaanstad`, 1 senses)

### Headword / form

TEI:

```xml
<form xml:lang="en">
  <orth>Zaanstad</orth>
  <pron>zän´stät´</pron>
</form>
```

XDXF:

```xml
<k>Zaanstad</k>
<tr>zän´stät´</tr>
```

### Sense 1 (n=1)

TEI:

```xml
<sense n="1" xml:lang="fa">
  <sense xml:lang="fa">
    <cit type="trans">
      <quote>شهر زانستاد (در باختر هلند)</quote>
    </cit>
  </sense>
</sense>
```

XDXF:

```xml
<def n="1" xml:lang="fa">
  <def xml:lang="fa">
    <dtrn>شهر زانستاد (در باختر هلند)</dtrn>
  </def>
</def>
```
