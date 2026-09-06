---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Una geografía perceptiva del Levante"
subtitle: "¿Qué evocaba el Levante en la Florencia del siglo XVI?"
summary: "El Levante es un topónimo escurridizo: suele definirse en relación con otro territorio, o por oposición a él. ¿Cuál era, pues, el Levante de la Toscana del siglo XVI? Los datos que he reunido en la base de datos MIA dan una respuesta inesperada."
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
  caption: "Mapa de densidad de los topónimos mencionados en ASFi MdP 4277 entre 1543 y 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Introducción
El *Levante* es un lugar escurridizo. Definido casi siempre en relación con otro territorio —o por oposición a él—, su sentido rara vez ha sido estable: evoca geografías distintas según el lugar y la época en que se usa la palabra. Ahora bien, si una definición objetiva y precisa del término se nos resiste, cabe al menos trazar un mapa subjetivo de esa región a partir de las correlaciones que existen dentro de un corpus de textos determinado. Dicho de otro modo: ¿qué espacio evocaba el *Levante* para un grupo concreto de lectores?  
En esta entrada mostraré cómo usar los datos de la [base de datos MIA](https://mia.medici.org/) del Medici Archive Project 
para visualizar los lugares concretos con que se asociaba el topónimo.  

# La base de datos MIA
MIA es una plataforma colaborativa en la que los investigadores suben y comparten sus propias fotografías de documentos del [Archivio di Stato di Firenze](https://archiviodistatofirenze.cultura.gov.it/asfi/home). A lo largo del último año, con el patrocinio del [National Endowment for the Humanities](https://www.neh.gov), nuestro equipo ha fotografiado, transcrito, resumido y clasificado miles de documentos de la sección de *avvisi* del fondo *Mediceo del Principato*, en Florencia. La base de datos no se concibió para el análisis estadístico, pero los metadatos que hemos puesto a disposición del público pueden descargarse y usarse como conjuntos de datos. 

# El conjunto de datos
El conjunto que preparé para esta ocasión abarca todas las noticias llegadas de *Levante* entre 1543 y 1566, esto es, desde el primer avviso que registra el archivo hasta el año de la muerte del sultán [Solimán I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). He aquí una muestra de lo que extraje del servidor: tres columnas con un número único de documento, un nombre de lugar y una fecha. 

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

## Limpieza de los datos
Para visualizar estos datos hay que convertirlos en un csv (valores separados por comas) legible, y traducir la información geográfica a un formato más «digerible» para la máquina: coordenadas GPS. Como el conjunto tiene cientos de entradas, más vale automatizar la operación, lo que puede hacerse con bastante rapidez y precisión mediante modelos de lenguaje preentrenados como [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) o [AI-21](https://www.ai21.com), por citar solo algunos. Eso sí: conviene vigilar de cerca, porque estos modelos tienen cierta propensión a alucinar.


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

# El mapa de densidad
Un mapa de densidad es una visualización que resalta la frecuencia con que un lugar aparece en un conjunto de datos. Sirve para apreciar no solo el alcance geográfico de los datos, sino también sus puntos focales. ¿Qué lugares del mapa se mencionan más a menudo, y cuáles solo de tanto en tanto? ¿Dónde están los centros, y a qué distancia queda la periferia? ¿En qué zona del mapa tenderá a fijarse la atención de un lector? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Para este experimento —y porque tenía prisa— recurrí a una de las API de [Map Box](https://www.mapbox.com). Muchas bibliotecas de visualización y sistemas de información geográfica permiten, con todo, producir el mismo tipo de mapa. 

# Algunas observaciones
El resultado tiene más de cuadro impresionista que de representación exacta de un concepto bien delimitado, y eso es justamente lo que me gusta de este experimento. Porque, {{< hl >}}si bien la ciencia de datos puede ser una gran aliada de las humanidades, no estamos obligados a jugar con sus reglas.{{< /hl >}}

Otro aspecto interesante: el mapa revela un *Levante* plenamente integrado en el resto de Europa y del Mediterráneo. Subraya también la centralidad de Edirne en la geografía política del Imperio otomano. Por lo demás, la ciudad más relevante de la Monarquía española en el mapa no es Madrid ni El Escorial, sino Nápoles. Y no es lo de menos que las islas y las pequeñas ciudades-estado como Ragusa parezcan desempeñar un papel importante de mediación entre las distintas potencias de la región.  


# Cómo pedir datos a MIA
MIA es una herramienta colaborativa excelente para los investigadores, pero los datos que guarda en sus servidores no son de fácil acceso: su *back-end*, por ejemplo, no está publicado en ningún repositorio público. Aun así, puede obtenerlos registrándose en MIA y lanzando peticiones al servidor con Python.

### Petición
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
No olvide sustituir LOGIN y PASSWORD por sus propias credenciales.

### Guardar la respuesta en un archivo
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Abrir el JSON
```python
f = open('response.json', encoding="utf8")
```
### Devolver el objeto JSON como diccionario
```python
json_complete = json.load(f)
```
### Seleccionar los datos del JSON e imprimirlos en formato CSV
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

Una vez descargado `results.csv`, puede pasar a limpiar los datos como se explicó más arriba. 
