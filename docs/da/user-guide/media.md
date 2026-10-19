Der er to måder at tilføje en ny mediefil (et billede, lydfil, videofil eller en anden fil), og eksisterende mediefiler kan linkes til nye objekter, når de oprettes:

## Tilføj en ny selvstændig mediefil

For at tilføje en selvstændig mediefil, klik på + ikonet i den øverste app-bar og vælg "Medieobjekt".

Klik på "vælg en fil" for at vælge en fil fra din computer. På en mobil enhed vil et klik på denne knap give dig mulighed for direkte at tage et billede med enhedens kamera.

Valgfrit,

- indtast en beskrivelse af mediefilen under "titel"
- indtast en dato
- sæt mediefilen som privat (hvilket gør den synlig kun for brugere med tilstrækkelig autorisation)

Klik på "tilføj" for at uploade filen og oprette medieobjektet.

## Tilføj en ny mediefil og link den til et andet objekt

Følgende objekttyper i Gramps kan have medieobjekter knyttet: personer, familier, begivenheder, steder, kilder og citater.

I detaljevisningen af ethvert objekt, klik på den blå redigeringsknap i nederste højre hjørne (hvis du ikke kan se den, har din bruger ikke redigeringsrettigheder). Klik på "galleri"-fanen og klik på den blå + knap.

En dialogboks åbnes, som tilbyder de samme felter som beskrevet i den foregående sektion. Klik på "gem" for at uploade filen, tilføje et nyt medieobjekt og linke det til det viste objekt.

## Link eksisterende mediefiler, når du opretter et objekt

Når du opretter en ny person, familie, begivenhed, sted, kilde eller citation, har formularen en "Medie"-sektion. Her kan du vælge en eller flere eksisterende medieobjekter, som er knyttet til det nye objekt, når du gemmer det.

Når du opretter en person sammen med deres fødsels- og dødsbegivenheder, er de valgte medieobjekter kun knyttet til personen, ikke til begivenhederne.

## Tekstgenkendelse (OCR)

Hvis serveradministratoren har aktiveret OCR-understøttelse, vises en "Tekstgenkendelse"-knap under billedet i detaljevisningen af et medieobjekt.

Klik på "Tekstgenkendelse", vælg sproget for den tekst, der vises i billedet, og klik derefter på "Kør". Billedet behandles med [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), og den genkendte tekst vises nedenfor.

Hvis din bruger har redigeringsrettigheder, klik på "Gem som note" for at oprette en ny note (af typen "Transkript"), der indeholder den genkendte tekst og linke den til medieobjektet.

!!! tip
    OCR-nøjagtighed afhænger i høj grad af billedkvalitet og det valgte sprog. Hvis resultatet ser forkert ud, så prøv et andet sprog – for eksempel kræver historiske tyske dokumenter ofte Fraktur-varianten frem for almindelig tysk.
