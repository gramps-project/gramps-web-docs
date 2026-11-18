# Importer data

Du kan bringe et eksisterende slægtstræ ind i Gramps Web ved at uploade en fil eksporteret fra et andet slægtsforskningsprogram, fra en online tjeneste eller fra Gramps Desktop.

Import har sin egen side, som er tilgængelig for træejere og administratorer. Åbn den med **Importer slægtstræ** i **Data** sektionen af [Administrationsindstillinger](settings.md) (brugerikonet i den øverste app-bar ▸ Administration). Mens træet stadig er tomt, fører **Importer slægtstræ** knappen på "Kom i gang" kortet på startsiden, i slægtsræet og i listerne også dertil.

## Hvilken fil skal bruges

| Kommer fra | Eksporter dit træ som | Filendelse |
|---|---|---|
| Et andet slægtsforskningsprogram eller online tjeneste | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Et regneark | Gramps CSV | `.csv` |
| Et adressekartotek | vCard | `.vcf` |

GEDCOM er det almindelige udvekslingsformat, som næsten hvert slægtsforskningsprogram og online tjeneste kan eksportere. Se efter en "Eksporter" eller "Download" mulighed i dit program eller på hjemmesiden, og vælg GEDCOM, hvis du får tilbudt flere formater. Gramps Wiki-siden [Import fra et andet slægtsforskningsprogram](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) har noter om specifikke programmer.

