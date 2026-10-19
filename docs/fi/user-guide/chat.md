# Käyttäminen AI-avustajaa

!!! info
    AI-avustaja vaatii Gramps Web API version 2.5.0 tai uudemman sekä Gramps Web version 24.10.0 tai uudemman. Gramps Web API version 3.6.0 esitteli työkalujen kutsumismahdollisuudet älykkäämmille vuorovaikutuksille.

**Avustaja**-näkymä Gramps Webissä (jos se on saatavilla asennuksessasi, nimeltään "Chat" vanhemmissa versioissa) antaa pääsyn AI-avustajaan, joka voi vastata kysymyksiin perhepuustasi.

!!! warning
    Koska tämä on edelleen uusi ja kehittyvä ominaisuus, jotkut kysymystyypit toimivat hyvin, kun taas toiset eivät. Lisäksi, kuten minkä tahansa AI-avustajan kanssa, se voi antaa faktuaalisesti väärää tietoa, joten varmista aina, että tarkistat tiedot.

## Kuinka se toimii

Ymmärtääksesi, minkä tyyppisiin kysymyksiin avustaja voi vastata, on hyödyllistä ymmärtää, miten se toimii sisäisesti:

1. Käyttäjä esittää kysymyksen.
2. Avustaja kysyy suoraan tietokannastasi erikoistyökalujen avulla: se etsii puusta [kokotekstihaku](search.md), suodattaa henkilöitä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskee suhteita yksilöiden välillä ja etsii täydellisiä tietueita, mukaan lukien niiden muistiinpanot.
3. Suuri kielimalli muotoilee vastauksen sen perusteella, mitä tietueita se on löytänyt.
4. Vastaus näytetään sinulle, ja siinä on linkkejä tietueisiin, joihin se perustuu.

Palvelimilla, joilla on Gramps Web API version 3.24 vanhempi, avustaja tuki myös semanttista hakua, jota ollaan poistamassa käytöstä.

Kun avustaja työskentelee, indikaattorit näyttävät, mitä työkaluja se tällä hetkellä käyttää (esim. etsii henkilöitä, tarkistaa suhteita), jotta voit seurata, kun se rakentaa vastaustaan. Pitkäkestoiset kysymykset käsitellään taustatehtävinä – voit navigoida muualle ja palata takaisin, ja edistyminen näkyy myös [Ilmoituksissa](notifications.md). Vastaukset on muotoiltu Markdownilla (luettelot, korostukset, linkit jne.) helpomman lukemisen vuoksi.

## Mitä voit kysyä

Gramps Web API version 3.6.0 myötä esiteltyjen työkalujen kutsumismahdollisuuksien avulla AI-avustaja voi nyt käsitellä monimutkaisempia kysymyksiä:

- **Perhesuhteet**: "Keitä ovat Jane Smithin isovanhemmat?" tai "Miten John Doe on sukua Mary Johnsonille?"
- **Suodatetut haut**: "Näytä kaikki henkilöt, jotka ovat syntyneet Lontoossa vuoden 1850 jälkeen" tai "Mitä tapahtumia tapahtui Pariisissa?"
- **Päivämääräpohjaiset kysymykset**: "Kuka kuoli ennen vuotta 1900?" tai "Listaa avioliitot, jotka tapahtuivat vuosina 1920–1950"
- **Paikkatiedot**: "Mitä paikkoja on Ranskassa?" tai "Kerro minulle St. Maryn kirkosta"
- **Yleiset kysymykset**: "Mikä on John Doen lasten nimet?" tai "Milloin Mary Smith syntyi?"

## Vinkkejä kysymysten esittämiseen

Saadaksesi parhaat tulokset AI-avustajalta:

- **Ole tarkka**: Muotoile kysymyksesi mahdollisimman yksityiskohtaisesti välttääksesi epäselvyyksiä. Esimerkiksi "Milloin John Smith, joka syntyi vuonna 1850 Bostonissa, meni naimisiin?" on parempi kuin "Milloin John Smith meni naimisiin?"
- **Käytä oikeita nimiä**: Mainitse erityiset nimet, paikat ja päivämäärät, kun se on relevanttia.
- **Kysy yksi asia kerrallaan**: Pilko monimutkaiset kysymykset yksinkertaisempiin osiin parempien tulosten saamiseksi.
- **Käytä omaa kieltäsi**: Suuret kielimallit ovat monikielisiä, joten voit esittää kysymyksiä omalla kielelläsi ja saada vastauksia samassa kielessä.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi, yhteisön kanssa.
