# Serverkonfiguration

Ved at bruge det standard Docker-billede kan al nødvendig konfiguration foretages fra browseren. Afhængigt af implementeringen kan det dog være nødvendigt at tilpasse serverkonfigurationen.

Denne side lister alle metoder til at ændre konfigurationen og alle eksisterende konfigurationsmuligheder.


## Konfigurationsfil vs. miljøvariabler

Til indstillingerne kan du enten bruge en konfigurationsfil eller miljøvariabler.

Når du bruger [Docker Compose-baseret opsætning](deployment.md), kan du inkludere en konfigurationsfil ved at tilføje følgende listeelement under `volumes:`-nøglen i `grampsweb:`-blokken:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
hvor `/path/to/config.cfg` er stien til konfigurationsfilen i din servers filsystem (den højre side refererer til stien i containeren og må ikke ændres).

Når du bruger miljøvariabler,

- præfiks hvert indstillingsnavn med `GRAMPSWEB_` for at opnå navnet på miljøvariablen
- Brug dobbelte understregninger til indstillinger for indlejrede ordbøger, f.eks. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` vil sætte værdien af konfigurationsmuligheden `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Bemærk, at konfigurationsmuligheder, der er indstillet via miljøet, har forrang over dem i konfigurationsfilen. Hvis begge er til stede, "vinder" miljøvariablen.

