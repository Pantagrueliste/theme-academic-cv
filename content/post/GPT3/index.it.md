---
title: Automatizzare la marcatura nelle edizioni critiche digitali
subtitle: I modelli linguistici pre-addestrati possono aumentare in modo significativo la produttività editoriale?

# Summary for listings and search engines
summary: "I modelli linguistici pre-addestrati possono aiutare gli studiosi ad automatizzare alcune delle operazioni più tediose e laboriose di un’edizione. A partire dalle annotazioni curate di *Secrets of Craft and Nature in Renaissance France*, valuto in che misura un modello come GPT-3 possa essere addestrato rapidamente ad annotare manoscritti tecnici del Cinquecento."

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
- Umanistica digitale
- Apprendimento automatico
- Edizioni critiche digitali
- Ricerca in corso

categories:
- Edizione efficiente
---
# Introduzione
Come produrre edizioni critiche digitali senza rovinarsi? In questo post, il primo di una serie dedicata all’edizione efficiente, valuto il ruolo che i modelli linguistici pre-addestrati possono svolgere nell’automazione delle operazioni editoriali, come la marcatura semantica.

{{< toc >}}

# Il problema
## Un lavoro d’amore
In amore non si bada a spese… o almeno così recita il vecchio proverbio. Vale in modo particolare per le edizioni critiche digitali: la trascrizione, la traduzione e l’annotazione necessarie alla loro realizzazione comportano migliaia di ore di lavoro, svolte – come nel caso di [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – da centinaia di collaboratori altamente qualificati.

In un certo senso, che i progetti di punta dell’umanistica digitale riescano a ottenere gli ingenti finanziamenti di cui hanno bisogno è una fortuna. Eppure la forte dipendenza dalla generosità di fondazioni facoltose, università e agenzie governative, e il bisogno prolungato di risorse umane considerevoli, non costituiscono un modello economico sostenibile per il futuro.

Anzi, se vogliamo incoraggiare studiosi di tutto il mondo a rendere i documenti storici accessibili a un pubblico più ampio, {{< hl >}}il costo delle edizioni critiche digitali dovrebbe diminuire di diversi ordini di grandezza{{< /hl >}}. 

## Una soglia alta
Paradossalmente, {{< hl >}}la soluzione potrebbe venire proprio da progetti ad alta intensità di lavoro come [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), che costituiscono un prezioso insieme di addestramento{{< /hl >}} per automatizzare alcune delle operazioni più ingrate e ripetitive dell’edizione digitale, come la marcatura.

Non che la marcatura sia poco importante. Al contrario, {{< hl >}}la marcatura è diventata la componente indispensabile di ogni progetto digitale serio.{{< /hl >}} Standardizzata dalla [Text Encoding Initiative](https://tei-c.org), ci permette di registrare il maggior numero possibile di aspetti del documento e del testo che esso trasmette: struttura, annotazioni marginali, cancellature, varianti, tipo di carta, macchie, calligrafia… tutto ciò che si vuole.

Tratto da [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), l’esempio seguente mostra come la marcatura arricchisca il testo di informazioni aggiuntive (categoria, struttura, campi semantici, cancellature ecc.), dando in definitiva alle edizioni digitali un vantaggio significativo sui loro antenati materiali.

<table>
<tr>
<th> Testo semplice </th>
<th> Marcatura XML</th>
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

Queste informazioni non sono preziose soltanto a fini archivistici, ma anche, come ho mostrato in altre occasioni, a fini sintetici e analitici. Tuttavia questo tipo di annotazione può richiedere moltissimo tempo, perché lo stesso testo deve spesso essere disponibile in più versioni: come traduzione, come trascrizione, come modernizzazione ecc. 

# La soluzione
## I transformer: la via più semplice all’automazione?
Nel 2020 [OpenAI](https://www.openai.com) ha presentato in pompa magna la sua ultima famiglia di modelli linguistici generalisti su larga scala, chiamata GPT-3, sigla di «Generative Pre-trained Transformer 3». I transformer rappresentano una svolta piuttosto recente nell’intelligenza artificiale. Imparano nuovi compiti con una rapidità impressionante, semplicemente leggendo un prompt e osservando un numero molto limitato di esempi. Possono inoltre ricevere un addestramento aggiuntivo con un insieme di dati ad hoc (fine-tuning), che ne migliora latenza e precisione. Per questo si dice che GPT-3 e i transformer analoghi sono [few-shot learners](https://arxiv.org/abs/2005.14165). 

OpenAI sostiene che GPT-3 contenga la cifra record di 175 miliardi di parametri e che sia stato addestrato su più di 570 GB di testo, in maggioranza documenti in inglese presumibilmente tratti da [internet](https://skylion007.github.io/OpenWebTextCorpus/). Per le sue sole dimensioni, GPT-3 ha fissato un nuovo standard nel settore, eseguendo fin da subito compiti diversi con un realismo inquietante. Scrive [editoriali](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausibili, [dialoga con gli esseri umani](https://www.quickchat.ai/emerson) nelle chat, [risponde alle email](https://www.jarvis.ai/?fpr=serpbattle), [riassume testi](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduce documenti, spiega il gergo, e così via.

Avendo avuto accesso anticipato all’API di OpenAI dal maggio 2021, ho potuto sperimentare la capacità del modello di risolvere una serie di compiti notoriamente difficili, come tradurre in inglese poesia francese e testi neolatini, spiegare analogie e perfino semplificare il quarto libro della *Fondazione della metafisica dei costumi* di Kant per un bambino di sette anni (benché in modo poco convincente).

### Codex
Uno degli ultimi sviluppi di GPT-3 riguarda i linguaggi di programmazione. Chiamato *Codex*, questo modello traduce il linguaggio naturale in linguaggio informatico e viceversa. Per esempio, se cerco un’espressione regolare che mi permetta di «trovare solo le parole che iniziano con una lettera maiuscola», GPT-3 la traduce prontamente in un’espressione regolare funzionante: ```[A-Z]+\w+```.

OpenAI sostiene che *Codex* sappia lavorare con una dozzina di linguaggi di programmazione, tra cui Python, JavaScript, Go, Perl, PHP, Ruby e Swift. Convertendo senza sforzo lo pseudocodice in codice, *Codex* permette di concentrarsi non sulla sintassi fastidiosa di un linguaggio informatico, ma sui passaggi logici e sulle strategie che consentono alle applicazioni di risolvere problemi.

### Oltre OpenAI
OpenAI, naturalmente, non è l’unico attore in campo. Come accennato, la Beijing Academy of Artificial Intelligence ha annunciato nel 2021 un modello ancora più grande e più capace, noto come *Wu Dao 2*. Nvidia e Microsoft hanno unito le forze per produrre il modello dal nome eloquente *Megatron-Turing NLG 530B*. Start-up più piccole come [AI21 Labs](https://www.ai21.com) e [Cohere](https://cohere.ai) propongono anch’esse API al pubblico. Meritano una menzione anche le iniziative open source come [EleutherAI](https://www.eleuther.ai). Il panorama dell’IA, ovviamente, evolve molto in fretta; per seguire le nuove iniziative del settore, date un’occhiata a [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Gli esperimenti

> [!NOTE]
> L’obiettivo di questi esperimenti è trovare la via più economica per un’automazione affidabile delle operazioni editoriali. Si potrebbe obiettare che alcune di esse potrebbero essere automatizzate anche con algoritmi di apprendimento supervisionato. Esploreremo questa ipotesi in un prossimo post.

Un transformer come GPT-3 può imparare ad annotare, per esempio, un manoscritto tecnico e scientifico del Cinquecento?

## Esperimento 1 – Categorizzazione dei testi
Cominciamo con qualcosa di relativamente semplice. In quanto «few-shot learner», GPT-3 dovrebbe essere in grado di capire rapidamente come il nostro gruppo editoriale ha classificato le voci del Ms. Fr. 640.

### Prompt engineering
Per addestrarlo ho usato un prompt molto essenziale e ho selezionato come esempi quattro brevi voci in testo semplice, tra cui una sulla «medicina», una sulle «armi e armature» e una sulla «pittura». 

### Verifica
Ho poi copiato un altro passo che non faceva parte della sequenza iniziale: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Il risultato è perfettamente coerente con il contenuto: 

```xml
<categories="painting">
```

Se proviamo con una voce appartenente a una categoria che non era nemmeno compresa nella selezione iniziale di testi scelti per addestrare GPT-3, il risultato è sorprendente. 

```xml
<categories="jewelry">
```

### Risultato
La categoria «jewelry» (gioielleria) non esiste nella nostra edizione del Ms. Fr. 640. Il gruppo editoriale [preferisce](https://edition640.makingandknowing.org/#/content/resources) la categoria più ampia «Stones» (pietre). L’intuizione di GPT-3 è però buona, e indica che con un po’ più di addestramento può imparare a categorizzare qualsiasi voce del Ms. Fr. 640, e forse anche quelle di testi tecnici cinquecenteschi analoghi.   

## Esperimento 2 – Marcatura semantica
Alziamo un po’ l’asticella. Se i transformer come GPT-3 sanno imparare a categorizzare i testi secondo criteri editoriali specifici, sanno anche riconoscere parte della loro marcatura?  

> [!NOTE]
> *Secrets of Craft and Nature* offre una [combinazione](https://edition640.makingandknowing.org/#/content/resources/principles) di etichette semantiche e strutturali. Purtroppo GPT-3 non elabora immagini, a differenza di altri progetti come [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). È probabile che le prossime iterazioni di GPT includano questa capacità, necessaria per riconoscere la maggior parte degli aspetti strutturali e materiali di un documento. Tralasceremo dunque questi tag particolari e ci concentreremo sulla marcatura che non richiede il riconoscimento delle immagini.

### Prompt engineering
I tag semantici comprendono riferimenti ad animali, piante, toponimi, percezioni sensoriali ecc. Nel prompt di addestramento ho selezionato alcuni esempi tratti dall’edizione:
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
### Verifica
Proviamo alcune parole facili con il modello `Davinci-codex`, come *Apothecary*, *smoke*, *glassmakers*, *latten* e *snake*. I risultati sono immediati e impeccabili:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Una prova più difficile implica l’uso di parole composte, come *copper plates*, *walnut oil* e *wood block*. Lo scopo di questa prova è verificare se GPT-3 gestisce correttamente i tag annidati. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

I risultati però sono contrastanti, perché `Davinci-codex` ha etichettato correttamente solo *walnut oil*, senza rilevare i tag annidati `tl` e `m` in *copper plates* e *wood block*. Tuttavia, come mostra la prova successiva, questi errori possono essere attenuati con un prompt di addestramento migliore. Dopo l’aggiunta di altri cinque esempi di tag annidati, `Davinci-codex` ha restituito un risultato quasi impeccabile, con un solo errore (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusione
È importante ricordare che queste prove sono state condotte su frammenti di testo brevi. Sospetto che, fornendo più contesto negli esempi e nel prompt, i modelli GPT-3 darebbero risultati ancora migliori. Inoltre, il fine-tuning del modello con insiemi di addestramento ad hoc migliorerebbe senza dubbio ulteriormente la precisione dell’etichettatura.  
Se questi esperimenti andrebbero ancora condotti su scala più ampia per dimostrare l’affidabilità dei modelli linguistici pre-addestrati, possiamo nondimeno concludere che {{< hl >}}questo approccio permette agli editori di automatizzare diverse operazioni di annotazione in pochi semplici passaggi, con un potenziale risparmio enorme di tempo e di denaro.{{< /hl >}}
