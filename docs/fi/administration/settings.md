# Hallintasettings

**Asetukset > Hallinta** -sivu on saatavilla käyttäjäkuvakkeesta sovelluksen yläreunassa. Se on käytettävissä vain omistaja- tai ylläpitäjäroolilla oleville käyttäjille ja tarjoaa työkaluja sukupuun tietokannan hallintaan.

Sivu on järjestetty taitettaviin osioihin. Klikkaa osiota otsikkoa laajentaaksesi sen.

## Tiedot

Kattaa käyttökiintiöt, tietojen tuonnin ja mediafileiden hallinnan.

### Käyttökiintiöt

Osiota yläreunassa näytetään nykyinen käyttö suhteessa mahdollisiin määritettyihin rajoihin:

- **Ihmiset** – sukupuussa olevien henkilöobjektien määrä verrattuna määritettyyn maksimiin (∞, jos rajoituksia ei ole)
- **Media tallennus** – ladattujen mediafileiden kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoituksia ei ole)

Kiintiöt määrittää palvelimen ylläpitäjä; katso [Palvelimen kokoonpano](../install_setup/configuration.md) lisätietoja varten.

### Tuo tiedot

Tuontiosio antaa sinun ladata sukupuutiedoston tai media-arkiston. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

### Mediafileiden tila

Tässä osiossa näytetään:

- Sukupuussa olevien mediaobjektien kokonaismäärä ja onko joillakin puuttuva tarkistussumma
- Mediaobjektien määrä, joiden liitetty tiedosto puuttuu palvelimelta

Vihreä rastimerkki osoittaa, että kaikki on kunnossa. Jos ongelmia havaitaan, linkit vaikuttaviin objekteihin näytetään. Puuttuvat tarkistussummat esiintyvät tyypillisesti, kun tietoja on tuotu muodosta, kuten GEDCOM, joka sisältää media viittauksia mutta ei itse tiedostoja. Puuttuvat tiedostot voidaan ladata tuontimedia-arkiston ominaisuuden kautta.

### Tuo media-arkisto

Mahdollistaa ZIP-tiedoston lataamisen mediafileistä puuttuvien tiedostojen täyttämiseksi. Katso [Tuo tiedot](import.md) täydellisiä ohjeita varten.

## Hakemisto

### Hallitse hakemistoa

Gramps Web ylläpitää täysipainoista hakemistoa, joka päivitetään automaattisesti aina, kun tiedot muuttuvat. Tilaindikaattori näyttää, kuinka monta objektia on tällä hetkellä indeksoitu verrattuna kokonaisobjektimäärään.

Klikkaa **Päivitä hakemisto** laukaistaksesi täydellisen uudelleenrakennuksen. Edistymisindikaattori näkyy, kun tehtävä suoritetaan taustalla. Tämä on yleensä tarpeen vain palvelimen päivityksen jälkeen.

### Semanttinen hakemisto

!!! warning "Poistettu käytöstä"
    Semanttinen haku on poistettu käytöstä ja se poistetaan Gramps Web API 3.25:ssä yhdessä tämän osion kanssa. AI-keskustelu ei tarvitse sitä, koska Gramps Web API 3.24.

