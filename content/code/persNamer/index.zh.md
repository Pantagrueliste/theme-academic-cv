---
title: persNamer
summary: 一个Python工具，把VIAF标识符转成TEI XML人物条目和标注标签，简化数字学术版本中的规范控制。
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

## persNamer：把TEI接上虚拟国际规范文档

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer是一个专门的Python工具，简化把VIAF（虚拟国际规范文档，Virtual International Authority File）中的规范人物数据整合进TEI XML文档的流程。它把VIAF标识符转成可直接使用的TEI标记，为数字学术版本创建结构化人物条目的手工劳动因此大减。

## TEI中规范控制的难处

数字学术版本往往需要精确识别历史人物，包括规范化的姓名和生卒年月。要在整个项目里保持一致的规范控制，需要：

1. 识别历史文本中的人物
2. 查找他们的规范数据
3. 创建格式正确的TEI条目
4. 确保全项目引用一致

这些步骤通常靠手工，费时，还容易前后不一。

## persNamer如何工作

persNamer把这套流程自动化：

1. **获取VIAF数据**：给定一个VIAF标识符，工具通过HTTP内容协商取回RDF数据
2. **提取关键信息**：解析RDF，提取首选姓名、出生日期和死亡日期
3. **生成TEI标记**：创建两段基本的XML片段：
   - 一条**规范文档条目**（`<person>`元素，带生成的`xml:id`、`<persName>`、`<birth>`、`<death>`和`<idno type="VIAF">`）
   - 一个独立的**标注标签**（`<persName>`，其`ref`属性指向规范条目）

这样双管齐下，校勘者既能维护一份集中的规范文档，又能把标注标签轻松插入TEI文本。

## 主要特性

- **标准化ID生成**：按`pers-[familyname]-[givenname initial]`格式生成一致的XML ID（如`pers-deteligny-c`）
- **RDF解析**：用`rdflib`从各种RDF属性（如`rdfs:label`、`schema:name`、`viaf:mainHead`）中提取信息
- **命令行界面**：只需一个VIAF编号作为必要参数即可运行
- **详细输出**：除最终XML外，还提供详细的处理信息

## 用法示例

```bash
python persNamer.py 314802260
```

这条命令生成：

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

persNamer对以下情形尤其有用：

- 需要规范控制的数字学术版本
- 涉及历史人物的TEI编码项目
- 把文献与规范记录相连的关联数据项目
- 保证大型TEI语料库的一致性
- 在数字人文课程中讲授规范控制概念

## 实现

persNamer用Python实现，依赖：
- `requests`：HTTP请求
- `rdflib`：RDF解析
- `lxml`：XML处理

源代码与文档见[GitHub仓库](https://github.com/Pantagrueliste/persNamer)。