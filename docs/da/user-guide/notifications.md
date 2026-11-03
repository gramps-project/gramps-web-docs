# Notifikationer

**Notifikationer** er et sidepanel element med et klokkeikon. Når der er opstået fejl, eller baggrundsopgaver kører, viser et badge antallet af ulæste notifikationer. Klik på det for at åbne notifikationsloggen.

Notifikationsloggen tjener to formål:

- Det er en optegnelse over fejl, der opstod under din session – mislykkede API-anmodninger, fejl i baggrundsopgaver, gemmefejl eller browser-niveau fejl.
- Det sporer fremskridtene for langvarige baggrundsopgaver – såsom importer og eksporter, generering af rapporter, OCR-tekstgenkendelse, databaseopgraderinger, sletning af mange objekter og genopbygning af søgeindekser – viser deres tilstand (f.eks. ventende, startet, i gang) og underretter dig, når de er færdige eller fejler.

Hver post viser en kort besked, kilden (Netværk, Opgave, Gem, eller Browser), og et tidsstempel. Færdige opgaver læser "Opgave fuldført" eller "Opgave fejlet".

Nogle notifikationer inkluderer strukturerede detaljer, såsom fejlmeddelelsen fra en mislykket opgave. Klik på en sådan post åbner en dialog med en opdeling af fejldataene og en **Kopier JSON** knap. Dette er nyttigt, når du rapporterer en fejl, da JSON'en indeholder de nøjagtige fejloplysninger fra serveren.

Brug **Ryd alle** for at afvise alle notifikationer.

Opgaver, der ændrer hele træet, såsom en import, en gendannelse, sletning af alle objekter eller genopbygning af søgeindekset, kan ikke køre samtidig. Hvis du starter en, mens en anden kører, vises en meddelelse om, at en anden opgave allerede kører på dette træ, og den kørende opgave vises med sin fremdrift.

!!! note
    Notifikationer gemmes kun i hukommelsen og ryddes, når du genindlæser siden.
