---
title: Multi-Saxon
summary: A high-performance tool for parallel XSLT 2.0/3.0 transformations of large XML TEI corpora, handling transformations that LXML cannot process.
tags:
  - XSLT
  - XML
  - TEI
  - Digital Humanities
  - Python
  - Java
  - Performance

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon in action
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/multi-saxon
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

## Multi-Saxon: Parallel XSLT Processing for Large TEI Corpora

Multi-Saxon addresses a critical gap in XML processing tools by enabling parallel execution of XSLT 2.0 and 3.0 transformations that LXML (a popular Python XML library) cannot handle. Designed specifically for large collections of XML TEI documents, Multi-Saxon significantly accelerates processing time through efficient parallel execution.

## Key Features

- **Advanced XSLT Support**: Processes XSLT 2.0 and 3.0 transformations beyond LXML's capabilities
- **Parallel Processing**: Dramatically reduces transformation time for large document collections through parallelization
- **TEI-Optimized**: Specifically engineered for Text Encoding Initiative (TEI) XML documents
- **Scalable Performance**: Efficiently handles corpora ranging from hundreds to thousands of documents
- **Cross-Platform**: Works across different operating systems and environments

## The Problem Multi-Saxon Solves

Digital humanities scholars working with TEI often face two significant challenges:

1. LXML (a common Python XML processing library) only supports XSLT 1.0, making it impossible to use more advanced XSLT 2.0/3.0 features
2. Processing large corpora of TEI documents sequentially can be prohibitively time-consuming

Multi-Saxon addresses both issues by leveraging Saxon's advanced XSLT capabilities while distributing processing across multiple cores for significant performance gains.

## Implementation

Multi-Saxon combines Python with Java's Saxon processor to create a high-performance transformation pipeline:

- Uses Java's Saxon library for robust XSLT 2.0/3.0 processing
- Implements multiprocessing to distribute transformations across available CPU cores
- Manages processor pools efficiently to maximize throughput
- Provides a straightforward interface for batch processing TEI documents

## Usage Example

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Impact for Digital Humanities

For digital humanities projects dealing with large TEI document collections, Multi-Saxon enables:

- Complex corpus-wide transformations that would be impossible with LXML
- Dramatically reduced processing times (often by factors of 5-10x on multi-core systems)
- More sophisticated analysis through advanced XSLT 2.0/3.0 features
- Simplified workflow for processing entire document collections

Find the source code and documentation at the [GitHub Repository](https://github.com/Pantagrueliste/multi-saxon).