!!! warning "Uden præfiks miljøvariabler er forældede"
    Af historiske grunde kan en håndfuld indstillinger – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` og `STATIC_PATH` – stadig indstilles via en miljøvariabel *uden* `GRAMPSWEB_` præfikset. Dette er forældet, logger en advarsel ved opstart, og vil stoppe med at fungere i en fremtidig version. Brug altid den præfikserede form, f.eks. `GRAMPSWEB_TREE` i stedet for `TREE`.

    Bemærk, at dette kun vedrører miljøvariabler. I en konfigurationsfil bruges indstillingsnavnene altid uden præfiks.

!!! tip "Kontrol af forældede muligheder"
    Forældede konfigurationsmuligheder, som din server stadig er afhængig af – såsom uden præfiks miljøvariabler, `SEARCH_INDEX_DIR` eller `EMAIL_USE_TLS` – logges som advarsler ved opstart. Siden Gramps Web API 3.22 er de også listet, sammen med deres erstatning og den version, hvor support vil blive fjernet, øverst på **Systemoplysninger**-siden (tilgængelig via brugerikonet i den øverste app-bar), når du er logget ind som administrator.

## Eksisterende konfigurationsindstillinger
Følgende konfigurationsmuligheder findes.

### Nødvendige indstillinger

Nøgle | Beskrivelse
----|-------------
`TREE` | Navnet på den familie trædatabase, der skal bruges. Vis tilgængelige træer med `gramps -l`. Hvis et træ med dette navn ikke eksisterer, vil et nyt tomt træ blive oprettet.
`SECRET_KEY` | Den hemmelige nøgle til flask. Den hemmelige nøgle må ikke deles offentligt. Ændring af den vil ugyldiggøre alle adgangstokens.
`USER_DB_URI` | Database-URL'en til bruger databasen. Enhver URL, der er kompatibel med SQLAlchemy, er tilladt.

!!! info
    Du kan generere en sikker hemmelig nøgle f.eks. med kommandoen

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valgfri indstillinger

Nøgle | Beskrivelse
----|-------------
`MEDIA_BASE_DIR` | Sti til at bruge som basisbibliotek for mediefiler, der overskriver det mediebibliotek, der er indstillet i Gramps. Når du bruger [S3](s3.md), skal den have formen `s3://<bucket_name>`
`TREE_ID` | Navnet på biblioteket for den familie trædatabase, der skal bruges i enkelttrætilstand (når `TREE` ikke er indstillet til `*`). Når den er indstillet, identificerer serveren træet ved dets biblioteknavn snarere end dets visningsnavn, hvilket er mere robust over for omdøbninger. Nødvendig, hvis du vil omdøbe træet via API'en. Biblioteknavnet kan findes via `GET /api/trees/-` (feltet `id`).
`SEARCH_INDEX_DB_URI` | Database-URL til søgeindekset. Kun `sqlite` eller `postgresql` er tilladt som backends. Standard til `sqlite:///indexdir/search_index.db`, der opretter en SQLite-fil i mappen `indexdir` i forhold til den sti, hvor scriptet køres.
`SEARCH_INDEX_DIR` | **Forældet** (brug `SEARCH_INDEX_DB_URI` i stedet). Bibliotek, der indeholder søgeindekset. Hvis det er indstillet, mens `SEARCH_INDEX_DB_URI` ikke er indstillet, afledes søgeindeks-URL'en som `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Sti til at servere statiske filer fra (f.eks. et statisk webfrontend)
`BASE_URL` | Basis-URL, hvor API'en kan nås (f.eks. `https://mygramps.mydomain.com/`). Dette er nødvendigt f.eks. for at opbygge korrekte links til nulstilling af adgangskoder.
`CORS_ORIGINS` | Oprindelser, hvor CORS-anmodninger er tilladt fra. Som standard er alle forbudt. Brug `"*"` for at tillade anmodninger fra ethvert domæne.
`EMAIL_HOST` | SMTP-servervært (f.eks. til at sende e-mails til nulstilling af adgangskoder)
`EMAIL_PORT` | SMTP-serverport. standard til 465
`EMAIL_HOST_USER` | SMTP-serverbrugernavn
`EMAIL_HOST_PASSWORD` | SMTP-serveradgangskode
`EMAIL_USE_TLS` | **Forældet** (brug `EMAIL_USE_SSL` eller `EMAIL_USE_STARTTLS` i stedet). Boolean, om der skal bruges TLS til at sende e-mails. Standard til `True`. Når der bruges STARTTLS, skal dette sættes til `False` og bruge en port forskellig fra 25.
`EMAIL_USE_SSL` | Boolean, om der skal bruges implicit SSL/TLS til SMTP (v3.6.0+). Standard til `True`, hvis `EMAIL_USE_TLS` ikke er eksplicit indstillet. Typisk brugt med port 465.
`EMAIL_USE_STARTTLS` | Boolean, om der skal bruges eksplicit STARTTLS til SMTP (v3.6.0+). Standard til `False`. Typisk brugt med port 587 eller 25.
`DEFAULT_FROM_EMAIL` | "Fra" adresse til automatiserede e-mails
`THUMBNAIL_CACHE_CONFIG` | Ordbog med indstillinger for miniaturecache. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`REQUEST_CACHE_CONFIG` | Ordbog med indstillinger for anmodningscache. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`PERSISTENT_CACHE_CONFIG` | Ordbog med indstillinger for den vedvarende cache, der bruges f.eks. til telemetri. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`CELERY_CONFIG` | Indstillinger for Celery-baggrundsopgavekøen. Se [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for mulige indstillinger.
`REPORT_DIR` | Midlertidigt bibliotek, hvor output fra kørsel af Gramps-rapporter vil blive gemt
`EXPORT_DIR` | Midlertidigt bibliotek, hvor output fra eksport af Gramps-databasen vil blive gemt
`REGISTRATION_DISABLED` | Hvis `True`, forbyder ny brugerregistrering (standard `False`)
`DISABLE_TELEMETRY` | Hvis `True`, deaktiverer statistiktelemetri (standard `False`). Se [telemetri](telemetry.md) for detaljer.
`PILLOW_MAX_IMAGE_PIXELS` | Sætter parameteren PIL.Image.MAX_IMAGE_PIXELS, som angiver antallet af pixels, som det behandlede billede kan indeholde. Se [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) for detaljer.
`MAX_THUMBNAIL_FILE_BYTES` | Sætter en hård maksimal filstørrelse for miniaturebilleder. Standard til `50 * 1024 * 1024` (50 MB). At hæve den kan i høj grad øge hukommelsesforbruget og kan føre til hukommelsesfejl eller datatab, hvis store filer dekomprimeres i hukommelsen.


!!! info
    Når du bruger miljøvariabler til konfiguration, skal boolske indstillinger som `EMAIL_USE_SSL` være enten strengen `true` eller `false` (store og små bogstaver er vigtige!).


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
`MEDIA_PREFIX_TREE` | Boolean, om der skal bruges en separat undermappe til mediefilerne for hvert træ. Standard til `False`, men anbefales kraftigt at bruge `True` i en multi-træ opsætning
`NEW_DB_BACKEND` | Den database backend, der skal bruges til nyoprettede familie træer. Skal være en af `sqlite`, `postgresql` eller `sharedpostgresql`. Standard til `sqlite`.
`POSTGRES_HOST` | Værtsnavnet på PostgreSQL-serveren, der bruges til at oprette nye træer, når der anvendes en multi-træ opsætning med SharedPostgreSQL-backend
`POSTGRES_PORT` | Porten til PostgreSQL-serveren, der bruges til at oprette nye træer, når der anvendes en multi-træ opsætning med SharedPostgreSQL-backend


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
`OIDC_OPENID_CONFIG_URL` | Valgfri: URL til OpenID Connect konfigurationsendpoint (hvis ikke bruger den standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, om lokal brugernavn/adgangskode-godkendelse skal deaktiveres. Standard til `False`
`OIDC_AUTO_REDIRECT` | Boolean, om der skal omdirigeres automatisk til OIDC, når kun én udbyder er konfigureret. Standard til `False`

#### Indbyggede OIDC-udbydere

For indbyggede udbydere (Google, Microsoft), brug disse indstillinger:

Nøgle | Beskrivelse
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Klient-ID til Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Klienthemmelighed til Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | Klient-ID til Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Klienthemmelighed til Microsoft OAuth

#### OIDC Rollekortlægning

Disse indstillinger giver dig mulighed for at kortlægge OIDC-grupper/roller fra din identitetsudbyder til Gramps Web-brugerroller:

Nøgle | Beskrivelse
----|-------------
`OIDC_ROLE_CLAIM` | Navnet på påstanden i OIDC-tokenet, der indeholder brugerens grupper/roller. Standard til "groups"
`OIDC_GROUP_ADMIN` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Admin" rolle
`OIDC_GROUP_OWNER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Owner" rolle
`OIDC_GROUP_EDITOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Editor" rolle
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Contributor" rolle
`OIDC_GROUP_MEMBER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Member" rolle
`OIDC_GROUP_GUEST` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægges til Gramps "Guest" rolle

### Indstillinger kun for AI-funktioner

Disse indstillinger er nødvendige, hvis du vil bruge AI-drevne funktioner som chat eller semantisk søgning.

Nøgle | Beskrivelse
----|-------------
`LLM_BASE_URL` | Basis-URL for OpenAI-kompatibel chat-API. Standard til `None`, som bruger OpenAI API.
`LLM_MODEL` | Modellen, der skal bruges til OpenAI-kompatibel chat-API. Hvis ikke indstillet (standard), er chat deaktiveret. Fra v3.6.0 bruger AI-assistenten Pydantic AI med værktøjsopkaldsfunktioner.
`VECTOR_EMBEDDING_MODEL` | Modellen, der skal bruges til semantisk søgning vektorembedninger. Når der bruges en lokal model, skal dette være et [Sentence Transformers](https://sbert.net/) modelnavn. Når der bruges en fjern API (se `VECTOR_EMBEDDING_BASE_URL`), er dette modelnavnet, der sendes til den fjerne udbyder. Hvis ikke indstillet (standard), er semantisk søgning og chat deaktiveret.
`VECTOR_EMBEDDING_BASE_URL` | Basis-URL for en fjern OpenAI-kompatibel embedding-API (f.eks. Ollama, OpenAI, LiteLLM). Hvis ikke indstillet (standard), bruges en lokal Sentence Transformers-model. Se [Brug af en fjern embedding-API](chat.md#using-a-remote-embedding-api) for detaljer.
`VECTOR_EMBEDDING_API_KEY` | API-nøgle til autentificerede fjern embedding-udbydere. Kun nødvendig, når `VECTOR_EMBEDDING_BASE_URL` er indstillet, og udbyderen kræver autentificering.
`LLM_MAX_CONTEXT_LENGTH` | Tegnbegrænsning for familie træets kontekst, der gives til LLM. Standard til 50000.
`LLM_SYSTEM_PROMPT` | Brugerdefineret systemprompt til LLM chatassistent (v3.6.0+). Hvis ikke indstillet, bruges den standard genealogi-optimerede prompt.


## Eksempel på konfigurationsfil

En minimal konfigurationsfil til produktion kunne se sådan ud:
```python
TREE="Mit Familie Træ"
BASE_URL="https://mitræ.example.com"
SECRET_KEY="..."  # din hemmelige nøgle
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Brug implicit SSL til port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # din SMTP-adgangskode
DEFAULT_FROM_EMAIL="gramps@example.com"
