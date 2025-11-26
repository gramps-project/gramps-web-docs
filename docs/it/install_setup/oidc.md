# Autenticazione OIDC

Gramps Web supporta l'autenticazione OpenID Connect (OIDC), consentendo agli utenti di accedere utilizzando fornitori di identità esterni. Questo include sia fornitori popolari come Google, Microsoft e GitHub, sia fornitori OIDC personalizzati come Keycloak, Authentik e altri.

## Panoramica

L'autenticazione OIDC consente di:

- Utilizzare fornitori di identità esterni per l'autenticazione degli utenti
- Supportare più fornitori di autenticazione contemporaneamente
- Mappare gruppi/ruoli OIDC ai ruoli utente di Gramps Web
- Implementare Single Sign-On (SSO) e Single Sign-Out
- Disabilitare facoltativamente l'autenticazione locale con nome utente/password

## Configurazione

Per abilitare l'autenticazione OIDC, è necessario configurare le impostazioni appropriate nel file di configurazione di Gramps Web o nelle variabili di ambiente. Vedi la pagina [Configurazione del server](configuration.md#settings-for-oidc-authentication) per un elenco completo delle impostazioni OIDC disponibili.

!!! info
    Quando si utilizzano variabili di ambiente, ricordati di anteporre a ciascun nome di impostazione `GRAMPSWEB_` (ad es., `GRAMPSWEB_OIDC_ENABLED`). Vedi [File di configurazione vs. variabili di ambiente](configuration.md#configuration-file-vs-environment-variables) per dettagli.

### Fornitori Integrati

Gramps Web ha supporto integrato per fornitori di identità popolari. Per utilizzarli, è necessario fornire solo l'ID client e il segreto client:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` e `OIDC_GITHUB_CLIENT_SECRET`

Puoi configurare più fornitori contemporaneamente. Il sistema rileverà automaticamente quali fornitori sono disponibili in base ai valori di configurazione.

### Fornitori OIDC Personalizzati

Per fornitori OIDC personalizzati (come Keycloak, Authentik o qualsiasi fornitore conforme agli standard OIDC), utilizza queste impostazioni:

Chiave | Descrizione
----|-------------
`OIDC_ENABLED` | Booleano, se abilitare l'autenticazione OIDC. Imposta su `True`.
`OIDC_ISSUER` | L'URL dell'emittente del tuo fornitore
`OIDC_CLIENT_ID` | ID client per il tuo fornitore OIDC
`OIDC_CLIENT_SECRET` | Segreto client per il tuo fornitore OIDC
`OIDC_NAME` | Nome di visualizzazione personalizzato (opzionale, predefinito "OIDC")
`OIDC_SCOPES` | Scopi OAuth (opzionale, predefinito "openid email profile")

## URI di Reindirizzamento Richiesti

Quando configuri il tuo fornitore OIDC, devi registrare il seguente URI di reindirizzamento:

**Per fornitori OIDC che supportano i caratteri jolly: (ad es., Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Dove `*` è un carattere jolly regex. A seconda dell'interprete regex del tuo fornitore, questo potrebbe essere anche un `.*` o simile.
Assicurati che il regex sia abilitato se il tuo fornitore lo richiede (ad es., Authentik).

**Per fornitori OIDC che non supportano i caratteri jolly: (ad es., Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Mappatura dei Ruoli

Gramps Web può mappare automaticamente gruppi o ruoli OIDC dal tuo fornitore di identità ai ruoli utente di Gramps Web. Questo ti consente di gestire centralmente i permessi degli utenti nel tuo fornitore di identità.

### Configurazione

Utilizza queste impostazioni per configurare la mappatura dei ruoli:

Chiave | Descrizione
----|-------------
`OIDC_ROLE_CLAIM` | Il nome del claim nel token OIDC che contiene i gruppi/ruoli dell'utente. Predefinito "groups"
`OIDC_GROUP_ADMIN` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Admin" di Gramps
`OIDC_GROUP_OWNER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Owner" di Gramps
`OIDC_GROUP_EDITOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Editor" di Gramps
`OIDC_GROUP_CONTRIBUTOR` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Contributor" di Gramps
`OIDC_GROUP_MEMBER` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Member" di Gramps
`OIDC_GROUP_GUEST` | Il nome del gruppo/ruolo dal tuo fornitore OIDC che si mappa al ruolo "Guest" di Gramps

### Comportamento della Mappatura dei Ruoli

- Se non è configurata alcuna mappatura dei ruoli (nessuna variabile `OIDC_GROUP_*` impostata), i ruoli utente esistenti vengono preservati
- Gli utenti vengono assegnati al ruolo più alto a cui hanno diritto in base alla loro appartenenza ai gruppi
- La mappatura dei ruoli è case-sensitive per impostazione predefinita (dipende dal tuo fornitore OIDC)

## Logout OIDC

Gramps Web supporta il Single Sign-Out (logout SSO) per i fornitori OIDC. Quando un utente esce da Gramps Web dopo aver effettuato l'autenticazione tramite OIDC, verrà automaticamente reindirizzato alla pagina di logout del fornitore di identità se il fornitore supporta l'`end_session_endpoint`.

### Logout Backchannel

Gramps Web implementa la specifica di Logout Back-Channel di OpenID Connect. Questo consente ai fornitori di identità di notificare a Gramps Web quando un utente esce da un'altra applicazione o dallo stesso fornitore di identità.

#### Configurazione

Per configurare il logout backchannel con il tuo fornitore di identità:

1. **Registrare l'endpoint di logout backchannel** nella configurazione del client del tuo fornitore di identità:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Configurare il tuo fornitore** per inviare notifiche di logout. I passaggi esatti dipendono dal tuo fornitore:

   **Keycloak:**

   - Nella configurazione del tuo client, vai su "Impostazioni"
   - Imposta "URL di Logout Backchannel" su `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Abilita "Logout Backchannel Session Required" se desideri un logout basato su sessione

   **Authentik:**

   - Nella configurazione del tuo fornitore, aggiungi l'URL di logout backchannel
   - Assicurati che il fornitore sia configurato per inviare token di logout

!!! warning "Scadenza del Token"
    A causa della natura stateless dei token JWT, il logout backchannel attualmente registra l'evento di logout ma non può revocare immediatamente i token JWT già emessi. I token rimarranno validi fino alla loro scadenza (predefinito: 15 minuti per i token di accesso).

    Per una maggiore sicurezza, considera:

    - Ridurre il tempo di scadenza del token JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Educare gli utenti a disconnettersi manualmente da Gramps Web quando escono dal tuo fornitore di identità

!!! tip "Come Funziona"
    Quando un utente esce dal tuo fornitore di identità o da un'altra applicazione:

    1. Il fornitore invia un `logout_token` JWT all'endpoint di logout backchannel di Gramps Web
    2. Gramps Web convalida il token e registra l'evento di logout
    3. Il JTI del token di logout viene aggiunto a una blacklist per prevenire attacchi di replay
    4. Qualsiasi nuova richiesta API con il JWT dell'utente verrà negata una volta scaduti i token

## Esempi di Configurazione

### Fornitore OIDC Personalizzato (Keycloak)

```python
TREE="Il Mio Albero Genealogico"
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
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # la tua password SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Fornitore Integrato (Google)

```python
TREE="Il Mio Albero Genealogico"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # la tua chiave segreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Più Fornitori

Puoi abilitare più fornitori OIDC contemporaneamente:

```python
TREE="Il Mio Albero Genealogico"
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

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Una guida alla configurazione OIDC realizzata dalla comunità per Gramps Web è disponibile sul [sito ufficiale della documentazione di Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La maggior parte della configurazione per Keycloak può rimanere ai suoi valori predefiniti (*Client → Crea client → Autenticazione client ATTIVA*).
Ci sono alcune eccezioni:

1. **Ambito OpenID** – L'ambito `openid` non è incluso per impostazione predefinita in tutte le versioni di Keycloak. Per evitare problemi, aggiungilo manualmente: *Client → [Client Gramps] → Scopi client → Aggiungi ambito → Nome: `openid` → Imposta come predefinito.*
2. **Ruoli** – I ruoli possono essere assegnati sia a livello di client che globalmente per realm.

    * Se utilizzi ruoli client, imposta l'opzione di configurazione `OIDC_ROLE_CLAIM` su: `resource_access.[gramps-client-name].roles`
    * Per rendere i ruoli visibili a Gramps, vai su *Scopi Client* (la sezione di primo livello, non sotto il client specifico), quindi: *Ruoli → Mapper → ruoli client → Aggiungi a userinfo → ON.*
