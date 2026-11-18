# Notifikationer

Klokken i den øverste app-bar åbner notifikationerne. Et badge på klokken viser antallet af ulæste notifikationer. Menuen viser kørende opgaver og de seneste notifikationer; **Vis alle** åbner den fulde notifikationslog. På små skærme åbner klokken loggen direkte.

Notifikationer handler om:

- **Ændringer fra andre brugere.** Når andre brugere ændrer træet, mens du bruger Gramps Web, siger en notifikation, hvem der ændrede hvad, f.eks. "Rediger person" eller "12 ændringer". Klik på den for at åbne ændringen i [revisionshistorikken](revisions.md). Ændringer, der ikke har en Gramps Web-bruger, såsom ændringer foretaget direkte i en delt database med Gramps Desktop, vises uden et navn. Dette er kun tilgængeligt for brugere, der kan se revisionshistorikken (medlemmer og derover).
- **Baggrundsopgaver** – såsom import og eksport, generering af rapporter, OCR-tekstgenkendelse, databaseopgraderinger, sletning eller redigering af mange objekter og genopbygning af søgeindekser – viser deres status (f.eks. ventende, startet, i gang) og underretter dig, når de er afsluttet eller fejler.
- **Fejl** der opstod under din session – mislykkede API-anmodninger, fejl i baggrundsopgaver, gemmefejl eller fejl på browserniveau.

Færdige eksporter og mediearkiver kan downloades fra deres notifikation, også efter du har forladt [Eksport siden](../administration/export.md).

Nogle notifikationer inkluderer strukturerede detaljer, såsom fejlmeddelelsen fra en mislykket opgave. Klikker du på en sådan post i notifikationsloggen, åbner der sig en dialog med en opdeling af fejldataene og en **Kopier JSON**-knap. Dette er nyttigt, når du rapporterer en fejl, da JSON'en indeholder de præcise fejloplysninger fra serveren.

Brug **Ryd alle** i notifikationsloggen for at afvise alle notifikationer.

Opgaver, der ændrer hele træet, såsom en import, en gendannelse, sletning af alle objekter eller genopbygning af søgeindekset, kan ikke køre samtidig. Hvis du starter en, mens en anden kører, siger en besked, at en anden opgave allerede kører på dette træ, og den kørende opgave vises med sin fremdrift.

!!! note
    Notifikationer gemmes kun i hukommelsen og ryddes, når du genindlæser siden. Gramps Web tjekker for ændringer fra andre brugere kun, mens det er åbent, så ændringer foretaget, mens du var væk, rapporteres ikke; se [Revisionshistorik](revisions.md) for dem.
