# aryanpour-tei
Aryanpour Dictionary in FreeDict (.tei) structured format

## Source layout

The dictionary source is split into `aryanpour.parts/NN-*.xml` files (one per
letter or group). Edit these part files; do not edit the generated `.tei` file.

## Build

Combine the parts into a single TEI file:

```bash
python3 combine_tei.py --output aryanpour.tei
```

## Convert for use in dictionary applications

Use [PyGlossary](https://github.com/ilius/pyglossary) to convert the generated
`aryanpour.tei` file to your desired format directly.

## View the file

+ Linux/Unix: `less aryanpour.tei`
+ Windows: Open with an editor/IDE (beware of the file size)

## Write a parser or dictionary application for it

See [freedict.py](https://github.com/ilius/pyglossary/blob/master/pyglossary/plugins/freedict.py)
