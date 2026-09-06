---
title: tei-mcp
summary: AIエージェントが妥当なTEI XMLを読み書きするのを助けるMCPサーバー。要素の検索、属性の解決、内容モデルの展開、入れ子の検証、文書の検証、ODDカスタマイズをカバーする16のツールを備えています。
tags:
  - XML
  - TEI
  - デジタル・ヒューマニティーズ
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: tei-mcpの起動バナー
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp：AIエージェントのためのTEI P5

tei-mcpは、AIコーディングアシスタントに[TEI P5](https://tei-c.org/guidelines/)仕様への直接アクセスを提供するオープンソースの[MCP](https://modelcontextprotocol.io)サーバーです。記憶した訓練データ――しばしばもっともらしいが誤ったマークアップを生み出します――に頼る代わりに、AIはリアルタイムで仕様に問い合わせることができます。

## 機能

サーバーはTEI P5のODDを解析し、16のツールを公開します。

- 任意の要素、クラス、マクロ、モジュールを名前で**検索**。大文字小文字を区別せず、タイプミスの候補も提示
- TEIのクラス階層全体にわたって**属性を解決**（ローカル＋継承）
- クラスとマクロを解決しつつ、**内容モデルを展開**して構造化された木に変換
- **入れ子を検証**――直接の親子関係、または経路追跡付きの再帰的な到達可能性
- TEI P5に照らして**文書を検証**：内容モデル、属性、閉じた値リスト、参照の整合性、非推奨警告
- 漸進的な編集ワークフローのために**単一要素を検証**
- **ODDカスタマイズを読み込み**、スキーマをプロジェクト固有のサブセットに制約
- 正規表現パターンで、すべてのエンティティ型を横断して**検索**

## インストール

```bash
pip install tei-mcp
```

または、次のコマンドで直接実行します。

```bash
uvx tei-mcp
```

## 使い方

MCP互換の任意のクライアント（Claude、Cursor、Windsurfなど）に追加します。

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

ソースコードとドキュメントは[GitHubリポジトリ](https://github.com/Pantagrueliste/tei-mcp)にあります。
