# Administration Indstillinger

Siden **Indstillinger > Administration** er tilgængelig via brugerikonet i den øverste app-bar. Den er kun tilgængelig for brugere med ejer- eller administratorrolle og giver værktøjer til at administrere familietrædatabasen.

Siden er organiseret i sammenklappelige sektioner. Klik på en sektionoverskrift for at udvide den.

## Data

Dækker brugsgrænser, import af data og mediefiladministration.

### Brugsgrænser

Toppen af sektionen viser nuværende brug i forhold til eventuelle konfigurerede grænser:

- **Personer** – antallet af personobjekter i træet versus den konfigurerede maksimum (∞ hvis ubegrænset)
- **Medielagring** – den samlede størrelse af uploadede mediefiler versus den konfigurerede lagergrænse (∞ hvis ubegrænset)

Grænserne sættes af serveradministratoren; se [Serverkonfiguration](../install_setup/configuration.md) for detaljer.

### Importer data

Importsektionen lader dig uploade en familietrefil eller et mediearkiv. Se [Importer data](import.md) for fulde instruktioner.

### Mediefilstatus

Denne sektion viser:

- Det samlede antal medieobjekter i træet og om nogle mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler fra serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data blev importeret fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades via funktionen til import af mediearkiv.

### Importer mediearkiv

Tillader upload af en ZIP-fil med mediefiler for at udfylde manglende filer. Se [Importer data](import.md) for fulde instruktioner.

## Søg indeks

### Administrer søgeindeks

Gramps Web opretholder et fuldtekst søgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der i øjeblikket er indekseret versus det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En fremdriftsindikator vises, mens opgaven kører i baggrunden. Dette er normalt kun nødvendigt efter en serveropgradering.

### Semantisk søgeindeks

!!! warning "Forældet"
    Semantisk søgning er forældet og vil blive fjernet i Gramps Web API 3.25, sammen med denne sektion. AI-chat har ikke brug for det, da Gramps Web API 3.24.

