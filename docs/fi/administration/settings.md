# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on vain käyttäjien saatavilla, joilla on Omistaja- tai Hallinnoija-rooli, ja se tarjoaa työkaluja sukupuu-tietokannan hallintaan.

Sivu on järjestetty taitettaviin osioihin. Napsauta osion otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediatiedostojen hallinnan.

### Käyttökiintiöt

Osion yläosa näyttää nykyisen käytön suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediataidostojen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen konfigurointi](../install_setup/configuration.md) lisätietoja varten.

### Tuo tiedot

Tuontiosio antaa sinun ladata sukupuu-tiedoston tai mediarchivin. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

### Mediataidoston tila

Tässä osiossa näkyy:

- Mediakohteiden kokonaismäärä puussa ja onko joillakin puuttuva tarkistussumma
- Mediakohteiden määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä rastimarkkeri osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää mediaviittauksia, mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuontimediarchivin ominaisuuden kautta.

### Tuo mediarchivi

Mahdollistaa mediataidostojen ZIP-tiedoston lataamisen puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysipainoista hakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/configuration.md), näkyviin tulee lisäosio, jossa on kaksi toimintoa:

- **Uudelleenrakennus semanttiselle hakemistolle** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain objekteja, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Puun asetukset

### Sukupuun nimi

!!! note
    Puun nimeäminen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaan asetettu [palvelimen konfiguroinnissa](../install_setup/configuration.md). Oletus yksipuus-asennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta pääasiallisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot upotetaan vientiin (esim. GEDCOM-tiedostoihin).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja ne tulevat voimaan heti tallennuksen jälkeen.

Käytä värivalitsimia valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä korvataan sukupuun nimellä selainikkunan otsikkorivillä ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään kojelaudan etusivulla. Huomautussisältö renderöidään pääkojelaudan sarakkeiden alle ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana kojelaudan etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediakohteen, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Puun tason asetukset (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataaksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, joita se voi – vastaavasti [Tarkista ja korjaa tietokanta -työkalun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) kanssa Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alla:

- Jos virheitä ei löydy, vahvistusviesti näytetään.
- Jos virheitä löytyy, näytetään yhteenveto sovelletuista korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, vaihda väriä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä nimetäksesi sen uudelleen (kynäkuvake), vaihtaaksesi sen väriä (värivalitsin) tai poistaaksesi sen (poistokuvake).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) siitä, miten tunnisteita käytetään koko Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` -tunnisteet.

## Vaaravyöhyke

!!! danger
    Toimet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen etenemistä.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistaa:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediakohteet

Sinua pyydetään vahvistamaan (kirjautumaan uudelleen) toimenpide. Poisto suoritetaan taustatehtävänä ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuontia tai poistaaksesi erityisiä objektityyppejä, jotka on tuotu väärin.

### Palauta varmuuskopiosta

Palauttaa puun vastaamaan ladattua Gramps XML (`.gramps`) varmuuskopiotiedostoa, lisäämällä, päivittämällä ja poistamalla objekteja tarpeen mukaan, jotta puu on identtinen varmuuskopion kanssa.

!!! danger
    Tämä on tuhoisa korvaus, ei yhdistäminen. Mikään olemassa oleva objekti, jota ei ole ladatussa varmuuskopiossa, poistetaan.

Lataa `.gramps`-tiedosto, ja napsauta sitten **Esikatsele palautusta**. Sinua pyydetään vahvistamaan, jos istuntosi ei ole tarpeeksi tuore. Esikatselu suoritetaan taustatehtävänä ja, kun se on valmis, avautuu dialogi, joka tiivistää muutokset objektityypin mukaan (ihmiset, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediakohteet, huomautukset, tunnisteet):

- **Lisää** – objekteja, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä puusta
- **Päivitä** – objekteja, jotka ovat molemmissa, mutta eroavat toisistaan
- **Poista** – objekteja, jotka ovat nykyisessä puussa mutta puuttuvat varmuuskopiosta
- **Muuttumaton** – objekteja, jotka ovat identtisiä molemmissa

Jos mitään objekteja poistetaan, dialogi varoittaa kuinka monta. Tarkista yhteenveto ja napsauta sitten **Palauta** ottaaksesi muutokset käyttöön tai **Peruuta** keskeyttääksesi.

!!! note
    Vain objektitiedot ja mediaviittaukset palautetaan. Binääriset mediataidostot itsessään ja puun metatiedot (oletushenkilö, kirjanmerkit, nimiryhmät) eivät vaikuta. Palauta puuttuvat mediataidostot erikseen [Tuo mediarchivi](#import-media-archive) -toiminnon kautta, jos tarpeen.

!!! tip
    Käytä tätä palauttaaksesi puun tunnettuun hyvään Gramps XML -varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.
