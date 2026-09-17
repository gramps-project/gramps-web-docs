# Configurazione del Server

Utilizzando l'immagine Docker predefinita, tutta la configurazione necessaria può essere effettuata dal browser. Tuttavia, a seconda del deployment, potrebbe essere necessario personalizzare la configurazione del server.

Questa pagina elenca tutti i metodi per modificare la configurazione e tutte le opzioni di configurazione esistenti.


## File di configurazione vs. variabili d'ambiente

Per le impostazioni, puoi utilizzare un file di configurazione o variabili d'ambiente.

Quando utilizzi la [configurazione basata su Docker Compose](deployment.md), puoi includere un file di configurazione aggiungendo il seguente elemento nell'elenco sotto la chiave `volumes:` nel blocco `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
dove `/path/to/config.cfg` è il percorso del file di configurazione nel file system del tuo server (il lato destro si riferisce al percorso nel contenitore e non deve essere modificato).

Quando utilizzi variabili d'ambiente,

- prefissa ogni nome di impostazione con `GRAMPSWEB_` per ottenere il nome della variabile d'ambiente
- Usa doppi underscore per le impostazioni dei dizionari annidati, ad esempio `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` imposterà il valore dell'opzione di configurazione `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Nota che le opzioni di configurazione impostate tramite l'ambiente hanno la precedenza su quelle nel file di configurazione. Se entrambe sono presenti, la variabile d'ambiente "vince".

!!! warning "Le variabili d'ambiente senza prefisso sono deprecate"
    Per motivi storici, un numero limitato di impostazioni – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, e `STATIC_PATH` – possono ancora essere impostate tramite una variabile d'ambiente *senza* il prefisso `GRAMPSWEB_`. Questo è deprecato, genera un avviso all'avvio e smetterà di funzionare in una futura versione. Usa sempre la forma con prefisso, ad esempio `GRAMPSWEB_TREE` invece di `TREE`.

    Nota che questo riguarda solo le variabili d'ambiente. In un file di configurazione, i nomi delle impostazioni sono sempre utilizzati senza prefisso.

!!! tip "Controllo delle opzioni deprecate"
    Le opzioni di configurazione deprecate di cui il tuo server si basa ancora – come le variabili d'ambiente senza prefisso, `SEARCH_INDEX_DIR`, o `EMAIL_USE_TLS` – vengono registrate come avvisi all'avvio. Dalla Gramps Web API 3.22, vengono anche elencate, insieme al loro sostituto e alla versione in cui il supporto sarà rimosso, nella parte superiore della pagina **Informazioni di Sistema** (accessibile tramite l'icona utente nella barra dell'app in alto) quando sei connesso come amministratore.

## Impostazioni di configurazione esistenti
Le seguenti opzioni di configurazione esistono.

### Impostazioni richieste

Chiave | Descrizione
----|-------------
`TREE` | Il nome del database dell'albero genealogico da utilizzare. Mostra gli alberi disponibili con `gramps -l`. Se un albero con questo nome non esiste, ne verrà creato uno nuovo vuoto.
`SECRET_KEY` | La chiave segreta per Flask. Il segreto non deve essere condiviso pubblicamente. Cambiarlo invaliderà tutti i token di accesso.
`USER_DB_URI` | L'URL del database del database utenti. È consentito qualsiasi URL compatibile con SQLAlchemy.

!!! info
    Puoi generare una chiave segreta sicura ad esempio con il comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Impostazioni opzionali

