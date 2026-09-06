---
title: "Automatizar el marcado en las ediciones críticas digitales"
subtitle: "¿Pueden los modelos de lenguaje preentrenados aumentar sustancialmente la productividad editorial?"

# Summary for listings and search engines
summary: Los modelos de lenguaje preentrenados pueden descargar a los investigadores de algunas de las tareas más tediosas y laboriosas de la edición. A partir de las anotaciones, revisadas con esmero, de *Secrets of Craft and Nature in Renaissance France*, evalúo hasta qué punto un modelo como GPT-3 puede entrenarse en poco tiempo para anotar manuscritos técnicos del siglo XVI.

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- Humanidades digitales
- Aprendizaje automático
- Ediciones críticas digitales
- Investigación en curso

categories:
- Edición eficiente
---
# Introducción
¿Cómo producir ediciones críticas digitales sin dejarse en ellas el presupuesto? En esta entrada, primera de una serie dedicada a la edición eficiente, examino el papel que pueden desempeñar los modelos de lenguaje preentrenados en la automatización de tareas editoriales como el marcado semántico.

{{< toc >}}

# El problema
## Una labor de amor
En el amor no se mira el gasto... o eso dice el refrán. Y a las ediciones críticas digitales se les aplica con especial justicia: la transcripción, la traducción y la anotación que exigen suman miles de horas de trabajo, a cargo —como en el caso de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)— de cientos de colaboradores altamente cualificados.

En cierto modo, es una suerte que los proyectos más visibles de las humanidades digitales consigan las enormes sumas que necesitan para funcionar. Ahora bien, depender de la munificencia de fundaciones acaudaladas, universidades y organismos públicos, y necesitar durante años un despliegue considerable de recursos humanos, no es un modelo económico con futuro.

En rigor, si queremos animar a investigadores de todo el mundo a poner los documentos históricos al alcance de un público más amplio, {{< hl >}}el coste de las ediciones críticas digitales tendría que bajar varios órdenes de magnitud{{< /hl >}}. 

## Un listón muy alto
Paradójicamente, {{< hl >}}la solución puede venir de proyectos tan intensivos en trabajo como [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), pues constituyen un valioso conjunto de entrenamiento{{< /hl >}} con el que automatizar algunas de las tareas más ingratas y repetitivas de la edición digital, empezando por el marcado.

No es que el marcado sea cosa menor. Al contrario: {{< hl >}}se ha convertido en el componente indispensable de cualquier proyecto digital serio.{{< /hl >}} Normalizado por la [Text Encoding Initiative](https://tei-c.org), permite registrar cuantos aspectos se quiera del documento y del texto que transmite: estructura, notas marginales, tachaduras, variantes, tipo de papel, manchas, caligrafía... Lo que se le ocurra.

El siguiente ejemplo, tomado de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), muestra cómo el marcado enriquece el texto con información añadida (categoría, estructura, campos semánticos, tachaduras, etc.), y da así a las ediciones digitales una ventaja considerable sobre sus antepasadas de papel.

<table>
<tr>
<th> Texto plano </th>
<th> Marcado XML</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

Esta información no solo vale con fines archivísticos; como he mostrado en otras ocasiones, sirve también para la síntesis y el análisis. Con todo, anotar así un texto puede llevar muchísimo tiempo, sobre todo porque el mismo texto suele tener que existir en varias versiones: traducción, transcripción, modernización, etc. 

