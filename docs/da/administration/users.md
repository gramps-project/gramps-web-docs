# Administrer brugere

Brugeradministrationsgrænsefladen er tilgængelig via **Indstillinger > Administrer brugere** (brugerikonet i den øverste app-bar). Den er kun tilgængelig for brugere med ejer- eller administratorrolle.

## Brugerroller

Se [Brugersystem](../install_setup/users.md) for en fuld beskrivelse af de tilgængelige brugerroller og deres tilladelser. Den primære forskel mellem gæster og medlemmer er, at gæster ikke kan se [private optegnelser](../user-guide/privacy.md), så vælg rollen sammen med det, du markerer som privat.

## Vis og filtrer brugere

Siden til at administrere brugere viser en tabel over alle registrerede brugerkonti med følgende kolonner:

- **Brugernavn** – login-navnet
- **Fulde navn** – visningsnavnet
- **E-mail** – brugerens e-mailadresse
- **Rolle** – den tildelte rolle (Gæst, Medlem, Bidragyder, Redaktør, Ejer eller Administrator)
- **Kilde til konto** – enten "Adgangskode" (lokal konto) eller navnet på en ekstern identitetsudbyder (f.eks. ved brug af OIDC)

Brug søgefeltet og rolle-dropdown-menuen øverst i tabellen for at filtrere listen. Klik på filter-ryd knappen for at nulstille alle filtre.

## Rediger en bruger

Klik på rediger (blyant) ikonet på en hvilken som helst række for at åbne redigeringsdialogen. Du kan ændre brugerens:

- Fulde navn
- E-mailadresse
- Rolle

Dette er den primære måde at **aktivere en ny selvregistreret bruger**: ændre deres rolle fra *deaktiveret* til en hvilken som helst aktiv rolle (f.eks. Medlem eller Redaktør).

E-mailadresser behøver ikke at være unikke (siden Gramps Web API 3.22), så flere konti kan dele den samme adresse.

Deaktivering af en bruger eller ændring af deres adgangskode afslutter alle deres sessioner inden for 15 minutter.

!!! note
    Ejere kan ikke redigere, ændre adgangskoden for eller slette brugere med en højere rolle, såsom webstedets administrator. Brugere med samme rolle, såsom to ejere af et træ, kan administrere hinanden.

## Tilføj en bruger manuelt

Klik på **tilføj bruger** (person-tilføj) ikonet over tabellen for at oprette en ny brugerkonto direkte uden at kræve selvregistrering. Udfyld brugernavnet, fulde navn, e-mailadresse, adgangskode og rolle i dialogen og klik på **Gem**.

## Slet en bruger

Klik på slet (skraldespand) ikonet på en hvilken som helst række og bekræft dialogen. Denne handling kan ikke fortrydes.

!!! note
    For at forhindre, at et træ efterlades uden nogen, der kan administrere det, kan du ikke sænke din egen rolle under Ejer eller slette din egen konto, hvis du er den eneste Ejer eller Administrator af træet. Forfrem en anden bruger til Ejer først. En administrator kan stadig ændre eller fjerne den sidste ejer af en anden brugers træ, da de kan udnævne en ny.

## Eksportér og importer brugerkonti

Disse knapper er nyttige, når du [migrerer til en anden Gramps Web-forekomst](export.md).

- **Eksportér brugeroplysninger** (download ikon) – downloader en JSON-fil, der indeholder alle brugerkonti (uden adgangskoder, da adgangskoder opbevares i krypteret form).
- **Importer brugerkonti** (gruppe-tilføj ikon) – uploader en tidligere eksporteret JSON-fil for at oprette brugerkonti i bulk. Alle importerede brugere skal indstille en ny adgangskode via "Glemt adgangskode" linket, da adgangskoder ikke kan overføres.

## Registreringslink (kun multi-træ opsætning)

I en multi-træ opsætning vises registreringslinket for nye brugere øverst på siden til at administrere brugere. Du kan kopiere dette link og dele det med personer, du ønsker at invitere til at registrere en konto på dit træ.

!!! note
    I en enkelt-træ opsætning er der et generisk "Registrer" link på login-siden; registreringslinket pr. træ er kun nødvendigt i multi-træ installationer.

## AI chat tilladelser

Hvis AI chat er blevet aktiveret på serveren, giver en dropdown-menu øverst på siden dig mulighed for at kontrollere, hvilke brugerroller der har lov til at bruge chatfunktionen:

- Alle (inklusive gæster)
- Medlem og derover
- Bidragyder og derover
- Redaktør og derover
- Kun ejere og administratorer
- Ingen (deaktiver chat for alle brugere)
