# Serverkonfiguration

Ved at bruge det standard Docker-billede kan al nødvendig konfiguration foretages fra browseren. Afhængigt af implementeringen kan det dog være nødvendigt at tilpasse serverkonfigurationen.

Denne side opregner alle metoder til at ændre konfigurationen og alle eksisterende konfigurationsmuligheder.


## Konfigurationsfil vs. miljøvariabler

Til indstillingerne kan du enten bruge en konfigurationsfil eller miljøvariabler.

Når du bruger den [Docker Compose-baserede opsætning](deployment.md), kan du inkludere en konfigurationsfil ved at tilføje følgende listeelement under `volumes:` nøglen i `grampsweb:` blokken:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
hvor `/path/to/config.cfg` er stien til konfigurationsfilen i din servers filsystem (den højre side henviser til stien i containeren og må ikke ændres).

Når du bruger miljøvariabler,

- præfiks hvert indstillingsnavn med `GRAMPSWEB_` for at få navnet på miljøvariablen
- Brug dobbelte understregninger til indstillinger for indlejrede ordbøger, f.eks. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` vil sætte værdien af `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurationsmuligheden

Bemærk, at konfigurationsmuligheder, der er indstillet via miljøet, har forrang over dem i konfigurationsfilen. Hvis begge er til stede, "vinder" miljøvariablen.

## Eksisterende konfigurationsindstillinger
Følgende konfigurationsmuligheder findes.

### Nødvendige indstillinger

Nøgle | Beskrivelse
----|-------------
`TREE` | Navnet på den familie trædatabase, der skal bruges. Vis tilgængelige træer med `gramps -l`. Hvis et træ med dette navn ikke findes, oprettes et nyt tomt.
`SECRET_KEY` | Den hemmelige nøgle til flask. Den hemmelige nøgle må ikke deles offentligt. Ændring af den vil ugyldiggøre alle adgangstokens.
`USER_DB_URI` | Database-URL'en for brugerens database. Enhver URL, der er kompatibel med SQLAlchemy, er tilladt.

!!! info
    Du kan generere en sikker hemmelig nøgle f.eks. med kommandoen

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valgfri indstillinger

