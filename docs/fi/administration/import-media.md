# Tuo mediasisältöjä

Jos olet [tuonut sukupuun](import.md) ja tarvitset vastaavien mediasisältöjen lataamista, käytä **Tuo mediasisältöjä** -toimintoa Tiedot-osiossa [Hallintasettingeissä](settings.md). Se odottaa ZIP-tiedostoa, joka sisältää puuttuvat mediasisällöt. Tiedostot yhdistetään puusi mediasisältöihin yhdellä kahdesta tavalla:

- **Tarkistussumman mukaan.** Mediasisältöjen osalta, joilla on tarkistussumma – kuten on tapauksessa puista, jotka on tuotu Gramps Desktopista – käytetään tiedostoa, jonka tarkistussumma vastaa, riippumatta sen nimestä tai ZIP-tiedoston kansiorakenteesta. Tämä toimii vain, jos Gramps-tietokannan tarkistussummat ovat oikein, mikä varmistetaan suorittamalla tarkistus- ja korjaustyökalu.
- **Polun mukaan.** Mediasisältöjä, joilla ei ole tarkistussummaa – kuten on tyypillistä GEDCOM-tuonnin jälkeen – yhdistetään niiden polun mukaan: ZIP-tiedoston on sisällettävä tiedosto tarkalleen suhteellisella polulla, joka on tallennettu mediasisältöön.

Jos GEDCOM-tiedostossasi tallennetut polut ovat absoluuttisia (esimerkiksi `C:\Users\...\photo.jpg`), yhdistäminen polun mukaan ei toimi. Tässä tapauksessa suositellaan ensin tuomaan kaikki Gramps Desktopiin, jossa on enemmän vaihtoehtoja yhdistää olemassa olevat mediasisältöjä tuodun puun kanssa, ja siirtymään sitten Gramps Webiin kuten on kuvattu [Gramps Desktopista tuleminen](import.md#coming-from-gramps-desktop).

## Mediatiedoston tila

**Tiedot**-osio [Hallintasettingeissä](settings.md) näyttää:

- Mediasisältöjen kokonaismäärän puussa ja onko joiltakin puuttunut tarkistussumma
- Mediasisältöjen määrän, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä valintamerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää mediasisältöviittauksia mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata kuten edellä on kuvattu.
