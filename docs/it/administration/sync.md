# Sincronizza Gramps Web e Gramps Desktop

*Gramps Web Sync* è un componente aggiuntivo per Gramps che consente di sincronizzare il tuo database Gramps sul computer desktop con Gramps Web, inclusi i file multimediali.

!!! warning
    Come con qualsiasi strumento di sincronizzazione, non considerare questo come uno strumento di backup. Una cancellazione accidentale da un lato verrà propagata all'altro lato. Assicurati di creare regolari backup (in formato XML di Gramps) del tuo albero genealogico.

!!! info
    La documentazione si riferisce all'ultima versione del componente aggiuntivo Gramps Web Sync. Utilizza il gestore dei componenti aggiuntivi di Gramps per aggiornare il componente aggiuntivo all'ultima versione, se necessario.

!!! note "Cosa è cambiato nella versione 1.5"
    L'interfaccia del componente aggiuntivo è stata riscritta nella versione 1.5. La procedura guidata passo-passo è scomparsa, sostituita da una finestra unica, e i file multimediali ora vengono confermati insieme alle modifiche degli oggetti anziché su una pagina separata in seguito. Se stai cercando il selettore della modalità di sincronizzazione, ora si trova **sopra** l'elenco delle modifiche anziché sotto di esso. La modalità di sincronizzazione **merge** è stata rimossa; vedi [Modalità di sincronizzazione](#sync-mode) qui sotto.

## Installazione

Il componente aggiuntivo richiede Gramps 6.0 in esecuzione su Python 3.10 o versioni successive. È disponibile in Gramps Desktop e può essere installato [nel modo consueto](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Assicurati di utilizzare la stessa versione di Gramps sul tuo desktop rispetto a quella in esecuzione sul tuo server. Consulta la sezione [Ottieni aiuto](../help/help.md) per scoprire quale versione di Gramps sta eseguendo il tuo server. La versione di Gramps ha la forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devono essere gli stessi su web e desktop.

### Requisiti del server

Il componente aggiuntivo controlla due cose sul tuo server non appena si connette e rifiuta di continuare se una delle due non è soddisfatta. Entrambi i controlli avvengono prima che venga scaricato qualsiasi cosa.

- **Versione 3.x dell'API Gramps Web.** Questa versione del componente aggiuntivo, per Gramps 6.0, funziona con l'API Gramps Web 3. Un server più vecchio deve essere aggiornato; un server che esegue una versione principale dell'API *più recente* necessita di una versione più recente di Gramps, non di un componente aggiuntivo più recente, poiché ogni linea di rilascio di Gramps si abbina a una versione dell'API. Puoi trovare la versione del tuo server sotto *Impostazioni ▸ Informazioni sulla versione* in Gramps Web.
- **Una coda di attività in background.** La sincronizzazione invia le sue modifiche come un'attività in background. Su un server senza una coda di attività configurata, l'applicazione delle modifiche verrebbe eseguita in modo sincrono e andrebbe in timeout su qualsiasi albero genealogico reale, quindi il componente aggiuntivo rifiuta di avviarsi piuttosto che fallire a metà strada.

Hai anche bisogno di un account con almeno privilegi di editor per applicare modifiche al database remoto.

Passo opzionale:

??? note inline end "Bug del portachiavi Gnome"
    Attualmente c'è un [bug nel portachiavi python](https://github.com/jaraco/keyring/issues/496) che influisce su molte configurazioni desktop Gnome. Potresti dover creare il file di configurazione `~/.config/python_keyring/keyringrc.cfg` e modificarlo in questo modo:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installa `keyring` (ad esempio `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) per consentire di memorizzare in modo sicuro la password API nel gestore delle password del tuo sistema.

Se il portachiavi non può essere utilizzato, il componente aggiuntivo lo segnala e continua senza di esso: ti verrà semplicemente chiesta la password ogni volta. Sul pacchetto **Snap** di Gramps, il portachiavi di sistema è bloccato dal confinement fino a quando non connetti l'interfaccia una volta:

```bash
snap connect gramps:password-manager-service
```

Il componente aggiuntivo mostra questo comando esatto quando rileva la situazione.

## Utilizzo

Una volta installato, il componente aggiuntivo è disponibile in Gramps sotto *Strumenti ▸ Elaborazione Albero Genealogico ▸ Gramps&nbsp;Web&nbsp;Sync*. Dopo aver confermato il dialogo di avviso che la cronologia delle modifiche verrà scartata, si apre la finestra di sincronizzazione.

**Nessuna modifica viene applicata al tuo albero locale o al server fino a quando non le confermi esplicitamente.**

La finestra ha una striscia lungo la parte superiore che nomina l'albero genealogico con cui stai sincronizzando, l'account e l'indirizzo a cui appartiene, e quando è stato sincronizzato l'ultima volta. In fondo, vengono mostrati la versione del componente aggiuntivo e dell'API Web del server — utile quando si riporta un problema.

### Connessione

Se hai già sincronizzato questo albero genealogico in precedenza e la tua password è memorizzata, il componente aggiuntivo si connette non appena si apre e passa direttamente al confronto. Altrimenti, chiede l'URL di base della tua istanza Gramps Web (esempio: `https://mygrampsweb.com/`), il tuo nome utente e la tua password.

L'URL e il nome utente sono memorizzati in testo semplice nella tua directory utente di Gramps. La password è memorizzata nel gestore delle password del tuo sistema solo se lasci selezionata l'opzione **Ricorda password**; deselezionarla rimuove qualsiasi password già memorizzata per quel server.

!!! tip "Diversi alberi genealogici, diversi server"
    Ogni server con cui sincronizzi è memorizzato separatamente, insieme al proprio record di quando è stato sincronizzato l'ultima volta. Alternare tra due server non disturba più nessuno dei due.

    Ogni voce registra anche **quale albero genealogico locale** è stato sincronizzato l'ultima volta. Il componente aggiuntivo si connette autonomamente solo quando corrisponde all'albero che hai aperto; altrimenti mostra i dettagli di connessione e attende che tu prema *Connetti*, con un avviso se le credenziali memorizzate appartengono a un albero diverso. Questo è importante perché sincronizzare un albero contro un server che contiene un albero *diverso* proporrebbe di eliminare i contenuti di entrambi.

Due azioni sono disponibili mentre non viene scritto nulla:

- **Cambia server…**, sulla striscia superiore, torna ai dettagli di connessione in modo da poter puntare questo albero a un server diverso. Interrompe un confronto in corso piuttosto che farti aspettare che finisca.
- **Dimentica questo server**, nel pannello di connessione, rimuove l'indirizzo memorizzato, il nome utente e la password, insieme al record di quando questo albero è stato sincronizzato l'ultima volta. La prossima sincronizzazione confronta quindi i due alberi da zero.

Se inserisci un indirizzo che inizia con `http://` anziché `https://`, appare un avviso mentre digiti. La tua password verrebbe inviata in testo chiaro, quindi usala solo per test locali.

### Revisione delle modifiche

Il componente aggiuntivo confronta i database locale e remoto e mostra cosa propone di fare. A differenza delle versioni precedenti, che elencavano le differenze grezze tra i due alberi, l'elenco ora mostra le **azioni** che verranno eseguite, raggruppate in base a quale database modificano:

```
▾ Cambierà su questo computer (7 oggetti)
    ▾ Aggiungi 3 oggetti
        Persona   John Smith        I0123
    ▾ Aggiorna 4 oggetti
        …
▾ Cambierà sul server (5 oggetti)
    …
```

Ogni riga nomina l'oggetto, quindi puoi capire chi o cosa è interessato anziché vedere solo un ID Gramps.

Se qualcosa verrà eliminato, un avviso sopra l'elenco indica quanti oggetti e da quale lato. Questo appare ogni volta che sono coinvolte cancellazioni, anche durante una normale sincronizzazione bidirezionale che sta propagando una cancellazione che hai effettuato tu stesso.

Premi **Applica** per eseguire ciò che l'elenco descrive.

!!! warning "Non modificare mentre rivedi"
    La finestra di sincronizzazione non blocca il resto di Gramps, quindi puoi continuare a lavorare mentre l'elenco è aperto. Se modifichi un oggetto interessato, il componente aggiuntivo lo rileva quando premi Applica, si ferma senza apportare modifiche e ti chiede di confrontare di nuovo. Niente viene perso, ma il confronto deve essere ripetuto.

#### Modalità di sincronizzazione

La modalità di sincronizzazione è selezionata **sopra** l'elenco delle modifiche. Cambiarla ricostruisce l'elenco, poiché la modalità decide cosa diventa effettivamente ogni differenza.

- **Sincronizzazione bidirezionale** (impostazione predefinita) — le modifiche da entrambi i lati vengono combinate. Gli oggetti modificati in entrambi i posti vengono uniti.
- **Ripristina il server per corrispondere a questo computer** — il server viene fatto corrispondere a questo computer. Qualsiasi cosa modificata solo sul server viene scartata.
- **Ripristina questo computer per corrispondere al server** — questo computer viene fatto corrispondere al server. Qualsiasi cosa modificata solo qui viene scartata.

!!! note
    La modalità **merge** disponibile nelle versioni precedenti è stata rimossa. Si differenziava dalla sincronizzazione bidirezionale solo nel ripristinare oggetti eliminati da un lato anziché propagare la cancellazione, che non era una distinzione che l'interfaccia potesse spiegare utilmente. Se ti sei affidato a essa, utilizza la sincronizzazione bidirezionale e ripristina qualsiasi cosa tu voglia mantenere da un backup.

### File multimediali

I file multimediali vengono gestiti come parte della stessa conferma, non come un passaggio separato. Se ci sono file da trasferire, una casella di controllo sotto l'elenco offre di spostarli:

```
[x] Trasferisci anche 12 file multimediali (4 da scaricare, 8 da caricare)
```

Deselezionala per sincronizzare le modifiche agli oggetti senza toccare i file.

I file che mancano su *entrambi* i lati sono elencati separatamente, perché non si può fare nulla al riguardo:

```
2 file multimediali mancano su entrambi i lati e non possono essere trasferiti.
```

Nota le seguenti limitazioni della sincronizzazione dei file multimediali:

- Se un file locale ha un checksum diverso da quello memorizzato nel database di Gramps (questo può accadere ad esempio per i file Word quando vengono modificati dopo essere stati aggiunti a Gramps), il caricamento fallirà con un messaggio di errore.
- Lo strumento non controlla l'integrità di tutti i file locali, quindi se un file locale esiste sotto il percorso memorizzato per l'oggetto multimediale, ma il file è diverso dal file sul server, lo strumento non lo rileverà. Usa il componente aggiuntivo Media Verify per rilevare file con checksum errati.

### Quando qualcosa va storto

Se una sincronizzazione fallisce a metà strada — ad esempio, a causa di una connessione interrotta — il componente aggiuntivo riporta ciò che era già stato applicato e offre **Riprova**, che riprende dal passaggio che è fallito piuttosto che ricominciare. La copia scaricata dell'albero remoto viene mantenuta, quindi riprovare non scarica e confronta di nuovo.

I dettagli tecnici del fallimento sono disponibili dietro un espansore *Dettagli*, con un pulsante per copiarli per una segnalazione di bug.

## Risoluzione dei problemi

### Registrazione di debug

Se stai riscontrando problemi con il componente aggiuntivo Sync, avvia Gramps con la registrazione di debug abilitata [avviando Gramps dalla riga di comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con l'opzione seguente:

```bash
gramps --debug grampswebsync
```

Questo stamperà molte dichiarazioni di registrazione utili nella riga di comando che ti aiuteranno a identificare la causa del problema.

### Credenziali del server

Se la connessione fallisce, controlla attentamente l'URL del server, il tuo nome utente e la tua password.

### Il componente aggiuntivo rifiuta di connettersi

Se il componente aggiuntivo riporta che la versione dell'API Gramps Web del server è troppo vecchia o troppo nuova, o che non è configurata alcuna coda di attività in background, consulta [Requisiti del server](#server-requirements) qui sopra. Questi vengono controllati prima di qualsiasi altra cosa, quindi il messaggio indica direttamente il problema.

### Problemi di autorizzazione

Se riscontri un errore relativo alle autorizzazioni, controlla il ruolo utente del tuo account utente Gramps Web. Puoi applicare modifiche al database remoto solo se sei un utente con ruolo di editor, proprietario o amministratore.

### Modifiche al database inaspettate

Se lo strumento di sincronizzazione rileva modifiche che pensi non siano avvenute, potrebbe esserci delle incoerenze in uno dei database che ingannano Gramps nel rilevare una differenza, oppure che l'orario non è sincronizzato tra il tuo computer locale e il tuo server.

Controlla che gli orologi su entrambe le macchine siano impostati correttamente (nota, il fuso orario non è importante poiché lo strumento utilizza timestamp Unix, che sono agnostici rispetto al fuso orario).

Puoi anche eseguire lo strumento di controllo e riparazione sul tuo database locale e vedere se questo aiuta.

Un metodo brutale ma efficace per garantire che le incoerenze nel tuo database locale non causino falsi positivi è esportare il tuo database in formato XML di Gramps e reimportarlo in un nuovo database vuoto. Questa è un'operazione senza perdita di dati ma assicura che tutti i dati vengano importati in modo coerente.

!!! tip
    Se il componente aggiuntivo propone un numero allarmante di cancellazioni, controlla prima la striscia superiore: nomina l'albero genealogico sul server a cui stai per scrivere. Sincronizzare contro un server che contiene un albero *diverso* produce esattamente questo sintomo.

### Errori di timeout

La sincronizzazione con il server viene elaborata da un lavoratore in background, quindi le sincronizzazioni di lunga durata non dovrebbero andare in timeout. Un server senza una coda di attività configurata viene rifiutato al momento della connessione per questo motivo — vedi [Requisiti del server](#server-requirements).

Le richieste dal componente aggiuntivo al server vanno in timeout dopo 60 secondi senza risposta, quindi un server irraggiungibile riporta un errore di connessione anziché bloccarsi indefinitamente.

### Errori inaspettati dei file multimediali

Se il caricamento di un file multimediale fallisce, è spesso causato da una discrepanza nel checksum del file effettivo su disco e il checksum nel database locale di Gramps. Questo accade spesso con file modificabili, come documenti di ufficio, modificati al di fuori di Gramps. Si prega di utilizzare il componente aggiuntivo Gramps Media Verify per correggere i checksum di tutti i file multimediali.

### Chiedi aiuto

Se tutto quanto sopra non aiuta, puoi chiedere aiuto alla comunità pubblicando nella [categoria Gramps Web del forum di Gramps](https://gramps.discourse.group/c/gramps-web/28). Assicurati di fornire:

- la versione del componente aggiuntivo Gramps Web Sync (e utilizza per favore l'ultima versione rilasciata) — è mostrata in fondo alla finestra di sincronizzazione, accanto alla versione dell'API Web del server
- la versione di Gramps desktop che stai utilizzando
- l'output della registrazione di debug di Gramps, abilitata come descritto sopra
- le informazioni sulla versione di Gramps Web (puoi trovarle sotto Impostazioni/Informazioni sulla versione)
- qualsiasi dettaglio tu possa fornire sulla tua installazione di Gramps Web (self-hosted, Grampshub, ...)
- l'output dei log del server Gramps Web, se hai accesso a essi (quando usi docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

## Contesto: come funziona il componente aggiuntivo

Se sei curioso di sapere come funziona effettivamente il componente aggiuntivo, puoi trovare ulteriori dettagli in questa sezione.

Il componente aggiuntivo è progettato per mantenere un database Gramps locale sincronizzato con un database Gramps Web remoto, per consentire modifiche sia locali che remote (editing collaborativo).

Non è **adatto**

- Per sincronizzare con un database che non è un derivato diretto (a partire da una copia del database o da un'esportazione/importazione XML di Gramps) del database locale
- Per unire due database con un gran numero di modifiche da entrambi i lati che necessitano di attenzione manuale per la fusione. Usa l'ottimo [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) per questo scopo.

I principi di funzionamento dello strumento sono molto semplici:

- Confronta i database locale e remoto
- Se ci sono differenze, controlla il timestamp dell'oggetto identico più recente, chiamiamolo **t**
- Se un oggetto è cambiato più recentemente di **t** esiste in un database ma non nell'altro, viene sincronizzato in entrambi (si presume oggetto nuovo)
- Se un oggetto è cambiato l'ultima volta prima di **t** è assente in un database, viene eliminato in entrambi (si presume oggetto eliminato)
- Se un oggetto è diverso ma è cambiato dopo **t** solo in un database, sincronizza con l'altro (si presume oggetto modificato)
- Se un oggetto è diverso ma è cambiato dopo **t** in entrambi i database, uniscili (si presume modifica conflittuale)

Il tempo dell'ultima sincronizzazione riuscita viene anche registrato, separatamente per ogni server, e utilizzato come **t** quando è più recente dell'oggetto identico più recente.

Questo algoritmo è semplice e robusto poiché non richiede il tracciamento della cronologia di sincronizzazione. Tuttavia, funziona meglio quando *sincronizzi spesso*.
