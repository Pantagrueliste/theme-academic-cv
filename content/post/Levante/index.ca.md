---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Una geografia perceptiva del Levante"
subtitle: "Amb què s’associava el Levante a la Florència del segle XVI?"
summary: "El Levante és un topònim esquiu: sol definir-se en relació amb – o per oposició a – un altre territori. Quin era, doncs, el Levante de la Toscana al segle XVI? Les dades que he extret de la base de dades MIA donen una resposta inesperada."
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
  caption: "Mapa de densitat dels topònims esmentats a ASFi MdP 4277, de 1543 a 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Introducció
El *Levante* és un lloc esquiu. Definit habitualment en relació amb – o per oposició a – un altre territori, el seu significat poques vegades ha estat estable, i ha evocat geografies diferents segons el lloc i el moment en què es feia servir el terme. Ara bé, si costa articular-ne una definició objectiva i precisa, sempre es pot aspirar a dibuixar un mapa subjectiu d’aquesta regió, prenent com a base les correlacions que existeixen dins d’un corpus de textos determinat. Dit d’una altra manera: quin espai podia evocar el *Levante* a un grup concret de lectors?  
En aquesta entrada mostraré com fer servir les dades de la [base de dades MIA](https://mia.medici.org/) del Medici Archive Project 
per visualitzar els llocs concrets amb què s’associava el topònim.  

# La base de dades MIA
La base de dades MIA és una plataforma col·laborativa per als estudiosos que volen pujar-hi i compartir les seves pròpies fotografies de material d’arxiu de l’[Arxiu d’Estat de Florència](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Durant l’últim any, i sota el patrocini del [National Endowment for the Humanities](https://www.neh.gov), el nostre equip ha fotografiat, transcrit, resumit i classificat milers de documents conservats a la secció d’*avvisi* de l’arxiu *Mediceo del Principato* de Florència. Tot i que la nostra base de dades no es va pensar en primer lloc per a l’anàlisi estadística, les metadades que hem posat a disposició es poden descarregar i fer servir com a conjunts de dades. 

# El conjunt de dades
En aquest cas, el conjunt de dades que he creat cobreix totes les notícies del *Levante* de 1543 a 1566, és a dir, des del primer avviso registrat als arxius fins a l’any de la mort del sultà [Solimà I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Heus aquí una mostra de les dades que he extret del servidor. Amb tres columnes, les dades consisteixen en un número de document únic, un nom de lloc i una data. 

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

## Netejar les dades
Per visualitzar aquestes dades, cal fer-les llegibles com a conjunt de dades csv (valors separats per comes). També cal convertir la informació geogràfica que contenen a un format més «amable per a les màquines»: les coordenades GPS. Com que el conjunt de dades conté centenars d’entrades, val més automatitzar el procés. Això es pot fer força de pressa i amb bastanta precisió amb models de llengua preentrenats com ara [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) o [AI-21](https://www.ai21.com), per esmentar-ne només uns quants. Aquesta operació, però, s’ha de supervisar de prop, perquè els models de llengua preentrenats tenen una lleugera tendència a al·lucinar.


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

# El mapa de densitat.
Un mapa de densitat és un tipus de visualització que destaca la freqüència amb què s’esmenta un lloc en un conjunt de dades determinat. És especialment útil per entendre no només l’abast geogràfic de les dades, sinó també els seus punts focals. Quins llocs del mapa s’esmenten més sovint? I quins són més episòdics? On són els centres, i fins on arriba la perifèria? En quin punt del mapa és més probable que es concentri l’atenció del lector? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Per a aquest experiment – i com que tenia pressa – vaig fer servir una de les API de [Map Box](https://www.mapbox.com). Tanmateix, moltes biblioteques de visualització i sistemes d’informació geogràfica permeten produir el mateix tipus de mapa de densitat. 

# Unes quantes observacions
El resultat és més un quadre impressionista que la representació precisa d’un concepte clarament definible, i això és justament el que m’agrada d’aquest experiment. En efecte, {{< hl >}}si bé la ciència de dades pot ser una aliada poderosa de les humanitats, no necessàriament ens hem de sotmetre a les seves regles.{{< /hl >}}

Un altre aspecte interessant d’aquest experiment és que el mapa revela un *Levante* completament integrat amb la resta d’Europa i de la Mediterrània. També posa en relleu la centralitat d’Edirne en la geografia política de l’Imperi Otomà. A més, la ciutat espanyola més rellevant del mapa no és Madrid ni l’Escorial, sinó Nàpols. I, per acabar, les illes i les petites ciutats estat com ara Ragusa semblen tenir un paper important com a mediadores entre les diferents potències de la regió.  


# Com sol·licitar dades a MIA
Tot i que MIA és una eina col·laborativa excel·lent per als investigadors, les dades que emmagatzema als seus servidors no són fàcilment accessibles. El seu *back-end*, per exemple, no està publicat en repositoris públics. Tanmateix, es poden obtenir les dades registrant-se a MIA i fent peticions al servidor amb Python.

### Petició
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Assegura’t de substituir LOGIN i PASSWORD per les teves pròpies credencials.

### Escriure la resposta en un fitxer
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Obrir el JSON
```python
f = open('response.json', encoding="utf8")
```
### Retornar l’objecte JSON com a diccionari
```python
json_complete = json.load(f)
```
### Seleccionar les dades del JSON i imprimir-les en format CSV
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

Un cop descarregat el fitxer `results.csv`, pots passar a netejar les dades tal com s’ha explicat més amunt. 