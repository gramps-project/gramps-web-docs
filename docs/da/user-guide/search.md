# Søg

Søgesiden er tilgængelig ved at klikke på forstørrelsesglasikonet i den øverste app-bar, eller ved at trykke på `s` [tastaturgenvej](shortcuts.md).

## Fuldtekst søgning

Skriv en hvilken som helst forespørgsel i søgefeltet og tryk på Enter (eller klik på søgeknappen). Gramps Web søger på tværs af alle objekttyper – personer, familier, begivenheder, steder, kilder, citater, arkiver, noter og medier – og returnerer matchende resultater rangeret efter relevans.

Resultaterne viser objekttypen, navnet og et kort resumé. Klik på et hvilket som helst resultat for at åbne den tilsvarende detaljeside.

Et afsluttende `*` kan bruges som et wildcard, f.eks. `Mey*` matcher "Meyer", "Meyers", "Meyerhofer" osv.

## Filtrering efter objekttype

Under søgefeltet giver toggle-knapper for hver objekttype (Personer, Familier, Begivenheder, Steder, …) dig mulighed for at indsnævre resultaterne til en eller flere specifikke typer. Som standard søges der i alle typer. Aktivering af en eller flere toggles begrænser resultaterne til kun disse typer.

## Semantisk søgning

Hvis serveradministratoren har aktiveret [semantisk (AI-drevet) søgning](../install_setup/configuration.md), vises en tilstandstoggle i øverste højre hjørne af søgesiden med to muligheder:

- **Søg** – standard fuldtekst søgning (standard)
- **Semantisk** – AI-drevet søgning, der forstår betydningen af din forespørgsel i stedet for at matche nøjagtige ord

Semantisk søgning er nyttig til naturlige sprogforespørgsler som "landmand i Bayern i det 19. århundrede". Det kræver, at den semantiske søgeindeks er udfyldt; se [Administrationsindstillinger](../administration/settings.md) for hvordan man bygger eller opdaterer indekset.
