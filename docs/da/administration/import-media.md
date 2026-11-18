# Importer mediefiler

Hvis du har [importeret et slægtstræ](import.md) og har brug for at uploade de tilsvarende mediefiler, skal du bruge **Importer mediefiler** på [Import-siden](import.md), under importen af slægtstræet. Det forventer en ZIP-fil, der indeholder de manglende mediefiler. Uploaden er kun mulig, når træet indeholder medieobjekter, da filerne matches til eksisterende medieobjekter – en slægtstræfil refererer kun til sine mediefiler, så importer det først.

Filer matches til medieobjekter i dit træ på en af to måder:

- **Efter checksum.** For medieobjekter, der har en checksum – som det er tilfældet for træer importeret fra Gramps Desktop – bruges filen med den matchende checksum, uanset dens navn eller mappestruktur i ZIP-filen. Dette fungerer kun, hvis checksummene i Gramps-databasen er korrekte, hvilket sikres ved at køre kontrol- og reparationsværktøjet.
- **Efter sti eller filnavn.** Medieobjekter uden en checksum – som det typisk er efter en GEDCOM-import – matches efter den relative sti, der er gemt i medieobjektet. Hvis ingen fil i ZIP'en har den sti, matches de kun efter filnavn, idet store og små bogstaver ignoreres (siden Gramps Web API 3.26). Dette fungerer også for absolutte stier fra andre programmer, såsom `C:\Users\...\Family\grandpa.jpg`, så du kan simpelthen lægge alle filer i ZIP-filen. Et filnavn bruges kun, hvis det er unikt, både i ZIP-filen og blandt de medieobjekter, der stadig ikke har en fil.

Efter uploaden angiver resultatet, hvor mange medieobjekter der blev fundet en fil til, og lister dem, for hvilke ZIP-filen ikke havde en fil, med deres Gramps ID og gemt sti. Brug denne liste til at finde de manglende filer, og upload derefter en anden ZIP-fil med kun disse – filer, der allerede er på serveren, påvirkes ikke.

Hvis flere medieobjekter har det samme filnavn i forskellige mapper, fungerer matching efter filnavn ikke for dem. Enten genskaber du mappestrukturen fra de gemte stier i ZIP-filen, eller importerer alt til Gramps Desktop først, som har flere muligheder for at associere eksisterende mediefiler med et importeret træ, og derefter flytter til Gramps Web som beskrevet i [Kommer fra Gramps Desktop](import.md#coming-from-gramps-desktop).

## Mediefilstatus

**Data**-sektionen i [Administrationsindstillingerne](settings.md) viser:

- Det samlede antal medieobjekter i træet og om nogen mangler en checksum
- Antallet af medieobjekter, hvis tilknyttede fil mangler fra serveren

Et grønt flueben indikerer, at alt er i orden. Hvis der opdages problemer, vises links til de berørte objekter. Manglende checksums opstår typisk, når data blev importeret fra et format som GEDCOM, der inkluderer mediereferencer, men ikke de faktiske filer. De manglende filer kan uploades som beskrevet ovenfor.
