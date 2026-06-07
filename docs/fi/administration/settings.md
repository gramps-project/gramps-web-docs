# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on käytettävissä vain omistaja- tai ylläpitäjäroolin omaaville käyttäjille ja tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty laajennettaviin osioihin. Napsauta osion otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediatiedostojen hallinnan.

### Käyttökiintiöt

Osion yläosa näyttää nykyisen käytön suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Mediavarasto** – ladattujen mediataidostojen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen konfigurointi](../install_setup/configuration.md) lisätietoja varten.

### Tietojen tuonti

Tuontiosio mahdollistaa sukupuutiedoston tai mediarkiston lataamisen. Katso [Tietojen tuonti](import.md) täydellisiä ohjeita varten.

### Mediataidostojen tila

Tämä osio näyttää:

- Mediakohtien kokonaismäärän puussa ja onko joillakin puuttuva tarkistussumma
- Mediakohtien määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä rastimarkkeri osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää mediaviittauksia, mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuontimediarkistotoiminnon kautta.

### Mediarkiston tuonti

Mahdollistaa ZIP-tiedoston lataamisen mediataidoista puuttuvien tiedostojen täyttämiseksi. Katso [Tietojen tuonti](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysimittaista hakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/configuration.md), näkyviin tulee lisäosio, jossa on kaksi toimintoa:

- **Uudelleenluo semanttinen hakemisto** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain objekteja, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Puun asetukset

### Sukupuun nimi

!!! note
    Puun nimeäminen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaisesti asetettu [palvelimen konfiguroinnissa](../install_setup/configuration.md). Oletus yksipuus-asennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Grampsin sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta pääasiallisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot on upotettu vientiin (esim. GEDCOM-tiedostot).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja ne astuvat voimaan heti tallennuksen jälkeen.

Käytä värivalitsimia valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selainikkunan otsikkorivillä ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään ohjauspaneelin etusivulla. Huomautuksen sisältö renderöidään pääohjauspaneelin sarakkeiden alle ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana ohjauspaneelin etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediakohtaa, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Puun tason asetuksia (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se voi – verrattavissa [Tarkista ja korjaa tietokanta -työkaluun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alla:

- Jos virheitä ei löytynyt, vahvistusviesti näytetään.
- Jos virheitä löytyi, näytetään yhteenveto tehdyistä korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, vaihda väriä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä nimetäksesi sen uudelleen (kynäkuvake), vaihtaaksesi sen väriä (värivalitsin) tai poistaaksesi sen (roskakori-kuvake).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) siitä, miten tunnisteita käytetään koko Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` -tunnisteet.

## Vaaravyöhyke

!!! danger
    Toimet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen jatkamista.

### Poista kaikki objektit

Poistaa objektit sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediakohtia

Sinua pyydetään todentamaan itsesi uudelleen (kirjautumaan sisään uudelleen) vahvistaaksesi toiminnon. Poisto suoritetaan taustatehtävänä, ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuontia tai poistaaksesi tietyt objektityypit, jotka on tuotu väärin.
