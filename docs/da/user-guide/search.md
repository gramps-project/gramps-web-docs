# Søgning

Søgesiden kan tilgås ved at klikke på forstørrelsesglasikonet i den øverste app-bar, eller ved at trykke på `s` [tastaturgenvej](shortcuts.md).

## Fuldtekst søgning

Skriv en hvilken som helst forespørgsel i søgefeltet og tryk på Enter (eller klik på søgeknappen). Gramps Web søger på tværs af alle objekttyper – personer, familier, begivenheder, steder, kilder, citater, arkiver, noter og medier – og returnerer matchende resultater rangeret efter relevans.

Resultaterne viser objekttypen, navnet og et kort resumé. Klik på et hvilket som helst resultat for at åbne den tilsvarende detaljeside.

## Søgesyntaks

- **Alle ord skal matche.** `Müller Berlin` finder objekter, der indeholder begge ord.
- **`or`** finder objekter, der indeholder enten ord, f.eks. `Meyer or Maier`. `and` kan også skrives mellem ord, men det gør ingen forskel.
- `or` gælder for de ord, der står direkte ved siden af: `Meyer or Maier Berlin` betyder "(Meyer or Maier) og Berlin". Parentheser understøttes ikke.
- **Anførselstegn** matcher en sætning, dvs. ord i denne rækkefølge: `"Johann Georg"`.
- **Wildcard:** et afsluttende `*` matcher enhver afslutning, f.eks. `Mey*` matcher "Meyer", "Meyers", "Meyerhofer" osv. Dette fungerer også for sætninger: `"Johann Georg"*`.
- `or` og `and` genkendes i enhver skrift. For at søge efter et af disse ord selv, sæt det i anførselstegn.
- Ord kan ikke udelukkes; der er ingen "not".

## Hvad søgningen finder

- Accenter behøver ikke at matche: "Müller" finder også "Muller", og "muller" finder "Müller".
- Familier og begivenheder findes også ved navnene på deres personer, f.eks. "Müller" finder familierne og begivenhederne for alle, der hedder Müller. Disse resultater rangeres under direkte matches.
- Standardtyper findes ved deres navne på dit interface-sprog, f.eks. "Taufe" finder dåb i det tyske interface.
- Understreger adskiller ord, så "microfilm" finder en mediefil ved navn `scanned_microfilm.png`.
- Brugere, der ikke kan se private optegnelser, finder ikke objekter gennem private oplysninger, såsom en familie gennem navnet på et privat medlem.

## Filtrering efter objekttype

Under søgefeltet giver toggle-knapper for hver objekttype (Personer, Familier, Begivenheder, Steder, …) dig mulighed for at indsnævre resultaterne til en eller flere specifikke typer. Som standard søges der i alle typer. Aktivering af en eller flere knapper begrænser resultaterne til kun disse typer.
