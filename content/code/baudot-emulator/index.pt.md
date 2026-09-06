---
title: Emulador de telégrafo ITA2
summary: Uma demonstração interativa do código telegráfico ITA2 (Baudot-Murray) que ajuda os estudantes a apreender os conceitos fundamentais da codificação binária e das máquinas de estados.
tags:
  - JavaScript
  - Interativo
  - Ensino

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Fita de telégrafo ITA2 com uma mensagem codificada
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
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

Este emulador ITA2 é um auxiliar pedagógico de uso prático: dá forma visível e interativa a conceitos abstratos de codificação. Quando os estudantes escrevem um texto e o veem converter-se de imediato em padrões de furos, estão a aprender vários conceitos-chave da informática e das telecomunicações.

## Vantagens pedagógicas

Em primeiro lugar, demonstra a representação binária – como um texto se converte em sequências de 1 e 0. Costumamos ensiná-la em abstrato; ora, ver os furos aparecerem na fita ajuda os estudantes a perceber como um sistema físico pode representar informação digital.

{{< Baudot >}}

O mecanismo de comutação LETTERS/FIGURES (letras/algarismos) introduz as máquinas de estados com toda a naturalidade. Experimentando, os estudantes descobrem que o mesmo padrão pode representar caracteres diferentes consoante o modo ativo. Esta experiência direta da codificação dependente de um estado prepara-os para conceitos informáticos mais complexos.

## Pormenores de implementação

O emulador está escrito em JavaScript e HTML/CSS, o que o torna fácil de incorporar em qualquer página web. O código é modular e pode adaptar-se a diferentes contextos educativos.

O código-fonte está disponível, e o emulador pode ser experimentado, no [repositório GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).