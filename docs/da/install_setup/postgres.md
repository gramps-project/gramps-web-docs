# Brug af en PostgreSQL-database

Som standard bruger Gramps en filbaseret SQLite-database til at gemme slægtsforskningen. Dette fungerer helt fint for Gramps Web og anbefales til de fleste brugere. Dog, fra og med Gramps Web API version 0.3.0, understøttes også en PostgreSQL-server med et enkelt slægtstræ pr. database, drevet af [Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Siden [version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) understøttes også SharedPostgreSQL Addon, som muliggør hosting af flere slægtstræer i en enkelt database, hvilket er særligt nyttigt, når det bruges sammen med Gramps Web API [multi-tree support](multi-tree.md).

## Opsætning af PostgreSQL-serveren

Hvis du ønsker at opsætte en ny database til brug med PostgreSQLAddon, kan du følge [instruktionerne i Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) for at opsætte serveren.

Alternativt kan du også bruge Docker Compose til at køre PostgreSQL-serveren i en container på samme docker-vært som Gramps Web.

Brugen af en dockeriseret PostgreSQL med Gramps er kun kompliceret af det faktum, at de standard PostgreSQL-billeder ikke har nogen lokaliteter installeret, som dog er nødvendige for Gramps til lokaliseret sortering af objekter. Den nemmeste mulighed er at bruge `gramps-postgres` billedet, der er udgivet i [denne repository](https://github.com/DavidMStraub/gramps-postgres-docker/). For at bruge det, tilføj følgende sektion til din `docker-compose.yml`:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
og tilføj også `postgres_data:` som nøgle under `volumes:` sektionen i denne YAML-fil. Dette billede indeholder en separat database til Gramps slægtsdata og til Gramps brugerdatabase; de kan hver især have separate adgangskoder.

## Importering af et Gramps slægtstræ

Igen, hvis du selv har opsat PostgreSQL-serveren, kan du følge [instruktionerne i Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) for at importere et slægtstræ til databasen.

Alternativt, hvis du har fulgt Docker Compose-instruktionerne ovenfor, kan du bruge følgende kommando til at importere en Gramps XML-fil, der er placeret på din docker-vært:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Konfigurering af Web API til brug med databasen

For at konfigurere Web API til brug med PostgreSQL-databasen, tilføj følgende under `environment:` nøgle i `grampsweb` tjenesten i `docker-compose.yml`:

```yaml
      # PostgreSQL add-on antager, at trænavnet er
      # lig med databasens navn, og her bruges det
      # standard database navn for PostgreSQL billedet
      TREE: postgres
      # Adgangsoplysningerne skal stemme overens med dem, der bruges til
      # PostgreSQL containeren
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Brug af en delt PostgreSQL-database i en multi-tree installation

Når du bruger en [multi-tree opsætning](multi-tree.md), er SharedPostgreSQL add-on en praktisk mulighed for at hoste alle træer, også nyoprettede via API'en, i en enkelt PostgreSQL-database uden at gå på kompromis med privatlivets fred eller sikkerhed.

For at opnå dette, opsæt en container baseret på `gramps-postgres` billedet som beskrevet ovenfor og sæt simpelthen konfigurationsmuligheden `NEW_DB_BACKEND` til `sharedpostgresql`, f.eks. via miljøvariablen `GRAMPSWEB_NEW_DB_BACKEND`.

## Brug af en PostgreSQL-database til brugerdatabasen

Uafhængigt af hvilken database backend der bruges til slægtsdataene, kan brugerdatabasen hostes i en PostgreSQL-database ved at angive en passende database-URL. Det nævnte `gramps-postgres` dockerbillede indeholder en separat database `grampswebuser`, der kan bruges til dette formål. I så fald ville den passende værdi for konfigurationsmuligheden `USER_DB_URI` være
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Brug af en PostgreSQL-database til søgeindekset

Siden Gramps Web API version 2.4.0, er søgeindekset hostet enten i en SQLite-database (standard) eller en PostgreSQL-database. Også til dette formål kan `gramps-postgres` billedet bruges. For søgeindekset kan vi bruge `gramps` databasen, der leveres af billedet, uanset om vi hoster vores slægtsdata i PostgreSQL eller ej (søgeindekset og slægtsdataene kan sameksistere i den samme database). Dette kan opnås, i det ovenstående eksempel, ved at sætte konfigurationsmuligheden `SEARCH_INDEX_DB_URI` til
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Problemer

I tilfælde af problemer, bedes du overvåge logudgangen fra Gramps Web og PostgreSQL-serveren. I tilfælde af docker opnås dette med

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Hvis du mistænker, at der er et problem med Gramps Web (eller dokumentationen), bedes du indgive et problem [på Github](https://github.com/gramps-project/gramps-web-api/issues).
