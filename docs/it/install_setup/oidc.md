# Autenticazione OIDC

Gramps Web supporta l'autenticazione OpenID Connect (OIDC), consentendo agli utenti di accedere utilizzando fornitori di identità esterni. Questo include i fornitori integrati Google e Microsoft, così come fornitori OIDC personalizzati come Keycloak, Authentik e Authelia.

!!! warning "GitHub come fornitore OIDC non è più supportato"
    Se hai impostato `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` da una versione precedente, rimuovili – ora vengono ignorati e gli utenti che in precedenza accedevano tramite GitHub non possono più accedere in questo modo. GitHub è un fornitore OAuth 2.0, non un fornitore OpenID Connect, e non ha mai restituito il claim su cui Gramps Web si basa per l'identità, quindi non è mai stato completamente affidabile.

## Panoramica

L'autenticazione OIDC ti consente di:

- Utilizzare fornitori di identità esterni per l'autenticazione degli utenti
- Supportare più fornitori di autenticazione simultaneamente
- Mappare gruppi/ruoli OIDC ai ruoli utente di Gramps Web
- Implementare Single Sign-On (SSO) e Single Sign-Out
- Disabilitare facoltativamente l'autenticazione locale con nome utente/password

## Configurazione

Per abilitare l'autenticazione OIDC, devi configurare le impostazioni appropriate nel tuo file di configurazione di Gramps Web o nelle variabili di ambiente. Consulta la pagina [Configurazione del Server](configuration.md#settings-for-oidc-authentication) per un elenco completo delle impostazioni OIDC disponibili.