Chiave | Descrizione
----|-------------
`MEDIA_BASE_DIR` | Percorso da utilizzare come directory base per i file multimediali, sovrascrivendo la directory base dei media impostata in Gramps. Quando si utilizza [S3](s3.md), deve avere la forma `s3://<bucket_name>`
`TREE_ID` | Il nome della directory del database dell'albero genealogico da utilizzare in modalità singolo albero (quando `TREE` non è impostato su `*`). Quando impostato, il server identifica l'albero dal suo nome di directory piuttosto che dal suo nome di visualizzazione, il che è più robusto rispetto ai rinomini. Richiesto se desideri rinominare l'albero tramite l'API. Il nome della directory può essere trovato tramite `GET /api/trees/-` (il campo `id`).
`SEARCH_INDEX_DB_URI` | URL del database per l'indice di ricerca. Solo `sqlite` o `postgresql` sono consentiti come backend. Di default è `sqlite:///indexdir/search_index.db`, creando un file SQLite nella cartella `indexdir` relativa al percorso in cui viene eseguito lo script.
`SEARCH_INDEX_DIR` | **Deprecato** (usa `SEARCH_INDEX_DB_URI` invece). Directory contenente l'indice di ricerca. Se impostato mentre `SEARCH_INDEX_DB_URI` è non impostato, l'URL dell'indice di ricerca è derivato come `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Percorso per servire file statici (ad esempio, un frontend web statico)
`BASE_URL` | URL di base dove l'API può essere raggiunta (ad esempio, `https://mygramps.mydomain.com/`). Questo è necessario ad esempio per costruire link corretti per il ripristino della password.
`CORS_ORIGINS` | Origini da cui sono consentite le richieste CORS. Per impostazione predefinita, tutte sono vietate. Usa `"*"` per consentire richieste da qualsiasi dominio.
`EMAIL_HOST` | Host del server SMTP (ad esempio, per inviare e-mail di ripristino della password)
`EMAIL_PORT` | Porta del server SMTP. di default è 465
`EMAIL_HOST_USER` | Nome utente del server SMTP
`EMAIL_HOST_PASSWORD` | Password del server SMTP
`EMAIL_USE_TLS` | **Deprecato** (usa `EMAIL_USE_SSL` o `EMAIL_USE_STARTTLS` invece). Booleano, se utilizzare TLS per l'invio di e-mail. Di default è `True`. Quando si utilizza STARTTLS, impostalo su `False` e utilizza una porta diversa da 25.
`EMAIL_USE_SSL` | Booleano, se utilizzare SSL/TLS implicito per SMTP (v3.6.0+). Di default è `True` se `EMAIL_USE_TLS` non è esplicitamente impostato. Tipicamente utilizzato con la porta 465.
`EMAIL_USE_STARTTLS` | Booleano, se utilizzare STARTTLS esplicito per SMTP (v3.6.0+). Di default è `False`. Tipicamente utilizzato con la porta 587 o 25.
`DEFAULT_FROM_EMAIL` | Indirizzo "Da" per e-mail automatiche
`THUMBNAIL_CACHE_CONFIG` | Dizionario con impostazioni per la cache delle miniature. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`REQUEST_CACHE_CONFIG` | Dizionario con impostazioni per la cache delle richieste. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`PERSISTENT_CACHE_CONFIG` | Dizionario con impostazioni per la cache persistente, utilizzata ad esempio per la telemetria. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`CELERY_CONFIG` | Impostazioni per la coda di attività in background Celery. Vedi [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) per le impostazioni possibili.
`REPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dei report di Gramps
`EXPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dell'esportazione del database di Gramps
`REGISTRATION_DISABLED` | Se `True`, vieta la registrazione di nuovi utenti (di default `False`)
`DISABLE_TELEMETRY` | Se `True`, disabilita la telemetria delle statistiche (di default `False`). Vedi [telemetria](telemetry.md) per dettagli.
`PILLOW_MAX_IMAGE_PIXELS` | Imposta il parametro PIL.Image.MAX_IMAGE_PIXELS, che indica il numero di pixel che l'immagine elaborata può contenere. Vedi [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) per dettagli.
`MAX_THUMBNAIL_FILE_BYTES` | Imposta una dimensione massima di file rigida per le miniature. Di default è `50 * 1024 * 1024` (50 MB). Aumentarla può aumentare notevolmente l'uso della memoria e può portare a crash per esaurimento della memoria o perdita di dati se file di grandi dimensioni vengono decompressi in memoria.


!!! info
    Quando si utilizzano variabili d'ambiente per la configurazione, le opzioni booleane come `EMAIL_USE_SSL` devono essere o la stringa `true` o `false` (case sensitive!).


### Impostazioni per database PostgreSQL

Queste impostazioni sono richieste se i tuoi alberi genealogici sono ospitati in un [database PostgreSQL](postgres.md) utilizzando l'addon SharedPostgreSQL.

Chiave | Descrizione
----|-------------
`POSTGRES_USER` | Il nome utente per la connessione al database
`POSTGRES_PASSWORD` | La password per l'utente del database


### Impostazioni rilevanti per l'hosting di più alberi

Le seguenti impostazioni sono rilevanti quando [si ospitano più alberi](multi-tree.md).


Chiave | Descrizione
----|-------------
`MEDIA_PREFIX_TREE` | Booleano, se utilizzare o meno una sottodirectory separata per i file multimediali di ciascun albero. Di default è `False`, ma si consiglia vivamente di utilizzare `True` in una configurazione multi-albero
`NEW_DB_BACKEND` | Il backend del database da utilizzare per i nuovi alberi genealogici creati. Deve essere uno tra `sqlite` o `sharedpostgresql`. Di default è `sqlite`. Il valore `postgresql` è ancora accettato ma deprecato, poiché il backend PostgreSQL sarà rimosso in una futura versione.
`POSTGRES_HOST` | Il nome host del server PostgreSQL utilizzato per creare nuovi alberi quando si utilizza una configurazione multi-albero con il backend SharedPostgreSQL
`POSTGRES_PORT` | La porta del server PostgreSQL utilizzata per creare nuovi alberi quando si utilizza una configurazione multi-albero con il backend SharedPostgreSQL


