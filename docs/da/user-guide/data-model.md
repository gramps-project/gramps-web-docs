# Hvordan Gramps organiserer data

Gramps Web gemmer et slægtstræ ikke som et diagram, men som separate objekter – personer, familier, begivenheder, steder, kilder osv. – der er knyttet til hinanden. Når du først ved, hvordan disse objekter passer sammen, bliver indtastning af data forudsigeligt: alt, hvad du vil linke til, skal eksistere først.

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

- Dine forældre og du er knyttet gennem den familie, hvor du er barn.
- Dine søskende er de andre børn i den samme familie.
- Du og din ægtefælle danner en anden familie, hvor du er en partner, sammen med dine børn.

En person kan være barn i én familie og partner i flere. Hvert barn har et forhold til hver af forældrene, såsom fødsel, adoption eller stedbarn, og hver familie har en forholdstype, såsom gift eller registreret partnerskab.

Det er derfor, at "tilføje forældre" til en person betyder at tilføje personen som barn til en familie – hvilket [trædiagrammet](tree-edit.md) gør for dig i ét trin.

## Begivenheder

En fødsel, død eller ægteskab er ikke et felt for en person, men en **begivenhed** for sig selv, med en type, en dato, et sted og en beskrivelse. Personer er knyttet til en begivenhed med en **rolle**: personen hvis fødsel det er, har rollen "Primær", mens en anden kan være knyttet til den samme begivenhed som vidne.

Begivenheder, der vedrører et par, såsom et ægteskab, tilhører familien snarere end nogen af partnerne. En begivenhed kan også deles af flere personer – for eksempel en folketællingsoptegnelse, der viser en hel husstand – i stedet for at blive indtastet én gang pr. person.

Dette påvirker redigering. Selve begivenheden – dens type, dato, sted og beskrivelse – er den samme for alle, der er knyttet til den, så redigering af en delt begivenhed fra én persons side ændrer den for dem alle. Redigeringsdialogen viser derfor de andre deltagere først, og felterne bliver først redigerbare efter **Rediger for alle**. Hvad der tilhører én persons link til begivenheden – rollen, og citeringer, noter og attributter, der kun gælder for den person – redigeres på begivenhedens side, i **Deltagere** fanen i redigeringstilstand. Der kan du også tilføje og fjerne deltagere. For eksempel tilhører en gudforældres rolle og noten "underskrevet med et mærke" gudforældres link til dåben, ikke dåben selv.

## Delte objekter: steder og kilder

Steder, kilder, citeringer, repositories, noter og medieobjekter eksisterer i deres egen ret, og et vilkårligt antal andre objekter kan henvise til den samme. Dette har et par konsekvenser:

- **Opret én gang, vælg mange gange.** Landsbyen, hvor ti af dine forfædre blev født, er ét sted, valgt i ti fødselsbegivenheder. Hvis du retter dens navn eller koordinater, gælder rettelsen overalt.
- **Opret det, før du vælger det.** Formularer i Gramps Web vælger steder og kilder, der allerede eksisterer. Opret først et nyt sted eller en kilde ved hjælp af **+** (Tilføj) knappen i den øverste app-bar.
- **Steder er indlejret.** Et sted kan være indeholdt af et større – en landsby af et amt, amtet af et land – så du ikke behøver at gentage hele hierarkiet for hver landsby.
- **Kilder og citeringer er separate.** En kilde er sognebåndet som helhed; en citering er den specifikke indtastning, der understøtter et faktum, med dens side, dato og din tillid til den. Mange citeringer kan pege på den samme kilde.

