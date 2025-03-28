---
title: persNamer
summary: A Python tool that converts VIAF identifiers into TEI XML person entries and annotation tags, streamlining authority control in digital scholarly editions.
tags:
  - XML
  - TEI
  - Digital Humanities
  - Python
  - VIAF
  - Linked Data

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: persNamer demonstration
  focal_point: Smart

links:
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/Pantagrueliste/persNamer
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

## persNamer: Connecting TEI to the Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer is a specialized Python tool that streamlines the integration of authoritative person data from VIAF (Virtual International Authority File) into TEI XML documents. By converting VIAF identifiers into ready-to-use TEI markup, persNamer significantly reduces the manual work involved in creating structured person entries for digital scholarly editions.

## The Challenge of Authority Control in TEI

Digital scholarly editions often require precise identification of historical persons, including their standardized names and life dates. Maintaining consistent authority control across a project requires:

1. Identifying persons in historical texts
2. Finding authoritative data about them
3. Creating properly formatted TEI entries
4. Ensuring consistent references throughout the project

These steps are typically manual, time-consuming, and prone to inconsistency.

## How persNamer Works

persNamer automates this workflow by:

1. **Fetching VIAF Data**: Given a VIAF identifier, the tool retrieves RDF data using HTTP content negotiation
2. **Extracting Key Information**: Parses the RDF to extract the preferred name, birth date, and death date
3. **Generating TEI Markup**: Creates two essential XML snippets:
   - An **authority file entry** (`<person>` element with a generated `xml:id`, `<persName>`, `<birth>`, `<death>`, and `<idno type="VIAF">`)
   - A separate **annotation tag** (`<persName>` with a `ref` attribute referencing the authority entry)

This dual output allows editors to maintain a centralized authority file while easily inserting annotation tags into their TEI texts.

## Key Features

- **Standardized ID Generation**: Creates consistent XML IDs in the format `pers-[familyname]-[givenname initial]` (e.g., `pers-deteligny-c`)
- **RDF Parsing**: Uses `rdflib` to extract information from various RDF properties (e.g., `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Command-Line Interface**: Simple execution with a VIAF number as the only required argument
- **Verbose Output**: Provides detailed processing information alongside the final XML output

## Example Usage

```bash
python persNamer.py 314802260
```

This command produces:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Application in Digital Humanities

persNamer is particularly valuable for:

- Digital scholarly editions requiring authority control
- TEI encoding projects working with historical figures
- Linked data initiatives connecting documents to authority records
- Ensuring consistency across large TEI corpora
- Teaching authority control concepts in digital humanities courses

## Implementation

persNamer is implemented in Python and depends on:
- `requests` for HTTP requests
- `rdflib` for RDF parsing
- `lxml` for XML handling

Find the source code and documentation at the [GitHub Repository](https://github.com/Pantagrueliste/persNamer).