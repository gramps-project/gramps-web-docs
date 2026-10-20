# Impostazioni di Amministrazione

La pagina **Impostazioni > Amministrazione** è accessibile tramite l'icona utente nella barra superiore dell'app. È disponibile solo per gli utenti con il ruolo di Proprietario o Amministratore e fornisce strumenti per gestire il database dell'albero genealogico.

La pagina è organizzata in sezioni espandibili. Clicca su un'intestazione di sezione per espanderla.

## Dati

Copre le quote di utilizzo, l'importazione dei dati e la gestione dei file multimediali.

### Quote di utilizzo

La parte superiore della sezione mostra l'utilizzo attuale rispetto a eventuali limiti configurati:

- **Persone** – il numero di oggetti persona nell'albero rispetto al massimo configurato (∞ se illimitato)
- **Archiviazione multimediale** – dimensione totale dei file multimediali caricati rispetto alla quota di archiviazione configurata (∞ se illimitato)

Le quote sono impostate dall'amministratore del server; vedere [Configurazione del server](../install_setup/configuration.md) per dettagli.

### Importa dati

La sezione di importazione consente di caricare un file dell'albero genealogico o un archivio multimediale. Vedi [Importa dati](import.md) per istruzioni complete.

### Stato dei file multimediali

Questa sezione mostra:

- Il numero totale di oggetti multimediali nell'albero e se alcuni mancano di un checksum
- Il numero di oggetti multimediali il cui file associato è mancante dal server

Un segno di spunta verde indica che tutto è in ordine. Se vengono rilevati problemi, vengono mostrati i collegamenti agli oggetti interessati. I checksum mancanti si verificano tipicamente quando i dati sono stati importati da un formato come GEDCOM che include riferimenti multimediali ma non i file effettivi. I file mancanti possono essere caricati tramite la funzione di importazione dell'archivio multimediale.

### Importa archivio multimediale

Consente di caricare un file ZIP di file multimediali per riempire i file mancanti. Vedi [Importa dati](import.md) per istruzioni complete.

## Indice di ricerca

### Gestisci indice di ricerca

Gramps Web mantiene un indice di ricerca a testo completo che viene normalmente aggiornato automaticamente ogni volta che i dati cambiano. L'indicatore di stato mostra quanti oggetti sono attualmente indicizzati rispetto al conteggio totale degli oggetti.

Clicca su **Aggiorna indice di ricerca** per attivare una ricostruzione completa. Un indicatore di progresso viene mostrato mentre il compito viene eseguito in background. Questo è solitamente necessario solo dopo un aggiornamento del server.

### Indice di ricerca semantica

!!! warning "Deprecato"
    La ricerca semantica è deprecata e verrà rimossa nell'API Gramps Web 3.25, insieme a questa sezione. La chat AI non ne ha bisogno poiché l'API Gramps Web 3.24.

