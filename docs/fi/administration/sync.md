# Synkronoi Gramps Web ja Gramps Desktop

*Gramps Web Sync* on lisäosa Grampsille, joka mahdollistaa Gramps-tietokannan synkronoinnin työpöytätietokoneellasi Gramps Webin kanssa, mukaan lukien mediafilet.

!!! warning
    Kuten minkä tahansa synkronointityökalun kanssa, älä pidä tätä varmuuskopiointityökaluna. Satunnainen poistaminen yhdellä puolella leviää toiselle puolelle. Varmista, että luot säännöllisiä varmuuskopioita (Gramps XML -muodossa) perheipuustasi.

!!! info
    Dokumentaatio viittaa Gramps Web Sync -lisäosan uusimpaan versioon. Käytä Grampsin lisäosahallintaa päivittääksesi lisäosan uusimpaan versioon tarvittaessa.

## Asennus

Lisäosa vaatii Gramps 6.0:n, joka toimii Python 3.10:ssä tai uudempana.
Se on saatavilla Gramps Desktopissa ja se voidaan asentaa [tavallisella tavalla](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Varmista, että käytät samaa Gramps-versiota työpöydälläsi kuin palvelimellasi. Katso [Get Help](../help/help.md) -osio saadaksesi selville, mikä Gramps-versio palvelimellasi on. Gramps-version muoto on `MAJOR.MINOR.PATCH`, ja `MAJOR` ja `MINOR` on oltava samat verkkosivustolla ja työpöydällä.

Valinnainen vaihe:

??? note inline end "Gnome keyring bug"
    Tällä hetkellä on olemassa [bugi python keyringissä](https://github.com/jaraco/keyring/issues/496), joka vaikuttaa moniin Gnome-työpöytäkonfiguraatioihin. Saatat joutua luomaan konfiguraatiotiedoston `~/.config/python_keyring/keyringrc.cfg` ja muokkaamaan sitä näyttämään tältä:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Asenna `keyring` (esim. `sudo apt install python3-keyring` tai `sudo dnf install python3-keyring`) voidaksesi tallentaa API-salasanan turvallisesti järjestelmäsi salasanojen hallintaan.

## Käyttö

Kun lisäosa on asennettu, se on saatavilla Grampsissa kohdassa *Työkalut > Perhepuun käsittely > Gramps&nbsp;Web&nbsp;Sync*. Kun se on käynnistetty ja vahvistat dialogin, että kumoamishistoria hylätään, taikuri ohjaa sinut synkronointivaiheiden läpi. Huomaa, että paikalliseen puuhun tai palvelimelle ei tehdä muutoksia ennen kuin vahvistat ne nimenomaisesti.

### Vaihe 1: syötä palvelimen tunnistetiedot

Työkalu kysyy sinulta Gramps Web -instanssisi perus-URL-osoitetta (esim. `https://mygrampsweb.com/`), käyttäjänimeäsi ja salasanaasi. Tarvitset tilin, jossa on vähintään muokkausoikeudet, jotta voit synkronoida muutoksia takaisin etä-tietokantaasi. Käyttäjänimi ja URL tallennetaan selkokielisenä Gramps-käyttäjähakemistoosi, salasana tallennetaan vain, jos `keyring` on asennettu (katso yllä).

### Vaihe 2: tarkista muutokset

Kun olet vahvistanut tunnistetietosi, työkalu vertaa paikallisia ja etä-tietokantoja ja arvioi, onko eroja. Jos eroja on, se näyttää luettelon objektimuutoksista (missä objekti voi olla henkilö, perhe, tapahtuma, paikka jne.), jotka kuuluvat johonkin seuraavista kategorioista:

- lisätty paikallisesti
- poistettu paikallisesti
- muokattu paikallisesti
- lisätty etäisesti
- poistettu etäisesti
- muokattu etäisesti
- muokattu samanaikaisesti (eli molemmilla puolilla)

Työkalu käyttää aikaleimoja arvioidakseen, mikä puoli on uudempi jokaiselle objektille (katso "Tausta" alla, jos olet kiinnostunut yksityiskohdista).

Jos muutokset näyttävät odotetuilta, voit napsauttaa "Käytä" soveltaaksesi tarvittavat muutokset paikallisiin ja etä-tietokantoihin.

!!! tip "Edistynyt: Synkronointitila"
    Muutosten luettelon alapuolella voit valita synkronointitilan.
    
    Oletus, **kaksisuuntainen synkronointi**, tarkoittaa, että se soveltaa muutoksia molemmille puolille (paikallinen ja etäinen) toistamalla havaitut muutokset (paikallisesti lisätyt objektit lisätään etäpuolelle jne.). Molemmilla puolilla muokatut objektit yhdistetään ja päivitetään myös molemmille puolille.

    Vaihtoehto **nollaa etä paikalliseksi** varmistaa sen sijaan, että etäinen Gramps-tietokanta näyttää täsmälleen samalta kuin paikallinen. Kaikki objektit, jotka on havaittu "lisätty etäisesti", poistetaan jälleen, objektit, jotka on havaittu "poistettu etäisesti", lisätään jälleen jne. *Muutoksia ei sovelleta paikalliseen Gramps-tietokantaan.*

    Vaihtoehto **nollaa paikallinen etäiseksi** toimii päinvastoin ja asettaa paikallisen tilan etä-tietokannan tilaksi. *Muutoksia ei sovelleta etä-tietokantaan.*

    Lopuksi, vaihtoehto **yhdistä** on samanlainen kuin kaksisuuntainen synkronointi siinä, että se muokkaa molempia tietokantoja, mutta se *ei poista mitään objekteja*, vaan palauttaa kaikki vain yhdeltä puolelta poistettavat objektit.

### Vaihe 3: synkronoi mediafilet

*Sen jälkeen*, kun tietokannat on synkronoitu, työkalu tarkistaa, onko uusia tai päivitettyjä mediafilejä. Jos se löytää sellaisia, se näyttää luettelon ja kysyy vahvistusta tarvittavien tiedostojen lataamiseen.

Huomaa seuraavat rajoitukset mediafilejen synkronoinnissa:

- Jos paikallisella tiedostolla on eri tarkistusluku kuin Gramps-tietokannassa tallennetulla tiedostolla (tämä voi tapahtua esim. Word-tiedostoille, kun niitä muokataan sen jälkeen, kun ne on lisätty Grampsiin), lataus epäonnistuu virheilmoituksella.
- Työkalu ei tarkista kaikkien paikallisten tiedostojen eheyttä, joten jos paikallinen tiedosto löytyy polulta, joka on tallennettu mediaobjektille, mutta tiedosto on erilainen kuin palvelimella oleva tiedosto, työkalu ei havaitse sitä. Käytä Media Verify -lisäosaa havaitaksesi tiedostot, joilla on virheelliset tarkistusluvut.

## Vianetsintä

### Virheenkorjauslokitus

Jos kohtaat ongelmia Sync-lisäosan kanssa, käynnistä Gramps virheenkorjauslokitus päällä [käynnistämällä Gramps komentoriviltä](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) seuraavalla vaihtoehdolla:

```bash
gramps --debug grampswebsync
```

Tämä tulostaa monia hyödyllisiä lokiviestejä komentoriville, jotka auttavat sinua tunnistamaan ongelman syyn.

### Palvelimen tunnistetiedot

Jos ensimmäinen vaihe epäonnistuu, tarkista palvelimen URL-osoite, käyttäjänimesi ja salasanasi.

### Oikeusongelmat

Jos kohtaat virheen, joka liittyy oikeuksiin, tarkista Gramps Web -käyttäjätilisi käyttäjärooli. Voit soveltaa muutoksia etä-tietokantaan vain, jos olet käyttäjä, jolla on muokkaaja-, omistaja- tai ylläpitäjärooli.

### Odottamattomat tietokannan muutokset

Jos synkronointityökalu havaitsee muutoksia, joita et usko tapahtuneen, voi olla, että jossakin tietokannassa on epäjohdonmukaisuuksia, jotka johtavat Grampsin havaitsemaan eron, tai että kellot ovat epäsynkronoituneita paikallisen tietokoneesi ja palvelimesi välillä.

Varmista, että molempien koneiden kellot on asetettu oikein (huomaa, että aikavyöhykkeellä ei ole merkitystä, koska työkalu käyttää Unix-aikaleimoja, jotka ovat aikavyöhykkeestä riippumattomia).

Voit myös suorittaa tarkistus- ja korjaustyökalun paikalliselle tietokannallesi ja katsoa, auttaako tämä.

Brute-force, mutta tehokas menetelmä varmistaa, että paikallisen tietokannan epäjohdonmukaisuudet eivät aiheuta väärien positiivisten tulosten syntymistä, on viedä tietokanta Gramps XML:ään ja tuoda se takaisin uuteen, tyhjään tietokantaan. Tämä on häviötön operaatio, mutta varmistaa, että kaikki tiedot tuodaan johdonmukaisesti.

### Aikakatkaisuvirheet

Jos kohtaat aikakatkaisuvirheitä (esim. HTTP-tilatunnus 408 -virhe tai muu virheilmoitus, joka sisältää sanan "timeout"), se johtuu todennäköisesti suuresta määrästä muutoksia, jotka on synkronoitava etäpuolelle yhdistettynä palvelimesi asetuksiin.

Synkronointilisäosan versioissa, jotka ovat aikaisempia kuin v1.2.0, ja Gramps Web API -versioissa, jotka ovat aikaisempia kuin v2.7.0 (katso version tietotabista Gramps Webissä), palvelinpuolen synkronointi käsiteltiin yhdessä pyynnössä, joka aikakatkaisi, riippuen palvelimen kokoonpanosta, minuutista korkeintaan muutamaan minuuttiin. Suurissa synkronoinneissa (kuten tuhansien objektien tuominen paikalliseen tietokantaan tai yrittäminen synkronoida koko paikallinen tietokanta tyhjään palvelinpuolen tietokantaan) tämä voi olla liian lyhyt.

Jos käytät synkronointilisäosaa v1.2.0 tai uudempi ja Gramps Web API:ta v2.7.0 tai uudempi, palvelinpuolen synkronointi käsitellään taustatyöntekijän toimesta ja voi kestää hyvin pitkään (edistymispalkki näytetään) ja aikakatkaisuvirheitä ei pitäisi esiintyä.

### Odottamattomat mediafilevirheet

Jos mediafilejen lataaminen epäonnistuu, se johtuu usein siitä, että tiedoston tarkistusluku levyllä ei vastaa paikallisessa Gramps-tietokannassa olevaa tarkistuslukua. Tämä tapahtuu usein muokattavissa tiedostoissa, kuten toimistodokumenteissa, joita on muokattu Grampsin ulkopuolella. Käytä Gramps Media Verify -lisäosaa korjataksesi kaikkien mediafilejen tarkistusluvut.

### Pyydä apua

Jos mikään yllä olevista ei auta, voit pyytää yhteisöltä apua julkaisemalla [Gramps Web -kategorian Gramps-foorumissa](https://gramps.discourse.group/c/gramps-web/28). Varmista, että annat:

- Gramps Web Sync -lisäosan version (ja käytä viimeisintä julkaistua versiota, kiitos)
- Käyttämäsi Gramps Desktopin version
- Grampsin virheenkorjauslokituksen tulosteen, joka on otettu käyttöön yllä kuvatulla tavalla
- Gramps Webin version tiedot (löydät sen kohdasta Asetukset/Versiotiedot)
- Kaikki tiedot, joita voit antaa Gramps Web -asennuksestasi (itse isännöity, Grampshub, ...)
- Gramps Web -palvelinlokiesi tulosteet, jos sinulla on pääsy niihin (dockerin käytön yhteydessä: `docker compose logs --tail 100 grampsweb` ja `docker compose logs --tail 100 grampsweb-celery`)

## Tausta: miten lisäosa toimii

Jos olet utelias siitä, miten lisäosa todella toimii, voit löytää lisää yksityiskohtia tästä osiosta.

Lisäosa on tarkoitettu pitämään paikallinen Gramps-tietokanta synkronoituna etä-Gramps Web -tietokannan kanssa, jotta sekä paikalliset että etäiset muutokset (yhteistyömuokkaus) ovat mahdollisia.

Se **ei sovellu**

- Synkronoimaan tietokannan kanssa, joka ei ole suora johdannainen (alkaen tietokannan kopioista tai Gramps XML -vienti/tuonti) paikallisesta tietokannasta
- Yhdistämään kahta tietokantaa, joissa on suuri määrä muutoksia molemmilla puolilla, jotka vaativat manuaalista huomiota yhdistämiseen. Käytä tätä tarkoitusta varten erinomaista [Tuontiyhdistämistyökalua](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Työkalun toimintaperiaatteet ovat hyvin yksinkertaiset:

- Se vertaa paikallisia ja etä-tietokantoja
- Jos eroja on, se tarkistaa viimeisimmän identtisen objektin aikaleiman, kutsutaan sitä **t**:ksi
- Jos objekti on muuttunut viimeisimmän **t**:n jälkeen yhdessä tietokannassa mutta ei toisessa, se synkronoidaan molempiin (olettaen, että uusi objekti)
- Jos objekti on muuttunut viimeksi ennen **t**:tä ja se puuttuu yhdestä tietokannasta, se poistetaan molemmista (olettaen, että poistettu objekti)
- Jos objekti on erilainen mutta muuttunut **t**:n jälkeen vain yhdessä tietokannassa, synkronoidaan toiseen (olettaen, että muokattu objekti)
- Jos objekti on erilainen mutta muuttunut **t**:n jälkeen molemmissa tietokannoissa, ne yhdistetään (olettaen, että ristiriitainen muokkaus)

Tämä algoritmi on yksinkertainen ja kestävä, koska se ei vaadi synkronointihistorian seuraamista. Se toimii kuitenkin parhaiten, kun *synkronoidaan usein*.
