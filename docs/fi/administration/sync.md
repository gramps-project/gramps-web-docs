# Synkronoi Gramps Web ja Gramps Desktop

*Gramps Web Sync* on Grampsin lisäosa, joka synkronoi Gramps-tietokannan työpöytätietokoneellasi Gramps Webin kanssa, mukaan lukien mediafilet. Muutokset, joita tehdään kummallakin puolella, siirtyvät toiselle puolelle, joten voit työskennellä paikallisesti ja verkossa samalla perhepuulla.

Kuten kaikissa synkronointityökaluissa, tämä ei ole varmuuskopio: jos poistat jotain yhdeltä puolelta, se poistetaan myös toiselta puolelta. Pidä säännöllisiä varmuuskopioita perhepuustasi Gramps XML -muodossa.

## Asennus

Lisäosa vaatii Gramps 6.0:n, joka toimii Python 3.10:llä tai uudempana. Se on saatavilla Gramps Desktopissa ja se voidaan asentaa [tavallisella tavalla](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Tämä dokumentaatio kuvaa lisäosan uusinta versiota; käytä Grampsin lisäosahallintaa päivittääksesi sen tarvittaessa.

Työpöytäsi ja palvelimesi on oltava samassa Gramps-versiossa. Versio on muotoa `MAJOR.MINOR.PATCH`, ja `MAJOR` ja `MINOR` on oltava samat. Katso [Hanki apua](../help/help.md) saadaksesi selville, mikä Gramps-versio palvelimellasi on.

### Palvelimen vaatimukset

Lisäosa tarkistaa kaksi asiaa palvelimestasi heti, kun se yhdistää, ennen kuin mitään ladataan, ja pysähtyy viestin kanssa, jos jokin ei täyty:

- **Gramps Web API versio 3.x.** Tämä lisäosan versio, Gramps 6.0:lle, toimii Gramps Web API 3:n kanssa. Vanhempi palvelin tarvitsee päivityksen; palvelin, joka käyttää *uudempaa* API-pääversiota, tarvitsee uuden version Grampsista, ei uutta lisäosaa, koska jokainen Gramps-julkaisulinja parittaa yhden API-version kanssa. Voit löytää palvelimesi version kohdasta *Asetukset ▸ Versiotiedot* Gramps Webissä.
- **Taustatehtäväjono.** Muutokset sovelletaan palvelimella taustatehtävänä. Ilman tehtäväjonoa tämä toimisi synkronoidusti ja aikakatkaisi minkä tahansa todellisen perhepuun.

Muutosten soveltamiseksi etädatabasesi tarvitset tilin, jolla on rooli editori, omistaja tai ylläpitäjä.

### Salasanasi tallentaminen (valinnainen)

Asenna `keyring` (esim. `sudo apt install python3-keyring` tai `sudo dnf install python3-keyring`) tallentaaksesi API-salasanan järjestelmäsi salasananhallintaan. Jos keyringiä ei voida käyttää, lisäosa ilmoittaa siitä ja jatkaa ilman sitä – sinulta kysytään vain salasana joka kerta.

Grampsin **Snap**-paketissa järjestelmän keyring on estetty eristyksen vuoksi, kunnes yhdistät käyttöliittymän kerran. Lisäosa näyttää tämän komennon, kun se havaitsee tilanteen:

```bash
snap connect gramps:password-manager-service
```

Monilla Gnome-työpöytäkonfiguraatioilla [bugi python keyringissä](https://github.com/jaraco/keyring/issues/496) tarkoittaa, että sinun on luotava konfiguraatiotiedosto `~/.config/python_keyring/keyringrc.cfg` seuraavalla sisällöllä:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Käyttö

Lisäosa on saatavilla Grampsissa kohdassa *Työkalut ▸ Perhepuun käsittely ▸ Gramps&nbsp;Web&nbsp;Sync*. Kun olet vahvistanut dialogin varoituksen siitä, että kumoamis historia hylätään, synkronointiwindows avautuu. Muutoksia ei sovelleta paikalliseen puuhusi tai palvelimelle ennen kuin vahvistat ne nimenomaisesti.

Ikkunan yläreunassa oleva nauha nimeää perhepuun, jonka kanssa synkronoidaan, tilin ja osoitteen, johon se kuuluu, sekä milloin se viimeksi synkronoitiin. Alareunassa näkyy lisäosan ja palvelimen Web API:n versio, mikä on hyödyllistä ongelman raportoinnissa.

### Yhdistäminen

Jos olet synkronoinut tämän perhepuun aiemmin ja salasanasi on tallennettu, lisäosa yhdistää heti avautuessaan ja siirtyy suoraan vertailuun. Muuten se kysyy Gramps Web -instanssisi perus-URL-osoitetta (esimerkki: `https://mygrampsweb.com/`), käyttäjänimeäsi ja salasanaasi.

URL-osoite ja käyttäjänimi tallennetaan selkokielellä Gramps-käyttäjäkansioosi. Salasana tallennetaan järjestelmäsi salasananhallintaan vain, jos jätät **Muista salasana** valittuna; valinnan poistaminen poistaa jo tallennetun salasanan kyseiselle palvelimelle. Jos syöt osoitteen, joka alkaa `http://` sen sijaan, että `https://`, lisäosa varoittaa sinua kirjoittaessasi, koska salasanasi lähetettäisiin selkokielellä.

Jokainen palvelin, jonka kanssa synkronoit, tallennetaan erikseen, yhdessä oman tietueensa kanssa siitä, milloin se viimeksi synkronoitiin, joten voit vuorotella kahden palvelimen välillä häiritsemättä kumpaakaan. Jokainen merkintä tallentaa myös, mikä paikallinen perhepuu siitä viimeksi synkronoitiin. Lisäosa yhdistää vain itsenäisesti, kun se vastaa avointa puuta; muuten se näyttää yhteystiedot ja odottaa, että painat *Yhdistä*.

Kaksi toimintoa on saatavilla, kun mitään ei kirjoiteta:

- **Vaihda palvelinta…**, yläreunassa, palaa yhteystietoihin, jotta voit osoittaa tämän puun eri palvelimelle. Se keskeyttää meneillään olevan vertailun sen sijaan, että saisi sinut odottamaan sen loppuun.
- **Unohda tämä palvelin**, yhteyspaneelissa, poistaa tallennetun osoitteen, käyttäjänimen ja salasanan sekä tietueen siitä, milloin tämä puu viimeksi synkronoitiin. Seuraava synkronointi vertaa sitten kahta puuta alusta alkaen.

### Muutosten tarkastelu

Lisäosa vertaa paikallisia ja etädatabasesi ja näyttää toimenpiteet, joita se ehdottaa suoritettavaksi, ryhmiteltynä sen mukaan, mikä tietokanta niitä muuttaa:

```
▾ Muutetaan tällä tietokoneella (7 objektia)
    ▾ Lisää 3 objektia
        Henkilö   John Smith        I0123
    ▾ Päivitä 4 objektia
        …
▾ Muutetaan palvelimella (5 objektia)
    …
```

Jokainen rivi nimeää objektin, joten voit kertoa, kuka tai mikä on vaikuttanut, sen sijaan että näkisit vain Gramps ID:n. Jos jotain on poistettava, luettelon ylle tulee huomautus siitä, kuinka monta objektia ja kummalla puolella.

Paina **Käytä** suorittaaksesi sen, mitä luettelo kuvaa.

Synkronointiwindows ei estä muuta Grampsia, joten voit jatkaa työskentelyä, kun luettelo on avoinna. Jos muokkaat vaikuttavaa objektia sillä välin, lisäosa huomaa sen, kun painat Käytä, pysähtyy ilman muutoksia ja pyytää sinua vertailemaan uudelleen.

#### Synkronointitila

Synkronointitila valitaan muutosten luettelon yläpuolella. Sen muuttaminen rakentaa luettelon uudelleen, koska tila päättää, mitä jokainen ero tulee.

- **Kaksisuuntainen synkronointi** (oletusarvo) – molemmilta puolilta tulevat muutokset yhdistetään. Molemmissa paikoissa muokatut objektit yhdistetään.
- **Nollaa palvelin vastaamaan tätä tietokonetta** – palvelin tehdään vastaamaan tätä tietokonetta. Palvelimella vain muutetut asiat hylätään.
- **Nollaa tämä tietokone vastaamaan palvelinta** – tämä tietokone tehdään vastaamaan palvelinta. Täällä vain muutetut asiat hylätään.

**Yhdistämistila**, joka oli saatavilla versioissa ennen 1.5, on poistettu. Se poikkesi kaksisuuntaisesta synkronoinnista vain palauttamalla objektit, jotka oli poistettu yhdeltä puolelta, sen sijaan että olisi levittänyt poistamisen. Jos olet luottanut siihen, käytä kaksisuuntaista synkronointia ja palauta kaikki, mitä haluat säilyttää varmuuskopiosta.

### Mediafilet

Mediafilejä käsitellään osana samaa vahvistusta, ei erillisenä vaiheena. Jos tiedostoja on siirrettävä, luettelon alapuolella oleva valintaruutu tarjoaa niiden siirtämistä:

```
[x] Siirrä myös 12 mediafileä (4 ladattavaa, 8 ladattavaa)
```

Poista valinta, jotta voit synkronoida objektimuutokset koskematta tiedostoihin.

Tiedostot, joita puuttuu *molemmilta* puolilta, luetellaan erikseen, koska niille ei voida tehdä mitään:

```
2 mediafileä puuttuu molemmilta puolilta eikä niitä voida siirtää.
```

Mediafilejen synkronoinnilla on kaksi rajoitusta:

- Jos paikallisella tiedostolla on eri tarkistusnumero kuin Gramps-tietokannassa tallennetulla (tämä voi tapahtua esimerkiksi Word-tiedostoille, joita on muokattu Grampsiin lisäämisen jälkeen), lataus epäonnistuu virheilmoituksella.
- Työkalu ei tarkista kaikkien paikallisten tiedostojen eheyttä. Jos tiedosto löytyy polulta, joka on tallennettu mediaobjektille, mutta eroaa palvelimella olevasta tiedostosta, työkalu ei havaitse sitä. Käytä Media Verify -lisäosaa löytääksesi tiedostoja, joiden tarkistusnumerot ovat virheellisiä.

### Jos synkronointi epäonnistuu

Jos synkronointi epäonnistuu osittain – esimerkiksi katkenneen yhteyden vuoksi – lisäosa raportoi, mitä se oli jo soveltanut ja tarjoaa **Yritä uudelleen**, mikä jatkaa epäonnistuneesta vaiheesta sen sijaan, että aloittaisi alusta. Lataus etäpuun kopio säilytetään, joten uudelleen yrittäminen ei lataa ja vertaa sitä toista kertaa.

Epäonnistumisen tekniset tiedot ovat saatavilla *Yksityiskohdat*-laajentimen takana, ja siellä on painike niiden kopioimiseen virheraporttia varten.

## Vianetsintä

**Odottamattomat muutokset.** Jos lisäosa ehdottaa hälyttävää määrää poistamisia, tarkista ensin yläreuna: se nimeää perhepuun palvelimella, johon olet kirjoittamassa. Synkronointi puuta palvelimelle, joka pitää *erilaista* puuta, tuottaa juuri tämän oireen.

Muuten, odottamattomat erot voivat johtua epäjohdonmukaisuuksista jommassakummassa tietokannassa tai kelloista, jotka ovat epäsynkronoituneita tietokoneesi ja palvelimesi välillä. Tarkista, että molemmat kellot on asetettu oikein (aikavyöhykkeellä ei ole väliä, koska työkalu käyttää Unix-aikaleimoja) ja suorita tarkistus- ja korjaustyökalu paikalliselle tietokannallesi. Viimeisenä keinona vie paikallinen tietokantasi Gramps XML:ään ja tuo se takaisin uuteen, tyhjään tietokantaan. Tämä on häviötön operaatio, mutta varmistaa, että kaikki tiedot tallennetaan johdonmukaisesti.

**Mediafile-virheet.** Epäonnistunut lataus johtuu usein tiedoston tarkistusnumeron ja levyllä olevan tiedoston tarkistusnumeron erosta, mikä tapahtuu muokattavissa tiedostoissa, kuten toimistodokumenteissa, joita on muokattu Grampsin ulkopuolella. Käytä Gramps Media Verify -lisäosaa korjataksesi tarkistusnumerot.

**Oikeusvirheet.** Tarkista Gramps Web -käyttäjätilisi rooli: vain editorit, omistajat ja ylläpitäjät voivat soveltaa muutoksia etädatabasesi.

### Pyydä apua

Jos mikään edellä mainituista ei auta, kysy yhteisöltä julkaisemalla [Gramps Web -kategoria Gramps-foorumissa](https://gramps.discourse.group/c/gramps-web/28). Ole hyvä ja anna:

- Gramps Web Sync -lisäosan versio, joka näkyy synkronointiwindowsin alareunassa palvelimen Web API -version vieressä (ja käytäthän viimeisintä julkaistua versiota)
- käyttämäsi Gramps Desktop -version
- Gramps Webin versiotiedot, jotka löytyvät kohdasta *Asetukset ▸ Versiotiedot*
- kaikki tiedot Gramps Web -asennuksestasi (itse isännöity, Grampshub, ...)
- Gramps Web -palvelinlokiesi tulosteet, jos sinulla on pääsy niihin (Dockerin käytön yhteydessä: `docker compose logs --tail 100 grampsweb` ja `docker compose logs --tail 100 grampsweb-celery`)

Jos sinulta pyydetään virheenkorjauslokia, käynnistä Gramps [komentoriviltä](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) virheenkorjauksen lokitus päällä ja toista ongelma:

```bash
gramps --debug grampswebsync
```

## Taustatiedot: kuinka lisäosa toimii

Lisäosan tarkoitus on pitää paikallinen Gramps-tietokanta synkronoituna etä-Gramps Web -tietokannan kanssa, mahdollistaen sekä paikalliset että etämuutokset (yhteistyömuokkaus).

Se ei **sovi**

- synkronoitavaksi tietokannan kanssa, joka ei ole suora johdannainen (alkaen tietokannan kopio tai Gramps XML -vienti/tuonti) paikallisesta tietokannasta,
- yhdistää kahta tietokantaa, joilla on suuri määrä muutoksia kummallakin puolella, jotka vaativat manuaalista huomiota yhdistämistä varten. Käytä tähän erinomaisia [Tuontiyhdistämistyökaluja](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Toimintaperiaatteet ovat yksinkertaisia:

- Se vertaa paikallisia ja etädatabasesi.
- Jos eroja on, se tarkistaa viimeisimmän identtisen objektin aikaleiman, kutsutaan sitä **t**.
- Jos objekti on muuttunut äskettäin kuin **t** on olemassa yhdessä tietokannassa, mutta ei toisessa, se synkronoidaan molempiin (olettaen uusi objekti).
- Jos objekti on muuttunut viimeksi ennen **t**:tä ja puuttuu yhdestä tietokannasta, se poistetaan molemmista (olettaen poistettu objekti).
- Jos objekti on erilainen, mutta muuttunut vain yhdessä tietokannassa **t**:n jälkeen, synkronoi se toiseen (olettaen muokattu objekti).
- Jos objekti on erilainen, mutta muuttunut **t**:n jälkeen molemmissa tietokannoissa, yhdistä ne (olettaen ristiriitainen muokkaus).

Viimeisen onnistuneen synkronoinnin aika tallennetaan myös erikseen jokaiselle palvelimelle, ja sitä käytetään **t**:nä, kun se on uudempi kuin uusin identtinen objekti.

Tämä algoritmi on yksinkertainen ja kestävä, koska se ei vaadi synkronointihistorian seuraamista. Se toimii kuitenkin parhaiten, kun *synkronoidaan usein*.
