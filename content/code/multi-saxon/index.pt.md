---
title: Multi-Saxon
summary: Uma ferramenta de alto desempenho para transformações XSLT 2.0/3.0 em paralelo sobre grandes corpora XML TEI, capaz de executar transformações que o LXML não consegue processar.
tags:
  - XSLT
  - XML
  - TEI
  - Humanidades digitais
  - Python
  - Java
  - Desempenho

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: O Multi-Saxon em ação
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
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

## Multi-Saxon: processamento XSLT em paralelo para grandes corpora TEI

O Multi-Saxon colmata uma lacuna crítica das ferramentas de processamento de XML: permite executar em paralelo transformações XSLT 2.0 e 3.0 que o LXML (uma biblioteca Python de XML muito usada) não consegue processar. Concebido especificamente para grandes coleções de documentos XML TEI, o Multi-Saxon acelera consideravelmente o processamento graças a uma execução paralela eficiente.

## Características principais

- **XSLT avançado**: processa transformações XSLT 2.0 e 3.0, para lá das capacidades do LXML
- **Processamento paralelo**: reduz drasticamente o tempo de transformação de grandes coleções de documentos graças à paralelização
- **Otimizado para TEI**: concebido especificamente para documentos XML da Text Encoding Initiative (TEI)
- **Desempenho escalável**: lida eficientemente com corpora de centenas a milhares de documentos
- **Multiplataforma**: funciona em diferentes sistemas operativos e ambientes

## O problema que o Multi-Saxon resolve

Os investigadores em humanidades digitais que trabalham com TEI deparam-se muitas vezes com dois obstáculos importantes:

1. O LXML (biblioteca Python corrente para o processamento de XML) só aceita XSLT 1.0, o que impede o uso das funcionalidades mais avançadas do XSLT 2.0/3.0
2. Processar sequencialmente grandes corpora de documentos TEI pode levar um tempo proibitivo

O Multi-Saxon responde a ambos os problemas tirando partido das capacidades XSLT avançadas do Saxon e distribuindo o processamento por vários núcleos, com ganhos de desempenho significativos.

## Implementação

O Multi-Saxon combina Python com o processador Saxon, em Java, para criar um pipeline de transformação de alto desempenho:

- Usa a biblioteca Java Saxon para um processamento robusto de XSLT 2.0/3.0
- Implementa multiprocessamento para distribuir as transformações pelos núcleos de CPU disponíveis
- Gere eficientemente os pools de processadores para maximizar o débito
- Oferece uma interface simples para o processamento em lote de documentos TEI

## Exemplo de utilização

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Impacto para as humanidades digitais

Para os projetos de humanidades digitais que lidam com grandes coleções de documentos TEI, o Multi-Saxon permite:

- Transformações complexas à escala do corpus, impossíveis com o LXML
- Tempos de processamento drasticamente reduzidos (muitas vezes por fatores de 5 a 10 em sistemas multinúcleo)
- Análises mais sofisticadas graças às funcionalidades avançadas do XSLT 2.0/3.0
- Um fluxo de trabalho simplificado para processar coleções inteiras de documentos

O código-fonte e a documentação estão no [repositório GitHub](https://github.com/Pantagrueliste/multi-saxon).