Hvis serveren har [semantisk (AI-drevet) søgning aktiveret](../install_setup/chat.md#semantic-search-deprecated), vises en ekstra sektion med to handlinger:

- **Regenerer semantisk søgeindeks** – genopbygger hele det semantiske indeks fra bunden. Dette er beregningsmæssigt dyrt og kan tage lang tid.
- **Opdater semantisk søgeindeks** – udfører en inkrementel opdatering, der kun tilføjer objekter, der endnu ikke er indekseret. Hurtigere end en fuld genopbygning.

## Træindstillinger

### Familietræ navn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træ opsætning](../install_setup/multi-tree.md) eller når `TREE_ID` er eksplicit indstillet i [serverkonfigurationen](../install_setup/configuration.md). På en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette give en fejl.

Dette giver mulighed for at ændre navnet på den underliggende Gramps familietrædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

!!! tip
    Hvis du kun ønsker at ændre navnet vist i app-bar, uden at omdøbe databasen, skal du i stedet bruge indstillingen [App titel](#app-title).

### Forskerinformation

Indstil navnet, adressen og kontaktoplysningerne for den primære forsker. Disse oplysninger er indlejret i eksporter (f.eks. GEDCOM-filer).

## Tilpasning

### Tema farver

Indstil en brugerdefineret **primær farve** og **accentfarve** for Gramps Web-grænsefladen. Disse farver anvendes på alle brugere af dette træ og træder i kraft straks efter gemning.

Brug farvevælgerne til at vælge farver, og klik derefter på **Gem**. Klik på **Nulstil** for at vende tilbage til standardindstillingerne.

### App titel

Indstil en brugerdefineret titel for applikationen. Hvis den er indstillet, overskriver den familietrænavnet i browserens titelbar og den øverste app-bar.

Indtast en titel og klik på **Gem**. Lad være med at udfylde for at bruge standarden (familietrænavnet).

### Hjemmeside note

Vælg et Gramps **Note** objekt til at vise på dashboardets hjemmeside. Notens indhold gengives under de primære dashboardkolonner og er synligt for alle brugere med adgang til træet.

Brug objektvælgeren til at søge efter og vælge en note, og gem derefter. Klik på **Fjern** for at rydde den nuværende hjemmeside note.

### Hjemmeside billede

Vælg et Gramps **Media** objekt til at vise som et billede på dashboardets hjemmeside. Når det kombineres med en hjemmeside note, vises billedet ved siden af noteteksten. Uden en note vises kun billedet.

Brug objektvælgeren til at søge efter og vælge et medieobjekt, og gem derefter. Klik på **Fjern** for at rydde det nuværende hjemmeside billede.

### Eksport/Import indstillinger

Træniveauindstillinger (app titel, tema farver, hjemmeside note/billede osv.) kan eksporteres som en JSON-fil til backup eller til at kopiere til en anden Gramps Web-instans.

- Klik på **Eksportér indstillinger** for at downloade de nuværende indstillinger som en JSON-fil.
- Klik på **Importer træindstillinger** for at uploade en tidligere eksporteret JSON-fil og anvende indstillingerne.

## Familietræ Behandling

### Tjek og Reparer Database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med [Tjek og Reparer Database værktøjet](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og Reparer** og vent på, at fremdriftsindikatoren fuldføres. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

### Verificer Data

Mens [Tjek og Reparer Database](#check-and-repair-database) leder efter *tekniske* inkonsistenser, leder dette værktøj efter *usandsynlige* data – analogt med [Verificer Data værktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) i Gramps Desktop. Det rapporterer ting, der ikke er umulige, men som er usandsynlige nok til at være værd at kigge nærmere på, såsom en mor på 12 år eller en person, der levede til 130.

Under **Indstillinger** kan du justere tærsklerne, som testene bruger – maksimal alder, minimums- og maksimumsalder for at gifte sig eller få børn, maksimum antal børn osv. – samt om der skal estimeres manglende eller unøjagtige datoer, og om der skal rapporteres ugyldige datoer såsom 31. februar.

Klik på **Verificer Data** for at starte. Tjekket kører som en baggrundsopgave, og resultaterne listes derefter under **Data Verifikationsresultater**. Intet ændres af dette værktøj: det rapporterer kun, hvad det finder.

!!! note
    En fund er ikke bevis på en fejl. Lange liv og store aldersforskelle forekommer, så behandl resultaterne som en liste over ting at tjekke snarere end en liste over ting at rette.

## Tags

### Administrer tags

Opret, omdøb, ændre farve og slet [tags](../user-guide/tags.md) for familietræet. Tags gemmes i Gramps-databasen, deles mellem alle brugere og er fuldt kompatible med Gramps Desktop.

Klik på **Ny Tag** for at oprette et tag. Brug kontrollerne ved siden af et eksisterende tag til at omdøbe det (blyantikon), ændre dets farve (farvevælger) eller slette det (sletteikon).

!!! note
    Sletning af et tag fjerner det fra alle objekter, det blev anvendt på.

Se [Tags](../user-guide/tags.md) for hvordan tags bruges i hele Gramps Web, inklusive de specielle `Blog` og `ToDo` tags.

## Sikkerhedskopier

En sikkerhedskopi indeholder familietrædata, inklusive private optegnelser, træindstillinger og brugerne af træet. Mediefiler er ikke inkluderet; se [Sikkerhedskopier dine mediefiler](export.md#back-up-your-media-files).

### Gemte sikkerhedskopier

Hvis serveradministratoren har indstillet et sikkerhedskopimappe (`BACKUP_DIR`, se [Serverkonfiguration](../install_setup/configuration.md)), kan sikkerhedskopier gemmes på serveren. Ellers viser sektionen en meddelelse om, at opbevaring af sikkerhedskopier ikke er konfigureret, og at kun gendannelse fra en uploadet fil er tilgængelig.

Klik på **Lav Sikkerhedskopi...** for at oprette en sikkerhedskopi. Den oprettes som en baggrundsopgave og vises derefter i listen over gemte sikkerhedskopier, med dens dato, antallet af personer og dens størrelse. Serveren opbevarer kun de nyeste sikkerhedskopier (fem som standard) og sletter automatisk ældre. Antallet af sikkerhedskopier, der kan oprettes pr. dag, er også begrænset.

For hver gemt sikkerhedskopi kan du:

- **Download** den som en `.tar` fil, for eksempel for at gemme en kopi et andet sted.
- **Gendanne** den, som beskrevet nedenfor.
- **Slette** den, efter bekræftelse.

En sikkerhedskopi lavet med en nyere version af Gramps Web end den, der kører på serveren, er markeret med et advarselsikon og kan ikke gendannes.

### Gendan fra Sikkerhedskopi

Gendanner træet fra en gemt sikkerhedskopi eller fra en uploadet fil. For at gendanne en gemt sikkerhedskopi skal du klikke på gendannelsesknappen ved siden af den. For at gendanne fra en fil skal du vælge en Gramps Web sikkerhedskopi (`.tar`) eller en Gramps XML-fil (`.gramps`) og klikke på **Gendan**.

!!! danger
    Gendannelse af data er en destruktiv erstatning, ikke en sammenlægning. Ethvert eksisterende objekt, der ikke er til stede i sikkerhedskopien, slettes.

For en Gramps Web sikkerhedskopi vises en dialog, der viser, hvornår sikkerhedskopien blev lavet, for hvilket træ, og med hvilken version, og lader dig vælge, hvilke dele der skal gendannes:

- **Data** – objekterne i familietræet
- **Træindstillinger** – indstillingerne på denne side, såsom tema farver, app titel og hjemmeside note
- **Brugere** – brugerne af træet

Klik på **Forhåndsvisning** for at se, hvad gendannelsen ville ændre. En Gramps XML-fil indeholder kun data, så forhåndsvisningen starter straks for en sådan fil. Du vil blive bedt om at re-autoriserer, hvis din session ikke er frisk nok. Forhåndsvisningen kører som en baggrundsopgave, og når den er fuldført, åbnes en dialog, der opsummerer ændringerne pr. objekttype (personer, familier, begivenheder, steder, citater, kilder, arkiver, medieobjekter, noter, tags), og for træindstillinger og brugere, hvis valgt:

- **Tilføj** – objekter til stede i sikkerhedskopien, men mangler i det nuværende træ
- **Opdater** – objekter til stede i begge, der adskiller sig
- **Slet** – objekter i det nuværende træ, der er fraværende fra sikkerhedskopien
- **Uændret** – objekter identiske i begge

Hvis der skulle slettes nogen objekter, advarer dialogen om, hvor mange. Gennemgå resuméet, og klik derefter på **Gendan** for at anvende ændringerne, eller **Annuller** for at annullere.

Efter gendannelsen listes brugere, der blev tilføjet fra sikkerhedskopien. De får et tilfældigt kodeord, så de skal nulstille deres kodeord, før de kan logge ind. Brugere, der allerede eksisterer på serveren, ændres aldrig. Medieobjekter, hvis filer mangler på serveren, listes også; upload dem via [Importer mediearkiv](#import-media-archive).

!!! note
    Gendannelse af data gendanner kun objektdata og mediereferencer. Binære mediefiler selv og træmetadata (standardperson, bogmærker, navnegrupper) påvirkes ikke.

!!! tip
    Brug dette til at rulle et træ tilbage til en kendt god sikkerhedskopi, for eksempel efter en dårlig import eller en uønsket masseændring.

## Farezone

!!! danger
    Handlinger i Farezonen er **irreversible**. Lav en [sikkerhedskopi](#backups) før du fortsætter.

### Slet alle objekter

Fjerner objekter fra familietræet. Klik på **Slet** for at åbne en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder helt træet
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-autoriserer (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremdriftsindikator vises.

!!! warning
    Sletning af kun et subset af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekter.

!!! tip
    Brug dette til at starte forfra, før du importerer et nyt træ, eller til at fjerne specifikke objekttyper, der blev importeret forkert.
