---
title: tei-mcp
summary: 一个MCP服务器，帮AI智能体读写有效的TEI XML；16个工具涵盖元素查询、属性解析、内容模型展开、嵌套验证、文档验证和ODD定制。
tags:
  - XML
  - TEI
  - 数字人文
  - Python
  - MCP
  - 人工智能

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: tei-mcp启动横幅
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

## tei-mcp：给AI智能体用的TEI P5

tei-mcp是一个开源[MCP](https://modelcontextprotocol.io)服务器，让AI编程助手直接访问[TEI P5](https://tei-c.org/guidelines/)规范。AI不必再倚赖记忆中的训练数据——那往往产出貌似合理、实则错误的标记——而可以实时查询规范。

## 功能

服务器解析TEI P5的ODD，提供16个工具：

- 按名称**查询**任何元素、类、宏或模块，不区分大小写，拼错了还会给出建议
- 沿完整的TEI类层次**解析属性**（本地＋继承）
- 把**内容模型展开**成结构化的树，并解析类与宏
- **验证嵌套**——直接的父子关系，或带路径追踪的递归可达性
- 依据TEI P5**验证文档**：内容模型、属性、封闭取值列表、引用完整性、弃用警告
- **验证单个元素**，适用于增量编辑的工作流
- **加载ODD定制**，把模式约束到项目特定的子集
- 用正则表达式在所有实体类型中**搜索**

## 安装

```bash
pip install tei-mcp
```

或直接运行：

```bash
uvx tei-mcp
```

## 用法

加入任何兼容MCP的客户端（Claude、Cursor、Windsurf等）：

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

源代码与文档见[GitHub仓库](https://github.com/Pantagrueliste/tei-mcp)。