### Impostazioni per l'autenticazione OIDC

Queste impostazioni sono necessarie se desideri utilizzare l'autenticazione OpenID Connect (OIDC) con fornitori esterni. Per istruzioni dettagliate sulla configurazione e esempi, vedere [Autenticazione OIDC](oidc.md).

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Booleano, se abilitare l'autenticazione OIDC. Di default è `False`.
`OIDC_ISSUER` | URL dell'emittente del fornitore OIDC (per fornitori OIDC personalizzati)
`OIDC_CLIENT_ID` | ID client OAuth (per fornitori OIDC personalizzati)
`OIDC_CLIENT_SECRET` | Segreto client OAuth (per fornitori OIDC personalizzati)
`OIDC_NAME` | Nome di visualizzazione personalizzato per il fornitore. Di default è "OIDC"
`OIDC_SCOPES` | Scopi OAuth. Di default è "openid email profile"
`OIDC_USERNAME_CLAIM` | Il claim da utilizzare per il nome utente. Di default è "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Facoltativo: URL per il punto di configurazione OpenID Connect (se non si utilizza il standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano, se disabilitare l'autenticazione locale con nome utente/password. Di default è `False`
`OIDC_AUTO_REDIRECT` | Booleano, se reindirizzare automaticamente a OIDC quando è configurato solo un fornitore. Di default è `False`

#### Fornitori OIDC integrati

Per i fornitori integrati (Google, Microsoft), utilizza queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client per Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Segreto client per Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID client per Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Segreto client per Microsoft OAuth

#### Mappatura dei ruoli OIDC

Queste impostazioni ti consentono di mappare i gruppi/ruoli OIDC dal tuo fornitore di identità ai ruoli utente di Gramps Web:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Di default è "groups"
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Admin" di Gramps
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Owner" di Gramps
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Editor" di Gramps
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Contributor" di Gramps
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Member" di Gramps
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Guest" di Gramps

### Impostazioni solo per funzionalità AI

Queste impostazioni sono necessarie se desideri utilizzare funzionalità potenziate dall'AI come chat o ricerca semantica.

Chiave | Descrizione
----|-------------
`LLM_BASE_URL` | URL di base per l'API chat compatibile con OpenAI. Di default è `None`, che utilizza l'API OpenAI.
`LLM_MODEL` | Il modello da utilizzare per l'API chat compatibile con OpenAI. Se non impostato (il predefinito), la chat è disabilitata. A partire dalla v3.6.0, l'assistente AI utilizza Pydantic AI con capacità di chiamata degli strumenti.
`VECTOR_EMBEDDING_MODEL` | Il modello da utilizzare per le embedding vettoriali di ricerca semantica. Quando si utilizza un modello locale, questo deve essere un nome di modello [Sentence Transformers](https://sbert.net/). Quando si utilizza un'API remota (vedi `VECTOR_EMBEDDING_BASE_URL`), questo è il nome del modello passato al fornitore remoto. Se non impostato (il predefinito), la ricerca semantica e la chat sono disabilitate.
`VECTOR_EMBEDDING_BASE_URL` | URL di base per un'API di embedding compatibile con OpenAI remota (ad esempio, Ollama, OpenAI, LiteLLM). Se non impostato (il predefinito), viene utilizzato un modello locale di Sentence Transformers. Vedi [Utilizzo di un'API di embedding remota](chat.md#using-a-remote-embedding-api) per dettagli.
`VECTOR_EMBEDDING_API_KEY` | Chiave API per fornitori di embedding remoti autenticati. Necessaria solo quando `VECTOR_EMBEDDING_BASE_URL` è impostato e il fornitore richiede autenticazione.
`LLM_MAX_CONTEXT_LENGTH` | Limite di caratteri per il contesto dell'albero genealogico fornito al LLM. Di default è 50000.
`LLM_SYSTEM_PROMPT` | Prompt di sistema personalizzato per l'assistente chat LLM (v3.6.0+). Se non impostato, utilizza il prompt ottimizzato per la genealogia predefinito.


## Esempio di file di configurazione

Un file di configurazione minimale per la produzione potrebbe apparire così:
```python
TREE="Il Mio Albero Genealogico"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Usa SSL implicito per la porta 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # la tua password SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
