# Autenticazione OIDC

Gramps Web supporta l'autenticazione OpenID Connect (OIDC), consentendo agli utenti di accedere utilizzando provider di identità esterni. Questo include i provider integrati Google e Microsoft, così come provider OIDC personalizzati come Keycloak, Authentik e Authelia.

!!! warning "GitHub come provider OIDC non è più supportato"
    Se hai impostato `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` da una versione precedente, rimuovili – ora vengono ignorati e gli utenti che in precedenza accedevano tramite GitHub non possono più farlo. GitHub è un provider OAuth 2.0, non un provider OpenID Connect, e non ha mai restituito il claim su cui Gramps Web si basa per l'identità, quindi non è mai stato completamente affidabile.

## Panoramica

L'autenticazione OIDC ti consente di:

- Utilizzare provider di identità esterni per l'autenticazione degli utenti
- Supportare più provider di autenticazione simultaneamente
- Mappare gruppi/ruoli OIDC ai ruoli utente di Gramps Web
- Implementare Single Sign-On (SSO) e Single Sign-Out
- Disabilitare facoltativamente l'autenticazione locale con nome utente/password

## Configurazione

Per abilitare l'autenticazione OIDC, è necessario configurare le impostazioni appropriate nel file di configurazione di Gramps Web o nelle variabili di ambiente. Vedi la pagina [Configurazione del server](configuration.md#settings-for-oidc-authentication) per un elenco completo delle impostazioni OIDC disponibili.

