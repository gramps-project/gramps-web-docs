# OIDC Authentication

Gramps Web understøtter OpenID Connect (OIDC) autentificering, hvilket giver brugerne mulighed for at logge ind ved hjælp af eksterne identitetsudbydere. Dette inkluderer de indbyggede udbydere Google og Microsoft samt brugerdefinerede OIDC-udbydere som Keycloak, Authentik og Authelia.

!!! warning "GitHub som OIDC-udbyder understøttes ikke længere"
    Hvis du har `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` indstillet fra en tidligere version, skal du fjerne dem – de ignoreres nu, og brugere, der tidligere loggede ind via GitHub, kan ikke længere logge ind på den måde. GitHub er en OAuth 2.0-udbyder, ikke en OpenID Connect-udbyder, og returnerede aldrig den påstand, som Gramps Web er afhængig af for identitet, så det var aldrig helt pålideligt.

## Oversigt

OIDC autentificering giver dig mulighed for at:

- Bruge eksterne identitetsudbydere til brugerautentificering
- Understøtte flere autentificeringsudbydere samtidigt
- Kortlægge OIDC grupper/roller til Gramps Web brugerroller
- Implementere Single Sign-On (SSO) og Single Sign-Out
- Valgfrit deaktivere lokal brugernavn/adgangskode autentificering

## Konfiguration

