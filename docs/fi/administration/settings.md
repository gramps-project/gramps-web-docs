# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on vain käyttäjien saatavilla, joilla on Omistaja- tai Hallintorooli, ja se tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty laajennettaviin osioihin. Napsauta osiota otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediatiedostojen hallinnan.

### Käyttökiintiöt

Osiota yläreunassa näkyy nykyinen käyttö suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediataidostojen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen konfiguraatio](../install_setup/configuration.md) lisätietoja varten.

### Tuo tiedot

Tuontiosio antaa sinun ladata sukupuutiedoston tai media-arkiston. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

### Mediataidoston tila

Tässä osiossa näkyy:

- Mediakohteiden kokonaismäärä puussa ja onko joillakin puuttuva tarkistussumma
- Mediakohteiden määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä tarkistusmerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin kohteisiin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tiedot on tuotu muodosta, kuten GEDCOM, joka sisältää mediaviittauksia, mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuomalla media-arkisto.

### Tuo media-arkisto

Sallii ladata ZIP-tiedoston mediataidoista puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysimääräistä tekstihakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta kohdetta on tällä hetkellä indeksoitu verrattuna kokonaiskohteiden määrään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/configuration.md), näkyviin tulee lisäosa, jossa on kaksi toimintoa:

- **Uudelleenluo semanttinen hakemisto** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain kohteet, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Puuasetukset

### Sukupuun nimi

!!! note
    Sukupuun nimeäminen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaan asetettu [palvelimen konfiguraatiossa](../install_setup/configuration.md). Oletus yksittäisen puun asennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta päätutkijan nimi, osoite ja yhteystiedot. Nämä tiedot sisältyvät vientiin (esim. GEDCOM-tiedostoihin).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja ne tulevat voimaan heti tallennuksen jälkeen.

Käytä väriä valitsimia valitaksesi värit, napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetuksiin.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimeä).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään kojelaudan etusivulla. Huomautussisältö renderöidään pääkojelaudan sarakkeiden alle ja on kaikkien puuhun pääsyyn oikeutettujen käyttäjien nähtävissä.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana kojelaudan etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediaobjektin, tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Puu-tason asetukset (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puu asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, joita se voi – verrattavissa [Tarkista ja korjaa tietokanta -työkaluun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulokset näkyvät painikkeen alla:

- Jos virheitä ei löytynyt, vahvistusviesti näytetään.
- Jos virheitä löytyi, näytetään yhteenveto sovituista korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Vaaravyöhyke

!!! danger
    Toimet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen jatkamista.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediakohteet

Sinua pyydetään vahvistamaan (kirjautumaan uudelleen) toimiaksesi. Poistaminen suoritetaan taustatehtävänä ja edistymisindikaattori näkyy.

!!! warning
    Vain tietyn objektityypin (eikä kaikkien objektien kerralla) poistaminen voi kestää erittäin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuomista tai poistaaksesi tiettyjä objektityyppejä, jotka on tuotu väärin.
