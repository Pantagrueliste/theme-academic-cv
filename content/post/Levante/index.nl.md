---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Een perceptuele geografie van de Levante"
subtitle: "Waarmee werd de Levante in het Florence van de zestiende eeuw geassocieerd?"
summary: "De Levante is een ongrijpbaar toponiem: het wordt doorgaans gedefinieerd in relatie tot – of in tegenstelling tot – een ander gebied. Wat was dan de Levante van Toscane in de zestiende eeuw? De gegevens die ik uit de MIA-database heb gehaald, geven een onverwacht antwoord."
authors: [clement]
tags: [MAP, Avviso]
categories: [Notities]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
draft: false
machine_translated: true


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Dichtheidskaart van de toponiemen die van 1543 tot 1566 in ASFi MdP 4277 worden genoemd"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Inleiding
De *Levante* is een ongrijpbare plek. Doorgaans gedefinieerd in relatie tot – of in tegenstelling tot – een ander gebied, heeft de term zelden een vaste betekenis gehad: naargelang van waar en wanneer hij werd gebruikt, riep hij andere geografieën op. Maar al valt een objectieve en precieze definitie moeilijk te formuleren, men kan toch hopen een subjectieve kaart van die regio te tekenen, op basis van de correlaties die binnen een bepaald tekstcorpus bestaan. Met andere woorden: welke ruimte kon de *Levante* voor een specifieke groep lezers oproepen?  
In dit bericht laat ik zien hoe je met gegevens uit de [MIA-database](https://mia.medici.org/) van het Medici Archive Project 
de specifieke plaatsen kunt visualiseren waarmee het toponiem werd geassocieerd.  

# De MIA-database
De MIA-database is een samenwerkingsplatform voor onderzoekers die hun eigen foto's van archiefmateriaal uit het [Staatsarchief van Florence](https://archiviodistatofirenze.cultura.gov.it/asfi/home) willen uploaden en delen. Het afgelopen jaar heeft ons team, met steun van het [National Endowment for the Humanities](https://www.neh.gov), duizenden documenten uit de *avvisi*-afdeling van het archief *Mediceo del Principato* in Florence gefotografeerd, getranscribeerd, samengevat en geclassificeerd. Onze database was weliswaar niet in de eerste plaats voor statistische analyse bedoeld, maar de metadata die we beschikbaar hebben gesteld, kunnen wel worden gedownload en als dataset worden gebruikt. 

# De dataset
De dataset die ik in dit geval heb aangemaakt, omvat alle nieuwsberichten uit de *Levante* van 1543 tot 1566, dat wil zeggen van de eerste in het archief geregistreerde avviso tot het sterfjaar van sultan [Süleyman I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Hier is een staaltje van de gegevens die ik van de server heb gehaald. Ze bestaan uit drie kolommen: een uniek documentnummer, een plaatsnaam en een datum. 

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

## De gegevens opschonen
Om deze gegevens te visualiseren, moeten we ze leesbaar maken als csv-dataset (comma separated values). Ook moeten we de geografische informatie omzetten in een “machinevriendelijker” formaat: gps-coördinaten. Omdat de dataset honderden regels telt, automatiseren we dat liever. Dat kan vrij snel en behoorlijk nauwkeurig met voorgetrainde taalmodellen als [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) of [AI-21](https://www.ai21.com), om er maar een paar te noemen. De operatie vraagt wel om nauwlettend toezicht, want voorgetrainde taalmodellen hebben een lichte neiging tot hallucineren.


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

# De dichtheidskaart.
Een dichtheidskaart is een visualisatie die laat zien hoe vaak een plaats in een bepaalde dataset wordt genoemd. Dat is bijzonder nuttig om niet alleen de geografische reikwijdte van je gegevens te begrijpen, maar ook hun brandpunten. Welke plaatsen op de kaart worden vaker genoemd? En welke slechts af en toe? Waar liggen de centra, en hoe ver reikt de periferie? Waar op de kaart richt de aandacht van een lezer zich het waarschijnlijkst? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Voor dit experiment – en omdat ik haast had – gebruikte ik een van de API's van [Mapbox](https://www.mapbox.com). Maar ook heel wat visualisatiebibliotheken en geografische informatiesystemen laten je hetzelfde soort dichtheidskaart maken. 

# Enkele observaties
Het resultaat is eerder een impressionistisch tableau dan de nauwkeurige weergave van een scherp omlijnd begrip, en dat is precies wat me aan dit experiment bevalt. {{< hl >}}Datawetenschap kan immers een machtige bondgenoot van de geesteswetenschappen zijn, maar dat betekent nog niet dat we ons aan haar regels moeten houden.{{< /hl >}}

Een ander interessant aspect van dit experiment is dat de kaart een *Levante* laat zien die volledig verweven is met de rest van Europa en de Middellandse Zee. Ook wordt duidelijk hoe centraal Edirne stond in de politieke geografie van het Ottomaanse Rijk. Bovendien is de belangrijkste Spaanse stad op de kaart Madrid noch het Escorial, maar Napels. En last but not least lijken eilanden en kleine stadstaten als Ragusa een belangrijke bemiddelende rol te hebben gespeeld tussen de verschillende mogendheden in de regio.  


# Gegevens opvragen bij MIA
MIA is weliswaar een uitstekend samenwerkingsinstrument voor onderzoekers, maar de gegevens op zijn servers zijn niet gemakkelijk toegankelijk. De back-end is bijvoorbeeld niet in openbare repository's gepubliceerd. Toch kun je de gegevens bemachtigen door je bij MIA te registreren en met Python verzoeken naar de server te sturen.

### Verzoek
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Vervang LOGIN en PASSWORD wel door je eigen inloggegevens.

### Antwoord naar een bestand schrijven
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### JSON openen
```python
f = open('response.json', encoding="utf8")
```
### JSON-object als dictionary teruggeven
```python
json_complete = json.load(f)
```
### Gegevens uit de JSON selecteren en in csv-formaat wegschrijven
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

Zodra je het bestand `results.csv` hebt gedownload, kun je de gegevens opschonen zoals hierboven beschreven. 