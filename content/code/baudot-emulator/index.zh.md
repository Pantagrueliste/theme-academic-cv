---
title: ITA2电报模拟器
summary: ITA2（Baudot-Murray）电报码的交互式演示，帮助学生掌握二进制编码与状态机的基本概念。
tags:
  - JavaScript
  - 交互式
  - 教学

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: 打有编码信息的ITA2电报纸带
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

这个ITA2模拟器把抽象的编码概念变得看得见、摸得着，是一件实用的教具。学生敲入文字，眼看着它立刻变成孔洞图案——这一过程中，他们学到的是计算与电信的几个关键概念。

## 教学价值

首先，它演示了二进制表示——文字如何变成一串串1和0。这一点我们通常讲得很抽象；而亲眼看着纸带上打出一个个孔，学生便更容易明白，物理系统是怎样表示数字信息的。

{{< Baudot >}}

LETTERS/FIGURES（字母/数字）换挡机制顺理成章地引出了状态机。学生一试便知：同一个图案，模式不同，代表的字符也不同。有了这种基于状态的编码的亲身体验，往后学更复杂的计算概念便有了根基。

## 实现细节

模拟器用JavaScript和HTML/CSS写成，可轻松嵌入任何网页。代码模块化，可按不同教学情境调整。

源代码和在线试用见[GitHub仓库](https://github.com/Pantagrueliste/BaudotMurray_Emulator)。