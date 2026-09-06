---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Una geografia percettiva del Levante"
subtitle: "A che cosa era associato il Levante nella Firenze del Cinquecento?"
summary: "Il Levante è un toponimo sfuggente, perché di solito viene definito in relazione – o in opposizione – a un altro territorio. Che cos’era dunque il Levante per la Toscana del XVI secolo? I dati che ho raccolto dalla banca dati MIA danno una risposta inattesa."
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
  caption: "Mappa di densità dei toponimi menzionati in ASFi MdP 4277 dal 1543 al 1566"
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
Il *Levante* è un luogo sfuggente. Definito di solito in relazione – o in opposizione – a un altro territorio, il suo significato è stato raramente stabile, evocando geografie diverse a seconda del luogo e del momento in cui il termine veniva usato. Ma se una definizione oggettiva e precisa del termine è difficile da formulare, si può ancora sperare di tracciare una mappa soggettiva di quella regione, prendendo come base le correlazioni esistenti all’interno di un dato corpus di testi. In altre parole: quale spazio poteva evocare il *Levante* per un gruppo specifico di lettori?  
In questo post mostrerò come usare i dati della [banca dati MIA](https://mia.medici.org/) del Medici Archive Project 
per visualizzare i luoghi specifici a cui il toponimo era associato.  

# La banca dati MIA
La banca dati MIA è una piattaforma collaborativa per gli studiosi che desiderano caricare e condividere le proprie fotografie di materiale d’archivio dell’[Archivio di Stato di Firenze](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Nel corso dell’ultimo anno, con il patrocinio del [National Endowment for the Humanities](https://www.neh.gov), il nostro gruppo ha fotografato, trascritto, riassunto e classificato migliaia di documenti conservati nella sezione degli *avvisi* del fondo *Mediceo del Principato* a Firenze. Sebbene la nostra banca dati non fosse pensata in primo luogo per l’analisi statistica, i metadati che abbiamo reso disponibili possono comunque essere scaricati e usati come insiemi di dati. 

# L’insieme di dati
In questo caso, l’insieme di dati che ho creato copre tutte le notizie dal *Levante* dal 1543 al 1566, vale a dire dal primo avviso registrato negli archivi fino all’anno della morte del sultano [Solimano I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Ecco un campione dei dati che ho estratto dal server. Composti da tre colonne, i dati consistono in un numero univoco di documento, un nome di luogo e una data. 

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

## Pulizia dei dati
Per visualizzare questi dati, dobbiamo renderli leggibili come insieme di dati csv (valori separati da virgola). Dobbiamo inoltre convertire le informazioni geografiche qui contenute in un formato più «leggibile dalla macchina»: le coordinate GPS. Poiché l’insieme di dati contiene centinaia di voci, è preferibile automatizzare il processo. Lo si può fare abbastanza in fretta e con buona precisione usando modelli linguistici pre-addestrati come [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) o [AI-21](https://www.ai21.com), per citarne solo alcuni. L’operazione va però supervisionata da vicino, perché i modelli linguistici pre-addestrati hanno una lieve tendenza ad avere allucinazioni.


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
Una mappa di densità è un tipo di visualizzazione che mette in evidenza la frequenza con cui un luogo è menzionato in un dato insieme di dati. È particolarmente utile per capire non solo l’estensione geografica dei propri dati, ma anche i loro punti focali. Quali luoghi sulla mappa sono menzionati più spesso? E quali sono più episodici? Dove sono i centri, e quanto è lontana la periferia? In quale punto della mappa è più probabile che si concentri l’attenzione di un lettore? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Ai fini di questo esperimento – e poiché avevo fretta – ho usato una delle API di [Mapbox](https://www.mapbox.com). Molte librerie di visualizzazione e molti sistemi informativi geografici permettono però di produrre lo stesso tipo di mappa di densità. 

# Alcune osservazioni
Il risultato è più un quadro impressionistico che la rappresentazione precisa di un concetto chiaramente definibile, ed è proprio questo che mi piace di questo esperimento. In effetti, {{< hl >}}se la scienza dei dati può essere un’alleata potente delle discipline umanistiche, non siamo per forza tenuti a rispettarne le regole.{{< /hl >}}

Un altro aspetto interessante di questo esperimento è che la mappa rivela un *Levante* completamente integrato con il resto dell’Europa e del Mediterraneo. Mette inoltre in evidenza la centralità di Edirne nella geografia politica dell’Impero ottomano. Per di più, la città spagnola più rilevante sulla mappa non è né Madrid né l’Escorial, ma Napoli. Infine, le isole e le piccole città-stato come Ragusa sembrano svolgere un ruolo importante di mediazione tra le diverse potenze della regione.  


# Come richiedere i dati a MIA
Sebbene MIA sia uno strumento collaborativo eccellente per i ricercatori, i dati che conserva sui suoi server non sono facilmente accessibili. Il suo back-end, per esempio, non è pubblicato in repository pubblici. È comunque possibile ottenere i dati registrandosi a MIA e inviando richieste al server con Python.

### Richiesta
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Ricordatevi di sostituire LOGIN e PASSWORD con le vostre credenziali.

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
### Restituzione dell’oggetto JSON come dizionario
```python
json_complete = json.load(f)
```
### Selezione dei dati dal JSON e stampa in formato CSV
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

Una volta scaricato il file `results.csv`, potete procedere alla pulizia dei dati come spiegato sopra. 
