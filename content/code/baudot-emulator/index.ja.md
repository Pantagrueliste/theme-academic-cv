---
title: ITA2電信エミュレータ
summary: ITA2（ボードー・マレー）電信符号のインタラクティブなデモンストレーション。二進法による符号化と状態機械という基本概念を学生が把握する助けになります。
tags:
  - JavaScript
  - インタラクティブ
  - 教育

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: 符号化されたメッセージを示すITA2電信テープ
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

このITA2エミュレータは、抽象的な符号化の概念を目に見える、操作できるものにすることで、実践的な教材として機能します。学生がテキストを入力し、それが即座に穴のパターンに変換されるのを見るとき、彼らはコンピューティングと電気通信におけるいくつかの鍵となる概念を学んでいるのです。

## 教育上の利点

第一に、二進表現――テキストがどのようにして1と0のパターンになるのか――を実演します。私たちはこれをしばしば抽象的に教えますが、実際に穴が現れるのを見ることで、物理的なシステムがどのようにデジタル情報を表現できるのかを学生は把握しやすくなります。

{{< Baudot >}}

LETTERS/FIGURESシフトの仕組みは、状態機械（ステートマシン）を自然に導入します。学生は試行錯誤を通じて、同じパターンが現在のモードに応じて異なる文字を表しうることを発見します。状態に基づく符号化をこうして体験することが、より複雑なコンピューティングの概念への準備になります。

## 実装の詳細

このエミュレータはJavaScriptとHTML/CSSで実装されており、どのウェブページにも容易に埋め込めます。コードはモジュール化されており、さまざまな教育の文脈に合わせて改変できます。

ソースコードの閲覧とエミュレータの試用は、[GitHubリポジトリ](https://github.com/Pantagrueliste/BaudotMurray_Emulator)から。