# Impostazioni di Amministrazione

La pagina **Impostazioni > Amministrazione** è accessibile tramite l'icona utente nella barra superiore dell'app. È disponibile solo per gli utenti con il ruolo di Proprietario o Amministratore e fornisce strumenti per gestire il database dell'albero genealogico.

La pagina è organizzata in sezioni espandibili. Clicca sull'intestazione di una sezione per espanderla.

## Dati

Copre le quote di utilizzo, l'importazione dei dati e la gestione dei file multimediali.

### Quote di utilizzo

La parte superiore della sezione mostra l'utilizzo attuale rispetto a eventuali limiti configurati:

- **Persone** – il numero di oggetti persona nell'albero rispetto al massimo configurato (∞ se illimitato)
- **Archiviazione multimediale** – dimensione totale dei file multimediali caricati rispetto alla quota di archiviazione configurata (∞ se illimitato)

Le quote sono impostate dall'amministratore del server; vedere [Configurazione del server](../install_setup/configuration.md) per dettagli.

### Importa dati

La sezione di importazione consente di caricare un file dell'albero genealogico o un archivio multimediale. Vedi [Importa dati](import.md) per le istruzioni complete.

### Stato dei file multimediali

Questa sezione mostra:

- Il numero totale di oggetti multimediali nell'albero e se alcuni mancano di un checksum
- Il numero di oggetti multimediali il cui file associato è assente dal server

Un segno di spunta verde indica che tutto è in ordine. Se vengono rilevati problemi, vengono mostrati i collegamenti agli oggetti interessati. I checksum mancanti si verificano tipicamente quando i dati sono stati importati da un formato come GEDCOM che include riferimenti multimediali ma non i file effettivi. I file mancanti possono essere caricati tramite la funzione di importazione dell'archivio multimediale.

### Importa archivio multimediale

Consente di caricare un file ZIP di file multimediali per riempire i file mancanti. Vedi [Importa dati](import.md) per le istruzioni complete.

## Indice di ricerca

### Gestisci indice di ricerca

Gramps Web mantiene un indice di ricerca a testo completo che viene normalmente aggiornato automaticamente ogni volta che i dati cambiano. L'indicatore di stato mostra quanti oggetti sono attualmente indicizzati rispetto al conteggio totale degli oggetti.

Clicca su **Aggiorna indice di ricerca** per attivare una ricostruzione completa. Viene mostrato un indicatore di progresso mentre il compito viene eseguito in background. Questo è solitamente necessario solo dopo un aggiornamento del server.

### Indice di ricerca semantica

Se il server ha [la ricerca semantica (potenziata da AI) abilitata](../install_setup/configuration.md), appare una sezione aggiuntiva con due azioni:

- **Rigenera indice di ricerca semantica** – ricostruisce l'intero indice semantico da zero. Questo è computazionalmente costoso e può richiedere molto tempo.
- **Aggiorna indice di ricerca semantica** – esegue un aggiornamento incrementale, aggiungendo solo oggetti non ancora indicizzati. Più veloce di una ricostruzione completa.

## Impostazioni dell'albero

### Nome dell'albero genealogico

!!! note
    Rinominare l'albero funziona solo in una [configurazione multi-albero](../install_setup/multi-tree.md) o quando `TREE_ID` è esplicitamente impostato nella [configurazione del server](../install_setup/configuration.md). In un'installazione predefinita a singolo albero senza `TREE_ID` impostato, questo genererà un errore.

Questo consente di cambiare il nome del database dell'albero genealogico di Gramps sottostante. Inserisci un nuovo nome e clicca su **Rinomina** per applicare.

