# Backup e ripristino

I proprietari dell'albero possono creare, scaricare e ripristinare i backup dell'albero nella sezione **Backup** delle [Impostazioni di amministrazione](settings.md).

Un backup contiene i dati dell'albero genealogico, inclusi i record privati, le impostazioni dell'albero e gli utenti dell'albero. I file multimediali non sono inclusi; vedere [Esegui il backup dei tuoi file multimediali](export.md#back-up-your-media-files).

## Backup memorizzati

Se l'amministratore del server ha impostato una directory di backup (`BACKUP_DIR`, vedere [Configurazione del server](../install_setup/configuration.md)), i backup possono essere memorizzati sul server. In caso contrario, la sezione mostra un avviso che indica che la memorizzazione dei backup non è configurata e che è disponibile solo il ripristino da un file caricato.

Clicca su **Crea Backup...** per creare un backup. Viene creato come un'attività in background e poi appare nell'elenco dei backup memorizzati, con la sua data, il numero di persone e la sua dimensione. Il server conserva solo i backup più recenti (cinque per impostazione predefinita) e elimina automaticamente quelli più vecchi. Anche il numero di backup che possono essere creati al giorno è limitato.

Per ogni backup memorizzato, puoi:

- **Scaricarlo** come file `.tar`, ad esempio per conservarne una copia altrove.
- **Ripristinarlo**, come descritto di seguito.
- **Elimarlo**, dopo aver confermato.

Un backup creato con una versione più recente di Gramps Web rispetto a quella in esecuzione sul server è contrassegnato con un'icona di avviso e non può essere ripristinato.

## Ripristina da Backup

Ripristina l'albero da un backup memorizzato o da un file caricato. Per ripristinare un backup memorizzato, clicca sul pulsante di ripristino accanto ad esso. Per ripristinare da un file, seleziona un backup di Gramps Web (`.tar`) o un file XML di Gramps (`.gramps`) e clicca su **Ripristina**.

!!! danger
    Il ripristino dei dati è una sostituzione distruttiva, non una fusione. Qualsiasi oggetto esistente non presente nel backup viene eliminato.

Per un backup di Gramps Web, viene visualizzata una finestra di dialogo che mostra quando è stato effettuato il backup, per quale albero e con quale versione, e ti consente di scegliere quali parti ripristinare:

- **Dati** – gli oggetti dell'albero genealogico
- **Impostazioni dell'albero** – le impostazioni della pagina di amministrazione, come i colori del tema, il titolo dell'app e la nota della home page
- **Utenti** – gli utenti dell'albero

Clicca su **Anteprima** per vedere quali cambiamenti apporterà il ripristino. Un file XML di Gramps contiene solo dati, quindi per tale file l'anteprima inizia subito. Ti verrà chiesto di ri-autenticarti se la tua sessione non è abbastanza recente. L'anteprima viene eseguita come un'attività in background e, una volta completata, apre una finestra di dialogo che riassume le modifiche per tipo di oggetto (persone, famiglie, eventi, luoghi, citazioni, fonti, repository, oggetti multimediali, note, tag), e per le impostazioni dell'albero e gli utenti se selezionati:

- **Aggiungi** – oggetti presenti nel backup ma mancanti nell'albero corrente
- **Aggiorna** – oggetti presenti in entrambi che differiscono
- **Elimina** – oggetti nell'albero corrente che sono assenti nel backup
- **Invariato** – oggetti identici in entrambi

Se ci sono oggetti che verrebbero eliminati, la finestra di dialogo avvisa quanti sono. Rivedi il riepilogo, quindi clicca su **Ripristina** per applicare le modifiche, o **Annulla** per abortire.

Dopo il ripristino, gli utenti aggiunti dal backup vengono elencati. Ricevono una password casuale, quindi devono reimpostare la propria password prima di poter accedere. Gli utenti che esistono già sul server non vengono mai modificati. Anche gli oggetti multimediali i cui file mancano sul server vengono elencati; caricali tramite [Importa file multimediali](import-media.md).

!!! note
    Il ripristino dei dati ripristina solo i dati degli oggetti e i riferimenti ai media. I file multimediali binari stessi e i metadati dell'albero (persona predefinita, segnalibri, gruppi di nomi) non sono interessati.

!!! tip
    Usa questo per ripristinare un albero a un backup noto e valido, ad esempio dopo un'importazione errata o una modifica di massa indesiderata.

## Gramps XML come backup

Se la memorizzazione dei backup non è disponibile, o se desideri solo conservare una copia dei dati dell'albero genealogico, [esporta](export.md) l'albero come Gramps XML. Tale file può essere ripristinato anche tramite [Ripristina da Backup](#restore-from-backup).

Nota che se il tuo utente di Gramps Web non ha il permesso di visualizzare record privati, l'esportazione non sarà un backup completo, poiché non conterrà alcun record privato.
