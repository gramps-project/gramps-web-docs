# Elenchi

Ogni tipo di oggetto in Gramps Web ha una vista elenco: Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Archivi, Note e Media. Funzionano tutte allo stesso modo e condividono gli stessi strumenti per ordinare, filtrare e modificare in blocco.

## Ordinamento e paginazione

Clicca sull'intestazione di una colonna per ordinare per quella colonna; cliccala di nuovo per invertire l'ordine. L'ordinamento viene eseguito dal server, quindi si applica all'intero elenco, non solo alla pagina che stai visualizzando.

Elenchi lunghi sono suddivisi in pagine. Usa i controlli di paginazione in fondo per spostarti tra di esse.

Sugli schermi stretti, la tabella passa automaticamente a un layout compatto, così le viste elenco rimangono utilizzabili su un telefono.

## Scelta delle colonne

Clicca sull'icona dell'ingranaggio sopra l'elenco per aprire la finestra di dialogo **Colonne**. Seleziona o deseleziona una colonna per mostrarla o nasconderla. **Ripristina** ripristina la selezione predefinita per quell'elenco.

Almeno una colonna deve rimanere visibile, quindi l'ultima colonna rimanente non può essere deselezionata.

La tua selezione di colonne viene ricordata per tipo di oggetto e per albero genealogico. È memorizzata nel tuo browser, quindi non è visibile ad altri utenti – ma non ti segue nemmeno su un browser o dispositivo diverso.

## Filtraggio

Clicca sul pulsante **filtra** per aprire il pannello di filtraggio. Un interruttore a pillola nella parte superiore del pannello passa tra due modalità:

- **semplice** – un insieme di filtri predefiniti che dipendono dal tipo di oggetto. Per le persone, ad esempio, puoi filtrare per anno di nascita, anno di morte, varie proprietà della persona, numero di associazioni, tag e se un oggetto è privato o pubblico.
- **GQL** – un singolo campo di testo per una query avanzata nel [Gramps Query Language](gql.md). Digita la query e premi Invio o clicca su **Applica**. Se la query non è valida, il bordo del campo diventa rosso.

I filtri attivi vengono mostrati come chip sopra l'elenco. Rimuovi un singolo filtro cliccando sul pulsante di cancellazione del chip, oppure usa **Rimuovi tutti i filtri** per rimuoverli tutti in una volta.

!!! nota
    Le due modalità sono alternative, non additive: una query GQL sostituisce i filtri semplici, e tornare alla modalità semplice elimina la query.

## Selezionare oggetti e agire su di essi in blocco

Gli utenti con permessi di modifica vedono un pulsante **Seleziona** accanto al pulsante di filtro. Cliccalo per entrare in modalità di selezione, che aggiunge una casella di controllo a ogni riga.

Seleziona gli oggetti che desideri, e appare una barra degli strumenti che mostra quanti sono stati selezionati, insieme a un menu a discesa **Azione** e a un pulsante **Applica**.

### Elimina

Seleziona uno o più oggetti, scegli **Elimina** e clicca su **Applica**. Una finestra di dialogo di conferma ti chiede di confermare, avvisando che l'azione non può essere annullata.

!!! suggerimento
    Le eliminazioni vengono registrate nella [cronologia delle revisioni](revisions.md) come qualsiasi altra modifica, quindi una cancellazione in blocco errata può essere annullata ripristinando la transazione corrispondente.

### Unisci

Seleziona **esattamente due** oggetti, scegli **Unisci** e clicca su **Applica**. Una finestra di dialogo chiede quale dei due dovrebbe fornire i dati principali per l'oggetto unito; clicca su quello che vuoi mantenere come principale. I dati dell'altro oggetto vengono uniti in esso e i riferimenti vengono aggiornati.

L'unione è disponibile per persone, famiglie, eventi, luoghi, fonti e citazioni. Non è disponibile per archivi, note e oggetti multimediali.

Se scegli un'azione senza una selezione valida – ad esempio un'unione con solo un oggetto selezionato – una finestra di dialogo spiega cosa è richiesto.
