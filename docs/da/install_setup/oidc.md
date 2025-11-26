# OIDC Authentication

Gramps Web understøtter OpenID Connect (OIDC) autentifikation, som giver brugerne mulighed for at logge ind ved hjælp af eksterne identitetsudbydere. Dette inkluderer både populære udbydere som Google, Microsoft og GitHub, samt tilpassede OIDC-udbydere som Keycloak, Authentik og andre.

## Oversigt

OIDC autentifikation giver dig mulighed for at:

- Bruge eksterne identitetsudbydere til brugerautentifikation
- Understøtte flere autentifikationsudbydere samtidigt
- Kortlægge OIDC grupper/roller til Gramps Web brugerroller
- Implementere Single Sign-On (SSO) og Single Sign-Out
- Valgfrit deaktivere lokal brugernavn/adgangskode autentifikation

## Konfiguration

For at aktivere OIDC autentifikation skal du konfigurere de relevante indstillinger i din Gramps Web konfigurationsfil eller miljøvariabler. Se siden [Server Configuration](configuration.md#settings-for-oidc-authentication) for en komplet liste over tilgængelige OIDC indstillinger.

!!! info
    Når du bruger miljøvariabler, skal du huske at præfikse hvert indstillingsnavn med `GRAMPSWEB_` (f.eks. `GRAMPSWEB_OIDC_ENABLED`). Se [Configuration file vs. environment variables](configuration.md#configuration-file-vs-environment-variables) for detaljer.

### Indbyggede Udbydere

Gramps Web har indbygget support for populære identitetsudbydere. For at bruge dem skal du kun angive klient-ID og klienthemmelighed:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` og `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` og `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` og `OIDC_GITHUB_CLIENT_SECRET`

Du kan konfigurere flere udbydere samtidigt. Systemet vil automatisk registrere, hvilke udbydere der er tilgængelige baseret på konfigurationsværdierne.

### Tilpassede OIDC Udbydere

For tilpassede OIDC udbydere (som Keycloak, Authentik eller enhver standard OIDC-kompatibel udbyder) skal du bruge disse indstillinger:

Key | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC autentifikation skal aktiveres. Sæt til `True`.
`OIDC_ISSUER` | Din udbyders issuer URL
`OIDC_CLIENT_ID` | Klient-ID for din OIDC udbyder
`OIDC_CLIENT_SECRET` | Klienthemmelighed for din OIDC udbyder
`OIDC_NAME` | Tilpasset visningsnavn (valgfrit, standard til "OIDC")
`OIDC_SCOPES` | OAuth scopes (valgfrit, standard til "openid email profile")

## Krævede Redirect URIs

Når du konfigurerer din OIDC udbyder, skal du registrere følgende redirect URI:

**For OIDC udbydere, der understøtter wildcard: (f.eks. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Hvor `*` er et regex wildcard. Afhængigt af din udbyders regex-fortolker kan dette også være en `.*` eller lignende. Sørg for, at regex er aktiveret, hvis din udbyder kræver det (f.eks. Authentik).

**For OIDC udbydere, der ikke understøtter wildcard: (f.eks. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Rollekortlægning

Gramps Web kan automatisk kortlægge OIDC grupper eller roller fra din identitetsudbyder til Gramps Web brugerroller. Dette giver dig mulighed for at administrere brugerrettigheder centralt i din identitetsudbyder.

### Konfiguration

Brug disse indstillinger til at konfigurere rollekortlægning:

Key | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på kravet i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard til "groups"
`OIDC_GROUP_ADMIN` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Admin" rolle
`OIDC_GROUP_OWNER` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Owner" rolle
`OIDC_GROUP_EDITOR` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Editor" rolle
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Contributor" rolle
`OIDC_GROUP_MEMBER` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Member" rolle
`OIDC_GROUP_GUEST` | Gruppen/rollenavn fra din OIDC udbyder, der kortlægges til Gramps "Guest" rolle

### Rollekortlægningsadfærd

- Hvis der ikke er konfigureret nogen rollekortlægning (ingen `OIDC_GROUP_*` variabler er sat), bevares eksisterende brugerroller
- Brugere tildeles den højeste rolle, de har ret til baseret på deres gruppemedlemskab
- Rollekortlægning er som standard skelnen mellem store og små bogstaver (afhænger af din OIDC udbyder)

## OIDC Logout

Gramps Web understøtter Single Sign-Out (SSO logout) for OIDC udbydere. Når en bruger logger ud fra Gramps Web efter at have autentificeret via OIDC, vil de automatisk blive omdirigeret til identitetsudbyderens logout-side, hvis udbyderen understøtter `end_session_endpoint`.

### Backchannel Logout

Gramps Web implementerer OpenID Connect Back-Channel Logout-specifikationen. Dette gør det muligt for identitetsudbydere at underrette Gramps Web, når en bruger logger ud fra en anden applikation eller selve identitetsudbyderen.

#### Konfiguration

For at konfigurere backchannel logout med din identitetsudbyder:

1. **Registrer backchannel logout endpoint** i din identitetsudbyders klientkonfiguration:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Konfigurer din udbyder** til at sende logout-notifikationer. De præcise trin afhænger af din udbyder:

   **Keycloak:**

   - I din klientkonfiguration, gå til "Indstillinger"
   - Sæt "Backchannel Logout URL" til `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Aktivér "Backchannel Logout Session Required", hvis du ønsker sessionsbaseret logout

   **Authentik:**

   - I din udbyderkonfiguration, tilføj backchannel logout URL
   - Sørg for, at udbyderen er konfigureret til at sende logout tokens

!!! warning "Token Udløb"
    På grund af den statsløse karakter af JWT tokens, logger backchannel logout i øjeblikket logout-begivenheden, men kan ikke straks tilbagekalde allerede udstedte JWT tokens. Tokens vil forblive gyldige, indtil de udløber (standard: 15 minutter for adgangstokens).

    For forbedret sikkerhed, overvej:

    - At reducere JWT token udløbstid (`JWT_ACCESS_TOKEN_EXPIRES`)
    - At informere brugerne om manuelt at logge ud fra Gramps Web, når de logger ud fra din identitetsudbyder

!!! tip "Sådan fungerer det"
    Når en bruger logger ud fra din identitetsudbyder eller en anden applikation:

    1. Udbyderen sender et `logout_token` JWT til Gramps Web's backchannel logout endpoint
    2. Gramps Web validerer tokenet og logger logout-begivenheden
    3. Logout-tokenets JTI tilføjes til en blokliste for at forhindre replay-angreb
    4. Eventuelle nye API-anmodninger med brugerens JWT vil blive nægtet, når tokens udløber

## Eksempel Konfigurationer

### Tilpasset OIDC Udbyder (Keycloak)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Tilpasset OIDC Konfiguration
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Familie SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Valgfrit: automatisk omdirigering til SSO login
OIDC_DISABLE_LOCAL_AUTH=True  # Valgfrit: deaktivere brugernavn/adgangskode login

# Valgfrit: Rollekortlægning fra OIDC grupper til Gramps roller
OIDC_ROLE_CLAIM="groups"  # eller "roles" afhængigt af din udbyder
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # dit SMTP kodeord
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Indbygget Udbyder (Google)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Flere Udbydere

Du kan aktivere flere OIDC udbydere samtidigt:

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Tilpasset udbyder
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

En fællesskabsudviklet OIDC opsætningsguide til Gramps Web er tilgængelig på den [officielle Authelia dokumentationshjemmeside](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

De fleste af konfigurationerne for Keycloak kan efterlades på deres standardindstillinger (*Client → Opret klient → Klientautentifikation TIL*). Der er et par undtagelser:

1. **OpenID scope** – `openid` scope er ikke inkluderet som standard i alle Keycloak versioner. For at undgå problemer, tilføj det manuelt: *Client → [Gramps klient] → Client scopes → Tilføj scope → Navn: `openid` → Sæt som standard.*
2. **Roller** – Roller kan tildeles enten på klientniveau eller globalt pr. realm.

    * Hvis du bruger klientroller, skal du indstille `OIDC_ROLE_CLAIM` konfigurationsindstillingen til: `resource_access.[gramps-client-name].roles`
    * For at gøre roller synlige for Gramps, naviger til *Client Scopes* (den øverste sektion, ikke under den specifikke klient), så: *Roller → Mappers → klientroller → Tilføj til userinfo → TIL.*
