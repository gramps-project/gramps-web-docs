# Hvordan Gramps organiserer data

Gramps Web gemmer et slægtstræ ikke som et diagram, men som separate objekter – personer, familier, begivenheder, steder, kilder osv. – der er knyttet til hinanden. Når du først ved, hvordan disse objekter passer sammen, bliver indtastning af data forudsigeligt: alt, hvad du vil knytte til, skal eksistere først.

Gramps Web bruger den samme datamodel som Gramps Desktop, så alt på denne side gælder for begge.

## Byggeklodserne

| Objekt | Hvad det repræsenterer | Eksempler |
|---|---|---|
| Person | En individuel | Dig, din bedstemor |
| Familie | Et par, deres børn, eller begge | Dine forældre og deres børn |
| Begivenhed | Noget der skete, med en dato og et sted | Fødselsdag, ægteskab, folketælling, emigration |
| Sted | En geografisk placering | En landsby, en sogn, et land |
| Kilde | Et dokument eller en samling af information | Et sognebånd, en folketælling, en bog |
| Citering | En specifik reference inden for en kilde | Side 12, indtastning 3 af sognebåndet |
| Repository | Hvor en kilde opbevares | Et arkiv, et bibliotek, en hjemmeside |
| Note | Fritekst | En transkription, forskningsbemærkninger |
| Medieobjekt | En fil | Et foto, et scannet certifikat |

Hver objekttype har sin egen liste i Gramps Web, se [Lister](lists.md).

## Personer og familier

Forældre og børn er ikke direkte knyttet til hinanden, men gennem en **familie**. En familie har op til to partnere og et vilkårligt antal børn:

- Dine forældre og du er knyttet gennem den familie, hvor du er et barn.
- Dine søskende er de andre børn i den samme familie.
- Du og din ægtefælle danner en anden familie, hvor du er en partner, sammen med dine børn.

En person kan være et barn i én familie og en partner i flere. Hvert barn har et forhold til hver af forældrene, såsom fødsel, adoption eller stedbarn, og hver familie har en forholdstype, såsom gift eller registreret partnerskab.

Det er derfor, "tilføje forældre" til en person betyder at tilføje personen som et barn til en familie – hvilket [trædiagrammet](tree-edit.md) gør for dig i ét trin.

## Begivenheder

En fødsel, død eller ægteskab er ikke et felt for en person, men en **begivenhed** for sig, med en type, en dato, et sted og en beskrivelse. Personer er knyttet til en begivenhed med en **rolle**: personen hvis fødsel det er, har rollen "Primær", mens en anden måske er knyttet til den samme begivenhed som vidne.

Begivenheder, der vedrører et par, såsom et ægteskab, tilhører familien snarere end nogen af partnerne. En begivenhed kan også deles af flere personer – for eksempel en folketællingsoptegnelse, der opregner en hel husstand – i stedet for at blive indtastet én gang pr. person.

## Delte objekter: steder og kilder

Steder, kilder, citater, repositories, noter og medieobjekter eksisterer i deres egen ret, og et vilkårligt antal andre objekter kan referere til den samme. Dette har nogle konsekvenser:

- **Opret én gang, vælg mange gange.** Landsbyen, hvor ti af dine forfædre blev født, er ét sted, valgt i ti fødselsbegivenheder. Hvis du retter dens navn eller koordinater, gælder rettelsen overalt.
- **Opret det, før du vælger det.** Formularer i Gramps Web vælger steder og kilder, der allerede eksisterer. Opret først et nyt sted eller en kilde ved hjælp af **+** (Tilføj) knappen i den øverste app-bar.
- **Steder er indlejret.** Et sted kan være omfattet af et større – en landsby af et amt, amtet af et land – så du ikke behøver at gentage hele hierarkiet for hver landsby.
- **Kilder og citater er adskilte.** En kilde er sognebåndet som helhed; en citering er den specifikke indtastning, der understøtter en kendsgerning, med dens side, dato og din tillid til den. Mange citater kan pege på den samme kilde.

