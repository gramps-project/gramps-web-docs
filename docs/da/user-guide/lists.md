# Lister

Hver objekttype i Gramps Web har en listevisning: Personer, Familier, Begivenheder, Steder, Kilder, Citeringer, Arkiver, Noter og Medier. De fungerer alle på samme måde og deler de samme værktøjer til sortering, filtrering og redigering i bulk.

## Sortering og paging

Klik på en kolonneoverskrift for at sortere efter den kolonne; klik igen for at omvende rækkefølgen. Sortering udføres af serveren, så det gælder for hele listen, ikke kun den side, du kigger på.

Lange lister er opdelt i sider. Brug pagineringskontrollerne nederst for at bevæge dig mellem dem.

På smalle skærme skifter tabellen automatisk til et kompakt layout, så listevisninger forbliver brugbare på en telefon.

## Valg af kolonner

Klik på tandhjulsikonet over listen for at åbne **Kolonner**-dialogen. Sæt eller fjern markeringen i en kolonne for at vise eller skjule den. **Nulstil** gendanner standardvalget for den liste.

Mindst én kolonne skal forblive synlig, så den sidste tilbageværende kolonne kan ikke få fjernet markeringen.

Dit kolonnevalg huskes pr. objekttype og pr. slægtstræ. Det gemmes i din browser, så det ikke er synligt for andre brugere – men det følger heller ikke med til en anden browser eller enhed.

## Filtrering

Klik på **filter**-knappen for at åbne filterpanelet. En pillekontakt øverst i panelet skifter mellem to tilstande:

- **simpel** – et sæt færdiglavede filtre, der afhænger af objekttypen. For personer kan du for eksempel filtrere efter fødselsår, dødsår, forskellige personlige egenskaber, antallet af tilknytninger, tags og om et objekt er privat eller offentligt.
- **GQL** – et enkelt tekstfelt til en avanceret forespørgsel i [Gramps Query Language](gql.md). Skriv forespørgslen og tryk på Enter eller klik på **Anvend**. Hvis forespørgslen er ugyldig, bliver feltets ramme rød.

Aktive filtre vises som chips over listen. Fjern et enkelt filter ved at klikke på chipens ryd-knap, eller brug **Fjern alle filtre** for at fjerne dem alle på én gang.

!!! note
    De to tilstande er alternativer, ikke additive: en GQL-forespørgsel erstatter de simple filtre, og hvis du skifter tilbage til simpel tilstand, fjernes forespørgslen.

## Vælg objekter og handlinger i bulk

Brugere med redigeringsrettigheder ser en **Vælg**-knap ved siden af filterknappen. Klik på den for at gå ind i udvælgelsestilstand, som tilføjer en afkrydsningsfelt til hver række.

Sæt kryds ved de objekter, du ønsker, og en værktøjslinje vises, der viser, hvor mange der er valgt, sammen med en **Handling** dropdown og en **Anvend**-knap.

### Slet

Vælg et eller flere objekter, vælg **Slet**, og klik på **Anvend**. En bekræftelsesdialog beder dig om at bekræfte og advarer om, at handlingen ikke kan fortrydes.

!!! tip
    Sletninger registreres i [revisionshistorikken](revisions.md) ligesom enhver anden ændring, så en fejlagtig bulk-sletning kan fortrydes ved at fortryde den tilsvarende transaktion.

### Sammenflet

Vælg **præcist to** objekter, vælg **Sammenflet**, og klik på **Anvend**. En dialog beder om at vælge, hvilket af de to der skal give de primære data til det sammenflettede objekt; klik på det, du vil beholde som primært. Det andet objekts data flettes ind i det, og referencer opdateres.

Sammenfletning er tilgængelig for personer, familier, begivenheder, steder, kilder og citeringer. Det er ikke tilgængeligt for arkiver, noter og medieobjekter.

Hvis du vælger en handling uden et gyldigt valg – for eksempel en sammenfletning med kun ét objekt valgt – forklarer en dialog, hvad der kræves.
