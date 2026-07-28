## Prepara il tuo database Gramps

Se stai utilizzando Gramps Desktop, ci sono due passaggi per preparare il tuo database per assicurarti che tutto funzioni senza problemi in seguito. Se stai migrando da un altro programma di genealogia, puoi saltare questo passaggio.

1. Controlla e ripara il database
    - Facoltativo: crea un backup del database esportando in Gramps XML
    - Esegui lo [Strumento di controllo e riparazione del database](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Questo risolve alcune incoerenze interne che potrebbero causare problemi in Gramps Web.
2. Converti i percorsi multimediali in relativi
    - Usa il Gestore multimediale di Gramps per [convertire tutti i percorsi multimediali da assoluti a relativi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Nota che anche con percorsi relativi, eventuali file multimediali al di fuori della tua directory multimediale di Gramps non funzioneranno correttamente quando sincronizzati con Gramps Web.

## Importa dati genealogici

Per importare un albero genealogico esistente, utilizza la pagina "Importa" e carica un file in uno dei formati supportati da Gramps &ndash; vedi [Importa da un altro programma di genealogia](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) nella Wiki di Gramps.

Se utilizzi già Gramps Desktop, è fortemente consigliato utilizzare il formato Gramps XML (`.gramps`) per garantire che i tuoi alberi online e offline utilizzino gli stessi identificatori e possano essere [sincronizzati](sync.md).

Dopo aver cliccato su "Importa", il file viene prima analizzato e una finestra di dialogo "Conferma importazione" mostra un'anteprima degli oggetti contenuti nel file (persone, famiglie, eventi, luoghi, ecc.) prima che venga aggiunto qualcosa al tuo albero. Controlla i conteggi, quindi clicca su "Importa" nella finestra di dialogo per procedere, o "Annulla" per abortire senza modificare nulla.

!!! warning
    Un'importazione regolare è puramente additiva: crea sempre nuovi oggetti e non aggiorna né elimina quelli esistenti, anche per oggetti che esistono già nel tuo albero sotto lo stesso ID Gramps o handle. Importare lo stesso file due volte &ndash; o importare un file che si sovrappone ai dati già presenti nell'albero &ndash; duplicherà ogni oggetto corrispondente piuttosto che fonderlo o saltarlo.

    Se hai bisogno di apportare modifiche fatte altrove a un albero già importato, utilizza invece [Ripristina da backup](settings.md#restore-from-backup), che sostituisce l'albero per corrispondere al file caricato piuttosto che aggiungervi.

## Perché non c'è supporto per il pacchetto Gramps XML?

Sebbene Gramps XML (`.gramps`) sia il formato preferito per l'importazione dei dati, il pacchetto Gramps XML (`.gpkg`) non è supportato da Gramps Web. Questo perché le routine di importazione ed esportazione per i file multimediali non sono adatte per l'uso su un server web.

Per importare i file multimediali appartenenti a un file `.gramps` importato, vedi la sezione successiva.

## Importa file multimediali

Se hai caricato un albero genealogico e hai bisogno di caricare i file multimediali corrispondenti, puoi utilizzare il pulsante "importa archivio multimediale" nella pagina "Importa".

Si aspetta un file ZIP con i file multimediali mancanti all'interno. La struttura delle cartelle nel file ZIP non deve essere la stessa della struttura delle cartelle all'interno della cartella multimediale di Gramps poiché i file vengono abbinati agli oggetti multimediali tramite il loro checksum.

Nota che questa funzionalità funziona solo per i file che hanno il checksum corretto nel database di Gramps (che dovrebbe essere garantito eseguendo lo strumento di controllo e riparazione nel primo passaggio).

Quando si passa a Gramps Web da un altro programma di genealogia che include file multimediali, è consigliato prima importare tutto in Gramps Desktop, che ha più opzioni per associare file multimediali esistenti a un albero importato.
