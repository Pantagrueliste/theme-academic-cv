---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Uma geografia percebida do Levante"
subtitle: "A que se associava o Levante na Florença do século XVI?"
summary: "O Levante é um topónimo esquivo: define-se quase sempre em relação a – ou por oposição a – outro território. O que era, então, o Levante da Toscana no século XVI? Os dados que recolhi na base de dados MIA dão uma resposta inesperada."
authors: [clement]
tags: [MAP, Avviso]
categories: [Notas]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Mapa de densidade dos topónimos mencionados no ASFi MdP 4277, de 1543 a 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Introdução
O *Levante* é um lugar esquivo. Definido em geral em relação a – ou por oposição a – outro território, o seu sentido raramente foi estável, evocando geografias diferentes consoante o lugar e a época em que o termo era usado. Ora, se é difícil articular uma definição objetiva e exata do termo, pode-se ainda assim tentar traçar um mapa subjetivo dessa região, tomando por base as correlações existentes num dado corpus de textos. Por outras palavras: que espaço podia o *Levante* evocar para um grupo determinado de leitores?  
Neste artigo, mostro como usar os dados da [base de dados MIA](https://mia.medici.org/) do Medici Archive Project 
para visualizar os lugares concretos a que o topónimo estava associado.  

# A base de dados MIA
A MIA é uma plataforma colaborativa para investigadores que queiram carregar e partilhar as suas próprias fotografias de documentos do [Arquivo de Estado de Florença](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Ao longo do último ano, e sob o patrocínio do [National Endowment for the Humanities](https://www.neh.gov), a nossa equipa fotografou, transcreveu, resumiu e classificou milhares de documentos guardados na secção dos *avvisi* do fundo *Mediceo del Principato*, em Florença. Embora a base de dados não tenha sido concebida para análise estatística, os metadados que disponibilizámos podem ser descarregados e usados como conjuntos de dados. 

# O conjunto de dados
Neste caso, o conjunto de dados que criei cobre todas as notícias do *Levante* de 1543 a 1566, isto é, do primeiro avviso registado no arquivo ao ano da morte do sultão [Solimão I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Eis uma amostra dos dados que extraí do servidor. Dispostos em três colunas, indicam um número único de documento, um nome de lugar e uma data. 

```csv
57386 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57386 Modon / Messinias, Nomos / Peloponnisos / Ellas 1565-1-3
57386 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57386 Evvoia / Evvoias, Nomos / Sterea Ellas-Evvoia / Ellas 1565-1-3
57386 Venetian Republic / Italia / Europe / World 1565-1-3
57386 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57386 Black Sea / Asia / World / Top of the TGN hierarchy 1565-1-3
57389 Otranto / Lecce / Puglia / Italia 1565-1-3
57389 Nisoi Aiyaiou / Ellas / Europe / World  1565-1-3
57389 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57389 Buda / Budapest / Budapest / Magyarorszag 1565-1-3
57389 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57389 Kipros / Asia / World / Top of the TGN hierarchy  1565-1-3
57389 Rodhos / Rodos, Nisos / Sporadhes / Nisoi Aiyaiou 1565-1-3
57389 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57389 Çorlu / Thraki / Ellas / Europe 1565-1-3
```

## Limpar os dados
Para visualizar estes dados, é preciso torná-los legíveis como um ficheiro csv (valores separados por vírgulas). É preciso ainda converter a informação geográfica aqui incluída num formato mais «amigo da máquina»: coordenadas GPS. Como o conjunto contém centenas de entradas, mais vale automatizar o processo. Consegue-se com bastante rapidez e precisão recorrendo a modelos de linguagem pré-treinados como o [GPT-3](https://wwww.openai.org), o [Bloom](https://huggingface.co/bigscience/bloom) ou o [AI-21](https://www.ai21.com), para citar apenas alguns. A operação exige, contudo, supervisão atenta, pois os modelos de linguagem pré-treinados têm uma ligeira tendência para alucinar.


```csv
documentId,latitude,longitude,documentDate
57386,35.899167,14.514167,1565-1-3
57386,37.05,22.116667,1565-1-3
57386,31.200028,29.918719,1565-1-3
57386,38.366667,23.666667,1565-1-3
57386,45.438333,12.331333,1565-1-3
57386,41.018611,28.984444,1565-1-3
57386,42.7,18.8,1565-1-3
57389,40.216667,18.166667,1565-1-3
57389,37.966667,23.716667,1565-1-3
57389,35.899167,14.514167,1565-1-3
57389,47.4925,19.051389,1565-1-3
57389,31.200028,29.918719,1565-1-3
57389,34.916667,33.616667,1565-1-3
57389,36.405419,28.227778,1565-1-3
57389,41.018611,28.984444,1565-1-3
57389,41.133333,27.416667,1565-1-3
```

# O mapa de densidade.
Um mapa de densidade é um tipo de visualização que realça a frequência com que um lugar é mencionado num dado conjunto de dados. É particularmente útil para perceber não só o alcance geográfico dos dados, mas também os seus pontos focais. Que lugares do mapa são mencionados com mais frequência? Quais são mais episódicos? Onde estão os centros, e a que distância fica a periferia? Em que zona do mapa é mais provável que se concentre a atenção de um leitor? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Para efeitos desta experiência – e como estava com pressa – usei uma das APIs da [Map Box](https://www.mapbox.com). Muitas bibliotecas de visualização e muitos sistemas de informação geográfica permitem, porém, produzir o mesmo tipo de mapa de densidade. 

# Algumas observações
O resultado é mais um quadro impressionista do que a representação exata de um conceito claramente definível, e é precisamente isso que me agrada nesta experiência. Com efeito, {{< hl >}}a ciência de dados pode ser uma aliada poderosa das humanidades, mas não somos obrigados a seguir-lhe as regras.{{< /hl >}}

Outro aspeto interessante da experiência é que o mapa revela um *Levante* completamente integrado no resto da Europa e do Mediterrâneo. Sublinha também a centralidade de Edirne na geografia política do Império Otomano. Além disso, a cidade espanhola mais relevante no mapa não é Madrid nem o Escorial, mas Nápoles. Por último, mas não menos importante, as ilhas e as pequenas cidades-Estado como Ragusa parecem ter desempenhado um papel importante de mediação entre as diferentes potências da região.  


# Como pedir dados à MIA
Embora a MIA seja uma ferramenta colaborativa notável para os investigadores, os dados que guarda nos seus servidores não são de acesso fácil. O seu back-end, por exemplo, não está publicado em repositórios públicos. Ainda assim, é possível obter os dados registando-se na MIA e fazendo pedidos ao servidor em Python.

### Pedido
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Não se esqueça de substituir LOGIN e PASSWORD pelas suas próprias credenciais.

### Escrever a resposta num ficheiro
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Abrir o JSON
```python
f = open('response.json', encoding="utf8")
```
### Devolver o objeto JSON como dicionário
```python
json_complete = json.load(f)
```
### Selecionar os dados do JSON e imprimi-los em formato CSV
```python
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['documentId', 'placeCited', 'documentDate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in json_complete['data']:
        if i['topics'] != None:
            for x in i['topics']:
                documentId=x['documentId']
                placeCited=x['topicPlaceName']
                year=i['date']['docYear']
                month=i['date']['docMonth']
                day=i['date']['docDay']
                documentDate=str(year)+ "-" + str(month)+"-" + str(day)
                writer.writerow({'documentId': documentId, 'placeCited': placeCited, 'documentDate': documentDate})
```

Depois de descarregar o ficheiro `results.csv`, pode passar à limpeza dos dados, como se explicou acima. 