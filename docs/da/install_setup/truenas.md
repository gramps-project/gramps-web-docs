# TrueNAS Opsætning

Denne vejledning forklarer, hvordan du opsætter Gramps Web på TrueNAS Community Edition 25.04.

!!! warning
    Denne vejledning er beregnet til TrueNAS Community Edition 25.04 eller senere, som introducerede et nyt Docker Compose-baseret appsystem. Den gælder ikke for tidligere versioner af TrueNAS.

## Forudsætninger

- TrueNAS Community Edition 25.04 eller senere
- Grundlæggende kendskab til TrueNAS webgrænsefladen
- Et datasæt til opbevaring af Gramps Web-data

## Oversigt

TrueNAS Community Edition 25.04 introducerede et nyt Docker Compose-baseret appsystem, der erstatter den tidligere Helm chart-baserede tilgang. Denne vejledning vil guide dig gennem oprettelsen af en brugerdefineret app til Gramps Web ved hjælp af Docker Compose.

## Trin 1: Forbered Lagring

1. Naviger til **Datasets** i TrueNAS webgrænsefladen
2. Opret et nyt datasæt til Gramps Web (f.eks. `grampsweb`). Noter den fulde sti til dette datasæt, f.eks. `/mnt/storage/grampsweb`, da du får brug for det senere.

Opret underkataloger til de forskellige komponenter:
- `users` - Bruger database
- `database` - Gramps databasefil(er)
- `media` - Mediefiler



## Trin 2: Opret Docker Compose App

1. Naviger til **Apps** i TrueNAS webgrænsefladen
2. Klik på **Discover Apps**
3. Søg efter "Gramps Web" og klik på det
4. Klik på "Install"

Dette vil tage dig til appens konfigurationsside.

## Trin 3: Konfigurer Appen

### Gramps Web konfiguration

- **Tidszone:** Indstil til din lokale tidszone (f.eks. `Europe/Berlin`)
- **Redis adgangskode:** Indstil en adgangskode til Redis. Denne vil kun blive brugt internt af appen.
- **Deaktiver telemetri:** venligst lad denne boks være ukontrolleret – se [her for detaljer](telemetry.md).
- **Hemmelig nøgle:** det er afgørende, at du indstiller dette til en stærk, unik værdi. Se [serverkonfiguration](configuration.md#existing-configuration-settings) for instruktioner om, hvordan du genererer en tilfældig nøgle.
- **Yderligere miljøvariabler:** Du skal indstille alle yderligere [konfigurationsmuligheder](configuration.md) som miljøvariabler præfiksede med `GRAMPSWEB_`. Tjek venligst [konfigurationsdokumentationen](configuration.md) i detaljer – for eksempel det faktum, at boolske værdier skal indstilles som `true` eller `false` (alt sammen med små bogstaver) i tilfælde af miljøvariabler, en almindelig faldgrube.

Venligst **mindst** indstil `GRAMPSWEB_BASE_URL` til den URL, din Gramps Web-instans vil være tilgængelig på – dette er nødvendigt for korrekt drift.

Du vil måske også sætte e-mailkonfiguration op på dette stadium. Hvis du gør det, kan du springe e-mailkonfigurationstrinnet over i onboarding-guiden. De relevante miljøvariabler er:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Alle konfigurationsindstillinger kan ændres senere ved at klikke på "Edit" i TrueNAS Apps-grænsefladen.


### Lagringskonfiguration

- **Brugerlagring**: Vælg stien til `users`-kataloget, du oprettede tidligere.
- **Indexlagring**: Du kan lade standardindstillingen "ixVolume (Datasæt oprettet automatisk af systemet)"
- **Thumbnail Cache Storage**: Du kan lade standardindstillingen "ixVolume (Datasæt oprettet automatisk af systemet)"
- **Cache Storage**: Du kan lade standardindstillingen "ixVolume (Datasæt oprettet automatisk af systemet)"
- **Medialagring**: Vælg stien til `media`-kataloget, du oprettede tidligere.
- **Gramps Database Storage**: Vælg stien til `database`-kataloget, du oprettede tidligere.

### Ressourcekonfiguration

Vi anbefaler, at du tildeler mindst 2 CPU'er og 4096 MB RAM for at sikre en glat drift.


## Trin 4: Adgang til Gramps Web

Når appen er implementeret, kan du få adgang til Gramps Web ved at klikke på "Web UI" knappen i TrueNAS Apps-grænsefladen. Du bør se onboarding-guiden "Velkommen til Gramps Web".

Hvis du vil tillade brugere at få adgang til din Gramps Web-grænseflade, **må du ikke** eksponere appen direkte til internettet, men fortsæt til næste trin.


## Trin 5: Opsæt en Reverse Proxy

For sikkert at eksponere din Gramps Web-instans til brugere, anbefales det at opsætte en reverse proxy. Dette giver dig mulighed for at administrere SSL/TLS-certifikater og kontrollere adgang.

Den nemmeste mulighed er at bruge den officielle TrueNAS Nginx Proxy Manager-app. Søg efter appen i TrueNAS Apps-grænsefladen og installer den. Du kan lade alle indstillinger være som standard, men vi anbefaler, at du indstiller én yderligere miljøvariabel: `DISABLE_IPV6` med værdien `true` for at undgå potentielle IPv6-relaterede problemer.

Når den er implementeret, skal du åbne Nginx Proxy Manager webgrænsefladen og oprette en ny proxy-vært med følgende indstillinger:

- Scheme: `http`
- Forward Hostname / IP: værtsnavnet på din TrueNAS-server (f.eks. `truenas`)
- Forward Port: den port, der er tildelt din Gramps Web-app (tjek TrueNAS Apps-grænsefladen for den nøjagtige port)
- I "SSL"-fanen, tjek "Force SSL"
- Under "SSL Certificates", vælg "Add SSL Certificate" > "Let's Encrypt" for at oprette et nyt Let's Encrypt-certifikat til dit domæne.

Se venligst [Nginx Proxy Manager dokumentationen](https://nginxproxymanager.com/guide/) for flere detaljer om konfiguration af din router og indhentning af SSL-certifikater.