For at aktivere OIDC autentificering skal du konfigurere de relevante indstillinger i din Gramps Web konfigurationsfil eller miljøvariabler. Se siden [Server Configuration](configuration.md#settings-for-oidc-authentication) for en komplet liste over tilgængelige OIDC-indstillinger.

!!! info
    Når du bruger miljøvariabler, skal du huske at præfikse hvert indstillingsnavn med `GRAMPSWEB_` (f.eks. `GRAMPSWEB_OIDC_ENABLED`). Se [Configuration file vs. environment variables](configuration.md#configuration-file-vs-environment-variables) for detaljer.

### Indbyggede Udbydere

Gramps Web har indbygget support for populære identitetsudbydere. For at bruge dem skal du kun angive klient-ID og klienthemmelighed:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` og `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` og `OIDC_MICROSOFT_CLIENT_SECRET`

Du kan konfigurere flere udbydere samtidigt. Systemet vil automatisk registrere, hvilke udbydere der er tilgængelige baseret på konfigurationsværdierne.

!!! tip "Microsoft: single-tenant implementeringer"
    Den indbyggede Microsoft-udbyder bruger multi-tenant `/common` endpointet og accepterer logins fra enhver Microsoft-konto efter design. Hvis du kun vil tillade brugere fra din egen tenant, skal du i stedet bruge [den brugerdefinerede OIDC-udbyder](#custom-oidc-providers) med din tenant-specifikke issuer-URL, hvilket holder issuer-validering aktiv og begrænser logins til den tenant.

### Brugerdefinerede OIDC Udbydere

For brugerdefinerede OIDC-udbydere (som Keycloak, Authentik, Authelia eller en single-tenant Microsoft Entra tenant) skal du bruge disse indstillinger:

Key | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC autentificering skal aktiveres. Sæt til `True`.
`OIDC_ISSUER` | Din udbyders issuer-URL. Discovery hentes fra `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | Klient-ID for din OIDC-udbyder
`OIDC_CLIENT_SECRET` | Klienthemmelighed for din OIDC-udbyder
`OIDC_NAME` | Brugerdefineret visningsnavn (valgfrit, standard til "OIDC")
`OIDC_SCOPES` | OAuth scopes (valgfrit, standard til "openid email profile")
`OIDC_USERNAME_CLAIM` | Påstand brugt til at generere brugernavnet (valgfrit, standard til "preferred_username")
`OIDC_PKCE` | Om der skal bruges PKCE, se [PKCE](#pkce) (valgfrit, aktiveres automatisk, hvis udbyderen understøtter det)

### PKCE

Siden Gramps Web API 3.23 understøtter Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256` metode) for autorisationskodeflowet. Nogle identitetsudbydere, såsom Pocket ID, kan konfigureres til at *kræve* PKCE for en klient og nægte logins, der ikke bruger det. Ældre versioner af Gramps Web API bruger aldrig PKCE, så logins med en sådan klient fejler.

Om PKCE bruges, afgøres ved login som følger:

- Hvis `OIDC_PKCE` er sat til `True`, bruges PKCE.
- Hvis `OIDC_PKCE` er sat til `False`, bruges PKCE ikke, selvom udbyderen understøtter det.
- Hvis `OIDC_PKCE` ikke er sat, eller er sat men tom, bruges PKCE, hvis udbyderens discovery-dokument (`/.well-known/openid-configuration`) viser `S256` i `code_challenge_methods_supported`, og bruges ikke ellers.

For de fleste opsætninger behøver du ikke at sætte noget. Sæt `OIDC_PKCE` til `True`, hvis din udbyder kræver PKCE, men ikke annoncerer `S256` i sit discovery-dokument, og til `False`, hvis din udbyder annoncerer `S256`, men håndterer det forkert. Som miljøvariabler skal booleans være små bogstaver (`GRAMPSWEB_OIDC_PKCE=true`), se [Configuration](configuration.md).

For de indbyggede udbydere er de tilsvarende indstillinger `OIDC_GOOGLE_PKCE` og `OIDC_MICROSOFT_PKCE`.

PKCE kodeverifikatoren opbevares i brugerens session mellem omdirigeringen til udbyderen og callbacken, så dette kræver ingen ændringer til omdirigerings-URI'erne.

### Multi-Tree Opsætninger

På en multi-tree server logges en bruger, der logger ind med en identitet, der allerede er knyttet til en Gramps Web-konto, ind i den konto's træ, så den almindelige login-side fungerer for dem.

For at oprette en *ny* konto med en OIDC-identitet skal Gramps Web vide, hvilket træ den skal tilhøre. Nye brugere skal derfor starte fra træets registreringslink (`/register/<tree_id>`, se [Registration link](../administration/users.md#registration-link-multi-tree-setup-only)), eller fra login-siden for træet (`/login/<tree_id>`). Begge tilbyder de konfigurerede udbydere. At logge ind med en ukendt identitet fra den almindelige login-side nægtes med en besked, der peger på registreringslinket. Dette kræver Gramps Web API 3.25.3 og Gramps Web 26.11.2 eller nyere.

Bag kulisserne starter login med:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

hvor `tree` er valgfrit, medmindre en ny konto oprettes. At sende ID'en for et træ, der ikke eksisterer, fejler login. På en single-tree server er `tree` valgfrit, men hvis det gives, skal det matche den konfigurerede `TREE`.

En OIDC-identitet er bundet til præcist én Gramps Web-konto, som igen tilhører præcist ét træ – at logge ind mod et andet træ fejler i stedet for at flytte kontoen. Der er ingen måde at knytte en enkelt identitet hos udbyderen til konti i flere træer; brugere, der har brug for adgang til flere træer, har brug for separate identiteter hos udbyderen (f.eks. forskellige brugernavne eller konti).

!!! warning
    En site-administrator konto uden tilknyttet træ (se [creating an admin account](../administration/owner.md)) kan ikke oprettes via OIDC, da en konto oprettet ved en OIDC-login altid tilhører et træ. Opret sådanne konti med et lokalt brugernavn og adgangskode.

### Native apps

Native apps, såsom mobilapps til Gramps Web, kan lade brugeren logge ind i systembrowseren og modtage resultatet ved en `https` link til appen. Siden Gramps Web API 3.26 fungerer dette, hvis linket er angivet i `OIDC_ALLOWED_REDIRECT_URIS`, f.eks.

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

Appens dokumentation fortæller dig, hvilket link der skal tilføjes. De omdirigerings-URI'er, der er registreret hos identitetsudbyderen, forbliver de samme.

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

Gramps Web kan automatisk kortlægge OIDC grupper eller roller fra din identitetsudbyder til Gramps Web brugerroller. Dette giver dig mulighed for at administrere brugerrettigheder centralt i din identitetsudbyder. Rolle kortlægning fungerer på samme måde for alle udbydere, indbyggede eller brugerdefinerede.

### Konfiguration

Brug disse indstillinger til at konfigurere rolle kortlægning:

Key | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på påstanden i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard til "groups". Prikkede stier understøttes, f.eks. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Admin" rolle
`OIDC_GROUP_OWNER` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Owner" rolle
`OIDC_GROUP_EDITOR` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Editor" rolle
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Contributor" rolle
`OIDC_GROUP_MEMBER` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Member" rolle
`OIDC_GROUP_GUEST` | Gruppen/rollenavn fra din OIDC-udbyder, der kortlægges til Gramps "Guest" rolle

### Rolle Kortlægningsadfærd

Hvis ingen `OIDC_GROUP_*` indstilling er konfigureret overhovedet, er rolle kortlægning slået fra, og roller administreres manuelt i Gramps Web; nye OIDC-konti oprettes derefter deaktiveret og skal godkendes af en eksisterende ejer eller administrator (se [First Login and Bootstrapping](#first-login-and-bootstrapping) nedenfor).

Når rolle kortlægning er konfigureret, ved hver login:

- Hvis rolle-påstanden er til stede, og brugeren tilhører en kortlagt gruppe, får de den tilsvarende rolle.
- Hvis rolle-påstanden er til stede, men brugeren tilhører ingen kortlagt gruppe, sættes deres rolle til deaktiveret. Dette er en fail-closed standard, ikke en fejl – Gramps Web kan ikke udlede en rolle for en gruppe, den ikke genkender.
- Hvis rolle-påstanden er helt fraværende fra tokenet, forbliver den eksisterende rolle uændret; en ny konto standardiseres stadig til deaktiveret.

!!! warning "Google sender ikke en grupper påstand"
    Googles tokens inkluderer aldrig en `groups` påstand, så med rolle kortlægning aktiveret falder Google-logins ind under "påstand fraværende" ovenfor: eksisterende brugere beholder deres rolle, men nye Google-brugere oprettes deaktiveret og kræver manuel godkendelse. Husk dette, før du aktiverer rolle kortlægning kun for en anden udbyder – det deaktiverer ikke i sig selv eksisterende Google-brugere.

Microsoft Entra returnerer app-roller og gruppe-medlemskaber kun i ID-tokenet, ikke fra userinfo-endpointet. Gramps Web fletter ID-tokenets påstande ind i userinfo-svaret, så `OIDC_ROLE_CLAIM` fungerer på samme måde som for andre udbydere; hvor begge indeholder en påstand, har userinfo-værdien forrang.

## Første Login og Bootstrapping

Nye konti oprettet gennem OIDC starter deaktiverede, medmindre rolle kortlægning tildeler dem en rolle (se ovenfor). På en helt ny instans kan ingen godkende en deaktiveret konto, og hvis `OIDC_DISABLE_LOCAL_AUTH` også er aktiveret, er der heller ikke nogen adgangskode-login at falde tilbage på.

!!! warning "Konfigurer en ejer/admin gruppe før første login"
    Før nogen logger ind via OIDC for første gang, skal du indstille `OIDC_GROUP_OWNER` (eller `OIDC_GROUP_ADMIN`) og sikre, at den første bruger tilhører den gruppe hos udbyderen. Ellers kan instansen slet ikke bootstrappes gennem OIDC.

## Konti og Brugernavne

Konti oprettet gennem OIDC får et genereret brugernavn, der tildeles én gang ved kontooprettelsen og aldrig ændres ved senere logins:

- Indbyggede udbydere: `<provider>_<claim value>`, f.eks. `microsoft_alice@contoso.com`
- Brugerdefineret udbyder: den bare påstandsværdi, f.eks. `alice`

Et numerisk suffiks tilføjes ved kollision. Der er ingen måde at omdøbe et OIDC-oprettet kontos brugernavn bagefter; det fulde navn og e-mailadresse opdateres derimod ved hver login.

Et OIDC-login knytter sig aldrig til en eksisterende lokal konto, der tilfældigvis deler sin e-mailadresse – dette er bevidst, da linking af konti via e-mail er en konto-overtagelsesvektor. En bruger, der allerede har en lokal konto, får en anden, separat konto første gang de logger ind via OIDC, medmindre de først knytter udbyderen til deres konto.

Siden Gramps Web API 3.24 kan brugere knytte OIDC-identiteter til deres eksisterende konto og liste og unlinke dem under [User Settings > Linked sign-in methods](../user-guide/settings.md#linked-sign-in-methods). Linking kræver en nylig login og bekræftes med brugerens egen token, så det fungerer også, når frontend er på en anden oprindelse end API'et. En identitet kan kun tilhøre én konto; for at knytte en, der allerede har sin egen konto, skal en administrator først slette den konto (dens redigeringer forbliver, men revisionshistorikken viser ikke længere dens navn). Den sidst knyttede identitet kan kun unlinkes med kontoens nuværende adgangskode, og slet ikke hvis `OIDC_DISABLE_LOCAL_AUTH` er indstillet.

E-mailadresser fra udbyderen gemmes kun, hvis udbyderen markerer dem som verificerede (eller udelader `email_verified` påstanden helt); ellers fortsætter login uden at gemme en e-mailadresse. Da e-mailadresser ikke skal være unikke (siden Gramps Web API 3.22), gemmes en adresse, selvom en anden konto allerede bruger den.

## OIDC Logout

Gramps Web understøtter Single Sign-Out (SSO logout) for OIDC-udbydere. `GET /api/oidc/logout/` slår op i udbyderens `end_session_endpoint` og returnerer det som `logout_url` i svaret; det er Gramps Web frontend, der navigerer browseren derhen for faktisk at afslutte sessionen hos identitetsudbyderen. `logout_url` er `null`, når udbyderen ikke har nogen `end_session_endpoint`.

!!! warning "Tokens tilbagekaldes ikke ved logout"
    At logge ud afslutter kun browser-sessionen; der er i øjeblikket ingen måde at tilbagekalde et Gramps Web-token, der allerede er blevet udstedt. Tokens forbliver gyldige, indtil de udløber (`JWT_ACCESS_TOKEN_EXPIRES`, standard 15 minutter for adgangstokens), uanset om brugeren siden har logget ud hos Gramps Web eller hos identitetsudbyderen.

## Fejlfinding

Start ved det punkt, hvor login stopper, og følg grenen. Gramps Web logger årsagen til en mislykket callback (se efter `OIDC callback error for provider` i serverloggen), som normalt er mere specifik end den besked, der vises i browseren.

**1. Mangler login-knappen?**

- Tjek `<BASE_URL>/api/oidc/config/`. Hvis `enabled` er `false` eller `providers` er tom, er OIDC ikke konfigureret: `OIDC_ENABLED` skal være `True`, og en brugerdefineret udbyder har brug for både `OIDC_ISSUER` og `OIDC_CLIENT_ID`.
- En indbygget udbyder (Google, Microsoft) er kun registreret, hvis både dens klient-ID og dens klienthemmelighed er indstillet.
- Se i serverloggen ved opstart efter `Could not load discovery document`. Dette betyder, at serveren ikke kunne nå `<issuer>/.well-known/openid-configuration` (eller `OIDC_OPENID_CONFIG_URL`). Den prøver igen ved første brug, men Gramps Web-containeren skal selv kunne løse og nå issuer-URL'en, ikke kun din browser.

**2. Får browseren en fejl lige efter at være sendt til udbyderen?**

Fejlen vises af identitetsudbyderen, før du logger ind.

- *"redirect URI mismatch"* (eller lignende): den omdirigerings-URI, der er registreret hos udbyderen, skal matche præcist, inklusive skema, vært, port og udbyder-ID. Se [Required Redirect URIs](#required-redirect-uris). Bemærk, at den er bygget fra `BASE_URL`, så en forkert `BASE_URL` giver en forkert omdirigerings-URI.
- *En PKCE-fejl* (for eksempel `invalid_request`, "code challenge required", eller en manglende `code_challenge` parameter): udbyderen kræver PKCE, men Gramps Web sendte det ikke. Gå til [PKCE-grenen](#pkce-branch) nedenfor.

**3. Accepterer udbyderen login, men Gramps Web viser derefter en fejl?**

- *`mismatching_state`, eller fejlen nævner sessionen eller tilstanden*: browseren sendte ikke session-cookien tilbage, som Gramps Web satte, da login startede. Denne cookie bærer også PKCE kodeverifikatoren. Sørg for, at adressen i browseren matcher `BASE_URL` (samme skema og vært), at en reverse proxy sender cookies og den originale vært igennem, og at login startes og afsluttes i den samme browserfane eller vindue.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: tjek serverloggen for den underliggende årsag. Almindelige årsager er en forkert klienthemmelighed, en issuer-URL, der ikke matcher `iss` påstanden i tokens, og udbyderen, der returnerer en fejl til callbacken (for eksempel PKCE, se nedenfor).
- *For mange forsøg*: login- og callback-endepunkterne er hastighedsbegrænsede (5 anmodninger pr. minut). Vent et minut og prøv igen.

**4. Lykkes login, men du ser "Account Under Review", eller kan ikke gøre noget?**

Nye konti oprettes deaktiverede, medmindre rolle kortlægning tildeler en rolle. Se [First Login and Bootstrapping](#first-login-and-bootstrapping) og [Role Mapping Behavior](#role-mapping-behavior). En administrator kan også aktivere kontoen under Indstillinger > Administration > Administrer brugere.

### PKCE-gren

Gramps Web beslutter, om der skal bruges PKCE, når et login starter (se [PKCE](#pkce)). For at finde ud af, hvad der skete for din opsætning, skal du arbejde igennem disse spørgsmål i rækkefølge:

1. **Er `OIDC_PKCE` sat?** (For indbyggede udbydere, `OIDC_GOOGLE_PKCE` eller `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE bruges. Spring til spørgsmål 3.
    - `False`: PKCE er bevidst slået fra, og udbyderens discovery-dokument ignoreres. Hvis din udbyder kræver PKCE, skal du fjerne indstillingen eller sætte den til `True`.
    - Ikke sat, eller tom: fortsæt med spørgsmål 2.
2. **Lister discovery-dokumentet `S256`?** Åbn `<issuer>/.well-known/openid-configuration` og se efter `S256` i `code_challenge_methods_supported`.
    - Ja: PKCE bruges automatisk. Fortsæt med spørgsmål 3.
    - Nej, eller feltet mangler: PKCE er **ikke** brugt. Sæt `OIDC_PKCE` til `True`, hvis din udbyder kræver det. Tjek også serverloggen for `Could not check the provider for PKCE support`, hvilket betyder, at discovery-dokumentet ikke kunne hentes, og PKCE derfor blev slået fra.
3. **Blev PKCE virkelig sendt?** Start et login og se på adressen til udbyderens login-side (eller den første omdirigering i din browsers netværksfaneblad). Den skal indeholde `code_challenge=` og `code_challenge_method=S256`.
    - Tilstede, men login fejler stadig ved callbacken: udbyderen afviste kodeverifikatoren. Session-cookien kan være gået tabt mellem omdirigeringen og callbacken (se gren 3 ovenfor), eller udbyderen understøtter ikke `S256`, i hvilket tilfælde du skal sætte `OIDC_PKCE` til `False`, hvis udbyderen ikke kræver PKCE.
    - Fraværende: de ovenstående indstillinger blev ikke anvendt. Tjek, at miljøvariablen har det rigtige præfiks og en lille værdi (for eksempel `GRAMPSWEB_OIDC_PKCE=true` i Docker; `True` læses ikke som en boolean), genstart serveren, og se på konfigurationen igen.

!!! note
    Med PKCE aktiveret hos udbyderen som *valgfrit*, eller slet ikke aktiveret, fungerer logins, uanset om Gramps Web sender en udfordring. Kun udbydere (eller klienter), der er konfigureret til *at kræve* PKCE, gør denne indstilling vigtig.

## Eksempel Konfigurationer

### Brugerdefineret OIDC Udbyder (Keycloak)

```python
TREE="Mit Familie Træ"
BASE_URL="https://mittræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Brugerdefineret OIDC Konfiguration
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="din-klient-hemmelighed"
OIDC_NAME="Familie SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Valgfrit: automatisk omdirigering til SSO login
OIDC_DISABLE_LOCAL_AUTH=True  # Valgfrit: deaktivere brugernavn/adgangskode login

# Valgfrit: Rolle kortlægning fra OIDC grupper til Gramps roller
OIDC_ROLE_CLAIM="groups"  # eller "roles" afhængigt af din udbyder
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Brug implicit SSL til port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # din SMTP adgangskode
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Indbygget Udbyder (Google)

```python
TREE="Mit Familie Træ"
BASE_URL="https://mittræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="din-google-klient-id"
OIDC_GOOGLE_CLIENT_SECRET="din-google-klient-hemmelighed"
```

### Flere Udbydere

Du kan aktivere flere OIDC-udbydere samtidigt:

```python
TREE="Mit Familie Træ"
BASE_URL="https://mittræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Brugerdefineret udbyder
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="din-klient-hemmelighed"
OIDC_NAME="Firma SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="din-google-klient-id"
OIDC_GOOGLE_CLIENT_SECRET="din-google-klient-hemmelighed"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="din-microsoft-klient-id"
OIDC_MICROSOFT_CLIENT_SECRET="din-microsoft-klient-hemmelighed"
```

### Pocket ID

Opret en OIDC-klient i Pocket ID med omdirigerings-URI `<BASE_URL>/api/oidc/callback/custom` (se [Required Redirect URIs](#required-redirect-uris)). Hvis du aktiverer "Require PKCE" for klienten, er der ikke behov for yderligere Gramps Web-konfiguration, da Pocket ID annoncerer PKCE-understøttelse i sit discovery-dokument. Konfigurer derefter:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<klient id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<klient hemmelighed>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

En community-lavet OIDC opsætningsguide til Gramps Web er tilgængelig på [den officielle Authelia dokumentations hjemmeside](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Det meste af konfigurationen for Keycloak kan efterlades på standardindstillingerne (*Client → Create client → Client authentication ON*).
Der er et par undtagelser:

1. **OpenID scope** – `openid` scope er ikke inkluderet som standard i alle Keycloak-versioner. For at undgå problemer, tilføj det manuelt: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Roller** – Roller kan tildeles enten på klientniveau eller globalt pr. realm.

    * Hvis du bruger klientroller, skal du indstille `OIDC_ROLE_CLAIM` konfigurationsmuligheden til: `resource_access.[gramps-client-name].roles`
    * For at gøre roller synlige for Gramps, naviger til *Client Scopes* (den øverste sektion, ikke under den specifikke klient), derefter: *Roles → Mappers → client roles → Add to userinfo → ON.*
