# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on vain käyttäjien käytettävissä, joilla on Omistaja- tai Hallintorooli, ja se tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty taitettaviin osioihin. Napsauta osion otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediatiedostojen hallinnan.

### Käyttökiintiöt

Osion yläosassa näkyy nykyinen käyttö suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediatiedostojen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen kokoonpano](../install_setup/configuration.md) lisätietoja varten.

### Tuo tietoja

Tuontiosio antaa sinun ladata sukupuun tiedoston tai media-arkiston. Katso [Tuo tietoja](import.md) täydellisiä ohjeita varten.

### Mediatiedostojen tila

Tässä osiossa näkyy:

- Mediatiedostojen kokonaismäärä puussa ja onko joiltakin puuttunut tarkistussumma
- Mediatiedostojen määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä tarkistusmerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää media viittauksia, mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuontimedia-arkiston ominaisuuden kautta.

### Tuo media-arkisto

Mahdollistaa mediatiedostojen ZIP-tiedoston lataamisen puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tietoja](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysimääräistä tekstihakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Napsauta **Päivitä hakemisto** laittaaksesi täyden uudelleenrakennuksen käyntiin. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on harvoin tarpeen.

Jos puulla ei vielä ole hakemistoa, esimerkiksi palvelimen päivityksen jälkeen, joka muutti hakemistomuotoa, Gramps Web rakentaa sen taustalla ensimmäisen kerran, kun puu avataan. Kun sitä rakennetaan, osiossa näkyy "Hakemistoa rakennetaan." sen sijaan, että näkyisi laskentatulokset, **Päivitä hakemisto** on poistettu käytöstä, ja hakutulokset voivat olla puutteellisia. Rakennus näkyy [Ilmoituksissa](../user-guide/notifications.md) "Päivitä hakemisto" -tehtävänä.

## Puuasetukset

### Sukupuun nimi

!!! note
    Puun nimeäminen uudelleen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaisesti asetettu [palvelimen kokoonpanoon](../install_setup/configuration.md). Oletus yksittäisen puun asennuksessa ilman asetettua `TREE_ID`, tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuun tietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi sen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä uudelleen, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta pääasiallisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot upotetaan vientiin (esim. GEDCOM-tiedostot).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja ne tulevat voimaan heti tallennuksen jälkeen.

Käytä värihakuja valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään ohjauspaneelin etusivulla. Huomautussisältö renderöidään pääohjauspaneelin sarakkeiden alle ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsijaa etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana ohjauspaneelin etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsijaa etsiäksesi ja valitaksesi mediaobjektin, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Puun tason asetuksia (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataaksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puuasetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se voi – verrattavissa [Tarkista ja korjaa tietokanta -työkaluun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alla:

- Jos virheitä ei löydy, vahvistusviesti näytetään.
- Jos virheitä löytyy, näytetään yhteenveto tehdyistä korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

### Vahvista tiedot

Kun [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – verrattavissa [Vahvista tiedot -työkaluun](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) Gramps Desktopissa. Se raportoi asioita, jotka eivät ole mahdottomia, mutta ovat tarpeeksi epätodennäköisiä, jotta ne ansaitsevat toisen katsauksen, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Vaihtoehdoissa** voit säätää testien käyttämät kynnykset – maksimi-ikä, minim- ja maksimi-ikä naimisiin menemiseen tai lasten saamiseen, maksimi lasten määrä ja niin edelleen – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset luetellaan sitten **Tietojen vahvistustulokset** -osiossa. Tämä työkalu ei muuta mitään: se vain raportoi, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät elämät ja suuret ikäerot tapahtuvat, joten käsittele tuloksia tarkistettavien asioiden luettelona sen sijaan, että pitäisit niitä korjattavien asioiden luettelona.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, väritä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä nimetäksesi sen uudelleen (kynäkuvake), muuttaaksesi sen väriä (värivalitsin) tai poistaaksesi sen (roskakori-ikoni).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) siitä, miten tunnisteita käytetään koko Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` tunnisteet.

## Varmuuskopiot

Varmuuskopio sisältää sukupuun tiedot, mukaan lukien yksityiset tiedot, puuasetukset ja puun käyttäjät. Mediatiedostoja ei sisällytetä; katso [Varmuuskopioi mediatiedostosi](export.md#back-up-your-media-files).

### Tallennetut varmuuskopiot

Jos palvelimen ylläpitäjä on määrittänyt varmuuskopiohakemiston (`BACKUP_DIR`, katso [Palvelimen kokoonpano](../install_setup/configuration.md)), varmuuskopiot voidaan tallentaa palvelimelle. Muussa tapauksessa osiossa näkyy ilmoitus, että varmuuskopioiden tallentaminen ei ole määritetty, ja vain palautus ladatusta tiedostosta on saatavilla.

Napsauta **Tee varmuuskopio...** luodaksesi varmuuskopion. Se luodaan taustatehtävänä ja näkyy sitten tallennettujen varmuuskopioiden luettelossa, jossa on sen päivämäärä, ihmisten määrä ja koko. Palvelin säilyttää vain uusimmat varmuuskopiot (viisi oletuksena) ja poistaa vanhemmat automaattisesti. Varmuuskopioiden luomisen määrä päivässä on myös rajoitettu.

Jokaiselle tallennetulle varmuuskopiolle voit:

- **Ladata** sen `.tar`-tiedostona, esimerkiksi pitääksesi kopion muualla.
- **Palauttaa** sen, kuten alla kuvataan.
- **Poistaa** sen vahvistamisen jälkeen.

Uudemmalla Gramps Web -versiolla tehty varmuuskopio kuin palvelimella käytössä oleva versio on merkitty varoituskuvakkeella eikä sitä voida palauttaa.

### Palauta varmuuskopiosta

Palauttaa puun tallennetusta varmuuskopiosta tai ladatusta tiedostosta. Palauttaaksesi tallennetun varmuuskopion, napsauta palautuspainiketta sen vieressä. Palauttaaksesi tiedostosta, valitse Gramps Web -varmuuskopio (`.tar`) tai Gramps XML -tiedosto (`.gramps`) ja napsauta **Palauta**.

!!! danger
    Tietojen palauttaminen on tuhoisa korvaus, ei yhdistäminen. Mikä tahansa olemassa oleva objekti, jota ei ole varmuuskopiossa, poistetaan.

Gramps Web -varmuuskopion kohdalla dialogi näyttää, milloin varmuuskopio tehtiin, minkä puun osalta ja millä versiolla, ja antaa sinun valita, mitkä osat palautetaan:

- **Tiedot** – sukupuun objektit
- **Puuasetukset** – tämän sivun asetukset, kuten teeman värit, sovelluksen otsikko ja etusivun huomautus
- **Käyttäjät** – puun käyttäjät

Napsauta **Esikatselu** nähdäksesi, mitä palautus muuttaisi. Gramps XML -tiedosto sisältää vain tietoja, joten tällaisen tiedoston esikatselu alkaa heti. Sinua pyydetään vahvistamaan, jos istuntosi ei ole tarpeeksi tuore. Esikatselu suoritetaan taustatehtävänä, ja kun se on valmis, avautuu dialogi, joka tiivistää muutokset objektityypin mukaan (ihmiset, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediaobjektit, huomautukset, tunnisteet) sekä puuasetusten ja käyttäjien osalta, jos valittu:

- **Lisää** – objekteja, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä puusta
- **Päivitä** – objekteja, jotka ovat molemmissa mutta eroavat
- **Poista** – objekteja nykyisessä puussa, joita ei ole varmuuskopiossa
- **Ei muuttunut** – objekteja, jotka ovat identtisiä molemmissa

Jos mitään objekteja poistettaisiin, dialogi varoittaa kuinka monta. Tarkista yhteenveto ja napsauta sitten **Palauta** ottaaksesi muutokset käyttöön tai **Peruuta** keskeyttääksesi.

Palautuksen jälkeen varmuuskopiosta lisätyt käyttäjät luetellaan. Heille annetaan satunnainen salasana, joten heidän on nollattava salasanansa ennen kuin he voivat kirjautua sisään. Palvelimella jo olemassa olevia käyttäjiä ei koskaan muuteta. Mediatiedostot, joiden tiedostot puuttuvat palvelimelta, luetellaan myös; lataa ne [Tuo media-arkisto](#import-media-archive) -toiminnon kautta.

!!! note
    Tietojen palauttaminen palauttaa vain objektitiedot ja media viittaukset. Binääri mediatiedostot itsessään ja puun metatiedot (oletus henkilö, kirjanmerkit, nimiryhmät) eivät vaikuta.

!!! tip
    Käytä tätä palauttaaksesi puu tunnettuun hyvään varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.

## Vaaravyöhyke

!!! danger
    Toimenpiteet vaaravyöhykkeessä ovat **korjaamattomia**. Tee [varmuuskopio](#backups) ennen etenemistä.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään vahvistamaan (kirjautumaan uudelleen) toimenpide. Poisto suoritetaan taustatehtävänä ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi puhtaana ennen uuden puun tuontia tai poistaaksesi erityisiä objektityyppejä, jotka on tuotu väärin.