!!! tip
    Se desideri solo cambiare il nome mostrato nella barra dell'app senza rinominare il database, utilizza invece l'impostazione [Titolo dell'app](#app-title).

### Informazioni sul ricercatore

Imposta il nome, l'indirizzo e i dettagli di contatto del ricercatore principale. Queste informazioni sono incorporate nelle esportazioni (ad es. file GEDCOM).

## Personalizzazione

### Colori del tema

Imposta un **colore primario** e un **colore di accento** personalizzati per l'interfaccia di Gramps Web. Questi colori vengono applicati a tutti gli utenti di questo albero e hanno effetto immediato dopo il salvataggio.

Utilizza i selettori di colore per scegliere i colori, quindi clicca su **Salva**. Clicca su **Ripristina** per tornare ai valori predefiniti.

### Titolo dell'app

Imposta un titolo personalizzato per l'applicazione. Se impostato, questo sovrascrive il nome dell'albero genealogico nella barra del titolo del browser e nella barra superiore dell'app.

Inserisci un titolo e clicca su **Salva**. Lascia vuoto per utilizzare il predefinito (il nome dell'albero genealogico).

### Nota della home page

Seleziona un oggetto **Nota** di Gramps da visualizzare nella home page del dashboard. Il contenuto della nota è reso sotto le colonne principali del dashboard ed è visibile a tutti gli utenti con accesso all'albero.

Utilizza il selettore di oggetti per cercare e scegliere una nota, quindi salva. Clicca su **Rimuovi** per cancellare la nota attuale della home page.

### Immagine della home page

Seleziona un oggetto **Media** di Gramps da visualizzare come immagine sulla home page del dashboard. Quando combinato con una nota della home page, l'immagine appare accanto al testo della nota. Senza una nota, viene mostrata solo l'immagine.

Utilizza il selettore di oggetti per cercare e scegliere un oggetto multimediale, quindi salva. Clicca su **Rimuovi** per cancellare l'immagine attuale della home page.

### Impostazioni di esportazione/importazione

Le impostazioni a livello di albero (titolo dell'app, colori del tema, nota/imagine della home page, ecc.) possono essere esportate come file JSON per backup o per copiare in un'altra istanza di Gramps Web.

- Clicca su **Esporta impostazioni** per scaricare le impostazioni correnti come file JSON.
- Clicca su **Importa impostazioni dell'albero** per caricare un file JSON precedentemente esportato e applicare le impostazioni.

## Elaborazione dell'albero genealogico

### Controlla e ripara il database

Questo strumento controlla il database di Gramps per incoerenze interne e ripara quelle che può – analogo allo strumento [Controlla e ripara il database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Clicca su **Controlla e ripara** e attendi che l'indicatore di progresso completi. Il risultato è mostrato sotto il pulsante:

- Se non sono stati trovati errori, viene visualizzato un messaggio di conferma.
- Se sono stati trovati errori, viene mostrato un riepilogo delle correzioni applicate.

Esegui questo strumento se incontri errori o comportamenti imprevisti che potrebbero essere causati da incoerenze del database, come relazioni mancanti tra oggetti.

## Tag

### Gestisci tag

Crea, rinomina, cambia colore ed elimina [tag](../user-guide/tags.md) per l'albero genealogico. I tag sono memorizzati nel database di Gramps, condivisi tra tutti gli utenti e completamente compatibili con Gramps Desktop.

Clicca su **Nuovo Tag** per creare un tag. Utilizza i controlli accanto a un tag esistente per rinominarlo (icona della matita), cambiare il suo colore (selettore di colore) o eliminarlo (icona di eliminazione).

!!! note
    Eliminare un tag lo rimuove da tutti gli oggetti a cui era stato applicato.

Vedi [Tag](../user-guide/tags.md) per come i tag vengono utilizzati in tutto Gramps Web, inclusi i tag speciali `Blog` e `ToDo`.

## Zona di pericolo

!!! danger
    Le azioni nella Zona di pericolo sono **irreversibili**. Fai un backup prima di procedere.

### Elimina tutti gli oggetti

Rimuove oggetti dall'albero genealogico. Cliccando su **Elimina** si apre una finestra di dialogo in cui puoi scegliere di eliminare:

- **Tutti gli oggetti** – cancella completamente l'albero
- **Tipi di oggetti specifici** – ad esempio, solo eventi o solo oggetti multimediali

Ti verrà chiesto di riautenticarti (accedere di nuovo) per confermare l'azione. L'eliminazione viene eseguita come un'attività in background e viene mostrato un indicatore di progresso.

!!! warning
    Eliminare solo un sottoinsieme di tipi di oggetti (anziché tutti gli oggetti in una volta) può richiedere molto tempo per alberi di grandi dimensioni, poiché il server deve controllare e aggiornare tutte le relazioni tra gli oggetti.

!!! tip
    Utilizza questo per partire da zero prima di importare un nuovo albero, o per rimuovere tipi di oggetti specifici che sono stati importati in modo errato.

### Ripristina da Backup

Ripristina l'albero per corrispondere a un file di backup XML di Gramps (`.gramps`) caricato, aggiungendo, aggiornando ed eliminando oggetti secondo necessità affinché l'albero risulti identico al backup.

!!! danger
    Questo è un sostituzione distruttiva, non una fusione. Qualsiasi oggetto esistente non presente nel backup caricato viene eliminato.

Carica un file `.gramps`, quindi clicca su **Anteprima Ripristino**. Ti verrà chiesto di riautenticarti se la tua sessione non è abbastanza fresca. Un'anteprima viene eseguita come un'attività in background e, una volta completata, apre una finestra di dialogo che riassume le modifiche per tipo di oggetto (persone, famiglie, eventi, luoghi, citazioni, fonti, archivi, oggetti multimediali, note, tag):

- **Aggiungi** – oggetti presenti nel backup ma mancanti dall'albero attuale
- **Aggiorna** – oggetti presenti in entrambi che differiscono
- **Elimina** – oggetti nell'albero attuale che sono assenti dal backup
- **Invariato** – oggetti identici in entrambi

Se alcuni oggetti verrebbero eliminati, la finestra di dialogo avvisa quanti. Rivedi il riepilogo, quindi clicca su **Ripristina** per applicare le modifiche, o **Annulla** per abortire.

!!! note
    Solo i dati degli oggetti e i riferimenti multimediali vengono ripristinati. I file multimediali binari stessi e i metadati dell'albero (persona predefinita, segnalibri, gruppi di nomi) non sono interessati. Ripristina i file multimediali mancanti separatamente tramite [Importa archivio multimediale](#import-media-archive) se necessario.

!!! tip
    Utilizza questo per ripristinare un albero a un backup XML di Gramps noto e buono, ad esempio dopo un'importazione errata o una modifica di massa indesiderata.
