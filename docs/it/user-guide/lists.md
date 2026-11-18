# Elenchi

Ogni tipo di oggetto in Gramps Web ha una vista elenco: Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Archivi, Note e Media. Funzionano tutti allo stesso modo e condividono gli stessi strumenti per ordinare, filtrare e modificare in blocco.

## Ordinamento e paginazione

Clicca sull'intestazione di una colonna per ordinare per quella colonna; cliccala di nuovo per invertire l'ordine. L'ordinamento viene eseguito dal server, quindi si applica all'intero elenco, non solo alla pagina che stai visualizzando.

Elenchi lunghi sono suddivisi in pagine. Usa i controlli di paginazione in fondo per spostarti tra di essi.

Sugli schermi stretti, la tabella passa automaticamente a un layout compatto, in modo che le viste elenco rimangano utilizzabili su un telefono.

## Scelta delle colonne

Clicca sull'icona dell'ingranaggio all'estremità destra della barra degli strumenti sopra l'elenco per aprire la finestra di dialogo **Colonne**. Seleziona o deseleziona una colonna per mostrarla o nasconderla. **Ripristina** ripristina la selezione predefinita per quell'elenco.

Almeno una colonna deve rimanere visibile, quindi l'ultima colonna rimanente non può essere deselezionata.

Oltre alle colonne predefinite, ogni elenco offre una colonna **Tag** e, per gli utenti che possono visualizzare record privati, una colonna **Privacy** che mostra un lucchetto per ogni oggetto privato. Se hai modificato la selezione delle colonne di un elenco in precedenza, nuove colonne come **Tag** non vengono aggiunte automaticamente; selezionale nella finestra di dialogo.

La tua selezione delle colonne viene memorizzata per tipo di oggetto e per albero genealogico. Viene archiviata nel tuo browser, quindi non è visibile ad altri utenti – ma non ti segue nemmeno su un browser o dispositivo diverso.

## Filtraggio

Clicca sul pulsante **filtra** per aprire il pannello di filtro. Offre tre modi per filtrare, che possono essere combinati:

