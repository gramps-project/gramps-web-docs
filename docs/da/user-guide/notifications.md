# Notifikationer

**Notifikationer** er et sidepanel-element med et klokkeikon. Når der er opstået fejl, eller baggrundsopgaver kører, viser et badge antallet af ulæste notifikationer. Klik på det for at åbne notifikationsloggen.

Notifikationsloggen tjener to formål:

- Det er en optegnelse over fejl, der opstod under din session – mislykkede API-anmodninger, fejl i baggrundsopgaver, gemmefejl eller browserfejl.
- Det sporer fremskridtene for langvarige baggrundsopgaver – såsom import og eksport, generering af rapporter, OCR-tekstgenkendelse, databaseopgraderinger og genopbygning af søge/semantisk indeks – og viser deres tilstand (f.eks. ventende, startet, i gang) og underretter dig, når de er færdige eller fejler.

Hver post viser en kort besked, kilden (Netværk, Opgave, Gem, eller Browser) og et tidsstempel.

Nogle notifikationer inkluderer strukturerede detaljer. Klik på en sådan post for at åbne en dialog med en opdeling af fejldataene og en **Kopier JSON**-knap. Dette er nyttigt, når du rapporterer en fejl, da JSON'en indeholder de præcise fejloplysninger fra serveren.

Brug **Ryd Alle** for at afvise alle notifikationer.

!!! note
    Notifikationer gemmes kun i hukommelsen og ryddes, når du genindlæser siden.