Hvis du ved et uheld har oprettet det samme sted eller kilde to gange, kan du [sammensmelte dubletterne](lists.md#merge).

## Redigering af en objekts side

På siden af en kilde, repository eller medieobjekt, klik på titlen i redigeringstilstand for at ændre den (for et medieobjekt, dets beskrivelse). Tryk på Enter, klik ✓, eller klik et andet sted for at gemme; tryk på Escape eller klik ✕ for at annullere.

De fleste lister på en objekts side bevarer den rækkefølge, du giver dem, for eksempel begivenheder, navne, attributter, adresser, citeringer eller børnene i en familie. I redigeringstilstand, vælg en række og flyt den med op- og ned-knapperne, eller træk den til sin nye position: med musen, tryk på rækken og flyt den; på en touchskærm, tryk og hold rækken, indtil den bliver taget op. Tryk på Escape mens du trækker for at annullere. Medier i galleriet kan omarrangeres på samme måde, se [Profilbilleder](media.md#profile-pictures).

## Hjemmepersonen

Hjemmepersonen er den person, som slægtstræets diagrammer starter fra, og det standard udgangspunkt for rapporter. Se [Første login](first-login.md) for hvordan du indstiller det.

!!! note "Forskellig fra Gramps Desktop"
    I Gramps Desktop gemmes hjemmepersonen i slægtstræets database, så den er den samme for alle, der åbner den database. Gramps Web bruger ikke dette. I stedet gemmes hjemmepersonen i din browser, separat for hvert træ: den deles ikke med andre brugere, og den følger ikke med dig til en anden browser eller enhed. Efter at have importeret et træ fra Gramps Desktop, eller når du bruger Gramps Web på en anden enhed, skal du indstille det igen.

## En anbefalet rækkefølge

Når du indtaster en ny familie manuelt, undgår denne rækkefølge at hoppe frem og tilbage mellem formularer:

1. **Steder og kilder.** Opret de steder, du har brug for, og hvis du registrerer kilder, den kilde, du arbejder ud fra.
2. **Personer.** Tilføj personerne med deres fødsels- og dødsdatoer og steder. Dette er hurtigst i redigeringstilstanden af slægtstrædiagrammet, som opretter familierne for dig – se [Start et nyt træ](start-tree.md) og [Redigering af slægtstræet](tree-edit.md).
3. **Yderligere begivenheder.** Åbn en familie (for eksempel fra en persons forholds-fane) for at tilføje ægteskabet, og en persons side for at tilføje andre begivenheder.
4. **Citeringer.** På fanen Kildeciteringer for personen, begivenheden eller et andet objekt, som en kilde understøtter, tilføj en ny citering, vælg kilden, og indtast siden.
5. **Noter og medier.** Vedhæft transkriptioner, fotos og scanninger – se [Tilføj mediefiler](media.md).

## Indtastning af datoer

En dato indtastes som separate år, måned og dag felter, som også kan udfyldes ved hjælp af en datovælger. Udelad de dele, du ikke kender: et år alene er en gyldig dato. 
I stedet for at gætte en præcis dag, beskriv hvad du faktisk ved ved at vælge datoens type med chipsene ovenfor felterne. En hint under chipsene forklarer den valgte type:

| Hvad du ved | Type | Eksempel |
|---|---|---|
| Den præcise dato, eller en del af den | Regelmæssig | 12. marts 1850, eller blot 1850 |
| En omtrentlig dato | Omtrent | omtrent 1850 |
| En grænse | Før, Efter | før 1900 |
| Datoen ligger et sted inden for en periode | Interval | mellem 1850 og 1855 (felterne "Tidligst" og "Senest") |
| Noget varede i en periode | Spænd | fra 1850 til 1855 |

For en Spænd kan enten af de to datoer ("Fra" og "Til") være tom, så "fra 1850" eller "til 1855" er en Spænd med kun én dato.

Felterne **Kvalitet** og **Kalender** er under **Flere muligheder**, som åbner af sig selv, når en dato bruger en af dem. Kvaliteten registrerer, hvordan du kom frem til en dato: "Estimeret" for et kvalificeret gæt, "Beregnet" for en dato afledt fra andre oplysninger, såsom et fødselsår beregnet ud fra en alder ved død.

!!! warning "Omtrentlige og estimerede datoer dækker 50 år på hver side"
    Når Gramps sammenligner datoer, behandler det en dato af typen "omtrent" – og enhver dato med kvaliteten "Estimeret" – som et interval, der strækker sig fra 50 år før til 50 år efter den angivne dato. For eksempel finder filtrering af Personen-listen personer født mellem 1840 og 1860 også en person født "omtrent 1880", fordi den dato anses for at dække 1830 til 1930. På samme måde betragtes "før" og "efter" som at strække sig op til 50 år før eller efter datoen.

    Dette kan føre til overraskende resultater, så brug "omtrent" og "Estimeret" kun, når du ikke kan indsnævre datoen. Hvis du kender en kortere periode, er et Interval som "mellem 1878 og 1882" mere præcist.

Kalenderen giver dig mulighed for at indtaste en dato i den kalender, der blev brugt i den oprindelige optegnelse, såsom den julianske kalender, i stedet for at konvertere den selv.
