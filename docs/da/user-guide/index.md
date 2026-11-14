---
hide:
  - toc
---

# Brugervejledning

Dette afsnit dokumenterer de funktioner, der er tilgængelige for brugere af Gramps Web.

!!! note "Ser du ikke alle funktioner?"
    Gramps Web bruger et rollebaseret tilladelsessystem. Nogle funktioner – såsom redigering af data, administration af tags eller visning af private optegnelser – er kun tilgængelige for brugere med tilstrækkelige tilladelser. Du kan tjekke din nuværende rolle i [Brugerindstillinger](settings.md). Hvis du har brug for mere adgang, skal du kontakte ejeren af dit træ eller administratoren. Se [Bruger system](../install_setup/users.md) for en beskrivelse af alle roller.

## Navigering i grænsefladen

### Hovednavigation

Sidebaren (eller hamburger-menuen på mobile enheder) er den primære måde at bevæge sig mellem sektioner:

- **Hjem** – dashboardet (se nedenfor)
- **Blog** – familiehistorier skrevet som blogindlæg
- **Slægtstræ** – interaktive trædiagrammer
- **Tidslinje** – kronologisk visning af begivenheder i træet (kræver en tilstrækkeligt ny Gramps Web API-version)
- **Kort** – geografisk visning af steder i træet
- **DNA** – DNA-matchanalyseværktøjer
- **Lister** – gennemse alle objekter af hver type: Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter
- **Medier** – gennemse alle mediefiler (fotos, dokumenter osv.)
- **Assistent** – AI chatassistent (hvis aktiveret af administratoren)
- **Historik** – nyligt ændrede objekter
- **Bogmærker** – dine gemte bogmærker
- **Opgaver** – forskningsopgaver
- **Rapporter** – generer rapporter
- **Eksport** – eksportér slægtstræet
- **Revisioner** – fuld transaktionshistorik (synlig for medlemmer og derover)
- **Notifikationer** – tidligere notifikationer

!!! note
    Tags administreres ikke længere fra sidebaren – tagadministration er flyttet til [Administrationsindstillinger](../administration/settings.md#tags) (kun ejer/administrator). Se [Tags](tags.md) for hvordan tags anvendes.

### Øverste app-bar

Baren øverst på hver side indeholder:

- **Tilføj** (plus-ikon, synligt for bidragydere og derover) – åbner en menu for at oprette et nyt objekt: Person, Familie, Begivenhed, Sted, Kilde, Citering, Arkiv, Note, Medieobjekt eller Opgave
- **Søg** (forstørrelsesglas) – åbner søgesiden
- **Brugerikon** – åbner indstillingsmenuen: Brugerindstillinger, Administration (kun ejere), Administrer brugere (kun ejere), Systeminfo

## Hjemmesiden (dashboard)

Dashboardet vises, når du logger ind første gang. Det har to kolonner:

**Venstre kolonne:**

- **Hjempersonkort** – viser navnet, fotoet (hvis tilgængeligt) og nøglefakta om din valgte hjemperson, med et link til deres fulde profil og hurtig navigation til slægtstræet. Klik på **Indstil hjemperson**-knappen på kortet for at søge efter og vælge en anden person.
- **Årsdage** – kommende fødselsdage og årsdag fra træet, baseret på dagens dato.
- **Nyligt ændret** – en kort liste over de senest modificerede objekter, nyttig til at spore samarbejdende redigeringer.

**Højre kolonne:**

- **Nye blogindlæg** – de seneste indlæg fra [bloggen](blog.md), hvis der findes nogen.
- **Statistik** – et resumé af objektantal i træet (antal personer, familier, begivenheder osv.).

Mens træet stadig er tomt, skjuler dashboardet de paneler, der ikke ville have noget at vise, og viser i stedet et **Kom i gang**-kort for brugere med redigeringstilladelser: det tilbyder først at oprette en person eller importere en slægtstræfil, og når der er personer, at forbinde dem ved at oprette en familie. Kortet forsvinder, så snart træet indeholder en familie.

Hvis træadministrator har konfigureret en **hjemmeside-notat** og/eller et **hjemmeside-billede**, vises disse fremtrædende over de primære kolonner. Billedet vises ved siden af notatteksten, når begge er indstillet. Se [Administrationsindstillinger](../administration/customization.md) for hvordan man konfigurerer disse.

!!! tip
    Hvis træet er tomt, og du har redigeringstilladelser, viser dashboardet en "Kom i gang"-opfordring med knapper til at tilføje din første person eller importere en slægtstræfil.

## Installation af Gramps Web som en app

Gramps Web er en progressiv webapp (PWA), hvilket betyder, at din browser kan installere den sammen med dine andre applikationer i stedet for at holde den i en browserfane. Den får derefter sit eget ikon og åbner i sit eget vindue, uden adresselinje og browser-værktøjslinjer.

Hvordan du installerer den afhænger af din browser:

- **Android (Chrome)** – åbn menuen og vælg "Installer app" eller "Tilføj til startskærm".
- **iOS/iPadOS (Safari)** – tryk på delingsknappen og vælg "Tilføj til startskærm".
- **Desktop (Chrome, Edge)** – klik på installationsikonet i højre ende af adresselinjen, eller brug browserens menupunkt "Installer".
- **Desktop (Firefox, Safari)** – installation understøttes ikke; brug en normal browserfane eller -vindue.

Der ændres ikke noget ved, hvordan Gramps Web fungerer, og ingen data gemmes anderledes – det er den samme applikation, bare præsenteret som en selvstændig app.

!!! note
    Gramps Web skal stadig nå din server for at vise dine data, så en installeret app giver dig ikke mulighed for at gennemse dit slægtstræ offline.
