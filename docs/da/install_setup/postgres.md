# Brug af en PostgreSQL-database

Som standard gemmer Gramps Web hvert slægtstræ i sin egen SQLite-databasefil. Dette kræver ingen yderligere service, sikkerhedskopier er så enkle som at kopiere filer, og det fungerer godt for de fleste installationer, inklusive dem [der hoster flere træer](multi-tree.md).

Alternativt kan slægtstræer hostes på en PostgreSQL-server ved hjælp af SharedPostgreSQL-tilføjelsen, som holder alle træer i en enkelt database. Dette kan give mening, hvis du allerede kører en PostgreSQL-server og ønsker at administrere sikkerhedskopier og overvågning der, eller hvis du forventer mange brugere, der redigerer samtidig. PostgreSQL kan også hoste [bruger databasen](#using-a-postgresql-database-for-the-user-database) og [søgeindekset](#using-a-postgresql-database-for-the-search-index), uafhængigt af hvor slægtstræerne er gemt.

!!! warning "PostgreSQL-tilføjelse afskrevet"
    Den ældre PostgreSQL-tilføjelse, som gemmer et enkelt slægtstræ pr. database, er afskrevet og vil ikke længere blive understøttet i en fremtidig version af Gramps Web API. Hvis du bruger den, se [Flytning af et træ fra PostgreSQL-tilføjelsen til SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Opsætning af PostgreSQL-serveren

Den nemmeste mulighed er at køre PostgreSQL-serveren i en container på samme Docker-vært som Gramps Web, ved hjælp af Docker Compose.

Gramps har brug for lokaliteter installeret på PostgreSQL-serveren for at sortere objekter korrekt på forskellige sprog, og de standard PostgreSQL-billeder inkluderer ikke nogen. Billedet [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) tilføjer dem. For at bruge det, tilføj følgende sektion til din `docker-compose.yml`:
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
og tilføj også `postgres_data:` som nøgle under `volumes:` sektionen af denne YAML-fil. Billedet indeholder to databaser, hver med sin egen bruger og adgangskode: `gramps` til de genealogiske data og `grampswebuser` til Gramps Web bruger databasen.

Hvis du bruger din egen PostgreSQL-server i stedet, skal du oprette en database med navnet `gramps`, som den konfigurerede bruger kan oprette tabeller i, og sørge for, at de lokaliteter, dine brugere har brug for, er installeret.

## Konfigurering af Gramps Web

Nye slægtstræer oprettes i SharedPostgreSQL-databasen, når Gramps Web kører i [multi-tree mode](multi-tree.md) og konfigurationsmuligheden `NEW_DB_BACKEND` er indstillet til `sharedpostgresql`. Med Docker Compose-opsætningen ovenfor, tilføj følgende under `environment:` nøgle i `grampsweb` tjenesten i `docker-compose.yml`:

```yaml
      # aktiver multi-tree mode
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # opret nye træer i SharedPostgreSQL-databasen
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # Værten og porten for PostgreSQL-serveren. 
      # Værten er navnet på PostgreSQL-tjenesten ovenfor
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Legitimationsoplysningerne skal stemme overens med dem, der bruges til
      # PostgreSQL-containeren
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Se [Konfiguration](configuration.md) for en beskrivelse af alle disse muligheder. Bemærk, at værten og porten gemmes med hvert træ, når det oprettes, så ændringer af dem senere kun påvirker nye træer.

## Oprettelse af et træ og import af data

For at oprette et nyt træ, POST til `/trees/` endpointet som beskrevet i [Opsætning til hosting af flere træer](multi-tree.md#create-a-new-tree). Svaret indeholder ID'et for det nye træ, som du har brug for for at [oprette træejerskontoen](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Når træejeren har logget ind, kan de [importere](../administration/import.md) et eksisterende slægtstræ, f.eks. en Gramps XML-fil eksporteret fra Gramps Desktop, via webgrænsefladen.

## Brug af en PostgreSQL-database til bruger databasen

Bruger databasen er normalt en SQLite-fil, uanset hvor slægtstræerne er hostet. For at bruge PostgreSQL i stedet, skal du indstille konfigurationsmuligheden `USER_DB_URI` til en PostgreSQL-database-URL. Med `gramps-postgres` billedet ovenfor, brug dets `grampswebuser` database:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Brug af en PostgreSQL-database til søgeindekset

Søgeindekset gemmes også i SQLite som standard. For at bruge PostgreSQL i stedet, skal du indstille konfigurationsmuligheden `SEARCH_INDEX_DB_URI` til en PostgreSQL-database-URL. Med `gramps-postgres` billedet ovenfor, kan du bruge dets `gramps` database, uanset om dine slægtstræer også er hostet der:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Flytning af et træ fra PostgreSQL-tilføjelsen til SharedPostgreSQL

Ældre installationer kan hoste deres slægtstræ med PostgreSQL-tilføjelsen, som gemmer et enkelt træ pr. database og er afskrevet. For at finde ud af, hvilken tilføjelse et træ bruger, skal du se på filen `database.txt` i træets undermappe i Gramps-databasedirektoriet: den indeholder `postgresql` for den afskrevne PostgreSQL-tilføjelse og `sharedpostgresql` for SharedPostgreSQL.

For at flytte et træ fra PostgreSQL-tilføjelsen til SharedPostgreSQL inden for den samme installation, mens du beholder dine brugerkonti og mediefiler:

1. [Sikkerhedskopier dit slægtstræ](../administration/export.md#back-up-your-family-tree) som en Gramps XML (`.gramps`) fil, ved hjælp af en konto, der kan se private optegnelser.
2. Ændre din konfiguration som beskrevet i [Konfigurering af Gramps Web](#configuring-gramps-web). Du kan fortsætte med at bruge din eksisterende `gramps-postgres` container.
3. [Opret et nyt træ](multi-tree.md#create-a-new-tree) og noter dets træ-ID.
4. Tildel dine eksisterende brugerkonti til det nye træ, som beskrevet i [Migrer eksisterende bruger database](multi-tree.md#migrate-existing-user-database).
5. Flyt dine mediefiler til den placering, der forventes for det nye træ, som beskrevet i [Migrer eksisterende mediefiler](multi-tree.md#migrate-existing-media-files).
6. Log ind og [importer](../administration/import.md) Gramps XML-filen til det nye træ.

Behold Gramps XML-filen, indtil du har kontrolleret, at det nye træ er komplet.

Hvis du flytter til en separat Gramps Web-installation i stedet, skal du følge trinene i [Flyt til en anden Gramps Web-instans](../administration/export.md#move-to-a-different-gramps-web-instance).

## Problemer

I tilfælde af problemer, bedes du overvåge logudgangen fra Gramps Web og PostgreSQL-serveren. I tilfælde af docker opnås dette med

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Hvis du har mistanke om, at der er et problem med Gramps Web (eller dokumentationen), bedes du indgive et problem [på Github](https://github.com/gramps-project/gramps-web-api/issues).
