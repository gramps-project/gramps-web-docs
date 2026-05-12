# Haku

Hakusivu on saatavilla napsauttamalla suurennuslasikuvaketta sovelluksen yläreunassa tai painamalla `s` [näppäinoikoreittiä](shortcuts.md).

## Kokotekstihaku

Kirjoita mikä tahansa kysely hakukenttään ja paina Enter (tai napsauta hakupainiketta). Gramps Web etsii kaikista objektityypeistä – ihmiset, perheet, tapahtumat, paikat, lähteet, viittaukset, arkistot, muistiinpanot ja media – ja palauttaa osumat, jotka on järjestetty merkityksellisyyden mukaan.

Tulokset näyttävät objektityypin, nimen ja lyhyen yhteenvedon. Napsauta mitä tahansa tulosta avataksesi vastaavan yksityiskohtasivun.

Perässä oleva `*` voidaan käyttää jokerina, esim. `Mey*` vastaa "Meyer", "Meyers", "Meyerhofer" jne.

## Suodatus objektityypin mukaan

Hakukentän alapuolella olevat kytkinpainikkeet jokaiselle objektityypille (Ihmiset, Perheet, Tapahtumat, Paikat, ...) antavat sinun rajata tuloksia yhteen tai useampaan erityiseen tyyppiin. Oletuksena haetaan kaikista tyypeistä. Yhden tai useamman kytkimen aktivointi rajoittaa tulokset vain näihin tyyppeihin.

## Semanttinen haku

Jos palvelimen ylläpitäjä on ottanut käyttöön [semanttisen (AI-pohjaisen) haun](../install_setup/configuration.md), hakusivun oikeassa yläkulmassa näkyy tilakytkin, jossa on kaksi vaihtoehtoa:

- **Haku** – standardi kokotekstihaku (oletus)
- **Semanttinen** – AI-pohjainen haku, joka ymmärtää kyselysi merkityksen sen sijaan, että se vastaisi tarkkoja sanoja

Semanttinen haku on hyödyllinen luonnollisen kielen kyselyille, kuten "viljelijä Baijerissa 1800-luvulla". Se vaatii semanttisen hakun indeksin olevan täytetty; katso [Hallinta-asetukset](../administration/settings.md) siitä, miten indeksi rakennetaan tai päivitetään.
