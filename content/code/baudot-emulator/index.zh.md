---
title: ITA2电报模拟器
summary: 一个ITA2（Baudot-Murray）电报码的交互式演示，帮助学生掌握二进制编码与状态机的基本概念。
tags:
  - JavaScript
  - 交互式
  - 教学

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: 显示已编码信息的ITA2电报纸带
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
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

这个ITA2模拟器通过把抽象的编码概念变得可见、可交互，成为一件实用的教学辅助工具。当学生输入文字并看到它立即转换成孔洞图案时，他们正在学习计算与电信领域的几个关键概念。

## 教育益处

首先，它演示了二进制表示——文本如何变成由1和0组成的图案。我们通常以抽象的方式讲授这一点，而亲眼看到纸带上打出的孔洞，能帮助学生理解物理系统如何表示数字信息。

{{< Baudot >}}

LETTERS/FIGURES（字母/数字）换挡机制自然而然地引入了状态机。学生通过实验发现，同一种图案会因当前模式不同而代表不同的字符。这种对基于状态的编码的亲身体验，为他们学习更复杂的计算概念做好了准备。

## 实现细节

该模拟器以JavaScript和HTML/CSS实现，可轻松嵌入任何网页。代码采用模块化设计，可针对不同的教育情境进行调整。

您可以在[GitHub仓库](https://github.com/Pantagrueliste/BaudotMurray_Emulator)查看源代码并亲自试用模拟器。