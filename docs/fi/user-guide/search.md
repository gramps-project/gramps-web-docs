# Haku

Hakusivu on saatavilla napsauttamalla suurennuslasikuvaketta ylävalikkopalkissa tai painamalla `s` [näppäinoikoreittiä](shortcuts.md).

## Koko tekstin haku

Kirjoita kysely hakukenttään. Tulokset näkyvät kirjoittaessasi, toisesta merkistä alkaen; paina Enter etsiäksesi yksittäistä merkkiä. Gramps Web etsii kaikista objektityypeistä – ihmiset, perheet, tapahtumat, paikat, lähteet, viittaukset, arkistot, muistiinpanot ja media – ja palauttaa osumat, jotka on järjestetty merkityksellisyyden mukaan. Tyhjentääksesi haun, napsauta tyhjennä-painiketta kentässä tai paina Escape.

Jokainen tulos näyttää objektityypin, sen nimen ja joitakin yksityiskohtia, esimerkiksi henkilön syntymän ja kuoleman, perheen avioliiton, lähteen kirjoittajan tai muistiinpanon ensimmäisen rivin. Napsauta mitä tahansa tulosta avataksesi vastaavan yksityiskohtasivun.

## Hakusyntaksi

- **Kaikkien sanojen on vastattava.** `Müller Berlin` löytää objekteja, jotka sisältävät molemmat sanat.
- **`or`** löytää objekteja, jotka sisältävät joko sanan, esim. `Meyer or Maier`. `and` voidaan myös kirjoittaa sanojen väliin, mutta sillä ei ole merkitystä.
- `or` koskee suoraan vierekkäisiä sanoja: `Meyer or Maier Berlin` tarkoittaa "(Meyer tai Maier) ja Berlin". Sulkuja ei tueta.
- **Lainausmerkit** vastaavat lausetta, eli sanoja tässä järjestyksessä: `"Johann Georg"`.
- **Jokerimerkki:** perässä oleva `*` vastaa mitä tahansa loppua, esim. `Mey*` vastaa "Meyer", "Meyers", "Meyerhofer" jne. Tämä toimii myös lauseissa: `"Johann Georg"*`.
- **Viimeinen sana on täydellinen.** Jos kysely päättyy kirjaimeen tai numeroon, sitä haetaan ikään kuin se päättyisi `*`, joten `Anna Smi` löytää jo "Anna Smith". Etsiäksesi viimeistä sanaa tarkasti, päätä kysely välilyönnillä tai laita sana lainausmerkkeihin. Sama pätee objektivalitsimien hakukenttiin ja [karttaan](map.md#search).
- `or` ja `and` tunnistetaan kaikissa kirjainkoolla. Etsiäksesi yhtä näistä sanoista itsestään, laita se lainausmerkkeihin.
- Sanoja ei voi sulkea pois; ei ole "not".

## Mitä haku löytää

- Aksenttien ei tarvitse vastata: "Müller" löytää myös "Muller", ja "muller" löytää "Müller".
- Perheitä ja tapahtumia löydetään myös heidän ihmistensä nimillä, esim. "Müller" löytää kaikkien nimeltä Müller olevien perheiden ja tapahtumien. Nämä tulokset sijoitetaan suoran osuman alapuolelle.
- Vakio-tyypit löytyvät nimilläsi käyttöliittymäkielessäsi, esim. "Taufe" löytää kasteet saksankielisessä käyttöliittymässä.
- Alaviivat erottavat sanoja, joten "microfilm" löytää median tiedoston nimeltä `scanned_microfilm.png`.
- Käyttäjät, jotka eivät voi nähdä yksityisiä tietueita, eivät löydä objekteja yksityisten tietojen kautta, kuten perhettä yksityisen jäsenen nimen kautta.

## Suodatus objektityypin mukaan

Hakukentän alapuolella on kytkinpainikkeet jokaiselle objektityypille (Ihmiset, Perheet, Tapahtumat, Paikat, …), joiden avulla voit rajoittaa tuloksia yhteen tai useampaan tiettyyn tyyppiin. Oletusarvoisesti kaikkia tyyppejä haetaan. Yhden tai useamman kytkimen aktivoiminen rajoittaa tuloksia vain näihin tyyppeihin.
