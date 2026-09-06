---
title: Multi-Saxon
summary: 一个高性能工具，对大型XML TEI语料库并行执行XSLT 2.0/3.0转换，处理LXML无能为力的转换。
tags:
  - XSLT
  - XML
  - TEI
  - 数字人文
  - Python
  - Java
  - 性能

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon运行中
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
machine_translated: true
---

## Multi-Saxon：大型TEI语料库的并行XSLT处理

Multi-Saxon填补了XML处理工具的一处要害空白：LXML（一个流行的Python XML库）处理不了的XSLT 2.0和3.0转换，它能并行执行。它专为大型XML TEI文档集合而设计，凭高效的并行执行大幅缩短处理时间。

## 主要特性

- **高级XSLT支持**：处理LXML力所不及的XSLT 2.0和3.0转换
- **并行处理**：借并行化大幅缩短大型文档集合的转换时间
- **为TEI优化**：专为文本编码倡议（TEI）XML文档打造
- **性能可扩展**：从数百到数千份文档的语料库，均可高效处理
- **跨平台**：可在不同操作系统和环境下运行

## Multi-Saxon解决什么问题

使用TEI的数字人文学者常常面临两大难题：

1. LXML（常用的Python XML处理库）只支持XSLT 1.0，XSLT 2.0/3.0的高级特性无从使用
2. 大型TEI语料库若逐份顺序处理，耗时可能长到令人却步

Multi-Saxon一举解决这两个问题：借用Saxon的高级XSLT能力，同时把处理分摊到多个核心，性能因此大增。

## 实现

Multi-Saxon把Python与Java的Saxon处理器结合起来，构成一条高性能的转换流水线：

- 用Java的Saxon库稳健地处理XSLT 2.0/3.0
- 以多进程把转换分摊到可用的CPU核心
- 高效管理处理器池，以求吞吐量最大化
- 为批量处理TEI文档提供简洁的接口

## 用法示例

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## 对数字人文的意义

对处理大型TEI文档集合的数字人文项目，Multi-Saxon让以下成为可能：

- LXML无法完成的复杂全语料库转换
- 大幅缩短处理时间（多核系统上常可提速5至10倍）
- 借助XSLT 2.0/3.0的高级特性做更精细的分析
- 简化整个文档集合的处理流程

源代码与文档见[GitHub仓库](https://github.com/Pantagrueliste/multi-saxon)。