# La solución
## Los transformadores: ¿el camino más corto hacia la automatización?
En 2020, [OpenAI](https://www.openai.com) presentó a bombo y platillo su última familia de modelos de lenguaje de gran escala y propósito general, GPT-3, siglas de «Generative Pre-trained Transformer 3». Los transformadores son un avance reciente de la inteligencia artificial: aprenden tareas nuevas con una rapidez asombrosa, con solo leer una instrucción (*prompt*) y ver un puñado de ejemplos. Admiten además un entrenamiento adicional con datos ad hoc (el *fine-tuning* o ajuste fino), que mejora la latencia y la precisión. De ahí que se diga que GPT-3 y sus semejantes son [aprendices con pocos ejemplos](https://arxiv.org/abs/2005.14165) (*few-shot learners*). 

Según OpenAI, GPT-3 contiene la cifra récord de 175 000 millones de parámetros y se ha entrenado con más de 570 GB de texto, en su mayoría documentos en inglés extraídos, cabe suponer, de [internet](https://skylion007.github.io/OpenWebTextCorpus/). Por su mero tamaño, GPT-3 ha fijado un nuevo estándar en el campo, y ejecuta de entrada las tareas más variadas con un realismo inquietante: escribe [artículos de opinión](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) verosímiles, [conversa con humanos](https://www.quickchat.ai/emerson) en salas de chat, [contesta correos electrónicos](https://www.jarvis.ai/?fpr=serpbattle), [resume textos](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduce documentos, explica la jerga de las profesiones, etc.

Con acceso anticipado a la API de OpenAI desde mayo de 2021, he podido poner a prueba la capacidad del modelo para resolver tareas de reconocida dificultad: traducir al inglés poesía francesa y textos neolatinos, explicar analogías e incluso simplificar el libro 4 de la *Fundamentación de la metafísica de las costumbres* de Kant para un niño de siete años (sin demasiado éxito, hay que decirlo).

### Codex
Uno de los últimos desarrollos de GPT-3 se ocupa de los lenguajes de programación. Se llama *Codex* y traduce el lenguaje natural a código, y viceversa. Si busco, por ejemplo, una expresión regular que me permita «encontrar solo las palabras que empiezan por mayúscula», GPT-3 la convierte al instante en una expresión regular que funciona: ```[A-Z]+\w+```.

OpenAI asegura que *Codex* maneja una docena de lenguajes, entre ellos Python, JavaScript, Go, Perl, PHP, Ruby y Swift. Al pasar del pseudocódigo al código sin fisuras, *Codex* permite concentrarse no en la sintaxis puntillosa de un lenguaje, sino en los pasos lógicos y las estrategias con que una aplicación resuelve un problema.

### Más allá de OpenAI
OpenAI no es, desde luego, el único actor en escena. Como ya se ha dicho, la Academia de Inteligencia Artificial de Pekín anunció en 2021 un modelo aún mayor y más capaz, *Wu Dao 2*. Nvidia y Microsoft unieron fuerzas para producir el modelo *Megatron-Turing NLG 530B*, de nombre bien elegido. Empresas emergentes de menor tamaño, como [AI21 Labs](https://www.ai21.com) y [Cohere](https://cohere.ai), ofrecen también sus API al público, y merecen mención iniciativas de código abierto como [EuletherAI](https://www.eleuther.ai). El panorama, claro está, cambia a gran velocidad; para seguir las novedades del campo, consulte [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Los experimentos

> [!NOTE]
> El objetivo de estos experimentos es dar con el camino más económico hacia una automatización fiable de las tareas editoriales. Se dirá que algunas podrían automatizarse también con algoritmos de aprendizaje supervisado; exploraremos esa hipótesis en una próxima entrada.

¿Puede un transformador como GPT-3 aprender a anotar, pongamos por caso, un manuscrito técnico y científico del siglo XVI?

## Experimento 1: categorizar textos
Empecemos por algo relativamente sencillo. Como «aprendiz con pocos ejemplos», GPT-3 debería captar en poco tiempo el modo en que nuestro equipo editorial ha clasificado las entradas del Ms. Fr. 640.

### Diseño del prompt
Para entrenarlo usé un prompt mínimo y elegí como ejemplos cuatro entradas breves en texto plano, entre ellas una de «medicina», otra de «armas y armaduras» y otra de «pintura». 

### Prueba
Después copié un pasaje que no formaba parte de la secuencia inicial: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
El resultado se ajusta perfectamente al contenido: 

```xml
<categories="painting">
```

Si probamos con una entrada de una categoría que ni siquiera figuraba entre los textos elegidos para entrenar a GPT-3, el resultado sorprende. 

```xml
<categories="jewelry">
```

### Resultado
La categoría «jewelry» (joyería) no existe en nuestra edición del Ms. Fr. 640: el equipo editorial [prefiere](https://edition640.makingandknowing.org/#/content/resources) la más amplia de «Stones» (piedras). La intuición de GPT-3, sin embargo, es buena, y hace pensar que con un poco más de entrenamiento podría aprender a categorizar cualquier entrada del Ms. Fr. 640, y acaso las de otros textos técnicos del siglo XVI.   

## Experimento 2: marcado semántico
Subamos el listón. Si un transformador como GPT-3 puede aprender a categorizar textos según criterios editoriales concretos, ¿podrá también identificar parte de su marcado?  

> [!NOTE]
> *Secrets of Craft and Nature* ofrece una [combinación](https://edition640.makingandknowing.org/#/content/resources/principles) de etiquetas semánticas y estructurales. Por desgracia, GPT-3 no procesa imágenes, a diferencia de otros proyectos como [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Es probable que futuras versiones de GPT incorporen esa capacidad, imprescindible para reconocer la mayoría de los aspectos estructurales y materiales de un documento. Dejaremos de lado esas etiquetas y nos centraremos en el marcado que no exige reconocer imágenes.

### Diseño del prompt
Las etiquetas semánticas señalan animales, plantas, topónimos, percepciones sensoriales, etc. Para el prompt de entrenamiento escogí unos cuantos ejemplos de la edición:
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### Prueba
Probemos con el modelo `Davinci-codex` unas cuantas palabras fáciles: *Apothecary* (boticario), *smoke* (humo), *glassmakers* (vidrieros), *latten* (latón) y *snake* (serpiente). El resultado es inmediato e impecable:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Una prueba más exigente es la de las palabras compuestas, como *copper plates* (planchas de cobre), *walnut oil* (aceite de nuez) y *wood block* (taco de madera): se trata de ver si GPT-3 maneja bien las etiquetas anidadas. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Aquí el resultado es desigual: `Davinci-codex` solo etiquetó bien *walnut oil*, y no detectó las etiquetas anidadas `tl` y `m` en *copper plates* y *wood block*. Ahora bien, como muestra la siguiente prueba, estos errores se corrigen con un prompt de entrenamiento mejor. Tras añadir cinco ejemplos más de etiquetas anidadas, `Davinci-codex` devolvió un resultado casi perfecto, con un solo fallo (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusión
Conviene no olvidar que estas pruebas se hicieron con fragmentos de texto muy breves. Sospecho que, con más contexto en los ejemplos y en el prompt, los modelos GPT-3 rendirían aún mejor; y el ajuste fino con datos de entrenamiento ad hoc mejoraría sin duda la precisión del etiquetado.  
Aunque haría falta repetir estos experimentos a mayor escala para demostrar la fiabilidad de los modelos de lenguaje preentrenados, sí cabe concluir que {{< hl >}}este enfoque permite a los editores automatizar varias tareas de anotación en unos pocos pasos, con un ahorro potencial enorme de tiempo y dinero.{{< /hl >}}
