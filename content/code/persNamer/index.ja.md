---
title: persNamer
summary: VIAF識別子をTEI XMLの人物エントリと注釈タグに変換し、デジタル校訂版の典拠管理を効率化するPythonツール。
tags:
  - XML
  - TEI
  - デジタル・ヒューマニティーズ
  - Python
  - VIAF
  - リンクトデータ

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: persNamerのデモンストレーション
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

## persNamer：TEIをバーチャル国際典拠ファイルにつなぐ

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamerは、VIAF（バーチャル国際典拠ファイル）の典拠データをTEI XML文書に取り込む作業を効率化する、専用のPythonツールです。VIAF識別子をそのまま使えるTEIマークアップに変換することで、デジタル校訂版のための構造化された人物エントリを作る手作業を大きく減らします。

## TEIにおける典拠管理の難しさ

デジタル校訂版では、標準化された名前や生没年を含め、歴史上の人物を正確に同定することがしばしば求められます。プロジェクト全体で典拠管理を一貫させるには、次の手順が要ります。

1. 歴史的テキストの中の人物を同定する
2. その人物についての典拠データを探す
3. 正しく整形されたTEIエントリを作る
4. プロジェクト全体で参照を一貫させる

これらの手順はふつう手作業で、時間がかかり、不整合も起こりがちです。

## persNamerの仕組み

persNamerは、次の手順でこのワークフローを自動化します。

1. **VIAFデータの取得**：VIAF識別子を受け取ると、HTTPコンテントネゴシエーションでRDFデータを取得します
2. **主要情報の抽出**：RDFを解析し、優先名、生年月日、没年月日を取り出します
3. **TEIマークアップの生成**：欠かせない二つのXMLスニペットを作ります。
   - **典拠ファイルのエントリ**（生成した`xml:id`、`<persName>`、`<birth>`、`<death>`、`<idno type="VIAF">`をもつ`<person>`要素）
   - それとは別の**注釈タグ**（典拠エントリを参照する`ref`属性をもつ`<persName>`）

この二つの出力があるおかげで、編集者は典拠ファイルを一元管理しながら、注釈タグをTEIテキストに手軽に挿し込めます。

## 主な機能

- **標準化されたID生成**：`pers-[familyname]-[givenname initial]`の形式で一貫したXML IDを生成（例：`pers-deteligny-c`）
- **RDF解析**：`rdflib`を使い、さまざまなRDFプロパティ（`rdfs:label`、`schema:name`、`viaf:mainHead`など）から情報を抽出
- **コマンドラインインターフェース**：必須引数はVIAF番号だけという手軽さ
- **詳細な出力**：最終的なXMLとあわせて、処理の経過を詳しく表示

## 使用例

```bash
python persNamer.py 314802260
```

このコマンドの出力は次のとおりです。

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## デジタル・ヒューマニティーズでの用途

persNamerがとりわけ役立つのは、次のような場面です。

- 典拠管理を必要とするデジタル校訂版
- 歴史上の人物を扱うTEIエンコーディングのプロジェクト
- 文書を典拠レコードに結びつけるリンクトデータの取り組み
- 大規模なTEIコーパス全体での一貫性の確保
- デジタル・ヒューマニティーズの授業での、典拠管理という概念の指導

## 実装

persNamerはPythonで書かれており、以下に依存しています。
- HTTPリクエストに`requests`
- RDF解析に`rdflib`
- XML処理に`lxml`

ソースコードとドキュメントは[GitHubリポジトリ](https://github.com/Pantagrueliste/persNamer)にあります。