Se il server ha [abilitata la ricerca semantica (basata su AI)](../install_setup/chat.md#semantic-search-deprecated), appare una sezione aggiuntiva con due azioni:

- **Rigenera indice di ricerca semantica** – ricostruisce l'intero indice semantico da zero. Questo è computazionalmente costoso e può richiedere molto tempo.
- **Aggiorna indice di ricerca semantica** – esegue un aggiornamento incrementale, aggiungendo solo oggetti non ancora indicizzati. Più veloce di una ricostruzione completa.

## Impostazioni dell'albero

### Nome dell'albero genealogico

!!! note
    Rinominare l'albero funziona solo in una [configurazione multi-albero](../install_setup/multi-tree.md) o quando `TREE_ID` è esplicitamente impostato nella [configurazione del server](../install_setup/configuration.md). In un'installazione predefinita a singolo albero senza `TREE_ID` impostato, questo genererà un errore.

Questo consente di cambiare il nome del database dell'albero genealogico Gramps sottostante. Inserisci un nuovo nome e clicca su **Rinomina** per applicare.

!!! tip
    Se desideri solo cambiare il nome mostrato nella barra dell'app senza rinominare il database, utilizza invece l'impostazione [Titolo dell'app](#app-title).

### Informazioni sul Ricercatore

Imposta il nome, l'indirizzo e i dettagli di contatto del ricercatore principale. Queste informazioni sono incorporate nelle esportazioni (ad es. file GEDCOM).

## Personalizzazione

### Colori del tema

Imposta un **colore primario** e un **colore di accento** personalizzati per l'interfaccia di Gramps Web. Questi colori vengono applicati a tutti gli utenti di questo albero e hanno effetto immediato dopo il salvataggio.

Utilizza i selettori di colore per scegliere i colori, quindi clicca su **Salva**. Clicca su **Ripristina** per tornare ai valori predefiniti.

### Titolo dell'app

Imposta un titolo personalizzato per l'applicazione. Se impostato, questo sovrascrive il nome dell'albero genealogico nella barra del titolo del browser e nella barra superiore dell'app.

Inserisci un titolo e clicca su **Salva**. Lascia vuoto per utilizzare il predefinito (il nome dell'albero genealogico).

### Nota della home page

Seleziona un oggetto **Nota** di Gramps da visualizzare nella home page del dashboard. Il contenuto della nota viene visualizzato sotto le colonne principali del dashboard ed è visibile a tutti gli utenti con accesso all'albero.

Utilizza il selettore di oggetti per cercare e scegliere una nota, quindi salva. Clicca su **Rimuovi** per cancellare la nota attuale della home page.

### Immagine della home page

Seleziona un oggetto **Media** di Gramps da visualizzare come immagine nella home page del dashboard. Quando combinata con una nota della home page, l'immagine appare accanto al testo della nota. Senza una nota, viene mostrata solo l'immagine.

Utilizza il selettore di oggetti per cercare e scegliere un oggetto multimediale, quindi salva. Clicca su **Rimuovi** per cancellare l'immagine attuale della home page.

### Impostazioni di esportazione/importazione

Le impostazioni a livello di albero (titolo dell'app, colori del tema, nota/imagine della home page, ecc.) possono essere esportate come file JSON per backup o per copiare in un'altra istanza di Gramps Web.

- Clicca su **Esporta impostazioni** per scaricare le impostazioni attuali come file JSON.
- Clicca su **Importa impostazioni dell'albero** per caricare un file JSON precedentemente esportato e applicare le impostazioni.

## Elaborazione dell'albero genealogico

### Controlla e Ripara il Database

Questo strumento controlla il database di Gramps per incoerenze interne e ripara quelle che può – analogo allo [Strumento Controlla e Ripara Database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Clicca su **Controlla e Ripara** e attendi che l'indicatore di progresso completi. Il risultato viene mostrato sotto il pulsante:

- Se non sono stati trovati errori, viene visualizzato un messaggio di conferma.
- Se sono stati trovati errori, viene mostrato un riepilogo delle correzioni applicate.

Esegui questo strumento se incontri errori o comportamenti imprevisti che potrebbero essere causati da incoerenze nel database, come relazioni mancanti tra oggetti.

### Verifica i Dati

Mentre [Controlla e Ripara Database](#check-and-repair-database) cerca incoerenze *tecniche*, questo strumento cerca dati *implausibili* – analogo allo [Strumento Verifica i Dati](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Riporta cose che non sono impossibili ma sono abbastanza improbabili da meritare un secondo sguardo, come una madre di 12 anni o una persona che ha vissuto fino a 130 anni.

Sotto **Opzioni** puoi regolare le soglie utilizzate dai test – età massima, età minima e massima per sposarsi o avere figli, numero massimo di figli, e così via – così come se stimare date mancanti o imprecise e se segnalare date non valide come il 31 febbraio.

Clicca su **Verifica i Dati** per iniziare. Il controllo viene eseguito come un'attività in background, e i risultati vengono quindi elencati sotto **Risultati della Verifica dei Dati**. Questo strumento non modifica nulla: riporta solo ciò che trova.

!!! note
    Un risultato non è prova di un errore. Vite lunghe e ampie differenze di età si verificano, quindi tratta i risultati come un elenco di cose da controllare piuttosto che come un elenco di cose da correggere.

## Tag

### Gestisci tag

Crea, rinomina, cambia colore e elimina [tag](../user-guide/tags.md) per l'albero genealogico. I tag sono memorizzati nel database di Gramps, condivisi tra tutti gli utenti e completamente compatibili con Gramps Desktop.

Clicca su **Nuovo Tag** per creare un tag. Utilizza i controlli accanto a un tag esistente per rinominarlo (icona della matita), cambiare il suo colore (selettore di colore) o eliminarlo (icona di eliminazione).

!!! note
    Eliminare un tag lo rimuove da tutti gli oggetti a cui è stato applicato.

Vedi [Tag](../user-guide/tags.md) per come i tag vengono utilizzati in tutto Gramps Web, inclusi i tag speciali `Blog` e `ToDo`.

## Backup

Un backup contiene i dati dell'albero genealogico, inclusi i record privati, le impostazioni dell'albero e gli utenti dell'albero. I file multimediali non sono inclusi; vedere [Esegui il backup dei tuoi file multimediali](export.md#back-up-your-media-files).

### Backup memorizzati

Se l'amministratore del server ha impostato una directory di backup (`BACKUP_DIR`, vedere [Configurazione del server](../install_setup/configuration.md)), i backup possono essere memorizzati sul server. Altrimenti, la sezione mostra un avviso che la memorizzazione dei backup non è configurata e solo il ripristino da un file caricato è disponibile.

Clicca su **Crea Backup...** per creare un backup. Viene creato come un'attività in background e poi appare nell'elenco dei backup memorizzati, con la sua data, il numero di persone e la sua dimensione. Il server conserva solo i backup più recenti (cinque per impostazione predefinita) e elimina automaticamente quelli più vecchi. Anche il numero di backup che possono essere creati al giorno è limitato.

Per ogni backup memorizzato, puoi:

- **Scaricarlo** come file `.tar`, ad esempio per conservare una copia altrove.
- **Ripristinarlo**, come descritto di seguito.
- **Elimarlo**, dopo aver confermato.

Un backup effettuato con una versione più recente di Gramps Web rispetto a quella in esecuzione sul server è contrassegnato con un'icona di avviso e non può essere ripristinato.

### Ripristina da Backup

Ripristina l'albero da un backup memorizzato o da un file caricato. Per ripristinare un backup memorizzato, clicca sul pulsante di ripristino accanto ad esso. Per ripristinare da un file, seleziona un backup di Gramps Web (`.tar`) o un file XML di Gramps (`.gramps`) e clicca su **Ripristina**.

!!! danger
    Ripristinare i dati è una sostituzione distruttiva, non una fusione. Qualsiasi oggetto esistente non presente nel backup viene eliminato.

Per un backup di Gramps Web, viene mostrata una finestra di dialogo che indica quando è stato effettuato il backup, per quale albero e con quale versione, e ti consente di scegliere quali parti ripristinare:

- **Dati** – gli oggetti dell'albero genealogico
- **Impostazioni dell'albero** – le impostazioni di questa pagina, come colori del tema, titolo dell'app e nota della home page
- **Utenti** – gli utenti dell'albero

Clicca su **Anteprima** per vedere cosa cambierebbe il ripristino. Un file XML di Gramps contiene solo dati, quindi per tale file l'anteprima inizia immediatamente. Ti verrà chiesto di ri-autenticarti se la tua sessione non è abbastanza fresca. L'anteprima viene eseguita come un'attività in background e, una volta completata, apre una finestra di dialogo che riassume le modifiche per tipo di oggetto (persone, famiglie, eventi, luoghi, citazioni, fonti, archivi, oggetti multimediali, note, tag), e per le impostazioni dell'albero e gli utenti se selezionati:

- **Aggiungi** – oggetti presenti nel backup ma assenti nell'albero corrente
- **Aggiorna** – oggetti presenti in entrambi che differiscono
- **Elimina** – oggetti nell'albero corrente che sono assenti dal backup
- **Invariato** – oggetti identici in entrambi

Se alcuni oggetti verrebbero eliminati, la finestra di dialogo avverte quanti. Rivedi il riepilogo, quindi clicca su **Ripristina** per applicare le modifiche, o **Annulla** per abortire.

Dopo il ripristino, gli utenti che sono stati aggiunti dal backup vengono elencati. Ricevono una password casuale, quindi devono reimpostare la loro password prima di poter accedere. Gli utenti che esistono già sul server non vengono mai modificati. Gli oggetti multimediali i cui file sono mancanti sul server vengono elencati; caricali tramite [Importa archivio multimediale](#import-media-archive).

!!! note
    Ripristinare i dati ripristina solo i dati degli oggetti e i riferimenti multimediali. I file multimediali binari stessi e i metadati dell'albero (persona predefinita, segnalibri, gruppi di nomi) non sono interessati.

!!! tip
    Utilizza questo per tornare a un backup noto e valido, ad esempio dopo un'importazione errata o una modifica di massa indesiderata.

## Zona di Pericolo

!!! danger
    Le azioni nella Zona di Pericolo sono **irreversibili**. Fai un [backup](#backups) prima di procedere.

### Elimina tutti gli oggetti

Rimuove oggetti dall'albero genealogico. Cliccando su **Elimina** si apre una finestra di dialogo in cui puoi scegliere di eliminare:

- **Tutti gli oggetti** – cancella completamente l'albero
- **Tipi di oggetti specifici** – ad esempio, solo eventi o solo oggetti multimediali

Ti verrà chiesto di ri-autenticarti (accedere di nuovo) per confermare l'azione. L'eliminazione viene eseguita come un'attività in background e viene mostrato un indicatore di progresso.

!!! warning
    Eliminare solo un sottoinsieme di tipi di oggetti (anziché tutti gli oggetti in una volta) può richiedere molto tempo per alberi grandi, poiché il server deve controllare e aggiornare tutte le relazioni tra gli oggetti.

!!! tip
    Utilizza questo per ricominciare da capo prima di importare un nuovo albero, o per rimuovere tipi di oggetti specifici che sono stati importati in modo errato.
