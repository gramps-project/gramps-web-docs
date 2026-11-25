# Serverkonfiguration

Ved brug af standard-Docker-imaget kan al nødvendig konfiguration foretages fra browseren. Afhængigt af implementeringen kan det dog være nødvendigt at tilpasse serverkonfigurationen.

Denne side viser alle metoder til at ændre konfigurationen samt alle eksisterende konfigurationsindstillinger.


## Konfigurationsfil kontra miljøvariabler

For indstillingerne kan du enten bruge en konfigurationsfil eller miljøvariabler.

Når du bruger den [Docker Compose-baserede opsætning](deployment.md), kan du inkludere en konfigurationsfil ved at tilføje følgende listeelement under nøglen `volumes:` i blokken `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
hvor `/path/to/config.cfg` er stien til konfigurationsfilen i din servers filsystem (højre side henviser til stien i containeren og må ikke ændres).

Når du bruger miljøvariabler,

- skal du præfikse hvert indstillingsnavn med `GRAMPSWEB_` for at få navnet på miljøvariablen
- skal du bruge dobbelte understregninger til indlejrede ordbogsindstillinger, f.eks. vil `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` angive værdien for konfigurationsindstillingen `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Bemærk, at konfigurationsindstillinger, der angives via miljøet, har forrang for dem i konfigurationsfilen. Hvis begge findes, vinder miljøvariablen.

