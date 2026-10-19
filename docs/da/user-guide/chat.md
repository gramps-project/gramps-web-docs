# Brug af AI-assistenten

!!! info
    AI-assistenten kræver Gramps Web API version 2.5.0 eller højere og Gramps Web version 24.10.0 eller højere. Gramps Web API version 3.6.0 introducerede værktøjsopkaldsfunktioner for mere intelligente interaktioner.

Den **Assistent** visning i Gramps Web (hvis tilgængelig i din installation, mærket "Chat" i ældre versioner) giver adgang til en AI-assistent, der kan besvare spørgsmål om dit slægtstræ.

!!! warning
    Da dette stadig er en ny og udviklende funktion, fungerer nogle typer spørgsmål godt, mens andre ikke gør. Desuden, ligesom med enhver AI-assistent, kan den give faktuelt forkerte svar, så sørg for altid at dobbelttjekke.

## Sådan fungerer det

For at forstå, hvilke typer spørgsmål assistenten kan besvare, er det nyttigt at forstå, hvordan det fungerer under motorhjelmen:

1. Brugeren stiller et spørgsmål.
2. Assistenten forespørger direkte din database ved hjælp af specialiserede værktøjer: den søger i træet med [fuldtekst søgning](search.md), filtrerer personer/begivenheder/familier/steder efter specifikke kriterier, beregner relationer mellem individer og slår komplette optegnelser op, inklusive deres noter.
3. En stor sprogmodel formulerer et svar baseret på de optegnelser, den har fundet.
4. Svaret vises for dig, med links til de optegnelser, det er baseret på.

På servere, der kører en Gramps Web API version ældre end 3.24, stolede assistenten også på semantisk søgning, som er ved at blive udfaset.

Mens assistenten arbejder, viser indikatorer, hvilke værktøjer den i øjeblikket bruger (f.eks. søger personer, ser op relationer), så du kan følge med, mens den bygger sit svar. Længere spørgsmål behandles som baggrundsopgaver – du kan navigere væk og komme tilbage, og fremskridt afspejles også i [Notifikationer](notifications.md). Svarene er formateret med Markdown (lister, fremhævelse, links osv.) for lettere læsning.

## Hvad du kan spørge om

Med værktøjsopkaldsfunktionerne introduceret i Gramps Web API version 3.6.0 kan AI-assistenten nu håndtere mere komplekse spørgsmål:

- **Familierelationer**: "Hvem er Janes Smiths bedsteforældre?" eller "Hvordan er John Doe relateret til Mary Johnson?"
- **Filtrerede søgninger**: "Vis mig alle personer født i London efter 1850" eller "Hvilke begivenheder fandt sted i Paris?"
- **Datarelaterede forespørgsler**: "Hvem døde før 1900?" eller "List ægteskaber, der fandt sted mellem 1920 og 1950"
- **Stedinformation**: "Hvilke steder er der i Frankrig?" eller "Fortæl mig om St. Mary's Church"
- **Generelle spørgsmål**: "Hvad hedder John Does børn?" eller "Hvornår blev Mary Smith født?"

## Tips til at stille spørgsmål

For at få de bedste resultater fra AI-assistenten:

- **Vær specifik**: Formuler dit spørgsmål med så mange detaljer som muligt for at undgå tvetydigheder. For eksempel, "Hvornår giftede John Smith, født i 1850 i Boston, sig?" er bedre end "Hvornår giftede John Smith sig?"
- **Brug rigtige navne**: Nævn specifikke navne, steder og datoer, når det er relevant.
- **Spørg om én ting ad gangen**: Del komplekse spørgsmål op i enklere dele for bedre resultater.
- **Brug dit eget sprog**: Store sprogmodeller er flersprogede, så du kan stille spørgsmål på dit eget sprog og modtage svar på samme sprog.

!!! tip
    Del venligst din erfaring om, hvad der fungerer og ikke fungerer med fællesskabet.
