---
hide:
  - toc
---

# Brugervejledning

Dette afsnit dokumenterer de funktioner, der er tilgængelige for brugere af Gramps Web.

!!! note "Ser du ikke alle funktioner?"
    Gramps Web bruger et rollebaseret tilladelsessystem. Nogle funktioner – såsom redigering af data, administration af tags eller visning af private optegnelser – er kun tilgængelige for brugere med tilstrækkelige tilladelser. Du kan tjekke din nuværende rolle i [Brugerindstillinger](settings.md). Hvis du har brug for mere adgang, skal du kontakte ejeren af dit træ eller administratoren. Se [Brugersystem](../install_setup/users.md) for en beskrivelse af alle roller.

## Navigering i grænsefladen

### Hovednavigation

Sidebaren (eller hamburger-menuen på mobile enheder) er den primære måde at bevæge sig mellem sektioner:

- **Hjem** – dashboardet (se nedenfor)
- **Blog** – familiehistorier skrevet som blogindlæg
- **Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter** – gennemse alle objekter af hver type
- **Medier** – gennemse alle mediefiler (fotos, dokumenter osv.)
- **Kort** – geografisk visning af steder i træet
- **Slægtstræ** – interaktive trædiagrammer
- **DNA** – DNA-matchanalyseværktøjer
- **Chat** – AI chatassistent (hvis aktiveret af administratoren)
- **Historik** – nyligt ændrede objekter
- **Bogmærker** – dine gemte bogmærker
- **Opgaver** – forskningsopgaver
- **Eksport** – eksportér slægtstræet
- **Rapporter** – generer rapporter
- **Revisioner** – fuld transaktionshistorik (synlig for medlemmer og derover)
- **Tags** – administrer tags (synlig for redaktører og derover)
- **Notifikationer** – tidligere notifikationer

### Øverste app-bar

Baren øverst på hver side indeholder:

- **Tilføj** (plus-ikon, synlig for bidragydere og derover) – åbner en menu for at oprette et nyt objekt: Person, Familie, Begivenhed, Sted, Kilde, Citering, Arkiv, Note, Medieobjekt eller Opgave
- **Søg** (forstørrelsesglas) – åbner søgesiden
- **Brugerikon** – åbner indstillingsmenuen: Brugerindstillinger, Administration (kun ejere), Administrer brugere (kun ejere), Systeminfo

## Hjemmesiden (dashboard)

Dashboardet vises, når du logger ind første gang. Det har to kolonner:

**Venstre kolonne:**

- **Hjempersonkort** – viser navnet, fotoet (hvis tilgængeligt) og nøglefakta om din valgte hjemperson, med et link til deres fulde profil og hurtig navigation til slægtstræet. Klik på knappen **Indstil hjemperson** på kortet for at søge efter og vælge en anden person.
- **Årsdage** – kommende fødselsdage og årsager fra træet, baseret på dagens dato.
- **Nyligt ændret** – en kort liste over de senest ændrede objekter, nyttig til at spore samarbejdende redigeringer.

**Højre kolonne:**

- **Nye blogindlæg** – de seneste indlæg fra [bloggen](blog.md), hvis der findes nogen.
- **Statistik** – et resumé af objektantal i træet (antal personer, familier, begivenheder osv.).

Hvis træadministrator har konfigureret en **hjemmeside note** og/eller et **hjemmeside billede**, vises disse fremtrædende over de vigtigste kolonner. Billedet vises ved siden af noteteksten, når begge er indstillet. Se [Administrationsindstillinger](../administration/settings.md#customization) for hvordan man konfigurerer disse.

!!! tip
    Hvis træet er tomt, og du har redigeringstilladelser, viser dashboardet en "Kom i gang" prompt med knapper til at tilføje din første person eller importere en slægtstræfil.
