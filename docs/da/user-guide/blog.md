# Brug den indbyggede blog

Bloggen er beregnet til at præsentere historier om din slægtshistorieforskning.

I Gramps-databasen repræsenteres blogindlæg som kilder med en vedhæftet note, der indeholder bloggens tekst, og eventuelt mediefiler til billederne af blogindlægget. Gramps Web behandler hver kilde med en tag `Blog` som blogartikel.

## Tilføj et blogindlæg

Den hurtigste måde at skrive et indlæg på er den dedikerede **Ny Blogindlæg** formular i Gramps Web. Åbn den enten fra den blå **+** knap på Blog-siden, eller fra **Tilføj** menuen (plus-ikonet) i den øverste app-bar ved at vælge **Blogindlæg**.

Formularen har felter til:

- **Titel** – titlen på indlægget (påkrævet)
- **Forfatter** – hvem der har skrevet det
- **Indhold** – en rich-text editor til selve indlægget
- **Media** – et eller flere medieobjekter. Den første bliver forhåndsvisningsbilledet vist over teksten; alle vises som et galleri nedenfor.
- **Tags** og en **privat** switch, som for enhver anden genstand

At gemme formularen opretter den underliggende kilde, note og `Blog` tag for dig, som beskrevet [nedenfor](#relation-mellem-blog-og-kilder).

### Tilføjelse af et indlæg manuelt

Du kan også oprette et indlæg ved at bygge de underliggende objekter selv. Dette er den eneste måde at gøre det på i Gramps Desktop ([synchroniseret](../administration/sync.md) med Gramps Web), og trinene er de samme i begge applikationer:

- Tilføj en ny kilde. Titlen på kilden vil være titlen på dit blogindlæg, forfatteren af kilden vil være forfatteren af indlægget.
- Valgfrit, associer kilden med et repository, der svarer til din Gramps Web blog
- Tilføj en ny note til kilden. Skriv dit blogindlæg og kopier teksten ind i noten.
- Valgfrit, tilføj en eller flere mediefiler til din kilde. Den første mediefil vil blive taget som forhåndsvisningsbilledet for indlægget vist over teksten. Alle mediefiler vil blive vist nedenfor teksten som et galleri.
- Tilføj etiketten `Blog` til kilden (opret den, hvis den ikke eksisterer)

## Relation mellem blog og kilder

Da blogindlæg blot er kilder, vises alle blogartikler også på listen over kilder og dukker op som kilder i søgninger. I kildevinduet er der en knap "vis i blog", der vil tage dig til blogvinduet for det pågældende blogindlæg. URL'en for blogindlægget indeholder også Gramps ID for den tilsvarende kilde, så en artikel på `yourdomain.com/blog/S0123` svarer til kilden på `yourdomain.com/source/S0123`.

I bunden af hvert blogindlæg er der en knap "detaljer", der vil tage dig til kildevinduet.
