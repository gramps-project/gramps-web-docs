# Tuo mediasisältöjä

Jos olet [tuonut sukupuun](import.md) ja tarvitset vastaavien mediasisältöjen lataamista, käytä **Tuo mediasisältöjä** [Tuontisivulla](import.md), sukupuun tuonnin alapuolella. Se odottaa ZIP-tiedostoa, joka sisältää puuttuvat mediasisällöt. Lataus on mahdollista vain, kun puu sisältää mediasisältöjä, koska tiedostot yhdistetään olemassa oleviin mediasisältöihin – sukupuutiedosto viittaa vain sen mediasisältöihin, joten tuo se ensin.

Tiedostot yhdistetään puusi mediasisältöihin yhdellä kahdesta tavalla:

- **Tarkistussumman mukaan.** Mediasisällöille, joilla on tarkistussumma – kuten on tapauksessa Gramps Desktopista tuoduissa puissa – käytetään tiedostoa, jonka tarkistussumma vastaa, riippumatta sen nimestä tai ZIP-tiedoston kansiorakenteesta. Tämä toimii vain, jos Gramps-tietokannan tarkistussummat ovat oikein, mikä varmistuu tarkistus- ja korjaustyökalun suorittamisella.
- **Polun tai tiedoston nimen mukaan.** Mediasisällöt ilman tarkistussummaa – kuten on tyypillistä GEDCOM-tuonnin jälkeen – yhdistetään mediasisällössä tallennettuun suhteelliseen polkuun. Jos ZIP-tiedostossa ei ole tiedostoa, jolla on tuo polku, ne yhdistetään pelkästään tiedoston nimen mukaan, unohtaen isot ja pienet kirjaimet (koska Gramps Web API 3.26). Tämä toimii myös absoluuttisten polkujen kanssa muista ohjelmista, kuten `C:\Users\...\Family\grandpa.jpg`, joten voit yksinkertaisesti laittaa kaikki tiedostot ZIP-tiedostoon. Tiedoston nimeä käytetään vain, jos se on ainutlaatuinen, sekä ZIP-tiedostossa että mediasisällöissä, joilla ei vielä ole tiedostoa.

Latauksen jälkeen tulos kertoo, kuinka monelle mediasisällölle tiedosto löytyi, ja listaa ne, joilta ZIP-tiedostosta puuttui tiedosto, niiden Gramps ID:n ja tallennetun polun kanssa. Käytä tätä luetteloa löytääksesi puuttuvat tiedostot, ja lataa sitten toinen ZIP-tiedosto, jossa on vain nämä – tiedostot, jotka ovat jo palvelimella, eivät vaikuta.

Jos useilla mediasisällöillä on sama tiedostonimi eri kansioissa, tiedostonimen mukaan yhdistäminen ei toimi niille. Joko luo kansiorakenne uudelleen tallennetuista poluista ZIP-tiedostossa, tai tuo kaikki ensin Gramps Desktopiin, joka tarjoaa enemmän vaihtoehtoja yhdistää olemassa olevat mediasisällöt tuotuun puuhun, ja siirry sitten Gramps Webiin kuten on kuvattu [Gramps Desktopista tulemisessa](import.md#coming-from-gramps-desktop).

## Mediatiedoston tila

**Tieto**-osiossa [Hallintasettings](settings.md) näkyy:

- Mediasisältöjen kokonaismäärä puussa ja onko joiltakin puuttuu tarkistussumma
- Mediasisältöjen määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä valintamerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää mediasisältöviittauksia mutta ei varsinaisia tiedostoja. Puuttuvat tiedostot voidaan ladata kuten edellä on kuvattu.
