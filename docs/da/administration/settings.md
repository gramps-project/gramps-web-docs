# Administration Indstillinger

Siden **Indstillinger > Administration** er tilgængelig via brugerikonet i den øverste app-bar. Den er kun tilgængelig for brugere med ejer- eller administratorrolle og giver værktøjer til at administrere slægtstrædatabasen.

Siden er organiseret i foldbare sektioner. Klik på en sektionoverskrift for at udvide den.

## Data

Dækker brugsgrænser, import af data og mediefiladministration.

### Brugsgrænser

Toppen af sektionen viser nuværende brug i forhold til eventuelle konfigurerede grænser:

- **Personer** – antallet af personobjekter i træet i forhold til den konfigurerede maksimum (∞ hvis ubegrænset)
- **Medielagring** – den samlede størrelse af uploadede mediefiler i forhold til den konfigurerede lagringsgrænse (∞ hvis ubegrænset)

Grænserne sættes af serveradministratoren; se [Serverkonfiguration](../install_setup/configuration.md) for detaljer.

### Importer data

Importsektionen lader dig uploade en slægtstræfil eller et mediearkiv. Se [Importer data](import.md) for fulde instruktioner.

### Mediefilstatus

Denne sektion viser:

- Det samlede antal medieobjekter i træet og om nogen mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler fra serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data importeres fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades via funktionen til import af mediearkiv.

### Importer mediearkiv

Muliggør upload af en ZIP-fil med mediefiler for at udfylde manglende filer. Se [Importer data](import.md) for fulde instruktioner.

## Søg indeks

### Administrer søgeindeks

Gramps Web opretholder et fuldtekstsøgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der aktuelt er indekseret i forhold til det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En fremdriftsindikator vises, mens opgaven kører i baggrunden. Dette er normalt kun nødvendigt efter en serveropgradering.

### Semantisk søgeindeks

Hvis serveren har [semantisk (AI-drevet) søgning aktiveret](../install_setup/configuration.md), vises en ekstra sektion med to handlinger:

- **Regenerer semantisk søgeindeks** – genopbygger hele det semantiske indeks fra bunden. Dette er beregningsmæssigt dyrt og kan tage lang tid.
- **Opdater semantisk søgeindeks** – udfører en inkrementel opdatering, der kun tilføjer objekter, der endnu ikke er indekseret. Hurtigere end en fuld genopbygning.

## Træindstillinger

### Slægtstræ navn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træ opsætning](../install_setup/multi-tree.md) eller når `TREE_ID` eksplicit er indstillet i [serverkonfigurationen](../install_setup/configuration.md). På en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette give en fejl.

Dette giver mulighed for at ændre navnet på den underliggende Gramps slægtstrædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

