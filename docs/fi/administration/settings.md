# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on käytettävissä vain käyttäjille, joilla on Omistaja- tai Ylläpitäjärooli, ja se tarjoaa työkaluja sukupuun tietokannan hallintaan.

## Käyttökiintiöt

Sivun yläosassa näkyy nykyinen käyttö suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoitukseton)
- **Media tallennus** – ladattujen mediafileiden kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoitukseton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen konfigurointi](../install_setup/configuration.md) lisätietoja varten.

## Tuo tietoja

Tuo-osio antaa sinun ladata sukupuutiedoston tai media-arkiston. Katso [Tuo tietoja](import.md) täydellisiä ohjeita varten.

## Mediafileiden tila

Tässä osiossa näkyy:

- Mediaobjektien kokonaismäärä puussa ja onko joillakin puuttuva tarkistussumma
- Mediaobjektien määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä valintamerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää media viittauksia, mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuomalla media-arkisto.

## Tuo media-arkisto

Mahdollistaa mediafileiden ZIP-tiedoston lataamisen puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tietoja](import.md) täydellisiä ohjeita varten.

## Hallitse hakemistoa

Gramps Web ylläpitää täysimittaista hakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/configuration.md), näkyviin tulee lisäosio, jossa on kaksi toimintoa:

- **Uudelleenluo semanttinen hakemisto** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain objekteja, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Sukupuun nimi

!!! note
    Sukupuun nimeäminen toimii vain [monisukupuuasetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaisesti asetettu [palvelimen konfiguroinnissa](../install_setup/configuration.md). Oletusarvoisessa yksittäisessä sukupuuasennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

## Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, joita se voi – vastaavasti [Tarkista ja korjaa tietokanta -työkalua](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alla:

- Jos virheitä ei löydy, vahvistusviesti näytetään.
- Jos virheitä löytyi, näytetään yhteenveto sovituista korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Vaaravyöhyke

!!! danger
    Toimet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen jatkamista.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään kirjautumaan uudelleen vahvistaaksesi toiminnon. Poisto suoritetaan taustatehtävänä ja edistymisindikaattori näkyy.

!!! warning
    Vain tiettyjen objektityyppien (eikä kaikkien objektien kerralla) poistaminen voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuomista tai poistaaksesi erityiset objektityypit, jotka on tuotu väärin.
