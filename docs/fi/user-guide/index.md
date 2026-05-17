---
hide:
  - toc
---

# Käyttäjän opas

Tässä osiossa dokumentoidaan Gramps Webin käyttäjille saatavilla olevat ominaisuudet.

!!! note "Etkö näe kaikkia ominaisuuksia?"
    Gramps Web käyttää rooliin perustuvaa käyttöoikeusjärjestelmää. Jotkin ominaisuudet – kuten tietojen muokkaaminen, tagien hallinta tai yksityisten tietojen katselu – ovat saatavilla vain käyttäjille, joilla on riittävät oikeudet. Voit tarkistaa nykyisen roolisi [Käyttäjäasetuksista](settings.md). Jos tarvitset enemmän käyttöoikeuksia, ota yhteyttä puusi omistajaan tai ylläpitäjään. Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi kuvauksen kaikista rooleista.

## Käyttöliittymässä navigointi

### Päävalikko

Sivupalkki (tai hampurilaisvalikko mobiilissa) on ensisijainen tapa siirtyä osioiden välillä:

- **Koti** – hallintapaneeli (katso alla)
- **Blogi** – perhehistorian tarinoita blogikirjoituksina
- **Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot** – selaa kaikkia kunkin tyyppisiä objekteja
- **Media** – selaa kaikkia mediakuvia (valokuvia, asiakirjoja jne.)
- **Kartta** – maantieteellinen näkymä paikoista puussa
- **Sukupuu** – interaktiiviset puukaaviot
- **DNA** – DNA-otteluanalyysityökalut
- **Chat** – AI-chat-avustaja (jos ylläpitäjä on ottanut sen käyttöön)
- **Historia** – äskettäin muutetut objektit
- **Kirjanmerkit** – tallennetut kirjanmerkit
- **Tehtävät** – tutkimustehtävät
- **Vienti** – vie sukupuu
- **Raportit** – luo raportteja
- **Muokkaukset** – täydellinen tapahtumahistoria (näkyvissä jäsenille ja sitä korkeammille)
- **Tagit** – hallitse tageja (näkyvissä muokkaajille ja sitä korkeammille)
- **Ilmoitukset** – aiemmat ilmoitukset

### Ylävalikkopalkki

Jokaisen sivun yläreunassa oleva palkki sisältää:

- **Lisää** (plus-ikoni, näkyvissä kontribuuttoreille ja sitä korkeammille) – avaa valikon uuden objektin luomiseksi: Henkilö, Perhe, Tapahtuma, Paikka, Lähde, Viittaus, Arkisto, Muistiinpano, Mediakohde tai Tehtävä
- **Haku** (suurenennuslasi) – avaa hakusivun
- **Käyttäjäikoni** – avaa asetusten valikon: Käyttäjäasetukset, Hallinta (vain omistajille), Käyttäjien hallinta (vain omistajille), Järjestelmän tiedot

## Etusivu (hallintapaneeli)

Hallintapaneeli näkyy, kun kirjaudut sisään ensimmäistä kertaa. Siinä on kaksi saraketta:

**Vasen sarake:**

- **Koti-henkilökortti** – näyttää valitun koti-henkilön nimen, valokuvan (jos saatavilla) ja keskeiset tiedot, sekä linkin heidän täydelliseen profiiliinsa ja nopean navigoinnin sukupuuhun. Napsauta **Aseta koti-henkilö** -painiketta kortilla etsiäksesi ja valitaksesi toisen henkilön.
- **Merkkipäivät** – tulevat syntymäpäivät ja merkkipäivät puusta, perustuen tämän päivän päivämäärään.
- **Äskettäin muutetut** – lyhyt lista äskettäin muokatuista objekteista, hyödyllinen yhteistyömuokkauksien seuraamiseen.

**Oikea sarake:**

- **Äskettäin julkaistut blogikirjoitukset** – uusimmat merkinnät [blogista](blog.md), jos sellaisia on.
- **Tilastot** – yhteenveto objektien määrästä puussa (ihmisten, perheiden, tapahtumien jne. määrä).

Jos puun ylläpitäjä on määrittänyt **etusivun muistiinpanon** ja/tai **etusivun kuvan**, nämä näkyvät selvästi pääsarakkeiden yläpuolella. Kuva näkyy muistiinpanotekstin vieressä, kun molemmat on asetettu. Katso [Hallinta-asetukset](../administration/settings.md#customization) saadaksesi tietoa näiden määrittämisestä.

!!! tip
    Jos puu on tyhjillään ja sinulla on muokkausoikeudet, hallintapaneeli näyttää "Aloita" -kehotteen, jossa on painikkeet ensimmäisen henkilön lisäämiseksi tai perhepuutiedoston tuomiseksi.
