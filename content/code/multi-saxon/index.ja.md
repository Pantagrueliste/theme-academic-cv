---
title: Multi-Saxon
summary: 大規模なXML TEIコーパスに対するXSLT 2.0/3.0変換を並列実行する高性能ツール。LXMLでは処理できない変換を扱います。
tags:
  - XSLT
  - XML
  - TEI
  - デジタル・ヒューマニティーズ
  - Python
  - Java
  - パフォーマンス

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: 動作中のMulti-Saxon
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/multi-saxon
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

## Multi-Saxon：大規模TEIコーパスのための並列XSLT処理

Multi-Saxonは、LXML（広く使われているPythonのXMLライブラリ）が扱えないXSLT 2.0および3.0の変換を並列実行できるようにすることで、XML処理ツールにおける重大な空白を埋めます。XML TEI文書の大規模なコレクション向けに特別に設計されたMulti-Saxonは、効率的な並列実行によって処理時間を大幅に短縮します。

## 主な機能

- **高度なXSLTサポート**：LXMLの能力を超えるXSLT 2.0および3.0の変換を処理
- **並列処理**：並列化により、大規模な文書コレクションの変換時間を劇的に短縮
- **TEI最適化**：Text Encoding Initiative（TEI）のXML文書向けに特別に設計
- **スケーラブルな性能**：数百から数千の文書からなるコーパスを効率的に処理
- **クロスプラットフォーム**：さまざまなオペレーティングシステムや環境で動作

## Multi-Saxonが解決する問題

TEIを扱うデジタル・ヒューマニティーズの研究者は、しばしば2つの大きな課題に直面します。

1. LXML（一般的なPythonのXML処理ライブラリ）はXSLT 1.0しかサポートしておらず、より高度なXSLT 2.0/3.0の機能を使うことができない
2. TEI文書の大規模なコーパスを逐次的に処理すると、法外に時間がかかることがある

Multi-Saxonは、Saxonの高度なXSLT機能を活用しつつ、処理を複数のコアに分散させることで、この両方の問題に対処し、大幅な性能向上を実現します。

## 実装

Multi-SaxonはPythonとJavaのSaxonプロセッサを組み合わせ、高性能な変換パイプラインを構築します。

- 堅牢なXSLT 2.0/3.0処理のためにJavaのSaxonライブラリを使用
- マルチプロセッシングを実装し、利用可能なCPUコアに変換を分散
- スループットを最大化するためにプロセッサプールを効率的に管理
- TEI文書のバッチ処理のための簡潔なインターフェースを提供

## 使用例

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## デジタル・ヒューマニティーズへのインパクト

大規模なTEI文書コレクションを扱うデジタル・ヒューマニティーズのプロジェクトに対して、Multi-Saxonは次のことを可能にします。

- LXMLでは不可能な、コーパス全体にわたる複雑な変換
- 処理時間の劇的な短縮（マルチコアシステムではしばしば5〜10倍）
- 高度なXSLT 2.0/3.0の機能による、より洗練された分析
- 文書コレクション全体を処理するワークフローの簡素化

ソースコードとドキュメントは[GitHubリポジトリ](https://github.com/Pantagrueliste/multi-saxon)にあります。