Jos palvelimella on [semanttinen (AI-pohjainen) haku käytössä](../install_setup/chat.md#semantic-search-deprecated), näkyviin tulee lisäosio, jossa on kaksi toimintoa:

- **Uudelleenluo semanttinen hakemisto** – rakentaa koko semanttisen hakemiston alusta alkaen. Tämä on laskennallisesti kallista ja voi kestää pitkään.
- **Päivitä semanttinen hakemisto** – suorittaa inkrementaalisen päivityksen, lisäämällä vain objektit, joita ei ole vielä indeksoitu. Nopeampi kuin täydellinen uudelleenrakennus.

## Sukupuun asetukset

### Sukupuun nimi

!!! note
    Sukupuun nimeäminen toimii vain [monisukupuuasetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaan asetettu [palvelimen kokoonpanossa](../install_setup/configuration.md). Oletus yksisukupuuasennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa Grampsin sukupuutietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi sen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

### Tutkijan tiedot

Aseta ensisijaisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot sisältyvät vientiin (esim. GEDCOM-tiedostot).

## Mukauttaminen

### Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän sukupuun käyttäjille ja ne tulevat voimaan heti tallennuksen jälkeen.

Käytä väriä valitsimia valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Nollaa** palauttaaksesi oletusasetukset.

### Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja sovelluksen yläreunassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

### Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään kojelaudan etusivulla. Huomautussisältö renderöidään pääkojelaudan sarakkeiden alapuolelle ja se on näkyvissä kaikille käyttäjille, joilla on pääsy sukupuuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyinen etusivun huomautus.

### Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana kojelaudan etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediaobjektin, ja tallenna sitten. Napsauta **Poista** poistaaksesi nykyinen etusivun kuva.

### Vienti/Tuontiasetukset

Sukupuun tason asetukset (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioimista varten toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo sukupuun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.

## Sukupuun käsittely

### Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se voi – vastaava [Tarkista ja korjaa tietokanta -työkalua](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näkyy painikkeen alapuolella:

- Jos virheitä ei löytynyt, vahvistusviesti näytetään.
- Jos virheitä löytyi, näytetään yhteenveto tehdyistä korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

### Vahvista tiedot

Vaikka [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – vastaava [Vahvista tiedot -työkalua](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) Gramps Desktopissa. Se raportoi asioita, jotka eivät ole mahdottomia, mutta ovat tarpeeksi epätodennäköisiä ollakseen tarkistamisen arvoisia, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Asetuksissa** voit säätää testien käyttämiä kynnysarvoja – maksimi-ikä, minim- ja maksimi-ikä naimisiin menemiseen tai lasten saamiseen, maksimi lasten määrä jne. – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset luetellaan sitten **Tietojen vahvistustulokset** -osiossa. Tämä työkalu ei muuta mitään: se vain raportoi, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät eliniät ja suuret ikäerot tapahtuvat, joten käsittele tuloksia tarkistettavien asioiden luettelona sen sijaan, että pitäisit niitä korjattavina asioina.

## Tunnisteet

### Hallitse tunnisteita

Luo, nimeä uudelleen, väritä ja poista [tunnisteita](../user-guide/tags.md) sukupuusta. Tunnisteet tallennetaan Gramps-tietokantaan, ja ne ovat kaikkien käyttäjien käytettävissä ja täysin yhteensopivia Gramps Desktopin kanssa.

Napsauta **Uusi tunniste** luodaksesi tunnisteen. Käytä ohjaimia olemassa olevan tunnisteen vieressä nimetäksesi sen uudelleen (kynäkuvake), muuttaaksesi sen väriä (värivalitsin) tai poistaaksesi sen (poistokuvake).

!!! note
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

Katso [Tunnisteet](../user-guide/tags.md) siitä, miten tunnisteita käytetään koko Gramps Webissä, mukaan lukien erityiset `Blog` ja `ToDo` -tunnisteet.

## Varmuuskopiot

Varmuuskopio sisältää sukupuun tiedot, mukaan lukien yksityiset tiedot, sukupuun asetukset ja sukupuun käyttäjät. Mediafilejä ei sisälly; katso [Varmuuskopioi mediafilejäsi](export.md#back-up-your-media-files).

### Tallennetut varmuuskopiot

Jos palvelimen ylläpitäjä on asettanut varmuuskopiohakemiston (`BACKUP_DIR`, katso [Palvelimen kokoonpano](../install_setup/configuration.md)), varmuuskopiot voidaan tallentaa palvelimelle. Muussa tapauksessa osiossa näkyy ilmoitus, että varmuuskopioiden tallentaminen ei ole määritetty, ja vain lataamisesta ladatusta tiedostosta palauttaminen on käytettävissä.

Napsauta **Tee varmuuskopio...** luodaksesi varmuuskopion. Se luodaan taustatehtävänä ja ilmestyy sitten tallennettujen varmuuskopioiden luetteloon, jossa on päivämäärä, henkilöiden määrä ja koko. Palvelin säilyttää vain uusimmat varmuuskopiot (viisi oletuksena) ja poistaa vanhemmat automaattisesti. Varmuuskopioiden määrä, joita voidaan luoda päivässä, on myös rajoitettu.

Jokaiselle tallennetulle varmuuskopialle voit:

- **Ladata** sen `.tar` -tiedostona, esimerkiksi pitääksesi kopion muualla.
- **Palauttaa** sen, kuten alla kuvataan.
- **Poistaa** sen, vahvistamisen jälkeen.

Uudemmalla Gramps Web -versiolla tehty varmuuskopio, kuin mitä palvelimella on käytössä, merkitään varoituskuvakkeella eikä sitä voida palauttaa.

### Palauta varmuuskopiosta

Palauttaa sukupuun tallennetusta varmuuskopiosta tai ladatusta tiedostosta. Palauttaaksesi tallennetun varmuuskopion, napsauta palautuspainiketta sen vieressä. Palauttaaksesi tiedostosta, valitse Gramps Web -varmuuskopio (`.tar`) tai Gramps XML -tiedosto (`.gramps`) ja napsauta **Palauta**.

!!! danger
    Tietojen palauttaminen on tuhoisa korvaus, ei yhdistäminen. Mikä tahansa olemassa oleva objekti, jota ei ole varmuuskopiossa, poistetaan.

Gramps Web -varmuuskopion kohdalla dialogi näyttää, milloin varmuuskopio on tehty, minkä sukupuun osalta ja millä versiolla, ja antaa sinun valita, mitkä osat palautetaan:

- **Tiedot** – sukupuun objektit
- **Sukupuun asetukset** – tämän sivun asetukset, kuten teeman värit, sovelluksen otsikko ja etusivun huomautus
- **Käyttäjät** – sukupuun käyttäjät

Napsauta **Esikatselu** nähdäksesi, mitä palautus muuttaisi. Gramps XML -tiedosto sisältää vain tietoja, joten tällaiselle tiedostolle esikatselu alkaa heti. Sinua pyydetään vahvistamaan, jos istuntosi ei ole tarpeeksi tuore. Esikatselu suoritetaan taustatehtävänä ja, kun se on valmis, avaa dialogi, joka tiivistää muutokset objektityypin mukaan (ihmiset, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediaobjektit, huomautukset, tunnisteet), sekä sukupuun asetukset ja käyttäjät, jos valittu:

- **Lisää** – objektit, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä sukupuusta
- **Päivitä** – objektit, jotka ovat molemmissa, mutta eroavat
- **Poista** – objektit nykyisessä sukupuussa, joita ei ole varmuuskopiossa
- **Pysynyt muuttumattomana** – objektit, jotka ovat identtisiä molemmissa

Jos mitään objekteja poistettaisiin, dialogi varoittaa kuinka monta. Tarkista yhteenveto ja napsauta sitten **Palauta** ottaaksesi muutokset käyttöön tai **Peruuta** keskeyttääksesi.

Palautuksen jälkeen varmuuskopiosta lisätyt käyttäjät luetellaan. He saavat satunnaisen salasanan, joten heidän on vaihdettava salasanansa ennen kirjautumista. Palvelimella jo olemassa olevia käyttäjiä ei koskaan muuteta. Mediaobjektit, joiden tiedostot puuttuvat palvelimelta, luetellaan myös; lataa ne [Tuo media-arkisto](#import-media-archive) -toiminnon kautta.

!!! note
    Tietojen palauttaminen palauttaa vain objektitiedot ja media viittaukset. Binäärimediafilejä ja sukupuun metatietoja (oletushenkilö, kirjanmerkit, nimiryhmät) ei vaikuta.

!!! tip
    Käytä tätä palauttaaksesi sukupuun tunnettuun hyvään varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.

## Vaaravyöhyke

!!! danger
    Toimenpiteet vaaravyöhykkeessä ovat **palautumattomia**. Tee [varmuuskopio](#backups) ennen jatkamista.

### Poista kaikki objektit

Poistaa objekteja sukupuusta. Napsauttamalla **Poista** avaa dialogin, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää sukupuun kokonaan
- **Erityiset objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään vahvistamaan (kirjautumaan sisään uudelleen) vahvistaaksesi toiminnon. Poisto suoritetaan taustatehtävänä ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla sukupuilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.

!!! tip
    Käytä tätä aloittaaksesi alusta ennen uuden sukupuun tuontia tai poistaaksesi erityiset objektityypit, jotka on tuotu väärin.
