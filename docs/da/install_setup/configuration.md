# Serverkonfiguration

Ved at bruge det standard Docker-billede kan al nødvendig konfiguration foretages fra browseren. Afhængigt af implementeringen kan det dog være nødvendigt at tilpasse serverkonfigurationen.

Denne side opregner alle metoder til at ændre konfigurationen og alle eksisterende konfigurationsmuligheder.

## Konfigurationsfil vs. miljøvariabler

Til indstillingerne kan du enten bruge en konfigurationsfil eller miljøvariabler.

Når du bruger den [Docker Compose-baserede opsætning](deployment.md), kan du inkludere en konfigurationsfil ved at tilføje følgende listeelement under `volumes:`-nøglen i `grampsweb:`-blokken:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
hvor `/path/to/config.cfg` er stien til konfigurationsfilen i din servers filsystem (den højre side refererer til stien i containeren og må ikke ændres).

Når du bruger miljøvariabler,

- præfiks hvert indstillingsnavn med `GRAMPSWEB_` for at få navnet på miljøvariablen
- Brug dobbelte understregninger til indstillinger for indlejrede ordbøger, f.eks. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` vil sætte værdien af `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurationsmuligheden

Bemærk, at konfigurationsmuligheder, der er indstillet via miljøet, har forrang over dem i konfigurationsfilen. Hvis begge er til stede, "vinder" miljøvariablen.

## Eksisterende konfigurationsindstillinger
Følgende konfigurationsmuligheder findes.

### Nødvendige indstillinger

Nøgle | Beskrivelse
----|-------------
`TREE` | Navnet på den familie trædatabase, der skal bruges. Vis tilgængelige træer med `gramps -l`. Hvis et træ med dette navn ikke findes, vil et nyt tomt træ blive oprettet.
`SECRET_KEY` | Den hemmelige nøgle til flask. Hemmeligheden må ikke deles offentligt. At ændre den vil ugyldiggøre alle adgangstokens.
`USER_DB_URI` | Database-URL'en til brugerens database. Enhver URL, der er kompatibel med SQLAlchemy, er tilladt.

!!! info
    Du kan generere en sikker hemmelig nøgle f.eks. med kommandoen

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valgfri indstillinger

