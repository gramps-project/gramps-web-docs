# OIDC Authentication

Gramps Web understøtter OpenID Connect (OIDC) autentifikation, hvilket giver brugerne mulighed for at logge ind ved hjælp af eksterne identitetsudbydere. Dette inkluderer de indbyggede udbydere Google og Microsoft samt tilpassede OIDC-udbydere som Keycloak, Authentik og Authelia.

!!! warning "GitHub som OIDC-udbyder understøttes ikke længere"
    Hvis du har `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` indstillet fra en tidligere version, skal du fjerne dem – de ignoreres nu, og brugere, der tidligere loggede ind via GitHub, kan ikke længere logge ind på den måde. GitHub er en OAuth 2.0-udbyder, ikke en OpenID Connect-udbyder, og har aldrig returneret den påstand, som Gramps Web er afhængig af for identitet, så det var aldrig helt pålideligt.

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
    Når du bruger miljøvariabler, skal du huske at præfiksere hvert indstillingsnavn med `GRAMPSWEB_` (f.eks. `GRAMPSWEB_OIDC_ENABLED`). Se [Configuration file vs. environment variables](configuration.md#configuration-file-vs-environment-variables) for detaljer.

### Indbyggede Udbydere

Gramps Web har indbygget support til populære identitetsudbydere. For at bruge dem skal du kun angive klient-ID og klienthemmelighed:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` og `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` og `OIDC_MICROSOFT_CLIENT_SECRET`

Du kan konfigurere flere udbydere samtidigt. Systemet vil automatisk registrere, hvilke udbydere der er tilgængelige baseret på konfigurationsværdierne.

!!! tip "Microsoft: single-tenant deployment"
    Den indbyggede Microsoft-udbyder bruger multi-tenant `/common` endpointet og accepterer login fra enhver Microsoft-konto som standard. Hvis du kun vil tillade brugere fra din egen lejer, skal du bruge [den tilpassede OIDC-udbyder](#custom-oidc-providers) med din lejer-specifikke udsteder-URL i stedet, hvilket holder udsteder-validering aktiv og begrænser login til den lejer.

### Tilpassede OIDC Udbydere

For tilpassede OIDC-udbydere (som Keycloak, Authentik, Authelia, eller en single-tenant Microsoft Entra lejer), brug disse indstillinger:

Key | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC autentifikation skal aktiveres. Sæt til `True`.
`OIDC_ISSUER` | Din udbyders udsteder-URL. Discovery hentes fra `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | Klient-ID for din OIDC-udbyder
`OIDC_CLIENT_SECRET` | Klienthemmelighed for din OIDC-udbyder
`OIDC_NAME` | Tilpasset visningsnavn (valgfrit, standard til "OIDC")
`OIDC_SCOPES` | OAuth scopes (valgfrit, standard til "openid email profile")
`OIDC_USERNAME_CLAIM` | Påstand brugt til at generere brugernavnet (valgfrit, standard til "preferred_username")

### Multi-Tree Opsætninger

På en multi-tree server skal det træ, som brugeren logger ind i, være kendt, før Gramps Web omdirigerer til identitetsudbyderen, så login starter med:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` er påkrævet i multi-tree opsætninger; hvis det udelades, eller hvis ID'et for et træ, der ikke eksisterer, gives, mislykkes login. På en single-tree server er `tree` valgfrit, men hvis det gives, skal det matche den konfigurerede `TREE`.

En OIDC identitet er bundet til præcist én Gramps Web-konto, som igen tilhører præcist ét træ – at logge ind mod et andet træ mislykkes i stedet for at flytte kontoen. Der er ingen måde at knytte en enkelt identitet hos udbyderen til konti i flere træer; brugere, der har brug for adgang til flere træer, har brug for separate identiteter hos udbyderen (f.eks. forskellige brugernavne eller konti).

!!! warning
    En site-administrator konto uden tilknyttet træ (se [creating an admin account](../administration/owner.md)) kan ikke logge ind via OIDC, da OIDC-login altid kræver et træ. Sådanne konti skal oprettes og godkendes med et lokalt brugernavn/adgangskode i stedet.

## Krævede Omdirigerings-URI'er

Når du konfigurerer din OIDC-udbyder, skal du registrere følgende omdirigerings-URI:

**For OIDC-udbydere, der understøtter wildcard: (f.eks. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Hvor `*` er et regex wildcard. Afhængigt af din udbyders regex-fortolker kan dette også være en `.*` eller lignende.
Sørg for, at regex er aktiveret, hvis din udbyder kræver det (f.eks. Authentik).

**For OIDC-udbydere, der ikke understøtter wildcard: (f.eks. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Træet er aldrig en del af omdirigerings-URI'en, selv på multi-tree servere – det rejser separat i sessionen, da udbydere kræver, at omdirigerings-URI'en matcher den registrerede præcist.

## Rolle Kortlægning

Gramps Web kan automatisk kortlægge OIDC grupper eller roller fra din identitetsudbyder til Gramps Web brugerroller. Dette giver dig mulighed for at administrere brugerrettigheder centralt i din identitetsudbyder. Rolle kortlægning fungerer på samme måde for alle udbydere, både indbyggede og tilpassede.

### Konfiguration

Brug disse indstillinger til at konfigurere rolle kortlægning:

Key | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på påstanden i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard til "groups". Dotted paths understøttes, f.eks. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Admin" rolle
`OIDC_GROUP_OWNER` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Owner" rolle
`OIDC_GROUP_EDITOR` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Editor" rolle
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Contributor" rolle
`OIDC_GROUP_MEMBER` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Member" rolle
`OIDC_GROUP_GUEST` | Gruppen/rolle navnet fra din OIDC-udbyder, der kortlægges til Gramps "Guest" rolle

### Rolle Kortlægningsadfærd

Hvis ingen `OIDC_GROUP_*` indstilling er konfigureret overhovedet, er rolle kortlægning slået fra, og roller administreres manuelt i Gramps Web; nye OIDC-konti oprettes derefter deaktiveret og skal godkendes af en eksisterende ejer eller administrator (se [First Login and Bootstrapping](#first-login-and-bootstrapping) nedenfor).

Når rolle kortlægning er konfigureret, ved hver login:

- Hvis rolle-påstanden er til stede, og brugeren tilhører en kortlagt gruppe, får de den tilsvarende rolle.
- Hvis rolle-påstanden er til stede, men brugeren tilhører ingen kortlagt gruppe, sættes deres rolle til deaktiveret. Dette er en fail-closed standard, ikke en fejl – Gramps Web kan ikke udlede en rolle for en gruppe, den ikke genkender.
- Hvis rolle-påstanden er helt fraværende fra tokenet, forbliver den eksisterende rolle uændret; en ny konto standardmæssigt er stadig deaktiveret.

!!! warning "Google sender ikke en groups claim"
    Googles tokens inkluderer aldrig en `groups` påstand, så med rolle kortlægning aktiveret falder Google-login under "påstand fraværende" ovenfor: eksisterende brugere beholder deres rolle, men nye Google-brugere oprettes deaktiveret og skal godkendes manuelt. Husk dette, før du aktiverer rolle kortlægning kun for en anden udbyder – det deaktiverer ikke i sig selv eksisterende Google-brugere.

Microsoft Entra returnerer app-roller og gruppe-medlemskaber kun i ID-tokenet, ikke fra userinfo endpointet. Gramps Web fusionerer ID-tokenets påstande ind i userinfo svaret, så `OIDC_ROLE_CLAIM` fungerer på samme måde som for andre udbydere; hvor begge indeholder en påstand, har userinfo-værdien forrang.

## Første Login og Bootstrapping

Nye konti oprettet gennem OIDC starter deaktiveret, medmindre rolle kortlægning tildeler dem en rolle (se ovenfor). På en helt ny instans kan ingen godkende en deaktiveret konto, og hvis `OIDC_DISABLE_LOCAL_AUTH` også er aktiveret, er der ingen adgangskode-login at falde tilbage på.

!!! warning "Konfigurer en ejer/admin gruppe før første login"
    Før nogen logger ind via OIDC for første gang, skal du indstille `OIDC_GROUP_OWNER` (eller `OIDC_GROUP_ADMIN`) og sikre, at den første bruger tilhører den gruppe hos udbyderen. Ellers kan instansen ikke bootstrappes gennem OIDC overhovedet.

## Konti og Brugernavne

Konti oprettet gennem OIDC får et genereret brugernavn, tildelt én gang ved konto-oprettelsen og aldrig ændret ved senere login:

- Indbyggede udbydere: `<provider>_<claim value>`, f.eks. `microsoft_alice@contoso.com`
- Tilpasset udbyder: den bare påstandsværdi, f.eks. `alice`

Et numerisk suffix tilføjes ved kollision. Der er ingen måde at omdøbe et OIDC-oprettet kontos brugernavn bagefter; fulde navn og e-mailadresse opdateres derimod ved hvert login.

Et OIDC-login knytter sig aldrig til en eksisterende lokal konto, der tilfældigvis deler sin e-mailadresse – dette er bevidst, da sammenkobling af konti via e-mail er en konto-overtagelsesvektor. En bruger, der allerede har en lokal konto, får en anden, separat konto første gang de logger ind via OIDC.

E-mailadresser fra udbyderen gemmes kun, hvis udbyderen markerer dem som verificerede (eller udelader `email_verified` påstanden helt) og hvis adressen ikke allerede bruges af en anden konto; ellers fortsætter login uden at gemme en e-mailadresse.

## OIDC Logout

Gramps Web understøtter Single Sign-Out (SSO logout) for OIDC-udbydere. `GET /api/oidc/logout/` ser op på udbyderens `end_session_endpoint` og returnerer det som `logout_url` i svaret; det er Gramps Web frontend, der navigerer browseren derhen for faktisk at afslutte sessionen hos identitetsudbyderen. `logout_url` er `null`, når udbyderen ikke har nogen `end_session_endpoint`.

!!! warning "Tokens bliver ikke tilbagekaldt ved logout"
    At logge ud afslutter kun browsersessionen; der er i øjeblikket ingen måde at tilbagekalde et Gramps Web-token, der allerede er blevet udstedt. Tokens forbliver gyldige, indtil de udløber (`JWT_ACCESS_TOKEN_EXPIRES`, standard 15 minutter for adgangstokens), uanset om brugeren siden har logget ud hos Gramps Web eller hos identitetsudbyderen.

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
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Valgfrit: automatisk omdirigering til SSO-login
OIDC_DISABLE_LOCAL_AUTH=True  # Valgfrit: deaktivere brugernavn/adgangskode-login

# Valgfrit: Rolle kortlægning fra OIDC grupper til Gramps roller
OIDC_ROLE_CLAIM="groups"  # eller "roles" afhængigt af din udbyder
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # din SMTP-adgangskode
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

Du kan aktivere flere OIDC-udbydere samtidigt:

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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

En community-lavet OIDC opsætningsguide til Gramps Web er tilgængelig på [den officielle Authelia dokumentationshjemmeside](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Det meste af konfigurationen for Keycloak kan efterlades på standardindstillingerne (*Client → Create client → Client authentication ON*).
Der er et par undtagelser:

1. **OpenID scope** – `openid` scope er ikke inkluderet som standard i alle Keycloak-versioner. For at undgå problemer, tilføj det manuelt: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Roller** – Roller kan tildeles enten på klientniveau eller globalt pr. realm.

    * Hvis du bruger klientroller, skal du indstille `OIDC_ROLE_CLAIM` konfigurationsmuligheden til: `resource_access.[gramps-client-name].roles`
    * For at gøre roller synlige for Gramps, naviger til *Client Scopes* (den øverste sektion, ikke under den specifikke klient), så: *Roles → Mappers → client roles → Add to userinfo → ON.*
