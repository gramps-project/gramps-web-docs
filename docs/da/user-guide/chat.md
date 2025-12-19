# Brug af AI-chat

!!! info
    AI-chat kræver Gramps Web API version 2.5.0 eller højere og Gramps Web version 24.10.0 eller højere.

Chatvisningen i Gramps Web (hvis tilgængelig i din installation) giver adgang til en AI-assistent, der kan besvare spørgsmål om dit slægtstræ.

!!! warning
    Da dette stadig er en ny og udviklende funktion, fungerer nogle typer spørgsmål godt, mens andre ikke gør. Ligesom med enhver AI-assistent kan den give faktuelt forkerte svar, så sørg for altid at dobbelttjekke.

## Hvordan det fungerer

For at forstå, hvilke typer spørgsmål assistenten kan besvare, er det nyttigt at forstå, hvordan det fungerer under motorhjelmen:

1. Brugeren stiller et spørgsmål.
2. Gramps Web identificerer et antal (f.eks. ti) Gramps-objekter, der sandsynligvis indeholder de oplysninger, der besvarer spørgsmålet. Til dette formål bruger den en teknik kaldet "semantisk søgning". For eksempel, hvis du spørger "Hvad hedder John Does børn?", hvis en familie eksisterer med John Doe som far, er det sandsynligt, at den er blandt de øverste resultater.
3. Gramps Web sender brugerens spørgsmål sammen med den hentede kontekstinformation til en stor sprogmodel ("chatbot") og beder den om at udtrække det rigtige svar.
4. Svaret vises for brugeren.

## Hvordan man stiller et spørgsmål

På grund af den måde, chatten fungerer på, er det (i øjeblikket) ikke muligt for AI-assistenten at besvare spørgsmål om specifikke relationer udover forældre eller børn, medmindre disse oplysninger er indeholdt som tekst i en note.

Da hvert svar er baseret på et begrænset antal af de bedste semantiske søgeresultater, kan det heller ikke besvare spørgsmål om statistikker ("hvor mange personer i min database ...").

For at undgå tvetydigheder og misforståelser er det nyttigt at formulere spørgsmålet så detaljeret som muligt.

Bemærk, at store sprogmodeller er flersprogede, så du kan tale med den på dit eget sprog, og den vil svare på samme sprog.

!!! tip
    Del venligst din erfaring om ting, der fungerer og ikke fungerer, med fællesskabet.
