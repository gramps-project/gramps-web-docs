---
hide:
  - toc
---

# Käyttäjän opas

Tässä osiossa dokumentoidaan Gramps Webin käyttäjille saatavilla olevat ominaisuudet.

!!! note "Etkö näe kaikkia ominaisuuksia?"
    Gramps Web käyttää rooliin perustuvaa käyttöoikeusjärjestelmää. Jotkin ominaisuudet – kuten tietojen muokkaaminen, tagien hallinta tai yksityisten tietojen katsominen – ovat saatavilla vain käyttäjille, joilla on riittävät käyttöoikeudet. Voit tarkistaa nykyisen roolisi [Käyttäjäasetuksista](settings.md). Jos tarvitset enemmän käyttöoikeuksia, ota yhteyttä puusi omistajaan tai ylläpitäjään. Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi kuvauksen kaikista rooleista.

## Käyttöliittymän navigointi

### Päävalikko

Sivupalkki (tai hampurilaisvalikko mobiilissa) on ensisijainen tapa siirtyä osioiden välillä:

- **Etusivu** – hallintapaneeli (katso alla)
- **Blogi** – perhesuhteisiin liittyviä tarinoita blogikirjoituksina
- **Suku puu** – interaktiiviset sukupuutkaaviot
- **Aikajana** – aikajana tapahtumista puussa (vaatii riittävän uuden Gramps Web API -version)
- **Kartta** – maantieteellinen näkymä paikoista puussa
- **DNA** – DNA-yhteensopivuusanalyysityökalut
- **Luettelot** – selaa kaikkia kunkin tyyppisiä objekteja: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot
- **Media** – selaa kaikkia mediakuvia (valokuvia, asiakirjoja jne.)
- **Avustaja** – AI-keskusteluavustaja (jos ylläpitäjä on sen mahdollistanut)
- **Historia** – äskettäin muutetut objektit
- **Kirjanmerkit** – tallennetut kirjanmerkkisi
- **Tehtävät** – tutkimustehtävät
- **Raportit** – luo raportteja
- **Vienti** – vie sukupuu
- **Muokkaukset** – täydellinen tapahtumahistoria (näkyvissä jäsenille ja sitä korkeammille)
- **Ilmoitukset** – aiemmat ilmoitukset

!!! note
    Tägejä ei enää hallita sivupalkista – tagien hallinta on siirtynyt [Hallinta-asetuksiin](../administration/settings.md#tags) (Omistaja/Ylläpitäjä vain). Katso [Tägien käyttö](tags.md) saadaksesi tietoa tagien käytöstä.

### Yläpalkki

Jokaisen sivun yläreunassa on:

- **Lisää** (plus-ikoni, näkyvissä kontribuuttoreille ja sitä korkeammille) – avaa valikon uuden objektin luomiseksi: Henkilö, Perhe, Tapahtuma, Paikka, Lähde, Viittaus, Arkisto, Muistiinpano, Mediakohde tai Tehtävä
- **Haku** (suurenennuslasi) – avaa hakusivun
- **Käyttäjäikoni** – avaa asetusten valikon: Käyttäjäasetukset, Hallinta (vain omistajille), Käyttäjien hallinta (vain omistajille), Järjestelmän tiedot

## Etusivu (hallintapaneeli)

Hallintapaneeli näkyy, kun kirjaudut ensimmäistä kertaa sisään. Siinä on kaksi saraketta:

**Vasen sarake:**

- **Kotihenkilön kortti** – näyttää valitun kotihenkilön nimen, valokuvan (jos saatavilla) ja keskeiset tiedot, linkin heidän täydelliseen profiiliinsa ja nopean navigoinnin sukupuuhun. Napsauta **Aseta kotihenkilö** -painiketta kortilla etsiäksesi ja valitaksesi toisen henkilön.
- **Merkkipäivät** – tulevat syntymäpäivät ja merkkipäivät puusta, perustuen tämän päivän päivämäärään.
- **Äskettäin muutetut** – lyhyt luettelo äskettäin muokatuista objekteista, hyödyllinen yhteistyömuokkauksien seuraamiseen.

**Oikea sarake:**

- **Äskettäin julkaistut blogikirjoitukset** – uusimmat merkinnät [blogista](blog.md), jos sellaisia on.
- **Tilastot** – yhteenveto objektien määrästä puussa (ihmisten, perheiden, tapahtumien jne. määrä).

Kun puu on vielä tyhjillään, hallintapaneeli piilottaa paneelit, joilla ei olisi mitään näytettävää, ja sen sijaan näyttää **Aloita**-kortin käyttäjille, joilla on muokkausoikeudet: se tarjoaa ensin mahdollisuuden luoda henkilön tai tuoda sukupuututiedosto, ja kun henkilöitä on olemassa, yhdistää heidät luomalla perheen. Kortti katoaa heti, kun puu sisältää perheen.

Jos puun ylläpitäjä on määrittänyt **etusivun muistiinpanon** ja/tai **etusivun kuvan**, nämä näkyvät selvästi pääsarakkeiden yläpuolella. Kuva näkyy muistiinpanotekstin vieressä, kun molemmat on asetettu. Katso [Hallinta-asetukset](../administration/settings.md#customization) saadaksesi tietoa näiden määrittämisestä.

!!! tip
    Jos puu on tyhjillään ja sinulla on muokkausoikeudet, hallintapaneeli näyttää "Aloita" -kehotteen, jossa on painikkeet ensimmäisen henkilön lisäämiseksi tai sukupuututiedoston tuomiseksi.

## Gramps Webin asentaminen sovelluksena

Gramps Web on edistyksellinen verkkosovellus (PWA), mikä tarkoittaa, että selain voi asentaa sen muiden sovellusten rinnalle sen sijaan, että se pidettäisiin selainvälilehdessä. Se saa sitten oman kuvakkeensa ja avautuu omassa ikkunassaan, ilman osoiteriviä ja selaintyökaluja.

Asentaminen riippuu selaimestasi:

- **Android (Chrome)** – avaa valikko ja valitse "Asenna sovellus" tai "Lisää aloitusnäyttöön".
- **iOS/iPadOS (Safari)** – napauta jakopainiketta ja valitse "Lisää aloitusnäyttöön".
- **Työpöytä (Chrome, Edge)** – napsauta asennusikonia osoiterivin oikeassa reunassa tai käytä selaimen valikon "Asenna" -kohtaa.
- **Työpöytä (Firefox, Safari)** – asennusta ei tueta; käytä normaalia selainvälilehteä tai -ikkunaa.

Mikään ei muutu siitä, miten Gramps Web toimii, eikä tietoja tallenneta eri tavalla – se on sama sovellus, vain esitetty itsenäisenä sovelluksena.

!!! note
    Gramps Web tarvitsee edelleen päästä palvelimellesi näyttääkseen tietosi, joten asennettu sovellus ei salli perhesukupuusi selaamista offline-tilassa.
