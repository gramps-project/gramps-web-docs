# Sincronizzare Gramps Web e Gramps Desktop

*Gramps Web Sync* è un componente aggiuntivo per Gramps che consente di sincronizzare il tuo database Gramps sul computer desktop con Gramps Web, inclusi i file multimediali.

!!! warning
    Come con qualsiasi strumento di sincronizzazione, non considerare questo come uno strumento di backup. Una cancellazione accidentale da un lato verrà propagata all'altro lato. Assicurati di creare backup regolari (in formato XML di Gramps) del tuo albero genealogico.

!!! info
    La documentazione si riferisce all'ultima versione del componente aggiuntivo Gramps Web Sync. Utilizza il gestore dei componenti aggiuntivi di Gramps per aggiornare il componente aggiuntivo all'ultima versione se necessario.

## Installazione

Il componente aggiuntivo richiede Gramps 6.0 in esecuzione su Python 3.10 o versioni successive. È disponibile in Gramps Desktop e può essere installato [nel modo consueto](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Assicurati di utilizzare la stessa versione di Gramps sul tuo desktop e quella in esecuzione sul tuo server. Consulta la sezione [Get Help](../help/help.md) per scoprire quale versione di Gramps è in esecuzione sul tuo server. La versione di Gramps ha la forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devono essere gli stessi su web e desktop.

Passo facoltativo:

??? note inline end "Bug del portachiavi Gnome"
    Attualmente c'è un [bug nel portachiavi python](https://github.com/jaraco/keyring/issues/496) che influisce su molte configurazioni desktop Gnome. Potresti dover creare il file di configurazione `~/.config/python_keyring/keyringrc.cfg` e modificarlo in questo modo:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installa `keyring` (ad es. `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) per consentire di memorizzare in modo sicuro la password API nel gestore delle password del tuo sistema.

## Utilizzo

Una volta installato, il componente aggiuntivo è disponibile in Gramps sotto *Strumenti > Elaborazione Albero Genealogico > Gramps&nbsp;Web&nbsp;Sync*. Una volta avviato, e dopo aver confermato il dialogo che la cronologia delle modifiche verrà scartata, una procedura guidata ti guiderà attraverso i passaggi di sincronizzazione. Nota che nessuna modifica verrà applicata al tuo albero locale o al server fino a quando non le confermerai esplicitamente.

### Passo 1: inserire le credenziali del server

Lo strumento ti chiederà l'URL di base (esempio: `https://mygrampsweb.com/`) della tua istanza di Gramps Web, il tuo nome utente e la password. Hai bisogno di un account con almeno privilegi di editor per sincronizzare le modifiche nel tuo database remoto. Il nome utente e l'URL verranno memorizzati in testo semplice nella directory utente di Gramps, la password verrà memorizzata solo se `keyring` è installato (vedi sopra).

### Passo 2: rivedere le modifiche

Dopo aver confermato le tue credenziali, lo strumento confronta i database locale e remoto e valuta se ci sono differenze. Se ci sono, visualizza un elenco delle modifiche agli oggetti (dove un oggetto può essere una persona, una famiglia, un evento, un luogo, ecc.) appartenenti a una delle seguenti categorie:

- aggiunto localmente
- eliminato localmente
- modificato localmente
- aggiunto remotamente 
- eliminato remotamente
- modificato remotamente
- modificato simultaneamente (cioè, da entrambi i lati)

Lo strumento utilizza i timestamp per valutare quale lato è più recente per ciascun oggetto (vedi "Background" qui sotto se sei interessato ai dettagli).

Se le modifiche sembrano come previsto, puoi fare clic su "Applica" per applicare le modifiche necessarie ai database locale e remoto.

!!! tip "Avanzato: Modalità di sincronizzazione"
    Sotto l'elenco delle modifiche, puoi selezionare una modalità di sincronizzazione.
    
    La modalità predefinita, **sincronizzazione bidirezionale**, significa che applicherà le modifiche a entrambi i lati (locale e remoto) replicando le modifiche rilevate (gli oggetti aggiunti localmente verranno aggiunti sul lato remoto, ecc.). Gli oggetti modificati su entrambi i lati verranno uniti e aggiornati su entrambi i lati.

    L'opzione **ripristina remoto su locale** garantirà invece che il database Gramps remoto appaia esattamente come quello locale. Qualsiasi oggetto rilevato come "aggiunto remotamente" verrà eliminato nuovamente, gli oggetti rilevati come "eliminati remotamente" verranno aggiunti nuovamente, ecc. *Nessuna modifica verrà applicata al database Gramps locale.*

    L'opzione **ripristina locale su remoto** funziona al contrario e imposta lo stato locale su quello del database remoto. *Nessuna modifica verrà applicata al database remoto.*

    Infine, l'opzione **unisci** è simile alla sincronizzazione bidirezionale in quanto modifica entrambi i database, ma *non elimina alcun oggetto*, ma ripristina tutti gli oggetti eliminati solo da un lato.

### Passo 3: sincronizzare i file multimediali

*Dopo* che i database sono stati sincronizzati, lo strumento controlla eventuali file multimediali nuovi o aggiornati. Se ne trova, visualizza un elenco e chiede conferma per caricare/scaricare i file necessari.

Nota le seguenti limitazioni della sincronizzazione dei file multimediali:

- Se un file locale ha un checksum diverso da quello memorizzato nel database di Gramps (questo può accadere ad esempio per i file Word quando vengono modificati dopo essere stati aggiunti a Gramps), il caricamento fallirà con un messaggio di errore.
- Lo strumento non controlla l'integrità di tutti i file locali, quindi se un file locale esiste sotto il percorso memorizzato per l'oggetto multimediale, ma il file è diverso dal file sul server, lo strumento non lo rileverà. Usa il componente aggiuntivo Media Verify per rilevare file con checksum errati.

## Risoluzione dei problemi

### Registrazione di debug

Se stai riscontrando problemi con il componente aggiuntivo Sync, avvia Gramps con la registrazione di debug abilitata [avviando Gramps dalla riga di comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con l'opzione seguente:

```bash
gramps --debug grampswebsync
```

Questo stamperà molte dichiarazioni di registrazione utili nella riga di comando che ti aiuteranno a identificare la causa del problema.

### Credenziali del server

Se il primo passo fallisce già, controlla attentamente l'URL del server, il tuo nome utente e la password.

### Problemi di autorizzazione

Se riscontri un errore relativo alle autorizzazioni, controlla il ruolo utente del tuo account utente Gramps Web. Puoi applicare modifiche al database remoto solo se sei un utente con ruolo di editor, proprietario o amministratore.

### Modifiche al database inaspettate

Se lo strumento di sincronizzazione rileva modifiche che pensi non siano avvenute, potrebbe esserci delle incoerenze in uno dei database che ingannano Gramps nel rilevare una differenza, oppure che l'orario non è sincronizzato tra il tuo computer locale e il tuo server.

Controlla che gli orologi su entrambe le macchine siano impostati correttamente (nota, il fuso orario non conta poiché lo strumento utilizza timestamp Unix, che sono indipendenti dal fuso orario).

Puoi anche eseguire lo strumento di controllo e riparazione sul tuo database locale e vedere se questo aiuta.

Un metodo brutale ma efficace per garantire che le incoerenze nel tuo database locale non causino falsi positivi è esportare il tuo database in formato XML di Gramps e reimportarlo in un nuovo database vuoto. Questa è un'operazione senza perdita di dati ma assicura che tutti i dati vengano importati in modo coerente.

### Errori di timeout

Se stai riscontrando errori di timeout (ad es. indicati da un errore di stato HTTP 408 o un altro messaggio di errore che include la parola "timeout"), è probabile che sia dovuto a un gran numero di modifiche che devono essere sincronizzate sul lato remoto in combinazione con la configurazione del tuo server.

Per le versioni del componente aggiuntivo di sincronizzazione precedenti alla v1.2.0 e le versioni dell'API Gramps Web precedenti alla v2.7.0 (vedi la scheda delle informazioni sulla versione in Gramps Web), la sincronizzazione sul lato server veniva elaborata in una singola richiesta che sarebbe scaduta, a seconda della configurazione del server, dopo uno o al massimo pochi minuti. Per grandi sincronizzazioni (come dopo aver importato migliaia di oggetti nel database locale o tentando di sincronizzare un intero database locale con un database vuoto sul server), questo può essere troppo breve.

Se stai utilizzando il componente aggiuntivo di sincronizzazione v1.2.0 o successivo e l'API Gramps Web v2.7.0 o successiva, la sincronizzazione sul lato server viene elaborata da un lavoratore in background e può durare molto a lungo (verrà visualizzata una barra di avanzamento) e gli errori di timeout non dovrebbero verificarsi.

### Errori inaspettati dei file multimediali

Se il caricamento di un file multimediale fallisce, è spesso causato da una discrepanza nel checksum del file effettivo su disco e il checksum nel database locale di Gramps. Questo accade spesso con file modificabili, come documenti di ufficio, modificati al di fuori di Gramps. Si prega di utilizzare il componente aggiuntivo Gramps Media Verify per correggere i checksum di tutti i file multimediali.

### Chiedi aiuto

Se tutto quanto sopra non aiuta, puoi chiedere aiuto alla comunità pubblicando nella [categoria Gramps Web del forum di Gramps](https://gramps.discourse.group/c/gramps-web/28). Assicurati di fornire:

- la versione del componente aggiuntivo Gramps Web Sync (e utilizza per favore l'ultima versione rilasciata)
- la versione di Gramps desktop che stai utilizzando
- l'output della registrazione di debug di Gramps, abilitata come descritto sopra
- le informazioni sulla versione di Gramps Web (puoi trovarle sotto Impostazioni/Informazioni sulla versione)
- eventuali dettagli che puoi fornire sulla tua installazione di Gramps Web (self-hosted, Grampshub, ...)
- l'output dei log del server Gramps Web, se hai accesso a essi (quando utilizzi docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

## Background: come funziona il componente aggiuntivo

Se sei curioso di sapere come funziona effettivamente il componente aggiuntivo, puoi trovare ulteriori dettagli in questa sezione.

Il componente aggiuntivo è progettato per mantenere un database Gramps locale in sincronizzazione con un database Gramps Web remoto, per consentire sia modifiche locali che remote (editing collaborativo).

Non è **adatto**

- Per sincronizzare con un database che non è un derivato diretto (partendo da una copia del database o da un'esportazione/importazione XML di Gramps) del database locale
- Per unire due database con un gran numero di modifiche su entrambi i lati che necessitano di attenzione manuale per la fusione. Usa l'ottimo [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) a questo scopo.

I principi di funzionamento dello strumento sono molto semplici:

- Confronta i database locale e remoto
- Se ci sono differenze, controlla il timestamp dell'oggetto identico più recente, chiamiamolo **t**
- Se un oggetto è cambiato più recentemente di **t** esiste in un database ma non nell'altro, viene sincronizzato in entrambi (si assume un nuovo oggetto)
- Se un oggetto è cambiato l'ultima volta prima di **t** è assente in un database, viene eliminato in entrambi (si assume un oggetto eliminato)
- Se un oggetto è diverso ma è cambiato dopo **t** solo in un database, viene sincronizzato nell'altro (si assume un oggetto modificato)
- Se un oggetto è diverso ma è cambiato dopo **t** in entrambi i database, vengono uniti (si assume una modifica conflittuale)

Questo algoritmo è semplice e robusto in quanto non richiede il tracciamento della cronologia di sincronizzazione. Tuttavia, funziona meglio quando *sincronizzi spesso*.