!!! warning "Miljøvariabler uden præfiks er forældede"
    Af historiske årsager kan en håndfuld indstillinger – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` og `STATIC_PATH` – stadig angives via en miljøvariabel *uden* præfikset `GRAMPSWEB_`. Dette er forældet, medfører en advarsel i loggen ved opstart og vil ophøre med at fungere i en fremtidig version. Brug altid formen med præfiks, f.eks. `GRAMPSWEB_TREE` i stedet for `TREE`.

    Bemærk, at dette kun vedrører miljøvariabler. I en konfigurationsfil bruges indstillingsnavnene altid uden præfiks.

!!! tip "Kontrol af forældede indstillinger"
    Forældede konfigurationsindstillinger, som din server stadig er afhængig af – f.eks. miljøvariabler uden præfiks, `SEARCH_INDEX_DIR` eller `EMAIL_USE_TLS` – logges som advarsler ved opstart. Siden Gramps Web API 3.22 vises de også sammen med deres erstatning og den version, hvor understøttelsen fjernes, øverst på siden **Systemoplysninger** (tilgængelig via brugerikonet i den øverste applinje), når du er logget ind som administrator.

    E-mailindstillingerne og basis-URL'en, som førstegangsopsætningsguiden i ældre versioner gemte i databasen, vises også dér. Angiv dem i din konfiguration med de gemte værdier; advarslen forsvinder, når de stemmer overens.

## Eksisterende konfigurationsindstillinger
Følgende konfigurationsindstillinger findes.

### Påkrævede indstillinger

Nøgle | Beskrivelse
----|-------------
`TREE` | Navnet på den familietredatabase, der skal bruges. Vis tilgængelige træer med `gramps -l`. Hvis der ikke findes et træ med dette navn, oprettes et nyt, tomt træ.
`SECRET_KEY` | Den hemmelige nøgle til flask. Hemmeligheden må ikke deles offentligt. Hvis du ændrer den, ugyldiggøres alle adgangstokens.
`USER_DB_URI` | Database-URL'en til brugerdatabasen. Alle URL'er, der er kompatible med SQLAlchemy, er tilladt.

!!! info
    Du kan generere en sikker hemmelig nøgle, f.eks. med kommandoen

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valgfrie indstillinger

Nøgle | Beskrivelse
----|-------------
`MEDIA_BASE_DIR` | Sti, der skal bruges som basismappe for mediefiler, og som tilsidesætter den mediebasismappe, der er angivet i Gramps. Ved brug af [S3](s3.md) skal den have formen `s3://<bucket_name>`
`TREE_ID` | Mappenavnet på den familietredatabase, der skal bruges i enkelttræstilstand (når `TREE` ikke er angivet til `*`). Når den er angivet, identificerer serveren træet via mappenavnet i stedet for visningsnavnet, hvilket er mere robust over for omdøbninger. Påkrævet, hvis du vil omdøbe træet via API'et. Mappenavnet kan findes via `GET /api/trees/-` (feltet `id`).
`SEARCH_INDEX_DB_URI` | Database-URL til søgeindekset. Kun `sqlite` eller `postgresql` er tilladt som backends. Standardværdien er `sqlite:///indexdir/search_index.db`, hvilket opretter en SQLite-fil i mappen `indexdir` i forhold til den sti, hvor scriptet køres
`SEARCH_INDEX_DIR` | **Forældet** (brug `SEARCH_INDEX_DB_URI` i stedet). Mappe, der indeholder søgeindekset. Hvis den er angivet, mens `SEARCH_INDEX_DB_URI` ikke er angivet, udledes søgeindeksets URL som `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Sti, som statiske filer skal leveres fra (f.eks. en statisk webfrontend)
`BASE_URL` | Basis-URL, hvor API'et kan nås (f.eks. `https://mygramps.mydomain.com/`). Dette er f.eks. nødvendigt for at opbygge korrekte links til nulstilling af adgangskoder. Web Push kræver også en offentligt tilgængelig HTTPS-URL; standardværdien `http://localhost/` deaktiverer Web Push. Når du konfigurerer denne indstilling via miljøet, skal du bruge `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Oprindelser, som CORS-anmodninger må komme fra. Som standard afvises alle. Brug `"*"` for at tillade anmodninger fra alle domæner.
`EMAIL_HOST` | SMTP-serverens vært (f.eks. til afsendelse af e-mails med links til nulstilling af adgangskoder)
`EMAIL_PORT` | SMTP-serverens port. Standardværdien er 465
`EMAIL_HOST_USER` | SMTP-serverens brugernavn
`EMAIL_HOST_PASSWORD` | SMTP-serverens adgangskode
`EMAIL_USE_TLS` | **Forældet** (brug `EMAIL_USE_SSL` eller `EMAIL_USE_STARTTLS` i stedet). Boolsk værdi, der angiver, om TLS skal bruges til afsendelse af e-mails. Standardværdien er `True`. Ved brug af STARTTLS skal du angive dette til `False` og bruge en anden port end 25.
`EMAIL_USE_SSL` | Boolsk værdi, der angiver, om implicit SSL/TLS skal bruges til SMTP (v3.6.0+). Standardværdien er `True`, hvis `EMAIL_USE_TLS` ikke er angivet eksplicit. Bruges typisk med port 465.
`EMAIL_USE_STARTTLS` | Boolsk værdi, der angiver, om eksplicit STARTTLS skal bruges til SMTP (v3.6.0+). Standardværdien er `False`. Bruges typisk med port 587 eller 25.
`DEFAULT_FROM_EMAIL` | "Fra"-adresse til automatiske e-mails
`THUMBNAIL_CACHE_CONFIG` | Ordbog med indstillinger for miniaturecachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`REQUEST_CACHE_CONFIG` | Ordbog med indstillinger for cachelagring af anmodninger. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`PERSISTENT_CACHE_CONFIG` | Ordbog med indstillinger for den permanente cache, der f.eks. bruges til telemetri. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`CELERY_CONFIG` | Indstillinger for Celery-køen til baggrundsopgaver. Se [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for mulige indstillinger.
`REPORT_DIR` | Midlertidig mappe, hvor outputtet fra kørsel af Gramps-rapporter gemmes
`EXPORT_DIR` | Midlertidig mappe, hvor outputtet fra eksport af Gramps-databasen gemmes
`BACKUP_DIR` | Mappe, hvor [sikkerhedskopier](../administration/backups.md) gemmes, i en undermappe pr. træ (v3.24.0+). Hvis den ikke er angivet (standardværdien), kan sikkerhedskopier ikke gemmes på serveren, men de kan stadig gendannes fra en uploadet fil. Brug en permanent placering, f.eks. en Docker-diskenhed, og helst en placering, der selv sikkerhedskopieres eller synkroniseres et andet sted.
`BACKUP_KEEP` | Antallet af gemte sikkerhedskopier, der bevares pr. træ; ældre sikkerhedskopier slettes, når en ny sikkerhedskopi oprettes (v3.24.0+). Standardværdien er `5`
`RATE_LIMIT_BACKUP` | Hastighedsbegrænsning for oprettelse af sikkerhedskopier pr. træ (v3.24.0+). Standardværdien er `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Hastighedsbegrænsning for oprettelse af mediearkiver på eksportsiden. Standardværdien er `"1 per hour"`
`REGISTRATION_DISABLED` | Hvis `True`, deaktiveres registrering af nye brugere (standardværdien er `False`). Siden Gramps Web API 3.26 skjuler login-siden derefter også sit registreringslink.
`PROXY_FIX_X_FOR` | Antallet af betroede reverse proxy-servere foran Gramps Web (v3.26.0+). Angiv `1` bag en enkelt reverse proxy, så hastighedsbegrænsninger gælder pr. klient i stedet for alle brugere samlet. Standardværdien er `0`. Angiv den kun, hvis serveren udelukkende er tilgængelig via disse proxyservere.
`DISABLE_TELEMETRY` | Hvis `True`, deaktiveres statistiktelemetri (standardværdien er `False`). Se [telemetri](telemetry.md) for detaljer.
`PILLOW_MAX_IMAGE_PIXELS` | Angiver parameteren PIL.Image.MAX_IMAGE_PIXELS, som angiver det antal pixels, det behandlede billede må indeholde. Se [dokumentationen](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) for detaljer.
`MAX_THUMBNAIL_FILE_BYTES` | Angiver en absolut maksimal filstørrelse for miniaturer. Standardværdien er `50 * 1024 * 1024` (50 MB). Hvis værdien hæves, kan hukommelsesforbruget stige kraftigt og medføre nedbrud på grund af manglende hukommelse eller datatab, hvis store filer dekomprimeres i hukommelsen.


!!! info
    Når du bruger miljøvariabler til konfiguration, skal booleske indstillinger som `EMAIL_USE_SSL` være enten strengen `true` eller `false` (forskel på store og små bogstaver!).


### Indstillinger for PostgreSQL-databaser

Disse indstillinger er påkrævede, hvis dine familietræer hostes i en [PostgreSQL-database](postgres.md) ved hjælp af tilføjelsesprogrammet SharedPostgreSQL.

Nøgle | Beskrivelse
----|-------------
`POSTGRES_USER` | Brugernavnet til databaseforbindelsen
`POSTGRES_PASSWORD` | Adgangskoden til databasebrugeren


### Indstillinger, der er relevante ved hosting af flere træer

Følgende indstillinger er relevante, når du [hoster flere træer](multi-tree.md).


Nøgle | Beskrivelse
----|-------------
`MEDIA_PREFIX_TREE` | Boolsk værdi, der angiver, om der skal bruges en separat undermappe til hvert træs mediefiler. Standardværdien er `False`, men det anbefales kraftigt at bruge `True` i en opsætning med flere træer
`NEW_DB_BACKEND` | Den databasebackend, der skal bruges til nyoprettede familietræer. Skal være enten `sqlite` eller `sharedpostgresql`. Standardværdien er `sqlite`. Værdien `postgresql` accepteres stadig, men er forældet, da PostgreSQL-backenden fjernes i Gramps Web API 4.0.
`POSTGRES_HOST` | Værtsnavnet på PostgreSQL-serveren, der bruges til oprettelse af nye træer ved brug af en opsætning med flere træer og SharedPostgreSQL-backenden
`POSTGRES_PORT` | Porten på PostgreSQL-serveren, der bruges til oprettelse af nye træer ved brug af en opsætning med flere træer og SharedPostgreSQL-backenden


### Indstillinger for OIDC-godkendelse

Disse indstillinger er nødvendige, hvis du vil bruge OpenID Connect-godkendelse (OIDC) med eksterne udbydere. Se [OIDC-godkendelse](oidc.md) for detaljerede opsætningsinstruktioner og eksempler.

Nøgle | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolsk værdi, der angiver, om OIDC-godkendelse skal aktiveres. Standardværdien er `False`.
`OIDC_ISSUER` | URL til OIDC-udbyderens issuer (for brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_ID` | OAuth-klient-ID (for brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_SECRET` | OAuth-klienthemmelighed (for brugerdefinerede OIDC-udbydere)
`OIDC_NAME` | Brugerdefineret visningsnavn for udbyderen. Standardværdien er "OIDC"
`OIDC_SCOPES` | OAuth-scopes. Standardværdien er "openid email profile"
`OIDC_USERNAME_CLAIM` | Det claim, der skal bruges til brugernavnet. Standardværdien er "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valgfrit: URL til OpenID Connect-konfigurationens endpoint (hvis standarden `/.well-known/openid-configuration` ikke bruges)
`OIDC_PKCE` | Boolsk værdi, der angiver, om PKCE skal bruges. Hvis den ikke angives, bruges PKCE, når udbyderens discovery-dokument angiver `S256`. Se [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolsk værdi, der angiver, om lokal brugernavns-/adgangskodegodkendelse skal deaktiveres. Standardværdien er `False`
`OIDC_AUTO_REDIRECT` | Boolsk værdi, der angiver, om der automatisk skal omdirigeres til OIDC, når kun én udbyder er konfigureret. Standardværdien er `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Liste over `https`-URI'er, hvor native apps kan modtage loginresultatet (v3.26.0+), angivet som en JSON-liste i en miljøvariabel. Tom som standard. Kun nødvendig, hvis dokumentationen til en native app beder om det. Se [Native apps](oidc.md#native-apps)

#### Indbyggede OIDC-udbydere

For indbyggede udbydere (Google, Microsoft) skal du bruge disse indstillinger:

Nøgle | Beskrivelse
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Klient-ID til Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Klienthemmelighed til Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | Klient-ID til Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Klienthemmelighed til Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Boolsk PKCE-indstilling for Google, se [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolsk PKCE-indstilling for Microsoft, se [PKCE](oidc.md#pkce)

#### OIDC-rolletilknytning

Med disse indstillinger kan du knytte OIDC-grupper/roller fra din identitetsudbyder til Gramps Web-brugerroller:

Nøgle | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Claim-navnet i OIDC-tokenet, der indeholder brugerens grupper/roller. Standardværdien er "groups"
`OIDC_GROUP_ADMIN` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Admin"
`OIDC_GROUP_OWNER` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Owner"
`OIDC_GROUP_EDITOR` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Editor"
`OIDC_GROUP_CONTRIBUTOR` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Contributor"
`OIDC_GROUP_MEMBER` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Member"
`OIDC_GROUP_GUEST` | Gruppe-/rollenavnet fra din OIDC-udbyder, der knyttes til Gramps-rollen "Guest"

### Indstillinger kun til AI-funktioner

Disse indstillinger er nødvendige, hvis du vil bruge AI-chat. Se [Opsætning af AI-chat](chat.md) for detaljer.

!!! note
    Indstillingerne `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` og `VECTOR_EMBEDDING_API_KEY` til semantisk søgning ignoreres siden Gramps Web API 3.25, hvor semantisk søgning blev fjernet. AI-chat kræver kun `LLM_MODEL`.

Nøgle | Beskrivelse
----|-------------
`LLM_BASE_URL` | Basis-URL til den OpenAI-kompatible chat-API. Standardværdien er `None`, hvilket bruger OpenAI API'et.
`LLM_MODEL` | Den model, der skal bruges til den OpenAI-kompatible chat-API. Hvis den ikke er angivet (standardværdien), er chat deaktiveret. Fra og med v3.6.0 bruger AI-assistenten Pydantic AI med funktioner til kald af værktøjer.
`LLM_MAX_OUTPUT_TOKENS` | Det maksimale antal tokens, modellen må generere i et enkelt svar. Ikke angivet som standard, så begrænsningen overlades til modelserveren. Nyttigt til modelservere uden egen begrænsning, hvor et svar ellers kunne fortsætte uendeligt.
`LLM_MAX_CONTEXT_LENGTH` | Tegngrænsen for den familietræskontekst, der leveres til LLM'en. Standardværdien er 50000.
`LLM_SYSTEM_PROMPT` | Brugerdefineret systemprompt til LLM-chatassistenten (v3.6.0+). Hvis den ikke er angivet, bruges standardprompten, der er optimeret til slægtsforskning.
`LLM_VISION` | Boolsk værdi, der angiver, om brugere kan vedhæfte billeder til deres spørgsmål (v3.26.0+). Aktivér den kun, hvis modellen accepterer billeder. Standardværdien er `False`. Se [Billeder i spørgsmål](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Boolsk værdi, der angiver, om assistenten kan foreslå ændringer til træet, som brugerne kan gennemgå og anvende (v3.26.0+). Standardværdien er `False`. Se [Lad assistenten foreslå ændringer](chat.md#letting-the-assistant-propose-changes)


## Eksempel på konfigurationsfil

En minimal konfigurationsfil til produktion kunne se sådan ud:
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
