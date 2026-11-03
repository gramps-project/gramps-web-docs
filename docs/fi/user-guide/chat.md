# Käyttämällä AI-avustajaa

!!! info
    AI-avustaja vaatii Gramps Web API -version 2.5.0 tai uudemman ja Gramps Web -version 24.10.0 tai uudemman. Gramps Web API -version 3.6.0 myötä esiteltiin työkalujen kutsumismahdollisuuksia älykkäämpiin vuorovaikutuksiin.

**Avustaja**-näkymä Gramps Webissä (jos se on saatavilla asennuksessasi, merkitty "Chat" vanhemmissa versioissa) antaa pääsyn AI-avustajaan, joka voi vastata kysymyksiin perhepuustasi.

!!! warning
    Koska tämä on edelleen uusi ja kehittyvä ominaisuus, jotkut kysymystyypit toimivat hyvin, kun taas toiset eivät. Myös, kuten minkä tahansa AI-avustajan kanssa, se voi antaa faktatietoja virheellisiä vastauksia, joten muista aina tarkistaa tiedot.

## Kuinka se toimii

Ymmärtääksesi, minkä tyyppisiin kysymyksiin avustaja voi vastata, on hyödyllistä ymmärtää, miten se toimii taustalla:

1. Käyttäjä esittää kysymyksen.
2. Avustaja kysyy suoraan tietokannastasi erikoistyökalujen avulla: se etsii puusta [kokotekstihaku](search.md), suodattaa henkilöitä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskee suhteita yksilöiden välillä ja etsii täydellisiä tietueita, mukaan lukien niiden muistiinpanot.
3. Suuri kielimalli muotoilee vastauksen sen perusteella, mitä tietueita se on löytänyt.
4. Vastaus näytetään sinulle, ja siinä on linkkejä tietueisiin, joihin se perustuu.

Avustaja vastaa vain puustasi, ei kielen mallin yleisestä tiedosta – edes tunnetuista henkilöistä. Jos puu ei tallenna jotain, se ilmoittaa siitä ja mainitsee siihen liittyvät tiedot, joita se on löytänyt, esimerkiksi muistiinpanossa. Linkit objekteihin, joita et saa nähdä, näytetään tavallisena tekstinä.

Seuraavat kysymykset pitävät aikaisempien kysymysten kontekstin samassa keskustelussa, joten voit kysyä "Ja milloin hän kuoli?" kysyttyäsi henkilöstä.

Kun avustaja työskentelee, indikaattorit näyttävät, mitä työkaluja se tällä hetkellä käyttää (esim. etsii henkilöitä, tarkistaa suhteita), joten voit seurata, kun se rakentaa vastaustaan. Pidempiä kysymyksiä käsitellään taustatehtävinä – voit siirtyä muualle ja palata takaisin, ja edistyminen näkyy myös [Ilmoituksissa](notifications.md). Vastaukset on muotoiltu Markdownilla (luettelot, korostus, linkit jne.) helpomman lukemisen vuoksi.

## Mitä voit kysyä

Gramps Web API -version 3.6.0 myötä esiteltyjen työkalujen kutsumismahdollisuuksien ansiosta AI-avustaja voi nyt käsitellä monimutkaisempia kysymyksiä:

- **Perhesuhteet**: "Keitä Jane Smithin isovanhemmat ovat?" tai "Miten John Doe on sukua Mary Johnsonille?"
- **Suodatetut haut**: "Näytä kaikki henkilöt, jotka on syntynyt Lontoossa vuoden 1850 jälkeen" tai "Mitä tapahtumia Pariisissa on tapahtunut?"
- **Päivämääräpohjaiset kysymykset**: "Kuka kuoli ennen vuotta 1900?" tai "Listaa avioliitot, jotka tapahtuivat vuosien 1920 ja 1950 välillä"
- **Paikkatiedot**: "Mitä paikkoja Ranskassa on?" tai "Kerro minulle St. Maryn kirkosta"
- **Yleiset kysymykset**: "Mikä on John Doen lasten nimet?" tai "Milloin Mary Smith syntyi?"

## Vinkkejä kysymysten esittämiseen

Saadaksesi parhaat tulokset AI-avustajalta:

- **Ole tarkka**: Muotoile kysymyksesi mahdollisimman yksityiskohtaisesti välttääksesi epäselvyyksiä. Esimerkiksi "Milloin John Smith, joka syntyi vuonna 1850 Bostonissa, meni naimisiin?" on parempi kuin "Milloin John Smith meni naimisiin?"
- **Käytä oikeita nimiä**: Mainitse erityiset nimet, paikat ja päivämäärät, kun se on relevanttia.
- **Kysy yksi asia kerrallaan**: Pilko monimutkaiset kysymykset yksinkertaisempiin osiin parempien tulosten saamiseksi.
- **Käytä omaa kieltäsi**: Suuret kielimallit ovat monikielisiä, joten voit esittää kysymyksiä omalla kielelläsi ja saada vastauksia samalla kielellä.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi, yhteisön kanssa.
