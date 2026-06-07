---
hide:
  - toc
---

# Brugervejledning

Dette afsnit dokumenterer de funktioner, der er tilgængelige for brugere af Gramps Web.

!!! note "Ser du ikke alle funktioner?"
    Gramps Web bruger et rollebaseret tilladelsessystem. Nogle funktioner – såsom redigering af data, administration af tags eller visning af private poster – er kun tilgængelige for brugere med tilstrækkelige tilladelser. Du kan tjekke din nuværende rolle i [Brugerindstillinger](settings.md). Hvis du har brug for mere adgang, skal du kontakte ejeren af dit træ eller administratoren. Se [Brugersystem](../install_setup/users.md) for en beskrivelse af alle roller.

## Navigere i grænsefladen

### Hovednavigation

Sidebaren (eller hamburger-menuen på mobilen) er den primære måde at bevæge sig mellem sektioner:

- **Hjem** – dashboardet (se nedenfor)
- **Blog** – familiehistorier skrevet som blogindlæg
- **Slægtstræ** – interaktive trædiagrammer
- **Tidslinje** – kronologisk visning af begivenheder i træet (kræver en tilstrækkelig ny version af Gramps Web API)
- **Kort** – geografisk visning af steder i træet
- **DNA** – DNA-matchanalyseværktøjer
- **Lister** – gennemse alle objekter af hver type: Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter
- **Medier** – gennemse alle mediefiler (fotos, dokumenter osv.)
- **Assistent** – AI chatassistent (hvis aktiveret af administratoren)
- **Historik** – nyligt ændrede objekter
- **Bogmærker** – dine gemte bogmærker
- **Opgaver** – forskningsopgaver
- **Rapporter** – generere rapporter
- **Eksport** – eksportere slægtstræet
- **Revisioner** – fuld transaktionshistorik (synlig for medlemmer og derover)
- **Notifikationer** – tidligere notifikationer

!!! note
    Tags administreres ikke længere fra sidebaren – tagadministration er flyttet til [Administrationsindstillinger](../administration/settings.md#tags) (kun ejer/administrator). Se [Tags](tags.md) for hvordan tags bruges.

### Øverste app-bar

Baren øverst på hver side indeholder:

- **Tilføj** (plus-ikon, synligt for bidragydere og derover) – åbner en menu for at oprette et nyt objekt: Person, Familie, Begivenhed, Sted, Kilde, Citering, Arkiv, Note, Medieobjekt eller Opgave
- **Søg** (forstørrelsesglas) – åbner søgesiden
- **Brugerikon** – åbner indstillingsmenuen: Brugerindstillinger, Administration (kun ejere), Administrer brugere (kun ejere), Systeminfo

## Hjemmesiden (dashboard)

Dashboardet vises, når du logger ind første gang. Det har to kolonner:

**Venstre kolonne:**

- **Hjemmepersonkort** – viser navnet, fotoet (hvis tilgængeligt) og nøglefakta om din valgte hjemmeperson, med et link til deres fulde profil og hurtig navigation til slægtstræet. Klik på **Indstil hjemmeperson**-knappen på kortet for at søge efter og vælge en anden person.
- **Årsdage** – kommende fødselsdage og årsager fra træet, baseret på dagens dato.
- **Nyligt ændret** – en kort liste over de senest ændrede objekter, nyttig til at spore samarbejdende redigeringer.

**Højre kolonne:**

- **Nye blogindlæg** – de seneste indlæg fra [bloggen](blog.md), hvis der findes nogen.
- **Statistik** – et resumé af objekttællinger i træet (antal personer, familier, begivenheder osv.).

Hvis træadministrator har konfigureret en **hjemmeside-note** og/eller et **hjemmesidebillede**, vises disse fremtrædende over de vigtigste kolonner. Billedet vises ved siden af noteteksten, når begge er indstillet. Se [Administrationsindstillinger](../administration/settings.md#customization) for hvordan du konfigurerer disse.

!!! tip
    Hvis træet er tomt, og du har redigeringstilladelser, viser dashboardet en "Kom i gang"-prompt med knapper til at tilføje din første person eller importere en slægtstræfil.
