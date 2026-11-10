# Slægtstræ

Slægtstræ-siden er tilgængelig fra sidepanelet og viser interaktive diagrammer centreret om en valgt person. Fem diagramtyper er tilgængelige via faner øverst på siden.

## Valg af startperson

Alle diagrammer starter fra den person, der aktuelt er valgt i træet (vist i værktøjslinjen). Den aktuelt centrerede person er fremhævet med en skygge. Brug **Hjem Person**-knappen til at hoppe tilbage til din hjemperson, eller **Tilbage**-knappen til at vende tilbage til den tidligere viste person. Klik på en persons kort i ethvert diagram for at recenter diagrammet på den person.

Hvis der ikke er sat nogen hjemperson, tilbyder siden en **Sæt Hjem Person**-knap til at søge efter og vælge en direkte. Hvis træet endnu ikke indeholder nogen personer, ser brugere med rollen som Redaktør eller højere i stedet en **Ny Person**-knap – den første person, der oprettes i et tomt træ, bliver automatisk din hjemperson, så diagrammet vises med det samme.

## Diagramtyper

### Forfædres træ

Et stamtavlediagram, der viser forfædrene til den valgte person. Forældre vises til venstre (eller højre, afhængigt af layoutet), bedsteforældre længere ude, og så videre.

### Efterkommere træ

Viser efterkommerne til den valgte person – børn, børnebørn og så videre.

### Timeglasdiagram

Kombinerer forfædre ovenfor og efterkommere nedenfor den valgte person i en enkelt visning.

### Forholdsdiagram

Viser forholdsvejen mellem to personer. Den valgte person er den ene ende; klik på en hvilken som helst anden person i diagrammet for at sætte den anden ende og vise den korteste forholdsvej mellem dem.

!!! note
    Den samme person kan optræde mere end én gang i diagrammet – for eksempel når nogen har været gift flere gange og optræder i flere familieenheder langs vejen. Dette er intentionelt, ikke en fejl.

### Vifte-diagram

Et cirkulært stamtavlediagram. Forfædre stråler ud fra den valgte person i centrum.

**Farve**-knappen i værktøjslinjen farver segmenterne efter en egenskab ved hver person: antallet af begivenheder eller noter, fødselsår, dødsår, alder, efternavn, religion eller forfaderfrekvens (hvor ofte en person optræder i diagrammet). Farvning efter efternavn bruger efternavnet fra personens fødenavn, eller det primære navn, hvis der ikke er noget fødenavn. For at fjerne farvningen skal du rydde chippen, der viser den valgte farve.

## Bevæge sig til slægtninge og udvide grene

I Forfædres træ og Vifte-diagrammet har den valgte person en chevron-knap, der åbner en menu med deres børn. I Efterkommere træet åbner den en menu med deres forældre i stedet. At vælge en person fra menuen centrerer diagrammet om dem.

I Forfædres træ, Efterkommere træ og Timeglasdiagrammet har personer i kanten af diagrammet, hvis forældre eller børn ikke vises, en chevron på den side, hvor deres gren fortsætter. Klik på den for at tilføje endnu en generation til den gren, mens den valgte person forbliver den samme. På denne måde kan du for eksempel se på alle bedsteforældre og derefter følge kun én linje længere tilbage. Udvidede grene nulstilles, når du vælger en anden person eller skifter til et andet diagram.

## Navigationskontroller

Alle diagramtyper deler en værktøjslinje med følgende knapper:

- **Hjem Person** – hop tilbage til din hjemperson
- **Tilbage** – gå tilbage til den tidligere centrerede person
- **Person Detaljer** – åbne den fulde profilside for den aktuelt centrerede person
- **Præferencer** – åbne en dialog for at justere diagram-specifikke visningsmuligheder (se nedenfor)

Alle diagrammer understøtter **pan** (klik og træk) og **zoom** (scrollhjul eller klem).

## Diagrampræferencer

**Præferencer**-dialogen (gearikon i værktøjslinjen) giver dig mulighed for at justere følgende muligheder, afhængigt af diagramtypen:

- **Maks. Forfadergenerationer** – hvor mange generationer af forfædre der skal vises
- **Maks. Efterkommergenerationer** – hvor mange generationer af efterkommere der skal vises
- **Maks. Grad af adskillelse** – for Forholdsdiagrammet, den maksimale længde af stien at søge, op til 6
- **Maks. Antal billeder vist** – begrænser profilbilleder vist i diagrammet for ydeevne
- **Navn Visningsformat** – styrer hvordan navne vises på personkort

Klik på **Nulstil** for at gendanne standardindstillingerne, eller **Luk** for at anvende dine ændringer.

Indstillinger for diagrampræferencer gemmes i browserens lokale lager, så de forbliver på tværs af sessioner på den samme enhed.

## Standard diagramtype

Den diagramtype, der vises, når du først åbner Slægtstræ-siden, kan konfigureres i [Brugerindstillinger](settings.md). Din valgte standard gælder på alle dine enheder.

## Redigering af træet

Brugere med rollen som Redaktør eller højere kan tilføje og linke personer direkte fra Forfædres træ. Se [Redigering af slægtstræet](tree-edit.md) for detaljer.
