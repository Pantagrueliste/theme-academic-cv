---
title: O arquivo num relance
subtitle: Como as visualizações interativas de dados enriquecem a investigação em arquivo

# Summary for listings and search engines
summary: As aplicações web de tipo dashboard aumentam a consciência situacional no arquivo, melhorando por fim a acessibilidade deste e a produtividade dos investigadores

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanidades digitais
- Visualização de dados
- Investigação em arquivo
- Investigação em curso

categories:
- Notas
---

# O problema
Os arquivos históricos podem ser de uma desordem intimidante. O *Mediceo del Principato*, no [Arquivo de Estado de Florença](https://www.archiviodistato.firenze.it/asfi/home), é um caso exemplar. Com efeito, só uma pequena parte está inventariada, e muitos dos seus documentos andam dispersos por mais de 6500 volumes sem razão aparente. Para complicar as coisas, o arquivo só permite consultar um número limitado de volumes – ou *filze*, como lá lhes chamam: maços, diríamos nós. Em tempos normais, o limite é de 4 *filze* por dia; em tempo de pandemia, porém, desceu para 4 de duas em duas semanas. Na falta de inventários detalhados, a dimensão considerável do arquivo obriga os investigadores a engendrar estratégias para encontrar depressa os documentos que procuram.

# A solução
Uns preferem confiar no acaso; outros tentam também fazer conjeturas informadas a partir da cronologia, dos destinatários, dos autores, da origem do fundo de arquivo, da língua, etc. *Olhar* para todas estas variáveis ao mesmo tempo, porém, pode revelar padrões inesperados na estrutura do arquivo e melhorar as nossas conjeturas. A minha experiência mostra que, uma vez representados graficamente, os metadados que os investigadores costumam reunir numa folha de cálculo aumentam significativamente a consciência situacional no arquivo.

# A experiência
A minha investigação atual centra-se na correspondência de um espião do século XVI. As suas cartas estão espalhadas por centenas de *filze*. Foram escritas sob identidades diferentes, a destinatários diferentes e por vezes inesperados, de lugares diferentes, etc. Para encontrar as *filze* com mais probabilidade de conter as cartas esperadas, montei um dashboard, uma aplicação web de visualização interativa de dados ([Plotly Dash](https://plotly.com/dash/)) que cruza informação de toda a espécie, geográfica e cronológica incluída, com um diagrama hierárquico ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) do fundo de arquivo. O dashboard diz-me num relance o que já foi encontrado, quanto isso representa, e dá-me uma ideia aproximada de onde poderia procurar cartas novas. Além disso, ao clicar em variáveis específicas, todos os diagramas se atualizam para mostrar correlações particulares.

# Próximos passos
Mais importante ainda, talvez: este dashboard pode ser reconvertido em índice visual. Quando a edição crítica destas cartas for publicada em linha, o dashboard funcionará como porta de entrada alternativa, a partir da qual os leitores poderão percorrer os dados. Por razões de confidencialidade, só posso mostrar por agora uma captura de ecrã com partes ocultadas, mas divulgarei o dashboard completo no próximo ano. Entretanto, um protótipo estará disponível em breve. Fiquem atentos!