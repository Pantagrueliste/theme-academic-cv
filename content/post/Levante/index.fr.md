---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Une géographie perceptive du Levante"
subtitle: "À quoi le Levante était-il associé dans la Florence du XVIe siècle ?"
summary: "Le Levante est un toponyme insaisissable, car on le définit généralement par rapport à – ou par opposition à – un autre territoire. Qu’était donc le Levante de la Toscane au XVIe siècle ? Les données que j’ai recueillies dans la base MIA apportent une réponse inattendue."
authors: [clement]
tags: [MAP, Avviso]
categories: [Notes]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Carte de densité des toponymes mentionnés dans ASFi MdP 4277, de 1543 à 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Introduction
Le *Levante* est un lieu insaisissable. Généralement défini par rapport à – ou par opposition à – un autre territoire, son sens a rarement été stable, évoquant des géographies différentes selon le lieu et l’époque où le terme était employé. Pourtant, s’il est difficile d’en articuler une définition objective et précise, on peut encore espérer dresser une carte subjective de cette région, en prenant pour base les corrélations qui existent au sein d’un corpus de textes donné. Autrement dit, quel espace le *Levante* pouvait-il évoquer pour un groupe de lecteurs déterminé ?  
Dans ce billet, je vous montre comment utiliser les données de la [base MIA](https://mia.medici.org/) du Medici Archive Project 
pour visualiser les lieux précis auxquels ce toponyme était associé.  

# La base MIA
La base MIA est une plateforme collaborative destinée aux chercheurs qui souhaitent téléverser et partager leurs propres photographies de documents d’archives conservés aux [Archives d’État de Florence](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Au cours de l’année écoulée, et sous le patronage du [National Endowment for the Humanities](https://www.neh.gov), notre équipe a photographié, transcrit, résumé et classé des milliers de documents conservés dans la section des *avvisi* du fonds *Mediceo del Principato* à Florence. Bien que notre base n’ait pas été conçue en premier lieu pour l’analyse statistique, les métadonnées que nous avons mises à disposition peuvent néanmoins être téléchargées et utilisées comme jeux de données.

# Le jeu de données
Dans le cas présent, le jeu de données que j’ai constitué couvre toutes les nouvelles du *Levante* de 1543 à 1566, c’est-à-dire du premier avviso enregistré dans les archives jusqu’à l’année de la mort du sultan [Soliman I^er^](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Voici un échantillon des données que j’ai extraites du serveur. Composées de trois colonnes, elles comprennent un numéro de document unique, un nom de lieu et une date.

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

## Nettoyer les données
Pour visualiser ces données, il faut les rendre lisibles sous forme de jeu de données csv (valeurs séparées par des virgules). Il faut aussi convertir les informations géographiques qu’elles contiennent dans un format plus « lisible par la machine » : des coordonnées GPS. Le jeu de données comptant des centaines d’entrées, mieux vaut automatiser ce processus. On peut le faire assez rapidement et avec une bonne précision à l’aide de modèles de langue pré-entraînés comme [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) ou [AI-21](https://www.ai21.com), pour n’en citer que quelques-uns. Cette opération doit toutefois être étroitement supervisée, car les modèles de langue pré-entraînés ont une légère tendance à halluciner.


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

# La carte de densité
Une carte de densité est un type de visualisation qui met en évidence la fréquence à laquelle un lieu est mentionné dans un jeu de données donné. Elle est particulièrement utile pour comprendre non seulement l’étendue géographique de ses données, mais aussi leurs points focaux. Quels lieux de la carte sont mentionnés le plus souvent ? Et lesquels ne le sont qu’épisodiquement ? Où sont les centres, et à quelle distance se trouve la périphérie ? Sur quelle partie de la carte l’attention d’un lecteur a-t-elle le plus de chances de se porter ?

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Pour les besoins de cette expérience – et comme j’étais pressé – j’ai utilisé l’une des API de [Mapbox](https://www.mapbox.com). Mais de nombreuses bibliothèques de visualisation et de nombreux systèmes d’information géographique permettent de produire le même type de carte de densité.

# Quelques observations
Le résultat tient davantage du tableau impressionniste que de la représentation exacte d’un concept clairement définissable, et c’est précisément ce qui me plaît dans cette expérience. En effet, {{< hl >}}si la science des données peut être une alliée puissante des humanités, nous ne sommes pas nécessairement tenus de nous plier à ses règles.{{< /hl >}}

Un autre aspect intéressant de cette expérience est que la carte révèle un *Levante* complètement intégré au reste de l’Europe et de la Méditerranée. Elle souligne aussi la centralité d’Edirne dans la géographie politique de l’Empire ottoman. En outre, la ville la plus importante de l’Espagne sur la carte n’est ni Madrid ni l’Escurial, mais Naples. Enfin, et ce n’est pas le moins important, les îles et les petites cités-États comme Raguse semblent jouer un rôle important de médiation entre les différentes puissances de la région.


# Comment demander des données à MIA
Bien que MIA soit un remarquable outil collaboratif pour les chercheurs, les données stockées sur ses serveurs ne sont pas facilement accessibles. Son back-end, par exemple, n’est pas publié dans des dépôts publics. Vous pouvez néanmoins obtenir les données en vous inscrivant à MIA et en adressant des requêtes au serveur avec Python.

### Requête
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Veillez à remplacer LOGIN et PASSWORD par vos propres identifiants.

### Écrire la réponse dans un fichier
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Ouvrir le JSON
```python
f = open('response.json', encoding="utf8")
```
### Renvoyer l’objet JSON sous forme de dictionnaire
```python
json_complete = json.load(f)
```
### Sélectionner les données du JSON et les écrire au format CSV
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

Une fois le fichier `results.csv` téléchargé, vous pouvez procéder au nettoyage des données comme expliqué plus haut.
