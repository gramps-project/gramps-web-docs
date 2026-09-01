# Kort

Kort-siden viser alle steder i dit slægtstræ som interaktive markører på et geografisk kort. Den er tilgængelig fra sidepanelet.

## Stedmarkører

Kun steder, der har GPS-koordinater gemt i Gramps-databasen, vises på kortet. Steder uden koordinater udelades stille og roligt. GPS-koordinater kan indstilles på stedets detaljeside (rediger stedet og udfyld felterne for breddegrad og længdegrad).

!!! tip
    Hvis mange af dine steder mangler på kortet, skal du åbne en steddetaljeside og kontrollere, om breddegrad og længdegrad er indstillet. Du kan tilføje eller rette koordinater direkte fra stedets redigeringsvisning.

Hvert sted med koordinater vises som en markør. Klik på en markør for at åbne et resumékort, der viser stednavnet og dets tilknyttede begivenheder og personer. Klik på stednavnet i kortet for at åbne den fulde steddetaljeside.

## Søgning

Søgefeltet i øverste venstre hjørne af kortet søger, mens du skriver, og grupperer resultaterne under tre overskrifter:

- **Steder** – steder i dit slægtstræ. Ved at vælge et panoreres kortet til det og fremhæver dets markør.
- **Personer** – personer i dit slægtstræ. Ved at vælge en skifter kortet til personvisningen beskrevet [nedenfor](#following-a-person-across-the-map).
- **Eksterne** – steder fra [OpenStreetMap](https://www.openstreetmap.org/), for hvor som helst i verden. Ved at vælge en panoreres og zoomes kortet til den pågældende placering; det filtrerer eller ændrer ikke dit slægtstræs steder.

De eksterne resultater er også nyttige, når du tilføjer koordinater til et sted: du kan slå placeringen op her for at se, hvor den er, før du indtaster dens breddegrad og længdegrad.

## Følge en person på kortet

At vælge en person – fra kortets søgefelt eller med **Åbn i kort**-knappen på en persons detaljeside – viser de steder, der er forbundet med den pågældende persons begivenheder, forbundet med linjer i kronologisk rækkefølge. Små pile langs hver linje angiver rejsens retning, så du kan følge en persons liv fra fødsel til død på kortet.

Steder på en steddetaljeside har også en **Åbn i kort**-knap, som åbner kortet centreret på det sted.

## Tidslinse

Tidslinse nederst på siden filtrerer, hvilke stedmarkører der vises baseret på året for deres tilknyttede begivenheder:

- Træk håndtaget for at vælge et år.
- Kun steder, der er knyttet til begivenheder, der falder inden for det valgte tidsvindue, vises.
- Brug dette til at spore, hvor dine forfædre boede på et bestemt tidspunkt i historien.

## Kortlag

En lagvælgerknap (stak-lag ikon, nederst til venstre) lader dig vælge mellem to grundkort:

### Grundkort

Det standardlag, drevet af [OpenFreeMap](https://openfreemap.org) (Liberty-stil for lys tilstand, mørk stil for mørk tilstand). Dette er et moderne generelt kort, der er velegnet til at finde steder.

### Historisk kort

Skifter grundkortet til [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), et fællesskabsdrevet projekt, der kortlægger verden, som den eksisterede på forskellige tidspunkter – tænk på det som en historisk modpart til OpenStreetMap.

Når det historiske kortlag er aktivt, filtrerer tidslinse også kortfliserne selv: OHM gengiver kortet, som det så ud i det valgte år, så historiske grænser, stednavne og funktioner vises i stedet for de moderne. Dette gør det muligt at se både din forfaders placering og den samtidige geografiske og politiske kontekst i en enkelt visning.

!!! note
    OpenHistoricalMap-dækning varierer efter region og periode. Områder eller epoker med sparsomme bidrag kan vise begrænset historisk detalje. Hvis du bemærker manglende eller unøjagtige historiske data, overvej at [bidrage til OpenHistoricalMap](https://www.openhistoricalmap.org) – det er et åbent fællesskabsprojekt, som alle kan redigere.

## Brugerdefinerede kortoverlejringer

Ud over de indbyggede grundlag kan du gøre ethvert scannet historisk kortbillede – gemt i Gramps som et **Medie** objekt – til en brugerdefineret overlejring, der er placeret på det live kort. Dette er nyttigt til scanninger af gamle byplaner, sognkort eller ejendomskort, som du ønsker at sammenligne direkte med moderne eller historisk geografi.

### Georeferencering af et billede

1. Åbn medieobjektet for det scannede kortbillede og skift til redigeringstilstand.
2. Åbn fanen "Kort" og klik på **Rediger koordinater**. Dette åbner en georeferenceringsdialog med billedet ved siden af et kort.
3. Klik på **Vælg et punkt på kortet**, og klik derefter på den placering på kortet, som et punkt på billedet skal svare til. Billedet placeres på kortet for første gang, så snart et punkt er valgt.
4. Brug **Skala**-skyderen til at ændre størrelsen på billedet, og **Opacitet**-skyderen til at se grundkortet igennem, mens du positionerer.
5. Klik på **Justér billedet** og klik på kortet igen for at flytte billedet, så det fastgjorte punkt præcist flugter.
6. Gentag skala-, opacitet- og justeringstrinene, indtil billedet matcher den underliggende geografi, og gem derefter.

Bag kulisserne gemmes billedets hjørnekoordinater i en `map:bounds` attribut på medieobjektet.

### Visning af overlejringer på Kort-siden

Når et medieobjekt er blevet georefereret på denne måde, bliver det automatisk tilgængeligt som et skiftbart lag på Kort-siden. Åbn lagvælgeren (stak-lag ikon, nederst til venstre) for at vise eller skjule hver overlejring uafhængigt af grundkortet. Overlejringer listes efter medieobjektets titel.
