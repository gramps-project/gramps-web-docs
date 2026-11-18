# Brug af AI-assistenten

**Assistent**-visningen i Gramps Web (hvis aktiveret i din installation) giver adgang til en AI-assistent, der besvarer spørgsmål om dit slægtstræ.

!!! warning
    Som med enhver AI-assistent kan svarene være forkerte. Brug linksene i svaret til at tjekke de optegnelser, det er baseret på.

## Sådan fungerer det

Assistenten kender ikke dit træ på forhånd. For at besvare et spørgsmål slår en stor sprogmodel op i de optegnelser, den har brug for, ligesom du ville gøre selv:

- den søger i træet med [fuldtekst søgning](search.md),
- den filtrerer personer, begivenheder og familier efter kriterier som navne, datoer, steder eller antallet af børn,
- den finder forfædre, efterkommere og andre slægtninge til en person, med deres relation,
- den læser komplette optegnelser om personer, familier, begivenheder, steder og noter.

Den svarer derefter baseret på de optegnelser, den har fundet, med links til dem. Mens den arbejder, vises de værktøjer, den bruger, så du kan følge med. Spørgsmål, der tager længere tid, kører i baggrunden – du kan navigere væk og komme tilbage.

Assistenten svarer kun ud fra dit træ, ikke fra den generelle viden om sprogmodellen – selv ikke om velkendte personer. Hvis træet ikke registrerer noget, siger det det, og nævner relateret information, den fandt, for eksempel i en note. Den ser kun, hvad du har lov til at se: links til private optegnelser vises som almindelig tekst for brugere, der ikke kan se dem.

Opfølgningsspørgsmål bevarer konteksten fra tidligere spørgsmål i den samme samtale, så du kan spørge "Og hvornår døde han?" efter at have spurgt om en person.

## Hvad du kan spørge om

- **Fakta om personer**: "Hvornår blev Mary Smith født?" eller "Hvad hedder John Does børn?"
- **Slægtninge**: "Hvem er bedsteforældrene til Jane Smith?" eller "Hvilke efterkommere af Johann Meyer emigrerede til Amerika?"
- **Søgninger med kriterier**: "Hvem blev født i London efter 1850?", "List ægteskaber mellem 1920 og 1950", eller "Hvilke par havde fem eller flere børn?"
- **Steder**: "Hvilke begivenheder fandt sted i Paris?" eller "Hvem blev født i Danmark?" – steder inden for et større sted er inkluderet.
- **Noter**: "Hvad siger noterne om gården til Meyer-familien?"

Spørgsmål, der kræver hele træet på én gang, såsom "Hvad er det mest almindelige fornavn?", fungerer mindre godt, da assistenten kun ser et begrænset antal optegnelser pr. opslag.

## Spørgsmål om billeder

Hvis serveradministratoren har aktiveret det, har prompten en knap til at vedhæfte billeder. Du kan også indsætte et billede eller trække billedfiler ind på prompten. Op til fire billeder kan vedhæftes til et spørgsmål, for eksempel et scan af en kirkebog for at spørge "Hvem nævnes i denne post, og er de i mit træ?"

Billederne sendes kun med det spørgsmål, de er vedhæftet. Opfølgningsspørgsmål kan referere til, hvad assistenten sagde om dem, men ikke til billederne selv, så vedhæft dem igen, hvis det er nødvendigt. Hvis dit træ har en grænse for AI-brug, tæller hvert billede som et ekstra spørgsmål.

## Lad assistenten ændre dit træ

Hvis serveradministratoren har aktiveret det, kan redaktører, ejere og administratorer bede assistenten om at ændre træet, for eksempel "Tilføj en dåb den 3. maj 1802 i St. Mary's til Johann Meyer" eller "Ret fødselsåret for Anna Smith, det skal være 1871".

Assistenten ændrer aldrig noget af sig selv. Den svarer med et **Foreslåede ændringer** kort, der viser hver optegnelse, den ville tilføje, redigere eller slette, med de gamle værdier gennemstreget og de nye værdier fremhævet. Intet sker, før du klikker på **Anvend**. Ændringerne foretages derefter i ét trin, som du kan fortryde ligesom enhver anden redigering, fra den besked, der vises, eller i [revisionshistorikken](revisions.md).

Tjek et forslag grundigt, før du anvender det – især at assistenten har valgt den rigtige person, og at den ikke har tilføjet en ny optegnelse (såsom et sted eller en kilde), der allerede findes i dit træ under et lidt andet navn. Hvis et forslag ikke er helt korrekt, så sig, hvad der skal ændres, og assistenten foreslår igen.

Når et forslag er blevet anvendt, kan ældre forslag i den samme samtale ikke længere anvendes, da de blev lavet til træet, som det var før. Det samme sker, hvis en af de berørte optegnelser er blevet ændret i mellemtiden.

## Tips til at stille spørgsmål

- **Navngiv personerne.** Assistenten ved ikke, hvem du er, eller hvem din hjemmeperson er, så i stedet for "min bedstemor", spørg om "bedstemoren til Anna Smith (født 1950)". Du kan også bruge Gramps ID'er, f.eks. "børnene til I0042".
- **Vær specifik** når navne er almindelige: "Hvornår giftede John Smith, født i 1850 i Boston, sig?" er bedre end "Hvornår giftede John Smith sig?"
- **Brug dit sprog.** Du kan spørge på dit eget sprog og modtage svar på samme sprog.
- **Spørg igen anderledes** hvis et svar ser ufuldstændigt ud – for eksempel ved at nævne det sted eller tidsrum, du er interesseret i.

!!! tip
    Del venligst din erfaring med, hvad der fungerer og ikke fungerer med fællesskabet.
