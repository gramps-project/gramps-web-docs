# Configurazione del Server

Utilizzando l'immagine Docker predefinita, tutta la configurazione necessaria può essere effettuata dal browser. Tuttavia, a seconda del deployment, potrebbe essere necessario personalizzare la configurazione del server.

Questa pagina elenca tutti i metodi per modificare la configurazione e tutte le opzioni di configurazione esistenti.

## File di configurazione vs. variabili d'ambiente

Per le impostazioni, puoi utilizzare un file di configurazione o variabili d'ambiente.

Quando utilizzi la [configurazione basata su Docker Compose](deployment.md), puoi includere un file di configurazione aggiungendo il seguente elemento alla lista sotto la chiave `volumes:` nel blocco `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
dove `/path/to/config.cfg` è il percorso del file di configurazione nel file system del tuo server (il lato destro si riferisce al percorso nel contenitore e non deve essere modificato).

Quando utilizzi variabili d'ambiente,

- prefissa ogni nome di impostazione con `GRAMPSWEB_` per ottenere il nome della variabile d'ambiente
- Usa doppi underscore per le impostazioni dei dizionari annidati, ad esempio `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` imposterà il valore dell'opzione di configurazione `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Nota che le opzioni di configurazione impostate tramite l'ambiente hanno la precedenza su quelle nel file di configurazione. Se entrambe sono presenti, la variabile d'ambiente "vince".

## Impostazioni di configurazione esistenti
Le seguenti opzioni di configurazione esistono.

### Impostazioni richieste

Chiave | Descrizione
----|-------------
`TREE` | Il nome del database dell'albero genealogico da utilizzare. Mostra gli alberi disponibili con `gramps -l`. Se un albero con questo nome non esiste, ne verrà creato uno nuovo vuoto.
`SECRET_KEY` | La chiave segreta per Flask. La chiave segreta non deve essere condivisa pubblicamente. Modificarla invaliderà tutti i token di accesso.
`USER_DB_URI` | L'URL del database degli utenti. È consentito qualsiasi URL compatibile con SQLAlchemy.

!!! info
    Puoi generare una chiave segreta sicura ad esempio con il comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Impostazioni opzionali

