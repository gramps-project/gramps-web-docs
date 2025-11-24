## Forbered din Gramps-database

Hvis du bruger Gramps Desktop, er der to trin til at forberede din database for at sikre, at alt kører glat i det følgende. Hvis du migrerer fra et andet slægtsforskningsprogram, kan du springe dette trin over.

1. Tjek og reparer databasen
    - Valgfrit: opret en databasebackup ved at eksportere til Gramps XML
    - Kør [Tjek og reparer databaseværktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Dette retter nogle interne inkonsistenser, der kan føre til problemer i Gramps Web.
2. Konverter mediestier til relative
    - Brug Gramps Media Manager til at [konvertere alle mediestier fra absolutte til relative](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Bemærk, at selv med relative stier vil mediefiler uden for din Gramps mediemappe ikke fungere korrekt, når de synkroniseres med Gramps Web.

## Importer slægtsdata

For at importere et eksisterende slægtstræ, brug "Import" siden og upload en fil i et af de filformater, der understøttes af Gramps &ndash; se [Import fra et andet slægtsforskningsprogram](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) i Gramps Wiki.

Hvis du allerede bruger Gramps Desktop, anbefales det stærkt at bruge Gramps XML (`.gramps`) formatet for at sikre, at dine online og offline træer bruger de samme identifikatorer og kan [synkroniseres](sync.md).

## Hvorfor ingen support for Gramps XML-pakke?

Mens Gramps XML (`.gramps`) er det foretrukne format til import af data, understøttes Gramps XML *pakke* (`.gpkg`) ikke af Gramps Web. Dette skyldes, at import- og eksportrutinerne for mediefiler ikke er velegnede til brug på en webserver.

For at importere mediefilerne, der tilhører en importeret `.gramps` fil, se næste sektion.

## Importer mediefiler

Hvis du har uploadet et slægtstræ og har brug for at uploade de tilsvarende mediefiler, kan du bruge knappen "importer mediearkiv" på "Import" siden.

Det forventer en ZIP-fil med de manglende mediefiler indeni. Mappestrukturen i ZIP-filen behøver ikke at være den samme som mappestrukturen inde i Gramps mediemappe, da filerne matches til medieobjekter ved deres checksum.

Bemærk, at denne funktion kun fungerer for filer, der har den korrekte checksum i Gramps-databasen (hvilket bør sikres ved at køre tjek og reparer værktøjet i det første trin).

Når du flytter til Gramps Web fra et andet slægtsforskningsprogram, der inkluderer mediefiler, anbefales det først at importere alt til Gramps Desktop, som har flere muligheder for at associere eksisterende mediefiler med et importeret træ.
