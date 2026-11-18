# Tag

I tag sono etichette che possono essere applicate a qualsiasi oggetto nel database di Gramps – persone, famiglie, eventi, luoghi, fonti, citazioni, repository, note e media. Sono utili per raggruppare e filtrare oggetti. I tag sono memorizzati nel database dell'albero genealogico di Gramps e sono condivisi tra tutti gli utenti; sono inoltre completamente compatibili con i tag creati in Gramps Desktop.

## Gestire i tag

I tag sono gestiti dalla sezione **Tag** delle [Impostazioni di Amministrazione](../administration/settings.md#tags), che è disponibile solo per gli utenti con il ruolo di Proprietario o Amministratore. Mostra tutti i tag esistenti e consente di:

- **Creare** un nuovo tag utilizzando il pulsante **Nuovo Tag**
- **Rinominare** un tag utilizzando l'icona di modifica (matita)
- **Cambiare il colore** di un tag utilizzando il selettore di colore
- **Eliminare** un tag utilizzando l'icona di eliminazione

!!! note
    Eliminare un tag lo rimuove da tutti gli oggetti a cui era stato applicato.

## Applicare tag agli oggetti

I tag possono essere applicati o rimossi da un oggetto nella sua pagina di dettaglio quando si è in modalità modifica. Per etichettare molti oggetti contemporaneamente, selezionali in un elenco e utilizza l'azione **Aggiungi Tag** o **Rimuovi Tag**, vedi [Elenco](lists.md#tags-and-privacy).

I tag sono mostrati nella colonna **Tag** degli elenchi, e nei risultati di ricerca, segnalibri e cronologia. Se un elenco non mostra la colonna, abilitala nel selettore di colonne.

## Filtrare per tag

Tutte le [pagine di elenco oggetti](lists.md) (Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Repository, Note, Media) includono un filtro per tag. Usalo per mostrare solo gli oggetti a cui è stato applicato un tag specifico.

## Tag speciali

Due tag hanno un significato speciale in Gramps Web:

- **`Blog`** – qualsiasi fonte contrassegnata con `Blog` è trattata come un post del blog e appare nella vista [Blog](blog.md)
- **`ToDo`** – qualsiasi nota contrassegnata con `ToDo` è trattata come un compito di ricerca e appare nella vista [Compiti](tasks.md)

Questi tag vengono creati automaticamente quando utilizzi per la prima volta le funzionalità Blog o Compiti. Rinominare o eliminare questi tag interromperà la funzionalità corrispondente.
