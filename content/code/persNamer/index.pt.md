---
title: persNamer
summary: Uma ferramenta em Python que converte identificadores VIAF em entradas de pessoa e etiquetas de anotação em XML TEI, simplificando o controlo de autoridade nas edições académicas digitais.
tags:
  - XML
  - TEI
  - Humanidades digitais
  - Python
  - VIAF
  - Dados ligados

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Demonstração do persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
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

## persNamer: ligar a TEI ao Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

O persNamer é uma ferramenta especializada em Python que simplifica a integração de dados de autoridade sobre pessoas, provenientes do VIAF (Virtual International Authority File), em documentos XML TEI. Ao converter identificadores VIAF em marcação TEI pronta a usar, o persNamer reduz consideravelmente o trabalho manual de criação de entradas estruturadas de pessoas para as edições académicas digitais.

## O desafio do controlo de autoridade em TEI

As edições académicas digitais exigem muitas vezes a identificação precisa de personagens históricas, com os seus nomes normalizados e datas de vida. Manter um controlo de autoridade coerente ao longo de um projeto obriga a:

1. Identificar as pessoas nos textos históricos
2. Encontrar dados de autoridade a seu respeito
3. Criar entradas TEI corretamente formatadas
4. Garantir referências coerentes em todo o projeto

Estes passos são, por norma, manuais, demorados e propensos a incoerências.

## Como funciona o persNamer

O persNamer automatiza este fluxo de trabalho:

1. **Obtenção dos dados VIAF**: a partir de um identificador VIAF, a ferramenta recupera os dados RDF por negociação de conteúdo HTTP
2. **Extração da informação essencial**: analisa o RDF para extrair o nome preferido, a data de nascimento e a data de morte
3. **Geração da marcação TEI**: cria dois fragmentos XML essenciais:
   - Uma **entrada de ficheiro de autoridade** (elemento `<person>` com um `xml:id` gerado, `<persName>`, `<birth>`, `<death>` e `<idno type="VIAF">`)
   - Uma **etiqueta de anotação** separada (`<persName>` com um atributo `ref` que remete para a entrada de autoridade)

Esta dupla saída permite aos editores manter um ficheiro de autoridade centralizado e, ao mesmo tempo, inserir facilmente etiquetas de anotação nos seus textos TEI.

## Características principais

- **Geração normalizada de identificadores**: cria IDs XML coerentes no formato `pers-[familyname]-[givenname initial]` (p. ex., `pers-deteligny-c`)
- **Análise de RDF**: usa o `rdflib` para extrair informação de várias propriedades RDF (p. ex., `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interface de linha de comandos**: execução simples, com o número VIAF como único argumento obrigatório
- **Saída detalhada**: fornece informação pormenorizada sobre o processamento, a par do XML final

## Exemplo de utilização

```bash
python persNamer.py 314802260
```

Este comando produz:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Aplicações nas humanidades digitais

O persNamer é particularmente útil para:

- Edições académicas digitais que exijam controlo de autoridade
- Projetos de codificação TEI que trabalhem com figuras históricas
- Iniciativas de dados ligados que liguem documentos a registos de autoridade
- Garantir a coerência em grandes corpora TEI
- Ensinar os conceitos do controlo de autoridade em cursos de humanidades digitais

## Implementação

O persNamer está escrito em Python e depende de:
- `requests` para os pedidos HTTP
- `rdflib` para a análise de RDF
- `lxml` para o tratamento de XML

O código-fonte e a documentação estão no [repositório GitHub](https://github.com/Pantagrueliste/persNamer).