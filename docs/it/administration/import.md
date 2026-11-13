# Importa dati

Puoi importare un albero genealogico esistente in Gramps Web caricando un file esportato da un altro programma genealogico, da un servizio online o da Gramps Desktop.

L'importazione si trova nella sezione **Dati** delle [Impostazioni di amministrazione](settings.md) (icona utente nella barra superiore dell'app ▸ Amministrazione), disponibile per i proprietari dell'albero e gli amministratori. Quando l'albero è ancora vuoto, il pulsante **Importa Albero Genealogico** nella scheda "Inizia" della homepage porta anche lì.

## Quale file utilizzare

| Proveniente da | Esporta il tuo albero come | Estensione del file |
|---|---|---|
| Un altro programma genealogico o servizio online | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Un foglio di calcolo | Gramps CSV | `.csv` |
| Un rubrica | vCard | `.vcf` |

GEDCOM è il formato di scambio comune che quasi tutti i programmi genealogici e i servizi online possono esportare. Cerca un'opzione "Esporta" o "Scarica" nel tuo programma o sul sito web, e scegli GEDCOM se ti vengono offerti diversi formati. La pagina Wiki di Gramps [Importa da un altro programma genealogico](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) ha note su programmi specifici.

Se utilizzi Gramps Desktop, scegli Gramps XML (`.gramps`) piuttosto che GEDCOM. Questo formato conserva tutti i dati di Gramps senza perdita, e i tuoi alberi online e offline mantengono gli stessi identificatori, così possono essere [synchronizzati](sync.md). Vedi [Proveniente da Gramps Desktop](#coming-from-gramps-desktop) qui sotto.

## Importa un file di albero genealogico

1. Apri la sezione **Dati** delle impostazioni di amministrazione.
2. Sotto "Importa Albero Genealogico", scegli il tuo file e clicca su **Importa**.
3. Il file viene prima analizzato e viene visualizzata una finestra di dialogo "Conferma Importazione" che mostra quanti oggetti contiene (persone, famiglie, eventi, luoghi, ecc.). Nulla è stato ancora aggiunto al tuo albero. Controlla che i conteggi sembrino plausibili, quindi clicca su **Importa** per procedere, oppure su **Annulla** per abortire senza modificare nulla.
4. L'importazione avviene in background e viene mostrato un indicatore di avanzamento. Una volta importati i dati, l'indice di ricerca viene aggiornato, il che può richiedere un po' di tempo per un albero grande. Se l'importazione fallisce, viene mostrato il motivo.

Quando l'importazione è terminata, controlla il risultato: confronta il numero di persone nel pannello **Statistiche** sulla homepage con il numero nel tuo vecchio programma, e apri una famiglia che conosci bene per vedere che genitori, figli, date e luoghi siano stati trasferiti come previsto.

!!! warning
    Un'importazione regolare è puramente additiva: crea sempre nuovi oggetti e non aggiorna o elimina mai quelli esistenti, anche per oggetti che già esistono nel tuo albero sotto lo stesso ID o handle di Gramps. Importare lo stesso file due volte – o importare un file che si sovrappone ai dati già presenti nell'albero – duplicherà ogni oggetto corrispondente piuttosto che fonderlo o saltarlo.

    Se hai bisogno di portare modifiche apportate altrove a un albero già importato, utilizza invece [Ripristina da Backup](settings.md#restore-from-backup), che sostituisce l'albero per corrispondere al file caricato piuttosto che aggiungerlo. Questo richiede un file Gramps XML o un backup di Gramps Web.

Se è stato impostato un limite sul numero di persone per il tuo albero (vedi [Quote di utilizzo](settings.md#usage-quotas)), un'importazione che lo supererebbe viene rifiutata nella sua interezza.

## File GEDCOM

Possono essere importati sia file GEDCOM 5.5.1 che GEDCOM 7. Ci sono alcune cose da tenere a mente.

### Codifica dei caratteri

Un file GEDCOM 5.5.1 dichiara la sua codifica dei caratteri nell'intestazione. Sono supportate le codifiche UTF-8, UTF-16, ANSEL e Windows (ANSI). Se i nomi con accenti o altri caratteri speciali appaiono distorti dopo l'importazione (ad esempio `MÃ¼ller` invece di `Müller`), è probabile che il file sia stato esportato con una codifica diversa da quella dichiarata. Esporta nuovamente il file dal tuo vecchio programma, scegliendo UTF-8 se ti viene data la scelta, e [ricomincia](#starting-over).

I file GEDCOM 7 devono sempre essere codificati come UTF-8; altri file vengono rifiutati con un errore "File GEDCOM non valido".

### Dati specifici del programma

Molti programmi aggiungono le proprie estensioni a GEDCOM che altri programmi non comprendono. Gramps non scarta silenziosamente tali dati: le righe che non può interpretare vengono raccolte in una nota di tipo "importazione GEDCOM", allegata alla persona, famiglia o altro oggetto a cui appartengono. Controlla queste note per vedere se qualcosa di importante non è stato trasferito.

### File multimediali

Un file GEDCOM contiene riferimenti a file multimediali (come foto o documenti scansionati), ma non i file stessi. Dopo l'importazione, gli oggetti multimediali esistono nel tuo albero, ma i loro file mancano, il che è mostrato sotto [Stato dei file multimediali](settings.md#media-file-status). Per aggiungere i file, vedi [Importa file multimediali](import-media.md).

## Proveniente da Gramps Desktop

Se stai utilizzando Gramps Desktop, ci sono due passaggi per preparare il tuo database per assicurarti che tutto funzioni senza problemi in seguito.

1. Controlla e ripara il database
    - Facoltativo: crea un backup del database esportando in Gramps XML
    - Esegui lo [Strumento di controllo e riparazione del database](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Questo risolve alcune incoerenze interne che potrebbero causare problemi in Gramps Web.
2. Converti i percorsi multimediali in relativi
    - Usa il Gestore Multimediale di Gramps per [convertire tutti i percorsi multimediali da assoluti a relativi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Nota che anche con percorsi relativi, eventuali file multimediali al di fuori della tua directory multimediale di Gramps non funzioneranno correttamente quando sincronizzati con Gramps Web.

Poi esporta il tuo albero in Gramps XML (`.gramps`), importalo come descritto sopra, e [carica i tuoi file multimediali](import-media.md). Per continuare a lavorare sullo stesso albero sul tuo computer e sul web, utilizza il [complemento di sincronizzazione Gramps Web](sync.md).

### Perché non supportare il pacchetto Gramps XML?

Sebbene Gramps XML (`.gramps`) sia il formato preferito per importare dati, il pacchetto Gramps XML (`.gpkg`) non è supportato da Gramps Web. Questo perché le routine di importazione ed esportazione per i file multimediali non sono adatte per l'uso su un server web.

## Problemi comuni

**"Formato non supportato".** Solo le estensioni di file elencate [sopra](#which-file-to-use) possono essere importate. Se il tuo programma o servizio online ti ha fornito un archivio ZIP, decomprimilo e carica il file `.ged` all'interno.

**Tutto appare due volte.** Lo stesso file è stato importato due volte. Poiché le importazioni non si fondono mai, [ricomincia](#starting-over).

**Caratteri speciali distorti.** Vedi [Codifica dei caratteri](#character-encoding).

**Le foto mancano.** Vedi [Importa file multimediali](import-media.md).

### Ricominciare

Se un'importazione è andata male, o vuoi correggere qualcosa nel tuo vecchio programma e importare di nuovo, prima svuota l'albero utilizzando [Elimina tutti gli oggetti](settings.md#delete-all-objects) nella Zona di Pericolo delle impostazioni di amministrazione, poi importa il file corretto. Nota che questo elimina anche eventuali modifiche apportate in Gramps Web dall'importazione.
