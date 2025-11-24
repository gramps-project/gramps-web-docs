# Arbejde med DNA-matcher

DNA-matcher er segmenter af DNA, der er enige mellem to individer, identificeret ved tilstedeværelsen af markører, såkaldte SNP'er (akronymet for single nucleotide polymorphisms, udtales "snips").

For at opnå disse data skal du have adgang til en DNA-test, der er uploadet til en matchende database, som gør det muligt at se DNA-segmentmatchdata (f.eks. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web udfører ikke selve matchningen, da det kun har adgang til de data, du uploader.

## Indtastning af DNA-matchdata

For at indtaste DNA-matchdata skal du have [redigeringsrettigheder](../install_setup/users.md), da dataene gemmes som en note i Gramps-databasen. DNA-visningen, der er tilgængelig fra hovedmenuen, giver en bekvem måde at indtaste disse data i det rigtige format.

For at indtaste en ny match skal du klikke på + knappen i nederste højre hjørne. I den dialog, der åbner, skal du vælge de to individer. Bemærk, at "Første person" og "Anden person" behandles forskelligt: matchen gemmes som en association fra den første til den anden person. Kun den første person vil være vælgbar for DNA-matchvisningen og kromosombrowseren. Typisk er den første person den, hvis DNA-test du har adgang til, og den anden person er en mere fjern slægtning.

Hvis den anden person ikke er i databasen, skal du først oprette den ved at bruge knappen "Opret person" i øverste højre hjørne af brugergrænsefladen. Når du har oprettet personen, kan du vende tilbage til DNA-matchvisningen og vælge den nyoprettede person.

Næste skridt er at indsætte de rå data i tekstfeltet. Dataene skal være en komma- eller tabulatorsepareret tabel over matcher, der typisk indeholder kromosomnummeret, start- og slutpositionen for matchen, antallet af SNP'er i matchen og længden af matchen i enheder af centimorgans (cM). Du kan også trække og slippe en fil med matchdata ind i tekstfeltet.

Et minimalt eksempel på en sådan tabel er:

```csv
Kromosom,Start placering,Slut placering,Centimorgans,SNP'er
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Hvis formatet er gyldigt, vises en forhåndsvisning under tekstfeltet som en tabel.

Til sidst skal du klikke på "Gem" knappen for at gemme matchen i databasen.

## Visning af DNA-matchdata

DNA-matchvisningen har en dropdown, der gør det muligt at vælge hver person i databasen, der har en tilknyttet DNA-match. Når en person er valgt, vises DNA-matchdataene i en tabel under dropdown-menuen. Den viser navnet på den person, som matchen er tilknyttet, relationen til den valgte person i dropdown-menuen (automatisk bestemt fra Gramps-databasen), den samlede længde af delt DNA i centimorgans (cM), antallet af delte segmenter og længden af det største af disse segmenter.

Når du klikker på en individuel match, åbner det en detaljeside, der viser alle segmenterne og om matchen er på den maternelle eller paternelle side. Denne information kan enten indtastes manuelt (ved at angive et `P` for paternal eller `M` for maternal i en kolonne kaldet `Side` i de rå data) eller automatisk bestemmes af Gramps baseret på den seneste fælles forfader.

## Redigering af en match

Du kan redigere en match ved at klikke på blyantknappen i nederste højre hjørne i matchdetaljevisningen. Dette åbner en lignende dialog som ved oprettelse af en ny match, men med dataene forudfyldt. Bemærk, at du kan ændre de rå data, men ikke de individer, der er tilknyttet matchen – du skal slette matchen og oprette en ny, hvis du vil ændre individerne.

## Arbejde med matchdata i Gramps Desktop

DNA-matchdataene gemmes som en note i Gramps-databasen. Formatet er kompatibelt med 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
tilgængelig for Gramps Desktop. Dens wiki-side indeholder flere detaljer om, hvordan man får dataene, hvordan man fortolker dem, og hvordan man indtaster dataene i Gramps.

!!! info
    Gramps Web API v2.8.0 introducerede nogle ændringer for at acceptere et bredere udvalg af rå DNA-matchdata, som endnu ikke er tilgængelige i Gramps Desktop Addon. Gramps Desktop Addon vil blive opdateret i fremtiden for at understøtte de samme formater.
