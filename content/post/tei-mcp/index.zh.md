---
title: "tei-mcp：面向AI智能体的TEI P5"
subtitle: 一个帮助AI助手理解TEI指南的MCP服务器

summary: >
  tei-mcp是一个开源MCP服务器，让AI编程助手直接访问TEI P5规范——元素查询、
  属性解析、嵌套验证、文档验证以及ODD定制。

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- 数字人文
- TEI
- MCP
- 人工智能

categories:
- 数字人文
---

如果您曾用AI编程助手编写TEI XML，大概已经注意到它会出错。元素出现在不该出现的地方。属性被凭空捏造。嵌套规则被无视。模型对TEI的样子有个大致印象，却对规范没有可靠的了解。

tei-mcp通过让AI智能体以工具方式直接访问TEI P5指南来解决这个问题。

{{< toc >}}

## 什么是MCP？

[模型上下文协议](https://modelcontextprotocol.io)（Model Context Protocol，MCP）是一项开放标准，允许AI应用连接外部数据源和工具。可以把它想成AI的USB接口：一个统一的协议，让任何兼容的客户端——Claude、Cursor、Windsurf等——都能接入专门的服务。

MCP服务器暴露出AI在对话过程中可以调用的*工具*。模型不必依赖记忆中的训练数据，而可以查询一个实时的权威来源。

## tei-mcp做什么

tei-mcp解析TEI P5的ODD规范，并暴露16个工具，涵盖编辑者或编码者最常问的问题：

- **这个元素是什么？** 按名称查询任何元素、类、宏或模块，支持不区分大小写的匹配和拼写错误建议。
- **它接受哪些属性？** 在完整的类层次结构中解析属性——先是本地属性，再按顺序列出继承的属性。
- **它里面可以放什么？** 将内容模型展开为结构化的树，或获取有效子元素的平面列表。
- **这个元素能放在这里吗？** 检查父子嵌套关系，或在完整的元素层次结构中追踪可达性。
- **我的文档有效吗？** 依据规范验证TEI XML文件：内容模型、属性值、封闭取值列表、引用完整性和弃用警告。
- **我的项目模式呢？** 加载ODD定制文件，把上述一切约束到您项目特定的TEI子集。

## 为什么重要

TEI编码需要不断查阅指南。经验丰富的编码者会内化最常见的模式，但即便是他们，遇到不太熟悉的元素或复杂的内容模型时也需要查规范。对于没有这种内化知识的AI助手来说，问题更严重：它们会幻觉出看似合理却不正确的标记。

有了tei-mcp，AI不必猜测。它可以在写下第一个尖括号之前，先到规范中查找答案。结果是符合TEI P5——或符合您项目ODD定制——的标记。

## 入门

从PyPI安装：

```bash
pip install tei-mcp
```

然后将其加入您MCP客户端的配置：

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

服务器首次运行时会下载TEI规范，并可与任何兼容MCP的客户端配合使用。

源代码与完整文档：
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
