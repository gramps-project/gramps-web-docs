# Lister

Hver objekttype i Gramps Web har en listevisning: Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter og Medier. De fungerer alle på samme måde og deler de samme værktøjer til sortering, filtrering og redigering i bulk.

## Sortering og paging

Klik på en kolonneoverskrift for at sortere efter den kolonne; klik på den igen for at omvende rækkefølgen. Sortering udføres af serveren, så den gælder for hele listen, ikke kun den side, du ser på.

Lange lister opdeles i sider. Brug pagineringskontrollerne nederst for at bevæge dig mellem dem.

På smalle skærme skifter tabellen automatisk til et kompakt layout, så listevisninger forbliver brugbare på en telefon.

## Vælge kolonner

Klik på tandhjulsikonet over listen for at åbne **Kolonner** dialogen. Sæt eller fjern markeringen i en kolonne for at vise eller skjule den. **Nulstil** gendanner standardvalget for den liste.

Mindst én kolonne skal forblive synlig, så den sidste tilbageværende kolonne kan ikke få fjernet markeringen.

Dit kolonnevalg huskes pr. objekttype og pr. slægtstræ. Det gemmes i din browser, så det ikke er synligt for andre brugere – men det følger heller ikke med til en anden browser eller enhed.

## Filtrering

Klik på **filter** knappen for at åbne filterpanelet. Det tilbyder tre måder at filtrere på, som kan kombineres:

- **Færdiglavede filtre** i sammenklappelige sektioner, der afhænger af objekttypen. For personer kan du for eksempel filtrere efter fødselsår, dødsår, forskellige personegenskaber, antallet af tilknytninger, tags og om et objekt er privat eller offentligt.
- **Avanceret filter** – en betingelsesbygger til filtre, som de færdiglavede ikke kan udtrykke, beskrevet [nedenfor](#avanceret-filter).
- **GQL** – et tekstfelt til en forespørgsel i [Gramps Query Language](gql.md). Skriv forespørgslen og tryk på Enter eller klik på **Anvend**. Hvis forespørgslen er ugyldig, bliver feltets ramme rød. En forespørgsel gælder oven på de andre filtre.

Aktive filtre vises som chips over listen. Fjern et enkelt filter ved at klikke på chipens ryd-knap, eller brug **Ryd alle filtre** for at fjerne dem alle på én gang.

### Avanceret filter

Klik på **Avanceret filter** nederst i filterpanelet for at åbne betingelsesbyggeren. Dens betingelser er de filterregler, der er kendt fra Gramps Desktop, såsom "Personer med &lt;navn&gt;" eller "Forfædre til &lt;person&gt;".

- Klik på **Tilføj betingelse** for at vælge en regel. Reglerne er grupperet i kategorier og kan søges efter navn eller beskrivelse.
- Udfyld reglens parametre. Hver parameter har et matchende input, for eksempel et datofelt, en tagvælger eller en objektvælger for en person eller et sted.
- Vælg, hvordan betingelserne i en gruppe kombineres: **Alle betingelser**, **Enhver betingelse**, eller – via menuen ved siden af dem – **Præcis én betingelse**.
- Klik på **Tilføj gruppe** for at tilføje en gruppe betingelser inden i en anden gruppe, med sin egen måde at kombinere dem på.
- Vælg **Ikke** på en betingelse eller gruppe for at invert den.

Klik på **Anvend** for at filtrere listen.

De færdiglavede filtre, der er aktive, når du åbner byggeren, vises der som betingelser. Hvis det filter, du bygger, kan udtrykkes med de færdiglavede filtre, vises det sammen med dem efter anvendelse. Ellers vises det som en enkelt **Avanceret filter** chip, og filterpanelet tilbyder en **Rediger** knap for at genåbne byggeren.

!!! note
    Regler, der henviser til brugerdefinerede filtre gemt i Gramps Desktop, er ikke tilgængelige i byggeren. Reglerne vises på dit sprog med Gramps Web API 3.24 eller nyere.

## Vælge objekter og handle på dem i bulk

Brugere med redigeringsrettigheder ser en **Vælg** knap ved siden af filterknappen. Klik på den for at gå ind i udvælgelsestilstand, som tilføjer en afkrydsningsfelt til hver række.

Sæt kryds ved de objekter, du ønsker, og en værktøjslinje vises, der viser, hvor mange der er valgt, sammen med en **Handling** dropdown og en **Anvend** knap.

### Slet

Vælg et eller flere objekter, vælg **Slet**, og klik på **Anvend**. En bekræftelsesdialog beder dig om at bekræfte, og advarer om, at handlingen ikke kan fortrydes.

!!! tip
    Sletninger registreres i [revisionshistorikken](revisions.md) ligesom enhver anden ændring, så en fejlagtig bulk-sletning kan fortrydes ved at fortryde den tilsvarende transaktion.

### Sammenlæg

Vælg **præcist to** objekter, vælg **Sammenlæg**, og klik på **Anvend**. En dialog beder om at vælge, hvilket af de to der skal give de primære data til det sammenlagte objekt; klik på det, du ønsker at beholde som primært. Det andet objekts data sammenlægges i det, og referencer opdateres.

Sammenlægning er tilgængelig for personer, familier, begivenheder, steder, kilder og citeringer. Det er ikke tilgængeligt for arkiver, noter og medieobjekter.

Hvis du vælger en handling uden et gyldigt valg – for eksempel en sammenlægning med kun ét objekt valgt – forklarer en dialog, hvad der kræves.
