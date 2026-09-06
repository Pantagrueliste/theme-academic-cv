---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Análisis bibliográfico a gran escala con modelos de lenguaje preentrenados"
subtitle: "Cómo convertir rápidamente miles de referencias bibliográficas en una base de datos BibTeX"
summary: "GPT-3 ayuda a convertir grandes cantidades de bibliografía en una base de datos en poco tiempo"
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

La automatización es clave para reducir el coste de los proyectos de humanidades digitales. Hasta hoy, las tareas repetitivas y tediosas propias del trabajo editorial en el ámbito académico se han llevado a cabo a un gran coste por investigadores desbordados, o bien se han «subcontratado» a estudiantes. En esta [serie de entradas](https://www.clementgodbarge.com/category/efficient-editing/), sostengo que la mayoría de estas tareas ingratas no solo *pueden*, sino que *deben* automatizarse. La automatización de las tareas editoriales reduce el coste global de los proyectos de humanidades digitales. Y, lo que es crucial, permite a los investigadores de regiones de bajos ingresos publicar documentos valiosos con rapidez y a un precio asequible.

En [la entrada anterior](https://www.clementgodbarge.com/post/gpt3/), mostré por ejemplo cómo los modelos de lenguaje preentrenados pueden encargarse de la mayor parte del trabajo de etiquetado XML de una edición digital. 

En esta entrada expongo un segundo ejemplo, esta vez con la bibliografía.


## El problema
Crear una base de datos bibliográfica a partir de las referencias mencionadas en un artículo académico es bastante sencillo. Se puede hacer una búsqueda rápida en un catálogo como [WorldCat](https://www.worldcat.org), descargar la referencia en un formato determinado o importarla automáticamente desde una base de datos local. Esto funciona bien con uno o dos artículos.
Sin embargo, a partir de cierto número de referencias, la tarea se vuelve ingrata y consume mucho tiempo. Para remediarlo, se pueden utilizar algoritmos de análisis sintáctico como [anystyle.io](https://anystyle.io). Pero estos algoritmos pueden ser difíciles de escalar.
Cuando utilicé anystyle para convertir los más de 150 ensayos académicos incluidos en nuestra [edición crítica del Ms. Fr. 640](https://edition640.makingandknowing.org/#/), la cantidad de errores acumulados era sencillamente inmanejable. No reconocía correctamente muchas de nuestras fuentes, confundiendo por ejemplo los largos títulos de los libros de la Edad Moderna con otra cosa, y no reconocía documentos menos típicos, como páginas web concretas, vídeos en línea, etc. Los analizadores funcionan bien siempre que el autor siga a rajatabla las reglas de una convención conocida, como Chicago, Turabian o MLA. Cualquier desviación de la norma provoca errores.

## La solución
Aquí es donde los {{< hl >}}modelos de lenguaje preentrenados{{< /hl >}} pueden ayudar, ya que {{< hl >}}entienden rápidamente los patrones de cualquier estilo bibliográfico{{< /hl >}}, incluso uno inventado por usted, y solo necesitan unos pocos ejemplos para convertir correctamente grandes cantidades de bibliografía formateada en una [base de datos BibTeX](http://www.bibtex.org/Format/). 

A principios de 2021 tuve la suerte de disfrutar de acceso anticipado a [GPT-3 Codex](https://openai.com/blog/openai-codex/) de OpenAI. Codex es un modelo que permite a los usuarios traducir el lenguaje natural a código y viceversa. OpenAI afirma que domina más de una docena de lenguajes de programación y, aunque su API sigue siendo accesible, en el momento de escribir esta entrada, como versión beta, ya impulsa aplicaciones populares como [Copilot](https://github.com/features/copilot/) de GitHub.

Tras trastear un poco con esta API, me di cuenta de que también podía funcionar muy bien con un código más simple como `BibTeX`. 

Y, de hecho, solo tuve que utilizar cuatro ejemplos en el prompt de entrada para que funcionara de forma fiable. 

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
Los {{< hl >}}[resultados](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) son asombrosos: más de 2000 referencias bibliográficas convertidas en cuestión de días.{{< /hl >}} Este enfoque no solo reprodujo con precisión el patrón expuesto en mi prompt de entrada, sino que además añadió correctamente tipos de entrada y de campo que no figuraban en él. `GPT-3`, en otras palabras, domina perfectamente `BibTeX`. Y, lo que quizá resulte más sorprendente para un modelo entrenado esencialmente en inglés, reconoció todas las lenguas (ruso, francés, italiano, latín, griego, alemán, español, etc.), añadiendo cada vez el campo `langid` correcto.

> [!NOTE]
> GPT-3 tiene actualmente tamaños de entrada y salida limitados, ya que puede procesar un máximo de 2048 tokens lingüísticos. En cuanto se levante esta limitación, la misma tarea llevaría probablemente una hora o menos.

De forma un tanto inesperada, GPT-3 también añadió información que no figuraba en las referencias originales. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

En esta referencia bibliográfica, por ejemplo, GPT-3 añadió el enlace permanente al repositorio de acceso abierto ([HAL](https://hal.archives-ouvertes.fr)) donde puede leerse el artículo, incluidos los campos ad hoc `HAL_ID` y `HAL_VERSION` creados por el repositorio HAL: 
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

Estas adiciones indican que {{< hl >}}GPT-3 no solo analiza la referencia bibliográfica, sino que también la completa a partir de lo que aprendió inicialmente.{{< /hl >}} Sería interesante, en este sentido, comprobar si se comporta de forma similar con referencias posteriores al entrenamiento de GPT-3...

## Limitaciones
GPT-3 no es perfecto, sin embargo. Necesita la supervisión de un ser humano. Una de sus limitaciones conocidas es la [alucinación](https://arxiv.org/abs/2005.00661), pues a veces inventa cosas y hace suposiciones improbables. 

En mi experimento, los episodios de incoherencia de GPT-3 se manifestaron cuando cambió espontáneamente el apellido de un autor de «Ruscelli» a «Ruscello». Técnicamente no es un error, ya que los apellidos italianos de la Edad Moderna podían usarse indistintamente en plural o en singular. Sin embargo, la convención actual es que, si un apellido está en plural o en singular, debe mantenerse tal cual. Hoy nadie llamaría Machiavello a Machiavelli, del mismo modo que se espera que usemos el nombre Rossello en lugar de Rosselli. ¿Ha ignorado GPT-3 esta convención por falta de conciencia cronológica? ¿O es que GPT-3 hizo una suposición a partir de los apellidos vecinos, que en esta parte de la bibliografía resultan estar todos en singular (Bariletto, Cesano, Rossello)?
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
Escritos a lo largo de cuatro años de intensas colaboraciones, los más de 150 ensayos [incluidos en nuestra edición digital](https://edition640.makingandknowing.org/#/essays) no solo aportan información esencial sobre el manuscrito que editamos y tradujimos, sino que también contienen valiosa información bibliográfica.

Reunir estas referencias bibliográficas en una base de datos permite a los editores cambiar el formato bibliográfico en un abrir y cerrar de ojos, lo que les da más flexibilidad para mostrar esta información como deseen. Esta base de datos también ofrece información valiosa sobre la edición y el proyecto que la hizo posible, abriendo nuevas perspectivas analíticas para los investigadores. Una base de datos así puede completarse con gran precisión y en un plazo récord.

Es cierto que pueden colarse algunos errores, sobre todo por la tendencia de GPT-3 a alucinar. Pero las futuras iteraciones de los modelos de lenguaje preentrenados mitigarán este problema.
