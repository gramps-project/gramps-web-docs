# Importer mediefiler

Hvis du har [importeret et slægtstræ](import.md) og har brug for at uploade de tilsvarende mediefiler, skal du bruge **Importer mediefiler** i Data-sektionen af [Administrationsindstillingerne](settings.md). Det forventer en ZIP-fil, der indeholder de manglende mediefiler. Filer matches til medieobjekter i dit træ på en af to måder:

- **Efter checksum.** For medieobjekter, der har en checksum – som det er tilfældet for træer importeret fra Gramps Desktop – bruges filen med den matchende checksum, uanset dens navn eller mappestruktur i ZIP-filen. Dette virker kun, hvis checksummene i Gramps-databasen er korrekte, hvilket sikres ved at køre kontrol- og reparationsværktøjet.
- **Efter sti.** Medieobjekter uden en checksum – som det typisk er efter en GEDCOM-import – matches efter deres sti: ZIP-filen skal indeholde filen under præcis den relative sti, der er gemt i medieobjektet.

Hvis stierne gemt i din GEDCOM-fil er absolutte (for eksempel `C:\Users\...\photo.jpg`), vil matching efter sti ikke fungere. I dette tilfælde anbefales det først at importere alt til Gramps Desktop, som har flere muligheder for at associere eksisterende mediefiler med et importeret træ, og derefter flytte til Gramps Web som beskrevet i [Kommer fra Gramps Desktop](import.md#coming-from-gramps-desktop).
