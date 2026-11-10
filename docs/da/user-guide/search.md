# Søg

Søgesiden er tilgængelig ved at klikke på forstørrelsesglasikonet i den øverste app-bar, eller ved at trykke på `s` [tastaturgenvej](shortcuts.md).

## Fuldtekst søgning

Skriv en forespørgsel i søgefeltet. Resultater vises, mens du skriver, fra det andet tegn; tryk på Enter for at søge efter et enkelt tegn. Gramps Web søger på tværs af alle objekttyper – personer, familier, begivenheder, steder, kilder, citater, arkiver, noter og medier – og returnerer matchende resultater rangeret efter relevans. For at rydde søgningen, klik på ryd-knappen i feltet eller tryk på Escape.

Hver resultat viser objekttypen, dens navn og nogle detaljer, for eksempel fødsel og død af en person, ægteskab af en familie, forfatteren af en kilde, eller den første linje af en note. Klik på et hvilket som helst resultat for at åbne den tilsvarende detaljeside.

## Søgning syntaks

- **Alle ord skal matche.** `Müller Berlin` finder objekter, der indeholder begge ord.
- **`or`** finder objekter, der indeholder enten ord, f.eks. `Meyer or Maier`. `and` kan også skrives mellem ord, men det gør ingen forskel.
- `or` gælder for de ord, der står direkte ved siden af: `Meyer or Maier Berlin` betyder "(Meyer or Maier) og Berlin". Parentheser understøttes ikke.
- **Anførselstegn** matcher en sætning, dvs. ord i denne rækkefølge: `"Johann Georg"`.
- **Wildcard:** et afsluttende `*` matcher enhver afslutning, f.eks. `Mey*` matcher "Meyer", "Meyers", "Meyerhofer" osv. Dette fungerer også for sætninger: `"Johann Georg"*`.
- **Det sidste ord er fuldført.** Hvis forespørgslen slutter med et bogstav eller ciffer, søges der, som om det sluttede med `*`, så `Anna Smi` finder allerede "Anna Smith". For at søge efter det sidste ord præcist, afslut forespørgslen med et mellemrum, eller sæt ordet i anførselstegn. Det samme gælder for søgefelterne i objektsvælgerne og [kortet](map.md#search).
- `or` og `and` genkendes i enhver skrift. For at søge efter et af disse ord selv, sæt det i anførselstegn.
- Ord kan ikke udelukkes; der er ingen "not".

## Hvad søgningen finder

- Accenter behøver ikke at matche: "Müller" finder også "Muller", og "muller" finder "Müller".
- Familier og begivenheder findes også ved navnene på deres personer, f.eks. "Müller" finder familierne og begivenhederne for alle, der hedder Müller. Disse resultater rangeres under direkte matches.
- Standardtyper findes ved deres navne på dit interface-sprog, f.eks. "Taufe" finder dåb i det tyske interface.
- Underscores adskiller ord, så "microfilm" finder en mediefil ved navn `scanned_microfilm.png`.
- Brugere, der ikke kan se private optegnelser, finder ikke objekter gennem private oplysninger, såsom en familie gennem navnet på et privat medlem.

## Filtrering efter objekttype

Under søgefeltet giver toggle-knapper for hver objekttype (Personer, Familier, Begivenheder, Steder, …) dig mulighed for at indsnævre resultaterne til en eller flere specifikke typer. Som standard søges der i alle typer. Aktivering af en eller flere knapper begrænser resultaterne til kun disse typer.
