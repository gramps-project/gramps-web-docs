# Administration Indstillinger

Siden **Indstillinger > Administration** er tilgængelig via brugerikonet i den øverste app-bar. Den er kun tilgængelig for brugere med ejer- eller administratorrolle og giver værktøjer til at administrere familie trædatabasen.

Siden er organiseret i foldbare sektioner. Klik på en sektionoverskrift for at udvide den.

## Data

Dækker brugskvoter, import af data og mediefiladministration.

### Brugskvoter

Toppen af sektionen viser nuværende brug i forhold til eventuelle konfigurerede grænser:

- **Personer** – antallet af personobjekter i træet versus den konfigurerede maksimale (∞ hvis ubegrænset)
- **Medielagring** – den samlede størrelse af uploadede mediefiler versus den konfigurerede lagerkvote (∞ hvis ubegrænset)

Kvoterne er sat af serveradministratoren; se [Serverkonfiguration](../install_setup/configuration.md) for detaljer.

### Importer data

Importsektionen giver dig mulighed for at uploade en familie træfil eller et mediearkiv. Se [Importer data](import.md) for fulde instruktioner.

### Mediefilstatus

Denne sektion viser:

- Det samlede antal medieobjekter i træet og om nogle mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler på serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data blev importeret fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades via import mediearkiv-funktionen.

### Importer mediearkiv

Giver mulighed for at uploade en ZIP-fil med mediefiler for at udfylde manglende filer. Se [Importer data](import.md) for fulde instruktioner.

## Søg indeks

### Administrer søgeindeks

Gramps Web opretholder et fuldtekst søgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der i øjeblikket er indekseret versus det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En fremdriftsindikator vises, mens opgaven kører i baggrunden. Dette er sjældent nødvendigt.

Hvis et træ endnu ikke har noget søgeindeks, for eksempel efter en serveropgradering, der ændrede indeksformatet, bygger Gramps Web det i baggrunden første gang træet åbnes. Mens det bliver bygget, viser sektionen "Søgeindekset bliver bygget." i stedet for tællerne, **Opdater søgeindeks** er deaktiveret, og søgeresultaterne kan være ufuldstændige. Bygningen vises i [Notifikationer](../user-guide/notifications.md) som opgaven "Opdater søgeindeks".

## Træindstillinger

### Familie Træ navn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træ opsætning](../install_setup/multi-tree.md) eller når `TREE_ID` er eksplicit indstillet i [serverkonfigurationen](../install_setup/configuration.md). På en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette give en fejl.

Dette giver mulighed for at ændre navnet på den underliggende Gramps familie trædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

