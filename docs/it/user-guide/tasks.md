# Usa la gestione delle attività integrata

Gramps Web contiene uno strumento di gestione delle attività genealogiche integrato. È progettato per consentire ai ricercatori di pianificare e dare priorità, ma anche di documentare le loro attività. Questo è il motivo per cui le attività sono rappresentate come fonti nel database di Gramps. Dopo aver completato un'attività, il contenuto associato può servire come fonte per documentare il processo di ricerca.

## Nozioni di base sulle attività

Le attività hanno le seguenti proprietà:

- Stato. Può essere "Aperto", "In Corso", "Bloccato" o "Fatto"
- Priorità. Può essere "Bassa", "Media" o "Alta"
- Tag. Le etichette sono normali tag di Gramps della fonte sottostante. (Nota che tutte le attività hanno inoltre l'etichetta `ToDo` per identificarle come attività, ma questa etichetta è nascosta nell'elenco delle attività per evitare ingombri.)
- Titolo. Mostrato nell'elenco delle attività
- Descrizione. Un campo di testo arricchito che può essere utilizzato per descrivere il problema, ma anche per documentare eventuali progressi effettuati
- Media. Qualsiasi file multimediale allegato all'attività

## Crea un'attività

Poiché le attività sono normali oggetti di Gramps, possono essere modificate o create dallo stesso gruppo di utenti che può modificare o creare altri oggetti (come persone o eventi).

Per creare un'attività, fai clic sul pulsante + nella pagina dell'elenco delle attività. Inserisci almeno un titolo. Lo stato sarà sempre "Aperto" alla creazione.

## Modifica un'attività

Per modificare i dettagli di un'attività, fai clic su di essa nell'elenco delle attività.

La pagina dei dettagli dell'attività non ha una "modalità di modifica" separata come altri oggetti di Gramps. Le modifiche al titolo, allo stato e alla priorità vengono applicate immediatamente. Le modifiche alla descrizione in formato testo arricchito richiedono di fare clic sul pulsante "salva" sotto di essa.

## Modifica in blocco delle proprietà delle attività

La priorità e lo stato delle attività possono essere modificati in blocco utilizzando le caselle di controllo nell'elenco delle attività per la selezione e i pulsanti appropriati sopra l'elenco delle attività.

## Attività in Gramps Desktop

Quando si aggiungono attività tramite Gramps Web, sia le fonti che le note avranno l'etichetta `ToDo` allegata, quindi le attività appariranno nel [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) del desktop così come nel [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Per aggiungere o modificare un'attività in Gramps Desktop, utilizza le seguenti linee guida

- Aggiungi una fonte con tag `ToDo` e il titolo dell'attività come titolo
- Facoltativamente, aggiungi una nota alla fonte con tag `ToDo`, tipo "To Do" e la descrizione come testo
- Aggiungi un attributo "Stato" e impostalo su "Aperto", "In Corso", "Bloccato" o "Fatto"
- Aggiungi un attributo "Priorità" e impostalo su 9 per bassa, 5 per media o 1 per alta (questi valori controintuitivi sono presi dalla specifica iCalendar)
