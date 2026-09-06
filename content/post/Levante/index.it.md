---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Una geografia percettiva del Levante"
subtitle: "Che cosa evocava il Levante nella Firenze del Cinquecento?"
summary: "Il Levante è un toponimo sfuggente: lo si definisce quasi sempre in rapporto – o in contrapposizione – a un altro territorio. Che cos’era, allora, il Levante per la Toscana del XVI secolo? I dati raccolti nella banca dati MIA danno una risposta inattesa."
authors: [clement]
tags: [MAP, Avviso]
categories: [Note]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Mappa di densità dei toponimi citati in ASFi MdP 4277 dal 1543 al 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Introduzione
Il *Levante* è un luogo che sfugge. Lo si definisce quasi sempre in rapporto – o in contrapposizione – a un altro territorio, e il suo significato è stato di rado stabile: evoca geografie diverse a seconda del luogo e del momento in cui la parola viene usata. Se però una definizione oggettiva e precisa è difficile da formulare, si può almeno tentare una mappa soggettiva di quella regione, fondata sulle correlazioni interne a un dato corpus di testi. In altre parole: quale spazio evocava il *Levante* per un determinato gruppo di lettori?  
In questo post mostro come usare i dati della [banca dati MIA](https://mia.medici.org/) del Medici Archive Project 
per visualizzare i luoghi a cui il toponimo era associato.  

# La banca dati MIA
MIA è una piattaforma collaborativa per gli studiosi che vogliono caricare e condividere le proprie fotografie di documenti dell’[Archivio di Stato di Firenze](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Nell’ultimo anno, col patrocinio del [National Endowment for the Humanities](https://www.neh.gov), il nostro gruppo ha fotografato, trascritto, riassunto e classificato migliaia di documenti della sezione degli *avvisi* del fondo *Mediceo del Principato*. La banca dati non nasce per l’analisi statistica; ma i metadati che abbiamo reso disponibili si possono scaricare e usare come veri e propri insiemi di dati. 

# L’insieme di dati
Nel nostro caso, l’insieme di dati che ho costruito raccoglie tutte le notizie «dal Levante» fra il 1543 e il 1566, cioè dal primo avviso registrato nell’archivio fino all’anno della morte del sultano [Solimano I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Ecco un campione di quanto ho estratto dal server: tre colonne, con il numero univoco del documento, un nome di luogo e una data. 

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

## Ripulire i dati
Per visualizzarli, i dati vanno resi leggibili come csv (valori separati da virgola), e l’informazione geografica va convertita in un formato più digeribile per la macchina: le coordinate GPS. Trattandosi di centinaia di voci, conviene automatizzare. Lo si fa abbastanza in fretta, e con buona precisione, con modelli linguistici pre-addestrati come [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) o [AI-21](https://www.ai21.com), per citarne solo alcuni; ma l’operazione va sorvegliata da vicino, perché questi modelli hanno una certa propensione ad allucinare.


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

# La mappa di densità
Una mappa di densità è una visualizzazione che mette in risalto la frequenza con cui un luogo viene citato in un insieme di dati. Serve a capire non soltanto l’estensione geografica dei propri dati, ma anche i loro punti focali. Quali luoghi ricorrono di più, e quali sono solo episodici? Dove sono i centri, e quanto è lontana la periferia? Su quale punto della mappa si concentrerebbe, con ogni probabilità, l’attenzione di un lettore? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Per questo esperimento – e perché avevo fretta – ho usato una delle API di [Mapbox](https://www.mapbox.com). Ma molte librerie di visualizzazione e molti sistemi informativi geografici producono lo stesso tipo di mappa. 

# Qualche osservazione
Il risultato è più un quadro impressionista che la rappresentazione esatta di un concetto ben definibile; ed è proprio questo che mi piace dell’esperimento. Perché {{< hl >}}la scienza dei dati può essere una potente alleata delle discipline umanistiche, ma non siamo obbligati a giocare secondo le sue regole.{{< /hl >}}

Un altro aspetto interessante: la mappa restituisce un *Levante* perfettamente integrato con il resto dell’Europa e del Mediterraneo. Mette in luce la centralità di Edirne nella geografia politica dell’Impero ottomano; e rivela che la città più rilevante della Spagna, sulla mappa, non è Madrid né l’Escorial, ma Napoli. Da ultimo, le isole e le piccole città-stato come Ragusa sembrano avere un ruolo importante di mediazione fra le potenze della regione.  


# Come richiedere i dati a MIA
MIA è uno strumento collaborativo eccellente, ma i dati che custodisce sui suoi server non sono facili da raggiungere: il back-end, per dire, non è pubblicato su alcun repository pubblico. Si possono comunque ottenere registrandosi a MIA e interrogando il server con Python.

### Richiesta
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Ricordate di sostituire LOGIN e PASSWORD con le vostre credenziali.

### Scrittura della risposta su file
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Apertura del JSON
```python
f = open('response.json', encoding="utf8")
```
### Conversione dell’oggetto JSON in dizionario
```python
json_complete = json.load(f)
```
### Selezione dei dati dal JSON e scrittura in formato CSV
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

Scaricato il file `results.csv`, potete passare alla pulizia dei dati come spiegato sopra. 