Hvis du bruger Gramps Desktop, skal du vælge Gramps XML (`.gramps`) i stedet for GEDCOM. Det bærer alle Gramps-data uden tab, og dine online og offline træer beholder de samme identifikatorer, så de kan blive [synkroniseret](sync.md). Se [Kommer fra Gramps Desktop](#coming-from-gramps-desktop) nedenfor.

## Importer en slægtstræfil

1. Åbn import-siden som beskrevet ovenfor.
2. Under "Importer slægtstræ", vælg din fil og klik på **Importer**. Upload-fremskridtet vises.
3. Filen læses først, og en "Bekræft import" dialog viser, hvor mange objekter den indeholder (personer, familier, begivenheder, steder osv.), samt importørens [rapport](#the-import-report), hvis den har en. Der er endnu ikke tilføjet noget til dit træ. Tjek, at tællingerne ser plausible ud, og klik derefter på **Importer** for at fortsætte, eller **Annuller** for at afbryde uden at ændre noget. Hvis dit træ allerede indeholder personer, advarer dialogen om, at import af de samme data igen skaber dubletter.
4. Importen kører i baggrunden, og en fremskridtsindikator vises. Når dataene er importeret, opdateres søgeindekset, hvilket kan tage lidt tid for et stort træ. Hvis importen mislykkes, vises årsagen.
5. Hvis træet endnu ikke har en hjemmeperson, bliver du tilbudt at vælge en.

Når importen er færdig, skal du tjekke resultatet: sammenlign antallet af personer i **Statistik** panelet på startsiden med antallet i dit gamle program, og åbn en familie, du kender godt, for at se, at forældre, børn, datoer og steder er kommet over som forventet. Hvis filen henviser til fotos eller andre mediefiler, skal du tilføje dem næste gang under [Importer mediefiler](import-media.md) på samme side.

!!! warning
    En almindelig import er udelukkende additiv: den opretter altid nye objekter og opdaterer eller sletter aldrig eksisterende, selv for objekter der allerede findes i dit træ under den samme Gramps ID eller håndtag. Import af den samme fil to gange – eller import af en fil, der overlapper med data, der allerede er i træet – vil duplikere hvert matchende objekt i stedet for at fusionere eller springe det over.

    Hvis du har brug for at bringe ændringer foretaget andre steder ind i et træ, der allerede er importeret, skal du i stedet bruge [Gendan fra backup](backups.md#restore-from-backup), som erstatter træet for at matche den uploadede fil i stedet for at tilføje til det. Dette kræver en Gramps XML-fil eller en Gramps Web-backup.

## Importrapporten

Importører rapporterer, hvad de ikke kunne importere fuldstændigt, for eksempel GEDCOM-linjer, de ikke forstod, referencer til poster, der mangler fra filen, eller et forældet filformat. Rapporten vises under **Rapport**, både i bekræftelsesdialogen og efter importen. Læs den, før du bekræfter: den forklarer ofte problemer, som du ellers kun ville bemærke senere i træet.

Ikke hver besked er et problem – mange GEDCOM-filer indeholder program-specifikke data, der rapporteres, men beholdes, se [Program-specifikke data](#program-specific-data). Brug knapperne ved siden af rapporten til at kopiere den eller downloade den som en tekstfil, for eksempel for at bede om hjælp i [forumet](../help/help.md).

## Brugsgrænser

Serveradministratoren kan sætte grænser for dit træ (se [Serverkonfiguration](../install_setup/configuration.md)). Toppen af **Data** sektionen viser den aktuelle brug i forhold til disse grænser:

- **Personer** – antallet af personobjekter i træet versus den konfigurerede maksimum (∞ hvis ubegrænset)
- **Medieopbevaring** – den samlede størrelse af uploadede mediefiler versus den konfigurerede opbevaringskvote (∞ hvis ubegrænset)

En import, der ville overskride grænsen for antallet af personer, nægtes som helhed.

## GEDCOM-filer

Både GEDCOM 5.5.1 og GEDCOM 7 filer kan importeres. Der er et par ting, du skal være opmærksom på.

### Tegnkodning

En GEDCOM 5.5.1 fil erklærer sin tegnkodning i sin header. UTF-8, UTF-16, ANSEL og Windows (ANSI) kodninger understøttes. Hvis navne med accenter eller andre specialtegn ser forvrængede ud efter importen (for eksempel `MÃ¼ller` i stedet for `Müller`), blev filen sandsynligvis eksporteret med en anden kodning end den, den erklærer. Eksporter filen igen fra dit gamle program, vælg UTF-8, hvis det tilbyder et valg, og [start forfra](#starting-over).

GEDCOM 7 filer skal altid være kodet som UTF-8; andre filer afvises med en "Ugyldig GEDCOM-fil" fejl.

### Program-specifikke data

Mange programmer tilføjer deres egne udvidelser til GEDCOM, som andre programmer ikke forstår. Gramps dropper ikke stille sådanne data: linjer, den ikke kan fortolke, samles i en note af typen "GEDCOM import", knyttet til den person, familie eller andet objekt, de tilhører. Gennemgå disse noter for at se, om der er noget vigtigt, der ikke kom over.

### Mediefiler

En GEDCOM-fil indeholder referencer til mediefiler (såsom fotos eller scannede dokumenter), men ikke filerne selv. Efter importen eksisterer medieobjekterne i dit træ, men deres filer mangler, hvilket vises under [Mediefilstatus](import-media.md#media-file-status). For at tilføje filerne, se [Importer mediefiler](import-media.md).

## Kommer fra Gramps Desktop

Hvis du bruger Gramps Desktop, er der to trin til at forberede din database for at sikre, at alt kører glat i det følgende.

1. Tjek og reparer databasen
    - Valgfrit: opret en databasebackup ved at eksportere til Gramps XML
    - Kør [Tjek og reparer databaseværktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Dette retter nogle interne uoverensstemmelser, der kan føre til problemer i Gramps Web.
2. Konverter mediestier til relative
    - Brug Gramps Mediemanager til [at konvertere alle mediestier fra absolutte til relative](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Bemærk, at selv med relative stier vil mediefiler uden for dit Gramps mediedirektorium ikke fungere korrekt, når de synkroniseres med Gramps Web.

Eksporter derefter dit træ til Gramps XML (`.gramps`), importer det som beskrevet ovenfor, og [upload dine mediefiler](import-media.md). For at fortsætte med at arbejde på det samme træ på din computer og på nettet, brug [Gramps Web Sync-tilføjelsen](sync.md).

### Hvorfor ingen support til Gramps XML-pakke?

Mens Gramps XML (`.gramps`) er det foretrukne format til import af data, understøttes Gramps XML *pakke* (`.gpkg`) ikke af Gramps Web. Dette skyldes, at import- og eksportrutinerne for mediefiler ikke er egnede til brug på en webserver.

## Almindelige problemer

**"Ikke-understøttet format".** Kun de filendelser, der er angivet [ovenfor](#which-file-to-use), kan importeres. Hvis dit program eller online tjeneste gav dig et ZIP-arkiv, skal du pakke det ud og uploade `.ged` filen indeni.

**Alt vises to gange.** Den samme fil blev importeret to gange. Da importer aldrig fusionerer, [start forfra](#starting-over).

**Forvrængede specialtegn.** Se [Tegnkodning](#character-encoding).

**Fotos mangler.** Se [Importer mediefiler](import-media.md).

### Starte forfra

Hvis en import gik galt, eller du vil rette noget i dit gamle program og importere igen, skal du først tømme træet ved at bruge [Slet alle objekter](#delete-all-objects), og derefter importere den korrigerede fil. Bemærk, at dette også sletter eventuelle ændringer, du har foretaget i Gramps Web siden importen.

### Slet alle objekter

!!! danger
    Sletning af objekter er **irreversibel**. Lav en [backup](backups.md) før du fortsætter.

**Slet alle objekter** findes i **Farezone** sektionen af [Administrationsindstillinger](settings.md). Klik på **Slet** åbner en dialog, hvor du kan vælge at slette:

- **Alle objekter** – rydder helt træet
- **Specifikke objekttyper** – for eksempel kun begivenheder eller kun medieobjekter

Du vil blive bedt om at re-autentificere (logge ind igen) for at bekræfte handlingen. Sletningen kører som en baggrundsopgave, og en fremskridtsindikator vises.

!!! warning
    Sletning af kun et delmængde af objekttyper (i stedet for alle objekter på én gang) kan tage meget lang tid for store træer, da serveren skal kontrollere og opdatere alle relationer mellem objekterne.
