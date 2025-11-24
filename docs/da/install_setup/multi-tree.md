# Opsætning til hosting af flere træer

Som standard tillader Gramps Web kun adgang til en enkelt familie træ database (“træ”), specificeret i konfigurationsfilen.

Dog, fra version 0.7.0 af Gramps Web API backend, er det også muligt at betjene flere træer fra en enkelt installation. Hver bruger er dog (i øjeblikket) knyttet til et enkelt træ, så denne opsætning er ikke egnet til at dele træer mellem brugere, men til at hoste flere isolerede Gramps Web instanser.

## Aktiver multi-træ support

For at aktivere multi-træ support skal `TREE` konfigurationsmuligheden sættes til en enkelt stjerne `*`, f.eks. i en konfigurationsfil:

```python
TREE = "*"
```

Dette vil gøre alle træer i serverens Gramps database katalog tilgængelige (givet tilstrækkelige brugerrettigheder). Træets ID er navnet på undermappen. Du kan liste eksisterende træer (navne og IDs) med kommandoen

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Derudover bør du sætte `MEDIA_PREFIX_TREE` konfigurationsmuligheden til `True` for at sikre, at mediefiler opbevares i separate undermapper. Ellers kan brugere få adgang til mediefiler, der tilhører et træ, de ikke har tilladelse til!

## Tilføj en brugerkonto til et specifikt træ

For at tilføje en bruger til et specifikt træ, skal du blot tilføje `--tree TREEID` kommandolinjeoptionen til tilføj bruger-kommandoen. Du kan også POSTe til `/users/` endpointet med `tree` egenskaben sat i JSON payloaden.

Brugernavne og e-mailadresser skal være unikke på tværs af *alle* træer.

## Opret et nyt træ

For at oprette et nyt træ anbefales det at POSTe til `/trees/` endpointet i stedet for at bruge Gramps CLI. Dette vil bruge en UUIDv4 som træ ID, hvilket fører til ekstra sikkerhed, da navnet ikke kan gættes. I øjeblikket understøttes kun SQLite for nyoprettede træer.

## Autoriser

For at autorisere (hente en token) er kun brugernavn og adgangskode nødvendige, ligesom i single-tree mode, da træ ID er kendt for hver bruger, så der er ikke behov for at angive det.

## Migrer eksisterende mediefiler

Hvis du vil migrere en eksisterende Gramps Web instans til multi-træ support og bruger lokale mediefiler, kan du blot flytte dem til en undermappe af den oprindelige placering med træ ID som navn.

Hvis du bruger mediefiler hostet på S3, kan du bruge scriptet, der findes i `scripts` mappen i `gramps-web-api` repository:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Dette forudsætter, at de relevante adgangsnøgler allerede er indstillet som miljøvariabler.

## Migrer eksisterende bruger database

Hvis du vil aktivere multi-træ support og genbruge eksisterende brugere, skal du tildele dem til et specifikt træ. Du kan bruge følgende kommando til dette formål,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Tilpas frontend

Registreringssiden, der er tilgængelig fra login-siden, fungerer ikke i en multi-træ opsætning, da et træ skal specificeres for registrering. Det er derfor tilrådeligt at sætte `hideRegisterLink` til `true` i [frontend konfigurationen](frontend-config.md).
