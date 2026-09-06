---
title: persNamer
summary: 一个Python工具，将VIAF标识符转换为TEI XML人物条目和注释标签，简化数字学术版本中的规范控制。
tags:
  - XML
  - TEI
  - 数字人文
  - Python
  - VIAF
  - 关联数据

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: persNamer演示
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
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
machine_translated: true
---

## persNamer：连接TEI与虚拟国际规范文档

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer是一个专门的Python工具，它简化了将VIAF（虚拟国际规范文档，Virtual International Authority File）中的权威人物数据整合到TEI XML文档中的过程。通过把VIAF标识符转换为即可使用的TEI标记，persNamer显著减少了为数字学术版本创建结构化人物条目所涉及的手工工作。

## TEI中规范控制的挑战

数字学术版本往往需要精确识别历史人物，包括其规范化姓名和生卒日期。在整个项目中保持一致的规范控制需要：

1. 识别历史文本中的人物
2. 查找有关他们的权威数据
3. 创建格式正确的TEI条目
4. 确保整个项目中引用的一致性

这些步骤通常是手工完成的，耗时且容易不一致。

## persNamer如何工作

persNamer通过以下方式将这一工作流自动化：

1. **获取VIAF数据**：给定一个VIAF标识符，工具通过HTTP内容协商检索RDF数据
2. **提取关键信息**：解析RDF以提取首选姓名、出生日期和死亡日期
3. **生成TEI标记**：创建两个基本的XML片段：
   - 一个**规范文档条目**（`<person>`元素，带有生成的`xml:id`、`<persName>`、`<birth>`、`<death>`和`<idno type="VIAF">`）
   - 一个单独的**注释标签**（带有引用规范条目的`ref`属性的`<persName>`）

这种双重输出让编辑者既能维护一个集中的规范文档，又能轻松地把注释标签插入其TEI文本。

## 主要特性

- **标准化ID生成**：以`pers-[familyname]-[givenname initial]`格式创建一致的XML ID（例如`pers-deteligny-c`）
- **RDF解析**：使用`rdflib`从各种RDF属性（例如`rdfs:label`、`schema:name`、`viaf:mainHead`）中提取信息
- **命令行界面**：只需一个VIAF编号作为唯一必需参数即可执行
- **详细输出**：在最终XML输出之外提供详细的处理信息

## 用法示例

```bash
python persNamer.py 314802260
```

该命令生成：

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## 在数字人文中的应用

persNamer对以下情形特别有价值：

- 需要规范控制的数字学术版本
- 涉及历史人物的TEI编码项目
- 将文献与规范记录相连接的关联数据项目
- 确保大型TEI语料库的一致性
- 在数字人文课程中讲授规范控制概念

## 实现

persNamer以Python实现，依赖于：
- `requests`用于HTTP请求
- `rdflib`用于RDF解析
- `lxml`用于XML处理

源代码与文档请见[GitHub仓库](https://github.com/Pantagrueliste/persNamer)。