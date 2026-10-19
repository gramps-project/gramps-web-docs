# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeesta sovelluksen yläreunassa. Se on vain käyttäjien saatavilla, joilla on Omistaja- tai Hallintorooli, ja se tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty laajennettaviin osioihin. Napsauta osion otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediafilejen hallinnan.

### Käyttökiintiöt

Osion yläosassa näkyy nykyinen käyttö suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediafilejen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Kiintiöt määrittää palvelimen järjestelmänvalvoja; katso [Palvelimen konfigurointi](../install_setup/configuration.md) lisätietoja varten.

### Tuo tiedot

Tuontiosio antaa sinun ladata sukupuu-tiedoston tai media-arkiston. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

### Mediafilejen tila

Tässä osiossa näkyy:

- Mediaobjektien kokonaismäärä puussa ja onko joiltakin puuttumassa tarkistussumma
- Mediaobjektien määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä tarkistusmerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää media viittauksia mutta ei varsinaisia tiedostoja. Puuttuvat tiedostot voidaan ladata tuomalla media-arkisto.

### Tuo media-arkisto

Mahdollistaa mediafilejen ZIP-tiedoston lataamisen puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysipainoista hakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

!!! warning "Vanha"
    Semanttinen haku on vanhentunut ja se poistetaan Gramps Web API 3.25:ssä tämän osion mukana. AI-keskustelu ei tarvitse sitä, koska Gramps Web API 3.24.

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/chat.md#semantic-search-deprecated), näkyy lisäosio, jossa on kaksi toimintoa:

- **Uudelleenrakennus semanttiselle hakemistolle** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain objekteja, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Puun asetukset

### Sukupuun nimi

!!! note
    Puun nimeäminen uudelleen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaan asetettu [palvelimen konfiguroinnissa](../install_setup/configuration.md). Oletus yksipuupohjaisessa asennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuun tietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä uudelleen, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta pääasiallisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot upotetaan vientiin (esim. GEDCOM-tiedostot).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja tulevat voimaan heti tallennuksen jälkeen.

Käytä värivalitsimia valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Nollaa** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään kojelaudan etusivulla. Huomautuksen sisältö renderöidään pääkojelaudan sarakkeiden alle ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyisen etusivun huomautuksen.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana kojelaudan etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediaobjektin, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyisen etusivun kuvan.

### Vienti/Tuontiasetukset

Puun tason asetuksia (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se voi – verrattavissa [Tarkista ja korjaa tietokanta -työkaluun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulokset näkyvät painikkeen alapuolella:

- Jos virheitä ei löydy, vahvistusviesti näytetään.
- Jos virheitä löytyy, näytetään yhteenveto tehdyistä korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

### Vahvista tiedot

Vaikka [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – verrattavissa [Vahvista tiedot -työkaluun](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) Gramps Desktopissa. Se raportoi asioita, jotka eivät ole mahdottomia, mutta ovat tarpeeksi epätodennäköisiä ollakseen tarkistamisen arvoisia, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Vaihtoehdoissa** voit säätää testien käyttämät kynnysarvot – maksimi-ikä, minim- ja maksimi-ikä naimisiin menemiseen tai lasten saamiseen, lasten enimmäismäärä ja niin edelleen – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset listataan sitten **Tietojen vahvistustulokset** -osiossa. Tämä työkalu ei muuta mitään: se vain raportoi, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät eliniät ja suuret ikäerot tapahtuvat, joten käsittele tuloksia tarkistettavien asioiden luettelona sen sijaan, että pitäisit niitä korjattavina asioina.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, vaihda väriä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä sen nimeämiseen uudelleen (kynäkuvake), värin muuttamiseen (värivalitsin) tai poistamiseen (poistokuvake).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) saadaksesi lisätietoja siitä, miten tunnisteita käytetään Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` tunnisteet.

## Vaaravyöhyke

!!! danger
    Toimenpiteet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen jatkamista.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään vahvistamaan henkilöllisyytesi (kirjautumaan uudelleen) vahvistaaksesi toiminnon. Poisto suoritetaan taustatehtävänä, ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuontia tai poistaaksesi tiettyjä objektityyppejä, jotka on tuotu väärin.

### Palauta varmuuskopiosta

Palauttaa puun vastaamaan ladattua Gramps XML (`.gramps`) varmuuskopiotiedostoa, lisäämällä, päivittämällä ja poistamalla objekteja tarpeen mukaan, jotta puu on identtinen varmuuskopion kanssa.

!!! danger
    Tämä on tuhoisa korvaus, ei yhdistäminen. Mikä tahansa olemassa oleva objekti, jota ei ole ladatussa varmuuskopiossa, poistetaan.

Lataa `.gramps`-tiedosto, ja napsauta sitten **Esikatsele palautusta**. Sinua pyydetään vahvistamaan henkilöllisyytesi, jos istuntosi ei ole tarpeeksi tuore. Esikatselu suoritetaan taustatehtävänä ja, kun se on valmis, avautuu dialogi, joka tiivistää muutokset objektityypin mukaan (ihmiset, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediaobjektit, huomautukset, tunnisteet):

- **Lisää** – objekteja, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä puusta
- **Päivitä** – objekteja, jotka ovat molemmissa, mutta eroavat
- **Poista** – objekteja, jotka ovat nykyisessä puussa mutta puuttuvat varmuuskopiosta
- **Ei muuttunut** – objekteja, jotka ovat identtisiä molemmissa

Jos jokin objekti poistettaisiin, dialogi varoittaa kuinka monta. Tarkista yhteenveto ja napsauta sitten **Palauta** ottaaksesi muutokset käyttöön tai **Peruuta** keskeyttääksesi.

!!! note
    Vain objektitiedot ja media viittaukset palautetaan. Binääriset mediafilet itsessään ja puun metatiedot (oletushenkilö, kirjanmerkit, nimiryhmät) eivät muutu. Palauta puuttuvat mediafilet erikseen [Tuo media-arkisto](#import-media-archive) -toiminnon kautta tarvittaessa.

!!! tip
    Käytä tätä palauttaaksesi puun tunnettuun hyvään Gramps XML -varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.
