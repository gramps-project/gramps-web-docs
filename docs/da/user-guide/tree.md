# Slægtstræ

Slægtstræ-siden er tilgængelig fra sidepanelet og viser interaktive diagrammer centreret om en valgt person. Fem diagramtyper er tilgængelige via faner øverst på siden.

## Valg af startperson

Alle diagrammer starter fra den person, der aktuelt er valgt i træet (vist i værktøjslinjen). Den aktuelt centrerede person er fremhævet med en skygge. Brug **Hjem Person**-knappen for at hoppe tilbage til din hjemperson, eller **Tilbage**-knappen for at vende tilbage til den tidligere viste person. Klik på en persons kort i ethvert diagram for at recenterere diagrammet på den person.

Hvis der ikke er indstillet nogen hjemperson, tilbyder siden en **Indstil Hjem Person**-knap for at søge efter og vælge en direkte. Hvis træet endnu ikke indeholder nogen personer, ser brugere med Editor-rollen eller højere i stedet en **Ny Person**-knap – den første person, der oprettes i et tomt træ, bliver automatisk din hjemperson, så diagrammet vises straks.

## Diagramtyper

### Forfædres træ

Et stamtavlediagram, der viser forfædrene til den valgte person. Forældre vises til venstre (eller højre, afhængigt af layoutet), bedsteforældre længere ude, og så videre.

### Efterkommere træ

Viser efterkommerne til den valgte person – børn, børnebørn og så videre.

### Timeglasdiagram

Kombinerer forfædre ovenfor og efterkommere nedenfor den valgte person i en enkelt visning.

### Forholdsdiagram

Viser forholdsvejen mellem to personer. Den valgte person er den ene ende; klik på en anden person i diagrammet for at sætte den anden ende og vise den korteste forholdsvej mellem dem.

!!! note
    Den samme person kan optræde mere end én gang i diagrammet – for eksempel når nogen har været gift flere gange og optræder i flere familieenheder langs vejen. Dette er intentionelt, ikke en fejl.

### Fan-diagram

Et cirkulært stamtavlediagram. Forfædre stråler ud fra den valgte person i midten.

## Bevæge sig til slægtninge og udvide grene

I Forfædres træ og Fan-diagrammet har den valgte person en chevron-knap, der åbner en menu med deres børn. I Efterkommere træet åbner den i stedet en menu med deres forældre. Valg af en person fra menuen centrerer diagrammet på dem.

I Forfædres træ, Efterkommere træ og Timeglasdiagrammet har personer i kanten af diagrammet, hvis forældre eller børn ikke vises, en chevron på den side, hvor deres gren fortsætter. Klik på den for at tilføje endnu en generation til den gren, mens den valgte person forbliver den samme. På den måde kan du for eksempel se på alle bedsteforældre og derefter følge kun én linje længere tilbage. Udvidede grene nulstilles, når du vælger en anden person eller skifter til et andet diagram.

## Navigationskontroller

Alle diagramtyper deler en værktøjslinje med følgende knapper:

- **Hjem Person** – hop tilbage til din hjemperson
- **Tilbage** – gå tilbage til den tidligere centrerede person
- **Persondetaljer** – åbne den fulde profilside for den aktuelt centrerede person
- **Præferencer** – åbne en dialog for at justere diagram-specifikke visningsmuligheder (se nedenfor)

Alle diagrammer understøtter **pan** (klik og træk) og **zoom** (scrollhjul eller klem).

## Diagrampræferencer

Dialogen **Præferencer** (gearikon i værktøjslinjen) giver dig mulighed for at justere følgende muligheder, afhængigt af diagramtypen:

- **Maks. Forfædregenerationer** – hvor mange generationer af forfædre der skal vises
- **Maks. Efterkommergenerationer** – hvor mange generationer af efterkommere der skal vises
- **Maks. Grad af adskillelse** – for Forholdsdiagrammet, den maksimale længde af stien, der skal søges
- **Maks. Antal viste billeder** – begrænser profilbilleder vist i diagrammet for ydeevne
- **Navnevisningsformat** – styrer hvordan navne vises på personkort

Klik på **Nulstil** for at gendanne standardindstillingerne, eller **Luk** for at anvende dine ændringer.

Indstillinger for diagrampræferencer gemmes i browserens lokale lager, så de forbliver på tværs af sessioner på den samme enhed.

## Standard diagramtype

Den diagramtype, der vises, når du først åbner Slægtstræ-siden, kan konfigureres i [Brugerindstillinger](settings.md). Din valgte standard gælder på alle dine enheder.

## Redigering af træet

Brugere med Editor-rollen eller højere kan tilføje og linke personer direkte fra Forfædres træ. Se [Redigering af slægtstræet](tree-edit.md) for detaljer.
