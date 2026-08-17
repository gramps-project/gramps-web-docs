# Serverkonfiguration

Ved at bruge det standard Docker-billede kan al nødvendig konfiguration foretages fra browseren. Afhængigt af implementeringen kan det dog være nødvendigt at tilpasse serverkonfigurationen.

Denne side lister alle metoder til at ændre konfigurationen og alle eksisterende konfigurationsmuligheder.


## Konfigurationsfil vs. miljøvariabler

For indstillingerne kan du enten bruge en konfigurationsfil eller miljøvariabler.

Når du bruger den [Docker Compose-baserede opsætning](deployment.md), kan du inkludere en konfigurationsfil ved at tilføje følgende listeelement under `volumes:`-nøglen i `grampsweb:`-blokken:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
hvor `/path/to/config.cfg` er stien til konfigurationsfilen i din servers filsystem (den højre side refererer til stien i containeren og må ikke ændres).

Når du bruger miljøvariabler,

- præfiks hvert indstillingsnavn med `GRAMPSWEB_` for at opnå navnet på miljøvariablen
- Brug dobbelte understregninger til indstillinger for indlejrede ordbøger, f.eks. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` vil sætte værdien af konfigurationsmuligheden `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Bemærk, at konfigurationsmuligheder, der er indstillet via miljøet, har forrang over dem i konfigurationsfilen. Hvis begge er til stede, "vinder" miljøvariablen.

