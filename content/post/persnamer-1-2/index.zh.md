---
title: "persNamer 1.2：一个VIAF编号，九份规范档"
subtitle: 这个小小的人物志工具，如今能直接并入您手头的TEI文件，还顺道捎回各大目录的标识符

summary: >
  给persNamer一个VIAF编号，它还您一条TEI人物条目。到了1.2版，这条条目总算有了血肉：姓名异形、规范化的日期、九份国内外规范档的标识符，还有一种合并模式——不再打印片段，而是让您已有的人物志继续生长。

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

[persNamer](/code/persnamer/)起初不过是个小方便：喂它一个VIAF编号，它吐出一条TEI的`<person>`条目，外加一个`<persName>`标签，拿去标注文本便是。它只会这一件事，而且做出来的条目实在单薄——一个名字、两个日期、一个标识符，仅此而已。今天发布的1.2版，会的仍是这一件事，只是从此做出的条目值得留着了。

## 一条人物条目如今有些什么

先从姓名说起。VIAF的一个簇里，每家参与图书馆各留一种写法；旧版persNamer只管拿碰到的第一个标签。问它伏尔泰，答的是“فولتير،”——阿拉伯文，末尾的逗号原样保留，`xml:id`还是空的。1.2版会把整个簇里的写法逐一清点，留下各源记录公认的那一种；其余的作为`<persName type="variant">`列在后面，常见者居前。日期先行规范化（`1572-08-00`写作`1572-08`），再写两遍：一遍是正文，一遍是`@when`属性——凡是会处理日期的程序，真正读的都是后者。性别与描述，VIAF给了才有。

我最盼着的，是这一处：凡VIAF经`schema:sameAs`及其自身来源ID链接到的标识符，一律各写一条`<idno>`——BnF、GND、美国国会图书馆、SUDOC、Wikidata、ISNI、BNE、LIBRIS、NDL。一个编号进，九份目录出。于人物志而言，这便是一纸名单与规范数据之网中一个节点的分别。

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

只有一个人的时候，把XML打印到终端就够了；可一部校勘版动辄几百人。于是persNamer如今一次可接多个VIAF编号，两次请求之间礼貌地歇一歇，抓回来的内容存入缓存；加上`--merge`，新条目便直接插进已有TEI文件的`<listPerson>`。文件里本来就有的记录，按VIAF编号认出，`xml:id`照旧沿用；新ID先与文件核对，撞上了就加后缀（`-2`、`-3`）；最后整份文件重新缩进——动手之前，先留一份`.bak`副本。

```bash
persnamer --merge edition.xml 314802260 36925746
```

有一处改动请您留意：姓氏前的介词，默认不再计入ID，于是夏尔·德·泰利尼是`pers-teligny-c`，而非`pers-deteligny-c`。项目若已沿用旧格式，`--keep-particle`可以恢复；若干脆不想依赖姓名，`--id-format viaf`会给出`pers-viaf-314802260`。

## 杂务

脚本已经打包成软件包，附带`persnamer`命令：`uv tool install`或`pipx`一行装好，或用`uvx`免安装跑一回。二十六个测试跑在录制好的VIAF响应上，因此无需联网；CI在Python 3.9至3.13上逐版跑过，输出则按TEI P5校验。许可证照旧，Apache 2.0。

它依旧答不上来的，是某人生于何地、以何为业：VIAF的簇RDF既无地点，也无职业。与之链接的BnF与GND记录里倒是有——而它们的编号，如今已在您手中。

代码与文档见[GitHub](https://github.com/Pantagrueliste/persNamer)。
