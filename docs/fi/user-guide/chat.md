# Käyttäminen AI-avustajaa

!!! info
    AI-avustaja vaatii Gramps Web API -version 2.5.0 tai uudemman ja Gramps Web -version 24.10.0 tai uudemman. Gramps Web API -version 3.6.0 myötä tuli käyttöön työkalujen kutsumismahdollisuudet älykkäämpiin vuorovaikutuksiin.

**Avustaja**-näkymä Gramps Webissä (jos se on saatavilla asennuksessasi, nimeltään "Chat" vanhemmissa versioissa) antaa pääsyn AI-avustajaan, joka voi vastata kysymyksiin perhepuustasi.

!!! warning
    Koska tämä on edelleen uusi ja kehittyvä ominaisuus, jotkut kysymystyypit toimivat hyvin, kun taas toiset eivät. Myös, kuten minkä tahansa AI-avustajan kanssa, se voi antaa faktuaalisesti vääriä vastauksia, joten varmista aina, että tarkistat tiedot.

## Kuinka se toimii

Ymmärtääksesi, minkä tyyppisiin kysymyksiin avustaja voi vastata, on hyödyllistä ymmärtää, miten se toimii "konehuoneen" alla:

1. Käyttäjä esittää kysymyksen.
2. AI-avustaja voi käyttää useita lähestymistapoja löytääkseen vastauksia:
   - **Semanttinen haku**: Gramps Web tunnistaa perhepuustasi ne objektit, jotka todennäköisimmin sisältävät relevanttia tietoa. Esimerkiksi, jos kysyt "Mikä on John Doen lasten nimet?", perheet, joissa John Doe on isä, ovat joukossa parhaat tulokset.
   - **Työkalujen kutsuminen (Gramps Web API v3.6.0+)**: Avustaja voi suoraan kysyä tietokannastasi erikoistyökalujen avulla etsiäkseen, suodattaakseen ihmisiä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskeakseen suhteita yksilöiden välillä ja saadakseen yksityiskohtaista tietoa.
3. Gramps Web syöttää kysymyksen yhdessä haetun tiedon suuren kielimallin käsiteltäväksi vastauksen muotoilemiseksi.
4. Vastaus näytetään sinulle.

Kun avustaja työskentelee, indikaattorit näyttävät, mitä työkaluja se tällä hetkellä käyttää (esim. etsii ihmisiä, tarkistaa suhteita), jotta voit seurata, kun se rakentaa vastaustaan. Pitempään kestäviä kysymyksiä käsitellään taustatehtävinä – voit siirtyä muualle ja palata takaisin, ja edistyminen näkyy myös [Ilmoituksissa](notifications.md). Vastaukset on muotoiltu Markdownilla (luettelot, korostukset, linkit jne.) helpomman lukemisen vuoksi.

## Mitä voit kysyä

Gramps Web API -version 3.6.0 myötä käyttöön otettujen työkalujen kutsumismahdollisuuksien ansiosta AI-avustaja voi nyt käsitellä monimutkaisempia kysymyksiä:

- **Perhesuhteet**: "Keitä Jane Smithin isovanhemmat ovat?" tai "Miten John Doe on sukua Mary Johnsonille?"
- **Suodatetut haut**: "Näytä kaikki Lontoossa syntyneet henkilöt vuoden 1850 jälkeen" tai "Mitä tapahtumia Pariisissa on ollut?"
- **Päivämääräperusteiset kysymykset**: "Kuka kuoli ennen vuotta 1900?" tai "Listaa avioliitot, jotka tapahtuivat vuosina 1920–1950"
- **Paikkatiedot**: "Mitä paikkoja Ranskassa on?" tai "Kerro minulle St. Maryn kirkosta"
- **Yleiset kysymykset**: "Mikä on John Doen lasten nimet?" tai "Milloin Mary Smith syntyi?"

## Vinkkejä kysymysten esittämiseen

Saadaksesi parhaat tulokset AI-avustajalta:

- **Ole tarkka**: Muotoile kysymyksesi mahdollisimman yksityiskohtaisesti välttääksesi epäselvyyksiä. Esimerkiksi "Milloin John Smith, joka syntyi vuonna 1850 Bostonissa, meni naimisiin?" on parempi kuin "Milloin John Smith meni naimisiin?"
- **Käytä oikeita nimiä**: Mainitse erityiset nimet, paikat ja päivämäärät, kun se on relevanttia.
- **Kysy yksi asia kerrallaan**: Pilko monimutkaiset kysymykset yksinkertaisempiin osiin parempien tulosten saavuttamiseksi.
- **Käytä omaa kieltäsi**: Suuret kielimallit ovat monikielisiä, joten voit esittää kysymyksiä omalla kielelläsi ja saada vastauksia samalla kielellä.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi yhteisön kanssa.
