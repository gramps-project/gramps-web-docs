# Synkronoi Gramps Web ja Gramps Desktop

*Gramps Web Sync* on Grampsin lisäosa, joka mahdollistaa Gramps-tietokannan synkronoinnin työpöytätietokoneellasi Gramps Webin kanssa, mukaan lukien mediatiedostot.

!!! warning
    Kuten minkä tahansa synkronointityökalun kanssa, älä pidä tätä varmuuskopiointityökaluna. Satunnainen poistaminen yhdellä puolella leviää toiselle puolelle. Varmista, että luot säännöllisesti varmuuskopioita (Gramps XML -muodossa) perhepuustasi.

!!! info
    Dokumentaatio viittaa Gramps Web Sync -lisäosan uuteen versioon. Käytä Gramps-lisäosahallintaa päivittääksesi lisäosan uusimpaan versioon tarvittaessa.

!!! note "Mitä muutoksia versiossa 1.5"
    Lisäosan käyttöliittymä kirjoitettiin uudelleen versiossa 1.5. Askel askeleelta -ohjelma on poistettu, ja sen sijaan on yksi ikkuna, ja mediakuvat vahvistetaan nyt yhdessä objektimuutosten kanssa erillisen sivun sijaan. Jos etsit synkronointitilan valitsinta, se sijaitsee nyt **ylhäällä** muutosten luettelon sijaan sen alla. **Yhdistä**-synkronointitila on poistettu; katso [Synkronointitila](#sync-mode) alla.

## Asennus

Lisäosa vaatii Gramps 6.0:n, joka toimii Python 3.10:ssä tai uudemmassa.
Se on saatavilla Gramps Desktopissa ja voidaan asentaa [tavallisella tavalla](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Varmista, että käytät samaa Gramps-versiota työpöydälläsi kuin palvelimellasi. Katso [Hanki apua](../help/help.md) -osio, jotta voit selvittää, mikä Gramps-versio palvelimellasi on. Gramps-version muoto on `MAJOR.MINOR.PATCH`, ja `MAJOR` ja `MINOR` on oltava samat verkkosivulla ja työpöydällä.

### Palvelinvaatimukset

Lisäosa tarkistaa kaksi asiaa palvelimeltasi heti yhteyden muodostamisen jälkeen ja kieltäytyy jatkamasta, jos kumpikaan ei täyty. Molemmat tarkistukset tapahtuvat ennen kuin mitään ladataan.

- **Gramps Web API versio 3.x.** Tämä lisäosan versio, Gramps 6.0:lle, toimii Gramps Web API 3:n kanssa. Vanhempi palvelin tarvitsee päivityksen; palvelin, joka käyttää *uudemman* API-pääversion, tarvitsee uudemman version Grampsista, ei uutta lisäosaa, koska jokainen Gramps-julkaisulinja parittaa yhden API-version kanssa. Voit löytää palvelimesi version kohdasta *Asetukset ▸ Versiotiedot* Gramps Webissä.
- **Taustatehtäväjono.** Synkronointi lähettää muutoksensa taustatehtävänä. Palvelimella, jolla ei ole määritetty tehtäväjonoa, muutosten soveltaminen tapahtuisi synkronisesti ja aikakatkaistaisiin minkä tahansa todellisen perhepuun kohdalla, joten lisäosa kieltäytyy aloittamasta sen sijaan, että se epäonnistuisi kesken kaiken.

Tarvitset myös tilin, jolla on vähintään muokkausoikeudet, voidaksesi soveltaa muutoksia etädatabaselle.

Valinnainen vaihe:

??? note inline end "Gnome keyring -bugi"
    Tällä hetkellä on [bugi python keyringissä](https://github.com/jaraco/keyring/issues/496), joka vaikuttaa moniin Gnome-työpöytäkonfiguraatioihin. Saatat joutua luomaan konfigurointitiedoston `~/.config/python_keyring/keyringrc.cfg` ja muokkaamaan sitä näyttämään tältä:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Asenna `keyring` (esim. `sudo apt install python3-keyring` tai `sudo dnf install python3-keyring`), jotta voit tallentaa API-salasanan turvallisesti järjestelmäsi salasanojen hallintaan.

Jos keyringia ei voida käyttää, lisäosa ilmoittaa siitä ja jatkaa ilman sitä — sinulta kysytään vain salasana joka kerta. Gramps **Snap** -paketissa järjestelmän keyring on estetty rajoitusten vuoksi, kunnes yhdistät käyttöliittymän kerran:

```bash
snap connect gramps:password-manager-service
```

Lisäosa näyttää tämän tarkan komennon, kun se havaitsee tilanteen.

## Käyttö

Kun lisäosa on asennettu, se on saatavilla Grampsissa kohdassa *Työkalut ▸ Perhepuun käsittely ▸ Gramps&nbsp;Web&nbsp;Sync*. Kun vahvistat dialogin varoituksen, että kumoamishistoria hylätään, synkronointisivu avautuu.

**Muutoksia ei sovelleta paikalliseen puuhusi tai palvelimelle ennen kuin vahvistat ne nimenomaisesti.**

Ikkunassa on yläreunassa nauha, joka nimeää perhepuun, jonka kanssa synkronoidaan, tilin ja osoitteen, johon se kuuluu, sekä milloin se on viimeksi synkronoitu. Alhaalla näytetään lisäosan ja palvelimen Web API:n versio — hyödyllinen ongelman raportoinnissa.

### Yhdistäminen

Jos olet synkronoinut tätä perhepuuta aiemmin ja salasanasi on tallennettu, lisäosa yhdistää heti avautuessaan ja siirtyy suoraan vertailuun. Muuten se kysyy Gramps Web -instanssisi perus-URL-osoitetta (esimerkki: `https://mygrampsweb.com/`), käyttäjänimeäsi ja salasanaasi.

URL-osoite ja käyttäjänimi tallennetaan selkokielisinä Gramps-käyttäjähakemistossasi. Salasana tallennetaan järjestelmän salasanojen hallintaan vain, jos jätät **Muista salasana** -valinnan rastituksi; rastin poistaminen poistaa kaikki tallennetut salasanat kyseiselle palvelimelle.

!!! tip "Useita perhepuuta, useita palvelimia"
    Jokainen palvelin, jonka kanssa synkronoidaan, tallennetaan erikseen, yhdessä oman tietueensa kanssa siitä, milloin se on viimeksi synkronoitu. Kahden palvelimen välillä vaihteleminen ei enää häiritse kumpaakaan.

    Jokainen merkintä tallentaa myös **mikä paikallinen perhepuu** se on viimeksi synkronoitu. Lisäosa yhdistää vain itsenäisesti, kun se vastaa avointa puuta; muuten se näyttää yhteystiedot ja odottaa, että painat *Yhdistä*, varoituksella, jos tallennetut tunnistetiedot kuuluvat eri puulle. Tämä on tärkeää, koska puun synkronointi palvelimen kanssa, joka pitää *eri* puuta, ehdottaa molempien sisältöjen poistamista.

Kaksi toimintoa on saatavilla, kun mitään ei kirjoiteta:

- **Vaihda palvelinta…**, yläreunassa, palaa yhteystietoihin, jotta voit osoittaa tämän puun eri palvelimelle. Se keskeyttää käynnissä olevan vertailun sen sijaan, että sinun pitäisi odottaa sen valmistumista.
- **Unohda tämä palvelin**, yhteyspaneelissa, poistaa tallennetun osoitteen, käyttäjänimen ja salasanan, yhdessä tietueen kanssa siitä, milloin tämä puu viimeksi synkronoitiin. Seuraava synkronointi vertaa sitten kahta puuta alusta alkaen.

Jos syöt osoitteen, joka alkaa `http://` sen sijaan, että se alkaisi `https://`, varoitus ilmestyy kirjoittaessasi. Salasana lähetettäisiin selkokielisenä, joten käytä sitä vain paikalliseen testaukseen.

### Muutosten tarkastelu

Lisäosa vertaa paikallisia ja etädatabaaseja ja näyttää, mitä se ehdottaa tehtäväksi. Toisin kuin aikaisemmissa versioissa, jotka listasivat raakoja eroja kahden puun välillä, luettelo näyttää nyt **toiminnot**, jotka toteutetaan, ryhmiteltynä sen mukaan, mikä tietokanta niitä muuttaa:

```
▾ Muutetaan tässä tietokoneessa (7 objektia)
    ▾ Lisää 3 objektia
        Henkilö   John Smith        I0123
    ▾ Päivitä 4 objektia
        …
▾ Muutetaan palvelimella (5 objektia)
    …
```

Jokaisessa rivissä nimetään objekti, joten voit kertoa, kuka tai mikä on vaikuttanut, sen sijaan että näkisit vain Gramps ID:n.

Jos jotain aiotaan poistaa, luettelon yläpuolella oleva varoitus kertoo, kuinka monta objektia ja kummalla puolella. Tämä ilmestyy aina, kun poistaminen on mukana, mukaan lukien tavallisessa kaksisuuntaisessa synkronoinnissa, joka levittää itse tekemäsi poistamisen.

Paina **Sovella** toteuttaaksesi sen, mitä luettelo kuvaa.

!!! warning "Älä muokkaa tarkastellessasi"
    Synkronointisivu ei estä muuta Grampsia, joten voit jatkaa työskentelyä, kun luettelo on avoinna. Jos muokkaat vaikuttavaa objektia, lisäosa havaitsee sen, kun painat Sovella, pysähtyy ilman muutoksia ja pyytää sinua vertailemaan uudelleen. Mikään ei katoa, mutta vertailu on toistettava.

#### Synkronointitila

Synkronointitila valitaan **ylhäällä** muutosten luettelon. Sen muuttaminen rakentaa luettelon uudelleen, koska tila päättää, mitä kukin ero oikeasti tulee.

- **Kaksisuuntainen synkronointi** (oletusarvo) — muutokset molemmilta puolilta yhdistetään. Molemmissa paikoissa muokatut objektit yhdistetään.
- **Nollaa palvelin vastaamaan tätä tietokonetta** — palvelin tehdään vastaamaan tätä tietokonetta. Palvelimella vain muutettu kaikki hylätään.
- **Nollaa tämä tietokone vastaamaan palvelinta** — tämä tietokone tehdään vastaamaan palvelinta. Täällä vain muutettu kaikki hylätään.

!!! note
    **Yhdistä**-tila, joka oli saatavilla aikaisemmissa versioissa, on poistettu. Se erosi kaksisuuntaisesta synkronoinnista vain palauttamalla objektit, jotka oli poistettu yhdeltä puolelta sen sijaan, että se levittäisi poistamisen, mikä ei ollut erottelu, jota käyttöliittymä voisi selittää hyödyllisesti. Jos olet luottanut siihen, käytä kaksisuuntaista synkronointia ja palauta kaikki, mitä haluat säilyttää varmuuskopiosta.

### Mediakuvat

Mediakuvia käsitellään osana samaa vahvistusta, ei erillisenä vaiheena. Jos tiedostoja on siirrettävä, luettelon alapuolella oleva valintaruutu tarjoaa niiden siirtämistä:

```
[x] Siirrä myös 12 mediakuvaa (4 ladattavaa, 8 ladattavaa)
```

Poista valinta synkronoimalla objektimuutokset ilman tiedostojen koskemista.

Tiedostot, joita ei ole *molemmilla* puolilla, luetellaan erikseen, koska niille ei voida tehdä mitään:

```
2 mediakuvaa puuttuu molemmilta puolilta eikä niitä voida siirtää.
```

Huomaa seuraavat rajoitukset mediakuvien synkronoinnissa:

- Jos paikallisella tiedostolla on eri tarkistussumma kuin Gramps-tietokannassa tallennettu (tämä voi tapahtua esimerkiksi Word-tiedostoille, kun niitä muokataan Grampsiin lisäämisen jälkeen), lataus epäonnistuu virheilmoituksella.
- Työkalu ei tarkista kaikkien paikallisten tiedostojen eheyttä, joten jos paikallinen tiedosto on olemassa polulla, joka on tallennettu mediakohteelle, mutta tiedosto on erilainen kuin palvelimella oleva tiedosto, työkalu ei havaitse sitä. Käytä Media Verify -lisäosaa havaitaksesi tiedostot, joilla on virheelliset tarkistussummat.

### Kun jokin menee pieleen

Jos synkronointi epäonnistuu kesken kaiken — esimerkiksi katkennut yhteys — lisäosa raportoi, mitä se oli jo soveltanut ja tarjoaa **Yritä uudelleen**, joka jatkaa epäonnistuneesta vaiheesta sen sijaan, että aloittaisi alusta. Lataettu kopio etäpuusta pidetään, joten uudelleen yrittäminen ei lataa ja vertaa sitä toista kertaa.

Epäonnistumisen tekniset tiedot ovat saatavilla *Yksityiskohdat* laajennuksen takana, ja niissä on painike niiden kopioimiseen virheraporttia varten.

## Vianetsintä

### Virheenkorjauslokitus

Jos kohtaat ongelmia Sync-lisäosan kanssa, käynnistä Gramps debug-lokitus päällä [käynnistämällä Gramps komentoriviltä](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) seuraavalla vaihtoehdolla:

```bash
gramps --debug grampswebsync
```

Tämä tulostaa monia hyödyllisiä lokituslauseita komentoriville, jotka auttavat sinua tunnistamaan ongelman syyn.

### Palvelimen tunnistetiedot

Jos yhdistäminen epäonnistuu, tarkista palvelimen URL-osoite, käyttäjänimesi ja salasanasi.

### Lisäosa kieltäytyy yhdistämästä

Jos lisäosa ilmoittaa, että palvelimen Gramps Web API -versio on liian vanha tai liian uusi, tai että taustatehtäväjonoa ei ole määritetty, katso [Palvelinvaatimukset](#server-requirements) yllä. Nämä tarkistetaan ennen mitään muuta, joten viesti nimeää ongelman suoraan.

### Oikeusongelmat

Jos kohtaat virheen, joka liittyy oikeuksiin, tarkista Gramps Web -käyttäjätilisi käyttäjärooli. Voit soveltaa muutoksia etädatabaselle vain, jos olet käyttäjä, jolla on muokkaaja-, omistaja- tai ylläpitäjärooli.

### Odottamattomat tietokannan muutokset

Jos synkronointityökalu havaitsee muutoksia, joita et usko tapahtuneen, voi olla, että jossakin tietokannassa on epäjohdonmukaisuuksia, jotka hämäävät Grampsia havaitsemaan eron, tai että aika on epäsynkronoitu paikallisen tietokoneesi ja palvelimesi välillä.

Tarkista, että molempien koneiden kellot ovat oikein asetettuja (huomaa, aikavyöhyke ei vaikuta, koska työkalu käyttää Unix-aikaleimoja, jotka ovat aikavyöhykkeestä riippumattomia).

Voit myös suorittaa tarkistus- ja korjaustyökalun paikalliselle tietokannallesi ja katsoa, auttaako tämä.

Brutaali mutta tehokas menetelmä varmistaa, että paikallisen tietokannan epäjohdonmukaisuudet eivät aiheuta väärien positiivisten tulosten syntymistä, on viedä tietokanta Gramps XML:ään ja tuoda se takaisin uuteen, tyhjään tietokantaan. Tämä on häviötön operaatio, mutta varmistaa, että kaikki tiedot tuodaan johdonmukaisesti.

!!! tip
    Jos lisäosa ehdottaa hälyttävän suurta määrää poistamisia, tarkista ensin yläreuna: se nimeää palvelimella olevan perhepuun, johon olet kirjoittamassa. Synkronoiminen palvelimen kanssa, joka pitää *eri* puuta, tuottaa juuri tämän oireen.

### Aikakatkaisuvirheet

Synkronointi palvelimelle käsitellään taustatyöntekijän avulla, joten pitkään kestävät synkronoinnit eivät saisi aikakatkaista. Palvelin, jolla ei ole määritetty tehtäväjonoa, hylätään yhteyden muodostamisen aikana tästä syystä — katso [Palvelinvaatimukset](#server-requirements).

Lisäosan pyynnöt palvelimelle aikakatkaistaan 60 sekunnin kuluttua ilman vastausta, joten saavuttamaton palvelin raportoi yhteysvirheen sen sijaan, että se joutuisi odottamaan loputtomasti.

### Odottamattomat mediakuvavirheet

Jos mediakuvan lataaminen epäonnistuu, se johtuu usein siitä, että tiedoston tarkistussumma levyllä ei vastaa paikallisessa Gramps-tietokannassa olevaa tarkistussummaa. Tämä tapahtuu usein muokattavien tiedostojen, kuten toimistodokumenttien, kohdalla, joita on muokattu Grampsin ulkopuolella. Käytä Gramps Media Verify -lisäosaa korjataksesi kaikkien mediakuvien tarkistussummat.

### Pyydä apua

Jos mikään yllä olevista ei auta, voit pyytää yhteisöltä apua julkaisemalla [Gramps-foorumin Gramps Web -kategoriassa](https://gramps.discourse.group/c/gramps-web/28). Varmista, että toimitat:

- Gramps Web Sync -lisäosan version (ja käytä viimeisintä julkaistua versiota, kiitos) — se näkyy synkronointisivun alareunassa, palvelimen Web API -version vieressä
- käyttämäsi Gramps Desktop -version
- Grampsin virheenkorjauslokituksen tulosteen, joka on otettu käyttöön yllä kuvatulla tavalla
- Gramps Webin versiotiedot (löydät sen Asetukset/Versiotiedot -kohdasta)
- kaikki tiedot, jotka voit antaa Gramps Web -asennuksestasi (itse isännöity, Grampshub, ...)
- Gramps Web -palvelinlokiesi tulosteet, jos sinulla on pääsy niihin (dockerin käytön yhteydessä: `docker compose logs --tail 100 grampsweb` ja `docker compose logs --tail 100 grampsweb-celery`)

## Taustatietoja: miten lisäosa toimii

Jos olet utelias siitä, miten lisäosa todella toimii, löydät lisää yksityiskohtia tästä osasta.

Lisäosan tarkoitus on pitää paikallinen Gramps-tietokanta synkronoituna etä-Gramps Web -tietokannan kanssa, jotta sekä paikalliset että etämuutokset (yhteistyömuokkaus) ovat mahdollisia.

Se ei **sovi**

- Synkronointiin tietokannan kanssa, joka ei ole suora johdannainen (alkaen tietokannan kopiosta tai Gramps XML -vienti/tuonti) paikallisesta tietokannasta
- Kahden tietokannan yhdistämiseen, joilla on suuri määrä muutoksia molemmilla puolilla, jotka tarvitsevat manuaalista huomiota yhdistämistä varten. Käytä tähän erinomaisia [Tuontiyhdistämistyökaluja](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Työkalun toimintaperiaatteet ovat hyvin yksinkertaisia:

- Se vertaa paikallisia ja etädatabaaseja
- Jos eroja on, se tarkistaa viimeisen identtisen objektin aikaleiman, kutsutaan sitä **t**:ksi
- Jos objekti, joka on muuttunut viimeksi **t**:n jälkeen, on olemassa yhdessä tietokannassa, mutta ei toisessa, se synkronoidaan molempiin (olettaen uusi objekti)
- Jos objekti, joka on muuttunut viimeksi ennen **t**:tä, puuttuu yhdestä tietokannasta, se poistetaan molemmista (olettaen poistettu objekti)
- Jos objekti on erilainen, mutta muuttunut vain yhdessä tietokannassa **t**:n jälkeen, synkronoidaan toiseen (olettaen muokattu objekti)
- Jos objekti on erilainen, mutta muuttunut molemmissa tietokannoissa **t**:n jälkeen, ne yhdistetään (olettaen ristiriitainen muokkaus)

Viimeisen onnistuneen synkronoinnin aikaleima tallennetaan myös erikseen jokaiselle palvelimelle, ja sitä käytetään **t**:nä, kun se on uudempi kuin uusin identtinen objekti.

Tämä algoritmi on yksinkertainen ja kestävä, koska se ei vaadi synkronointihistorian seuraamista. Se toimii kuitenkin parhaiten, kun *synkronoidaan usein*.
