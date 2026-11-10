# Kuinka Gramps järjestää tietoja

Gramps Web tallentaa sukupuun ei kaaviona, vaan erillisinä objekteina – ihmiset, perheet, tapahtumat, paikat, lähteet ja niin edelleen – jotka ovat linkitetty toisiinsa. Kun tiedät, miten nämä objektit liittyvät toisiinsa, tietojen syöttäminen muuttuu ennakoitavaksi: mitä tahansa, mihin haluat linkittää, on ensin oltava olemassa.

Gramps Web käyttää samaa tietomallia kuin Gramps Desktop, joten kaikki tällä sivulla pätee molempiin.

## Rakennuspalikat

| Objekti | Mitä se edustaa | Esimerkit |
|---|---|---|
| Henkilö | Yksilö | Sinä, isoäitisi |
| Perhe | Pari, heidän lapsensa tai molemmat | Vanhempasi ja heidän lapsensa |
| Tapahtuma | Jokin, mikä tapahtui, päivämäärän ja paikan kanssa | Syntymä, avioliitto, väestönlaskenta, maahanmuutto |
| Paikka | Maantieteellinen sijainti | Kylä, seurakunta, maa |
| Lähde | Asiakirja tai tietokokoelma | Seurakuntarekisteri, väestönlaskenta, kirja |
| Viittaus | Tietty viittaus lähteessä | Sivun 12, merkintä 3 seurakuntarekisterissä |
| Arkisto | Missä lähde säilytetään | Arkisto, kirjasto, verkkosivusto |
| Huomautus | Vapaa teksti | Transkriptio, tutkimusmuistiinpanot |
| Mediakohde | Tiedosto | Valokuva, skannattu todistus |

Jokaisella objektityypillä on oma luettelonsa Gramps Webissä, katso [Luettelot](lists.md).

## Ihmiset ja perheet

Vanhemmat ja lapset eivät ole suoraan linkitetty toisiinsa, vaan **perheen** kautta. Perheessä voi olla enintään kaksi kumppania ja mielivaltainen määrä lapsia:

- Vanhempasi ja sinä olette linkitetty perheen kautta, jossa olet lapsi.
- Sisaruksesi ovat saman perheen muut lapset.
- Sinä ja puolisosi muodostatte toisen perheen, jossa olette kumppaneita yhdessä lasten kanssa.

Henkilö voi olla lapsi yhdessä perheessä ja kumppani useissa. Jokaisella lapsella on suhde jokaiseen vanhempaan, kuten syntymä, adoptointi tai lapsipuoli, ja jokaisella perheellä on suhdetyyppi, kuten avioliitto tai rekisteröity parisuhde.

Tämä on syy siihen, miksi "vanhempien lisääminen" henkilöön tarkoittaa henkilön lisäämistä lapsena perheeseen – mitä [puukaavio](tree-edit.md) tekee puolestasi yhdellä askeleella.

## Tapahtumat

Syntymä, kuolema tai avioliitto ei ole henkilön kenttä, vaan oma **tapahtumansa**, jolla on tyyppi, päivämäärä, paikka ja kuvaus. Ihmiset linkitetään tapahtumaan **roolin** kautta: henkilöllä, jonka syntymästä on kyse, on rooli "Pääasiallinen", kun taas joku muu voi olla linkitetty samaan tapahtumaan todistajana.

Tapahtumat, jotka koskevat paria, kuten avioliitto, kuuluvat perheelle eivätkä kummallekaan kumppanille. Tapahtuma voi myös olla useiden ihmisten yhteinen – esimerkiksi väestönlaskentatieto, joka listaa koko talouden – sen sijaan, että se syötettäisiin kerran per henkilö.

## Jaetut objektit: paikat ja lähteet

Paikat, lähteet, viittaukset, arkistot, huomautukset ja mediakohteet ovat olemassa omana itsenään, ja mielivaltainen määrä muita objekteja voi viitata samaan. Tällä on muutamia seurauksia:

- **Luo kerran, valitse monta kertaa.** Kylä, jossa kymmenen esi-isääsi syntyi, on yksi paikka, valittuna kymmenessä syntymätapahtumassa. Jos korjaat sen nimen tai koordinaatit, korjaus koskee kaikkia.
- **Luo se ennen kuin valitset sen.** Lomakkeet Gramps Webissä valitsevat paikkoja ja lähteitä, jotka jo olemassa. Luo uusi paikka tai lähde ensin käyttämällä **+** (Lisää) -painiketta ylävalikkopalkissa.
- **Paikat ovat sisäkkäisiä.** Paikka voi olla suuremman paikan sisällä – kylä piirikunnassa, piirikunta maassa – joten sinun ei tarvitse toistaa koko hierarkiaa jokaiselle kylälle.
- **Lähteet ja viittaukset ovat erillisiä.** Lähde on seurakuntarekisteri kokonaisuudessaan; viittaus on tietty merkintä, joka tukee faktaa, sen sivu, päivämäärä ja luottamuksesi siihen. Monet viittaukset voivat viitata samaan lähteeseen.