- **Filtri predefiniti** in sezioni espandibili che dipendono dal tipo di oggetto. Per le persone, ad esempio, puoi filtrare per nome, anno di nascita, anno di morte, varie proprietà della persona, numero di associazioni, tag e se un oggetto è privato o pubblico. Le famiglie possono essere filtrate per il nome del padre, della madre o di un figlio, le fonti per autore e i luoghi e archivi per il loro tipo.
- **Filtro avanzato** – un costruttore di condizioni per filtri che i filtri predefiniti non possono esprimere, descritto [di seguito](#advanced-filter).
- **GOQL** – un campo di testo per un'espressione nel [Gramps Object Query Language](goql.md), con evidenziazione della sintassi. Digita l'espressione e premi Invio o clicca su **Applica**. Se l'espressione non è valida, il campo viene contrassegnato come errore. Un'espressione si applica sopra gli altri filtri.

I filtri attivi vengono mostrati come chip in una riga sotto la barra degli strumenti. Rimuovi un singolo filtro cliccando sul pulsante di cancellazione del chip, oppure usa **Cancella tutti i filtri** per rimuoverli tutti in una volta.

### Filtro avanzato

Clicca su **Filtro avanzato** in fondo al pannello di filtro per aprire il costruttore di condizioni. Le sue condizioni sono le regole di filtro note da Gramps Desktop, come "Persone con il &lt;nome&gt;" o "Antenati di &lt;persona&gt;".

- Clicca su **Aggiungi condizione** per scegliere una regola. Le regole sono raggruppate in categorie e possono essere cercate per nome o descrizione.
- Compila i parametri della regola. Ogni parametro ha un input corrispondente, ad esempio un campo data, un selettore di tag o un selettore di oggetti per una persona o un luogo.
- Scegli come le condizioni di un gruppo sono combinate: **Tutte le condizioni**, **Qualsiasi condizione**, o – tramite il menu accanto a esse – **Esattamente una condizione**.
- Clicca su **Aggiungi gruppo** per aggiungere un gruppo di condizioni all'interno di un altro gruppo, con il proprio modo di combinarle.
- Seleziona **Non** su una condizione o gruppo per invertirlo.

Clicca su **Applica** per filtrare l'elenco.

I filtri predefiniti e l'espressione GOQL che sono attivi quando apri il costruttore appaiono lì come condizioni. Un'espressione GOQL può anche essere aggiunta come condizione a sé stante, ad esempio per combinare diverse espressioni con **Qualsiasi condizione**. Se il filtro che costruisci può essere espresso con i filtri predefiniti, viene mostrato con essi dopo l'applicazione. Altrimenti, viene mostrato come un singolo chip **Filtro avanzato**, e il pannello di filtro offre un pulsante **Modifica** per riaprire il costruttore.

!!! nota
    Le regole che si riferiscono a filtri personalizzati salvati in Gramps Desktop non sono disponibili nel costruttore. Le regole sono mostrate nella tua lingua con Gramps Web API 3.24 o versioni successive.

#### Filtri salvati

Per riutilizzare un filtro che hai costruito, clicca su **Salva** nel costruttore di condizioni e dagli un nome. Salvare sotto un nome esistente sostituisce quel filtro. **Filtri salvati** nel costruttore elenca i filtri salvati per il tipo di oggetto corrente; selezionandone uno lo carichi nel costruttore, dove puoi modificarlo prima di cliccare su **Applica**.

I filtri salvati sono memorizzati nel tuo browser, per albero genealogico e tipo di oggetto, quindi non sono disponibili per altri utenti o sui tuoi altri dispositivi.

Un filtro salvato può smettere di funzionare quando l'albero cambia, ad esempio se si riferisce a una persona che è stata successivamente eliminata (il selettore di oggetti mostra quindi "Non trovato"). Un tale filtro non può essere applicato o salvato fino a quando la condizione non viene corretta.

## Selezione di oggetti e azioni in blocco

Gli utenti con permessi di modifica vedono un pulsante **Seleziona** accanto al pulsante di filtro. Cliccalo per entrare in modalità di selezione, che aggiunge una casella di controllo a ogni riga.

Seleziona gli oggetti desiderati e appare una barra degli strumenti che mostra quanti sono selezionati, insieme a un menu a discesa **Azione** e un pulsante **Applica**.

La casella di controllo nell'intestazione della tabella seleziona tutti gli oggetti nella pagina corrente. Se ci sono più oggetti che corrispondono ai filtri correnti, la barra degli strumenti offre quindi **Seleziona tutti (N)**, che seleziona tutti gli N oggetti corrispondenti su tutte le pagine. Deselezionare una riga, cambiare pagina o filtri, o uscire dalla modalità di selezione termina questa selezione.

### Elimina

Seleziona uno o più oggetti, scegli **Elimina** e clicca su **Applica**. Una finestra di conferma ti chiede di confermare, avvisando che l'azione non può essere annullata.

Eliminare più di dieci oggetti viene eseguito come un'attività in background. Il suo progresso viene mostrato accanto al pulsante **Applica** e nelle [Notifiche](notifications.md), e l'elenco si ricarica quando è completato.

!!! consiglio
    Le eliminazioni sono registrate nella [cronologia delle revisioni](revisions.md) come qualsiasi altra modifica, quindi un'eliminazione errata in blocco può essere annullata ripristinando la transazione corrispondente.

### Tag e privacy

Le azioni **Aggiungi Tag**, **Rimuovi Tag** e **Privacy** modificano tutti gli oggetti selezionati contemporaneamente (richiede Gramps Web API 3.26 o versioni successive):

- **Aggiungi Tag** aggiunge un tag esistente o uno nuovo che crei nella finestra di dialogo.
- **Rimuovi Tag** rimuove un tag dagli oggetti selezionati che lo hanno.
- **Privacy** contrassegna gli oggetti selezionati come privati o pubblici. Questo cambia solo gli oggetti stessi, non le loro parti o i record a cui sono collegati – vedi [Record privati](privacy.md).

Come per l'eliminazione, modificare più di dieci oggetti viene eseguito come un'attività in background. Le modifiche sono registrate nella [cronologia delle revisioni](revisions.md) come un'unica transazione, quindi possono essere annullate insieme.

### Unisci

Seleziona **esattamente due** oggetti, scegli **Unisci** e clicca su **Applica**. Una finestra di dialogo chiede quale dei due dovrebbe fornire i dati principali per l'oggetto unito; clicca su quello che vuoi mantenere come principale. I dati dell'altro oggetto vengono uniti in esso e i riferimenti vengono aggiornati.

L'unione è disponibile per persone, famiglie, eventi, luoghi, fonti e citazioni. Non è disponibile per archivi, note e oggetti multimediali.

Nella vista media, la selezione funziona sia nel layout galleria che nell'elenco: in modalità di selezione, cliccare su una tessera o riga la attiva/disattiva. Gli oggetti multimediali non possono essere uniti.

Se scegli un'azione senza una selezione valida – ad esempio un'unione con solo un oggetto selezionato – una finestra di dialogo spiega cosa è richiesto.
