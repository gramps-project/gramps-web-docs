# Tilpas træet

Træejere og administratorer kan tilpasse navnet og udseendet af træet samt dets startside for alle brugere. Disse indstillinger findes i sektionerne **Træindstillinger** og **Tilpasning** i [Administrationsindstillingerne](settings.md).

## Slægtstræ navn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træ opsætning](../install_setup/multi-tree.md) eller når `TREE_ID` er eksplicit indstillet i [serverkonfigurationen](../install_setup/configuration.md). I en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette medføre en fejl.

Dette gør det muligt at ændre navnet på den underliggende Gramps slægtstrædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

!!! tip
    Hvis du kun ønsker at ændre navnet vist i app-baren uden at omdøbe databasen, skal du i stedet bruge indstillingen [App titel](#app-title).

## Forskerinformation

Indstil navn, adresse og kontaktoplysninger for den primære forsker. Disse oplysninger er indlejret i eksport (f.eks. GEDCOM-filer).

## Tema farver

Indstil en tilpasset **primær farve** og **accentfarve** for Gramps Web-grænsefladen. Disse farver anvendes for alle brugere af dette træ og træder i kraft straks efter gemning.

Brug farvevælgerne til at vælge farver, og klik derefter på **Gem**. Klik på **Nulstil** for at vende tilbage til standardindstillingerne.

## App titel

Indstil en tilpasset titel for applikationen. Hvis den er indstillet, overskriver denne titlen på slægtstræet i browserens titelbar og den øverste app-bar.

Indtast en titel og klik på **Gem**. Lad stå tomt for at bruge standarden (slægtstræets navn).

## Startside note

Vælg et Gramps **Note** objekt til at vise på dashboardets startside. Noteindholdet vises under de primære dashboardkolonner og er synligt for alle brugere med adgang til træet.

Brug objektvælgeren til at søge efter og vælge en note, og gem derefter. Klik på **Fjern** for at slette den nuværende startside note.

## Startside billede

Vælg et Gramps **Media** objekt til at vise som et billede på dashboardets startside. Når det kombineres med en startside note, vises billedet ved siden af noteteksten. Uden en note vises kun billedet.

Brug objektvælgeren til at søge efter og vælge et medieobjekt, og gem derefter. Klik på **Fjern** for at slette det nuværende startside billede.

## Eksport/import indstillinger

Træniveauindstillinger (app titel, tema farver, startside note/billede osv.) kan eksporteres som en JSON-fil til backup eller for at kopiere til en anden Gramps Web-instans.

- Klik på **Eksporter indstillinger** for at downloade de nuværende indstillinger som en JSON-fil.
- Klik på **Importer træindstillinger** for at uploade en tidligere eksporteret JSON-fil og anvende indstillingerne.
