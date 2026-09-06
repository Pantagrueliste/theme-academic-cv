---
title: Automatizzare la marcatura nelle edizioni critiche digitali
subtitle: I modelli linguistici pre-addestrati possono far crescere davvero la produttività editoriale?

# Summary for listings and search engines
summary: "I modelli linguistici pre-addestrati possono togliere agli studiosi alcune delle incombenze più tediose e faticose di un’edizione. A partire dalle annotazioni curate di *Secrets of Craft and Nature in Renaissance France*, valuto fino a che punto un modello come GPT-3 possa essere addestrato in poco tempo ad annotare manoscritti tecnici del Cinquecento."

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
Come si producono edizioni critiche digitali senza svenarsi? Con questo post apro una serie dedicata all’edizione efficiente; qui valuto quale parte possano avere i modelli linguistici pre-addestrati nell’automazione delle operazioni editoriali, a cominciare dalla marcatura semantica.

{{< toc >}}

# Il problema
## Un lavoro d’amore
Quando c’è di mezzo l’amore non si bada a spese… o così, almeno, vuole il proverbio. E vale a maggior ragione per le edizioni critiche digitali: trascrivere, tradurre e annotare significa migliaia di ore di lavoro, che in un caso come quello di [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) sono state prestate da centinaia di collaboratori di altissima qualificazione.

Per certi versi è una fortuna che i progetti più in vista dell’umanistica digitale riescano a raccogliere le somme enormi di cui hanno bisogno. Ma una dipendenza così stretta dalla munificenza di fondazioni facoltose, università e agenzie governative, unita al bisogno prolungato di tante risorse umane, non è un modello economico su cui costruire il futuro.

Anzi: se vogliamo che studiosi di ogni parte del mondo rendano i documenti storici accessibili a un pubblico più vasto, {{< hl >}}il costo delle edizioni critiche digitali dovrebbe scendere di parecchi ordini di grandezza{{< /hl >}}. 

## Una soglia alta
Paradossalmente, {{< hl >}}la soluzione potrebbe venire proprio dai progetti più affamati di manodopera, come [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), che costituiscono un prezioso insieme di addestramento{{< /hl >}} per automatizzare le operazioni più ingrate e ripetitive dell’edizione digitale, a cominciare dalla marcatura.

