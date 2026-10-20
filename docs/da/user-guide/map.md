# Kort

Kort-siden viser alle steder i dit slægtstræ som interaktive markører på et geografisk kort. Den er tilgængelig fra sidepanelet.

## Stedmarkører

Kun steder, der har GPS-koordinater gemt i Gramps-databasen, vises på kortet. Steder uden koordinater udelades stille og roligt. GPS-koordinater kan indstilles på stedets detaljeside (rediger stedet og udfyld felterne for bredde- og længdegrad).

!!! tip
    Hvis mange af dine steder mangler på kortet, skal du åbne en steddetaljeside og tjekke, om bredde- og længdegrad er indstillet. Du kan tilføje eller rette koordinater direkte fra stedets redigeringsvisning.

Hvert sted med koordinater vises som en markør. Klik på en markør for at åbne et resumékort, der viser stedets navn og dets tilknyttede begivenheder og personer. Klik på stedets navn i kortet for at åbne den fulde steddetaljeside.

## Søgning

Søgefeltet i øverste venstre hjørne af kortet søger, mens du skriver, og grupperer resultaterne under tre overskrifter:

- **Steder** – steder i dit slægtstræ. Ved at vælge et panorerer kortet til det og fremhæver dets markør.
- **Personer** – personer i dit slægtstræ. Ved at vælge en skifter kortet til personvisningen beskrevet [nedenfor](#following-a-person-across-the-map).
- **Eksterne** – placeringer fra [OpenStreetMap](https://www.openstreetmap.org/), for hvor som helst i verden. Ved at vælge en panorerer og zoomer kortet til den placering; det filtrerer eller ændrer ikke dine træers steder.

De eksterne resultater er også nyttige, når du tilføjer koordinater til et sted: du kan finde placeringen her for at se, hvor den er, før du indtaster dens bredde- og længdegrad.

## Følge en person på kortet

At vælge en person – fra kortets søgefelt eller med **Åbn i kort**-knappen på en persons detaljeside – viser de steder, der er knyttet til den pågældende persons begivenheder, forbundet med linjer i kronologisk rækkefølge. Små pile langs hver linje angiver rejsens retning, så du kan følge en persons liv fra fødsel til død på kortet.

Steder på en steddetaljeside har også en **Åbn i kort**-knap, som åbner kortet centreret på det sted.

## Tidslinse

Tidslinse nederst på siden filtrerer, hvilke stedmarkører der vises baseret på året for deres tilknyttede begivenheder:

- Træk håndtaget for at vælge et år.
- Kun steder knyttet til begivenheder, der falder inden for det valgte tidsvindue, vises.
- Brug dette til at spore, hvor dine forfædre levede på et bestemt tidspunkt i historien.

## Kortlag

En lagvælgerknap (stabel-lag ikon, nederst til venstre) lader dig vælge mellem to basiskort. Under dem viser den dine egne kortlag under "Dine kort" (se [Brugerdefinerede kortoverlejringer](#custom-map-overlays) og [Kortfiler for steder](#map-files-of-places)) og [Wikidata-bygninger](#wikidata-buildings) laget under "Eksterne", som hver kan tændes og slukkes.

Etiketterne for begge basiskort vises på det sprog, du har valgt i Gramps Web, hvor kortdataene har et navn på det sprog, og i det lokale navn ellers.

### Basiskort

Det standardlag, der drives af [OpenFreeMap](https://openfreemap.org) (Liberty-stil til lys tilstand, mørk stil til mørk tilstand). Dette er et moderne generelt kort, der er velegnet til at lokalisere steder.

### Historisk kort

Skifter basiskortet til [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), et fællesskabsdrevet projekt, der kortlægger verden, som den eksisterede på forskellige tidspunkter – tænk på det som en historisk modpart til OpenStreetMap.

Når det historiske kortlag er aktivt, filtrerer tidslinse også kortfliserne selv: OHM gengiver kortet, som det så ud i det valgte år, så historiske grænser, stednavne og funktioner vises i stedet for de moderne. Dette gør det muligt at se både din forfaders placering og den samtidige geografiske og politiske kontekst i en enkelt visning.

!!! note
    OpenHistoricalMap-dækning varierer efter region og periode. Områder eller epoker med sparsomme bidrag kan vise begrænsede historiske detaljer. Hvis du bemærker manglende eller unøjagtige historiske data, kan du overveje at [bidrage til OpenHistoricalMap](https://www.openhistoricalmap.org) – det er et åbent fællesskabsprojekt, som alle kan redigere.

## Brugerdefinerede kortoverlejringer

Ud over de indbyggede basiskortlag kan du gøre ethvert scannet historisk kortbillede – gemt i Gramps som et **Medie**-objekt – til en brugerdefineret overlejring, der er placeret på det live kort. Dette er nyttigt til scanninger af gamle byplaner, sognkort eller ejendomskort, som du ønsker at sammenligne direkte med moderne eller historisk geografi.

### Georeferering af et billede

1. Åbn medieobjektet for det scannede kortbillede, og skift til redigeringstilstand.
2. Åbn fanen "Kort" og klik på **Rediger koordinater**. Dette åbner en georeferering-dialog med billedet ved siden af et kort.
3. Klik på **Vælg et punkt på kortet**, og klik derefter på den placering på kortet, som et punkt på billedet skal svare til. Billedet placeres på kortet for første gang, så snart et punkt er valgt.
4. Brug **Skala**-skyderen til at ændre størrelsen på billedet, og **Opacitet**-skyderen til at se basiskortet gennem det, mens du positionerer.
5. Klik på **Justér billedet** og klik på kortet igen for at flytte billedet, så det fastgjorte punkt præcist flugter.
6. Gentag skala-, opacitet- og justeringstrinene, indtil billedet matcher den underliggende geografi, og gem det.

Bag kulisserne gemmer dette billedets hjørnekoordinater i en `map:bounds`-attribut på medieobjektet.

### Visning af overlejringer på Kort-siden

Når et medieobjekt er blevet georefereret på denne måde, bliver det automatisk tilgængeligt som et skifteligt lag på Kort-siden. Åbn lagvælgeren (stabel-lag ikon, nederst til venstre) for at vise eller skjule hver overlejring uafhængigt af basiskortet. Overlejringer listes efter medieobjektets titel.

## Kortfiler for steder

Steder kan have kortfiler knyttet som medieobjekter – for eksempel grænserne for et sogn, et distrikt eller en ejendom, eller en rute. Understøttede filtyper er KML (`.kml`), GeoJSON (`.geojson`) og GPX (`.gpx`) filer.

Når du vælger et sted på kortet, tegnes dets kortfiler oven på kortet ved hjælp af de farver, der er gemt i filen, hvor de har dem. Dette fungerer også for steder uden koordinater: kortet zoomer derefter til det område, der dækkes af filerne. Mens stedet er valgt, listes dets filer i lagvælgeren under "Dine kort", hvor du kan slukke for hver af dem.

For at tilføje en kortfil til et sted, tilføj det til stedets galleri som enhver anden [mediefil](media.md).

## Wikidata-bygninger

"Wikidata-bygninger"-laget viser bygninger registreret i [Wikidata](https://www.wikidata.org/), såsom kirker, gårde eller byhuse. Det er som standard slået fra og kan tændes i lagvælgeren under "Eksterne". Bygninger vises kun, når kortet er zoomet ind langt nok. Når tidslinse er aktiv, vises kun bygninger, der eksisterede på det valgte tidspunkt.

Klik på en bygning for at se dens detaljer fra Wikidata, såsom hvornår den blev bygget eller nedrevet, dens adresser, beboere og ejere.

### Gemme en bygning som et sted

Brugere, der kan tilføje objekter, ser en **Gem som sted**-knap i bygningens detaljer. Den åbner formularen for et nyt sted, forudfyldt med bygningens navn på dit sprog, en stedtype (`Gård` for gårde, ellers `Bygning`), dens koordinater og et link til Wikidata-elementet. Udfyld formularen, for eksempel ved at vælge det omgivende sted, og gem det.

Hvis et sted i dit træ er på samme placering som bygningen, læses knappen **Åbn gemt sted** i stedet og viser det sted.

!!! info
    Serveradministratoren kan fjerne Wikidata-bygninger-laget med `mapWikidata`-muligheden i [frontend-konfigurationen](../install_setup/frontend-config.md).
