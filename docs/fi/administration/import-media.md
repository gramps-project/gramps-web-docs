# Tuo media tiedostoja

Jos olet [tuonut sukupuun](import.md) ja tarvitset vastaavien media tiedostojen lataamista, käytä **Tuo media tiedostoja** -toimintoa Tiedot-osiossa [Hallinta-asetuksissa](settings.md). Se odottaa ZIP-tiedostoa, joka sisältää puuttuvat media tiedostot. Tiedostot yhdistetään puusi mediaobjekteihin yhdellä kahdesta tavalla:

- **Tarkistussumman mukaan.** Mediaobjekteille, joilla on tarkistussumma – kuten on tapaus Gramps Desktopista tuoduissa puissa – käytetään tiedostoa, jonka tarkistussumma vastaa, riippumatta sen nimestä tai ZIP-tiedoston kansiorakenteesta. Tämä toimii vain, jos Gramps-tietokannan tarkistussummat ovat oikein, mikä varmistuu tarkistus- ja korjaustyökalun suorittamisella.
- **Polun mukaan.** Mediaobjektit ilman tarkistussummaa – kuten on tyypillistä GEDCOM-tuonnin jälkeen – yhdistetään niiden polun mukaan: ZIP-tiedoston on sisällettävä tiedosto tarkalleen suhteellisella polulla, joka on tallennettu mediaobjektiin.

Jos GEDCOM-tiedostossasi tallennetut polut ovat absoluuttisia (esimerkiksi `C:\Users\...\photo.jpg`), yhdistäminen polun mukaan ei toimi. Tässä tapauksessa suositellaan ensin tuomaan kaikki Gramps Desktopiin, jossa on enemmän vaihtoehtoja yhdistää olemassa olevia media tiedostoja tuodun puun kanssa, ja siirtymään sitten Gramps Webiin kuten on kuvattu [Gramps Desktopista tuleminen](import.md#coming-from-gramps-desktop).
