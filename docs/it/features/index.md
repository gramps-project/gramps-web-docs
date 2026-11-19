---
hide:
  - toc
  - navigation
---

# Caratteristiche

Gramps Web è un'app web per la genealogia collaborativa. È costruita su [Gramps](https://gramps-project.org/), il programma di genealogia open-source, e funziona con gli stessi dati. Puoi eseguirla sul tuo server o utilizzare un fornitore di hosting.

[Prova la demo](#demo){ .md-button .md-button--primary } [Inizia](../install_setup/setup.md){ .md-button }

## Esplora il tuo albero genealogico { .feature-group }

![Grafico a ventaglio che mostra sette generazioni di antenati](screenshots/fan.png){ align=right width="400"}

### Grafici interattivi dell'albero genealogico

Naviga nel tuo albero genealogico come un albero degli antenati, albero dei discendenti, grafico a clessidra, grafico delle relazioni o grafico a ventaglio, con grafiche interattive di alta qualità e un numero configurabile di generazioni.

Passa il mouse su qualsiasi persona per vedere una scheda di anteprima con i loro fatti principali e salta direttamente dal grafico alla pagina dei dettagli completi.

<div style="clear:both;"></div>

---

![Cronologia degli eventi familiari tra gli anni '40 e '70](screenshots/timeline.png){ align=left width="400"}

### Cronologia cronologica

Vedi ogni evento nel tuo albero genealogico disposto su una cronologia orizzontale e zoomabile. Scorri e ingrandisci attraverso i secoli, quindi filtra per una singola persona – o per tutti i loro antenati o discendenti – o per tutto ciò che è accaduto in un luogo.

Vedi [Cronologia](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Mappa di Londra con un luogo selezionato, che mostra la sua foto e gli eventi](screenshots/map.png){ align=right width="400"}

### Mappa interattiva

Visualizza tutti i luoghi nel tuo albero su una mappa interattiva e ricercabile. Cerca nuovi luoghi direttamente su OpenStreetMap quando crei un luogo, traccia le persone nel tuo database geograficamente e segui la vita di una singola persona collegando i loro eventi con linee sulla mappa.

<div style="clear:both;"></div>

---

![Londra sul layer OpenHistoricalMap, con il cursore temporale impostato su 1707](screenshots/ohm.png){ align=left width="400"}

### Mappe storiche

Trasforma una mappa storica memorizzata come oggetto multimediale in Gramps in un overlay mappa personalizzato.

Puoi anche passare alle mappe vettoriali storiche del progetto [OpenHistoricalMap](https://www.openhistoricalmap.org/). Usa il cursore temporale per scorrere attraverso l'evoluzione dei luoghi nella tua storia familiare e visualizza i luoghi in cui gli antenati vivevano o dove sono accaduti eventi.

<div style="clear:both;"></div>

---

![Risultati di ricerca per "Albert" tra persone, eventi e media](screenshots/search.png){ align=right width="400"}

### Trova qualsiasi cosa

Il motore di ricerca full-text copre tutti i tipi di oggetti Gramps, inclusi i contenuti delle note testuali, e supporta caratteri jolly e operatori logici.

Per query precise, le visualizzazioni dell'elenco degli oggetti offrono una modalità di filtro avanzata basata sul [Gramps Object Query Language](../user-guide/goql.md), insieme a filtri rapidi per testo, tag e privacy.

Dalla pagina di qualsiasi persona, [Ricerca Esterna](../user-guide/external-search.md) apre una ricerca precompilata su FamilySearch, Ancestry, CompGen e altri siti – e puoi aggiungere i tuoi.

<div style="clear:both;"></div>

## Costruisci e ricerca { .feature-group }

![Albero genealogico in modalità modifica con il dialogo per aggiungere un familiare](screenshots/tree-edit.png){ align=left width="400"}

### Costruisci il tuo albero direttamente nel grafico

Passa la vista dell'albero in modalità modifica e fai crescere il tuo albero genealogico senza lasciare il grafico. Ogni scheda persona ha un pulsante **+** per aggiungere un padre, una madre, un figlio o un coniuge – collegando qualcuno già nel tuo database o creando una persona completamente nuova sul posto. Ogni modifica viene salvata immediatamente.

Vedi [Modifica dell'albero genealogico](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![L'assistente AI che legge un certificato di nascita e propone nuovi record](screenshots/chat.png){ align=right width="400"}

### Assistente AI integrato

Fai domande sul tuo albero genealogico nella tua lingua e ricevi risposte basate sui tuoi dati.

L'assistente non si limita a cercare: interroga direttamente il tuo database con un insieme di strumenti, filtrando persone, eventi, famiglie e luoghi, e calcolando le relazioni tra gli individui. Puoi vedere quali strumenti sta utilizzando mentre costruisce una risposta, e le domande più lunghe vengono eseguite come attività in background in modo da poter navigare altrove e tornare.

L'assistente è facoltativo e deve essere [configurato dall'amministratore del server](../install_setup/chat.md) con un fornitore di modelli AI.

<div style="clear:both;"></div>

---

![Browser dei cromosomi che mostra i segmenti di DNA condivisi di undici corrispondenze](screenshots/dna.png){ align=left width="400"}

### Corrispondenze DNA, browser dei cromosomi & Y-DNA

Carica i dati delle corrispondenze DNA dal tuo fornitore di test DNA, memorizzali insieme al tuo albero genealogico e visualizza le tue corrispondenze in un browser dei cromosomi interattivo.

I dati grezzi SNP del cromosoma Y possono essere utilizzati per determinare il [gruppo haplogroup Y-DNA](../user-guide/y-dna.md) più probabile di una persona e visualizzare i loro antenati patrilineari nell'albero del cromosoma Y umano, con stime temporali. L'analisi viene eseguita interamente sul tuo server – nessun dato viene inviato a terzi.

<div style="clear:both;"></div>

---

![Dipinto con due persone contrassegnate e gli altri volti rilevati delineati](screenshots/tag.png){ align=right width="400"}

### Contrassegna le persone nelle foto con il rilevamento facciale automatico

Identifica gli antenati nelle vecchie foto di famiglia insieme ai tuoi parenti. I volti vengono rilevati automaticamente, quindi contrassegnare una persona richiede due clic.

<div style="clear:both;"></div>

---

![Elenco delle attività di ricerca con stato, priorità e tag](screenshots/tasks.png){ align=left width="400"}

### App di gestione delle attività integrata

Gramps Web viene fornito con un'app di gestione delle attività integrata per organizzare e pianificare la tua ricerca genealogica. Assegna a ogni attività uno stato, una priorità e tag, documenta i tuoi progressi in una descrizione in formato testo arricchito e allega i media raccolti lungo il percorso.

Le attività sono memorizzate come fonti nel database di Gramps, quindi fanno parte dei tuoi dati genealogici e possono essere accessibili e modificate anche in Gramps Desktop.

<div style="clear:both;"></div>

---

![Post del blog sull'identificazione delle persone in una fotografia di famiglia](screenshots/blog.png){ align=right width="400"}

### Blog di genealogia incluso

Riassumi la tua ricerca sotto forma di storie di blog con immagini e condividile con i tuoi parenti. Un editor dedicato rende la scrittura di un nuovo post semplice. Tutti i dati sono memorizzati nel database di Gramps.

<div style="clear:both;"></div>

## Lavorare insieme { .feature-group }

![Elenco delle persone nell'albero genealogico](screenshots/list.png){ align=left width="400"}

### Livelli di privacy e accesso degli utenti

Puoi [contrassegnare i record come privati](../user-guide/privacy.md) – fino a un singolo nome, collegamento a un evento o corrispondenza DNA – e controllare quali utenti possono visualizzare i record privati. I record privati vengono filtrati a livello di database per la massima sicurezza. Inoltre, puoi controllare cosa gli utenti possono aggiungere e modificare.

Gli utenti possono accedere con una password o tramite un fornitore di identità esterno utilizzando [OpenID Connect](../install_setup/oidc.md) – Google e Microsoft già integrati, più fornitori personalizzati come Keycloak, Authentik e Authelia.

<div style="clear:both;"></div>

---

![Una revisione che mostra i campi modificati in un record di persona](screenshots/revisions.png){ align=right width="400"}

### Cronologia delle revisioni completa – con annullamento

Ogni modifica al tuo albero genealogico viene registrata. Sfoglia l'intera cronologia raggruppata per transazione, approfondisci qualsiasi modifica individuale per vedere esattamente quali campi sono stati aggiunti, rimossi o modificati, e annulla una transazione se si rivela essere un errore. Ogni pagina di oggetto ha anche la propria scheda di revisione che mostra chi l'ha modificata e quando.

Vedi [Cronologia delle revisioni](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Menu Strumenti di Gramps Desktop con l'entry Gramps Web Sync](screenshots/sync.png){ align=left width="300"}

### Integrazione completa con Gramps Desktop

Gramps Web utilizza lo stesso modello di dati e database di [Gramps Desktop](https://gramps-project.org/). Puoi sfogliare e modificare tutti gli stessi [tipi di record](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): persone, famiglie, eventi, luoghi, repository, fonti, citazioni, oggetti multimediali e note.

Con il [complemento Gramps Web Sync](../administration/sync.md) per Gramps Desktop, puoi sincronizzare i tuoi dati in entrambe le direzioni, in modo da poter continuare a lavorare in Gramps Desktop e in Gramps Web fianco a fianco.

<div style="clear:both;"></div>

## Report e esportazione dei dati { .feature-group }

![Report sugli antenati generato come PDF](screenshots/report.png){ align=right width="400"}

### Genera report stampabili

Gramps Web è costruito sullo stesso nucleo di Gramps Desktop, quindi puoi generare quasi tutti i [report](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) supportati dall'app desktop direttamente dal browser, inclusi grafici delle relazioni o report di libri in PDF.

<div style="clear:both;"></div>

---

![Pagina di esportazione con l'elenco dei formati di file disponibili](screenshots/export.png){ align=left width="300"}

### Nessun lock-in – importazione ed esportazione dei dati

Importa dati in vari formati, inclusi Gramps XML e GEDCOM, e scarica tutti i tuoi dati in qualsiasi momento – dati dell'albero genealogico, file multimediali e account utente – per backup o per spostarti su un server diverso.

Le importazioni possono essere visualizzate in anteprima come prova prima che venga scritto qualcosa, e un backup completo può essere ripristinato nell'albero.

<div style="clear:both;"></div>

## Usalo ovunque { .feature-group }

![La stessa pagina di una persona su un desktop e su un telefono](screenshots/mobile.png){ align=right width="400"}

### Funziona su ogni dispositivo

Usa Gramps Web su qualsiasi dispositivo con un browser web: carica foto, crea o modifica record, o mostra il tuo albero genealogico ai parenti alla prossima riunione di famiglia.

Gramps Web è un'app web progressiva: installala sulla tua schermata principale o sul desktop e si comporta come un'app nativa. Sul desktop, le [scorciatoie da tastiera](../user-guide/shortcuts.md) ti portano ovunque in un paio di tasti – premi `?` per vederle tutte.

<div style="clear:both;"></div>

---

![Menu di selezione della lingua](screenshots/lang.png){ align=left width="300"}

### Completamente internazionalizzato

Usa l'interfaccia in uno qualsiasi dei più di 50 lingue tradotte dalla comunità di Gramps.

<div style="clear:both;"></div>

## E altro ancora

- **Notifiche e attività in background** – importazioni, esportazioni, report e ricostruzioni di indici vengono eseguiti in background, con progressi ed errori raccolti in un unico posto
- **Tag, segnalibri e cronologia** – organizza gli oggetti con tag codificati a colori e torna a ciò su cui stavi lavorando
- **Modifica di massa** – seleziona più oggetti nelle visualizzazioni dell'elenco per eliminarli tutti in una volta o unire oggetti duplicati
- **Visualizzazioni dell'elenco personalizzabili** – scegli quali colonne mostrare e filtra per testo, tag o privacy
- **Riconoscimento del testo (OCR)** – estrai testo da documenti scansionati nella tua galleria multimediale
- **Verifica dei dati** – controlla il tuo albero per date implausibili e altri problemi di dati
- **Calendari** – inserisci date nel calendario gregoriano, giuliano, ebraico, repubblicano francese, persiano, islamico o svedese
- **Rendilo tuo** – dai al tuo sito un nome, colori del tema e testo e immagine della homepage

## Demo

Per accedere alla demo, utilizza una delle seguenti coppie nome utente/password. Ognuna rappresenta uno dei ruoli utente in Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

La demo viene ripristinata ogni due ore, quindi eventuali modifiche che apporti sono temporanee.

[Vai al Login della Demo](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Grazie

La demo è gentilmente supportata da DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
