# Elenchi

Ogni tipo di oggetto in Gramps Web ha una vista elenco: Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Archivi, Note e Media. Funzionano tutte allo stesso modo e condividono gli stessi strumenti per ordinare, filtrare e modificare in massa.

## Ordinamento e paginazione

Clicca sull'intestazione di una colonna per ordinare in base a quella colonna; cliccala di nuovo per invertire l'ordine. L'ordinamento viene eseguito dal server, quindi si applica all'intero elenco, non solo alla pagina che stai visualizzando.

Elenchi lunghi sono suddivisi in pagine. Usa i controlli di paginazione in basso per spostarti tra di esse.

Sugli schermi stretti, la tabella passa automaticamente a un layout compatto, in modo che le viste elenco rimangano utilizzabili su un telefono.

## Scelta delle colonne

Clicca sull'icona dell'ingranaggio sopra l'elenco per aprire la finestra di dialogo **Colonne**. Seleziona o deseleziona una colonna per mostrarla o nasconderla. **Ripristina** ripristina la selezione predefinita per quell'elenco.

Almeno una colonna deve rimanere visibile, quindi l'ultima colonna rimanente non può essere deselezionata.

La tua selezione di colonne viene memorizzata per tipo di oggetto e per albero genealogico. È memorizzata nel tuo browser, quindi non è visibile ad altri utenti – ma non ti segue nemmeno su un browser o dispositivo diverso.

## Filtraggio

Clicca sul pulsante **filtra** per aprire il pannello di filtraggio. Offre tre modi per filtrare, che possono essere combinati:

- **Filtri predefiniti** in sezioni espandibili che dipendono dal tipo di oggetto. Per le persone, ad esempio, puoi filtrare per anno di nascita, anno di morte, varie proprietà della persona, numero di associazioni, tag e se un oggetto è privato o pubblico.
- **Filtro avanzato** – un costruttore di condizioni per filtri che quelli predefiniti non possono esprimere, descritto [di seguito](#filtro-avanzato).
- **GQL** – un campo di testo per una query nel [Gramps Query Language](gql.md). Digita la query e premi Invio o clicca su **Applica**. Se la query non è valida, il bordo del campo diventa rosso. Una query si applica sopra gli altri filtri.

I filtri attivi vengono mostrati come chip sopra l'elenco. Rimuovi un singolo filtro cliccando sul pulsante di cancellazione del chip, oppure usa **Cancella tutti i filtri** per rimuoverli tutti in una volta.

### Filtro avanzato

Clicca su **Filtro avanzato** in fondo al pannello di filtraggio per aprire il costruttore di condizioni. Le sue condizioni sono le regole di filtro conosciute da Gramps Desktop, come "Persone con il &lt;nome&gt;" o "Antenati di &lt;persona&gt;".

- Clicca su **Aggiungi condizione** per scegliere una regola. Le regole sono raggruppate in categorie e possono essere cercate per nome o descrizione.
- Compila i parametri della regola. Ogni parametro ha un input corrispondente, ad esempio un campo data, un selettore di tag o un selettore di oggetti per una persona o un luogo.
- Scegli come le condizioni di un gruppo sono combinate: **Tutte le condizioni**, **Qualsiasi condizione**, o – tramite il menu accanto a esse – **Esattamente una condizione**.
- Clicca su **Aggiungi gruppo** per aggiungere un gruppo di condizioni all'interno di un altro gruppo, con il proprio modo di combinarle.
- Seleziona **Non** su una condizione o gruppo per invertirla.

Clicca su **Applica** per filtrare l'elenco.

I filtri predefiniti che sono attivi quando apri il costruttore appaiono lì come condizioni. Se il filtro che costruisci può essere espresso con i filtri predefiniti, viene mostrato con essi dopo l'applicazione. Altrimenti, viene mostrato come un singolo chip di **Filtro avanzato**, e il pannello di filtraggio offre un pulsante **Modifica** per riaprire il costruttore.

!!! nota
    Le regole che si riferiscono a filtri personalizzati salvati in Gramps Desktop non sono disponibili nel costruttore. Le regole sono mostrate nella tua lingua con Gramps Web API 3.24 o versioni successive.

## Selezione di oggetti e azioni in massa

Gli utenti con permessi di modifica vedono un pulsante **Seleziona** accanto al pulsante di filtro. Cliccalo per entrare in modalità di selezione, che aggiunge una casella di controllo a ogni riga.

Seleziona gli oggetti che desideri, e appare una barra degli strumenti che mostra quanti sono selezionati, insieme a un menu a discesa **Azione** e a un pulsante **Applica**.

La casella di controllo nell'intestazione della tabella seleziona tutti gli oggetti nella pagina corrente. Se più oggetti corrispondono ai filtri attuali, la barra degli strumenti offre quindi **Seleziona tutto (N)**, che seleziona tutti gli N oggetti corrispondenti su tutte le pagine. Deselezionare una riga, cambiare pagina o filtri, o uscire dalla modalità di selezione termina questa selezione.

### Elimina

Seleziona uno o più oggetti, scegli **Elimina**, e clicca su **Applica**. Una finestra di conferma ti chiede di confermare, avvisando che l'azione non può essere annullata.

L'eliminazione di più di dieci oggetti viene eseguita come un'attività in background. Il suo progresso è mostrato accanto al pulsante **Applica** e nelle [Notifiche](notifications.md), e l'elenco si ricarica quando è completata.

!!! suggerimento
    Le eliminazioni vengono registrate nella [cronologia delle revisioni](revisions.md) come qualsiasi altra modifica, quindi un'eliminazione di massa errata può essere annullata annullando la transazione corrispondente.

### Unisci

Seleziona **esattamente due** oggetti, scegli **Unisci**, e clicca su **Applica**. Una finestra di dialogo chiede quale dei due dovrebbe fornire i dati principali per l'oggetto unito; clicca su quello che vuoi mantenere come principale. I dati dell'altro oggetto vengono uniti in esso e i riferimenti vengono aggiornati.

L'unione è disponibile per persone, famiglie, eventi, luoghi, fonti e citazioni. Non è disponibile per archivi, note e oggetti multimediali.

Nella vista media, la selezione funziona sia nella galleria che nel layout elenco: in modalità di selezione, cliccare su una tessera o riga la attiva/disattiva. **Elimina** è l'unica azione disponibile per i media.

Se scegli un'azione senza una selezione valida – ad esempio un'unione con solo un oggetto selezionato – una finestra di dialogo spiega cosa è richiesto.
