# Administrer Brugere

Brugeradministrationsgrænsefladen er tilgængelig via **Indstillinger > Administrer Brugere** (brugerikonet i den øverste app-bar). Den er kun tilgængelig for brugere med ejer- eller administratorrolle.

## Brugerroller

Se [Brugersystem](../install_setup/users.md) for en fuld beskrivelse af de tilgængelige brugerroller og deres rettigheder.

## Vis og filtrer brugere

Siden til at administrere brugere viser en tabel over alle registrerede brugerkonti med følgende kolonner:

- **Brugernavn** – login-navnet
- **Fuldt Navn** – visningsnavnet
- **E-mail** – brugerens e-mailadresse
- **Rolle** – den tildelte rolle (Gæst, Medlem, Bidragyder, Redaktør, Ejer eller Administrator)
- **Kontokilde** – enten "Adgangskode" (lokal konto) eller navnet på en ekstern identitetsudbyder (f.eks. når der bruges OIDC)

Brug søgefeltet og rolle-dropdown-menuen øverst i tabellen til at filtrere listen. Klik på filter-ryd-knappen for at nulstille alle filtre.

## Rediger en bruger

Klik på redigeringsikonet (blyant) på en hvilken som helst række for at åbne redigeringsdialogen. Du kan ændre brugerens:

- Fulde navn
- E-mailadresse
- Rolle

Dette er den primære måde at **aktivere en ny selvregistreret bruger**: ændre deres rolle fra *deaktiveret* til en hvilken som helst aktiv rolle (f.eks. Medlem eller Redaktør).

E-mailadresser behøver ikke at være unikke (siden Gramps Web API 3.22), så flere konti kan dele den samme adresse.

## Tilføj en bruger manuelt

Klik på **tilføj bruger** (person-tilføj) ikonet over tabellen for at oprette en ny brugerkonto direkte uden at kræve selvregistrering. Udfyld brugernavnet, fulde navn, e-mailadresse, adgangskode og rolle i dialogen og klik på **Gem**.

## Slet en bruger

Klik på slet (skraldespand) ikonet på en hvilken som helst række og bekræft dialogen. Denne handling kan ikke fortrydes.

!!! note
    For at forhindre, at et træ efterlades uden nogen, der kan administrere det, kan du ikke sænke din egen rolle under Ejer eller slette din egen konto, hvis du er den eneste Ejer eller Administrator af træet. Forfrem en anden bruger til Ejer først. En administrator kan stadig ændre eller fjerne den sidste ejer af en anden brugers træ, da de kan udpege en ny.

## Eksportér og importer brugerkonti

Disse knapper er nyttige, når du [migrerer til en anden Gramps Web-instans](export.md).

- **Eksportér brugeroplysninger** (download-ikon) – downloader en JSON-fil, der indeholder alle brugerkonti (uden adgangskoder, da adgangskoder opbevares i krypteret form).
- **Importer brugerkonti** (gruppe-tilføj ikon) – uploader en tidligere eksporteret JSON-fil for at oprette brugerkonti i bulk. Alle importerede brugere skal indstille en ny adgangskode via "Glemt adgangskode"-linket, da adgangskoder ikke kan overføres.

## Registreringslink (kun multi-træ opsætning)

I en multi-træ opsætning vises registreringslinket for nye brugere øverst på siden til at administrere brugere. Du kan kopiere dette link og dele det med personer, du ønsker at invitere til at registrere en konto på dit træ.

!!! note
    I en enkelt-træ opsætning er der et generisk "Registrer" link på login-siden; registreringslinket pr. træ er kun nødvendigt i multi-træ installationer.

## AI chat rettigheder

Hvis AI chat er blevet aktiveret på serveren, giver en dropdown-menu øverst på siden dig mulighed for at kontrollere, hvilke brugerroller der har lov til at bruge chat-funktionen:

- Alle (inklusive gæster)
- Medlem og derover
- Bidragyder og derover
- Redaktør og derover
- Ejere og administratorer kun
- Ingen (deaktiver chat for alle brugere)
