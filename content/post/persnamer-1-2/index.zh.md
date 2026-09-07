---
title: "persNamer 1.2：一个VIAF编号，九份规范档"
subtitle: 这个小小的人物志工具现在能把条目并入您已有的TEI文件，并带上各大目录的标识符

summary: >
  persNamer接过一个VIAF编号，交回一条TEI人物条目。1.2版让这条条目值得拥有：姓名的异形、规范化的日期、九份国内外规范档的标识符，以及一种合并模式——不再打印片段，而是让已有的人物志不断长大。

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- 关联数据
- 数字人文
- Python

categories:
- 数字人文
---

[persNamer](/code/persnamer/)起初只是个小便利：给它一个VIAF编号，它还您一条TEI `<person>`条目，外加一个用来给文本作标注的`<persName>`标签。它只做一件事，而做出来的条目很单薄——一个名字、两个日期、一个标识符。今天发布的1.2版，那一件事照做，但条目从此值得留下。

## 人物条目现在包含什么

先说姓名。一个VIAF簇里，每家参与的图书馆各贡献一个名字，旧版persNamer只是把碰到的第一个标签拿来就用。问它伏尔泰，它会答“فولتير،”——阿拉伯文的写法，连末尾的逗号一并奉上——还附赠一个空的`xml:id`。1.2版在整个簇里给各种写法计数，保留源记录一致认可的那个；其余的作为`<persName type="variant">`跟在后面，最常见的排最前。日期经过规范化（`1572-08-00`变为`1572-08`），并输出两次：一次是文本，一次是`@when`属性——任何按日期处理这份文件的程序，真正读的是后者。性别与描述则在VIAF提供时出现。

我最想要的部分：VIAF通过`schema:sameAs`及其自身来源ID链接到的每一个标识符，都写成一条`<idno>`——BnF、GND、美国国会图书馆、SUDOC、Wikidata、ISNI、BNE、LIBRIS、NDL。一个编号进去，九份目录出来。对人物志而言，这就是一张名单与规范数据之网中一个节点的区别。

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## 从片段到人物志

把XML打印到终端，一个人的时候没问题。一部校勘版动辄有几百人。persNamer现在一次可以接收多个VIAF编号，请求之间礼貌地停一停，抓到的内容缓存起来，再加上`--merge`，就把新条目直接插进已有TEI文件的`<listPerson>`。文件里已有的记录按VIAF编号认出来，沿用其`xml:id`；新ID先与文件核对，若会冲突就加后缀（`-2`、`-3`）；文件重新缩进，动手之前先写一份`.bak`副本。

```bash
persnamer --merge edition.xml 314802260 36925746
```

有一处改动需要知道：姓氏前的小品词现在默认不再进入ID，所以夏尔·德·泰利尼是`pers-teligny-c`，而不是`pers-deteligny-c`。若您的项目已经定下旧格式，`--keep-particle`可以恢复；若您宁可完全不依赖姓名，`--id-format viaf`会给出`pers-viaf-314802260`。

## 杂务

脚本现在是一个带`persnamer`命令的软件包，用`uv tool install`或`pipx`一行即可安装（或者用`uvx`免安装跑一次）。二十六个测试跑在录好的VIAF响应上，测试套件因此不需要联网；CI在Python 3.9到3.13上逐一跑过，输出按TEI P5验证。许可证仍是Apache 2.0。

它仍然做不到的，是告诉您某人生在哪里、以何为业：VIAF的簇RDF既不带地点，也不带职业。与之链接的BnF和GND记录有，而现在，它们的编号已在您手里。

代码与文档见[GitHub](https://github.com/Pantagrueliste/persNamer)。
