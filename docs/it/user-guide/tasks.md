# Usa la gestione delle attività integrata

Gramps Web contiene uno strumento di gestione delle attività genealogiche integrato. È progettato per consentire ai ricercatori di pianificare e dare priorità, ma anche di documentare le loro attività. Questo è il motivo per cui le attività sono rappresentate come fonti nel database di Gramps. Dopo aver completato un'attività, il contenuto associato può servire come fonte che documenta il processo di ricerca.

## Nozioni di base sulle attività

Le attività hanno le seguenti proprietà:

- Stato. Può essere "Aperto", "In Corso", "Bloccato" o "Fatto"
- Priorità. Può essere "Bassa", "Media" o "Alta"
- Tag. Le etichette sono normali tag di Gramps della fonte sottostante. (Nota che tutte le attività hanno anche l'etichetta `ToDo` per identificarle come attività, ma questa etichetta è nascosta nell'elenco delle attività per evitare confusione.)
- Titolo. Mostrato nell'elenco delle attività
- Descrizione. Un campo di testo ricco che può essere utilizzato per descrivere il problema, ma anche per documentare eventuali progressi effettuati
- Media. Qualsiasi file multimediale allegato all'attività

## Crea un'attività

Poiché le attività sono normali oggetti di Gramps, possono essere modificate o create dallo stesso gruppo di utenti che può modificare o creare altri oggetti (come persone o eventi).

Per creare un'attività, fai clic sul pulsante + nella pagina dell'elenco delle attività. Inserisci almeno un titolo e, facoltativamente, una priorità, una descrizione, allegati e tag. Lo stato sarà sempre "Aperto" alla creazione.

## L'elenco delle attività

Per impostazione predefinita, l'elenco delle attività è ordinato per stato – le attività completate per ultime – e all'interno di ciascuno stato per priorità, dalla più alta alla più bassa. Il menu di ordinamento nella barra dei filtri ordina anche per priorità, titolo o ultima modifica (la più recente per prima).

Fai clic su un'attività per aprirla. Gli utenti con permessi di modifica possono anche fare clic sull'icona di stato di un'attività per cambiarne lo stato direttamente nell'elenco, ad esempio per segnarla come completata.

Il pulsante **filtra** sopra l'elenco filtra le attività per titolo, stato, priorità o tag, con un'espressione [GOQL](goql.md), o con il [filtro avanzato](lists.md#advanced-filter). Selezionando più stati o priorità vengono mostrate le attività con uno di essi, ad esempio tutte le attività aperte e bloccate.

## Modifica un'attività

La pagina dell'attività non ha una "modalità di modifica" separata come altri oggetti di Gramps:

- Fai clic sul titolo per modificarlo. Premi Invio, fai clic su ✓, o fai clic altrove per salvare; premi Esc o fai clic su ✕ per annullare.
- Le modifiche allo stato e alla priorità vengono applicate immediatamente.
- Per modificare la descrizione o gli allegati, fai clic sul pulsante di modifica accanto al titolo della sezione. La descrizione viene salvata con il pulsante "salva" sottostante; la modifica degli allegati termina con **Fatto**.
- Il pulsante di blocco imposta se l'attività è privata. La descrizione dell'attività ottiene la stessa privacy.

Gli utenti senza permessi di modifica vedono lo stato e la priorità come testo, e le sezioni senza contenuto sono nascoste.

Sotto il titolo, gli editor vedono altri due pulsanti: **Modifica Fonte** apre la fonte che rappresenta l'attività, dove possono essere modificate le sue altre note, citazioni e attributi. **Elimina** elimina l'attività dopo una conferma e ritorna all'elenco delle attività; il messaggio che appare ha un pulsante di annullamento per ripristinare l'attività.

## Modifica in blocco delle proprietà delle attività

Gli utenti con permessi di modifica vedono una casella di controllo su ciascuna riga dell'elenco delle attività. Seleziona le attività e utilizza **Imposta Priorità** o **Imposta Stato** sopra l'elenco per cambiare tutte le attività selezionate in una sola volta.

## Attività in Gramps Desktop

Quando si aggiungono attività tramite Gramps Web, sia le fonti che le note avranno l'etichetta `ToDo` allegata, quindi le attività appariranno nel [Gramplet Note To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) del desktop così come nel [Rapporto To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Per aggiungere o modificare un'attività in Gramps Desktop, utilizza le seguenti linee guida:

- Aggiungi una fonte con l'etichetta `ToDo` e il titolo dell'attività come titolo
- Facoltativamente, aggiungi una nota alla fonte con l'etichetta `ToDo`, il tipo "To Do" e la descrizione come testo
- Aggiungi un attributo "Stato" e impostalo su "Aperto", "In Corso", "Bloccato" o "Fatto"
- Aggiungi un attributo "Priorità" e impostalo su 9 per bassa, 5 per media o 1 per alta (questi valori controintuitivi sono presi dalla specifica iCalendar)
