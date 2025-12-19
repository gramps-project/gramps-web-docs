# Käyttäen AI-chatia

!!! info
    AI-chat vaatii Gramps Web API -version 2.5.0 tai uudemman ja Gramps Web -version 24.10.0 tai uudemman.

Chat-näkymä Gramps Webissä (jos se on saatavilla asennuksessasi) antaa pääsyn AI-avustajaan, joka voi vastata kysymyksiin perhepuustasi.

!!! warning
    Koska tämä on edelleen uusi ja kehittyvä ominaisuus, jotkut kysymystyypit toimivat hyvin, kun taas toiset eivät. Lisäksi, kuten minkä tahansa AI-avustajan kanssa, se voi antaa faktuaalisesti vääriä vastauksia, joten varmista aina, että tarkistat tiedot.

## Kuinka se toimii

Ymmärtääksesi, minkä tyyppisiin kysymyksiin avustaja voi vastata, on hyödyllistä ymmärtää, miten se toimii sisäisesti:

1. Käyttäjä esittää kysymyksen.
2. Gramps Web tunnistaa useita (esim. kymmenen) Gramps-objektia, jotka todennäköisesti sisältävät tiedot, jotka vastaavat kysymykseen. Tätä varten se käyttää tekniikkaa, jota kutsutaan "semanttiseksi hauksi". Esimerkiksi, jos kysyt "Mikä on John Doen lasten nimet?", jos perhettä, jossa John Doe on isä, on olemassa, se todennäköisesti on yksi parhaista tuloksista.
3. Gramps Web syöttää käyttäjän kysymyksen yhdessä haetun kontekstin tiedon suurelle kielimallille ("chatbot") ja pyytää sitä erottamaan oikea vastaus.
4. Vastaus näytetään käyttäjälle.

## Kuinka esittää kysymys

Chatin toiminnan vuoksi AI-avustajan ei (toistaiseksi) ole mahdollista vastata kysymyksiin erityisistä suhteista, lukuun ottamatta vanhempia tai lapsia, ellei tätä tietoa ole tekstinä muistiinpanossa.

Koska jokainen vastaus perustuu rajalliseen määrään parhaita semanttisia hakutuloksia, se ei myöskään voi vastata kysymyksiin tilastoista ("kuinka monta ihmistä tietokannassani ...").

Epäselvyyksien ja väärinkäsitysten välttämiseksi on hyödyllistä muotoilla kysymys mahdollisimman yksityiskohtaisesti.

Huomaa, että suuret kielimallit ovat monikielisiä, joten voit puhua sille omalla kielelläsi, ja se vastaa samalla kielellä.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi, yhteisön kanssa.