!!! tip
    Hvis du kun ønsker at ændre navnet vist i app-baren uden at omdøbe databasen, brug indstillingen [App titel](#app-title) i stedet.

### Forskerinformation

Indstil navnet, adressen og kontaktoplysningerne for den primære forsker. Disse oplysninger er indlejret i eksporter (f.eks. GEDCOM-filer).

## Tilpasning

### Tema farver

Indstil en brugerdefineret **primær farve** og **accentfarve** for Gramps Web-grænsefladen. Disse farver anvendes for alle brugere af dette træ og træder i kraft straks efter gemning.

Brug farvevælgerne til at vælge farver, og klik derefter på **Gem**. Klik på **Nulstil** for at vende tilbage til standardindstillingerne.

### App titel

Indstil en brugerdefineret titel for applikationen. Hvis den er indstillet, overskriver den navnet på familie træet i browserens titelbar og den øverste app-bar.

Indtast en titel og klik på **Gem**. Lad være med at udfylde for at bruge standarden (familie træ navn).

### Hjemmeside note

Vælg et Gramps **Note** objekt til at vise på dashboardets startside. Noteindholdet gengives under de vigtigste dashboardkolonner og er synligt for alle brugere med adgang til træet.

Brug objektvælgeren til at søge efter og vælge en note, og gem derefter. Klik på **Fjern** for at rydde den nuværende hjemmeside note.

### Hjemmeside billede

Vælg et Gramps **Media** objekt til at vise som billede på dashboardets startside. Når det kombineres med en hjemmeside note, vises billedet ved siden af noteteksten. Uden en note vises kun billedet.

Brug objektvælgeren til at søge efter og vælge et medieobjekt, og gem derefter. Klik på **Fjern** for at rydde det nuværende hjemmesidebillede.

### Eksport/Import indstillinger

Træniveauindstillinger (app titel, tema farver, hjemmeside note/billede osv.) kan eksporteres som en JSON-fil til backup eller til at kopiere til en anden Gramps Web-instans.

- Klik på **Eksporter indstillinger** for at downloade de nuværende indstillinger som en JSON-fil.
- Klik på **Importer træindstillinger** for at uploade en tidligere eksporteret JSON-fil og anvende indstillingerne.

## Familie Træ Behandling

### Tjek og Reparer Database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med værktøjet [Tjek og Reparer Database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og Reparer** og vent på, at fremdriftsindikatoren fuldføres. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

### Verificer Dataene

Mens [Tjek og Reparer Database](#check-and-repair-database) leder efter *tekniske* inkonsistenser, leder dette værktøj efter *utroværdige* data – analogt med værktøjet [Verificer Dataene](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) i Gramps Desktop. Det rapporterer ting, der ikke er umulige, men som er usandsynlige nok til at være værd at tage et ekstra kig på, såsom en mor på 12 eller en person, der levede til 130.

Under **Indstillinger** kan du justere tærsklerne, som testene bruger – maksimal alder, minimums- og maksimumsalder for at gifte sig eller få børn, maksimalt antal børn osv. – samt om der skal estimeres manglende eller unøjagtige datoer og om der skal rapporteres ugyldige datoer som 31. februar.

Klik på **Verificer Dataene** for at starte. Tjekket kører som en baggrundsopgave, og resultaterne listes derefter under **Data Verifikationsresultater**. Intet ændres af dette værktøj: det rapporterer kun, hvad det finder.

!!! note
    En fund er ikke bevis på en fejl. Lange liv og store aldersforskelle forekommer, så behandl resultaterne som en liste over ting, der skal tjekkes, snarere end en liste over ting, der skal rettes.

## Tags

### Administrer tags

Opret, omdøb, ændre farve og slet [tags](../user-guide/tags.md) for familie træet. Tags gemmes i Gramps-databasen, deles på tværs af alle brugere og er fuldt kompatible med Gramps Desktop.

Klik på **Ny Tag** for at oprette et tag. Brug kontrollerne ved siden af et eksisterende tag for at omdøbe det (blyantikon), ændre dets farve (farvevælger) eller slette det (sletteikon).

!!! note
    Sletning af et tag fjerner det fra alle objekter, det blev anvendt på.

Se [Tags](../user-guide/tags.md) for hvordan tags bruges i hele Gramps Web, inklusive de særlige `Blog` og `ToDo` tags.

## Backups

En backup indeholder familie trædata, inklusive private optegnelser, træindstillingerne og brugerne af træet. Mediefiler er ikke inkluderet; se [Sikkerhedskopier dine mediefiler](export.md#back-up-your-media-files).

### Gemte backups

Hvis serveradministratoren har indstillet en backupmappe (`BACKUP_DIR`, se [Serverkonfiguration](../install_setup/configuration.md)), kan backups gemmes på serveren. Ellers viser sektionen en meddelelse om, at opbevaring af backups ikke er konfigureret, og kun gendannelse fra en uploadet fil er tilgængelig.

Klik på **Lav Backup...** for at oprette en backup. Den oprettes som en baggrundsopgave og vises derefter i listen over gemte backups, med sin dato, antallet af personer og sin størrelse. Serveren opbevarer kun de nyeste backups (fem som standard) og sletter automatisk ældre. Antallet af backups, der kan oprettes pr. dag, er også begrænset.

For hver gemt backup kan du:

- **Download** den som en `.tar` fil, for eksempel for at gemme en kopi et andet sted.
- **Gendanne** den, som beskrevet nedenfor.
- **Slette** den, efter bekræftelse.

En backup lavet med en nyere version af Gramps Web end den, der kører på serveren, er markeret med et advarselsikon og kan ikke gendannes.

### Gendan fra Backup

Gendanner træet fra en gemt backup eller fra en uploadet fil. For at gendanne en gemt backup, klik på gendannelsesknappen ved siden af den. For at gendanne fra en fil, vælg en Gramps Web backup (`.tar`) eller en Gramps XML-fil (`.gramps`) og klik på **Gendan**.

!!! danger
    Gendannelse af data er en destruktiv erstatning, ikke en sammensmeltning. Ethvert eksisterende objekt, der ikke er til stede i backupen, slettes.

For en Gramps Web backup vises en dialog, der viser, hvornår backupen blev lavet, for hvilket træ, og med hvilken version, og lader dig vælge, hvilke dele der skal gendannes:

- **Data** – objekterne i familie træet
- **Træindstillinger** – indstillingerne på denne side, såsom tema farver, app titel og hjemmeside note
- **Brugere** – brugerne af træet

Klik på **Forhåndsvisning** for at se, hvad gendannelsen ville ændre. En Gramps XML-fil indeholder kun data, så for en sådan fil starter forhåndsvisningen straks. Du vil blive bedt om at re-authentificere, hvis din session ikke er frisk nok. Forhåndsvisningen kører som en baggrundsopgave, og når den er fuldført, åbner den en dialog, der opsummerer ændringerne pr. objekttype (personer, familier, begivenheder, steder, citater, kilder, arkiver, medieobjekter, noter, tags), og for træindstillingerne og brugerne, hvis valgt:

- **Tilføj** – objekter til stede i backupen, men mangler fra det nuværende træ
- **Opdater** – objekter til stede i begge, der adskiller sig
- **Slet** – objekter i det nuværende træ, der er fraværende fra backupen
- **Uændret** – objekter identiske i begge

Hvis nogen objekter ville blive slettet, advarer dialogen om, hvor mange. Gennemgå resuméet, og klik derefter på **Gendan** for at anvende ændringerne, eller **Annuller** for at annullere.

Efter gendannelsen listes brugere, der blev tilføjet fra backupen. De får et tilfældigt kodeord, så de skal nulstille deres kodeord, før de kan logge ind. Brugere, der allerede eksisterer på serveren, ændres aldrig. Medieobjekter, hvis filer mangler på serveren, listes også; upload dem via [Importer mediearkiv](#import-media-archive).

!!! note
    Gendannelse af data gendanner kun objektdata og mediereferencer. Binære mediefiler selv og træmetadata (standardperson, bogmærker, navnegrupper) påvirkes ikke.

!!! tip
    Brug dette til at rulle et træ tilbage til en kendt god backup, for eksempel efter en dårlig import eller en uønsket masseændring.

## Farezone

!!! danger
    Handlinger i Farezonen er **irreversible**. Lav en [backup](#backups) før du fortsætter.

### Slet alle objekter

Fjerner objekter fra familie træet. Klik på **Slet** for at åbne en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder helt træet
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-authentificere (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremdriftsindikator vises.

!!! warning
    Sletning af kun et delmængde af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekter.

!!! tip
    Brug dette til at starte frisk før import af et nyt træ, eller til at fjerne specifikke objekttyper, der blev importeret forkert.
