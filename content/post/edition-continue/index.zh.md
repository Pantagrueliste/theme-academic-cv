---
title: "新工具，旧习惯"
subtitle: 一篇Programming Historian教程：边编码，边出版校勘本

summary: >
  计算机问世已有半个世纪，我们做数字版本却仍像在做印刷书。我为Programming Historian en français
  撰写的新教程分上下两篇，上篇介绍一套基本构件，让校勘本能够随编码进度同步出版。

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: '雅卡尔提花织机前的织工，以及为花样编程的一长串打孔卡。图片来源：[*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- 数字人文
- 数字版本
- 学术校勘
- TEI

categories:
- 数字人文

projects: [DCE]
---

近代早期的人文主义者接纳了印刷术，也给校勘本定下了沿用至今的形态：先确定文本，再排版付印，一次出版；即便要更正，也得等到多年后的再版。计算机问世已有半个世纪，我们做数字版本却仍像在做印刷书：文本定稿，一次性发布，勘误留待日后。工具是新的，习惯却还是旧的。

我为*Programming Historian en français*撰写的新教程[《L’édition critique en continu : publier au rythme de l’encodage (Partie 1)》](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1)，就是要让新工具名副其实。TEI编码既然是代码——它确实是——就可以像代码一样做版本控制、验证和转换。软件开发者早就不再等待成品：每一处改动都自动检查，通过了就发布。校勘本没有理由不能照此运作：每封书信一经编码、审校，便即刻出版；一旦发现更好的读法，就随时公开修订。


## 上篇：基本构件

上篇介绍几样构件，帮助校勘者摆脱沿袭下来的工作流程，而且全部开源：

- **ODD**：规定整个项目编码方式的唯一文档；
- 由它生成的**RELAX NG模式**，负责约束结构；
- **Schematron规则**，补上模式无法表达的编辑约束；
- **验证脚本**，一条命令即可检查整个语料库，并借助XSLT生成便于阅读的输出。

示例均取自菲利波·卡夫里亚纳（Filippo Cavriana）的书信，也就是我正[按照这一思路构建](/post/cavriana-edition/)的校勘本。下篇将加入一条流水线，把这些构件串联起来，让语料库的每一处改动都随改随验、随验随发。本教程隶属于我的[高效校勘](/project/dce/)项目，该项目致力于降低学术校勘本的成本；而把出版自动化，让校勘者不必再在流程末端干等技术专家，正是其中最能省钱的环节之一。


## 抵制、否认，或流于表面

人们对人工智能的反应也是同一个套路：要么抵制，要么否认，要么只是表面上用一用。这也是我喜欢数字人文的原因之一：很少有哪个领域把这种悖论暴露得如此直白。新工具本该促使我们重新思考如何把工作做得更好，而不是给老套路刷上一层新漆。这篇教程便是在学术校勘领域接下这份邀请。下篇敬请期待。

感谢我的编辑达芙妮·马特利耶（Daphné Mathelier）和马蒂亚斯·吉勒·勒旺松（Matthias Gille Levenson），审稿人雅丝明·马卡里奥斯（Jasmin Macarios）和埃尔莎·范·科特（Elsa Van Kote），以及阿妮莎·霍斯（Anisa Hawes）。

教程以开放获取方式发布：[programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1)（DOI：[10.46430/phfr0044](https://doi.org/10.46430/phfr0044)）。
