# Kuinka Gramps järjestää tietoja

Gramps Web tallentaa sukupuun ei kaaviona, vaan erillisinä objekteina – ihmisinä, perheinä, tapahtumina, paikkoina, lähteinä ja niin edelleen – jotka ovat toisiinsa linkitettyjä. Kun tiedät, miten nämä objektit liittyvät toisiinsa, tietojen syöttäminen muuttuu ennakoitavaksi: mitä tahansa, mihin haluat linkittää, on ensin oltava olemassa.

Gramps Web käyttää samaa tietomallia kuin Gramps Desktop, joten kaikki tällä sivulla pätee molempiin.

## Rakennuspalikat

| Objekti | Mitä se edustaa | Esimerkkejä |
|---|---|---|
| Henkilö | Yksilö | Sinä, isoäitisi |
| Perhe | Pari, heidän lapsensa tai molemmat | Vanhempasi ja heidän lapsensa |
| Tapahtuma | Jokin, mikä tapahtui, päivämäärällä ja paikalla | Syntymä, avioliitto, väestönlaskenta, maahanmuutto |
| Paikka | Maantieteellinen sijainti | Kylä, seurakunta, maa |
| Lähde | Asiakirja tai tietokokoelma | Seurakuntarekisteri, väestönlaskenta, kirja |
| Viittaus | Tietty viittaus lähteessä | Sivun 12, merkintä 3 seurakuntarekisterissä |
| Arkisto | Missä lähde säilytetään | Arkisto, kirjasto, verkkosivusto |
| Huomautus | Vapaa teksti | Transkriptio, tutkimusmuistiinpanot |
| Mediakohde | Tiedosto | Valokuva, skannattu todistus |

Jokaisella objektityypillä on oma luettelo Gramps Webissä, katso [Luettelot](lists.md).

## Ihmiset ja perheet

Vanhempia ja lapsia ei linkitetä suoraan toisiinsa, vaan **perheen** kautta. Perheessä voi olla enintään kaksi kumppania ja minkä tahansa määrän lapsia:

- Vanhempasi ja sinä olette linkitetty perheen kautta, jossa olet lapsi.
- Sisaruksesi ovat saman perheen muut lapset.
- Sinä ja puolisosi muodostatte toisen perheen, jossa olette kumppaneita yhdessä lastenne kanssa.

Henkilö voi olla lapsi yhdessä perheessä ja kumppani useissa. Jokaisella lapsella on suhde jokaiseen vanhempaan, kuten syntymä, adoptio tai lapsipuoli, ja jokaisella perheellä on suhteen tyyppi, kuten avioliitto tai rekisteröity parisuhde.

Tämä on syy siihen, miksi "vanhempien lisääminen" henkilöön tarkoittaa, että henkilö lisätään lapsena perheeseen – mitä [puukaavio](tree-edit.md) tekee puolestasi yhdessä vaiheessa.

## Tapahtumat

Syntymä, kuolema tai avioliitto ei ole henkilön kenttä, vaan oma **tapahtumansa**, jolla on tyyppi, päivämäärä, paikka ja kuvaus. Ihmiset linkitetään tapahtumaan **roolin** kautta: syntymän osalta rooli on "Pääasiallinen", kun taas joku muu voi olla linkitetty samaan tapahtumaan todistajana.

Tapahtumat, jotka koskevat paria, kuten avioliitto, kuuluvat perheelle eivätkä kummallekaan kumppanille. Tapahtuma voi myös olla useiden ihmisten jaettavissa – esimerkiksi väestönlaskentatieto, joka listaa koko talouden – sen sijaan, että se syötettäisiin kerran per henkilö.

Tämä vaikuttaa muokkaamiseen. Tapahtuma itsessään – sen tyyppi, päivämäärä, paikka ja kuvaus – on sama kaikille, jotka ovat siihen linkitettyjä, joten jaetun tapahtuman muokkaaminen yhden henkilön sivulta muuttaa sen kaikille heille. Muokkausdialogi listaa siksi muut osallistujat ensin, ja kentät tulevat muokattaviksi vasta **Muokkaa kaikille** -valinnan jälkeen. Se, mikä kuuluu yhden henkilön linkkiin tapahtumaan – rooli, ja viittaukset, huomautukset ja attribuutit, jotka koskevat vain kyseistä henkilöä – muokataan tapahtuman sivulla, **Osallistujat**-välilehdellä muokkaustilassa. Siellä voit myös lisätä ja poistaa osallistujia. Esimerkiksi kummivanhemman rooli ja huomautus "allekirjoitettu merkillä" kuuluvat kummivanhemman linkkiin kasteeseen, eivät itse kasteeseen.

