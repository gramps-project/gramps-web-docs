# Lister

Hver objekttype i Gramps Web har en listevisning: Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter og Medier. De fungerer alle på samme måde og deler de samme værktøjer til sortering, filtrering og redigering i bulk.

## Sortering og paging

Klik på en kolonneoverskrift for at sortere efter den kolonne; klik på den igen for at omvende rækkefølgen. Sortering udføres af serveren, så den gælder for hele listen, ikke kun den side, du ser på.

Lange lister er opdelt i sider. Brug pagineringskontrollerne nederst for at bevæge dig mellem dem.

På smalle skærme skifter tabellen automatisk til et kompakt layout, så listevisninger forbliver brugbare på en telefon.

## Vælg kolonner

Klik på tandhjulsikonet i højre ende af værktøjslinjen over listen for at åbne **Kolonner**-dialogen. Marker eller fjern markeringen i en kolonne for at vise eller skjule den. **Nulstil** gendanner standardvalget for den liste.

Mindst én kolonne skal forblive synlig, så den sidste tilbageværende kolonne kan ikke fjernes.

Udover de standardkolonner tilbyder hver liste en **Tags**-kolonne og, for brugere der kan se private optegnelser, en **Privatliv**-kolonne, der viser et lås for hvert privat objekt. Hvis du har ændret kolonnevalget for en liste før, tilføjes nye kolonner som **Tags** ikke automatisk; marker dem i dialogen.

Dit kolonnevalg huskes pr. objekttype og pr. slægtstræ. Det gemmes i din browser, så det ikke er synligt for andre brugere – men det følger heller ikke med til en anden browser eller enhed.

## Filtrering

Klik på **filter**-knappen for at åbne filterpanelet. Det tilbyder tre måder at filtrere på, som kan kombineres:

