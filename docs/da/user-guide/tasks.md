# Brug den indbyggede opgavestyring

Gramps Web indeholder et indbygget genealogisk opgavestyringsværktøj. Det er designet til at gøre det muligt for forskere at planlægge og prioritere, men også dokumentere deres opgaver. Derfor repræsenteres opgaver som kilder i Gramps-databasen. Efter afslutningen af en opgave kan det tilknyttede indhold fungere som en kilde, der dokumenterer forskningsprocessen.

## Opgavegrundlæggende

Opgaver har følgende egenskaber:

- Status. Dette kan være "Åben", "I gang", "Blokeret" eller "Udført"
- Prioritet. Dette kan være "Lav", "Mellem" eller "Høj"
- Tags. Etiketterne er normale Gramps-tags for den underliggende kilde. (Bemærk, at alle opgaver desuden har etiketten `ToDo` for at identificere dem som opgaver, men denne etiket er skjult i opgavelisten for at undgå rod.)
- Titel. Vist i opgavelisten
- Beskrivelse. Et rigt tekstfelt, der kan bruges til at beskrive problemstillingen, men også dokumentere eventuelle fremskridt
- Medier. Enhver mediefil knyttet til opgaven

## Opret en opgave

Da opgaver er normale Gramps-objekter, kan de redigeres eller oprettes af den samme gruppe brugere, der kan redigere eller oprette andre objekter (som personer eller begivenheder).

For at oprette en opgave skal du klikke på + knappen på opgaveliste-siden. Indtast mindst en titel. Status vil altid være "Åben" ved oprettelse.

## Rediger en opgave

For at redigere en af opgavens detaljer skal du klikke på den i opgavelisten.

Opgavedetaljesiden har ikke en separat "redigeringsmode" som andre Gramps-objekter. Ændringer til titlen, status og prioritet anvendes straks. Ændringer til den rige tekstbeskrivelse kræver, at du klikker på "gem" knappen under den.

## Bulkændring af opgaveegenskaber

Prioriteten og status for opgaver kan ændres i bulk ved at bruge afkrydsningsfelterne i opgavelisten til at vælge og de passende knapper over opgavelisten.

## Opgaver i Gramps Desktop

Når du tilføjer opgaver via Gramps Web, vil både kilderne og noterne have etiketten `ToDo` knyttet til dem, så opgaverne vil vises i desktop [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) samt i [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

For at tilføje eller redigere en opgave i Gramps Desktop, brug følgende retningslinjer:

- Tilføj en kilde med etiketten `ToDo` og opgavens titel som titel
- Valgfrit, tilføj en note til kilden med etiketten `ToDo`, skriv "To Do", og beskrivelsen som tekst
- Tilføj en attribut "Status" og indstil den til "Åben", "I gang", "Blokeret" eller "Udført"
- Tilføj en attribut "Prioritet" og indstil den til 9 for lav, 5 for mellem, eller 1 for høj (disse modintuitive værdier er taget fra iCalendar-specifikationen)