Nøgle | Beskrivelse
----|-------------
`MEDIA_BASE_DIR` | Sti til at bruge som basisbibliotek for mediefiler, der overskriver det mediebibliotek, der er indstillet i Gramps. Når du bruger [S3](s3.md), skal den have formen `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | Database-URL til søgeindekset. Kun `sqlite` eller `postgresql` er tilladt som backends. Standard til `sqlite:///indexdir/search_index.db`, der opretter en SQLite-fil i mappen `indexdir` i forhold til stien, hvor scriptet køres.
`STATIC_PATH` | Sti til at servere statiske filer fra (f.eks. et statisk webfrontend)
`BASE_URL` | Basis-URL, hvor API'en kan nås (f.eks. `https://mygramps.mydomain.com/`). Dette er nødvendigt f.eks. for at opbygge korrekte links til nulstilling af adgangskoder.
`CORS_ORIGINS` | Oprindelser, hvor CORS-anmodninger er tilladt fra. Som standard er alle forbudt. Brug `"*"` for at tillade anmodninger fra ethvert domæne.
`EMAIL_HOST` | SMTP-servervært (f.eks. til at sende e-mails til nulstilling af adgangskoder)
`EMAIL_PORT` | SMTP-serverport. standard til 465
`EMAIL_HOST_USER` | SMTP-serverbrugernavn
`EMAIL_HOST_PASSWORD` | SMTP-serveradgangskode
`EMAIL_USE_TLS` | Boolean, om der skal bruges TLS til at sende e-mails. Standard til `True`. Når du bruger STARTTLS, skal du sætte dette til `False` og bruge en port forskellig fra 25.
`DEFAULT_FROM_EMAIL` | "Fra" adresse til automatiserede e-mails
`THUMBNAIL_CACHE_CONFIG` | Ordbog med indstillinger for miniaturecache. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`REQUEST_CACHE_CONFIG` | Ordbog med indstillinger for anmodningscachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`PERSISTENT_CACHE_CONFIG` | Ordbog med indstillinger for den vedvarende cache, der bruges f.eks. til telemetri. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`CELERY_CONFIG` | Indstillinger for Celery-baggrundsopgavekøen. Se [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for mulige indstillinger.
`REPORT_DIR` | Midlertidig mappe, hvor output fra kørsel af Gramps-rapporter vil blive gemt
`EXPORT_DIR` | Midlertidig mappe, hvor output fra eksport af Gramps-databasen vil blive gemt
`REGISTRATION_DISABLED` | Hvis `True`, forbyder ny brugerregistrering (standard `False`)
`DISABLE_TELEMETRY` | Hvis `True`, deaktiverer statistiktelemetri (standard `False`). Se [telemetri](telemetry.md) for detaljer.

!!! info
    Når du bruger miljøvariabler til konfiguration, skal boolske indstillinger som `EMAIL_USE_TLS` være enten strengen `true` eller `false` (store og små bogstaver er vigtige!).

### Indstillinger kun for PostgreSQL backend-database

Dette er nødvendigt, hvis du har konfigureret din Gramps-database til at arbejde med [PostgreSQL-tilføjelsen](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Nøgle | Beskrivelse
----|-------------
`POSTGRES_USER` | Brugernavnet til databaseforbindelsen
`POSTGRES_PASSWORD` | Adgangskoden til databasebrugeren

### Indstillinger relevante for hosting af flere træer

Følgende indstillinger er relevante, når du [hoster flere træer](multi-tree.md).

Nøgle | Beskrivelse
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, om der skal bruges en separat undermappe til mediefilerne for hvert træ. Standard til `False`, men det anbefales stærkt at bruge `True` i en multi-tree opsætning.
`NEW_DB_BACKEND` | Den databasebackend, der skal bruges til nyoprettede familietræer. Skal være en af `sqlite`, `postgresql` eller `sharedpostgresql`. Standard til `sqlite`.
`POSTGRES_HOST` | Værtsnavnet på PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-tree opsætning med SharedPostgreSQL-backend.
`POSTGRES_PORT` | Porten på PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-tree opsætning med SharedPostgreSQL-backend.

### Indstillinger for OIDC-godkendelse

Disse indstillinger er nødvendige, hvis du vil bruge OpenID Connect (OIDC) godkendelse med eksterne udbydere. For detaljerede opsætningsinstruktioner og eksempler, se [OIDC-godkendelse](oidc.md).

Nøgle | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC-godkendelse skal aktiveres. Standard til `False`.
`OIDC_ISSUER` | OIDC-udbyderens udsteder-URL (til brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_ID` | OAuth-klient-ID (til brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_SECRET` | OAuth-klienthemmelighed (til brugerdefinerede OIDC-udbydere)
`OIDC_NAME` | Brugerdefineret visningsnavn for udbyderen. Standard til "OIDC"
`OIDC_SCOPES` | OAuth-scopes. Standard til "openid email profile"
`OIDC_USERNAME_CLAIM` | Den påstand, der skal bruges til brugernavnet. Standard til "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valgfri: URL til OpenID Connect konfigurationsendpoint (hvis ikke bruger standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, om lokal brugernavn/adgangskode-godkendelse skal deaktiveres. Standard til `False`
`OIDC_AUTO_REDIRECT` | Boolean, om der skal omdirigeres automatisk til OIDC, når kun én udbyder er konfigureret. Standard til `False`

#### Indbyggede OIDC-udbydere

For indbyggede udbydere (Google, Microsoft, GitHub), brug disse indstillinger:

Nøgle | Beskrivelse
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Klient-ID til Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Klienthemmelighed til Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | Klient-ID til Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Klienthemmelighed til Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | Klient-ID til GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Klienthemmelighed til GitHub OAuth

#### OIDC Rollekortlægning

Disse indstillinger giver dig mulighed for at kortlægge OIDC-grupper/roller fra din identitetsudbyder til Gramps Web-brugerroller:

Nøgle | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på påstanden i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard til "groups"
`OIDC_GROUP_ADMIN` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Admin"-rollen
`OIDC_GROUP_OWNER` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Owner"-rollen
`OIDC_GROUP_EDITOR` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Editor"-rollen
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Contributor"-rollen
`OIDC_GROUP_MEMBER` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Member"-rollen
`OIDC_GROUP_GUEST` | Gruppen/rolenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Guest"-rollen

### Indstillinger kun for AI-funktioner

Disse indstillinger er nødvendige, hvis du vil bruge AI-drevne funktioner som chat eller semantisk søgning.

Nøgle | Beskrivelse
----|-------------
`LLM_BASE_URL` | Basis-URL for den OpenAI-kompatible chat-API. Standard til `None`, som bruger OpenAI API.
`LLM_MODEL` | Modellen, der skal bruges til den OpenAI-kompatible chat-API. Hvis ikke indstillet (standard), er chat deaktiveret.
`VECTOR_EMBEDDING_MODEL` | Den [Sentence Transformers](https://sbert.net/) model, der skal bruges til semantisk søgning vektorindlejringer. Hvis ikke indstillet (standard), er semantisk søgning og chat deaktiveret.
`LLM_MAX_CONTEXT_LENGTH` | Tegngrænse for familietræets kontekst, der gives til LLM. Standard til 50000.

## Eksempel på konfigurationsfil

En minimal konfigurationsfil til produktion kunne se således ud:
```python
TREE="Mit Familietræ"
BASE_URL="https://mitræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # din SMTP-adgangskode
DEFAULT_FROM_EMAIL="gramps@example.com"