!!! tip
    Hvis du kun ønsker at ændre navnet vist i app-baren uden at omdøbe databasen, brug indstillingen [App titel](#app-title) i stedet.

### Forskerinformation

Indstil navnet, adressen og kontaktoplysningerne for den primære forsker. Disse oplysninger er indlejret i eksporter (f.eks. GEDCOM-filer).

## Tilpasning

### Tema farver

Indstil en brugerdefineret **primær farve** og **accentfarve** for Gramps Web-grænsefladen. Disse farver anvendes for alle brugere af dette træ og træder i kraft straks efter gemning.

Brug farvevælgerne til at vælge farver, og klik derefter på **Gem**. Klik på **Nulstil** for at vende tilbage til standardindstillingerne.

### App titel

Indstil en brugerdefineret titel for applikationen. Hvis den er indstillet, overskriver dette slægtstrænavnet i browserens titelbar og den øverste app-bar.

Indtast en titel og klik på **Gem**. Lad være med at udfylde for at bruge standarden (slægtstrænavnet).

### Hjemmeside note

Vælg et Gramps **Note** objekt til at vise på dashboardets hjemmeside. Noteindholdet gengives under de primære dashboardkolonner og er synligt for alle brugere med adgang til træet.

Brug objektvælgeren til at søge efter og vælge en note, og gem derefter. Klik på **Fjern** for at rydde den nuværende hjemmeside note.

### Hjemmeside billede

Vælg et Gramps **Media** objekt til at vise som et billede på dashboardets hjemmeside. Når det kombineres med en hjemmeside note, vises billedet ved siden af noteteksten. Uden en note vises kun billedet.

Brug objektvælgeren til at søge efter og vælge et medieobjekt, og gem derefter. Klik på **Fjern** for at rydde det nuværende hjemmeside billede.

### Eksport/Import indstillinger

Træniveauindstillinger (apptitel, tema farver, hjemmeside note/billede osv.) kan eksporteres som en JSON-fil til backup eller til at kopiere til en anden Gramps Web-forekomst.

- Klik på **Eksportér indstillinger** for at downloade de nuværende indstillinger som en JSON-fil.
- Klik på **Importer træindstillinger** for at uploade en tidligere eksporteret JSON-fil og anvende indstillingerne.

## Slægtstræ Behandling

### Tjek og Reparer Database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med værktøjet [Tjek og Reparer Database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og Reparer** og vent på, at fremdriftsindikatoren fuldføres. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

### Bekræft Dataene

Mens [Tjek og Reparer Database](#check-and-repair-database) ser efter *tekniske* inkonsistenser, ser dette værktøj efter *usandsynlige* data – analogt med værktøjet [Bekræft Dataene](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) i Gramps Desktop. Det rapporterer ting, der ikke er umulige, men som er usandsynlige nok til at være værd at se nærmere på, såsom en mor på 12 år eller en person, der levede til 130.

Under **Indstillinger** kan du justere tærsklerne, som testene bruger – maksimal alder, minimums- og maksimumsalder for at gifte sig eller få børn, maksimalt antal børn osv. – samt om der skal estimeres manglende eller unøjagtige datoer, og om der skal rapporteres ugyldige datoer som 31. februar.

Klik på **Bekræft Dataene** for at starte. Tjekket kører som en baggrundsopgave, og resultaterne listes derefter under **Data Verifikationsresultater**. Intet ændres af dette værktøj: det rapporterer kun, hvad det finder.

!!! note
    En opdagelse er ikke bevis på en fejl. Lange liv og store aldersforskelle forekommer, så behandl resultaterne som en liste over ting, der skal tjekkes, snarere end en liste over ting, der skal rettes.

## Tags

### Administrer tags

Opret, omdøb, ændr farve og slet [tags](../user-guide/tags.md) for slægtstræet. Tags gemmes i Gramps-databasen, deles på tværs af alle brugere og er fuldt kompatible med Gramps Desktop.

Klik på **Ny Tag** for at oprette et tag. Brug kontrollerne ved siden af et eksisterende tag for at omdøbe det (blyantikon), ændre dets farve (farvevælger) eller slette det (sletteikon).

!!! note
    Sletning af et tag fjerner det fra alle objekter, det blev anvendt på.

Se [Tags](../user-guide/tags.md) for hvordan tags bruges i hele Gramps Web, inklusive de specielle `Blog` og `ToDo` tags.

## Farezone

!!! danger
    Handlinger i Farezonen er **irreversible**. Lav en backup, før du fortsætter.

### Slet alle objekter

Fjerner objekter fra slægtstræet. Klik på **Slet** for at åbne en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder træet helt
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-autentificere (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremdriftsindikator vises.

!!! warning
    At slette kun et delmængde af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekter.

!!! tip
    Brug dette til at starte forfra, før du importerer et nyt træ, eller til at fjerne specifikke objekttyper, der blev importeret forkert.

### Gendan fra Backup

Nulstiller træet for at matche en uploadet Gramps XML (`.gramps`) backupfil, tilføjer, opdaterer og sletter objekter efter behov, så træet ender med at være identisk med backupen.

!!! danger
    Dette er en destruktiv erstatning, ikke en sammenlægning. Enhver eksisterende objekt, der ikke er til stede i den uploadede backup, slettes.

Upload en `.gramps` fil, og klik derefter på **Forhåndsvis Gendan**. Du vil blive bedt om at re-autentificere, hvis din session ikke er frisk nok. En forhåndsvisning kører som en baggrundsopgave, og når den er færdig, åbnes en dialog, der opsummerer ændringerne pr. objekttype (personer, familier, begivenheder, steder, citater, kilder, arkiver, medieobjekter, noter, tags):

- **Tilføj** – objekter til stede i backupen, men mangler i det nuværende træ
- **Opdater** – objekter til stede i begge, der adskiller sig
- **Slet** – objekter i det nuværende træ, der er fraværende fra backupen
- **Uændret** – objekter identiske i begge

Hvis nogen objekter ville blive slettet, advarer dialogen om, hvor mange. Gennemgå resuméet, og klik derefter på **Gendan** for at anvende ændringerne, eller **Annuller** for at annullere.

!!! note
    Kun objektdata og mediereferencer gendannes. Binære mediefiler selv og træmetadata (standardperson, bogmærker, navnegrupper) påvirkes ikke. Gendan manglende mediefiler separat via [Importer mediearkiv](#import-media-archive), hvis nødvendigt.

!!! tip
    Brug dette til at rulle et træ tilbage til en kendt god Gramps XML backup, for eksempel efter en dårlig import eller en uønsket masseændring.
