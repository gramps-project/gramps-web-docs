Der er to måder at tilføje en ny mediefil (et billede, lydfil, videofil eller enhver anden fil), og eksisterende mediefiler kan linkes til nye objekter, når de oprettes:

## Tilføj en ny selvstændig mediefil

For at tilføje en selvstændig mediefil, klik på + ikonet i den øverste app-bar og vælg "Medieobjekt".

Klik på "vælg en fil" for at vælge en fil fra din computer. På en mobil enhed vil klik på denne knap give dig mulighed for direkte at tage et billede med enhedens kamera.

Valgfrit,

- indtast en beskrivelse af mediefilen under "titel"
- indtast en dato
- indstil mediefilen som privat (hvilket gør den synlig kun for brugere med tilstrækkelig autorisation)

Klik på "tilføj" for at uploade filen og oprette medieobjektet.

## Tilføj en ny mediefil og link den til et andet objekt

Følgende objekttyper i Gramps kan have medieobjekter knyttet: personer, familier, begivenheder, steder, kilder og citater.

I detaljevisningen af ethvert objekt, klik på den blå redigeringsknap i nederste højre hjørne (hvis du ikke kan se den, har din bruger ikke redigeringsrettigheder). Klik på "galleri"-fanen og klik på den blå + knap.

Et dialogvindue åbnes, der tilbyder de samme felter som beskrevet i den foregående sektion. Klik på "gem" for at uploade filen, tilføje et nyt medieobjekt og linke det til det viste objekt.

## Profilbilleder

Det første billede i en persons galleri bruges som deres profilbillede. I redigeringstilstand er det markeret med et "Profilbillede" badge. For at bruge et andet billede, flyt det til den første position med pilknapperne på galleri-miniaturebillederne, eller træk det derhen: med musen, tryk på miniaturebilledet og flyt det; på en berøringsskærm, tryk og hold det, indtil det bliver løftet.
Hvis en person endnu ikke har noget medie, viser redigeringstilstand en **Tilføj profilbillede** pladsholder i stedet. Klik på det for at uploade en ny mediefil eller vælge en eksisterende.

## Link eksisterende mediefiler, når du opretter et objekt

Når du opretter en ny person, familie, begivenhed, sted, kilde eller citat, har formularen en "Medie" sektion. Her kan du vælge en eller flere eksisterende medieobjekter, som er knyttet til det nye objekt, når du gemmer det.

Når du opretter en person sammen med deres fødsels- og dødsbegivenheder, er de valgte medieobjekter kun knyttet til personen, ikke til begivenhederne.

## Gennemse medier

Medievisningen viser medieobjekterne som et galleri af miniaturebilleder eller som en liste; valget huskes i din browser. Ligesom de andre [listevisninger](lists.md) kan den sorteres (inklusive efter dato), filtreres og bruges til at vælge og slette medier i bulk.

Klik på en flise i galleriet for at åbne mediet i lysboksen. Brug piletasterne, swipe, eller klik på pilknapperne for at træde igennem de filtrerede og sorterede resultater, på tværs af sider. **Detaljer** knappen i lysboksen åbner medieobjektets side. Klik på en række i liste-layoutet åbner medieobjektets side direkte.

Videoer vises med et miniaturebillede og en afspilningsknap. Lyd- og videofiler kan afspilles på medieobjektets side, i lysboksen, i [blogindlæg](blog.md) og når de er indlejret i noter.

## Tekstgenkendelse (OCR)

Hvis serveradministrator har aktiveret OCR-support, vises en "Tekstgenkendelse" knap under billedet i en medieobjekts detaljevisning.

Klik på "Tekstgenkendelse", vælg sproget for teksten vist i billedet, og klik derefter på "Kør". Billedet behandles med [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) og den genkendte tekst vises nedenfor.

Hvis din bruger har redigeringsrettigheder, klik på "Gem som note" for at oprette en ny note (af typen "Transkript") indeholdende den genkendte tekst og linke den til medieobjektet.

!!! tip
    OCR-nøjagtighed afhænger i høj grad af billedkvalitet og det valgte sprog. Hvis resultatet ser forkert ud, så prøv et andet sprog – for eksempel kræver historiske tyske dokumenter ofte Fraktur-varianten frem for almindelig tysk.
