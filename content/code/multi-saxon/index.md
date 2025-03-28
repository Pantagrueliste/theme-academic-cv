---
title: Multi-Saxon
summary: A utility tool for managing and executing XSLT transformations across multiple Saxon processor versions with a unified interface.
tags:
  - XSLT
  - XML
  - Digital Humanities
  - Java

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon logo
  focal_point: Smart

links:
  - icon: github
    icon_pack: fab
    name: Code
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

## Multi-Saxon: A Unified Interface for Saxon Processors

Multi-Saxon provides a straightforward way to use multiple versions of the Saxon XSLT processor without changing your workflow or configuration. This tool is particularly valuable for digital humanists and developers who need to maintain compatibility with different XSLT stylesheet versions or test transformations across multiple Saxon versions.

## Why Multi-Saxon?

When working with digital editions and XML-based scholarly projects, you may encounter XSLT stylesheets designed for specific Saxon versions. Rather than maintaining multiple environments or manually switching JAR files, Multi-Saxon offers:

- A unified command-line interface for all Saxon versions
- Simple version switching with minimal configuration
- Batch processing capabilities across multiple files
- Consistent output handling regardless of Saxon version

## Features

- Support for Saxon 9, 10, and 11 (HE, PE, and EE editions)
- Automatic classpath management for each version
- XSLT 1.0, 2.0, and 3.0 support
- XQuery support
- Customizable output formatting
- Extension function support

## Implementation Details

Multi-Saxon is implemented as a Java application that:

1. Manages a repository of Saxon processor JARs
2. Provides a version-agnostic API for XSLT transformations
3. Handles classpath isolation to prevent version conflicts
4. Provides consistent error reporting across versions

## Usage Example

```bash
# Transform using Saxon 11
multi-saxon -v 11 -s source.xml -xsl stylesheet.xsl -o output.html

# Compare transformation results between versions
multi-saxon -compare -v 9,10,11 -s source.xml -xsl stylesheet.xsl
```

## Integration with Digital Humanities Workflows

Multi-Saxon fits perfectly into digital humanities publication pipelines, enabling scholars to:

- Maintain backward compatibility with legacy stylesheets
- Test transformations across processor versions to ensure portability
- Create reproducible transformation workflows for scholarly editions
- Simplify collaboration across teams with different XSLT processor preferences

You can find the source code and try Multi-Saxon yourself at the [GitHub Repository](https://github.com/Pantagrueliste/multi-saxon).