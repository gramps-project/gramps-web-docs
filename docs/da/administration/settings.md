# Administrationsindstillinger

Siden **Indstillinger > Administration** er tilgængelig via brugerikonet i den øverste app-bar. Den er kun tilgængelig for brugere med ejer- eller administratorrolle og giver værktøjer til at administrere familie trædatabasen.

Siden er organiseret i sammenklappelige sektioner. Klik på en sektionoverskrift for at udvide den.

## Data

Dækker brugskvoter, import af data og mediefiladministration.

### Brugskvoter

Toppen af sektionen viser nuværende brug i forhold til eventuelle konfigurerede grænser:

- **Personer** – antallet af personobjekter i træet i forhold til den konfigurerede maksimum (∞ hvis ubegrænset)
- **Medielagring** – den samlede størrelse af uploadede mediefiler i forhold til den konfigurerede lagerkvote (∞ hvis ubegrænset)

Kvoterne sættes af serveradministratoren; se [Serverkonfiguration](../install_setup/configuration.md) for detaljer.

### Importer data

Importsektionen lader dig uploade en familie træfil eller et mediearkiv. Se [Importer data](import.md) for fulde instruktioner.

### Mediefilstatus

Denne sektion viser:

- Det samlede antal medieobjekter i træet og om nogen mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler fra serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data er importeret fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades via funktionen til import af mediearkiv.

### Importer mediearkiv

Muliggør upload af en ZIP-fil med mediefiler for at udfylde manglende filer. Se [Importer data](import.md) for fulde instruktioner.

## Søgeindeks

### Administrer søgeindeks

Gramps Web opretholder et fuldtekst-søgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der i øjeblikket er indekseret i forhold til det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En fremdriftsindikator vises, mens opgaven kører i baggrunden. Dette er normalt kun nødvendigt efter en serveropgradering.

### Semantisk søgeindeks

Hvis serveren har [semantisk (AI-drevet) søgning aktiveret](../install_setup/configuration.md), vises en ekstra sektion med to handlinger:

- **Regenerer semantisk søgeindeks** – genopbygger hele det semantiske indeks fra bunden. Dette er beregningsmæssigt dyrt og kan tage lang tid.
- **Opdater semantisk søgeindeks** – udfører en inkrementel opdatering, der kun tilføjer objekter, der endnu ikke er indekseret. Hurtigere end en fuld genopbygning.

## Træindstillinger

### Familietrænavn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træopsætning](../install_setup/multi-tree.md) eller når `TREE_ID` er eksplicit indstillet i [serverkonfigurationen](../install_setup/configuration.md). På en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette give en fejl.

Dette giver mulighed for at ændre navnet på den underliggende Gramps familietrædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

!!! tip
    Hvis du kun ønsker at ændre navnet, der vises i app-baren uden at omdøbe databasen, skal du i stedet bruge indstillingen [App-titel](#app-title).

### Forskerinformation

Indstil navnet, adressen og kontaktoplysningerne for den primære forsker. Disse oplysninger er indlejret i eksporter (f.eks. GEDCOM-filer).

## Tilpasning

### Tema farver

Indstil en tilpasset **primær farve** og **accentfarve** for Gramps Web-grænsefladen. Disse farver anvendes for alle brugere af dette træ og træder i kraft straks efter gemning.

Brug farvevælgerne til at vælge farver, og klik derefter på **Gem**. Klik på **Nulstil** for at vende tilbage til standardindstillingerne.

### App-titel

Indstil en tilpasset titel for applikationen. Hvis den er indstillet, overskriver den familietrænavnet i browserens titelbar og den øverste app-bar.

Indtast en titel og klik på **Gem**. Lad være med at udfylde for at bruge standarden (familietrænavnet).

### Hjemmeside note

Vælg et Gramps **Note** objekt til at vise på dashboardets startside. Noteindholdet vises under de vigtigste dashboardkolonner og er synligt for alle brugere med adgang til træet.

Brug objektvælgeren til at søge efter og vælge en note, og gem derefter. Klik på **Fjern** for at rydde den nuværende hjemmeside note.

### Hjemmeside billede

Vælg et Gramps **Media** objekt til at vise som et billede på dashboardets startside. Når det kombineres med en hjemmeside note, vises billedet ved siden af noteteksten. Uden en note vises kun billedet.

Brug objektvælgeren til at søge efter og vælge et medieobjekt, og gem derefter. Klik på **Fjern** for at rydde det nuværende hjemmesidebillede.

### Eksport/Import indstillinger

Træniveauindstillinger (app-titel, tema farver, hjemmeside note/billede osv.) kan eksporteres som en JSON-fil til backup eller til at kopiere til en anden Gramps Web-instans.

- Klik på **Eksporter indstillinger** for at downloade de nuværende indstillinger som en JSON-fil.
- Klik på **Importer træindstillinger** for at uploade en tidligere eksporteret JSON-fil og anvende indstillingerne.

## Familietræbehandling

### Tjek og reparation af database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med værktøjet [Tjek og reparation af database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og reparation** og vent på, at fremdriftsindikatoren er færdig. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

## Farezone

!!! danger
    Handlinger i farezonen er **irreversible**. Lav en backup, før du fortsætter.

### Slet alle objekter

Fjerner objekter fra familietræet. Klik på **Slet** for at åbne en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder helt træet
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-autoriseres (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremdriftsindikator vises.

!!! warning
    At slette kun en delmængde af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekter.

!!! tip
    Brug dette til at starte forfra, før du importerer et nyt træ, eller til at fjerne specifikke objekttyper, der blev importeret forkert.
