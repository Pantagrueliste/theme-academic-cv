---
title: "persNamer 1.2: One VIAF Number, Nine Authority Files"
subtitle: The little personography tool now merges into your existing TEI file and carries the identifiers of the big catalogues

summary: >
  persNamer takes a VIAF number and hands back a TEI person entry. Version
  1.2 makes that entry worth having: variant names, normalised dates, the
  identifiers of nine national and international authority files, and a
  merge mode that grows an existing personography instead of printing snippets.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Linked Data
- Digital Humanities
- Python

categories:
- Digital Humanities
---

[persNamer](/code/persnamer/) started as a small convenience: give it a
VIAF number, get back a TEI `<person>` entry and the `<persName>` tag to
annotate your text with. It did one thing, and the entry it produced was
thin — a name, two dates, one identifier. Version 1.2, released today,
keeps the one thing and makes the entry worth keeping.

## What a person entry now contains

Start with the name. A VIAF cluster carries one name per contributing
library, and the old persNamer simply took the first label it met. Ask it
for Voltaire and it would answer « فولتير، » — the Arabic form, trailing
comma included — with an empty `xml:id` for good measure. Version 1.2
counts the forms across the cluster and keeps the one the source records
agree on; the others come along as `<persName type="variant">`, most
common first. Dates are normalised (`1572-08-00` becomes `1572-08`) and
emitted twice, as text and as a `@when` attribute, which is what any
date-aware processing of the file will actually read. Sex and
descriptions appear when VIAF exposes them.

The part I wanted most: every identifier VIAF links to, through
`schema:sameAs` and its own source IDs, is written out as an `<idno>` —
BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL.
One number in, nine catalogues out. For a personography, that is the
difference between a list of names and a node in the web of authority
data.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## From snippets to a personography

Printing XML to the terminal is fine for one person. Editions have
hundreds. persNamer now takes several VIAF numbers at once, pauses
politely between requests, caches what it fetches, and — with `--merge` —
inserts the new entries straight into the `<listPerson>` of an existing
TEI file. Records already there are recognised by their VIAF number and
their `xml:id` reused; new ids are checked against the file and suffixed
(`-2`, `-3`) if they would collide; the file is re-indented and a `.bak`
copy written first.

```bash
persnamer --merge edition.xml 314802260 36925746
```

One change to know about: the family-name particle is now dropped from
the id by default, so Charles de Téligny is `pers-teligny-c` rather than
`pers-deteligny-c`. If your project settled on the old form,
`--keep-particle` restores it; `--id-format viaf` gives you
`pers-viaf-314802260` if you would rather not depend on names at all.

## Housekeeping

The script is now a package with a `persnamer` command, installable in
one line with `uv tool install` or `pipx` (or run once, uninstalled, with
`uvx`). Twenty-six tests run against recorded VIAF responses, so the
suite needs no network; CI exercises them on Python 3.9 through 3.13, and
the output is validated against TEI P5. Apache 2.0, as before.

What it still cannot do is tell you where someone was born or what they
did for a living: VIAF's cluster RDF carries neither places nor
occupations. The linked BnF and GND records do, and now you have their
numbers.

Code and documentation on
[GitHub](https://github.com/Pantagrueliste/persNamer).
