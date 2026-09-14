# Importer data

Du kan bringe et eksisterende slægtstræ ind i Gramps Web ved at uploade en fil eksporteret fra et andet slægtsforskningsprogram, fra en online tjeneste eller fra Gramps Desktop.

Importen findes i **Data** sektionen af [Administrationsindstillingerne](settings.md) (brugerikonet i den øverste app-bar ▸ Administration), som er tilgængelig for træejere og administratorer. Mens træet stadig er tomt, fører **Importer Slægtstræ** knappen på "Kom i gang" kortet på startsiden også dertil.

## Hvilken fil skal bruges

| Kommer fra | Eksporter dit træ som | Filendelse |
|---|---|---|
| Et andet slægtsforskningsprogram eller online tjeneste | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Et regneark | Gramps CSV | `.csv` |
| En adressebog | vCard | `.vcf` |

GEDCOM er det almindelige udvekslingsformat, som næsten hvert slægtsforskningsprogram og online tjeneste kan eksportere. Se efter en "Eksporter" eller "Download" mulighed i dit program eller på hjemmesiden, og vælg GEDCOM, hvis du får tilbudt flere formater. Gramps Wiki-siden [Import fra et andet slægtsforskningsprogram](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) har noter om specifikke programmer.

Hvis du bruger Gramps Desktop, vælg Gramps XML (`.gramps`) frem for GEDCOM. Det bærer alle Gramps-data uden tab, og dine online og offline træer bevarer de samme identifikatorer, så de kan [synkroniseres](sync.md). Se [Kommer fra Gramps Desktop](#coming-from-gramps-desktop) nedenfor.

## Importer en slægtstræfil

1. Åbn **Data** sektionen af administrationsindstillingerne.
2. Under "Importer Slægtstræ", vælg din fil og klik på **Importer**.
3. Filen parses først, og en "Bekræft import" dialog viser, hvor mange objekter den indeholder (personer, familier, begivenheder, steder osv.). Der er endnu ikke tilføjet noget til dit træ. Tjek, at tællingerne ser plausible ud, og klik derefter på **Importer** for at fortsætte, eller **Annuller** for at afbryde uden at ændre noget.
4. Importen kører i baggrunden, og en statusindikator vises. Når dataene er importeret, opdateres søgeindekset, hvilket kan tage lidt tid for et stort træ.

Når importen er færdig, skal du tjekke resultatet: sammenlign antallet af personer i **Statistik** panelet på startsiden med antallet i dit gamle program, og åbn en familie, du kender godt, for at se, at forældre, børn, datoer og steder er kommet over som forventet.

!!! warning
    En almindelig import er udelukkende additiv: den opretter altid nye objekter og opdaterer eller sletter aldrig eksisterende, selv for objekter der allerede findes i dit træ under den samme Gramps ID eller håndtag. At importere den samme fil to gange – eller importere en fil, der overlapper med data, der allerede er i træet – vil duplikere hvert matchende objekt i stedet for at sammenflette eller springe det over.

    Hvis du har brug for at bringe ændringer foretaget andre steder ind i et træ, der allerede er importeret, skal du i stedet bruge [Gendan fra backup](settings.md#restore-from-backup), som erstatter træet for at matche den uploadede fil i stedet for at tilføje til det. Dette kræver en Gramps XML-fil.

Hvis der er sat en grænse for antallet af personer for dit træ (se [Brugsgrænser](settings.md#usage-quotas)), vil en import, der ville overskride det, blive afvist som helhed.

## GEDCOM-filer

Både GEDCOM 5.5.1 og GEDCOM 7 filer kan importeres. Der er et par ting, man skal være opmærksom på.

### Tegnkodning

En GEDCOM 5.5.1 fil erklærer sin tegnkodning i sin header. UTF-8, UTF-16, ANSEL og Windows (ANSI) kodninger understøttes. Hvis navne med accenter eller andre specielle tegn ser forvrængede ud efter importen (for eksempel `MÃ¼ller` i stedet for `Müller`), blev filen sandsynligvis eksporteret med en anden kodning end den, den erklærer. Eksporter filen igen fra dit gamle program, og vælg UTF-8, hvis det tilbyder et valg, og [start forfra](#starting-over).

GEDCOM 7 filer skal altid være kodet som UTF-8; andre filer afvises med en "Ugyldig GEDCOM-fil" fejl.

### Program-specifik data

Mange programmer tilføjer deres egne udvidelser til GEDCOM, som andre programmer ikke forstår. Gramps dropper ikke stille sådanne data: linjer, den ikke kan fortolke, samles i en note af typen "GEDCOM import", knyttet til den person, familie eller andet objekt, de tilhører. Gennemgå disse noter for at se, om der er noget vigtigt, der ikke kom med.

### Mediefiler

En GEDCOM-fil indeholder referencer til mediefiler (såsom fotos eller scannede dokumenter), men ikke filerne selv. Efter importen eksisterer medieobjekterne i dit træ, men deres filer mangler, hvilket vises under [Mediefilstatus](settings.md#media-file-status). For at tilføje filerne, se [Importer mediefiler](#import-media-files) nedenfor.

## Kommer fra Gramps Desktop

Hvis du bruger Gramps Desktop, er der to trin til at forberede din database for at sikre, at alt kører glat i det følgende.

1. Tjek og reparer databasen
    - Valgfrit: opret en databasebackup ved at eksportere til Gramps XML
    - Kør [Tjek og reparer databaseværktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Dette retter nogle interne inkonsistenser, der kan føre til problemer i Gramps Web.
2. Konverter mediestier til relative
    - Brug Gramps Media Manager til at [konvertere alle mediestier fra absolutte til relative](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Bemærk, at selv med relative stier, vil eventuelle mediefiler uden for din Gramps mediedirectory ikke fungere korrekt, når de synkroniseres med Gramps Web.

Eksporter derefter dit træ til Gramps XML (`.gramps`), importer det som beskrevet ovenfor, og upload dine mediefiler som beskrevet i næste sektion. For at fortsætte med at arbejde på det samme træ på din computer og på nettet, skal du bruge [Gramps Web Sync-tilføjelsen](sync.md).

### Hvorfor ingen support for Gramps XML-pakke?

Mens Gramps XML (`.gramps`) er det foretrukne format til import af data, understøttes Gramps XML *pakke* (`.gpkg`) ikke af Gramps Web. Dette skyldes, at import- og eksportrutinerne for mediefiler ikke er egnede til brug på en webserver.

## Importer mediefiler

Hvis du har importeret et slægtstræ og har brug for at uploade de tilsvarende mediefiler, skal du bruge **Importer mediefiler** i Data-sektionen af administrationsindstillingerne. Det forventer en ZIP-fil, der indeholder de manglende mediefiler. Filer matches til medieobjekter i dit træ på en af to måder:

- **Efter checksum.** For medieobjekter, der har en checksum – som det er tilfældet for træer importeret fra Gramps Desktop – bruges filen med den matchende checksum, uanset dens navn eller mappestruktur i ZIP-filen. Dette fungerer kun, hvis checksummene i Gramps-databasen er korrekte, hvilket kørsel af tjek og reparer værktøjet sikrer.
- **Efter sti.** Medieobjekter uden en checksum – som det typisk er efter en GEDCOM-import – matches efter deres sti: ZIP-filen skal indeholde filen under præcist den relative sti, der er gemt i medieobjektet.

Hvis de stier, der er gemt i din GEDCOM-fil, er absolutte (for eksempel `C:\Users\...\photo.jpg`), vil matchning efter sti ikke fungere. I dette tilfælde anbefales det først at importere alt til Gramps Desktop, som har flere muligheder for at associere eksisterende mediefiler med et importeret træ, og derefter flytte til Gramps Web som beskrevet i [Kommer fra Gramps Desktop](#coming-from-gramps-desktop).

## Almindelige problemer

**"Uunderstøttet format".** Kun de filendelser, der er angivet [ovenfor](#which-file-to-use), kan importeres. Hvis dit program eller online tjeneste gav dig et ZIP-arkiv, skal du pakke det ud og uploade den `.ged` fil, der er indeni.

**Alt vises to gange.** Den samme fil blev importeret to gange. Da importer aldrig sammenfletter, [start forfra](#starting-over).

**Forvrængede specialtegn.** Se [Tegnkodning](#character-encoding).

**Fotos mangler.** Se [Importer mediefiler](#import-media-files).

### Starte forfra

Hvis en import gik galt, eller du vil rette noget i dit gamle program og importere igen, skal du først tømme træet ved at bruge [Slet alle objekter](settings.md#delete-all-objects) i Farezonen i administrationsindstillingerne, og derefter importere den korrigerede fil. Bemærk, at dette også sletter eventuelle ændringer, du har foretaget i Gramps Web siden importen.
