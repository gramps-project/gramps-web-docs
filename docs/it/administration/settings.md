# Impostazioni di Amministrazione

La pagina **Impostazioni > Amministrazione** è accessibile tramite l'icona utente nella barra superiore dell'app. È disponibile solo per gli utenti con il ruolo di Proprietario o Amministratore e fornisce strumenti per gestire il database dell'albero genealogico.

## Quote di utilizzo

La parte superiore della pagina mostra l'utilizzo attuale rispetto a eventuali limiti configurati:

- **Persone** — il numero di oggetti persona nell'albero rispetto al massimo configurato (∞ se illimitato)
- **Archiviazione media** — dimensione totale dei file multimediali caricati rispetto alla quota di archiviazione configurata (∞ se illimitato)

Le quote sono impostate dall'amministratore del server; vedere [Configurazione del server](../install_setup/configuration.md) per dettagli.

## Importa dati

La sezione di importazione consente di caricare un file dell'albero genealogico o un archivio multimediale. Vedi [Importa dati](import.md) per istruzioni complete.

## Stato dei file multimediali

Questa sezione mostra:

- Il numero totale di oggetti multimediali nell'albero e se alcuni mancano di un checksum
- Il numero di oggetti multimediali il cui file associato è mancante dal server

Un segno di spunta verde indica che tutto è in ordine. Se vengono rilevati problemi, vengono mostrati i collegamenti agli oggetti interessati. I checksum mancanti si verificano tipicamente quando i dati sono stati importati da un formato come GEDCOM che include riferimenti multimediali ma non i file effettivi. I file mancanti possono essere caricati tramite la funzione di importazione dell'archivio multimediale.

## Importa archivio multimediale

Consente di caricare un file ZIP di file multimediali per riempire i file mancanti. Vedi [Importa dati](import.md) per istruzioni complete.

## Gestisci indice di ricerca

Gramps Web mantiene un indice di ricerca a testo completo che viene normalmente aggiornato automaticamente ogni volta che i dati cambiano. L'indicatore di stato mostra quanti oggetti sono attualmente indicizzati rispetto al conteggio totale degli oggetti.

Clicca su **Aggiorna indice di ricerca** per attivare una ricostruzione completa. Un indicatore di progresso viene mostrato mentre il compito viene eseguito in background. Questo è solitamente necessario solo dopo un aggiornamento del server.

### Indice di ricerca semantica

Se il server ha [la ricerca semantica (potenziata da AI) abilitata](../install_setup/configuration.md), appare una sezione aggiuntiva con due azioni:

- **Rigenera indice di ricerca semantica** — ricostruisce l'intero indice semantico da zero. Questo è computazionalmente costoso e può richiedere molto tempo.
- **Aggiorna indice di ricerca semantica** — esegue un aggiornamento incrementale, aggiungendo solo oggetti non ancora indicizzati. Più veloce di una ricostruzione completa.

## Nome dell'albero genealogico

!!! note
    Rinominare l'albero funziona solo in una [configurazione multi-albero](../install_setup/multi-tree.md) o quando `TREE_ID` è esplicitamente impostato nella [configurazione del server](../install_setup/configuration.md). In un'installazione predefinita a albero singolo senza `TREE_ID` impostato, questo genererà un errore.

Questo consente di cambiare il nome del database dell'albero genealogico di Gramps sottostante. Inserisci un nuovo nome e clicca su **Rinomina** per applicare.

## Controlla e Ripara il Database

Questo strumento controlla il database di Gramps per incoerenze interne e ripara quelle che può — analogo allo strumento [Controlla e Ripara il Database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Clicca su **Controlla e Ripara** e attendi che l'indicatore di progresso completi. Il risultato è mostrato sotto il pulsante:

- Se non sono stati trovati errori, viene visualizzato un messaggio di conferma.
- Se sono stati trovati errori, viene mostrato un riepilogo delle correzioni applicate.

Esegui questo strumento se incontri errori o comportamenti imprevisti che potrebbero essere causati da incoerenze nel database, come relazioni mancanti tra oggetti.

## Zona di Pericolo

!!! danger
    Le azioni nella Zona di Pericolo sono **irreversibili**. Fai un backup prima di procedere.

### Elimina tutti gli oggetti

Rimuove oggetti dall'albero genealogico. Cliccando su **Elimina** si apre una finestra di dialogo in cui puoi scegliere di eliminare:

- **Tutti gli oggetti** — cancella completamente l'albero
- **Tipi di oggetti specifici** — ad esempio, solo eventi o solo oggetti multimediali

Ti verrà chiesto di ri-autenticarti (accedere di nuovo) per confermare l'azione. L'eliminazione viene eseguita come un'attività in background e viene mostrato un indicatore di progresso.

!!! warning
    Eliminare solo un sottoinsieme di tipi di oggetti (anziché tutti gli oggetti contemporaneamente) può richiedere molto tempo per alberi di grandi dimensioni, poiché il server deve controllare e aggiornare tutte le relazioni tra gli oggetti.

!!! tip
    Usa questo per ricominciare da capo prima di importare un nuovo albero, o per rimuovere tipi di oggetti specifici che sono stati importati in modo errato.
