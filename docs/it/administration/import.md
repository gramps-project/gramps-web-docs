# Importa dati

Puoi importare un albero genealogico esistente in Gramps Web caricando un file esportato da un altro programma di genealogia, da un servizio online o da Gramps Desktop.

L'importazione ha la sua pagina, disponibile per i proprietari dell'albero e gli amministratori. Aprila con **Importa Albero Genealogico** nella sezione **Dati** delle [Impostazioni di amministrazione](settings.md) (icona utente nella barra superiore dell'app ▸ Amministrazione). Mentre l'albero è ancora vuoto, il pulsante **Importa Albero Genealogico** della scheda "Inizia" nella home page, nell'albero genealogico e nelle liste porta lì anche.

## Quale file utilizzare

| Proveniente da | Esporta il tuo albero come | Estensione del file |
|---|---|---|
| Un altro programma di genealogia o servizio online | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Un foglio di calcolo | Gramps CSV | `.csv` |
| Un rubrica | vCard | `.vcf` |

GEDCOM è il formato di scambio comune che quasi ogni programma di genealogia e servizio online può esportare. Cerca un'opzione "Esporta" o "Scarica" nel tuo programma o sul sito web, e scegli GEDCOM se ti vengono offerti diversi formati. La pagina Wiki di Gramps [Importa da un altro programma di genealogia](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) ha note su programmi specifici.

Se utilizzi Gramps Desktop, scegli Gramps XML (`.gramps`) piuttosto che GEDCOM. Questo formato conserva tutti i dati di Gramps senza perdita, e i tuoi alberi online e offline mantengono gli stessi identificatori, così possono essere [sincronizzati](sync.md). Vedi [Proveniente da Gramps Desktop](#coming-from-gramps-desktop) qui sotto.

## Importa un file di albero genealogico

1. Apri la pagina di importazione come descritto sopra.
2. Sotto "Importa Albero Genealogico", scegli il tuo file e clicca su **Importa**. Il progresso del caricamento viene mostrato.
3. Il file viene letto per primo, e una finestra di dialogo "Conferma Importazione" mostra quanti oggetti contiene (persone, famiglie, eventi, luoghi, e così via), e il [rapporto](#the-import-report) dell'importatore se ne ha uno. Nulla è stato ancora aggiunto al tuo albero. Controlla che i conteggi sembrino plausibili, poi clicca su **Importa** per procedere, o su **Annulla** per abortire senza modificare nulla. Se il tuo albero contiene già persone, la finestra di dialogo avverte che importare gli stessi dati di nuovo creerà duplicati.
4. L'importazione avviene in background e viene mostrato un indicatore di progresso. Una volta importati i dati, l'indice di ricerca viene aggiornato, il che può richiedere un po' di tempo per un albero grande. Se l'importazione fallisce, viene mostrato il motivo.
5. Se l'albero non ha ancora una persona principale, ti viene offerto di sceglierne una.

Quando l'importazione è terminata, controlla il risultato: confronta il numero di persone nel pannello **Statistiche** sulla home page con il numero nel tuo vecchio programma, e apri una famiglia che conosci bene per vedere che genitori, figli, date e luoghi siano stati trasferiti come previsto. Se il file fa riferimento a foto o altri file multimediali, aggiungili successivamente, sotto [Importa File Multimediali](import-media.md) sulla stessa pagina.

!!! warning
    Un'importazione regolare è puramente additiva: crea sempre nuovi oggetti e non aggiorna o elimina quelli esistenti, anche per oggetti che esistono già nel tuo albero con lo stesso ID o handle di Gramps. Importare lo stesso file due volte – o importare un file che sovrappone dati già presenti nell'albero – duplicherà ogni oggetto corrispondente piuttosto che fonderlo o saltarlo.

    Se hai bisogno di apportare modifiche fatte altrove a un albero già importato, utilizza [Ripristina da Backup](backups.md#restore-from-backup) invece, che sostituisce l'albero per corrispondere al file caricato piuttosto che aggiungere a esso. Questo richiede un file Gramps XML o un backup di Gramps Web.

## Il rapporto di importazione

Gli importatori segnalano cosa non sono riusciti a importare completamente, ad esempio righe GEDCOM che non hanno capito, riferimenti a record mancanti dal file, o un formato di file obsoleto. Il rapporto viene mostrato sotto **Rapporto**, sia nella finestra di dialogo di conferma che dopo l'importazione. Leggilo prima di confermare: spesso spiega problemi che altrimenti noteresti solo più tardi nell'albero.

Non ogni messaggio è un problema – molti file GEDCOM contengono dati specifici del programma che vengono segnalati ma mantenuti, vedi [Dati specifici del programma](#program-specific-data). Usa i pulsanti accanto al rapporto per copiarlo o scaricarlo come file di testo, ad esempio per chiedere aiuto nel [forum](../help/help.md).

## Quote di utilizzo

L'amministratore del server può impostare limiti per il tuo albero (vedi [Configurazione del server](../install_setup/configuration.md)). La parte superiore della sezione **Dati** mostra l'utilizzo attuale rispetto a questi limiti:

- **Persone** – il numero di oggetti persona nell'albero rispetto al massimo configurato (∞ se illimitato)
- **Archiviazione multimediale** – dimensione totale dei file multimediali caricati rispetto alla quota di archiviazione configurata (∞ se illimitato)

Un'importazione che supererebbe il limite sul numero di persone viene rifiutata nel suo complesso.

## File GEDCOM

Possono essere importati sia file GEDCOM 5.5.1 che GEDCOM 7. Ci sono alcune cose di cui essere a conoscenza.

### Codifica dei caratteri

Un file GEDCOM 5.5.1 dichiara la sua codifica dei caratteri nell'intestazione. Sono supportate le codifiche UTF-8, UTF-16, ANSEL e Windows (ANSI). Se i nomi con accenti o altri caratteri speciali appaiono distorti dopo l'importazione (ad esempio `MÃ¼ller` invece di `Müller`), il file è stato probabilmente esportato con una codifica diversa da quella dichiarata. Esporta nuovamente il file dal tuo vecchio programma, scegliendo UTF-8 se ti viene offerta un'opzione, e [ricomincia](#starting-over).

I file GEDCOM 7 devono sempre essere codificati come UTF-8; altri file vengono rifiutati con un errore "File GEDCOM non valido".

### Dati specifici del programma

Molti programmi aggiungono le proprie estensioni a GEDCOM che altri programmi non comprendono. Gramps non elimina silenziosamente tali dati: le righe che non può interpretare vengono raccolte in una nota di tipo "importazione GEDCOM", allegata alla persona, famiglia o altro oggetto a cui appartengono. Rivedi queste note per vedere se qualcosa di importante non è stato trasferito.

### File multimediali

Un file GEDCOM contiene riferimenti a file multimediali (come foto o documenti scansionati), ma non i file stessi. Dopo l'importazione, gli oggetti multimediali esistono nel tuo albero, ma i loro file sono mancanti, il che è mostrato sotto [Stato del file multimediale](import-media.md#media-file-status). Per aggiungere i file, vedi [Importa file multimediali](import-media.md).

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

**"Formato non supportato".** Solo le estensioni di file elencate [sopra](#which-file-to-use) possono essere importate. Se il tuo programma o servizio online ti ha fornito un archivio ZIP, estrailo e carica il file `.ged` all'interno.

**Tutto appare due volte.** Lo stesso file è stato importato due volte. Poiché le importazioni non fondono mai, [ricomincia](#starting-over).

**Caratteri speciali distorti.** Vedi [Codifica dei caratteri](#character-encoding).

**Le foto mancano.** Vedi [Importa file multimediali](import-media.md).

### Ricominciare

Se un'importazione è andata male, o vuoi correggere qualcosa nel tuo vecchio programma e importare di nuovo, svuota prima l'albero utilizzando [Elimina tutti gli oggetti](#delete-all-objects), poi importa il file corretto. Nota che questo elimina anche eventuali modifiche apportate in Gramps Web dall'importazione.

### Elimina tutti gli oggetti

!!! danger
    Eliminare oggetti è **irreversibile**. Fai un [backup](backups.md) prima di procedere.

**Elimina tutti gli oggetti** si trova nella sezione **Zona di Pericolo** delle [Impostazioni di amministrazione](settings.md). Cliccando su **Elimina** si apre una finestra di dialogo in cui puoi scegliere di eliminare:

- **Tutti gli oggetti** – svuota completamente l'albero
- **Tipi di oggetti specifici** – ad esempio, solo eventi o solo oggetti multimediali

Ti verrà chiesto di ri-autenticarti (accedere di nuovo) per confermare l'azione. L'eliminazione avviene come un'attività in background e viene mostrato un indicatore di progresso.

!!! warning
    Eliminare solo un sottoinsieme di tipi di oggetti (anziché tutti gli oggetti contemporaneamente) può richiedere molto tempo per alberi grandi, poiché il server deve controllare e aggiornare tutte le relazioni tra gli oggetti.
