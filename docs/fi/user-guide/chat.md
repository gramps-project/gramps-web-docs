# Käyttäminen AI-chatin

!!! info
    AI-chat vaatii Gramps Web API -version 2.5.0 tai uudemman ja Gramps Web -version 24.10.0 tai uudemman. Gramps Web API -version 3.6.0 myötä otettiin käyttöön työkalujen kutsumismahdollisuudet älykkäämpiin vuorovaikutuksiin.

Chat-näkymä Gramps Webissä (jos se on saatavilla asennuksessasi) antaa pääsyn AI-avustajaan, joka voi vastata kysymyksiin perhepuustasi.

!!! warning
    Koska tämä on edelleen uusi ja kehittyvä ominaisuus, jotkut kysymystyypit toimivat hyvin, kun taas toiset eivät. Myös, kuten kaikissa AI-avustajissa, se voi antaa faktuaalisesti vääriä vastauksia, joten varmista aina, että tarkistat tiedot.

## Kuinka se toimii

Ymmärtääksesi, minkä tyyppisiin kysymyksiin avustaja voi vastata, on hyödyllistä ymmärtää, miten se toimii "konepellin alla":

1. Käyttäjä esittää kysymyksen.
2. AI-avustaja voi käyttää useita lähestymistapoja löytääkseen vastauksia:
   - **Semanttinen haku**: Gramps Web tunnistaa perhepuustasi ne objektit, jotka todennäköisimmin sisältävät relevanttia tietoa. Esimerkiksi, jos kysyt "Mikä on John Doen lasten nimet?", perheet, joissa John Doe on isä, ovat joukossa parhaat tulokset.
   - **Työkalujen kutsuminen (Gramps Web API v3.6.0+)**: Avustaja voi suoraan kysyä tietokannastasi erikoistyökalujen avulla etsiäkseen, suodattaakseen henkilöitä/tapahtumia/perheitä/paikkoja tietyillä kriteereillä, laskeakseen suhteita yksilöiden välillä ja noutaakseen yksityiskohtaista tietoa.
3. Gramps Web syöttää kysymyksen yhdessä haetun tiedon kanssa suurelle kielimallille muotoillakseen vastauksen.
4. Vastaus näytetään sinulle.

## Mitä voit kysyä

Työkalujen kutsumismahdollisuuksien myötä, jotka otettiin käyttöön Gramps Web API -version 3.6.0 myötä, AI-avustaja voi nyt käsitellä monimutkaisempia kysymyksiä:

- **Perhesuhteet**: "Keitä ovat Jane Smithin isovanhemmat?" tai "Miten John Doe on sukua Mary Johnsonille?"
- **Suodatetut haut**: "Näytä kaikki henkilöt, jotka on syntynyt Lontoossa vuoden 1850 jälkeen" tai "Mitä tapahtumia tapahtui Pariisissa?"
- **Päivämäärään perustuvat kysymykset**: "Kuka kuoli ennen vuotta 1900?" tai "Listaa avioliitot, jotka tapahtuivat vuosien 1920 ja 1950 välillä"
- **Paikkatiedot**: "Mitä paikkoja on Ranskassa?" tai "Kerro minulle St. Maryn kirkosta"
- **Yleiset kysymykset**: "Mikä on John Doen lasten nimet?" tai "Milloin Mary Smith syntyi?"

## Vinkkejä kysymysten esittämiseen

Saadaksesi parhaat tulokset AI-avustajalta:

- **Ole tarkka**: Muotoile kysymyksesi mahdollisimman yksityiskohtaisesti välttääksesi epäselvyyksiä. Esimerkiksi "Milloin John Smith, joka syntyi vuonna 1850 Bostonissa, meni naimisiin?" on parempi kuin "Milloin John Smith meni naimisiin?"
- **Käytä oikeita nimiä**: Mainitse erityiset nimet, paikat ja päivämäärät, kun se on relevanttia.
- **Kysy yksi asia kerrallaan**: Pilko monimutkaiset kysymykset yksinkertaisempiin osiin parempien tulosten saavuttamiseksi.
- **Käytä omaa kieltäsi**: Suuret kielimallit ovat monikielisiä, joten voit esittää kysymyksiä omalla kielelläsi ja saada vastauksia samassa kielessä.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi yhteisön kanssa.