## Jaetut objektit: paikat ja lähteet

Paikat, lähteet, viittaukset, arkistot, huomautukset ja mediakohteet ovat olemassa omana itsenään, ja minkä tahansa määrän muita objekteja voi viitata samaan. Tällä on muutamia seurauksia:

- **Luo kerran, valitse monta kertaa.** Kylä, jossa kymmenen esi-isääsi syntyi, on yksi paikka, joka valitaan kymmenessä syntymätapahtumassa. Jos korjaat sen nimen tai koordinaatit, korjaus pätee joka puolella.
- **Luo se ennen kuin valitset sen.** Gramps Webin lomakkeet valitsevat paikkoja ja lähteitä, jotka jo olemassa. Luo ensin uusi paikka tai lähde käyttämällä **+** (Lisää) -painiketta yläpalkissa.
- **Paikat ovat pesäkkäin.** Paikka voi olla suuremman paikan sisällä – kylä maakunnassa, maakunta maassa – joten sinun ei tarvitse toistaa koko hierarkiaa jokaiselle kylälle.
- **Lähteet ja viittaukset ovat erillisiä.** Lähde on seurakuntarekisteri kokonaisuudessaan; viittaus on tietty merkintä, joka tukee faktaa, sen sivun, päivämäärän ja luottamuksesi siihen. Monet viittaukset voivat osoittaa samaan lähteeseen.

