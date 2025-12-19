# Brug af AI-chat

!!! info
    AI-chat kræver Gramps Web API version 2.5.0 eller højere og Gramps Web version 24.10.0 eller højere. Gramps Web API version 3.6.0 introducerede værktøjsopkaldsfunktioner for mere intelligente interaktioner.

Chatvisningen i Gramps Web (hvis tilgængelig i din installation) giver adgang til en AI-assistent, der kan besvare spørgsmål om dit slægtstræ.

!!! warning
    Da dette stadig er en ny og udviklende funktion, fungerer nogle typer spørgsmål godt, mens andre ikke gør. Ligesom med enhver AI-assistent kan den give faktuelt forkerte svar, så sørg for altid at dobbelttjekke.

## Hvordan det fungerer

For at forstå, hvilke typer spørgsmål assistenten kan besvare, er det nyttigt at forstå, hvordan det fungerer under motorhjelmen:

1. Brugeren stiller et spørgsmål.
2. AI-assistenten kan bruge flere tilgange til at finde svar:
   - **Semantisk søgning**: Gramps Web identificerer objekter i dit slægtstræ, der sandsynligvis indeholder relevant information. For eksempel, hvis du spørger "Hvad hedder John Does børn?", vil familier med John Doe som far være blandt de øverste resultater.
   - **Værktøjsopkald (Gramps Web API v3.6.0+)**: Assistenten kan direkte forespørge din database ved hjælp af specialiserede værktøjer til at søge, filtrere personer/begivenheder/familier/steder efter specifikke kriterier, beregne relationer mellem individer og hente detaljeret information.
3. Gramps Web sender spørgsmålet sammen med de hentede oplysninger til en stor sprogmodel for at formulere et svar.
4. Svaret vises for dig.

## Hvad du kan spørge om

Med de værktøjsopkaldsfunktioner, der blev introduceret i Gramps Web API version 3.6.0, kan AI-assistenten nu håndtere mere komplekse spørgsmål:

- **Familierelationer**: "Hvem er Jane Smiths bedsteforældre?" eller "Hvordan er John Doe relateret til Mary Johnson?"
- **Filtrerede søgninger**: "Vis mig alle personer født i London efter 1850" eller "Hvilke begivenheder fandt sted i Paris?"
- **Dato-baserede forespørgsler**: "Hvem døde før 1900?" eller "List ægteskaber, der fandt sted mellem 1920 og 1950"
- **Stedinformation**: "Hvilke steder er der i Frankrig?" eller "Fortæl mig om St. Mary's Church"
- **Generelle spørgsmål**: "Hvad hedder John Does børn?" eller "Hvornår blev Mary Smith født?"

## Tips til at stille spørgsmål

For at få de bedste resultater fra AI-assistenten:

- **Vær specifik**: Formuler dit spørgsmål med så mange detaljer som muligt for at undgå tvetydigheder. For eksempel, "Hvornår giftede John Smith, født i 1850 i Boston, sig?" er bedre end "Hvornår giftede John Smith sig?"
- **Brug rigtige navne**: Nævn specifikke navne, steder og datoer, når det er relevant.
- **Spørg om én ting ad gangen**: Del komplekse spørgsmål op i enklere dele for bedre resultater.
- **Brug dit sprog**: Store sprogmodeller er flersprogede, så du kan stille spørgsmål på dit eget sprog og modtage svar på samme sprog.

!!! tip
    Del venligst din oplevelse om, hvad der fungerer og ikke fungerer med fællesskabet.
