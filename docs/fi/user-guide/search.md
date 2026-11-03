# Haku

Hakusivulle pääsee napsauttamalla suurennuslasikuvaketta ylävalikkopalkissa tai painamalla `s` [pikanäppäintä](shortcuts.md).

## Koko tekstin haku

Kirjoita mikä tahansa kysely hakukenttään ja paina Enter (tai napsauta hakupainiketta). Gramps Web etsii kaikista objektityypeistä – ihmiset, perheet, tapahtumat, paikat, lähteet, viittaukset, arkistot, muistiinpanot ja media – ja palauttaa osumat, jotka on järjestetty relevanssin mukaan.

Tulokset näyttävät objektityypin, nimen ja lyhyen yhteenvedon. Napsauta mitä tahansa tulosta avataksesi vastaavan yksityiskohtasivun.

## Hakusyntaksi

- **Kaikkien sanojen on vastattava.** `Müller Berlin` löytää objekteja, jotka sisältävät molemmat sanat.
- **`or`** löytää objekteja, jotka sisältävät joko sanan, esim. `Meyer or Maier`. `and` voidaan myös kirjoittaa sanojen väliin, mutta sillä ei ole merkitystä.
- `or` koskee suoraan vierekkäisiä sanoja: `Meyer or Maier Berlin` tarkoittaa "(Meyer or Maier) ja Berlin". Sulkuja ei tueta.
- **Lainausmerkit** vastaavat lausetta, eli sanoja tässä järjestyksessä: `"Johann Georg"`.
- **Jokerimerkki:** perässä oleva `*` vastaa mitä tahansa loppua, esim. `Mey*` vastaa "Meyer", "Meyers", "Meyerhofer" jne. Tämä toimii myös lauseille: `"Johann Georg"*`.
- `or` ja `and` tunnistetaan kaikissa kirjainkokoissa. Jos haluat etsiä yhtä näistä sanoista itsessään, laita se lainausmerkkeihin.
- Sanoja ei voi sulkea pois; ei ole "not".

## Mitä haku löytää

- Aksentteja ei tarvitse vastata: "Müller" löytää myös "Muller", ja "muller" löytää "Müller".
- Perheitä ja tapahtumia löydetään myös niiden ihmisten nimien perusteella, esim. "Müller" löytää kaikkien nimeltä Müller olevien perheiden ja tapahtumien tiedot. Nämä tulokset sijoittuvat suoran osuman alle.
- Vakiotyypit löytyvät nimilläsi käyttöliittymäkielessäsi, esim. "Taufe" löytää kasteet saksankielisessä käyttöliittymässä.
- Alaviivat erottavat sanoja, joten "microfilm" löytää mediatiedoston nimeltä `scanned_microfilm.png`.
- Käyttäjät, jotka eivät voi nähdä yksityisiä tietoja, eivät löydä objekteja yksityisten tietojen kautta, kuten perhettä yksityisen jäsenen nimen kautta.

## Suodatus objektityypin mukaan

Hakukentän alla olevat kytkinpainikkeet jokaiselle objektityypille (Ihmiset, Perheet, Tapahtumat, Paikat, …) antavat sinun rajata tuloksia yhteen tai useampaan tiettyyn tyyppiin. Oletuksena kaikki tyypit haetaan. Yhden tai useamman kytkimen aktivointi rajoittaa tuloksia vain näihin tyyppeihin.
