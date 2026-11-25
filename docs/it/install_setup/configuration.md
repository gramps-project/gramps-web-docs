# Configurazione del server

Utilizzando l'immagine Docker predefinita, tutta la configurazione necessaria può essere eseguita dal browser. Tuttavia, a seconda della distribuzione, potrebbe essere necessario personalizzare la configurazione del server.

Questa pagina elenca tutti i metodi per modificare la configurazione e tutte le opzioni di configurazione esistenti.


## File di configurazione e variabili d'ambiente

Per le impostazioni puoi utilizzare un file di configurazione oppure variabili d'ambiente.

Quando utilizzi la [configurazione basata su Docker Compose](deployment.md), puoi includere un file di configurazione aggiungendo il seguente elemento all'elenco sotto la chiave `volumes:` nel blocco `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
dove `/path/to/config.cfg` è il percorso del file di configurazione nel file system del tuo server (il lato destro fa riferimento al percorso nel container e non deve essere modificato).

Quando utilizzi variabili d'ambiente,

- anteponi `GRAMPSWEB_` a ogni nome di impostazione per ottenere il nome della variabile d'ambiente
- usa i doppi underscore per le impostazioni dei dizionari annidati, ad esempio `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` imposterà il valore dell'opzione di configurazione `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Nota che le opzioni di configurazione impostate tramite l'ambiente hanno la precedenza su quelle presenti nel file di configurazione. Se sono presenti entrambe, la variabile d'ambiente "vince".

