# Kuinka Gramps järjestää tietoja

Gramps Web tallentaa sukupuun ei kaaviona, vaan erillisinä objekteina – ihmiset, perheet, tapahtumat, paikat, lähteet ja niin edelleen – jotka ovat linkitetty toisiinsa. Kun tiedät, miten nämä objektit liittyvät toisiinsa, tietojen syöttäminen muuttuu ennakoitavaksi: mitä tahansa, mitä haluat linkittää, on ensin oltava olemassa.

Gramps Web käyttää samaa tietomallia kuin Gramps Desktop, joten kaikki tällä sivulla pätee molempiin.

## Rakennuspalikat

| Objekti | Mitä se edustaa | Esimerkkejä |
|---|---|---|
| Henkilö | Yksilö | Sinä, isoäitisi |
| Perhe | Pari, heidän lapsensa tai molemmat | Vanhempasi ja heidän lapsensa |
| Tapahtuma | Jokin, mikä tapahtui, päivämäärän ja paikan kanssa | Syntymä, avioliitto, väestönlaskenta, maahanmuutto |
| Paikka | Maantieteellinen sijainti | Kylä, seurakunta, maa |
| Lähde | Asiakirja tai tietokokoelma | Seurakuntarekisteri, väestönlaskenta, kirja |
| Viite | Tietty viittaus lähteessä | Sivun 12, merkintä 3 seurakuntarekisterissä |
| Arkisto | Missä lähde säilytetään | Arkisto, kirjasto, verkkosivusto |
| Huomautus | Vapaa teksti | Transkriptio, tutkimusmuistiinpanot |
| Mediaobjekti | Tiedosto | Valokuva, skannattu todistus |

Jokaisella objektityypillä on oma luettelonsa Gramps Webissä, katso [Luettelot](lists.md).

## Ihmiset ja perheet

Vanhemmat ja lapset eivät ole suoraan linkitetty toisiinsa, vaan **perheen** kautta. Perheessä voi olla enintään kaksi kumppania ja mielivaltainen määrä lapsia:

- Vanhempasi ja sinä olette linkitetty perheen kautta, jossa olet lapsi.
- Sisaruksesi ovat saman perheen muut lapset.
- Sinä ja puolisosi muodostatte toisen perheen, jossa olette kumppaneita yhdessä lasten kanssa.

Yksi henkilö voi olla lapsi yhdessä perheessä ja kumppani useissa. Jokaisella lapsella on suhde jokaiseen vanhempaan, kuten syntymä, adoptointi tai lapsipuoli, ja jokaisella perheellä on suhdetyyppi, kuten avioliitto tai rekisteröity parisuhde.

Tämä on syy siihen, miksi "vanhempien lisääminen" henkilöön tarkoittaa henkilön lisäämistä lapsena perheeseen – mitä [puukaavio](tree-edit.md) tekee puolestasi yhdessä vaiheessa.

## Tapahtumat

Syntymä, kuolema tai avioliitto ei ole henkilön kenttä, vaan oma **tapahtumansa**, jolla on tyyppi, päivämäärä, paikka ja kuvaus. Ihmiset linkitetään tapahtumaan **roolin** kautta: henkilö, jonka syntymästä on kyse, on roolissa "Pääasiallinen", kun taas joku muu voi olla linkitetty samaan tapahtumaan todistajana.

Tapahtumat, jotka koskevat paria, kuten avioliitto, kuuluvat perheelle eivätkä kummallekaan kumppanille. Tapahtuma voi myös olla useiden ihmisten jaettavissa – esimerkiksi väestönlaskentatieto, joka listaa koko kotitalouden – sen sijaan, että se syötetään kerran per henkilö.

## Jaetut objektit: paikat ja lähteet

Paikat, lähteet, viitteet, arkistot, huomautukset ja mediaobjektit ovat olemassa omana itsenään, ja mielivaltainen määrä muita objekteja voi viitata samaan. Tällä on muutamia seurauksia:

- **Luo kerran, valitse monta kertaa.** Kylä, jossa kymmenen esi-isääsi syntyi, on yksi paikka, joka valitaan kymmenessä syntymätapahtumassa. Jos korjaat sen nimen tai koordinaatit, korjaus pätee joka puolella.
- **Luo se ennen kuin valitset sen.** Lomakkeet Gramps Webissä valitsevat paikkoja ja lähteitä, jotka jo olemassa. Luo uusi paikka tai lähde ensin käyttämällä **+** (Lisää) -painiketta sovelluksen yläreunassa.
- **Paikat ovat sisäkkäin.** Paikka voi olla suuremman paikan sisällä – kylä piirin sisällä, piiri maan sisällä – joten sinun ei tarvitse toistaa koko hierarkiaa jokaiselle kylälle.
- **Lähteet ja viitteet ovat erillisiä.** Lähde on seurakuntarekisteri kokonaisuudessaan; viite on tietty merkintä, joka tukee faktaa, sen sivun, päivämäärän ja luottamuksesi siihen. Monet viitteet voivat viitata samaan lähteeseen.