!!! info
    Quando utilizzi le variabili di ambiente, ricorda di anteporre a ciascun nome di impostazione `GRAMPSWEB_` (ad esempio, `GRAMPSWEB_OIDC_ENABLED`). Consulta [File di configurazione vs. variabili di ambiente](configuration.md#configuration-file-vs-environment-variables) per ulteriori dettagli.

### Fornitori Integrati

Gramps Web ha supporto integrato per fornitori di identità popolari. Per utilizzarli, devi solo fornire l'ID client e il segreto client:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`

Puoi configurare più fornitori simultaneamente. Il sistema rileverà automaticamente quali fornitori sono disponibili in base ai valori di configurazione.

!!! tip "Microsoft: distribuzioni single-tenant"
    Il fornitore Microsoft integrato utilizza l'endpoint multi-tenant `/common` e accetta accessi da qualsiasi account Microsoft per design. Se desideri consentire solo agli utenti del tuo tenant, utilizza il [fornitore OIDC personalizzato](#custom-oidc-providers) con l'URL dell'emittente specifico del tuo tenant, il che mantiene attiva la convalida dell'emittente e limita gli accessi a quel tenant.

### Fornitori OIDC Personalizzati

Per fornitori OIDC personalizzati (come Keycloak, Authentik, Authelia, o un tenant Microsoft Entra single-tenant), utilizza queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Booleano, se abilitare l'autenticazione OIDC. Imposta su `True`.
`OIDC_ISSUER` | URL dell'emittente del tuo fornitore. La scoperta viene recuperata da `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID client per il tuo fornitore OIDC
`OIDC_CLIENT_SECRET` | Segreto client per il tuo fornitore OIDC
`OIDC_NAME` | Nome di visualizzazione personalizzato (opzionale, predefinito "OIDC")
`OIDC_SCOPES` | Scopi OAuth (opzionale, predefinito "openid email profile")
`OIDC_USERNAME_CLAIM` | Claim utilizzato per generare il nome utente (opzionale, predefinito "preferred_username")

### Configurazioni Multi-Albero

Su un server multi-albero, l'albero in cui l'utente sta accedendo deve essere noto prima che Gramps Web reindirizzi al fornitore di identità, quindi il login inizia con:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` è richiesto nelle configurazioni multi-albero; ometterlo, o passare l'ID di un albero che non esiste, fallisce il login. Su un server single-tree `tree` è facoltativo, ma se fornito deve corrispondere al `TREE` configurato.

Un'identità OIDC è legata esattamente a un account Gramps Web, che a sua volta appartiene esattamente a un albero – accedere a un albero diverso fallisce piuttosto che spostare l'account. Non c'è modo di collegare un'unica identità presso il fornitore a conti in diversi alberi; gli utenti che necessitano di accesso a più alberi hanno bisogno di identità separate presso il fornitore (ad esempio, nomi utente o account distinti).

!!! warning
    Un account amministratore del sito senza un albero associato (vedi [creazione di un account admin](../administration/owner.md)) non può accedere tramite OIDC, poiché il login OIDC richiede sempre un albero. Tali account devono essere creati e autenticati con un nome utente/password locale.

## URI di Reindirizzamento Richiesti

Quando configuri il tuo fornitore OIDC, devi registrare il seguente URI di reindirizzamento:

**Per fornitori OIDC che supportano i caratteri jolly: (ad esempio, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Dove `*` è un carattere jolly regex. A seconda dell'interprete regex del tuo fornitore, questo potrebbe anche essere un `.*` o simile.
Assicurati che il regex sia abilitato se il tuo fornitore lo richiede (ad esempio, Authentik).

**Per fornitori OIDC che non supportano i caratteri jolly: (ad esempio, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

L'albero non fa mai parte dell'URI di reindirizzamento, anche sui server multi-albero – viaggia separatamente nella sessione, poiché i fornitori richiedono che l'URI di reindirizzamento corrisponda esattamente a quello registrato.

## Mappatura dei Ruoli

Gramps Web può mappare automaticamente gruppi o ruoli OIDC dal tuo fornitore di identità ai ruoli utente di Gramps Web. Questo ti consente di gestire centralmente i permessi degli utenti nel tuo fornitore di identità. La mappatura dei ruoli funziona allo stesso modo per tutti i fornitori, integrati o personalizzati.

### Configurazione

Utilizza queste impostazioni per configurare la mappatura dei ruoli:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Predefinito "groups". I percorsi puntati sono supportati, ad esempio `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Admin" di Gramps
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Owner" di Gramps
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Editor" di Gramps
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Contributor" di Gramps
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Member" di Gramps
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che mappa al ruolo "Guest" di Gramps

### Comportamento della Mappatura dei Ruoli

Se nessuna impostazione `OIDC_GROUP_*` è configurata, la mappatura dei ruoli è disattivata e i ruoli sono gestiti manualmente in Gramps Web; i nuovi account OIDC vengono quindi creati disabilitati e devono essere approvati da un proprietario o amministratore esistente (vedi [Primo Accesso e Bootstrap](#first-login-and-bootstrapping) qui sotto).

Una volta configurata la mappatura dei ruoli, ad ogni accesso:

- Se il claim del ruolo è presente e l'utente appartiene a un gruppo mappato, riceve il ruolo corrispondente.
- Se il claim del ruolo è presente ma l'utente non appartiene a nessun gruppo mappato, il suo ruolo è impostato su disabilitato. Questo è un default fail-closed, non un bug – Gramps Web non può dedurre un ruolo per un gruppo che non riconosce.
- Se il claim del ruolo è assente dal token, il ruolo esistente rimane invariato; un nuovo account continua a essere disabilitato per impostazione predefinita.

!!! warning "Google non invia un claim di gruppi"
    I token di Google non includono mai un claim `groups`, quindi con la mappatura dei ruoli abilitata, gli accessi Google rientrano sotto "claim assente" sopra: gli utenti esistenti mantengono il loro ruolo, ma i nuovi utenti Google vengono creati disabilitati e necessitano di approvazione manuale. Tieni presente questo prima di abilitare la mappatura dei ruoli solo per un altro fornitore – non disabilita, di per sé, gli utenti Google esistenti.

Microsoft Entra restituisce ruoli delle app e appartenenze ai gruppi solo nel token ID, non dall'endpoint userinfo. Gramps Web unisce i claim del token ID nella risposta userinfo in modo che `OIDC_ROLE_CLAIM` funzioni allo stesso modo degli altri fornitori; dove entrambi contengono un claim, il valore userinfo ha la precedenza.

## Primo Accesso e Bootstrap

I nuovi account creati tramite OIDC partono disabilitati a meno che la mappatura dei ruoli non assegni loro un ruolo (vedi sopra). Su un'istanza completamente nuova, nessuno può approvare un account disabilitato, e se `OIDC_DISABLE_LOCAL_AUTH` è anche abilitato non c'è accesso con password su cui fare affidamento.

!!! warning "Configura un gruppo di proprietari/amministratori prima del primo accesso"
    Prima che chiunque acceda tramite OIDC per la prima volta, imposta `OIDC_GROUP_OWNER` (o `OIDC_GROUP_ADMIN`) e assicurati che il primo utente appartenga a quel gruppo presso il fornitore. Altrimenti, l'istanza non può essere avviata tramite OIDC.

## Account e Nomi Utente

Gli account creati tramite OIDC ottengono un nome utente generato, assegnato una sola volta alla creazione dell'account e mai cambiato nei successivi accessi:

- Fornitori integrati: `<provider>_<claim value>`, ad esempio `microsoft_alice@contoso.com`
- Fornitore personalizzato: il valore del claim nudo, ad esempio `alice`

Un suffisso numerico viene aggiunto in caso di collisione. Non c'è modo di rinominare successivamente il nome utente di un account creato tramite OIDC; il nome completo e l'indirizzo e-mail, al contrario, vengono aggiornati ad ogni accesso.

Un accesso OIDC non si attacca mai a un account locale esistente che condivide per caso il suo indirizzo e-mail – questo è deliberato, poiché collegare account tramite e-mail è un vettore di takeover dell'account. Un utente che ha già un account locale ottiene un secondo account separato la prima volta che accede tramite OIDC.

Gli indirizzi e-mail dal fornitore vengono memorizzati solo se il fornitore li segna come verificati (o omette completamente il claim `email_verified`) e se l'indirizzo non è già utilizzato da un altro account; altrimenti, il login procede senza memorizzare un indirizzo e-mail.

## Logout OIDC

Gramps Web supporta il Single Sign-Out (logout SSO) per i fornitori OIDC. `GET /api/oidc/logout/` cerca l'`end_session_endpoint` del fornitore e lo restituisce come `logout_url` nella risposta; è il frontend di Gramps Web che naviga il browser lì per terminare effettivamente la sessione presso il fornitore di identità. `logout_url` è `null` quando il fornitore non ha un `end_session_endpoint`.

!!! warning "I token non vengono revocati al logout"
    Disconnettersi termina solo la sessione del browser; attualmente non c'è modo di revocare un token di Gramps Web che è già stato emesso. I token rimangono validi fino alla scadenza (`JWT_ACCESS_TOKEN_EXPIRES`, predefinito 15 minuti per i token di accesso), indipendentemente dal fatto che l'utente si sia disconnesso successivamente da Gramps Web o dal fornitore di identità.

## Esempi di Configurazione

### Fornitore OIDC Personalizzato (Keycloak)

```python
TREE="Il Mio Albero Familiare"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Configurazione OIDC Personalizzata
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Opzionale: reindirizza automaticamente al login SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Opzionale: disabilita il login con nome utente/password

# Opzionale: Mappatura dei ruoli dai gruppi OIDC ai ruoli di Gramps
OIDC_ROLE_CLAIM="groups"  # o "roles" a seconda del tuo fornitore
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Usa SSL implicito per la porta 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # la tua password SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Fornitore Integrato (Google)

```python
TREE="Il Mio Albero Familiare"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Più Fornitori

Puoi abilitare più fornitori OIDC simultaneamente:

```python
TREE="Il Mio Albero Familiare"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Fornitore personalizzato
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Company SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Una guida di configurazione OIDC creata dalla comunità per Gramps Web è disponibile sul [sito ufficiale della documentazione di Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La maggior parte della configurazione per Keycloak può essere lasciata ai suoi valori predefiniti (*Client → Crea client → Autenticazione client ATTIVA*).
Ci sono alcune eccezioni:

1. **Ambito OpenID** – L'ambito `openid` non è incluso per impostazione predefinita in tutte le versioni di Keycloak. Per evitare problemi, aggiungilo manualmente: *Client → [client Gramps] → Client scopes → Aggiungi ambito → Nome: `openid` → Imposta come predefinito.*
2. **Ruoli** – I ruoli possono essere assegnati sia a livello di client che globalmente per realm.

    * Se stai utilizzando ruoli client, imposta l'opzione di configurazione `OIDC_ROLE_CLAIM` su: `resource_access.[gramps-client-name].roles`
    * Per rendere i ruoli visibili a Gramps, naviga su *Client Scopes* (la sezione di primo livello, non sotto il client specifico), quindi: *Ruoli → Mappers → ruoli client → Aggiungi a userinfo → ON.*