!!! warning "Le variabili d'ambiente senza prefisso sono deprecate"
    Per motivi storici, alcune impostazioni – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` e `STATIC_PATH` – possono ancora essere impostate tramite una variabile d'ambiente *senza* il prefisso `GRAMPSWEB_`. Questa modalità è deprecata, genera un avviso all'avvio e smetterà di funzionare in una versione futura. Usa sempre la forma con prefisso, ad esempio `GRAMPSWEB_TREE` invece di `TREE`.

    Nota che questo riguarda solo le variabili d'ambiente. In un file di configurazione, i nomi delle impostazioni vengono sempre utilizzati senza prefisso.

!!! tip "Controllare le opzioni deprecate"
    Le opzioni di configurazione deprecate da cui il tuo server dipende ancora – come le variabili d'ambiente senza prefisso, `SEARCH_INDEX_DIR` o `EMAIL_USE_TLS` – vengono registrate come avvisi all'avvio. A partire da Gramps Web API 3.22, sono inoltre elencate, insieme alla relativa sostituzione e alla versione in cui il supporto verrà rimosso, nella parte superiore della pagina **Informazioni di sistema** (accessibile tramite l'icona utente nella barra superiore dell'app) quando hai effettuato l'accesso come amministratore.

    Anche le impostazioni e-mail e l'URL di base che la procedura guidata di primo avvio delle versioni precedenti memorizzava nel database vengono elencati qui. Impostali nella tua configurazione con i valori memorizzati; l'avviso scompare quando coincidono.

## Impostazioni di configurazione esistenti
Sono disponibili le seguenti opzioni di configurazione.

### Impostazioni obbligatorie

Chiave | Descrizione
----|-------------
`TREE` | Il nome del database dell'albero genealogico da utilizzare. Mostra gli alberi disponibili con `gramps -l`. Se non esiste un albero con questo nome, ne verrà creato uno nuovo vuoto.
`SECRET_KEY` | La chiave segreta per Flask. Il segreto non deve essere condiviso pubblicamente. Modificandola, tutti i token di accesso verranno invalidati.
`USER_DB_URI` | L'URL del database degli utenti. È consentito qualsiasi URL compatibile con SQLAlchemy.

!!! info
    Puoi generare una chiave segreta sicura, ad esempio con il comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Impostazioni facoltative

Chiave | Descrizione
----|-------------
`MEDIA_BASE_DIR` | Percorso da utilizzare come directory di base per i file multimediali, sovrascrivendo la directory di base dei file multimediali impostata in Gramps. Quando utilizzi [S3](s3.md), deve avere il formato `s3://<bucket_name>`
`TREE_ID` | Il nome della directory del database dell'albero genealogico da utilizzare in modalità albero singolo (quando `TREE` non è impostato su `*`). Se impostato, il server identifica l'albero tramite il nome della directory anziché tramite il nome visualizzato, una modalità più robusta rispetto alla ridenominazione. Obbligatorio se vuoi rinominare l'albero tramite l'API. Il nome della directory può essere trovato tramite `GET /api/trees/-` (il campo `id`).
`SEARCH_INDEX_DB_URI` | URL del database per l'indice di ricerca. Come backend sono consentiti solo `sqlite` o `postgresql`. Il valore predefinito è `sqlite:///indexdir/search_index.db`, che crea un file SQLite nella cartella `indexdir` relativa al percorso da cui viene eseguito lo script
`SEARCH_INDEX_DIR` | **Deprecato** (usa invece `SEARCH_INDEX_DB_URI`). Directory contenente l'indice di ricerca. Se impostata mentre `SEARCH_INDEX_DB_URI` non è impostato, l'URL dell'indice di ricerca viene derivato come `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Percorso da cui distribuire i file statici (ad esempio un frontend web statico)
`BASE_URL` | URL di base a cui è possibile raggiungere l'API (ad esempio `https://mygramps.mydomain.com/`). È necessario, ad esempio, per creare correttamente i link di reimpostazione della password. Web Push richiede inoltre un URL HTTPS accessibile pubblicamente; il valore predefinito `http://localhost/` disabilita Web Push. Quando configuri questa impostazione tramite l'ambiente, usa `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Origini da cui sono consentite le richieste CORS. Per impostazione predefinita, tutte sono vietate. Usa `"*"` per consentire richieste da qualsiasi dominio.
`EMAIL_HOST` | Host del server SMTP (ad esempio per l'invio di e-mail di reimpostazione della password)
`EMAIL_PORT` | Porta del server SMTP. Il valore predefinito è 465
`EMAIL_HOST_USER` | Nome utente del server SMTP
`EMAIL_HOST_PASSWORD` | Password del server SMTP
`EMAIL_USE_TLS` | **Deprecato** (usa invece `EMAIL_USE_SSL` o `EMAIL_USE_STARTTLS`). Valore booleano che indica se utilizzare TLS per l'invio delle e-mail. Il valore predefinito è `True`. Quando utilizzi STARTTLS, imposta questo valore su `False` e usa una porta diversa da 25.
`EMAIL_USE_SSL` | Valore booleano che indica se utilizzare SSL/TLS implicito per SMTP (v3.6.0+). Il valore predefinito è `True` se `EMAIL_USE_TLS` non è impostato esplicitamente. Generalmente utilizzato con la porta 465.
`EMAIL_USE_STARTTLS` | Valore booleano che indica se utilizzare STARTTLS esplicito per SMTP (v3.6.0+). Il valore predefinito è `False`. Generalmente utilizzato con la porta 587 o 25.
`DEFAULT_FROM_EMAIL` | Indirizzo "Da" per le e-mail automatiche
`THUMBNAIL_CACHE_CONFIG` | Dizionario con le impostazioni per la cache delle miniature. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni disponibili.
`REQUEST_CACHE_CONFIG` | Dizionario con le impostazioni per la cache delle richieste. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni disponibili.
`PERSISTENT_CACHE_CONFIG` | Dizionario con le impostazioni per la cache persistente, utilizzata ad esempio per la telemetria. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni disponibili.
`CELERY_CONFIG` | Impostazioni per la coda di attività in background Celery. Consulta [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) per le impostazioni disponibili.
`REPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dei report Gramps eseguiti
`EXPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dell'esportazione del database Gramps
`BACKUP_DIR` | Directory in cui vengono memorizzati i [backup](../administration/backups.md), in una sottodirectory per ogni albero (v3.24.0+). Se non impostata (valore predefinito), i backup non possono essere memorizzati sul server, ma possono comunque essere ripristinati da un file caricato. Usa una posizione persistente, ad esempio un volume Docker, e preferibilmente una posizione a sua volta sottoposta a backup o sincronizzata altrove.
`BACKUP_KEEP` | Numero di backup memorizzati da conservare per ogni albero; quelli più vecchi vengono eliminati quando viene creato un nuovo backup (v3.24.0+). Il valore predefinito è `5`
`RATE_LIMIT_BACKUP` | Limite di frequenza per la creazione dei backup, per albero (v3.24.0+). Il valore predefinito è `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Limite di frequenza per la creazione degli archivi multimediali nella pagina Esporta. Il valore predefinito è `"1 per hour"`
`REGISTRATION_DISABLED` | Se `True`, impedisce la registrazione di nuovi utenti (valore predefinito `False`). A partire da Gramps Web API 3.26, la pagina di accesso nasconde anche il relativo link di registrazione.
`PROXY_FIX_X_FOR` | Numero di proxy inversi attendibili davanti a Gramps Web (v3.26.0+). Impostalo su `1` quando ti trovi dietro un singolo proxy inverso, in modo che i limiti di frequenza si applichino per client anziché complessivamente a tutti gli utenti. Il valore predefinito è `0`. Impostalo solo se il server è raggiungibile esclusivamente tramite questi proxy.
`DISABLE_TELEMETRY` | Se `True`, disabilita la telemetria delle statistiche (valore predefinito `False`). Per i dettagli, consulta la [telemetria](telemetry.md).
`PILLOW_MAX_IMAGE_PIXELS` | Imposta il parametro PIL.Image.MAX_IMAGE_PIXELS, che indica il numero di pixel che può contenere l'immagine elaborata. Per i dettagli, consulta la [documentazione](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS).
`MAX_THUMBNAIL_FILE_BYTES` | Imposta una dimensione massima rigida per i file delle miniature. Il valore predefinito è `50 * 1024 * 1024` (50 MB). Aumentarlo può incrementare notevolmente l'utilizzo della memoria e causare arresti anomali per esaurimento della memoria o perdita di dati se file di grandi dimensioni vengono decompressi in memoria.