!!! info
    Quando utilizzi variabili di ambiente, ricorda di anteporre a ciascun nome di impostazione `GRAMPSWEB_` (ad es., `GRAMPSWEB_OIDC_ENABLED`). Vedi [File di configurazione vs. variabili di ambiente](configuration.md#configuration-file-vs-environment-variables) per dettagli.

### Provider Integrati

Gramps Web ha supporto integrato per i provider di identità più popolari. Per utilizzarli, devi solo fornire l'ID client e il segreto client:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`

Puoi configurare più provider simultaneamente. Il sistema rileverà automaticamente quali provider sono disponibili in base ai valori di configurazione.

!!! tip "Microsoft: distribuzioni single-tenant"
    Il provider Microsoft integrato utilizza l'endpoint multi-tenant `/common` e accetta accessi da qualsiasi account Microsoft per design. Se desideri consentire solo agli utenti del tuo tenant, utilizza il [provider OIDC personalizzato](#custom-oidc-providers) con l'URL dell'emittente specifico del tuo tenant, il che mantiene attiva la convalida dell'emittente e limita gli accessi a quel tenant.

### Provider OIDC Personalizzati

Per i provider OIDC personalizzati (come Keycloak, Authentik, Authelia, o un tenant Microsoft Entra single-tenant), utilizza queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Booleano, se abilitare l'autenticazione OIDC. Imposta su `True`.
`OIDC_ISSUER` | L'URL dell'emittente del tuo provider. La scoperta viene recuperata da `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID client per il tuo provider OIDC
`OIDC_CLIENT_SECRET` | Segreto client per il tuo provider OIDC
`OIDC_NAME` | Nome visualizzato personalizzato (opzionale, predefinito "OIDC")
`OIDC_SCOPES` | Scopi OAuth (opzionale, predefinito "openid email profile")
`OIDC_USERNAME_CLAIM` | Claim utilizzato per generare il nome utente (opzionale, predefinito "preferred_username")
`OIDC_PKCE` | Se utilizzare PKCE, vedi [PKCE](#pkce) (opzionale, abilitato automaticamente se il provider lo supporta)

### PKCE

Dalla versione 3.23 dell'API Gramps Web, Gramps Web supporta [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, metodo `S256`) per il flusso di codice di autorizzazione. Alcuni provider di identità, come Pocket ID, possono essere configurati per *richiedere* PKCE per un client e rifiutare accessi che non lo utilizzano. Le versioni precedenti dell'API Gramps Web non utilizzano mai PKCE, quindi gli accessi con tale client falliscono.

Se PKCE viene utilizzato è deciso al momento del login come segue:

- Se `OIDC_PKCE` è impostato su `True`, viene utilizzato PKCE.
- Se `OIDC_PKCE` è impostato su `False`, PKCE non viene utilizzato, anche se il provider lo supporta.
- Se `OIDC_PKCE` non è impostato, o è impostato ma vuoto, PKCE viene utilizzato se il documento di scoperta del provider (`/.well-known/openid-configuration`) elenca `S256` in `code_challenge_methods_supported`, e non viene utilizzato altrimenti.

Per la maggior parte delle configurazioni non è necessario impostare nulla. Imposta `OIDC_PKCE` su `True` se il tuo provider richiede PKCE ma non pubblicizza `S256` nel suo documento di scoperta, e su `False` se il tuo provider pubblicizza `S256` ma lo gestisce in modo errato. Come variabili di ambiente, i booleani devono essere in minuscolo (`GRAMPSWEB_OIDC_PKCE=true`), vedi [Configurazione](configuration.md).

Per i provider integrati, le opzioni corrispondenti sono `OIDC_GOOGLE_PKCE` e `OIDC_MICROSOFT_PKCE`.

Il verificatore del codice PKCE viene mantenuto nella sessione dell'utente tra il reindirizzamento al provider e il callback, quindi non è necessario alcun cambiamento negli URI di reindirizzamento.

### Configurazioni Multi-Albero

Su un server multi-albero, l'albero in cui l'utente sta accedendo deve essere noto prima che Gramps Web reindirizzi al provider di identità, quindi il login inizia con:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` è richiesto nelle configurazioni multi-albero; ometterlo o passare l'ID di un albero che non esiste provoca il fallimento del login. Su un server single-tree `tree` è facoltativo, ma se fornito deve corrispondere a `TREE` configurato.

Un'identità OIDC è legata esattamente a un account Gramps Web, che a sua volta appartiene esattamente a un albero – accedere a un albero diverso fallisce piuttosto che spostare l'account. Non c'è modo di collegare una singola identità presso il provider a account in diversi alberi; gli utenti che necessitano di accesso a più alberi hanno bisogno di identità separate presso il provider (ad es. nomi utente o account distinti).

!!! warning
    Un account di amministratore del sito senza un albero associato (vedi [creazione di un account admin](../administration/owner.md)) non può accedere tramite OIDC, poiché il login OIDC richiede sempre un albero. Tali account devono essere creati e autenticati con un nome utente/password locale.

## URI di Reindirizzamento Richiesti

Quando configuri il tuo provider OIDC, devi registrare il seguente URI di reindirizzamento:

**Per i provider OIDC che supportano i caratteri jolly: (ad es., Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Dove `*` è un carattere jolly regex. A seconda dell'interprete regex del tuo provider, potrebbe essere anche un `.*` o simile. Assicurati che il regex sia abilitato se il tuo provider lo richiede (ad es., Authentik).

**Per i provider OIDC che non supportano i caratteri jolly: (ad es., Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

L'albero non è mai parte dell'URI di reindirizzamento, anche sui server multi-albero – viaggia separatamente nella sessione, poiché i provider richiedono che l'URI di reindirizzamento corrisponda esattamente a quello registrato.

## Mappatura dei Ruoli

Gramps Web può mappare automaticamente i gruppi o i ruoli OIDC dal tuo provider di identità ai ruoli utente di Gramps Web. Questo ti consente di gestire centralmente i permessi degli utenti nel tuo provider di identità. La mappatura dei ruoli funziona allo stesso modo per tutti i provider, integrati o personalizzati.

### Configurazione

Utilizza queste impostazioni per configurare la mappatura dei ruoli:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Predefinito "groups". I percorsi con punti sono supportati, ad es. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Admin" di Gramps
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Owner" di Gramps
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Editor" di Gramps
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Contributor" di Gramps
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Member" di Gramps
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo dal tuo provider OIDC che mappa al ruolo "Guest" di Gramps

### Comportamento della Mappatura dei Ruoli

Se non è configurata alcuna impostazione `OIDC_GROUP_*`, la mappatura dei ruoli è disattivata e i ruoli sono gestiti manualmente in Gramps Web; i nuovi account OIDC vengono quindi creati disabilitati e devono essere approvati da un proprietario o un amministratore esistente (vedi [Primo Accesso e Avvio](#first-login-and-bootstrapping) qui sotto).

Una volta configurata la mappatura dei ruoli, ad ogni accesso:

- Se il claim del ruolo è presente e l'utente appartiene a un gruppo mappato, riceve il ruolo corrispondente.
- Se il claim del ruolo è presente ma l'utente non appartiene a nessun gruppo mappato, il suo ruolo è impostato su disabilitato. Questo è un default di chiusura, non un bug – Gramps Web non può inferire un ruolo per un gruppo che non riconosce.
- Se il claim del ruolo è completamente assente dal token, il ruolo esistente rimane invariato; un nuovo account continua a essere disabilitato.

!!! warning "Google non invia un claim di gruppi"
    I token di Google non includono mai un claim `groups`, quindi con la mappatura dei ruoli abilitata, gli accessi Google rientrano sotto "claim assente" sopra: gli utenti esistenti mantengono il loro ruolo, ma i nuovi utenti Google vengono creati disabilitati e necessitano di approvazione manuale. Tieni presente questo prima di abilitare la mappatura dei ruoli solo per un altro provider – non disabilita, di per sé, gli utenti Google esistenti.

Microsoft Entra restituisce ruoli delle app e appartenenze ai gruppi solo nel token ID, non dall'endpoint userinfo. Gramps Web unisce i claim del token ID nella risposta userinfo in modo che `OIDC_ROLE_CLAIM` funzioni allo stesso modo degli altri provider; dove entrambi contengono un claim, il valore userinfo ha la precedenza.

## Primo Accesso e Avvio

I nuovi account creati tramite OIDC partono disabilitati a meno che la mappatura dei ruoli non assegni loro un ruolo (vedi sopra). Su un'istanza completamente nuova, nessuno può approvare un account disabilitato, e se `OIDC_DISABLE_LOCAL_AUTH` è anche abilitato non c'è nemmeno un accesso con password su cui fare affidamento.

!!! warning "Configura un gruppo di proprietari/amministratori prima del primo accesso"
    Prima che qualcuno acceda tramite OIDC per la prima volta, imposta `OIDC_GROUP_OWNER` (o `OIDC_GROUP_ADMIN`) e assicurati che il primo utente appartenga a quel gruppo presso il provider. Altrimenti, l'istanza non può essere avviata tramite OIDC.

## Account e Nomi Utente

Gli account creati tramite OIDC ottengono un nome utente generato, assegnato una sola volta alla creazione dell'account e mai cambiato nei successivi accessi:

- Provider integrati: `<provider>_<claim value>`, ad es. `microsoft_alice@contoso.com`
- Provider personalizzato: il valore del claim nudo, ad es. `alice`

Un suffisso numerico viene aggiunto in caso di collisione. Non c'è modo di rinominare successivamente il nome utente di un account creato tramite OIDC; il nome completo e l'indirizzo e-mail, al contrario, vengono aggiornati ad ogni accesso.

Un accesso OIDC non si attacca mai a un account locale esistente che condivide per caso il suo indirizzo e-mail – questo è voluto, poiché collegare account tramite e-mail è un vettore di takeover dell'account. Un utente che ha già un account locale ottiene un secondo account separato la prima volta che accede tramite OIDC.

Gli indirizzi e-mail del provider vengono memorizzati solo se il provider li contrassegna come verificati (o omette completamente il claim `email_verified`); altrimenti l'accesso procede senza memorizzare un indirizzo e-mail. Poiché gli indirizzi e-mail non devono essere unici (dalla versione 3.22 dell'API Gramps Web), un indirizzo viene memorizzato anche se un altro account lo utilizza già.

## Logout OIDC

Gramps Web supporta il Single Sign-Out (logout SSO) per i provider OIDC. `GET /api/oidc/logout/` cerca l'`end_session_endpoint` del provider e lo restituisce come `logout_url` nella risposta; è il frontend di Gramps Web che naviga il browser lì per terminare effettivamente la sessione presso il provider di identità. `logout_url` è `null` quando il provider non ha un `end_session_endpoint`.

!!! warning "I token non vengono revocati al logout"
    Disconnettersi termina solo la sessione del browser; attualmente non c'è modo di revocare un token Gramps Web che è già stato emesso. I token rimangono validi fino alla scadenza (`JWT_ACCESS_TOKEN_EXPIRES`, predefinito 15 minuti per i token di accesso), indipendentemente dal fatto che l'utente si sia successivamente disconnesso da Gramps Web o dal provider di identità.

## Risoluzione dei Problemi

Inizia dal punto in cui il login si ferma e segui il ramo. Gramps Web registra il motivo di un callback fallito (cerca `OIDC callback error for provider` nel log del server), che è solitamente più specifico del messaggio mostrato nel browser.

**1. Il pulsante di accesso è mancante?**

- Controlla `<BASE_URL>/api/oidc/config/`. Se `enabled` è `false` o `providers` è vuoto, OIDC non è configurato: `OIDC_ENABLED` deve essere `True`, e un provider personalizzato ha bisogno sia di `OIDC_ISSUER` che di `OIDC_CLIENT_ID`.
- Un provider integrato (Google, Microsoft) è registrato solo se sia il suo ID client che il suo segreto client sono impostati.
- Controlla nel log del server all'avvio per `Could not load discovery document`. Questo significa che il server non è riuscito a raggiungere `<issuer>/.well-known/openid-configuration` (o `OIDC_OPENID_CONFIG_URL`). Riprova al primo utilizzo, ma il contenitore Gramps Web deve essere in grado di risolvere e raggiungere l'URL dell'emittente stesso, non solo il tuo browser.

**2. Il browser riceve un errore subito dopo essere stato inviato al provider?**

L'errore è mostrato dal provider di identità, prima che tu acceda.

- *"redirect URI mismatch"* (o simile): l'URI di reindirizzamento registrato presso il provider deve corrispondere esattamente, incluso schema, host, porta e ID del provider. Vedi [URI di Reindirizzamento Richiesti](#required-redirect-uris). Nota che è costruito da `BASE_URL`, quindi un `BASE_URL` errato dà un URI di reindirizzamento errato.
- *Un errore PKCE* (ad esempio `invalid_request`, "code challenge required", o un parametro `code_challenge` mancante): il provider richiede PKCE ma Gramps Web non lo ha inviato. Vai al [ramo PKCE](#pkce-branch) qui sotto.

**3. Il provider accetta il login ma Gramps Web mostra poi un errore?**

- *`mismatching_state`, o l'errore menziona la sessione o lo stato*: il browser non ha restituito il cookie di sessione che Gramps Web ha impostato quando è iniziato il login. Questo cookie porta anche il verificatore del codice PKCE. Assicurati che l'indirizzo nel browser corrisponda a `BASE_URL` (stesso schema e host), che un proxy inverso passi i cookie e l'host originale, e che il login sia iniziato e completato nella stessa scheda o finestra del browser.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: controlla il log del server per il motivo sottostante. Le cause comuni sono un segreto client errato, un URL dell'emittente che non corrisponde al claim `iss` dei token, e il provider che restituisce un errore al callback (ad esempio PKCE, vedi sotto).
- *Troppi tentativi*: gli endpoint di login e callback sono limitati (5 richieste al minuto). Aspetta un minuto e riprova.

**4. Il login ha successo ma vedi "Account Under Review", o non puoi fare nulla?**

I nuovi account vengono creati disabilitati a meno che la mappatura dei ruoli non assegni un ruolo. Vedi [Primo Accesso e Avvio](#first-login-and-bootstrapping) e [Comportamento della Mappatura dei Ruoli](#role-mapping-behavior). Un amministratore può anche attivare l'account sotto Impostazioni > Amministrazione > Gestisci utenti.

### Ramo PKCE

Gramps Web decide se utilizzare PKCE quando inizia un login (vedi [PKCE](#pkce)). Per scoprire cosa è successo per la tua configurazione, segui queste domande in ordine:

1. **È impostato `OIDC_PKCE`?** (Per i provider integrati, `OIDC_GOOGLE_PKCE` o `OIDC_MICROSOFT_PKCE`.)
    - `True`: viene utilizzato PKCE. Salta alla domanda 3.
    - `False`: PKCE è deliberatamente disattivato e il documento di scoperta del provider viene ignorato. Se il tuo provider richiede PKCE, rimuovi l'impostazione o impostala su `True`.
    - Non impostato, o vuoto: continua con la domanda 2.
2. **Il documento di scoperta elenca `S256`?** Apri `<issuer>/.well-known/openid-configuration` e cerca `S256` in `code_challenge_methods_supported`.
    - Sì: PKCE viene utilizzato automaticamente. Continua con la domanda 3.
    - No, o il campo è mancante: PKCE **non** viene utilizzato. Imposta `OIDC_PKCE` su `True` se il tuo provider lo richiede. Controlla anche il log del server per `Could not check the provider for PKCE support`, il che significa che il documento di scoperta non è stato recuperato e quindi PKCE è stato disattivato.
3. **PKCE è stato realmente inviato?** Inizia un login e guarda l'indirizzo della pagina di accesso del provider (o il primo reindirizzamento nella scheda di rete del tuo browser). Dovrebbe contenere `code_challenge=` e `code_challenge_method=S256`.
    - Presente, ma il login fallisce ancora al callback: il provider ha rifiutato il verificatore del codice. Il cookie di sessione potrebbe essere andato perso tra il reindirizzamento e il callback (vedi ramo 3 sopra), o il provider non supporta `S256`, nel qual caso imposta `OIDC_PKCE` su `False` se il provider non richiede PKCE.
    - Assente: le impostazioni sopra non sono state applicate. Controlla che la variabile di ambiente abbia il prefisso corretto e un valore in minuscolo (ad esempio `GRAMPSWEB_OIDC_PKCE=true` in Docker; `True` non viene letto come booleano), riavvia il server e guarda di nuovo la configurazione.

!!! note
    Con PKCE abilitato presso il provider come *opzionale*, o non abilitato affatto, gli accessi funzionano indipendentemente dal fatto che Gramps Web invii o meno una sfida. Solo i provider (o i client) configurati per *richiedere* PKCE rendono questa impostazione rilevante.

## Configurazioni di Esempio

### Provider OIDC Personalizzato (Keycloak)

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
OIDC_ROLE_CLAIM="groups"  # o "roles" a seconda del tuo provider
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

### Provider Integrato (Google)

```python
TREE="Il Mio Albero Familiare"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Più Provider

Puoi abilitare più provider OIDC simultaneamente:

```python
TREE="Il Mio Albero Familiare"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Provider personalizzato
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

### Pocket ID

Crea un client OIDC in Pocket ID con l'URI di reindirizzamento `<BASE_URL>/api/oidc/callback/custom` (vedi [URI di Reindirizzamento Richiesti](#required-redirect-uris)). Se abiliti "Richiedi PKCE" per il client, non è necessaria alcuna configurazione aggiuntiva di Gramps Web, poiché Pocket ID pubblicizza il supporto PKCE nel suo documento di scoperta. Quindi configura:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Una guida alla configurazione OIDC realizzata dalla comunità per Gramps Web è disponibile sul [sito ufficiale della documentazione di Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La maggior parte della configurazione per Keycloak può essere lasciata ai suoi valori predefiniti (*Client → Crea client → Autenticazione client ATTIVA*).
Ci sono alcune eccezioni:

1. **Ambito OpenID** – L'ambito `openid` non è incluso per impostazione predefinita in tutte le versioni di Keycloak. Per evitare problemi, aggiungilo manualmente: *Client → [Client Gramps] → Scopi client → Aggiungi ambito → Nome: `openid` → Imposta come predefinito.*
2. **Ruoli** – I ruoli possono essere assegnati sia a livello di client che globalmente per realm.

    * Se stai utilizzando ruoli client, imposta l'opzione di configurazione `OIDC_ROLE_CLAIM` su: `resource_access.[gramps-client-name].roles`
    * Per rendere i ruoli visibili a Gramps, naviga su *Scopi Client* (la sezione di livello superiore, non sotto il client specifico), quindi: *Ruoli → Mapper → ruoli client → Aggiungi a userinfo → ON.*
