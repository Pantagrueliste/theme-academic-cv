---
title: tei-mcp
summary: 一个MCP服务器，帮助AI智能体读写有效的TEI XML，提供16个工具，涵盖元素查询、属性解析、内容模型展开、嵌套验证、文档验证和ODD定制。
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

## tei-mcp：面向AI智能体的TEI P5

tei-mcp是一个开源[MCP](https://modelcontextprotocol.io)服务器，让AI编程助手直接访问[TEI P5](https://tei-c.org/guidelines/)规范。AI不必依赖记忆中的训练数据——那往往产生貌似合理却不正确的标记——而可以实时查询规范。

## 功能

服务器解析TEI P5的ODD并暴露16个工具：

- 按名称**查询**任何元素、类、宏或模块，支持不区分大小写的匹配和拼写错误建议
- 在完整的TEI类层次结构中**解析属性**（本地+继承）
- 将**内容模型展开**为结构化的树，并解析类和宏
- **验证嵌套**——直接父子关系或带路径追踪的递归可达性
- 依据TEI P5**验证文档**：内容模型、属性、封闭取值列表、引用完整性和弃用警告
- **验证单个元素**，适用于增量编辑工作流
- **加载ODD定制**，将模式约束到项目特定的子集
- 用正则表达式模式在所有实体类型中**搜索**

## 安装

```bash
pip install tei-mcp
```

或直接运行：

```bash
uvx tei-mcp
```

## 用法

添加到任何兼容MCP的客户端（Claude、Cursor、Windsurf等）：

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

源代码与文档请见[GitHub仓库](https://github.com/Pantagrueliste/tei-mcp)。
