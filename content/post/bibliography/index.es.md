---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Convertir bibliografías a gran escala con modelos de lenguaje preentrenados"
subtitle: "Cómo transformar en poco tiempo miles de referencias bibliográficas en una base de datos BibTeX"
summary: "GPT-3 permite volcar en una base de datos, en muy poco tiempo, grandes cantidades de bibliografía"
authors: [clement]
tags: [Humanidades digitales, GPT-3, Bibliografía, Automatización]
categories: [Edición eficiente]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

La automatización es la clave para abaratar los proyectos de humanidades digitales. Hasta hoy, las tareas repetitivas y tediosas del trabajo editorial en el mundo académico las han hecho, a un precio muy alto, investigadores desbordados, o bien se han «subcontratado» a los estudiantes. En esta [serie de entradas](https://www.clementgodbarge.com/category/efficient-editing/) sostengo que la mayoría de esas tareas ingratas no solo *pueden* automatizarse: *deben* automatizarse. Automatizar el trabajo editorial reduce el coste global de los proyectos de humanidades digitales y, lo que es decisivo, permite a los investigadores de regiones con pocos recursos publicar documentos valiosos con rapidez y a un precio asequible.

En [la entrada anterior](https://www.clementgodbarge.com/post/gpt3/) mostré, por ejemplo, cómo los modelos de lenguaje preentrenados pueden hacerse cargo de la mayor parte del etiquetado XML de una edición digital. 

En esta presento un segundo ejemplo, esta vez con la bibliografía.


## El problema
Crear una base de datos bibliográfica con las referencias que cita un artículo académico no tiene mayor misterio: basta una búsqueda rápida en un catálogo como [WorldCat](https://www.worldcat.org), descargar la referencia en el formato deseado o importarla automáticamente desde una base de datos local. Con uno o dos artículos, el método funciona.
Pasado cierto número de referencias, sin embargo, la tarea se vuelve ingrata y devora el tiempo. Para remediarlo existen analizadores como [anystyle.io](https://anystyle.io), pero escalarlos no es fácil.
Cuando usé anystyle para convertir los más de 150 ensayos académicos de nuestra [edición crítica del Ms. Fr. 640](https://edition640.makingandknowing.org/#/), los errores se acumularon hasta volverse sencillamente inmanejables: no reconocía bien muchas de nuestras fuentes —confundía, por ejemplo, los largos títulos de los libros de la Edad Moderna con otra cosa— y se le escapaban los documentos menos convencionales, como páginas web concretas, vídeos en línea, etc. Los analizadores funcionan siempre que el autor siga a rajatabla una convención conocida —Chicago, Turabian, MLA—; en cuanto se aparta de la norma, llegan los errores.

## La solución
Aquí es donde los {{< hl >}}modelos de lenguaje preentrenados{{< /hl >}} pueden echar una mano: {{< hl >}}captan en un instante los patrones de cualquier estilo bibliográfico{{< /hl >}}, incluso uno inventado por usted, y con unos pocos ejemplos convierten correctamente grandes cantidades de bibliografía ya formateada en una [base de datos BibTeX](http://www.bibtex.org/Format/). 

A comienzos de 2021 tuve la suerte de acceder de forma anticipada a [GPT-3 Codex](https://openai.com/blog/openai-codex/), de OpenAI. Codex es un modelo que traduce el lenguaje natural a código y viceversa. OpenAI asegura que domina más de una docena de lenguajes de programación y, aunque su API sigue en fase beta mientras escribo estas líneas, ya mueve aplicaciones tan populares como [Copilot](https://github.com/features/copilot/), de GitHub.

Tras trastear un poco con la API, comprendí que también podía rendir muy bien con un código más simple, como `BibTeX`. 

De hecho, me bastaron cuatro ejemplos en el prompt de entrada para que funcionara de forma fiable. 

### Prompt de entrada

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### Resultados
Los {{< hl >}}[resultados](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) son llamativos: más de 2000 referencias bibliográficas convertidas en cuestión de días.{{< /hl >}} El método no solo reprodujo con exactitud el patrón de mi prompt, sino que añadió por su cuenta, y correctamente, tipos de entrada y de campo que no figuraban en él. `GPT-3`, dicho de otro modo, habla `BibTeX` con toda fluidez. Y, lo que acaso sorprenda más en un modelo entrenado sobre todo en inglés, reconoció todas las lenguas (ruso, francés, italiano, latín, griego, alemán, español, etc.) y añadió en cada caso el campo `langid` correcto.

> [!NOTE]
> Por ahora, GPT-3 tiene un tamaño de entrada y de salida limitado: procesa como máximo 2048 tokens lingüísticos. En cuanto se levante esa limitación, la misma tarea llevará probablemente una hora o menos.

Algo inesperadamente, GPT-3 añadió además información que no estaba en las referencias originales. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

En esta referencia, por ejemplo, GPT-3 añadió el enlace permanente al repositorio de acceso abierto ([HAL](https://hal.archives-ouvertes.fr)) donde puede leerse el artículo, con los campos ad hoc `HAL_ID` y `HAL_VERSION` que crea el propio repositorio: 
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

Estos añadidos indican que {{< hl >}}GPT-3 no se limita a analizar la referencia bibliográfica: la completa con lo que aprendió en su día.{{< /hl >}} Sería interesante, en este sentido, comprobar si hace lo mismo con referencias posteriores a su entrenamiento...

## Limitaciones
GPT-3 no es perfecto, sin embargo, y necesita la supervisión de un ser humano. Una de sus limitaciones conocidas es la [alucinación](https://arxiv.org/abs/2005.00661): a veces inventa cosas y hace suposiciones improbables. 

En mi experimento, los arrebatos de incoherencia de GPT-3 se hicieron patentes cuando cambió por su cuenta el apellido de un autor, de «Ruscelli» a «Ruscello». En rigor no es un error, pues los apellidos italianos de la Edad Moderna se usaban indistintamente en singular o en plural. Pero la convención actual manda conservar el apellido tal como está, en singular o en plural: hoy nadie llama Machiavello a Machiavelli, del mismo modo que se espera que escribamos Rossello y no Rosselli. ¿Ignoró GPT-3 la convención por falta de conciencia cronológica? ¿O hizo una suposición a partir de los apellidos vecinos, que en esta parte de la bibliografía están todos, casualmente, en singular (Bariletto, Cesano, Rossello)?
Quién sabe.

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## Conclusión
Escritos a lo largo de cuatro años de intensa colaboración, los más de 150 ensayos [que incluye nuestra edición digital](https://edition640.makingandknowing.org/#/essays) no solo aportan información esencial sobre el manuscrito que editamos y tradujimos: contienen también una valiosa información bibliográfica.

Reunir esas referencias en una base de datos permite a los editores cambiar el formato bibliográfico en un abrir y cerrar de ojos y presentar la información como mejor les parezca. La base de datos dice además mucho sobre la edición y sobre el proyecto que la hizo posible, y abre nuevas perspectivas de análisis a los investigadores. Y puede completarse con gran precisión y en un plazo récord.

Es verdad que algún error puede colarse, sobre todo por la propensión de GPT-3 a alucinar. Pero las próximas generaciones de modelos de lenguaje preentrenados atenuarán el problema.