Non che la marcatura sia cosa da poco. Al contrario: {{< hl >}}la marcatura è ormai la componente irrinunciabile di ogni progetto digitale che si rispetti.{{< /hl >}} Normalizzata dalla [Text Encoding Initiative](https://tei-c.org), permette di registrare del documento, e del testo che esso trasmette, quanti più aspetti si vogliano: struttura, note marginali, cancellature, varianti, tipo di carta, macchie, grafia… tutto quello che vi viene in mente.

L’esempio che segue, tratto da [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), mostra come la marcatura arricchisca il testo di informazioni ulteriori (categoria, struttura, campi semantici, cancellature e via dicendo), dando in definitiva alle edizioni digitali un vantaggio netto sui loro antenati di carta.

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

Informazioni preziose non soltanto a fini di conservazione, ma anche – come ho avuto modo di mostrare altrove – per la sintesi e l’analisi. Il guaio è che annotare in questo modo costa un tempo enorme, tanto più che lo stesso testo deve spesso esistere in più vesti: come traduzione, come trascrizione, come versione modernizzata e così via. 

# La soluzione
## I transformer: la via più breve all’automazione?
Nel 2020 [OpenAI](https://www.openai.com) ha presentato in pompa magna la sua nuova famiglia di modelli linguistici generalisti su larga scala, GPT-3, sigla di «Generative Pre-trained Transformer 3». I transformer sono una svolta recente dell’intelligenza artificiale: imparano compiti nuovi con una rapidità sconcertante, semplicemente leggendo un prompt e guardando un pugno di esempi; e possono ricevere un addestramento supplementare su un insieme di dati ad hoc (il cosiddetto fine-tuning), che ne migliora latenza e precisione. Per questo si dice che GPT-3 e i transformer analoghi sono [few-shot learners](https://arxiv.org/abs/2005.14165). 

OpenAI dichiara per GPT-3 la cifra record di 175 miliardi di parametri e un addestramento su oltre 570 GB di testo, in massima parte documenti in inglese presumibilmente raccolti da [internet](https://skylion007.github.io/OpenWebTextCorpus/). Per le sole dimensioni, GPT-3 ha fissato un nuovo metro di paragone nel settore: esegue fin da subito i compiti più diversi con un realismo che mette a disagio. Scrive [editoriali](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausibili, [conversa con gli umani](https://www.quickchat.ai/emerson) nelle chat, [risponde alle email](https://www.jarvis.ai/?fpr=serpbattle), [riassume testi](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduce documenti, spiega il gergo, e via dicendo.

Avendo accesso in anteprima all’API di OpenAI dal maggio 2021, ho potuto mettere alla prova il modello su una serie di compiti che passano per difficili: tradurre in inglese poesia francese e testi neolatini, spiegare analogie, perfino semplificare il quarto libro della *Fondazione della metafisica dei costumi* di Kant per un bambino di sette anni (con esiti, va detto, poco convincenti).

### Codex
Uno degli ultimi sviluppi di GPT-3 riguarda i linguaggi di programmazione. Il modello, battezzato *Codex*, traduce il linguaggio naturale in linguaggio informatico e viceversa. Se cerco, poniamo, un’espressione regolare che «trovi soltanto le parole che iniziano con la maiuscola», GPT-3 me la restituisce subito, e funzionante: ```[A-Z]+\w+```.

Secondo OpenAI, *Codex* sa lavorare con una dozzina di linguaggi, fra cui Python, JavaScript, Go, Perl, PHP, Ruby e Swift. Convertendo senza attriti lo pseudocodice in codice, permette di concentrarsi non sulla sintassi pignola di un linguaggio, ma sui passaggi logici e sulle strategie con cui un’applicazione risolve un problema.

### Oltre OpenAI
OpenAI, si capisce, non è sola in campo. Come si è detto, nel 2021 la Beijing Academy of Artificial Intelligence ha annunciato un modello ancora più grande e più capace, *Wu Dao 2*. Nvidia e Microsoft hanno unito le forze per produrre *Megatron-Turing NLG 530B*, un nome che dice tutto. Start-up più piccole come [AI21 Labs](https://www.ai21.com) e [Cohere](https://cohere.ai) offrono anch’esse API al pubblico, e meritano una menzione le iniziative open source come [EleutherAI](https://www.eleuther.ai). Il panorama, si sa, cambia in fretta: per seguire le novità del settore, tenete d’occhio [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Gli esperimenti

> [!NOTE]
> L’obiettivo di questi esperimenti è individuare la via più economica verso un’automazione affidabile delle operazioni editoriali. Si potrebbe obiettare che alcune di esse si prestano anche ad algoritmi di apprendimento supervisionato: è un’ipotesi che esploreremo in un prossimo post.

Un transformer come GPT-3 può imparare ad annotare, poniamo, un manoscritto tecnico-scientifico del Cinquecento?

## Esperimento 1 – Categorizzazione dei testi
Partiamo da qualcosa di relativamente semplice. Da bravo «few-shot learner», GPT-3 dovrebbe capire in fretta secondo quali criteri il nostro gruppo di lavoro ha classificato le voci del Ms. Fr. 640.

### Prompt engineering
Per addestrarlo mi sono servito di un prompt ridotto all’osso e di quattro brevi voci in testo semplice, scelte come esempi: fra queste, una di «medicina», una di «armi e armature» e una di «pittura». 

### Verifica
Ho poi incollato un altro passo, estraneo alla sequenza iniziale: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Il risultato è perfettamente in linea con il contenuto: 

```xml
<categories="painting">
```

Se proviamo con una voce di una categoria che non figurava nemmeno fra i testi scelti per l’addestramento di GPT-3, la risposta sorprende. 

```xml
<categories="jewelry">
```

### Risultato
La categoria «jewelry» (gioielli) non esiste nella nostra edizione del Ms. Fr. 640: il gruppo di lavoro [preferisce](https://edition640.makingandknowing.org/#/content/resources) quella, più ampia, di «Stones» (pietre). L’intuizione di GPT-3 è però buona, e lascia pensare che con un po’ di addestramento in più saprebbe categorizzare qualunque voce del Ms. Fr. 640, e forse anche quelle di testi tecnici cinquecenteschi affini.   

## Esperimento 2 – Marcatura semantica
Alziamo l’asticella. Se un transformer come GPT-3 impara a categorizzare i testi secondo criteri editoriali specifici, saprà anche riconoscerne, almeno in parte, la marcatura?  

> [!NOTE]
> *Secrets of Craft and Nature* adotta una [combinazione](https://edition640.makingandknowing.org/#/content/resources/principles) di etichette semantiche e strutturali. Purtroppo GPT-3 non elabora immagini, a differenza di altri progetti come [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). È probabile che le prossime versioni di GPT acquisiscano questa capacità, indispensabile per riconoscere la maggior parte degli aspetti strutturali e materiali di un documento. Lasceremo dunque da parte quei tag e ci concentreremo sulla marcatura che non richiede il riconoscimento delle immagini.

### Prompt engineering
I tag semantici segnalano animali, piante, toponimi, percezioni sensoriali e altro ancora. Nel prompt di addestramento ho raccolto qualche esempio tratto dall’edizione:
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
Proviamo con il modello `Davinci-codex` qualche parola facile: *Apothecary*, *smoke*, *glassmakers*, *latten* e *snake*. Le risposte arrivano all’istante e sono impeccabili:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Una prova più severa richiede parole composte – *copper plates*, *walnut oil*, *wood block* – per vedere se GPT-3 se la cava con i tag annidati. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Qui i risultati sono in chiaroscuro: `Davinci-codex` ha etichettato correttamente solo *walnut oil*, senza cogliere i tag `tl` e `m` annidati in *copper plates* e *wood block*. Ma, come mostra la prova successiva, basta un prompt di addestramento migliore per attenuare questi errori. Aggiunti altri cinque esempi di tag annidati, `Davinci-codex` ha restituito un risultato quasi perfetto, con un solo errore (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusione
Va ricordato che queste prove sono state condotte su frammenti di testo molto brevi. Sospetto che, dando più contesto negli esempi e nel prompt, i modelli GPT-3 farebbero ancora meglio; e un fine-tuning su insiemi di dati ad hoc migliorerebbe senza dubbio la precisione dell’etichettatura.  
Se per dimostrare l’affidabilità dei modelli linguistici pre-addestrati occorreranno ancora esperimenti su scala più ampia, si può nondimeno concludere che {{< hl >}}questo approccio permette a chi cura un’edizione di automatizzare parecchie operazioni di annotazione in pochi passaggi, con un risparmio potenzialmente enorme di tempo e di denaro.{{< /hl >}}