- **Færdiglavede filtre** i sammenklappelige sektioner, der afhænger af objekttypen. For personer kan du for eksempel filtrere efter navn, fødselsår, dødsår, forskellige personegenskaber, antallet af tilknytninger, tags og om et objekt er privat eller offentligt. Familier kan filtreres efter farens, morens eller et barns navn, kilder efter forfatter, og steder og arkiver efter deres type.
- **Avanceret filter** – en betingelsesbygger for filtre, som de færdiglavede ikke kan udtrykke, beskrevet [nedenfor](#advanced-filter).
- **GOQL** – et tekstfelt til et udtryk i [Gramps Object Query Language](goql.md), med syntaksfremhævning. Skriv udtrykket og tryk på Enter eller klik på **Anvend**. Hvis udtrykket er ugyldigt, markeres feltet som en fejl. Et udtryk gælder oven på de andre filtre.

Aktive filtre vises som chips i en række under værktøjslinjen. Fjern et enkelt filter ved at klikke på chipens ryd-knap, eller brug **Ryd alle filtre** for at fjerne dem alle på én gang.

### Avanceret filter

Klik på **Avanceret filter** nederst i filterpanelet for at åbne betingelsesbyggeren. Dens betingelser er de filterregler, der kendes fra Gramps Desktop, såsom "Personer med &lt;navn&gt;" eller "Forfædre til &lt;person&gt;".

- Klik på **Tilføj betingelse** for at vælge en regel. Reglerne er grupperet i kategorier og kan søges efter navn eller beskrivelse.
- Udfyld reglens parametre. Hver parameter har et matchende input, for eksempel et datofelt, en tagvælger eller en objektvælger for en person eller et sted.
- Vælg hvordan betingelserne i en gruppe kombineres: **Alle betingelser**, **Enhver betingelse**, eller – via menuen ved siden af dem – **Præcis én betingelse**.
- Klik på **Tilføj gruppe** for at tilføje en gruppe betingelser inden i en anden gruppe, med sin egen måde at kombinere dem på.
- Vælg **Ikke** på en betingelse eller gruppe for at invertere den.

Klik på **Anvend** for at filtrere listen.

De færdiglavede filtre og det GOQL-udtryk, der er aktive, når du åbner byggeren, vises der som betingelser. Et GOQL-udtryk kan også tilføjes som en betingelse for sig selv, for eksempel for at kombinere flere udtryk med **Enhver betingelse**. Hvis det filter, du bygger, kan udtrykkes med de færdiglavede filtre, vises det sammen med dem efter anvendelse. Ellers vises det som en enkelt **Avanceret filter** chip, og filterpanelet tilbyder en **Rediger**-knap for at genåbne byggeren.

!!! note
    Regler, der henviser til brugerdefinerede filtre gemt i Gramps Desktop, er ikke tilgængelige i byggeren. Reglerne vises på dit sprog med Gramps Web API 3.24 eller nyere.

#### Gemte filtre

For at genbruge et filter, du har bygget, klik på **Gem** i betingelsesbyggeren og giv det et navn. Gemning under et eksisterende navn erstatter det filter. **Gemte filtre** i byggeren viser de gemte filtre for den aktuelle objekttype; ved at vælge et indlæses det i byggeren, hvor du kan ændre det, inden du klikker på **Anvend**.

Gemte filtre gemmes i din browser, pr. slægtstræ og objekttype, så de ikke er tilgængelige for andre brugere eller på dine andre enheder.

Et gemt filter kan stoppe med at fungere, når træet ændres, for eksempel hvis det henviser til en person, der siden er blevet slettet (objektvælgeren viser derefter "Ikke fundet"). Et sådant filter kan ikke anvendes eller gemmes, før betingelsen er rettet.

## Vælg objekter og handle på dem i bulk

Brugere med redigeringsrettigheder ser en **Vælg**-knap ved siden af filterknappen. Klik på den for at gå ind i udvælgelsestilstand, som tilføjer en afkrydsningsfelt til hver række.

Marker de objekter, du ønsker, og en værktøjslinje vises, der viser, hvor mange der er valgt, sammen med en **Handling** dropdown og en **Anvend**-knap.

Afkrydsningsfeltet i tabeloverskriften vælger alle objekter på den aktuelle side. Hvis flere objekter matcher de aktuelle filtre, tilbyder værktøjslinjen derefter **Vælg alle (N)**, som vælger alle N matchende objekter på tværs af alle sider. At fjerne markeringen i en række, ændre siden eller filtrene, eller forlade udvælgelsestilstand afslutter denne udvælgelse.

### Slet

Vælg et eller flere objekter, vælg **Slet**, og klik på **Anvend**. En bekræftelsesdialog beder dig bekræfte, og advarer om, at handlingen ikke kan fortrydes.

Sletning af mere end ti objekter kører som en baggrundsopgave. Dens fremskridt vises ved siden af **Anvend**-knappen og i [Notifikationer](notifications.md), og listen genindlæses, når det er færdigt.

!!! tip
    Sletninger registreres i [revisionshistorikken](revisions.md) ligesom enhver anden ændring, så en fejlagtig bulk-sletning kan fortrydes ved at fortryde den tilsvarende transaktion.

### Tags og privatliv

Handlingerne **Tilføj tag**, **Fjern tag** og **Privatliv** ændrer alle valgte objekter på én gang (kræver Gramps Web API 3.26 eller nyere):

- **Tilføj tag** tilføjer et eksisterende tag eller et nyt, du opretter i dialogen.
- **Fjern tag** fjerner et tag fra de valgte objekter, der har det.
- **Privatliv** markerer de valgte objekter som private eller offentlige. Dette ændrer kun selve objekterne, ikke deres dele eller de optegnelser, de linker til – se [Private optegnelser](privacy.md).

Som med sletning kører redigering af mere end ti objekter som en baggrundsopgave. Ændringerne registreres i [revisionshistorikken](revisions.md) som én transaktion, så de kan fortrydes sammen.

### Sammenlægning

Vælg **præcist to** objekter, vælg **Sammenlæg**, og klik på **Anvend**. En dialog beder om at vide, hvilket af de to der skal give de primære data til det sammenlagte objekt; klik på det, du vil beholde som primært. Det andet objekts data sammenlægges ind i det, og referencer opdateres.

Sammenlægning er tilgængelig for personer, familier, begivenheder, steder, kilder og citeringer. Det er ikke tilgængeligt for arkiver, noter og medieobjekter.

I medievisningen fungerer udvælgelse i både galleriet og liste-layoutet: i udvælgelsestilstand skifter klik på en flise eller række den. Medieobjekter kan ikke sammenlægges.

Hvis du vælger en handling uden en gyldig udvælgelse – for eksempel en sammenlægning med kun ét objekt valgt – forklarer en dialog, hvad der kræves.