Jos olet vahingossa luonut saman paikan tai lähteen kahdesti, voit [yhdistää kaksoiskappaleet](lists.md#merge).

## Objektin sivun muokkaaminen

Lähteen, arkiston tai mediakohteen sivulla napsauta otsikkoa muokkaustilassa muuttaaksesi sitä (mediakohteen kohdalla sen kuvausta). Paina Enter, napsauta ✓ tai napsauta muualle tallentaaksesi; paina Escape tai napsauta ✕ peruuttaaksesi.

Useimmat luettelot objektin sivulla säilyttävät antamasi järjestyksen, esimerkiksi tapahtumat, nimet, attribuutit, osoitteet, viittaukset tai perheen lapset. Muokkaustilassa valitse rivi ja siirrä se ylös- ja alaspainikkeilla tai vedä se uuteen sijaintiin: hiirellä paina riviä ja siirrä se; kosketusnäytöllä paina ja pidä riviä, kunnes se nousee. Paina Escape vetäessäsi peruuttaaksesi. Mediagalleriaa voidaan järjestää samalla tavalla, katso [Profiilikuvat](media.md#profile-pictures).

## Kotihenkilö

Kotihenkilö on henkilö, josta sukupuun kaaviot alkavat ja oletuslähtökohta raporteille. Katso [Ensimmäinen kirjautuminen](first-login.md) siitä, miten se asetetaan.

!!! huomautus "Eri kuin Gramps Desktop"
    Gramps Desktopissa Kotihenkilö tallennetaan sukupuun tietokantaan, joten se on sama kaikille, jotka avaavat kyseisen tietokannan. Gramps Web ei käytä sitä. Sen sijaan Kotihenkilö tallennetaan selaimeesi, erikseen jokaiselle puulle: sitä ei jaeta muiden käyttäjien kanssa, eikä se seuraa sinua toiseen selaimeen tai laitteeseen. Kun tulet puun Gramps Desktopista tai käytät Gramps Webiä toisella laitteella, sinun on asetettava se uudelleen.

## Suositeltu järjestys

Kun syötät uutta perhettä käsin, tämä järjestys välttää hyppimistä lomakkeiden välillä:

1. **Paikat ja lähteet.** Luo tarvitsemasi paikat ja, jos tallennat lähteitä, lähde, jota käytät.
2. **Ihmiset.** Lisää ihmiset heidän syntymä- ja kuolinpäivillään ja -paikoillaan. Tämä on nopeinta sukupuun kaavion muokkaustilassa, joka luo perheet puolestasi – katso [Aloita uusi puu](start-tree.md) ja [Sukupuun muokkaaminen](tree-edit.md).
3. **Lisätapahtumat.** Avaa perhe (esimerkiksi henkilön Suhteet-välilehdeltä) lisätäksesi avioliiton, ja henkilön sivu lisätäksesi muita tapahtumia.
4. **Viittaukset.** Henkilön, tapahtuman tai muun objektin Lähdeviittaukset-välilehdellä, jota lähde tukee, lisää uusi viittaus, valitse lähde ja syötä sivu.
5. **Huomautukset ja media.** Liitä transkriptioita, valokuvia ja skannauksia – katso [Lisää mediakuvia](media.md).

## Päivämäärien syöttäminen

Päivämäärä syötetään erillisinä vuosina, kuukausina ja päivinä, jotka voidaan myös täyttää päivämäärävalitsimella. Jätä pois osat, joita et tiedä: pelkkä vuosi on voimassa oleva päivämäärä. 
Sen sijaan, että arvaisit tarkkaa päivää, kuvaa mitä todella tiedät valitsemalla päivämäärän tyyppi kenttien yläpuolella olevilla siruilla. Vihje sirujen alla selittää valitun tyypin:

| Mitä tiedät | Tyyppi | Esimerkki |
|---|---|---|
| Tarkka päivämäärä tai osa siitä | Säännöllinen | 12. maaliskuuta 1850 tai vain 1850 |
| Suunnilleen oikea päivämäärä | Noin | noin 1850 |
| Rajoitus | Ennen, Jälkeen | ennen 1900 |
| Päivämäärä on jossain aikavälillä | Aikaväli | välillä 1850 ja 1855 (kentät "Varhaisin" ja "Viimeisin") |
| Jokin kesti tietyn ajan | Aika | ajalta 1850–1855 |

Aikavälin osalta kumpikin kahdesta päivämäärästä ("Alkaen" ja "Päättyen") voidaan jättää tyhjiksi, joten "alkaen 1850" tai "päättyen 1855" on Aika, jossa on vain yksi päivämäärä.

**Laatu** ja **Kalenteri** -kentät ovat kohdassa **Lisää vaihtoehtoja**, joka avautuu itsestään, kun päivämäärä käyttää kumpaakin niistä. Laatu tallentaa, miten päädyit päivämäärään: "Arvioitu" koulutetulle arvaukselle, "Laskettu" päivämäärälle, joka on johdettu muista tiedoista, kuten syntymävuosi, joka on laskettu kuolinikästä.

!!! varoitus "Noin ja arvioidut päivämäärät kattavat 50 vuotta kumpaankin suuntaan"
    Kun Gramps vertaa päivämääriä, se käsittelee "noin" -tyyppistä päivämäärää – ja mitä tahansa päivämäärää, jonka laatu on "Arvioitu" – aikavälinä, joka ulottuu 50 vuotta ennen ja 50 vuotta jälkeen annetun päivämäärän. Esimerkiksi, kun suodatat Ihmiset-luetteloa henkilöille, jotka ovat syntyneet välillä 1840 ja 1860, löydät myös henkilön, joka on syntynyt "noin 1880", koska tätä päivämäärää pidetään kattavan aikavälin 1830–1930. Samalla tavalla "ennen" ja "jälkeen" otetaan huomioon jopa 50 vuotta ennen tai jälkeen päivämäärän.

    Tämä voi johtaa yllättäviin tuloksiin, joten käytä "noin" ja "Arvioitu" vain silloin, kun et voi tarkentaa päivämäärää. Jos tiedät lyhyemmän aikavälin, Aikaväli, kuten "välillä 1878 ja 1882", on tarkempi.

Kalenteri antaa sinun syöttää päivämäärän alkuperäisessä asiakirjassa käytetyssä kalenterissa, kuten Julian kalenterissa, sen sijaan, että muuntasit sen itse.