!!! warning "Uden præfiks miljøvariabler er forældede"
    Af historiske grunde kan en håndfuld indstillinger – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` og `STATIC_PATH` – stadig indstilles via en miljøvariabel *uden* `GRAMPSWEB_` præfikset. Dette er forældet, logger en advarsel ved opstart, og vil stoppe med at fungere i en fremtidig udgivelse. Brug altid den præfikserede form, f.eks. `GRAMPSWEB_TREE` i stedet for `TREE`.

    Bemærk, at dette kun vedrører miljøvariabler. I en konfigurationsfil bruges indstillingsnavnene altid uden præfiks.

## Eksisterende konfigurationsindstillinger
Følgende konfigurationsmuligheder eksisterer.

### Nødvendige indstillinger

Nøgle | Beskrivelse
----|-------------
`TREE` | Navnet på den familie trædatabase, der skal bruges. Vis tilgængelige træer med `gramps -l`. Hvis et træ med dette navn ikke eksisterer, vil et nyt tomt blive oprettet.
`SECRET_KEY` | Den hemmelige nøgle til flask. Hemmeligheden må ikke deles offentligt. Ændring af den vil ugyldiggøre alle adgangstokens.
`USER_DB_URI` | Database-URL'en til brugerdatabasen. Enhver URL, der er kompatibel med SQLAlchemy, er tilladt.

!!! info
    Du kan generere en sikker hemmelig nøgle f.eks. med kommandoen

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valgfri indstillinger

Nøgle | Beskrivelse
----|-------------
`MEDIA_BASE_DIR` | Sti til at bruge som basisdirectory for mediefiler, der overskriver den mediebaserede mappe indstillet i Gramps. Når du bruger [S3](s3.md), skal den have formen `s3://<bucket_name>`
`TREE_ID` | Mappenavnet på den familie trædatabase, der skal bruges i enkelt-trætilstand (når `TREE` ikke er indstillet til `*`). Når den er indstillet, identificerer serveren træet ved sit mappenavn i stedet for sit visningsnavn, hvilket er mere robust over for omdøbninger. Nødvendig, hvis du vil omdøbe træet via API'en. Mappenavnet kan findes via `GET /api/trees/-` (feltet `id`).
`SEARCH_INDEX_DB_URI` | Database-URL til søgeindekset. Kun `sqlite` eller `postgresql` er tilladt som backend. Standard til `sqlite:///indexdir/search_index.db`, der opretter en SQLite-fil i mappen `indexdir` i forhold til den sti, hvor scriptet køres.
`SEARCH_INDEX_DIR` | **Forældet** (brug `SEARCH_INDEX_DB_URI` i stedet). Mappen, der indeholder søgeindekset. Hvis den er indstillet, mens `SEARCH_INDEX_DB_URI` ikke er indstillet, afledes søgeindeks-URL'en som `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Sti til at servere statiske filer fra (f.eks. et statisk webfrontend)
`BASE_URL` | Basis-URL, hvor API'en kan nås (f.eks. `https://mygramps.mydomain.com/`). Dette er nødvendigt f.eks. for at bygge korrekte links til nulstilling af adgangskoder
`CORS_ORIGINS` | Oprindelser, hvor CORS-anmodninger er tilladt fra. Som standard er alle forbudt. Brug `"*"` for at tillade anmodninger fra ethvert domæne.
`EMAIL_HOST` | SMTP-servervært (f.eks. til sending af e-mails til nulstilling af adgangskoder)
`EMAIL_PORT` | SMTP-serverport. standard til 465
`EMAIL_HOST_USER` | SMTP-serverbrugernavn
`EMAIL_HOST_PASSWORD` | SMTP-serveradgangskode
`EMAIL_USE_TLS` | **Forældet** (brug `EMAIL_USE_SSL` eller `EMAIL_USE_STARTTLS` i stedet). Boolean, om der skal bruges TLS til at sende e-mails. Standard til `True`. Når du bruger STARTTLS, skal du indstille dette til `False` og bruge en port forskellig fra 25.
`EMAIL_USE_SSL` | Boolean, om der skal bruges implicit SSL/TLS til SMTP (v3.6.0+). Standard til `True`, hvis `EMAIL_USE_TLS` ikke er eksplicit indstillet. Typisk brugt med port 465.
`EMAIL_USE_STARTTLS` | Boolean, om der skal bruges eksplicit STARTTLS til SMTP (v3.6.0+). Standard til `False`. Typisk brugt med port 587 eller 25.
`DEFAULT_FROM_EMAIL` | "Fra" adresse til automatiserede e-mails
`THUMBNAIL_CACHE_CONFIG` | Ordbog med indstillinger for thumbnail-cachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`REQUEST_CACHE_CONFIG` | Ordbog med indstillinger for anmodningscachen. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`PERSISTENT_CACHE_CONFIG` | Ordbog med indstillinger for den vedvarende cache, der bruges f.eks. til telemetri. Se [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for mulige indstillinger.
`CELERY_CONFIG` | Indstillinger for Celery-baggrundsopgavekøen. Se [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for mulige indstillinger.
`REPORT_DIR` | Midlertidig mappe, hvor output fra kørsel af Gramps-rapporter vil blive gemt
`EXPORT_DIR` | Midlertidig mappe, hvor output fra eksport af Gramps-databasen vil blive gemt
`REGISTRATION_DISABLED` | Hvis `True`, forbyder ny brugerregistrering (standard `False`)
`DISABLE_TELEMETRY` | Hvis `True`, deaktiverer statistiktelemetri (standard `False`). Se [telemetri](telemetry.md) for detaljer.
`PILLOW_MAX_IMAGE_PIXELS` | Sætter parameteren PIL.Image.MAX_IMAGE_PIXELS, som angiver antallet af pixels, som det behandlede billede kan indeholde. Se [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) for detaljer.
`MAX_THUMBNAIL_FILE_BYTES` | Sætter en hård maksimal filstørrelse for thumbnails. Standard til `50 * 1024 * 1024` (50 MB). At hæve den kan i høj grad øge hukommelsesforbruget og kan føre til hukommelsesfejl eller datatab, hvis store filer dekomprimeres i hukommelsen.


!!! info
    Når du bruger miljøvariabler til konfiguration, skal boolske indstillinger som `EMAIL_USE_SSL` være enten strengen `true` eller `false` (store og små bogstaver er følsomme!).


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
`MEDIA_PREFIX_TREE` | Boolean, om der skal bruges en separat undermappe til mediefilerne for hvert træ. Standard til `False`, men anbefales stærkt at bruge `True` i en multi-træopsætning
`NEW_DB_BACKEND` | Den databasebackend, der skal bruges til nyoprettede familie træer. Skal være en af `sqlite`, `postgresql` eller `sharedpostgresql`. Standard til `sqlite`.
`POSTGRES_HOST` | Værtsnavnet på PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-træopsætning med SharedPostgreSQL-backend
`POSTGRES_PORT` | Porten på PostgreSQL-serveren, der bruges til at oprette nye træer, når der bruges en multi-træopsætning med SharedPostgreSQL-backend


### Indstillinger for OIDC-godkendelse

Disse indstillinger er nødvendige, hvis du vil bruge OpenID Connect (OIDC) godkendelse med eksterne udbydere. For detaljerede opsætningsinstruktioner og eksempler, se [OIDC-godkendelse](oidc.md).

Nøgle | Beskrivelse
----|-------------
`OIDC_ENABLED` | Boolean, om OIDC-godkendelse skal aktiveres. Standard til `False`.
`OIDC_ISSUER` | OIDC-udbyderens udsteder-URL (for brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_ID` | OAuth-klient-ID (for brugerdefinerede OIDC-udbydere)
`OIDC_CLIENT_SECRET` | OAuth-klienthemmelighed (for brugerdefinerede OIDC-udbydere)
`OIDC_NAME` | Brugerdefineret visningsnavn for udbyderen. Standard til "OIDC"
`OIDC_SCOPES` | OAuth-scopes. Standard til "openid email profile"
`OIDC_USERNAME_CLAIM` | Den påstand, der skal bruges til brugernavnet. Standard til "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valgfri: URL til OpenID Connect-konfigurationsendpointet (hvis ikke bruger standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, om lokal brugernavn/adgangskode-godkendelse skal deaktiveres. Standard til `False`
`OIDC_AUTO_REDIRECT` | Boolean, om der automatisk skal omdirigeres til OIDC, når kun én udbyder er konfigureret. Standard til `False`

#### Indbyggede OIDC-udbydere

For indbyggede udbydere (Google, Microsoft) skal du bruge disse indstillinger:

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
`OIDC_GROUP_ADMIN` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Admin"-rollen
`OIDC_GROUP_OWNER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Owner"-rollen
`OIDC_GROUP_EDITOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Editor"-rollen
`OIDC_GROUP_CONTRIBUTOR` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Contributor"-rollen
`OIDC_GROUP_MEMBER` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Member"-rollen
`OIDC_GROUP_GUEST` | Gruppen/rollenavnet fra din OIDC-udbyder, der kortlægger til Gramps "Guest"-rollen

### Indstillinger kun for AI-funktioner

Disse indstillinger er nødvendige, hvis du vil bruge AI-drevne funktioner som chat eller semantisk søgning.

Nøgle | Beskrivelse
----|-------------
`LLM_BASE_URL` | Basis-URL for OpenAI-kompatibel chat-API. Standard til `None`, som bruger OpenAI API.
`LLM_MODEL` | Modellen, der skal bruges til OpenAI-kompatibel chat-API. Hvis ikke indstillet (standard), er chat deaktiveret. Fra v3.6.0 bruger AI-assistenten Pydantic AI med værktøjsopkaldsfunktioner.
`VECTOR_EMBEDDING_MODEL` | Den [Sentence Transformers](https://sbert.net/) model, der skal bruges til semantisk søgning vektorembedninger. Hvis ikke indstillet (standard), er semantisk søgning og chat deaktiveret.
`LLM_MAX_CONTEXT_LENGTH` | Tegnbegrænsning for familie trækontexten, der gives til LLM. Standard til 50000.
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