Nøgle | Beskrivelse
----|-------------
`MEDIA_BASE_DIR` | Sti, der skal bruges som basisdirectory for mediefiler, som overskriver den mediebaserede mappe, der er indstillet i Gramps. Når du bruger [S3](s3.md), skal den have formen `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | Database-URL for søgeindekset. Kun `sqlite` eller `postgresql` er tilladt som backends. Standard er `sqlite:///indexdir/search_index.db`, som opretter en SQLite-fil i mappen `indexdir` i forhold til den sti, hvor scriptet køres
`STATIC_PATH` | Sti til at servere statiske filer fra (f.eks. et statisk web frontend)
`BASE_URL` | Basis-URL, hvor API'en kan nås (f.eks. `https://mygramps.mydomain.com/`). Dette er nødvendigt f.eks. for at bygge korrekte links til nulstilling af adgangskoder
`CORS_ORIGINS` | Oprindelser, hvor CORS-anmodninger er tilladt fra. Som standard er alle forbudt. Brug `"*"` for at tillade anmodninger fra ethvert domæne.
`EMAIL_HOST` | SMTP-servervært (f.eks. til at sende e-mails til nulstilling af adgangskoder)
`EMAIL_PORT` | SMTP-serverport. standard er 465
`EMAIL_HOST_USER` | SMTP-serverbrugernavn
`EMAIL_HOST_PASSWORD` | SMTP-serveradgangskode
`EMAIL_USE_TLS` | **Forældet** (brug `EMAIL_USE_SSL` eller `EMAIL_USE_STARTTLS` i stedet). Boolean, om der skal bruges TLS til at sende e-mails. Standard er `True`. Når du bruger STARTTLS, skal du sætte dette til `False` og bruge en port, der er forskellig fra 25.
`EMAIL_USE_SSL` | Boolean, om der skal bruges implicit SSL/TLS til SMTP (v3.6.0+). Standard er `True`, hvis `EMAIL_USE_TLS` ikke er eksplicit indstillet. Typisk brugt med port 465.
`EMAIL_USE_STARTTLS` | Boolean, om der skal bruges eksplicit STARTTLS til SMTP (v3.6.0+). Standard er `False`. Typisk brugt med port 587 eller 25.
`DEFAULT_FROM_EMAIL` | "Fra" adresse til automatiserede e-mails
`THUMBNAIL_CACHE_CONFIG` | Ordbog med indstillinger for thumbnail-cachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`REQUEST_CACHE_CONFIG` | Ordbog med indstillinger for anmodningscachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`PERSISTENT_CACHE_CONFIG` | Ordbog med indstillinger for den vedholdende cache, der bruges f.eks. til telemetri. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`CELERY_CONFIG` | Indstillinger for Celery-baggrundsopgavekøen. Se [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for mulige indstillinger.
`REPORT_DIR` | Midlertidig mappe, hvor output fra kørsel af Gramps-rapporter vil blive gemt
`EXPORT_DIR` | Midlertidig mappe, hvor output fra eksport af Gramps-databasen vil blive gemt
`REGISTRATION_DISABLED` | Hvis `True`, forbyder ny brugerregistrering (standard `False`)
`DISABLE_TELEMETRY` | Hvis `True`, deaktiverer statistiktelemetri (standard `False`). Se [telemetri](telemetry.md) for detaljer.


!!! info
    Når du bruger miljøvariabler til konfiguration, skal booleske indstillinger som `EMAIL_USE_TLS` være enten strengen `true` eller `false` (case sensitive!).


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
`MEDIA_PREFIX_TREE` | Boolean, om der skal bruges en separat undermappe til mediefilerne for hvert træ. Standard er `False`, men det anbefales stærkt at bruge `True` i en multi-tree opsætning
`NEW_DB_BACKEND` | Den databasebackend, der skal bruges til nyoprettede familie træer. Skal være en af `sqlite`, `postgresql` eller `sharedpostgresql`. Standard er `sqlite`.
`POSTGRES_HOST` | Værtsnavnet på PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-tree opsætning med SharedPostgreSQL-backend
`POSTGRES_PORT` | Porten til PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-tree opsætning med SharedPostgreSQL-backend


### Indstillinger for OIDC-godkendelse

Disse indstillinger er nødvendige, hvis du vil bruge OpenID Connect (OIDC) godkendelse med eksterne udbydere. For detaljerede opsætningsinstruktioner og eksempler, se [OIDC-godkendelse](oidc.md).

Nøgle | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC-godkendelse skal aktiveres. Standard er `False`.
`OIDC_ISSUER` | OIDC-udbyderens udsteder-URL (til brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_ID` | OAuth-klient-ID (til brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_SECRET` | OAuth-klienthemmelighed (til brugerdefinerede OIDC-udbydere)
`OIDC_NAME` | Brugerdefineret visningsnavn for udbyderen. Standard er "OIDC"
`OIDC_SCOPES` | OAuth-scopes. Standard er "openid email profile"
`OIDC_USERNAME_CLAIM` | Den påstand, der skal bruges til brugernavnet. Standard er "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valgfri: URL til OpenID Connect-konfigurationsendpointet (hvis ikke bruger standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, om lokal brugernavn/adgangskode-godkendelse skal deaktiveres. Standard er `False`
`OIDC_AUTO_REDIRECT` | Boolean, om der automatisk skal omdirigeres til OIDC, når kun én udbyder er konfigureret. Standard er `False`

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

#### OIDC Rolle Mapping

Disse indstillinger giver dig mulighed for at kortlægge OIDC-grupper/roller fra din identitetsudbyder til Gramps Web-brugerroller:

Nøgle | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på påstanden i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard er "groups"
`OIDC_GROUP_ADMIN` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Admin" rolle
`OIDC_GROUP_OWNER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Owner" rolle
`OIDC_GROUP_EDITOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Editor" rolle
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Contributor" rolle
`OIDC_GROUP_MEMBER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Member" rolle
`OIDC_GROUP_GUEST` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Guest" rolle

### Indstillinger kun for AI-funktioner

Disse indstillinger er nødvendige, hvis du vil bruge AI-drevne funktioner som chat eller semantisk søgning.

Nøgle | Beskrivelse
----|-------------
`LLM_BASE_URL` | Basis-URL for OpenAI-kompatibel chat-API. Standard er `None`, som bruger OpenAI API.
`LLM_MODEL` | Modellen, der skal bruges til OpenAI-kompatibel chat-API. Hvis ikke indstillet (standard), er chat deaktiveret. Fra v3.6.0 bruger AI-assistenten Pydantic AI med værktøjsopkaldsfunktioner.
`VECTOR_EMBEDDING_MODEL` | Den [Sentence Transformers](https://sbert.net/) model, der skal bruges til semantisk søgning vektorembedding. Hvis ikke indstillet (standard), er semantisk søgning og chat deaktiveret.
`LLM_MAX_CONTEXT_LENGTH` | Tegnbegrænsning for familie trækontexten, der gives til LLM. Standard er 50000.
`LLM_SYSTEM_PROMPT` | Brugerdefineret systemprompt til LLM chatassistent (v3.6.0+). Hvis ikke indstillet, bruges den standard genealogi-optimerede prompt.


## Eksempel på konfigurationsfil

En minimal konfigurationsfil til produktion kunne se sådan ud:
```python
TREE="Mit Familie Træ"
BASE_URL="https://mittræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Brug implicit SSL til port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # din SMTP-adgangskode
DEFAULT_FROM_EMAIL="gramps@example.com"
