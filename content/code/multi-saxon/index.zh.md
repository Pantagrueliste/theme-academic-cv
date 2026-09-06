---
title: Multi-Saxon
summary: 一个高性能工具，用于对大型XML TEI语料库进行并行的XSLT 2.0/3.0转换，处理LXML无法处理的转换。
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
  caption: Multi-Saxon运行实况
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

## Multi-Saxon：面向大型TEI语料库的并行XSLT处理

Multi-Saxon填补了XML处理工具中的一个关键空白，使LXML（一个流行的Python XML库）无法处理的XSLT 2.0和3.0转换得以并行执行。Multi-Saxon专为大型XML TEI文档集合设计，通过高效的并行执行显著缩短处理时间。

## 主要特性

- **高级XSLT支持**：处理超出LXML能力范围的XSLT 2.0和3.0转换
- **并行处理**：通过并行化大幅缩短大型文档集合的转换时间
- **为TEI优化**：专为文本编码倡议（TEI）XML文档设计
- **可扩展的性能**：高效处理从数百到数千份文档的语料库
- **跨平台**：可在不同的操作系统和环境中运行

## Multi-Saxon解决的问题

使用TEI的数字人文学者常常面临两大挑战：

1. LXML（一个常用的Python XML处理库）仅支持XSLT 1.0，无法使用更高级的XSLT 2.0/3.0特性
2. 顺序处理大型TEI文档语料库可能耗时到令人却步

Multi-Saxon通过利用Saxon的高级XSLT能力，并将处理分布到多个核心上以获得显著的性能提升，同时解决了这两个问题。

## 实现

Multi-Saxon将Python与Java的Saxon处理器结合，构建了一条高性能的转换流水线：

- 使用Java的Saxon库进行稳健的XSLT 2.0/3.0处理
- 实现多进程处理，将转换分布到可用的CPU核心上
- 高效管理处理器池以最大化吞吐量
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

## 对数字人文的影响

对于处理大型TEI文档集合的数字人文项目，Multi-Saxon使以下成为可能：

- 用LXML不可能完成的复杂的全语料库转换
- 大幅缩短的处理时间（在多核系统上通常可提速5至10倍）
- 借助高级XSLT 2.0/3.0特性进行更精细的分析
- 简化处理整个文档集合的工作流

源代码与文档请见[GitHub仓库](https://github.com/Pantagrueliste/multi-saxon)。
