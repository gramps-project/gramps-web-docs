# Administrationsindstillinger

Siden **Indstillinger > Administration** er tilgængelig via brugerikonet i den øverste app-bar. Den er kun tilgængelig for brugere med ejer- eller administratorrolle og giver værktøjer til at administrere familie trædatabasen.

## Brugskvoter

Øverst på siden vises nuværende brug i forhold til eventuelle konfigurerede grænser:

- **Personer** – antallet af personobjekter i træet versus den konfigurerede maksimale (∞ hvis ubegrænset)
- **Medieopbevaring** – den samlede størrelse af uploadede mediefiler versus den konfigurerede opbevaringskvote (∞ hvis ubegrænset)

Kvoterne sættes af serveradministratoren; se [Serverkonfiguration](../install_setup/configuration.md) for detaljer.

## Importer data

Importsektionen giver dig mulighed for at uploade en familie træfil eller et mediearkiv. Se [Importer data](import.md) for fulde instruktioner.

## Mediefilstatus

Denne sektion viser:

- Det samlede antal medieobjekter i træet og om nogen mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler fra serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data blev importeret fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades via importmediearkivfunktionen.

## Importer mediearkiv

Giver mulighed for at uploade en ZIP-fil med mediefiler for at udfylde manglende filer. Se [Importer data](import.md) for fulde instruktioner.

## Administrer søgeindeks

Gramps Web opretholder et fuldtekst søgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der aktuelt er indekseret i forhold til det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En fremdriftsindikator vises, mens opgaven kører i baggrunden. Dette er normalt kun nødvendigt efter en serveropgradering.

### Semantisk søgeindeks

Hvis serveren har [semantisk (AI-drevet) søgning aktiveret](../install_setup/configuration.md), vises en yderligere sektion med to handlinger:

- **Regenerer semantisk søgeindeks** – genopbygger hele det semantiske indeks fra bunden. Dette er beregningsmæssigt dyrt og kan tage lang tid.
- **Opdater semantisk søgeindeks** – udfører en inkrementel opdatering, der kun tilføjer objekter, der endnu ikke er indekseret. Hurtigere end en fuld genopbygning.

## Familie trænavn

!!! note
    Omdøbning af træet fungerer kun i en [multi-træ opsætning](../install_setup/multi-tree.md) eller når `TREE_ID` er eksplicit indstillet i [serverkonfigurationen](../install_setup/configuration.md). På en standard installation med et enkelt træ uden `TREE_ID` indstillet, vil dette give en fejl.

Dette giver mulighed for at ændre navnet på den underliggende Gramps familie trædatabase. Indtast et nyt navn og klik på **Omdøb** for at anvende.

## Tjek og reparation af database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med [Tjek og reparation af databaseværktøjet](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og reparation** og vent på, at fremdriftsindikatoren er færdig. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

## Farezone

!!! danger
    Handlinger i farezonen er **irreversible**. Lav en sikkerhedskopi, før du fortsætter.

### Slet alle objekter

Fjerner objekter fra familie træet. Klik på **Slet** for at åbne en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder træet helt
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-autoriseres (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremdriftsindikator vises.

!!! warning
    Sletning af kun et delmængde af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekter.

!!! tip
    Brug dette til at starte forfra, før du importerer et nyt træ, eller til at fjerne specifikke objekttyper, der blev importeret forkert.