Chiave | Descrizione
----|-------------
`MEDIA_BASE_DIR` | Percorso da utilizzare come directory principale per i file multimediali, sovrascrivendo la directory principale dei media impostata in Gramps. Quando si utilizza [S3](s3.md), deve avere la forma `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | URL del database per l'indice di ricerca. Solo `sqlite` o `postgresql` sono consentiti come backend. Predefinito a `sqlite:///indexdir/search_index.db`, creando un file SQLite nella cartella `indexdir` relativa al percorso in cui viene eseguito lo script
`STATIC_PATH` | Percorso da cui servire file statici (ad esempio, un frontend web statico)
`BASE_URL` | URL di base dove l'API può essere raggiunta (ad esempio, `https://mygramps.mydomain.com/`). Questo è necessario ad esempio per costruire link corretti per il reset della password
`CORS_ORIGINS` | Origini da cui sono consentite le richieste CORS. Per impostazione predefinita, tutte sono vietate. Usa `"*"` per consentire richieste da qualsiasi dominio.
`EMAIL_HOST` | Host del server SMTP (ad esempio, per inviare e-mail di reset della password)
`EMAIL_PORT` | Porta del server SMTP. predefinito a 465
`EMAIL_HOST_USER` | Nome utente del server SMTP
`EMAIL_HOST_PASSWORD` | Password del server SMTP
`EMAIL_USE_TLS` | Booleano, se utilizzare TLS per inviare e-mail. Predefinito a `True`. Quando si utilizza STARTTLS, impostalo su `False` e utilizza una porta diversa da 25.
`DEFAULT_FROM_EMAIL` | Indirizzo "Da" per e-mail automatiche
`THUMBNAIL_CACHE_CONFIG` | Dizionario con impostazioni per la cache delle miniature. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`REQUEST_CACHE_CONFIG` | Dizionario con impostazioni per la cache delle richieste. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`PERSISTENT_CACHE_CONFIG` | Dizionario con impostazioni per la cache persistente, utilizzata ad esempio per la telemetria. Vedi [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) per le impostazioni possibili.
`CELERY_CONFIG` | Impostazioni per la coda di attività in background Celery. Vedi [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) per le impostazioni possibili.
`REPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dell'esecuzione dei report di Gramps
`EXPORT_DIR` | Directory temporanea in cui verrà memorizzato l'output dell'esportazione del database di Gramps
`REGISTRATION_DISABLED` | Se `True`, vieta la registrazione di nuovi utenti (predefinito `False`)
`DISABLE_TELEMETRY` | Se `True`, disabilita la telemetria delle statistiche (predefinito `False`). Vedi [telemetria](telemetry.md) per i dettagli.

!!! info
    Quando si utilizzano variabili d'ambiente per la configurazione, le opzioni booleane come `EMAIL_USE_TLS` devono essere o la stringa `true` o `false` (case sensitive!).

### Impostazioni solo per il database backend PostgreSQL

Questo è necessario se hai configurato il tuo database Gramps per funzionare con l'[addon PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Chiave | Descrizione
----|-------------
`POSTGRES_USER` | Il nome utente per la connessione al database
`POSTGRES_PASSWORD` | La password per l'utente del database

### Impostazioni rilevanti per l'hosting di più alberi

Le seguenti impostazioni sono rilevanti quando [si ospitano più alberi](multi-tree.md).

Chiave | Descrizione
----|-------------
`MEDIA_PREFIX_TREE` | Booleano, se utilizzare o meno una sottocartella separata per i file multimediali di ciascun albero. Predefinito a `False`, ma si raccomanda fortemente di utilizzare `True` in un'installazione multi-albero
`NEW_DB_BACKEND` | Il backend del database da utilizzare per i nuovi alberi genealogici creati. Deve essere uno tra `sqlite`, `postgresql` o `sharedpostgresql`. Predefinito a `sqlite`.
`POSTGRES_HOST` | Il nome host del server PostgreSQL utilizzato per creare nuovi alberi quando si utilizza un'installazione multi-albero con il backend SharedPostgreSQL
`POSTGRES_PORT` | La porta del server PostgreSQL utilizzato per creare nuovi alberi quando si utilizza un'installazione multi-albero con il backend SharedPostgreSQL

### Impostazioni per l'autenticazione OIDC

Queste impostazioni sono necessarie se desideri utilizzare l'autenticazione OpenID Connect (OIDC) con fornitori esterni. Per istruzioni dettagliate sulla configurazione e esempi, vedi [Autenticazione OIDC](oidc.md).

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Booleano, se abilitare l'autenticazione OIDC. Predefinito a `False`.
`OIDC_ISSUER` | URL dell'emittente del fornitore OIDC (per fornitori OIDC personalizzati)
`OIDC_CLIENT_ID` | ID client OAuth (per fornitori OIDC personalizzati)
`OIDC_CLIENT_SECRET` | Segreto client OAuth (per fornitori OIDC personalizzati)
`OIDC_NAME` | Nome visualizzato personalizzato per il fornitore. Predefinito a "OIDC"
`OIDC_SCOPES` | Scopi OAuth. Predefinito a "openid email profile"
`OIDC_USERNAME_CLAIM` | Il claim da utilizzare per il nome utente. Predefinito a "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Facoltativo: URL per il punto di configurazione OpenID Connect (se non si utilizza il standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano, se disabilitare l'autenticazione locale con nome utente/password. Predefinito a `False`
`OIDC_AUTO_REDIRECT` | Booleano, se reindirizzare automaticamente a OIDC quando è configurato solo un fornitore. Predefinito a `False`

#### Fornitori OIDC integrati

Per i fornitori integrati (Google, Microsoft, GitHub), utilizza queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client per Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Segreto client per Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID client per Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Segreto client per Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | ID client per GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Segreto client per GitHub OAuth

#### Mappatura dei Ruoli OIDC

Queste impostazioni ti consentono di mappare i gruppi/ruoli OIDC dal tuo fornitore di identità ai ruoli utente di Gramps Web:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Predefinito a "groups"
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Admin" di Gramps
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Owner" di Gramps
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Editor" di Gramps
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Contributor" di Gramps
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Member" di Gramps
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Guest" di Gramps

### Impostazioni solo per funzionalità AI

Queste impostazioni sono necessarie se desideri utilizzare funzionalità potenziate dall'IA come chat o ricerca semantica.

Chiave | Descrizione
----|-------------
`LLM_BASE_URL` | URL di base per l'API chat compatibile con OpenAI. Predefinito a `None`, che utilizza l'API OpenAI.
`LLM_MODEL` | Il modello da utilizzare per l'API chat compatibile con OpenAI. Se non impostato (il predefinito), la chat è disabilitata.
`VECTOR_EMBEDDING_MODEL` | Il modello [Sentence Transformers](https://sbert.net/) da utilizzare per le embedding vettoriali di ricerca semantica. Se non impostato (il predefinito), la ricerca semantica e la chat sono disabilitate.
`LLM_MAX_CONTEXT_LENGTH` | Limite di caratteri per il contesto dell'albero genealogico fornito al LLM. Predefinito a 50000.

## Esempio di file di configurazione

Un file di configurazione minimale per la produzione potrebbe apparire così:
```python
TREE="Il Mio Albero Genealogico"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # la tua password SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
