---
title: persNamer
summary: VIAF識別子をTEI XMLの人物エントリと注釈タグに変換し、デジタル校訂版における典拠管理を効率化するPythonツール。
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

## persNamer：TEIをバーチャル国際典拠ファイルに接続する

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamerは、VIAF（バーチャル国際典拠ファイル）からの典拠のある人物データをTEI XML文書に統合する作業を効率化する、専用のPythonツールです。VIAF識別子をすぐに使えるTEIマークアップに変換することで、persNamerは、デジタル校訂版のための構造化された人物エントリを作成する際の手作業を大幅に削減します。

## TEIにおける典拠管理の課題

デジタル校訂版では、標準化された名前や生没年を含め、歴史上の人物を正確に識別することがしばしば求められます。プロジェクト全体で一貫した典拠管理を維持するには、次のことが必要です。

1. 歴史的テキストの中の人物を特定する
2. その人物についての典拠データを見つける
3. 適切に整形されたTEIエントリを作成する
4. プロジェクト全体で一貫した参照を確保する

これらのステップは通常、手作業で、時間がかかり、不整合が生じやすいものです。

## persNamerの仕組み

persNamerは、次のようにしてこのワークフローを自動化します。

1. **VIAFデータの取得**：VIAF識別子が与えられると、HTTPコンテントネゴシエーションを使ってRDFデータを取得します
2. **主要情報の抽出**：RDFを解析し、優先名、生年月日、没年月日を抽出します
3. **TEIマークアップの生成**：2つの重要なXMLスニペットを作成します：
   - **典拠ファイルのエントリ**（生成された`xml:id`、`<persName>`、`<birth>`、`<death>`、`<idno type="VIAF">`を持つ`<person>`要素）
   - 独立した**注釈タグ**（典拠エントリを参照する`ref`属性を持つ`<persName>`）

この二重の出力により、編集者は集中管理された典拠ファイルを維持しながら、注釈タグをTEIテキストに簡単に挿入できます。

## 主な機能

- **標準化されたID生成**：`pers-[familyname]-[givenname initial]`の形式で一貫したXML IDを作成（例：`pers-deteligny-c`）
- **RDF解析**：`rdflib`を使い、さまざまなRDFプロパティ（例：`rdfs:label`、`schema:name`、`viaf:mainHead`）から情報を抽出
- **コマンドラインインターフェース**：VIAF番号を唯一の必須引数として簡単に実行
- **詳細な出力**：最終的なXML出力とともに、詳細な処理情報を提供

## 使用例

```bash
python persNamer.py 314802260
```

このコマンドは次を生成します。

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## デジタル・ヒューマニティーズにおける応用

persNamerは特に次の用途に有用です。

- 典拠管理を必要とするデジタル校訂版
- 歴史上の人物を扱うTEIエンコーディングプロジェクト
- 文書を典拠レコードに結びつけるリンクトデータの取り組み
- 大規模なTEIコーパス全体での一貫性の確保
- デジタル・ヒューマニティーズの授業における典拠管理の概念の教育

## 実装

persNamerはPythonで実装されており、以下に依存しています。
- HTTPリクエストのための`requests`
- RDF解析のための`rdflib`
- XML処理のための`lxml`

ソースコードとドキュメントは[GitHubリポジトリ](https://github.com/Pantagrueliste/persNamer)にあります。