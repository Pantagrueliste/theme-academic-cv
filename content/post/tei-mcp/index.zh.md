---
title: "tei-mcp：给AI智能体用的TEI P5"
subtitle: 一个帮AI助手读懂TEI指南的MCP服务器

summary: >
  tei-mcp是一个开源MCP服务器，让AI编程助手直接访问TEI P5规范——
  元素查询、属性解析、嵌套验证、文档验证、ODD定制。

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

如果您用AI编程助手写过TEI XML，大概已经领教过它的错误：元素放错地方，属性凭空捏造，嵌套规则视若无睹。模型对TEI长什么样有个大概印象，对规范本身却没有可靠的知识。

tei-mcp的解法，是让AI智能体通过工具直接访问TEI P5指南。

{{< toc >}}

## MCP是什么？

[模型上下文协议](https://modelcontextprotocol.io)（Model Context Protocol，MCP）是一项开放标准，让AI应用能接上外部数据源和工具。不妨把它看作AI的USB接口：一套协议，任何兼容的客户端——Claude、Cursor、Windsurf等等——都能借此接入专门的服务。

MCP服务器对外提供*工具*，AI在对话中可以随时调用。模型不必再靠记忆里的训练数据，而可以查询一个实时的、权威的来源。

## tei-mcp做什么

tei-mcp解析TEI P5的ODD规范，提供16个工具，涵盖校勘者或编码者最常问的问题：

- **这个元素是什么？** 按名称查询任何元素、类、宏或模块，不区分大小写，拼错了还会给出建议。
- **它能带哪些属性？** 沿完整的类层次解析属性——先列本地属性，再依次列出继承的属性。
- **它里面能放什么？** 把内容模型展开成结构化的树，或列出有效子元素的平面清单。
- **这个元素能放在这儿吗？** 检查父子嵌套关系，或在完整的元素层次中追踪可达性。
- **我的文档有效吗？** 依据规范验证TEI XML文件：内容模型、属性值、封闭取值列表、引用完整性、弃用警告。
- **我的项目模式呢？** 加载ODD定制文件，把上述一切约束到您项目特定的TEI子集。

## 为什么要紧

TEI编码离不开时时翻查指南。老手把最常见的模式记在心里，可遇到生僻元素或复杂的内容模型，照样得查规范。AI助手没有这种内化的知识，问题更严重：它们会幻觉出看似合理、实则错误的标记。

有了tei-mcp，AI就不必猜了。写下第一个尖括号之前，它可以先去规范里查答案。结果便是符合TEI P5——或符合您项目ODD定制——的标记。

## 上手

从PyPI安装：

```bash
pip install tei-mcp
```

然后加入您MCP客户端的配置：

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

服务器首次运行时下载TEI规范，可配合任何兼容MCP的客户端使用。

源代码与完整文档：
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
