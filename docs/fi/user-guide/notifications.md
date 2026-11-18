# Ilmoitukset

Yläosan sovellusvalikossa oleva kello avaa ilmoitukset. Kellossa oleva merkki näyttää lukemattomien ilmoitusten määrän. Valikossa luetellaan käynnissä olevat tehtävät ja viimeisimmät ilmoitukset; **Näytä kaikki** avaa täydellisen ilmoituslokin. Pienillä näytöillä kello avaa lokin suoraan.

Ilmoitukset koskevat:

- **Muutoksia muilta käyttäjiltä.** Kun muut käyttäjät muuttavat puuta, kun käytät Gramps Webiä, ilmoitus kertoo, kuka muutti mitä, esim. "Muokkaa henkilöä" tai "12 muutosta". Napsauta sitä avataksesi muutoksen [muutoshistoriassa](revisions.md). Muutokset, joilla ei ole Gramps Web -käyttäjää, kuten muutokset, jotka on tehty suoraan jaettuun tietokantaan Gramps Desktopilla, näytetään ilman nimeä. Tämä on saatavilla vain käyttäjille, jotka voivat nähdä muutoshistorian (jäsenet ja korkeammat).
- **Taustatehtävät** – kuten tuonnit ja viennit, raporttien luominen, OCR-tekstintunnistus, tietokannan päivitykset, monien objektien poistaminen tai muokkaaminen sekä hakemistojen uudelleenrakentaminen – näyttävät niiden tilan (esim. odottaa, aloitettu, käynnissä) ja ilmoittavat sinulle, kun ne valmistuvat tai epäonnistuvat.
- **Virheet**, jotka tapahtuivat istuntosi aikana – epäonnistuneet API-pyynnöt, taustatehtävien virheet, tallennusvirheet tai selainkohtaiset virheet.

Valmiit viennit ja media-arkistot voidaan ladata niiden ilmoituksesta, myös sen jälkeen, kun olet poistunut [Vienti-sivulta](../administration/export.md).

Jotkut ilmoitukset sisältävät jäsenneltyä tietoa, kuten epäonnistuneen tehtävän virheilmoituksen. Napsauttamalla tällaista merkintää ilmoituslokissa avautuu dialogi, jossa on erittely virhetiedoista ja **Kopioi JSON** -painike. Tämä on hyödyllistä virheiden ilmoittamisessa, sillä JSON sisältää tarkat virhetiedot palvelimelta.

Käytä **Tyhjennä kaikki** ilmoituslokissa hylätäksesi kaikki ilmoitukset.

Tehtävät, jotka muuttavat koko puuta, kuten tuonti, palautus, kaikkien objektien poistaminen tai hakemiston uudelleenrakentaminen, eivät voi olla käynnissä samanaikaisesti. Jos aloitat yhden, kun toinen on käynnissä, viesti ilmoittaa, että toinen tehtävä on jo käynnissä tällä puulla, ja käynnissä oleva tehtävä näytetään edistymisensä kanssa.

!!! huomautus
    Ilmoitukset tallennetaan vain muistiin ja ne tyhjennetään, kun lataat sivun uudelleen. Gramps Web tarkistaa muutoksia muilta käyttäjiltä vain, kun se on avoinna, joten poissa ollessasi tehdyt muutokset eivät tule näkyviin; katso [Muutoshistoria](revisions.md) niitä varten.