!!! info
    Quando utilizzi variabili d'ambiente per la configurazione, le opzioni booleane come `EMAIL_USE_SSL` devono essere esattamente la stringa `true` o `false` (con distinzione tra maiuscole e minuscole!).


### Impostazioni per i database PostgreSQL

Queste impostazioni sono obbligatorie se i tuoi alberi genealogici sono ospitati in un [database PostgreSQL](postgres.md) utilizzando l'addon SharedPostgreSQL.

Chiave | Descrizione
----|-------------
`POSTGRES_USER` | Il nome utente per la connessione al database
`POSTGRES_PASSWORD` | La password dell'utente del database


### Impostazioni rilevanti per l'hosting di più alberi

Le seguenti impostazioni sono rilevanti quando [ospiti più alberi](multi-tree.md).


Chiave | Descrizione
----|-------------
`MEDIA_PREFIX_TREE` | Valore booleano che indica se utilizzare o meno una sottocartella separata per i file multimediali di ogni albero. Il valore predefinito è `False`, ma in una configurazione con più alberi si consiglia vivamente di utilizzare `True`
`NEW_DB_BACKEND` | Il backend del database da utilizzare per gli alberi genealogici appena creati. Deve essere `sqlite` o `sharedpostgresql`. Il valore predefinito è `sqlite`. Il valore `postgresql` è ancora accettato, ma è deprecato, poiché il backend PostgreSQL verrà rimosso in Gramps Web API 4.0.
`POSTGRES_HOST` | Il nome host del server PostgreSQL utilizzato per creare nuovi alberi quando utilizzi una configurazione con più alberi e il backend SharedPostgreSQL
`POSTGRES_PORT` | La porta del server PostgreSQL utilizzata per creare nuovi alberi quando utilizzi una configurazione con più alberi e il backend SharedPostgreSQL


### Impostazioni per l'autenticazione OIDC