Jos olet vahingossa luonut saman paikan tai lähteen kahdesti, voit [yhdistää kaksoiskappaleet](lists.md#merge).

## Objektin sivun muokkaaminen

Lähteen, arkiston tai mediakohteen sivulla napsauta otsikkoa muokkaustilassa muuttaaksesi sitä (mediakohteen kohdalla sen kuvausta). Paina Enter, napsauta ✓ tai napsauta muualle tallentaaksesi; paina Escape tai napsauta ✕ peruuttaaksesi.

Useimmat luettelot objektin sivulla säilyttävät antamasi järjestyksen, esimerkiksi tapahtumat, nimet, attribuutit, osoitteet, viittaukset tai perheen lapset. Muokkaustilassa valitse rivi ja siirrä se ylös- tai alaspainikkeilla tai vedä se uuteen sijaintiin: hiirellä, paina riviä ja siirrä se; kosketusnäytöllä, paina ja pidä riviä, kunnes se nousee ylös. Paina Escape vetäessäsi peruuttaaksesi. Galleriassa olevia medioita voidaan järjestää samalla tavalla, katso [Profiilikuvat](media.md#profile-pictures).

## Kotihenkilö

Kotihenkilö on henkilö, josta sukupuu alkaa ja oletuslähtökohta raporteille. Katso [Ensimmäinen kirjautuminen](first-login.md) siitä, miten se asetetaan.

!!! note "Eri kuin Gramps Desktop"
    Gramps Desktopissa Kotihenkilö tallennetaan sukupuun tietokantaan, joten se on sama kaikille, jotka avaavat kyseisen tietokannan. Gramps Web ei käytä sitä. Sen sijaan Kotihenkilö tallennetaan selaimeesi, erikseen jokaiselle puulle: sitä ei jaeta muiden käyttäjien kanssa, eikä se seuraa sinua toiseen selaimeen tai laitteeseen. Kun tuodaan puu Gramps Desktopista tai kun käytät Gramps Webiä toisella laitteella, sinun on asetettava se uudelleen.

## Suositeltu järjestys

Kun syötät uutta perhettä käsin, tämä järjestys välttää hyppimistä lomakkeiden välillä:

1. **Paikat ja lähteet.** Luo tarvitsemasi paikat ja, jos kirjaat lähteitä, lähde, jota käytät.
2. **Ihmiset.** Lisää ihmiset heidän syntymä- ja kuolinpäivineen sekä paikkoineen. Tämä on nopeinta Sukupuu-kaavion muokkaustilassa, joka luo perheet puolestasi – katso [Aloita uusi puu](start-tree.md) ja [Sukupuun muokkaaminen](tree-edit.md).
3. **Lisätapahtumat.** Avaa perhe (esimerkiksi henkilön Suhteet-välilehdeltä) lisätäksesi avioliiton, ja henkilön sivu lisätäksesi muita tapahtumia.
4. **Viittaukset.** Henkilön, tapahtuman tai muun objektin Lähdeviittaukset-välilehdellä, jota lähde tukee, lisää uusi viittaus, valitse lähde ja syötä sivu.
5. **Huomautukset ja media.** Liitä transkriptioita, valokuvia ja skannauksia – katso [Lisää mediakuvia](media.md).

## Päivämäärien syöttäminen

Päivämäärä syötetään erillisinä vuosina, kuukausina ja päivinä, jotka voidaan myös täyttää päivämäärävalitsimella. Jätä pois osat, joita et tiedä: pelkkä vuosi on voimassa oleva päivämäärä. 
Sen sijaan, että arvaisit tarkkaa päivää, kuvaa mitä tiedät valitsemalla päivämäärän tyyppi kenttien yläpuolella olevilla siruilla. Vihje sirujen alla selittää valitun tyypin:

| Mitä tiedät | Tyyppi | Esimerkki |
|---|---|---|
| Tarkka päivämäärä tai osa siitä | Säännöllinen | 12. maaliskuuta 1850 tai vain 1850 |
| Noin arvioitu päivämäärä | Noin | noin 1850 |
| Rajoitus | Ennen, Jälkeen | ennen 1900 |
| Päivämäärä on jossain aikavälillä | Aikaväli | välillä 1850 ja 1855 (kentät "Varhaisin" ja "Viimeisin") |
| Jokin kesti tietyn ajan | Kesto | vuodesta 1850 vuoteen 1855 |

Keston osalta kumpikin kahdesta päivämäärästä ("Alkaen" ja "Päättyen") voidaan jättää tyhjiksi, joten "vuodesta 1850" tai "vuoteen 1855" on kesto, jossa on vain yksi päivämäärä.

**Laatu** ja **Kalenteri** -kentät löytyvät **Lisäasetuksista**, joka avautuu automaattisesti, kun päivämäärä käyttää jotain niistä. Laatu tallentaa, miten päädyit päivämäärään: "Arvioitu" koulutetulle arvaukselle, "Laskettu" päivämäärälle, joka on johdettu muista tiedoista, kuten syntymävuosi, joka on laskettu kuolinikästä.

!!! warning "Noin ja arvioidut päivämäärät kattavat 50 vuotta kumpaankin suuntaan"
    Kun Gramps vertaa päivämääriä, se käsittelee "noin" -tyyppistä päivämäärää – ja mitä tahansa päivämäärää, jonka laatu on "Arvioitu" – aikavälinä, joka ulottuu 50 vuotta ennen ja 50 vuotta jälkeen annetun päivämäärän. Esimerkiksi, kun suodatat Ihmiset-luetteloa henkilöille, jotka ovat syntyneet välillä 1840 ja 1860, se löytää myös henkilön, joka on syntynyt "noin 1880", koska tätä päivämäärää pidetään kattavan aikavälin 1830–1930. Samalla tavalla "ennen" ja "jälkeen" katsotaan ulottuvan jopa 50 vuotta ennen tai jälkeen päivämäärän.

    Tämä voi johtaa yllättäviin tuloksiin, joten käytä "noin" ja "Arvioitu" vain silloin, kun et voi tarkentaa päivämäärää. Jos tiedät lyhyemmän aikavälin, aikaväli, kuten "välillä 1878 ja 1882", on tarkempi.

Kalenteri antaa sinun syöttää päivämäärän alkuperäisessä asiakirjassa käytetyssä kalenterissa, kuten Julian kalenterissa, sen sijaan, että muuntasit sen itse.
