---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Percepcyjna geografia Lewantu"
subtitle: "Z czym kojarzono Lewant w szesnastowiecznej Florencji?"
summary: "Lewant to toponim nieuchwytny: zwykle definiuje się go w relacji do innego terytorium – albo w opozycji do niego. Czym więc był Lewant Toskanii w XVI wieku? Dane, które zebrałem z bazy MIA, dają nieoczekiwaną odpowiedź."
authors: [clement]
tags: [MAP, Avviso]
categories: [Notatki]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
draft: false
machine_translated: true


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Mapa gęstości toponimów wzmiankowanych w ASFi MdP 4277 w latach 1543–1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Wprowadzenie
*Levante* – Lewant – to miejsce nieuchwytne. Definiowany zwykle w relacji do innego terytorium – albo w opozycji do niego – rzadko miał stałe znaczenie i przywoływał różne geografie zależnie od tego, gdzie i kiedy używano tego słowa. Jeśli jednak trudno o obiektywną i ścisłą definicję terminu, można przynajmniej spróbować nakreślić subiektywną mapę tego regionu, opierając się na korelacjach istniejących w danym korpusie tekstów. Innymi słowy: jaką przestrzeń mógł *Levante* przywoływać w wyobraźni określonej grupy czytelników?  
W tym wpisie pokażę, jak wykorzystać dane z [bazy MIA](https://mia.medici.org/) prowadzonej przez Medici Archive Project, 
by zwizualizować konkretne miejsca, z którymi kojarzono ten toponim.  

# Baza MIA
Baza MIA to platforma współpracy dla badaczy, którzy chcą zamieszczać i udostępniać własne fotografie materiałów archiwalnych z [Archiwum Państwowego we Florencji](https://archiviodistatofirenze.cultura.gov.it/asfi/home). W ciągu minionego roku, pod patronatem [National Endowment for the Humanities](https://www.neh.gov), nasz zespół sfotografował, przepisał, streścił i sklasyfikował tysiące dokumentów przechowywanych w dziale *avvisi* zespołu *Mediceo del Principato* we Florencji. Choć nasza baza nie była pomyślana przede wszystkim z myślą o analizie statystycznej, udostępnione przez nas metadane można pobrać i wykorzystać jako zbiory danych. 

# Zbiór danych
W tym przypadku stworzony przeze mnie zbiór obejmuje wszystkie wiadomości z *Levante* z lat 1543–1566, to znaczy od pierwszego avviso odnotowanego w archiwum do roku śmierci sułtana [Sulejmana I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Oto próbka danych, które pobrałem z serwera. Składają się z trzech kolumn: unikatowego numeru dokumentu, nazwy miejsca i daty. 

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

## Czyszczenie danych
Aby zwizualizować te dane, musimy je przekształcić w czytelny zbiór csv (wartości rozdzielone przecinkami). Musimy też przełożyć zawarte tu informacje geograficzne na format „przyjaźniejszy maszynie”: współrzędne GPS. Ponieważ zbiór liczy setki wpisów, wolimy ten proces zautomatyzować. Da się to zrobić dość szybko i całkiem dokładnie przy użyciu wstępnie wytrenowanych modeli językowych, takich jak [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) czy [AI-21](https://www.ai21.com), by wymienić tylko kilka. Operację tę trzeba jednak ściśle nadzorować, bo wstępnie wytrenowane modele językowe mają lekką skłonność do halucynowania.


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

# Mapa gęstości
Mapa gęstości to typ wizualizacji, który uwydatnia, jak często dane miejsce pojawia się w zbiorze. Przydaje się szczególnie do zrozumienia nie tylko zasięgu geograficznego danych, ale i ich punktów ogniskowych. Które miejsca na mapie wzmiankowane są częściej? A które tylko epizodycznie? Gdzie leżą ośrodki i jak daleko sięgają peryferie? Na czym na mapie najprawdopodobniej skupi się uwaga czytelnika? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Na potrzeby tego eksperymentu – a że się spieszyłem – użyłem jednego z API [Mapboxa](https://www.mapbox.com). Wiele bibliotek do wizualizacji i systemów informacji geograficznej pozwala jednak uzyskać ten sam rodzaj mapy gęstości. 

# Kilka spostrzeżeń
Wynik jest raczej impresjonistycznym obrazem niż ścisłym odwzorowaniem wyraźnie definiowalnego pojęcia – i właśnie to lubię w tym eksperymencie. Bo też {{< hl >}}choć nauka o danych może być potężnym sprzymierzeńcem humanistyki, nie musimy koniecznie grać według jej reguł.{{< /hl >}}

Inny ciekawy aspekt tego eksperymentu: mapa ukazuje *Levante* całkowicie zintegrowany z resztą Europy i Morza Śródziemnego. Uwydatnia też centralne miejsce Edirne w geografii politycznej Imperium Osmańskiego. Co więcej, najważniejszym hiszpańskim miastem na mapie nie jest ani Madryt, ani Escorial, lecz Neapol. Wreszcie wyspy i małe miasta-państwa, takie jak Ragusa, zdają się odgrywać ważną rolę pośredników między różnymi potęgami regionu.  


# Jak pobrać dane z MIA
Choć MIA jest znakomitym narzędziem współpracy dla badaczy, dane przechowywane na jej serwerach nie są łatwo dostępne. Jej back-end, na przykład, nie został opublikowany w żadnym publicznym repozytorium. Dane można jednak uzyskać, rejestrując się w MIA i wysyłając zapytania do serwera z poziomu Pythona.

### Zapytanie
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Pamiętaj, by zastąpić LOGIN i PASSWORD własnymi danymi logowania.

### Zapis odpowiedzi do pliku
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Otwarcie pliku JSON
```python
f = open('response.json', encoding="utf8")
```
### Zwrócenie obiektu JSON jako słownika
```python
json_complete = json.load(f)
```
### Wybór danych z JSON-a i zapis w formacie CSV
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

Po pobraniu pliku `results.csv` można przystąpić do czyszczenia danych, jak opisano wyżej. 