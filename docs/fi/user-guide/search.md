# Haku

Hakusivulle pääsee napsauttamalla suurennuslasikuvaketta ylävalikossa tai painamalla `s` [näppäinoikoreittiä](shortcuts.md).

## Koko tekstin haku

Kirjoita mikä tahansa kysely hakukenttään ja paina Enter (tai napsauta hakupainiketta). Gramps Web etsii kaikista objektityypeistä – ihmiset, perheet, tapahtumat, paikat, lähteet, viittaukset, arkistot, muistiinpanot ja media – ja palauttaa osumat, jotka on järjestetty relevanssin mukaan.

Tuloksissa näkyvät objektityyppi, nimi ja lyhyt yhteenveto. Napsauta mitä tahansa tulosta avataksesi vastaavan yksityiskohtasivun.

Perässä oleva `*` voidaan käyttää jokerimerkkinä, esim. `Mey*` vastaa "Meyer", "Meyers", "Meyerhofer" jne.

## Suodatus objektityypin mukaan

Hakukentän alapuolella olevat kytkinpainikkeet jokaiselle objektityypille (Ihmiset, Perheet, Tapahtumat, Paikat, …) antavat sinun rajata tuloksia yhteen tai useampaan tiettyyn tyyppiin. Oletuksena haetaan kaikista tyypeistä. Yhden tai useamman kytkimen aktivoiminen rajoittaa tulokset vain näihin tyyppeihin.

## Semanttinen haku

!!! warning "Poistettu käytöstä"
    Semanttinen haku on poistettu käytöstä ja se poistuu Gramps Web API 3.25:ssä. Yllä kuvattu koko tekstin haku ei vaikuta.

Jos palvelimen ylläpitäjä on mahdollistanut [semanttisen (AI-pohjaisen) haun](../install_setup/chat.md#semantic-search-deprecated), hakusivun oikeassa yläkulmassa näkyy tilakytkin, jossa on kaksi vaihtoehtoa:

- **Haku** – standardi koko tekstin haku (oletus)
- **Semanttinen** – AI-pohjainen haku, joka ymmärtää kyselysi merkityksen sen sijaan, että se vastaisi tarkkoja sanoja

Semanttinen haku on hyödyllinen luonnollisen kielen kyselyille, kuten "maanviljelijä Baijerissa 1800-luvulla". Se vaatii semanttisen hakun indeksin olevan täytetty; katso [Hallintasettings](../administration/settings.md) kuinka rakentaa tai päivittää indeksi.
