---
hide:
  - toc
---

# Käyttäjän opas

Tässä osiossa dokumentoidaan Gramps Webin käyttäjille saatavilla olevat ominaisuudet.

!!! note "Etkö näe kaikkia ominaisuuksia?"
    Gramps Web käyttää rooliin perustuvaa käyttöoikeusjärjestelmää. Jotkin ominaisuudet – kuten tietojen muokkaaminen, tagien hallinta tai yksityisten tietojen katselu – ovat saatavilla vain käyttäjille, joilla on riittävät käyttöoikeudet. Voit tarkistaa nykyisen roolisi [Käyttäjäasetuksista](settings.md). Jos tarvitset lisää käyttöoikeuksia, ota yhteyttä puun omistajaan tai ylläpitäjään. Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi kuvauksen kaikista rooleista.

## Käyttöliittymässä navigointi

### Päävalikko

Sivupalkki (tai hampurilaisvalikko mobiilissa) on ensisijainen tapa siirtyä osioiden välillä:

- **Etusivu** – hallintapaneeli (katso alla)
- **Blogi** – perhesuhteista kertovia tarinoita blogikirjoituksina
- **Sukupuu** – interaktiiviset sukupuukaaviot
- **Aikajana** – aikajärjestyksessä esitetyt tapahtumat puussa (vaatii riittävän uuden Gramps Web API -version)
- **Kartta** – maantieteellinen näkymä paikoista puussa
- **DNA** – DNA-yhteensopivuuden analyysityökalut
- **Luettelot** – selaa kaikkia kunkin tyyppisiä objekteja: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot
- **Media** – selaa kaikkia mediatauluja (valokuvia, asiakirjoja jne.)
- **Avustaja** – AI-keskusteluavustaja (jos ylläpitäjä on sen mahdollistanut)
- **Historia** – äskettäin muutetut objektit
- **Kirjanmerkit** – tallennetut kirjanmerkkisi
- **Tehtävät** – tutkimustehtävät
- **Raportit** – luo raportteja
- **Vienti** – vie sukupuu
- **Muokkaukset** – täydellinen tapahtumahistoria (näkyvissä jäsenille ja sitä korkeammille)

!!! note
    Tägejä ei enää hallita sivupalkista – tagien hallinta on siirtynyt [Hallinta-asetuksiin](../administration/settings.md#tags) (Omistaja/Ylläpitäjä vain). Katso [Tägien käyttö](tags.md) saadaksesi tietoa siitä, miten tageja käytetään.

### Ylävalikkopalkki

Jokaisen sivun yläreunassa oleva palkki sisältää:

- **Lisää** (plus-kuvake, näkyvissä osallistujille ja sitä korkeammille) – avaa valikon uuden objektin luomiseksi: Henkilö, Perhe, Tapahtuma, Paikka, Lähde, Viittaus, Arkisto, Muistiinpano, Mediakohde tai Tehtävä
- **Haku** (suurenennuslasi) – avaa hakusivun
- **Kello** – avaa [ilmoitukset](notifications.md), mukaan lukien muiden käyttäjien tekemät muutokset ja valmiit taustatehtävät
- **Käyttäjäkuvake** – avaa asetusten valikon: Käyttäjäasetukset, Hallinta (vain omistajille), Käyttäjien hallinta (vain omistajille), Järjestelmätiedot

## Etusivu (hallintapaneeli)

Hallintapaneeli näkyy, kun kirjaudut ensimmäisen kerran sisään. Siinä on kaksi saraketta:

**Vasen sarake:**

- **Kotihenkilön kortti** – näyttää valitun kotihenkilön nimen, valokuvan (jos saatavilla) ja keskeiset tiedot, sekä linkin heidän täydelliseen profiiliinsa ja nopean navigoinnin sukupuuhun. Napsauta **Aseta kotihenkilö** -painiketta kortilla etsiäksesi ja valitaksesi toisen henkilön.
- **Merkkipäivät** – tulevat syntymäpäivät ja merkkipäivät puusta, perustuen tämän päivän päivämäärään.
- **Äskettäin muutetut** – lyhyt lista äskettäin muokatuista objekteista, hyödyllinen yhteistyömuokkauksien seuraamiseen.

**Oikea sarake:**

- **Äskettäin julkaistut blogikirjoitukset** – uusimmat merkinnät [blogista](blog.md), jos sellaisia on.
- **Tilastot** – yhteenveto objektien määrästä puussa (ihmisten, perheiden, tapahtumien jne. määrä).

Kun puu on vielä tyhjillään, hallintapaneeli piilottaa paneelit, joilla ei ole mitään näytettävää, ja näyttää sen sijaan **Aloita**-kortin käyttäjille, joilla on muokkausoikeudet: se tarjoaa ensin mahdollisuuden luoda henkilön tai tuoda perhesuhteetiedoston, ja kun henkilöitä on olemassa, yhdistää heidät perheen luomisen avulla. Kortti katoaa heti, kun puussa on perhe.

Jos puun ylläpitäjä on määrittänyt **etusivun muistiinpanon** ja/tai **etusivun kuvan**, nämä näkyvät selvästi pääsarakkeiden yläpuolella. Kuva näkyy muistiinpanotekstin vieressä, kun molemmat on asetettu. Katso [Hallinta-asetukset](../administration/customization.md) saadaksesi tietoa näiden määrittämisestä.

!!! tip
    Jos puu on tyhjillään ja sinulla on muokkausoikeudet, hallintapaneeli näyttää "Aloita" -kehotteen, jossa on painikkeet ensimmäisen henkilön lisäämiseksi tai perhesuhteetiedoston tuomiseksi.

## Gramps Webin asentaminen sovelluksena

Gramps Web on edistyksellinen verkkosovellus (PWA), mikä tarkoittaa, että selain voi asentaa sen muiden sovellustesi rinnalle sen sijaan, että se pidettäisiin selainvälilehdessä. Se saa sitten oman kuvakkeensa ja avautuu omassa ikkunassaan, ilman osoiteriviä ja selainvalikoita.

Asennustapa riippuu selaimestasi:

- **Android (Chrome)** – avaa valikko ja valitse "Asenna sovellus" tai "Lisää aloitusnäyttöön".
- **iOS/iPadOS (Safari)** – napauta jakopainiketta ja valitse "Lisää aloitusnäyttöön".
- **Työpöytä (Chrome, Edge)** – napsauta asennuskuvaketta osoiterivin oikeassa päässä tai käytä selaimen valikon "Asenna" -kohtaa.
- **Työpöytä (Firefox, Safari)** – asennusta ei tueta; käytä normaalia selainvälilehteä tai -ikkunaa.

Mikään ei muutu siinä, miten Gramps Web toimii, eikä tietoja tallenneta eri tavalla – se on sama sovellus, vain esitetty erillisenä sovelluksena.

!!! note
    Gramps Web tarvitsee edelleen päästä palvelimellesi näyttääkseen tietosi, joten asennettu sovellus ei salli sinun selata perhesuhteitasi offline-tilassa.
