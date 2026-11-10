# Utilizzare la gestione delle attività integrata

Gramps Web contiene uno strumento di gestione delle attività genealogiche integrato. È progettato per consentire ai ricercatori di pianificare e dare priorità, ma anche documentare le loro attività. Ecco perché le attività sono rappresentate come fonti nel database di Gramps. Dopo aver completato un'attività, il contenuto associato può servire come fonte per documentare il processo di ricerca.

## Nozioni di base sulle attività

Le attività hanno le seguenti proprietà:

- Stato. Questo può essere "Aperto", "In Corso", "Bloccato" o "Fatto"
- Priorità. Questo può essere "Bassa", "Media" o "Alta"
- Etichette. Le etichette sono normali etichette di Gramps della fonte sottostante. (Si noti che tutte le attività hanno inoltre l'etichetta `ToDo` per identificarle come attività, ma questa etichetta è nascosta nell'elenco delle attività per evitare ingombri.)
- Titolo. Mostrato nell'elenco delle attività
- Descrizione. Un campo di testo arricchito che può essere utilizzato per descrivere il problema, ma anche per documentare eventuali progressi effettuati
- Media. Qualsiasi file multimediale allegato all'attività

## Creare un'attività

Poiché le attività sono oggetti normali di Gramps, possono essere modificate o create dallo stesso gruppo di utenti che può modificare o creare altri oggetti (come persone o eventi).

Per creare un'attività, fare clic sul pulsante + nella pagina dell'elenco delle attività. Inserire almeno un titolo e, facoltativamente, una priorità, una descrizione, allegati e etichette. Lo stato sarà sempre "Aperto" alla creazione.

## L'elenco delle attività

L'elenco delle attività è ordinato per stato – le attività completate per ultime – e all'interno di ciascuno stato per priorità, dalla più alta alla più bassa.

Fare clic su un'attività per aprirla. Gli utenti con permessi di modifica possono anche fare clic sull'icona di stato di un'attività per cambiare il suo stato direttamente nell'elenco, ad esempio per contrassegnarla come completata.

Il pulsante **filtra** sopra l'elenco filtra le attività per etichetta, con un'espressione [GOQL](goql.md) o con il [filtro avanzato](lists.md#advanced-filter).

## Modificare un'attività

La pagina dell'attività non ha una "modalità di modifica" separata come altri oggetti di Gramps:

- Fare clic sul titolo per modificarlo. Premere Invio, fare clic su ✓ o fare clic altrove per salvare; premere Esc o fare clic su ✕ per annullare.
- Le modifiche allo stato e alla priorità vengono applicate immediatamente.
- Per modificare la descrizione o gli allegati, fare clic sul pulsante di modifica accanto al titolo della sezione. La descrizione viene salvata con il pulsante "salva" sotto di essa; la modifica degli allegati termina con **Fatto**.
- Il pulsante di blocco imposta se l'attività è privata. La descrizione dell'attività riceve la stessa privacy.

Gli utenti senza permessi di modifica vedono lo stato e la priorità come testo, e le sezioni senza contenuto sono nascoste.

Sotto il titolo, gli editor vedono due ulteriori pulsanti: **Modifica Fonte** apre la fonte che rappresenta l'attività, dove possono essere modificate altre note, citazioni e attributi. **Elimina** elimina l'attività dopo una conferma e torna all'elenco delle attività; il messaggio che appare ha un pulsante di annullamento per ripristinare l'attività.

## Modifica massiva delle proprietà delle attività

Gli utenti con permessi di modifica vedono una casella di controllo su ciascuna riga dell'elenco delle attività. Selezionare le attività e utilizzare **Imposta Priorità** o **Imposta Stato** sopra l'elenco per cambiare tutte le attività selezionate contemporaneamente.

## Attività in Gramps Desktop

Quando si aggiungono attività tramite Gramps Web, sia le fonti che le note avranno l'etichetta `ToDo` allegata, quindi le attività appariranno nel [Gramplet Note To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) del desktop così come nel [Rapporto To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Per aggiungere o modificare un'attività in Gramps Desktop, utilizzare le seguenti linee guida

- Aggiungere una fonte con etichetta `ToDo` e il titolo dell'attività come titolo
- Facoltativamente, aggiungere una nota alla fonte con etichetta `ToDo`, tipo "To Do", e la descrizione come testo
- Aggiungere un attributo "Stato" e impostarlo su "Aperto", "In Corso", "Bloccato" o "Fatto"
- Aggiungere un attributo "Priorità" e impostarlo su 9 per bassa, 5 per media o 1 per alta (questi valori controintuitivi sono presi dalla specifica iCalendar)
