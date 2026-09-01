---
hide:
  - toc
---

# Käyttäjän opas

Tässä osiossa dokumentoidaan Gramps Webin käyttäjille saatavilla olevat ominaisuudet.

!!! note "Etkö näe kaikkia ominaisuuksia?"
    Gramps Web käyttää rooliin perustuvaa käyttöoikeusjärjestelmää. Jotkin ominaisuudet – kuten tietojen muokkaaminen, tagien hallinta tai yksityisten tietojen tarkastelu – ovat saatavilla vain käyttäjille, joilla on riittävät käyttöoikeudet. Voit tarkistaa nykyisen roolisi [Käyttäjäasetuksista](settings.md). Jos tarvitset enemmän pääsyä, ota yhteyttä puusi omistajaan tai ylläpitäjään. Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi kuvauksen kaikista rooleista.

## Käyttöliittymässä navigointi

### Päävalikko

Sivupalkki (tai hampurilaisvalikko mobiilissa) on ensisijainen tapa siirtyä osioiden välillä:

- **Koti** – hallintapaneeli (katso alla)
- **Blogi** – perhesuhteisiin liittyvät tarinat blogikirjoituksina
- **Sukujuuri** – interaktiiviset puukaaviot
- **Aikajana** – aikajananäkymä tapahtumista puussa (vaatii riittävän uuden Gramps Web API -version)
- **Kartta** – maantieteellinen näkymä paikoista puussa
- **DNA** – DNA-otteluanalyysityökalut
- **Luettelot** – selaa kaikkia kunkin tyyppisiä objekteja: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot
- **Media** – selaa kaikkia mediakuvia (valokuvia, asiakirjoja jne.)
- **Avustaja** – AI-chat-avustaja (jos ylläpitäjä on sen mahdollistanut)
- **Historia** – äskettäin muutetut objektit
- **Kirjanmerkit** – tallennetut kirjanmerkkisi
- **Tehtävät** – tutkimustehtävät
- **Raportit** – luo raportteja
- **Vienti** – vie sukupuu
- **Muokkaukset** – täydellinen tapahtumahistoria (näkyy jäsenille ja sitä korkeammille)
- **Ilmoitukset** – aiemmat ilmoitukset

!!! note
    Tägejä ei enää hallita sivupalkista – tagien hallinta on siirtynyt [Hallinta-asetuksiin](../administration/settings.md#tags) (Omistaja/Ylläpitäjä vain). Katso [Tägien käyttö](tags.md) saadaksesi lisätietoja.

### Yläosan sovellusvalikko

Jokaisen sivun yläosassa oleva palkki sisältää:

- **Lisää** (plus-ikoni, näkyvissä kontribuuttoreille ja sitä korkeammille) – avaa valikon uuden objektin luomiseksi: Henkilö, Perhe, Tapahtuma, Paikka, Lähde, Viittaus, Arkisto, Muistiinpano, Mediakohde tai Tehtävä
- **Haku** (suurenennuslasi) – avaa hakusivun
- **Käyttäjäikoni** – avaa asetusten valikon: Käyttäjäasetukset, Hallinta (vain omistajille), Käyttäjien hallinta (vain omistajille), Järjestelmäinfo

## Etusivu (hallintapaneeli)

Hallintapaneeli näkyy, kun kirjaudut ensimmäisen kerran sisään. Siinä on kaksi saraketta:

**Vasen sarake:**

- **Koti-henkilökortti** – näyttää valitun koti-henkilön nimen, valokuvan (jos saatavilla) ja keskeiset tiedot, sekä linkin heidän täydelliseen profiiliinsa ja nopean navigoinnin sukupuuhun. Napsauta **Aseta koti-henkilö** -painiketta kortilla etsiäksesi ja valitaksesi toisen henkilön.
- **Merkkipäivät** – tulevat syntymäpäivät ja merkkipäivät puusta, perustuen tämän päivän päivämäärään.
- **Äskettäin muutettu** – lyhyt lista äskettäin muokatuista objekteista, hyödyllinen yhteistyömuokkauksen seuraamiseen.

**Oikea sarake:**

- **Äskettäin julkaistut blogikirjoitukset** – uusimmat merkinnät [blogista](blog.md), jos sellaisia on.
- **Tilastot** – yhteenveto objektien määrästä puussa (ihmisten, perheiden, tapahtumien jne. määrä).

Jos puun ylläpitäjä on määrittänyt **etusivun muistiinpanon** ja/tai **etusivun kuvan**, nämä näkyvät selvästi pääsarakkeiden yläpuolella. Kuva näkyy muistiinpanotekstin vieressä, kun molemmat on asetettu. Katso [Hallinta-asetukset](../administration/settings.md#customization) saadaksesi ohjeita näiden määrittämiseen.

!!! tip
    Jos puu on tyhjillään ja sinulla on muokkausoikeudet, hallintapaneeli näyttää "Aloita" -kehotteen, jossa on painikkeet ensimmäisen henkilön lisäämiseksi tai sukupuun tiedoston tuomiseksi.

## Gramps Webin asentaminen sovelluksena

Gramps Web on progressiivinen web-sovellus (PWA), mikä tarkoittaa, että selain voi asentaa sen muiden sovellusten rinnalle sen sijaan, että se pidettäisiin selainvälilehdessä. Se saa sitten oman kuvakkeensa ja avautuu omassa ikkunassaan, ilman osoiteriviä ja selainvalikoita.

Asennustapa riippuu selaimestasi:

- **Android (Chrome)** – avaa valikko ja valitse "Asenna sovellus" tai "Lisää aloitusnäyttöön".
- **iOS/iPadOS (Safari)** – napauta jakopainiketta ja valitse "Lisää aloitusnäyttöön".
- **Työpöytä (Chrome, Edge)** – napsauta asennuskuvaketta osoiterivin oikeassa päässä tai käytä selaimen valikon "Asenna" -kohtaa.
- **Työpöytä (Firefox, Safari)** – asennusta ei tueta; käytä normaalia selainvälilehteä tai -ikkunaa.

Mikään ei muutu siitä, miten Gramps Web toimii, eikä tietoja tallenneta eri tavalla – se on sama sovellus, vain esitetty erillisenä sovelluksena.

!!! note
    Gramps Web tarvitsee edelleen päästä palvelimellesi näyttääkseen tietosi, joten asennettu sovellus ei salli sinun selata sukupuuta offline-tilassa.
