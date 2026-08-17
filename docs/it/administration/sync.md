# Sincronizzare Gramps Web e Gramps Desktop

*Gramps Web Sync* è un componente aggiuntivo per Gramps che sincronizza il database di Gramps sul tuo computer desktop con Gramps Web, inclusi i file multimediali. Le modifiche apportate da entrambi i lati vengono trasferite all'altro, in modo da poter lavorare localmente e online sullo stesso albero genealogico.

Come qualsiasi strumento di sincronizzazione, non è un backup: se elimini qualcosa da un lato, verrà eliminato anche dall'altro lato. Mantieni backup regolari del tuo albero genealogico in formato XML di Gramps.

## Installazione

Il componente aggiuntivo richiede Gramps 6.0 in esecuzione su Python 3.10 o versione successiva. È disponibile in Gramps Desktop e può essere installato [nel modo consueto](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Questa documentazione descrive l'ultima versione del componente aggiuntivo; utilizza il gestore di componenti aggiuntivi di Gramps per aggiornarlo se necessario.

Il tuo desktop e il tuo server devono eseguire la stessa versione di Gramps. La versione ha la forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devono corrispondere. Vedi [Ottieni aiuto](../help/help.md) per scoprire quale versione di Gramps sta eseguendo il tuo server.

### Requisiti del server

Il componente aggiuntivo controlla due cose sul tuo server non appena si connette, prima che venga scaricato qualsiasi cosa, e si ferma con un messaggio se una delle due non è soddisfatta:

- **Versione API di Gramps Web 3.x.** Questa versione del componente aggiuntivo, per Gramps 6.0, funziona con l'API di Gramps Web 3. Un server più vecchio ha bisogno di un aggiornamento; un server che esegue una versione principale dell'API *più recente* necessita di una versione più recente di Gramps, non di un componente aggiuntivo più recente, poiché ogni linea di rilascio di Gramps è abbinata a una versione dell'API. Puoi trovare la versione del tuo server sotto *Impostazioni ▸ Informazioni sulla versione* in Gramps Web.
- **Una coda di attività in background.** Le modifiche vengono applicate sul server come un'attività in background. Senza una coda di attività, questo verrebbe eseguito in modo sincrono e andrebbe in timeout su qualsiasi vero albero genealogico.

Per applicare modifiche al database remoto, hai bisogno di un account con il ruolo di editor, proprietario o amministratore.

### Memorizzare la tua password (opzionale)

Installa `keyring` (ad es. `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) per memorizzare la password API nel gestore delle password del tuo sistema. Se il keyring non può essere utilizzato, il componente aggiuntivo lo segnala e continua senza di esso: ti verrà semplicemente chiesta la password ogni volta.

Nel pacchetto **Snap** di Gramps, il keyring di sistema è bloccato da confinamento fino a quando non connetti l'interfaccia una volta. Il componente aggiuntivo mostra questo comando quando rileva la situazione:

```bash
snap connect gramps:password-manager-service
```

In molte configurazioni desktop di Gnome, un [bug in python keyring](https://github.com/jaraco/keyring/issues/496) significa che devi creare il file di configurazione `~/.config/python_keyring/keyringrc.cfg` con il seguente contenuto:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Utilizzo

Il componente aggiuntivo è disponibile in Gramps sotto *Strumenti ▸ Elaborazione Albero Genealogico ▸ Gramps&nbsp;Web&nbsp;Sync*. Dopo aver confermato il dialogo di avviso che la cronologia delle annullazioni verrà scartata, si apre la finestra di sincronizzazione. Nessuna modifica viene applicata al tuo albero locale o al server fino a quando non le confermi esplicitamente.

Una striscia lungo la parte superiore della finestra nomina l'albero genealogico con cui stai sincronizzando, l'account e l'indirizzo a cui appartiene, e quando è stato sincronizzato l'ultima volta. In fondo, viene mostrata la versione del componente aggiuntivo e dell'API Web del server, utile quando si segnala un problema.

### Connessione

Se hai già sincronizzato questo albero genealogico in precedenza e la tua password è memorizzata, il componente aggiuntivo si connette non appena si apre e passa direttamente al confronto. Altrimenti, chiede l'URL di base della tua istanza di Gramps Web (esempio: `https://mygrampsweb.com/`), il tuo nome utente e la tua password.

L'URL e il nome utente sono memorizzati in testo chiaro nella directory utente di Gramps. La password è memorizzata nel gestore delle password del tuo sistema solo se lasci selezionata l'opzione **Ricorda password**; deselezionandola rimuove qualsiasi password già memorizzata per quel server. Se inserisci un indirizzo che inizia con `http://` invece di `https://`, il componente aggiuntivo ti avverte mentre digiti, poiché la tua password verrebbe inviata in testo chiaro.

Ogni server con cui sincronizzi è memorizzato separatamente, insieme al proprio record di quando è stato sincronizzato l'ultima volta, in modo da poter alternare tra due server senza disturbare nessuno. Ogni voce registra anche quale albero genealogico locale è stato sincronizzato l'ultima volta. Il componente aggiuntivo si connette autonomamente solo quando corrisponde all'albero che hai aperto; altrimenti mostra i dettagli di connessione e aspetta che tu prema *Connetti*.

Due azioni sono disponibili mentre non viene scritto nulla:

- **Cambia server…**, sulla striscia superiore, ritorna ai dettagli di connessione in modo da poter puntare questo albero a un server diverso. Interrompe un confronto in corso piuttosto che farti aspettare che finisca.
- **Dimentica questo server**, nel pannello di connessione, rimuove l'indirizzo memorizzato, il nome utente e la password, insieme al record di quando questo albero è stato sincronizzato l'ultima volta. La prossima sincronizzazione confronta quindi i due alberi da zero.

### Revisione delle modifiche

Il componente aggiuntivo confronta i database locale e remoto e mostra le azioni che propone di eseguire, raggruppate in base a quale database modificano:

```
▾ Cambierà su questo computer (7 oggetti)
    ▾ Aggiungi 3 oggetti
        Persona   John Smith        I0123
    ▾ Aggiorna 4 oggetti
        …
▾ Cambierà sul server (5 oggetti)
    …
```

Ogni riga nomina l'oggetto, così puoi capire chi o cosa è interessato piuttosto che vedere solo un ID di Gramps. Se qualcosa verrà eliminato, una nota sopra l'elenco indica quanti oggetti e da quale lato.

Premi **Applica** per eseguire quanto descritto nell'elenco.

La finestra di sincronizzazione non blocca il resto di Gramps, quindi puoi continuare a lavorare mentre l'elenco è aperto. Se nel frattempo modifichi un oggetto interessato, il componente aggiuntivo se ne accorge quando premi Applica, si ferma senza modificare nulla e ti chiede di confrontare di nuovo.

#### Modalità di sincronizzazione

La modalità di sincronizzazione è selezionata sopra l'elenco delle modifiche. Cambiarla ricostruisce l'elenco, poiché la modalità decide cosa diventa ciascuna differenza.

- **Sincronizzazione bidirezionale** (predefinita) – le modifiche da entrambi i lati sono combinate. Gli oggetti modificati in entrambi i luoghi vengono uniti.
- **Ripristina il server per corrispondere a questo computer** – il server viene fatto corrispondere a questo computer. Qualsiasi cosa cambiata solo sul server viene scartata.
- **Ripristina questo computer per corrispondere al server** – questo computer viene fatto corrispondere al server. Qualsiasi cosa cambiata solo qui viene scartata.

La modalità **unione** disponibile nelle versioni precedenti alla 1.5 è stata rimossa. Si differenziava dalla sincronizzazione bidirezionale solo nel ripristinare oggetti eliminati da un lato invece di propagare l'eliminazione. Se ti affidavi a essa, utilizza la sincronizzazione bidirezionale e ripristina qualsiasi cosa tu voglia mantenere da un backup.

### File multimediali

I file multimediali vengono gestiti come parte della stessa conferma, non come un passaggio separato. Se ci sono file da trasferire, una casella di controllo sotto l'elenco offre di spostarli:

```
[x] Trasferisci anche 12 file multimediali (4 da scaricare, 8 da caricare)
```

Deselezionala per sincronizzare le modifiche agli oggetti senza toccare i file.

I file che mancano su *entrambi* i lati sono elencati separatamente, poiché non si può fare nulla al riguardo:

```
2 file multimediali mancano su entrambi i lati e non possono essere trasferiti.
```

La sincronizzazione dei file multimediali ha due limitazioni:

- Se un file locale ha un checksum diverso da quello memorizzato nel database di Gramps (questo può accadere ad esempio per i file Word modificati dopo essere stati aggiunti a Gramps), il caricamento fallirà con un messaggio di errore.
- Lo strumento non verifica l'integrità di tutti i file locali. Se un file esiste sotto il percorso memorizzato per l'oggetto multimediale ma differisce dal file sul server, lo strumento non lo rileverà. Usa il componente aggiuntivo Media Verify per trovare file con checksum errati.

### Se una sincronizzazione fallisce

Se una sincronizzazione fallisce a metà strada – ad esempio, a causa di una connessione interrotta – il componente aggiuntivo riporta ciò che era già stato applicato e offre **Riprovare**, che riprende dal passaggio che è fallito piuttosto che ricominciare. La copia scaricata dell'albero remoto viene mantenuta, quindi riprovare non scarica e confronta di nuovo.

Dettagli tecnici del fallimento sono disponibili dietro un espansore *Dettagli*, con un pulsante per copiarli per un rapporto di bug.

## Risoluzione dei problemi

**Modifiche inaspettate.** Se il componente aggiuntivo propone un numero allarmante di eliminazioni, controlla prima la striscia superiore: nomina l'albero genealogico sul server a cui stai per scrivere. Sincronizzare un albero contro un server che contiene un albero *diverso* produce esattamente questo sintomo.

Altrimenti, differenze che non ti aspettavi possono derivare da incoerenze in uno dei database, o da orologi che non sono sincronizzati tra il tuo computer e il tuo server. Controlla che entrambi gli orologi siano impostati correttamente (il fuso orario non importa, poiché lo strumento utilizza timestamp Unix) ed esegui lo strumento di controllo e riparazione sul tuo database locale. Come ultima risorsa, esporta il tuo database locale in XML di Gramps e reimportalo in un nuovo database vuoto. Questa è un'operazione senza perdita di dati, ma garantisce che tutti i dati siano memorizzati in modo coerente.

**Errori nei file multimediali.** Un caricamento fallito è spesso causato da una discrepanza tra il checksum del file su disco e il checksum nel database locale di Gramps, che si verifica con file modificabili come documenti di ufficio modificati al di fuori di Gramps. Usa il componente aggiuntivo Gramps Media Verify per correggere i checksum.

**Errori di autorizzazione.** Controlla il ruolo del tuo account utente di Gramps Web: solo editor, proprietari e amministratori possono applicare modifiche al database remoto.

### Chiedi aiuto

Se nessuna delle informazioni sopra ti aiuta, chiedi alla comunità pubblicando nella [categoria Gramps Web del forum di Gramps](https://gramps.discourse.group/c/gramps-web/28). Si prega di fornire:

- la versione del componente aggiuntivo Gramps Web Sync, mostrata in fondo alla finestra di sincronizzazione accanto alla versione dell'API Web del server (e si prega di utilizzare l'ultima versione rilasciata)
- la versione di Gramps desktop che stai utilizzando
- le informazioni sulla versione di Gramps Web, trovate sotto *Impostazioni ▸ Informazioni sulla versione*
- eventuali dettagli sulla tua installazione di Gramps Web (self-hosted, Grampshub, ...)
- l'output dei log del server di Gramps Web, se hai accesso a essi (quando usi Docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

Se ti viene chiesto un log di debug, avvia Gramps [dalla riga di comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con il logging di debug abilitato e riproduci il problema:

```bash
gramps --debug grampswebsync
```

## Contesto: come funziona il componente aggiuntivo

Il componente aggiuntivo è progettato per mantenere un database locale di Gramps in sincronizzazione con un database remoto di Gramps Web, consentendo sia modifiche locali che remote (editing collaborativo).

Non è **adatto**

- per sincronizzare con un database che non è un derivato diretto (partendo da una copia del database o da un'esportazione/importazione XML di Gramps) del database locale,
- per unire due database con un gran numero di modifiche da entrambi i lati che necessitano di attenzione manuale per l'unione. Usa l'ottimo [Strumento di Importazione e Unione](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) a questo scopo.

I principi di funzionamento sono semplici:

- Confronta i database locale e remoto.
- Se ci sono differenze, controlla il timestamp dell'ultimo oggetto identico, chiamiamolo **t**.
- Se un oggetto è cambiato più recentemente di **t** esiste in un database ma non nell'altro, viene sincronizzato in entrambi (si assume un oggetto nuovo).
- Se un oggetto è cambiato l'ultima volta prima di **t** è assente in un database, viene eliminato in entrambi (si assume un oggetto eliminato).
- Se un oggetto è diverso ma è cambiato dopo **t** solo in un database, sincronizzalo con l'altro (si assume un oggetto modificato).
- Se un oggetto è diverso ma è cambiato dopo **t** in entrambi i database, uniscili (si assume una modifica conflittuale).

Il tempo dell'ultima sincronizzazione riuscita è anche registrato, separatamente per ogni server, e utilizzato come **t** quando è più recente dell'oggetto identico più recente.

Questo algoritmo è semplice e robusto poiché non richiede di tenere traccia della cronologia di sincronizzazione. Tuttavia, funziona meglio quando *sincronizzi spesso*.