Jos olet vahingossa luonut saman paikan tai lähteen kahdesti, voit [yhdistää kaksoiskappaleet](lists.md#merge).

## Kotihenkilö

Kotihenkilö on henkilö, josta sukupuun kaaviot alkavat ja oletuslähtökohta raporteille. Katso [Ensimmäinen kirjautuminen](first-login.md) siitä, miten se asetetaan.

!!! note "Eroaa Gramps Desktopista"
    Gramps Desktopissa Kotihenkilö tallennetaan sukupuun tietokantaan, joten se on sama kaikille, jotka avaavat kyseisen tietokannan. Gramps Web ei käytä sitä. Sen sijaan Kotihenkilö tallennetaan selaimeesi, erikseen jokaiselle puulle: sitä ei jaeta muiden käyttäjien kanssa, eikä se seuraa sinua toiseen selaimeen tai laitteeseen. Kun tuot puun Gramps Desktopista tai käytät Gramps Webiä toisella laitteella, sinun on asetettava se uudelleen.

## Suositeltu järjestys

Kun syötät uutta perhettä käsin, tämä järjestys välttää hyppimistä lomakkeiden välillä:

1. **Paikat ja lähteet.** Luo tarvitsemasi paikat ja, jos tallennat lähteitä, lähde, jota käytät.
2. **Ihmiset.** Lisää ihmiset heidän syntymä- ja kuolinpäivineen ja -paikkoineen. Tämä on nopeinta Sukupuu-kaavion muokkaustilassa, joka luo perheet puolestasi – katso [Aloita uusi puu](start-tree.md) ja [Sukupuun muokkaaminen](tree-edit.md).
3. **Lisätapahtumat.** Avaa perhe (esimerkiksi henkilön Suhde-välilehdeltä) lisätäksesi avioliiton, ja henkilön sivulta lisätäksesi muita tapahtumia.
4. **Viitteet.** Henkilön, tapahtuman tai muun objektin Lähdeviitteet-välilehdellä, jota lähde tukee, lisää uusi viite, valitse lähde ja syötä sivu.
5. **Huomautukset ja media.** Liitä transkriptioita, valokuvia ja skannauksia – katso [Lisää media tiedostoja](media.md).

## Päivämäärien syöttäminen

Päivämäärä syötetään erillisinä vuosina, kuukausina ja päivinä, jotka voidaan myös täyttää päivämäärävalitsimella. Jätä pois osat, joita et tiedä: pelkkä vuosi on voimassa oleva päivämäärä.

Sen sijaan, että arvailisit tarkkaa päivää, kuvaa, mitä tiedät päivämäärän **Tyypistä**:

| Mitä tiedät | Tyyppi | Esimerkki |
|---|---|---|
| Tarkka päivämäärä tai osa siitä | Säännöllinen | 12. maaliskuuta 1850, tai vain 1850 |
| Suunnilleen oikea päivämäärä | noin | noin 1850 |
| Rajoitus | ennen, jälkeen | ennen 1900 |
| Päivämäärä on jossain aikavälillä | Aikaväli | 1850 ja 1855 välillä |
| Jokin kesti tietyn ajan | Kesto | 1850:stä 1855:een |
| Vain aikavälin alku tai loppu | alkaen, asti | alkaen 1850 |

**Laatu**-kenttä tallentaa, miten päädyit päivämäärään: "Arvioitu" koulutetulle arvaukselle, "Laskettu" päivämäärälle, joka on johdettu muista tiedoista, kuten syntymävuosi, joka on laskettu kuolinikäisestä.

!!! warning "Noin ja arvioidut päivämäärät kattavat 50 vuotta kumpaankin suuntaan"
    Kun Gramps vertaa päivämääriä, se käsittelee "noin" -tyyppistä päivämäärää – ja mitä tahansa päivämäärää, jonka laatu on "Arvioitu" – aikavälinä, joka ulottuu 50 vuotta ennen ja 50 vuotta jälkeen annetun päivämäärän. Esimerkiksi, kun suodatat Ihmiset-luetteloa henkilöille, jotka ovat syntyneet 1840 ja 1860 välillä, löydät myös henkilön, joka on syntynyt "noin 1880", koska tätä päivämäärää pidetään kattavan 1830–1930. Samalla tavalla "ennen" ja "jälkeen" otetaan huomioon jopa 50 vuotta ennen tai jälkeen päivämäärän.

    Tämä voi johtaa yllättäviin tuloksiin, joten käytä "noin" ja "Arvioitu" vain, kun et voi tarkentaa päivämäärää. Jos tiedät lyhyemmän aikavälin, aikaväli, kuten "1850 ja 1855 välillä", on tarkempi.

**Kalenteri**-kenttä antaa sinun syöttää päivämäärän alkuperäisessä asiakirjassa käytetyssä kalenterissa, kuten Julian kalenterissa, sen sijaan, että muuntasit sen itse.