Hvis du ved et uheld har oprettet det samme sted eller kilde to gange, kan du [sammensmelte duplikaterne](lists.md#merge).

## Hjemmepersonen

Hjemmepersonen er den person, som slægtstræet starter fra, og det standard startpunkt for rapporter. Se [Første login](first-login.md) for hvordan du indstiller det.

!!! note "Forskellig fra Gramps Desktop"
    I Gramps Desktop gemmes hjemmepersonen i slægtstrædatabasen, så den er den samme for alle, der åbner den database. Gramps Web bruger ikke dette. I stedet gemmes hjemmepersonen i din browser, separat for hvert træ: den deles ikke med andre brugere, og den følger ikke med til en anden browser eller enhed. Efter at have importeret et træ fra Gramps Desktop, eller når du bruger Gramps Web på en anden enhed, skal du indstille det igen.

## En anbefalet rækkefølge

Når du indtaster en ny familie manuelt, undgår denne rækkefølge at hoppe frem og tilbage mellem formularer:

1. **Steder og kilder.** Opret de steder, du har brug for, og hvis du registrerer kilder, den kilde, du arbejder ud fra.
2. **Personer.** Tilføj personerne med deres fødsels- og dødsdatoer og steder. Dette er hurtigst i redigeringstilstand for slægtstrædiagrammet, som opretter familierne for dig – se [Start et nyt træ](start-tree.md) og [Redigering af slægtstræet](tree-edit.md).
3. **Yderligere begivenheder.** Åbn en familie (for eksempel fra en persons forholds-fane) for at tilføje ægteskabet, og en persons side for at tilføje andre begivenheder.
4. **Citeringer.** På fanen Kildeciteringer for personen, begivenheden eller et andet objekt, som en kilde understøtter, tilføj en ny citering, vælg kilden, og indtast siden.
5. **Noter og medier.** Vedhæft transkriptioner, fotos og scanninger – se [Tilføj mediefiler](media.md).

## Indtastning af datoer

En dato indtastes som separate år, måned og dag felter, som også kan udfyldes ved hjælp af en datovælger. Udelad de dele, du ikke kender: et år alene er en gyldig dato.

I stedet for at gætte en præcis dag, beskriv hvad du faktisk ved med datoens **Type**:

| Hvad du ved | Type | Eksempel |
|---|---|---|
| Den nøjagtige dato, eller del af den | Regelmæssig | 12. marts 1850, eller bare 1850 |
| En omtrentlig dato | omkring | omkring 1850 |
| En grænse | før, efter | før 1900 |
| Datoen ligger et sted inden for en periode | Interval | mellem 1850 og 1855 |
| Noget varede i en periode | Spænd | fra 1850 til 1855 |
| Kun starten eller slutningen af en periode | fra, til | fra 1850 |

**Kvalitet** feltet registrerer, hvordan du kom frem til en dato: "Estimeret" for et kvalificeret gæt, "Beregnet" for en dato afledt fra anden information, såsom et fødselsår beregnet ud fra en alder ved død.

!!! warning "Omkring og estimerede datoer dækker 50 år på hver side"
    Når Gramps sammenligner datoer, behandler det en dato af typen "omkring" – og enhver dato med kvaliteten "Estimeret" – som et interval, der strækker sig fra 50 år før til 50 år efter den angivne dato. For eksempel finder filtrering af listen over personer for personer født mellem 1840 og 1860 også en person født "omkring 1880", fordi den dato anses for at dække 1830 til 1930. På samme måde betragtes "før" og "efter" som at strække sig op til 50 år før eller efter datoen.

    Dette kan føre til overraskende resultater, så brug "omkring" og "Estimeret" kun, når du ikke kan indsnævre datoen. Hvis du kender en kortere periode, er et interval som "mellem 1878 og 1882" mere præcist.

**Kalender** feltet giver dig mulighed for at indtaste en dato i den kalender, der blev brugt i den oprindelige optegnelse, såsom den julianske kalender, i stedet for at konvertere den selv.
