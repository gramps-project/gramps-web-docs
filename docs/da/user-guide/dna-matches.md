# Arbejde med DNA-matcher

DNA-matcher er segmenter af DNA, der er ens mellem to individer, identificeret ved tilstedeværelsen af markører, såkaldte SNP'er (akronymet for single nucleotide polymorphisms, udtales "snips").

For at få adgang til disse data skal du have adgang til en DNA-test, der er uploadet til en matchende database, som gør det muligt at se DNA-segmentmatchdata (f.eks. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web udfører ikke selve matchningen, da det kun har adgang til de data, du uploader.

## Indtastning af DNA-matchdata

For at indtaste DNA-matchdata skal du have [redigeringsrettigheder](../install_setup/users.md), da dataene gemmes som en note i Gramps-databasen. DNA-visningen, der er tilgængelig fra hovedmenuen, giver en praktisk måde at indtaste disse data i det rigtige format.

For at indtaste et nyt match skal du klikke på + knappen i nederste højre hjørne. I den dialog, der åbner, skal du vælge de to individer. Bemærk, at "Første person" og "Anden person" behandles forskelligt: matchen gemmes som en association fra den første til den anden person. Kun den første person vil være vælgbar for DNA-matchvisningen og kromosombrowseren. Typisk er den første person den, hvis DNA-test du har adgang til, og den anden person er en mere fjern slægtning.

Hvis den anden person ikke er i databasen, skal du først oprette den ved at bruge "Opret person" knappen i det øverste højre hjørne af brugergrænsefladen. Når du har oprettet personen, kan du vende tilbage til DNA-matchvisningen og vælge den nyoprettede person.

Næste skridt er at indsætte de rå data i tekstfeltet. Dataene skal være en komma- eller tabulatorsepareret tabel over matcher, der typisk indeholder kromosomnummeret, start- og slutpositionen for matchen, antallet af SNP'er i matchen og længden af matchen i enheder af centimorganer (cM). Du kan også trække og slippe en fil med matchdata ind i tekstfeltet.

Et minimalt eksempel på en sådan tabel er:

```csv
Kromosom,Start placering,Slut placering,Centimorganer,SNP'er
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Hvis formatet er gyldigt, vises en forhåndsvisning under tekstfeltet som en tabel.

Til sidst skal du klikke på "Gem" knappen for at gemme matchen i databasen.

## Visning af DNA-matchdata

DNA-matchvisningen har en dropdown, der gør det muligt at vælge hver person i databasen, der har en tilknyttet DNA-match. Når en person er valgt, listes deres matcher i en tabel: navnet på matchen, deres forhold til den valgte person, den samlede længde af delt DNA i centimorganer (cM), antallet af delte segmenter og længden af det største af disse segmenter.

For matcher, der allerede er placeret i træet, viser forholds kolonnen det forhold, der er registreret i træet (automatisk bestemt fra Gramps-databasen). For matcher, der ikke er relateret til den valgte person i træet, viser det forholdet estimeret ud fra det delte DNA, markeret med "≈".

Klik på en match for at åbne dens side, med et resumé af det delte DNA, [forholdsestimatet](#relationship-estimate), et diagram over forholdet i træet og listen over segmenter. Hvert segment viser, om det er på den paternale eller maternelle side. Siden kan enten indtastes manuelt (ved at angive et `P` for paternal eller `M` for maternal i en kolonne navngivet `Side` i de rå data) eller bestemmes automatisk fra den seneste fælles forfader. Download-knappen ved siden af segmenterne gemmer dem som en CSV-fil i det format, som matchdialogen accepterer.

## Forholdsestimat

Delt DNA er ikke bevis på et specifikt forhold: mængden af DNA, to slægtninge deler, varierer meget, og forskellige forhold overlapper. Gramps Web viser derfor et udvalg af mulige forhold med deres sandsynligheder, beregnet ud fra antallet og længderne af de delte segmenter (kræver Gramps Web API 3.26 eller nyere).

Forhold er grupperet efter deres *grad*:

- **Forælder eller barn** og **Fuld søskende** vises for sig.
- **Slægtning af grad 2** inkluderer halvsøskende, bedsteforældre og børnebørn samt tanter, onkler, niecer og nevøer.
- **Slægtning af grad 3** inkluderer første fætre, oldeforældre, grandtanter og grandonkler samt halvtanter og halvonkler.
- Hver yderligere grad er cirka en generation længere væk, f.eks. første fætre en gang fjernet er grad 4, og anden fætre er grad 5. Grad 9 og derover grupperes som "9+".

Forhold med samme grad deler i gennemsnit omtrent den samme mængde DNA, så DNA alene kan ikke skelne dem. Brug alderen på personerne til at beslutte mellem dem – en 30-årig slægtning af grad 2 til en 60-årig er mere sandsynligvis en niece end en bedsteforælder.

Estimatet er mest pålideligt for nære slægtninge. For fjerne forhold deler matcher kun få segmenter, og sandsynlighederne spreder sig over flere grader.

### Tjekke træet mod DNA'et

Hvis matchen er placeret i træet, kontrollerer Gramps Web, om det delte DNA passer til det forhold, der er registreret der. Hvis DNA'et er meget usandsynligt for det forhold, vises et advarselsikon i matchtabelen og en advarsel på matchens side. Tallet i parentes, f.eks. "1 : 500", sammenligner, hvor sandsynligt DNA'et er for det registrerede forhold med, hvor sandsynligt det er for det mest sandsynlige forhold.

En advarsel er en grund til at se nærmere på, ikke bevis på en fejl. Almindelige årsager er:

- en fejl i træet, såsom en forkert forælder,
- en fejlagtig forældretilknytning, f.eks. en ukendt adoption eller en anden biologisk far,
- ufuldstændige matchdata, for eksempel hvis kun segmenter over en høj tærskel blev kopieret fra testtjenesten,
- forhold gennem mere end én linje, f.eks. personer, der er relateret gennem både deres mor og far ("pedigree collapse"), som deler mere DNA end forventet.

Forhold, der ikke er ved fødsel, såsom gennem en adoption, bliver ikke kontrolleret.

## Redigering af en match

For at redigere en match skal du åbne dens side og klikke på redigeringsknappen eller trykke på `e`. Bemærk, at du kan ændre de rå data, men ikke de individer, der er tilknyttet matchen – du skal slette matchen og oprette en ny, hvis du vil ændre individerne.

## Private matcher

Dialogerne til at tilføje og redigere en match har en **Privat** switch. En privat match, inklusive dens segmenter, er skjult for brugere, der ikke kan se private optegnelser. Private matcher er markeret med en lås for alle andre. Se [Private optegnelser](privacy.md) for mere om privatliv.

## Arbejde med matchdata i Gramps Desktop

DNA-matchdata gemmes som en note i Gramps-databasen. Formatet er kompatibelt med 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
tilgængelig for Gramps Desktop. Dens wiki-side indeholder flere detaljer om, hvordan man får dataene, hvordan man fortolker dem, og hvordan man indtaster dataene i Gramps.

!!! info
    Gramps Web API v2.8.0 introducerede nogle ændringer for at acceptere et bredere udvalg af rå DNA-matchdata, som endnu ikke er tilgængelige i Gramps Desktop Addon. Gramps Desktop Addon vil blive opdateret i fremtiden for at understøtte de samme formater.
