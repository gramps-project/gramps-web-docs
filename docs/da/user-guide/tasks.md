# Brug den indbyggede opgavestyring

Gramps Web indeholder et indbygget genealogisk opgavestyringsværktøj. Det er beregnet til at gøre det muligt for forskere at planlægge og prioritere, men også dokumentere deres opgaver. Derfor repræsenteres opgaver som kilder i Gramps-databasen. Efter afslutningen af en opgave kan det tilknyttede indhold fungere som en kilde, der dokumenterer forskningsprocessen.

## Opgavegrundlæggende

Opgaver har følgende egenskaber:

- Status. Dette kan være "Åben", "I gang", "Blokeret" eller "Udført"
- Prioritet. Dette kan være "Lav", "Medium" eller "Høj"
- Tags. Etiketterne er normale Gramps-tags for den underliggende kilde. (Bemærk, at alle opgaver desuden har `ToDo`-etiketten for at identificere dem som opgaver, men denne etiket er skjult i opgavelisten for at undgå rod.)
- Titel. Vist i opgavelisten
- Beskrivelse. Et felt med rig tekst, der kan bruges til at beskrive problemstillingen, men også dokumentere eventuelle fremskridt
- Medier. Eventuelle mediefiler knyttet til opgaven

## Opret en opgave

Da opgaver er normale Gramps-objekter, kan de redigeres eller oprettes af den samme gruppe brugere, der kan redigere eller oprette andre objekter (som personer eller begivenheder).

For at oprette en opgave skal du klikke på + knappen på opgaveliste-siden. Indtast mindst en titel, og valgfrit en prioritet, en beskrivelse, vedhæftninger og tags. Status vil altid være "Åben" ved oprettelse.

## Opgavelisten

Opgavelisten er sorteret efter status – udførte opgaver sidst – og inden for hver status efter prioritet, højeste først.

Klik på en opgave for at åbne den. Brugere med redigeringsrettigheder kan også klikke på statusikonet for en opgave for at ændre dens status direkte i listen, for eksempel for at markere den som udført.

Knappen **filter** ovenfor listen filtrerer opgaverne efter tag, med et [GOQL](goql.md) udtryk, eller med det [avancerede filter](lists.md#advanced-filter).

## Rediger en opgave

Opgave-siden har ikke en separat "redigeringsmode" som andre Gramps-objekter:

- Klik på titlen for at redigere den. Tryk på Enter, klik ✓, eller klik et andet sted for at gemme; tryk på Escape eller klik ✕ for at annullere.
- Ændringer til status og prioritet anvendes straks.
- For at redigere beskrivelsen eller vedhæftningerne skal du klikke på redigeringsknappen ved siden af overskriften for sektionen. Beskrivelsen gemmes med "gem" knappen under den; redigering af vedhæftninger afsluttes med **Udført**.
- Låseknappen angiver, om opgaven er privat. Opgavens beskrivelse får samme privatliv.

Brugere uden redigeringsrettigheder ser status og prioritet som tekst, og sektioner uden indhold er skjult.

Under titlen ser redaktører to yderligere knapper: **Rediger kilde** åbner den kilde, der repræsenterer opgaven, hvor dens andre noter, citater og attributter kan redigeres. **Slet** sletter opgaven efter en bekræftelse og vender tilbage til opgavelisten; den besked, der vises, har en fortrydelsesknap til at gendanne opgaven.

## Masseændring af opgaveegenskaber

Brugere med redigeringsrettigheder ser en afkrydsningsfelt på hver række i opgavelisten. Vælg opgaver og brug **Indstil prioritet** eller **Indstil status** ovenfor listen for at ændre alle valgte opgaver på én gang.

## Opgaver i Gramps Desktop

Når du tilføjer opgaver via Gramps Web, vil både kilderne og noterne have `ToDo`-etiketten knyttet til dem, så opgaverne vil vises i desktop [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) samt i [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

For at tilføje eller redigere en opgave i Gramps Desktop skal du følge følgende retningslinjer

- Tilføj en kilde med tag `ToDo` og opgavens titel som titel
- Valgfrit, tilføj en note til kilden med tag `ToDo`, skriv "To Do", og beskrivelsen som tekst
- Tilføj en attribut "Status" og indstil den til "Åben", "I gang", "Blokeret" eller "Udført"
- Tilføj en attribut "Prioritet" og indstil den til 9 for lav, 5 for medium eller 1 for høj (disse modstridende værdier er taget fra iCalendar-specifikationen)