Queste impostazioni sono necessarie se vuoi utilizzare l'autenticazione OpenID Connect (OIDC) con provider esterni. Per istruzioni dettagliate sulla configurazione ed esempi, consulta [Autenticazione OIDC](oidc.md).

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Valore booleano che indica se abilitare l'autenticazione OIDC. Il valore predefinito è `False`.
`OIDC_ISSUER` | URL dell'emittente del provider OIDC (per provider OIDC personalizzati)
`OIDC_CLIENT_ID` | ID client OAuth (per provider OIDC personalizzati)
`OIDC_CLIENT_SECRET` | Segreto client OAuth (per provider OIDC personalizzati)
`OIDC_NAME` | Nome visualizzato personalizzato per il provider. Il valore predefinito è "OIDC"
`OIDC_SCOPES` | Ambiti OAuth. Il valore predefinito è "openid email profile"
`OIDC_USERNAME_CLAIM` | Claim da utilizzare per il nome utente. Il valore predefinito è "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Facoltativo: URL dell'endpoint di configurazione OpenID Connect (se non utilizzi il percorso standard `/.well-known/openid-configuration`)
`OIDC_PKCE` | Valore booleano che indica se utilizzare PKCE. Se non impostato, PKCE viene utilizzato quando il documento di discovery del provider elenca `S256`. Consulta [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Valore booleano che indica se disabilitare l'autenticazione locale tramite nome utente/password. Il valore predefinito è `False`
`OIDC_AUTO_REDIRECT` | Valore booleano che indica se reindirizzare automaticamente a OIDC quando è configurato un solo provider. Il valore predefinito è `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Elenco di URI `https` presso i quali le app native possono ricevere il risultato dell'accesso (v3.26.0+), impostato come elenco JSON in una variabile d'ambiente. Vuoto per impostazione predefinita. Necessario solo se richiesto dalla documentazione di un'app nativa. Consulta [App native](oidc.md#native-apps)

#### Provider OIDC integrati

Per i provider integrati (Google, Microsoft), usa queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client per OAuth Google
`OIDC_GOOGLE_CLIENT_SECRET` | Segreto client per OAuth Google
`OIDC_MICROSOFT_CLIENT_ID` | ID client per OAuth Microsoft
`OIDC_MICROSOFT_CLIENT_SECRET` | Segreto client per OAuth Microsoft
`OIDC_GOOGLE_PKCE` | Impostazione PKCE per Google, consulta [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Impostazione PKCE per Microsoft, consulta [PKCE](oidc.md#pkce)

#### Mappatura dei ruoli OIDC

Queste impostazioni ti consentono di mappare i gruppi/ruoli OIDC del tuo provider di identità ai ruoli utente di Gramps Web:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Il valore predefinito è "groups"
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Admin"
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Owner"
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Editor"
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Contributor"
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Member"
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo del tuo provider OIDC che corrisponde al ruolo Gramps "Guest"

### Impostazioni solo per le funzionalità di IA

Queste impostazioni sono necessarie se vuoi utilizzare la chat IA. Per i dettagli, consulta [Configurazione della chat IA](chat.md).

!!! note
    Le impostazioni `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` e `VECTOR_EMBEDDING_API_KEY` per la ricerca semantica vengono ignorate a partire da Gramps Web API 3.25, che ha rimosso la ricerca semantica. La chat IA richiede solo `LLM_MODEL`.

Chiave | Descrizione
----|-------------
`LLM_BASE_URL` | URL di base per l'API di chat compatibile con OpenAI. Il valore predefinito è `None`, che utilizza l'API OpenAI.
`LLM_MODEL` | Il modello da utilizzare per l'API di chat compatibile con OpenAI. Se non impostato (valore predefinito), la chat è disabilitata. A partire dalla v3.6.0, l'assistente IA utilizza Pydantic AI con funzionalità di chiamata degli strumenti.
`LLM_MAX_OUTPUT_TOKENS` | Numero massimo di token che il modello può generare in una singola risposta. Non impostato per impostazione predefinita, lasciando il limite al server del modello. Utile per i server dei modelli che non dispongono di un proprio limite, dove altrimenti una risposta potrebbe continuare indefinitamente.
`LLM_MAX_CONTEXT_LENGTH` | Limite di caratteri per il contesto dell'albero genealogico fornito al LLM. Il valore predefinito è 50000.
`LLM_SYSTEM_PROMPT` | Prompt di sistema personalizzato per l'assistente della chat LLM (v3.6.0+). Se non impostato, utilizza il prompt predefinito ottimizzato per la genealogia.
`LLM_VISION` | Valore booleano che indica se gli utenti possono allegare immagini alle proprie domande (v3.26.0+). Abilitalo solo se il modello accetta immagini. Il valore predefinito è `False`. Consulta [Immagini nelle domande](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Valore booleano che indica se l'assistente può proporre modifiche all'albero affinché gli utenti le esaminino e le applichino (v3.26.0+). Il valore predefinito è `False`. Consulta [Consentire all'assistente di proporre modifiche](chat.md#letting-the-assistant-propose-changes)


## Esempio di file di configurazione

Un file di configurazione minimo per la produzione potrebbe avere questo aspetto:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
