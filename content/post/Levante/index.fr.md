---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Le Levante, géographie d’une perception"
subtitle: "Qu’évoquait le Levante dans la Florence du XVIe siècle ?"
summary: "Le Levante est un toponyme fuyant : on ne le définit jamais que par rapport à un autre territoire, ou contre lui. Quel était donc le Levante des Toscans au XVIe siècle ? Les données que j’ai tirées de la base MIA donnent une réponse à laquelle on ne s’attendait pas."
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
  caption: "Carte de densité des toponymes cités dans ASFi MdP 4277, 1543-1566"
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
Le *Levante* est un lieu qui se dérobe. On ne le définit jamais que par rapport à un autre territoire, ou contre lui ; aussi son sens n’a-t-il guère été stable, et le mot a désigné des géographies fort différentes selon le lieu et l’époque où on l’employait. Mais si une définition objective et précise reste hors de portée, on peut du moins tenter d’en dresser une carte subjective, en s’appuyant sur les corrélations qu’un corpus donné laisse apparaître. Autrement dit : quel espace le *Levante* évoquait-il pour tel groupe de lecteurs ?  
Je montre dans ce billet comment exploiter les données de la [base MIA](https://mia.medici.org/) du Medici Archive Project 
pour visualiser les lieux auxquels ce toponyme se trouvait associé.  

# La base MIA
MIA est une plateforme collaborative où les chercheurs déposent et partagent leurs propres photographies de documents conservés aux [Archives d’État de Florence](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Depuis un an, avec le soutien du [National Endowment for the Humanities](https://www.neh.gov), notre équipe a photographié, transcrit, résumé et classé des milliers de documents de la section des *avvisi* du fonds *Mediceo del Principato*. La base n’a pas été conçue d’abord pour l’analyse statistique ; il n’en reste pas moins que les métadonnées que nous avons mises en ligne se laissent télécharger et traiter comme des jeux de données.

# Le jeu de données
Le jeu que j’ai constitué ici couvre toutes les nouvelles du *Levante* de 1543 à 1566, c’est-à-dire du premier avviso conservé dans le fonds jusqu’à l’année de la mort du sultan [Soliman I^er^](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). En voici un échantillon, tel que je l’ai extrait du serveur : trois colonnes, avec le numéro unique du document, un nom de lieu et une date.

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

## Toilette des données
Avant toute visualisation, il faut mettre ces données au format csv (valeurs séparées par des virgules), et traduire l’information géographique qu’elles contiennent dans une langue que la machine entende mieux : celle des coordonnées GPS. Comme le jeu compte des centaines d’entrées, on préférera automatiser l’opération. Des modèles de langue pré-entraînés comme [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) ou [AI-21](https://www.ai21.com), pour ne citer qu’eux, s’en acquittent vite et plutôt bien ; mais il faut les surveiller de près, car ces modèles ont une légère propension à l’hallucination.


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
Une carte de densité fait ressortir la fréquence avec laquelle chaque lieu est cité dans un jeu de données. On y lit non seulement l’étendue géographique du corpus, mais aussi ses foyers : quels lieux reviennent sans cesse, lesquels ne font que passer ? Où sont les centres, et jusqu’où s’étend la périphérie ? Vers quel point de la carte, en somme, l’attention d’un lecteur avait-elle le plus de chances de se porter ?

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Pour cette expérience – et parce que le temps pressait – j’ai eu recours à l’une des API de [Mapbox](https://www.mapbox.com) ; mais bien des bibliothèques de visualisation et des systèmes d’information géographique produisent le même genre de carte.

# Quelques observations
Le résultat tient plus du tableau impressionniste que de la représentation exacte d’un concept bien délimité, et c’est justement ce qui me plaît dans l’exercice : {{< hl >}}la science des données peut être une alliée précieuse des humanités, sans que nous soyons tenus pour autant de nous plier à ses règles.{{< /hl >}}

Autre enseignement : la carte fait voir un *Levante* pleinement intégré au reste de l’Europe et de la Méditerranée. Elle met en lumière la place centrale d’Edirne dans la géographie politique de l’Empire ottoman. La ville d’Espagne qui y pèse le plus n’est ni Madrid ni l’Escurial, mais Naples. Enfin, et ce n’est pas le moindre, les îles et les petites cités-États comme Raguse semblent avoir joué un rôle d’intermédiaire de premier plan entre les puissances de la région.


# Comment obtenir les données de MIA
MIA est un remarquable outil de travail collectif, mais les données de ses serveurs ne se laissent pas prendre facilement ; la salle des machines, par exemple, n’est publiée dans aucun dépôt public. On peut cependant les obtenir en s’inscrivant sur MIA, puis en interrogeant le serveur depuis Python.

### Requête
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Remplacez LOGIN et PASSWORD par vos propres identifiants.

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
### Charger l’objet JSON dans un dictionnaire
```python
json_complete = json.load(f)
```
### Extraire les données du JSON et les écrire au format CSV
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

Une fois le fichier `results.csv` en main, il ne reste qu’à procéder à la toilette des données décrite plus haut.
