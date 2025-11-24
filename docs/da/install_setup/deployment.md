# Udrulning af Gramps Web med Docker

Den mest bekvemme mulighed for at hoste Gramps Web på din egen server (eller virtuelle server) er med Docker Compose.

Vi antager, at Docker og Docker Compose allerede er installeret på dit system. Du kan bruge Windows, Mac OS eller Linux som værtsystem. De understøttede arkitekturer inkluderer ikke kun x86-64 (desktop-systemer), men også ARM-systemer som en Raspberry Pi, som kan fungere som en billig, men kraftfuld (nok) webserver.

!!! note
    Du behøver ikke at installere Gramps på serveren, da det er indeholdt i docker-billedet.


## Trin 1: Docker-konfiguration

Opret en ny fil på serveren med navnet `docker-compose.yml` og indsæt følgende indhold: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Dette vil generere seks navngivne volumener for at sikre, at alle relevante data forbliver, når containeren genstartes.

!!! warning
    Ovenstående vil gøre API'en tilgængelig på port 80 på værtsmaskinen **uden SSL/TLS-beskyttelse**. Du kan bruge dette til lokal testning, men udsæt det ikke direkte for internettet, det er helt usikkert!

## Trin 2: Sikre adgang med SSL/TLS

Web-API'en **skal** serveres til det offentlige internet over HTTPS. Der er flere muligheder, f.eks.

- Brug af docker-hosting, der automatisk inkluderer SSL/TLS
- Brug af en Nginx Reverse Proxy med et Let's Encrypt-certifikat

Se [Docker med Let's Encrypt](lets_encrypt.md) for hvordan man opsætter det første.

Hvis du planlægger at bruge Gramps Web kun på dit lokale netværk, kan du springe dette trin over.

## Trin 3: Start serveren

Kør

```
docker compose up -d
```

Ved første kørsel vil appen vise en første-kørselsguide, der giver dig mulighed for at

- Oprette en konto for ejer (admin) brugeren
- Indstille nogle nødvendige konfigurationsmuligheder
- Importere et slægtstræ i Gramps XML (`.gramps`) format

## Trin 4: Upload mediefiler

Der er flere muligheder for at uploade mediefiler.

- Når du bruger filer, der er gemt på den samme server som Gramps Web, kan du montere et bibliotek ind i Docker-containeren i stedet for at bruge et navngivet volumen, dvs. `/home/server_user/gramps_media/:/app/media` i stedet for `gramps_media:/app/media`, og uploade dine mediefiler der.
- Når du bruger mediefiler [hostet på S3](s3.md), kan du bruge S3 Media Uploader Addon
- Den måske mest bekvemme mulighed er at bruge [Gramps Web Sync](../administration/sync.md).
