---
title: Multi-Saxon
summary: 大規模なXML TEIコーパスに対してXSLT 2.0/3.0の変換を並列実行する高性能ツール。LXMLの手に余る変換を引き受けます。
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

Multi-Saxonは、LXML（広く使われているPythonのXMLライブラリ）では扱えないXSLT 2.0および3.0の変換を並列に実行できるようにし、XML処理ツールの重大な空白を埋めます。XML TEI文書の大規模なコレクションに的を絞って設計されており、効率のよい並列実行で処理時間を大幅に縮めます。

## 主な機能

- **高度なXSLT対応**：LXMLの手に余るXSLT 2.0および3.0の変換を処理
- **並列処理**：並列化により、大規模な文書コレクションの変換時間を劇的に短縮
- **TEIに最適化**：Text Encoding Initiative（TEI）のXML文書に特化して設計
- **スケーラブルな性能**：数百から数千の文書からなるコーパスを効率よく処理
- **クロスプラットフォーム**：さまざまなOSや環境で動作

## Multi-Saxonが解決する問題

TEIを扱うデジタル・ヒューマニティーズの研究者は、往々にして二つの壁にぶつかります。

1. LXML（Pythonでよく使われるXML処理ライブラリ）はXSLT 1.0にしか対応しておらず、XSLT 2.0/3.0の高度な機能が使えない
2. TEI文書の大規模なコーパスを一つずつ順に処理すると、途方もない時間がかかる

Multi-Saxonは、Saxonの高度なXSLT機能を活かしつつ処理を複数のコアに振り分けることで、この両方に対処し、大幅な性能向上を実現します。

## 実装

Multi-SaxonはPythonとJavaのSaxonプロセッサを組み合わせ、高性能な変換パイプラインを構成します。

- 堅牢なXSLT 2.0/3.0処理にJavaのSaxonライブラリを使用
- マルチプロセッシングにより、利用可能なCPUコアに変換を分散
- スループットを最大化するようプロセッサプールを効率よく管理
- TEI文書をバッチ処理するための簡潔なインターフェースを提供

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

大規模なTEI文書コレクションを扱うデジタル・ヒューマニティーズのプロジェクトにとって、Multi-Saxonは次のことを可能にします。

- LXMLでは不可能な、コーパス全体にわたる複雑な変換
- 処理時間の劇的な短縮（マルチコア環境では5〜10倍になることも珍しくありません）
- XSLT 2.0/3.0の高度な機能による、より洗練された分析
- 文書コレクション全体を処理するワークフローの簡素化

ソースコードとドキュメントは[GitHubリポジトリ](https://github.com/Pantagrueliste/multi-saxon)にあります。
