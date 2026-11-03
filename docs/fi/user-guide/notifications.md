# Ilmoitukset

**Ilmoitukset** on sivupalkin kohde, jossa on kellokuvake. Kun virheitä on tapahtunut tai taustatehtäviä on käynnissä, merkki näyttää lukemattomien ilmoitusten määrän. Napsauta sitä avataksesi ilmoituslokin.

Ilmoituslokilla on kaksi tarkoitusta:

- Se on kirjaus virheistä, jotka tapahtuivat istuntosi aikana – epäonnistuneet API-pyynnöt, taustatehtävien virheet, tallennusvirheet tai selainkohtaiset virheet.
- Se seuraa pitkään kestäviä taustatehtäviä – kuten tuontia ja vientiä, raporttien luomista, OCR-tekstintunnistusta, tietokannan päivityksiä, monien objektien poistamista ja hakemiston uudelleenrakentamista – näyttäen niiden tilan (esim. odottaa, aloitettu, käynnissä) ja ilmoittaen sinulle, kun ne valmistuvat tai epäonnistuvat.

Jokainen merkintä näyttää lyhyen viestin, lähteen (Verkko, Tehtävä, Tallennus tai Selain) ja aikaleiman. Valmiit tehtävät lukevat "Tehtävä suoritettu" tai "Tehtävä epäonnistui".

Jotkut ilmoitukset sisältävät rakenteellista tietoa, kuten epäonnistuneen tehtävän virheilmoituksen. Napsauttamalla tällaista merkintää avautuu dialogi, jossa on erittely virheaineistosta ja **Kopioi JSON** -painike. Tämä on hyödyllistä, kun ilmoitat virheestä, sillä JSON sisältää tarkat virhetiedot palvelimelta.

Käytä **Tyhjennä kaikki** poistaaksesi kaikki ilmoitukset.

Tehtävät, jotka muuttavat koko puun, kuten tuonti, palautus, kaikkien objektien poistaminen tai hakemiston uudelleenrakentaminen, eivät voi käynnistyä samanaikaisesti. Jos aloitat yhden, kun toinen on käynnissä, viesti ilmoittaa, että toinen tehtävä on jo käynnissä tällä puulla, ja käynnissä oleva tehtävä näytetään sen edistymisen kanssa.

!!! huomautus
    Ilmoitukset tallennetaan vain muistiin ja ne tyhjennetään, kun lataat sivun uudelleen.
