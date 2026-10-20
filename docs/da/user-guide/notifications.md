# Notifikationer

**Notifikationer** er et sidepanel-element med et klokkeikon. Når der er opstået fejl, eller baggrundsopgaver kører, viser et badge antallet af ulæste notifikationer. Klik på det for at åbne notifikationsloggen.

Notifikationsloggen tjener to formål:

- Det er en optegnelse over fejl, der opstod under din session – mislykkede API-anmodninger, fejl i baggrundsopgaver, fejl ved gemning eller fejl på browserniveau.
- Den sporer fremskridtene for langvarige baggrundsopgaver – såsom import og eksport, generering af rapporter, OCR-tekstgenkendelse, databaseopgraderinger og genopbygning af søge-/semantiske indekser – og viser deres tilstand (f.eks. ventende, startet, i gang) og underretter dig, når de er færdige eller mislykkes.

Hver post viser en kort besked, kilden (Netværk, Opgave, Gem, eller Browser) og et tidsstempel. Færdige opgaver læser "Opgave fuldført" eller "Opgave mislykkedes".

Nogle notifikationer inkluderer strukturerede detaljer, såsom fejlmeddelelsen fra en mislykket opgave. Klik på en sådan post for at åbne en dialog med en opdeling af fejldataene og en **Kopier JSON**-knap. Dette er nyttigt, når du rapporterer en fejl, da JSON'en indeholder de nøjagtige fejloplysninger fra serveren.

Brug **Ryd alle** for at afvise alle notifikationer.

Opgaver, der ændrer hele træet, såsom en import, en gendannelse, sletning af alle objekter eller genopbygning af søgeindekset, kan ikke køre samtidig. Hvis du starter en, mens en anden kører, vises en besked om, at en anden opgave allerede kører på dette træ, og den kørende opgave vises med sin fremdrift.

!!! note
    Notifikationer gemmes kun i hukommelsen og ryddes, når du genindlæser siden.
