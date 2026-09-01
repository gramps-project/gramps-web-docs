# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa. Se on vain käyttäjien käytettävissä, joilla on Omistaja- tai Ylläpitäjärooli, ja se tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty laajennettaviin osioihin. Napsauta osion otsikkoa laajentaaksesi sitä.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediatiedostojen hallinnan.

### Käyttökiintiöt

Osion yläosassa näkyy nykyinen käyttö suhteessa kaikkiin määritettyihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajaton)
- **Media tallennus** – ladattujen mediataidostojen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajaton)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen konfiguraatio](../install_setup/configuration.md) lisätietoja varten.

### Tuo tiedot

Tuontiosio antaa sinun ladata sukupuutiedoston tai mediarchiivin. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

### Mediataidostojen tila

Tässä osiossa näkyy:

- Mediakohteiden kokonaismäärä puussa ja onko joiltakin puuttumassa tarkistussumma
- Mediakohteiden määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä tarkistusmerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin kohteisiin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää mediaviittauksia, mutta ei varsinaisia tiedostoja. Puuttuvat tiedostot voidaan ladata tuontimediarchiivin ominaisuuden kautta.

### Tuo mediarchiivi

Mahdollistaa ZIP-tiedoston lataamisen mediataidoista puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysimittaista hakemistoa, joka päivitetään normaalisti automaattisesti aina, kun tiedot muuttuvat. Tilanneindikaattori näyttää, kuinka monta kohdetta on tällä hetkellä indeksoitu verrattuna kokonaiskohteiden määrään.

Napsauta **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/configuration.md), näkyviin tulee lisäosio, jossa on kaksi toimintoa:

- **Uudelleenrakennus semanttiselle hakemistolle** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti raskasta ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain kohteet, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Puun asetukset

### Sukupuun nimi

!!! note
    Puun nimeäminen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaisesti asetettu [palvelimen konfiguraatiossa](../install_setup/configuration.md). Oletus yksittäisen puun asennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Gramps-sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta ensisijaisen tutkijan nimi, osoite ja yhteystiedot. Tämä tieto upotetaan vientiin (esim. GEDCOM-tiedostoihin).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja tulevat voimaan heti tallentamisen jälkeen.

Käytä värivalitsimia valitaksesi värit, napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään kojelaudan etusivulla. Huomautuksen sisältö renderöidään pääkojelaudan sarakkeiden alle ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana kojelaudan etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediakohteen, tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Puun tason asetuksia (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioida toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se voi – vastaava [Tarkista ja korjaa tietokanta -työkalua](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alla:

- Jos virheitä ei löytynyt, vahvistusviesti näytetään.
- Jos virheitä löytyi, näytetään yhteenvedon korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista kohteiden välillä.

### Vahvista tiedot

Kun [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – vastaava [Vahvista tiedot -työkalua](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) Gramps Desktopissa. Se raportoi asioita, jotka eivät ole mahdottomia, mutta ovat tarpeeksi epätodennäköisiä ollakseen tarkistamisen arvoisia, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Asetuksissa** voit säätää testien käyttämät kynnysarvot – maksimi-ikä, minim- ja maksimi-ikä naimisiin menemiseen tai lasten saamiseen, maksimi lasten määrä jne. – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset luetellaan sitten **Tietojen vahvistustulokset** -osiossa. Tämä työkalu ei muuta mitään: se vain raportoi, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät elämät ja suuret ikäerot tapahtuvat, joten käsittele tuloksia tarkistettavien asioiden luettelona sen sijaan, että pitäisit niitä korjattavina asioina.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, vaihda väriä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä nimetäksesi sen uudelleen (kynäkuvake), muuttaaksesi sen väriä (värivalitsin) tai poistaaksesi sen (poistokuvake).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista kohteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) siitä, miten tunnisteita käytetään koko Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` -tunnisteet.

## Vaaravyöhyke

!!! danger
    Toimenpiteet vaaravyöhykkeellä ovat **palautumattomia**. Tee varmuuskopio ennen jatkamista.

### Poista kaikki kohteet

Poistaa kohteet sukupuusta. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki kohteet** – tyhjentää puun kokonaan
- **Tietyt kohteet** – esimerkiksi vain tapahtumat tai vain mediakohteet

Sinua pyydetään vahvistamaan toiminto kirjautumalla uudelleen. Poistaminen suoritetaan taustatehtävänä, ja edistymisindikaattori näkyy.

!!! warning
    Vain osan kohdetyyppien poistaminen (eikä kaikkia kohteita kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet kohteiden välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden puun tuontia tai poistaaksesi erityiset kohteet, jotka on tuotu väärin.

### Palauta varmuuskopiosta

Palauttaa puun vastaamaan ladattua Gramps XML (`.gramps`) varmuuskopiotiedostoa, lisäämällä, päivittämällä ja poistamalla kohteita tarpeen mukaan, jotta puu on identtinen varmuuskopion kanssa.

!!! danger
    Tämä on tuhoisa korvaus, ei yhdistäminen. Mikä tahansa olemassa oleva kohde, jota ei ole ladatussa varmuuskopiossa, poistetaan.

Lataa `.gramps`-tiedosto, napsauta sitten **Esikatsele palautusta**. Sinua pyydetään vahvistamaan, jos istuntosi ei ole tarpeeksi tuore. Esikatselu suoritetaan taustatehtävänä, ja sen valmistuttua avautuu dialogi, joka tiivistää muutokset kohdetyyppien mukaan (ihmiset, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediakohteet, huomautukset, tunnisteet):

- **Lisää** – kohteet, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä puusta
- **Päivitä** – kohteet, jotka ovat molemmissa, mutta eroavat
- **Poista** – kohteet nykyisessä puussa, joita ei ole varmuuskopiossa
- **Muuttumaton** – kohteet, jotka ovat identtisiä molemmissa

Jos jokin kohde poistettaisiin, dialogi varoittaa kuinka monta. Tarkista yhteenveto, napsauta sitten **Palauta** ottaaksesi muutokset käyttöön tai **Peruuta** keskeyttääksesi.

!!! note
    Vain kohdetiedot ja mediaviittaukset palautetaan. Binääriset mediataidot itsessään ja puun metatiedot (oletushenkilö, kirjanmerkit, nimiryhmät) eivät vaikuta. Palauta puuttuvat mediataidot erikseen [Tuo mediarchiivi](#import-media-archive) -toiminnon kautta tarvittaessa.

!!! tip
    Käytä tätä palauttaaksesi puun tunnettuun hyvään Gramps XML -varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.
