---
hide:
  - toc
---

# Käyttäjän opas

Tässä osiossa dokumentoidaan Gramps Webin käyttäjille saatavilla olevat ominaisuudet.

!!! note "Etkö näe kaikkia ominaisuuksia?"
    Gramps Web käyttää rooliin perustuvaa käyttöoikeusjärjestelmää. Jotkin ominaisuudet – kuten tietojen muokkaaminen, tunnisteiden hallinta tai yksityisten tietojen katsominen – ovat saatavilla vain käyttäjille, joilla on riittävät käyttöoikeudet. Voit tarkistaa nykyisen roolisi [Käyttäjäasetuksista](settings.md). Jos tarvitset enemmän pääsyä, ota yhteyttä puusi omistajaan tai ylläpitäjään. Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi kuvauksen kaikista rooleista.

## Käyttöliittymän navigointi

### Päävalikko

Sivupalkki (tai hampurilaisvalikko mobiililaitteilla) on ensisijainen tapa siirtyä osioiden välillä:

- **Etusivu** – hallintapaneeli (katso alla)
- **Blogi** – perhehistorian tarinat blogikirjoituksina
- **Perhepuu** – interaktiiviset puukaaviot
- **Aikajana** – aikajänne tapahtumista puussa (vaatii riittävän uuden Gramps Web API -version)
- **Kartta** – maantieteellinen näkymä paikoista puussa
- **DNA** – DNA-otteluanalyysityökalut
- **Luettelot** – selaa kaikkia kunkin tyyppisiä objekteja: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot
- **Media** – selaa kaikkia mediakuvia (valokuvia, asiakirjoja jne.)
- **Avustaja** – AI-keskusteluavustaja (jos ylläpitäjä on sen mahdollistanut)
- **Historia** – äskettäin muutetut objektit
- **Kirjanmerkit** – tallennetut kirjanmerkit
- **Tehtävät** – tutkimustehtävät
- **Raportit** – luo raportteja
- **Vienti** – vie perhepuu
- **Muokkaukset** – täydellinen tapahtumahistoria (näkyvissä jäsenille ja sitä korkeammille)
- **Ilmoitukset** – aiemmat ilmoitukset

!!! note
    Tunnisteita ei enää hallita sivupalkista – tunnisteiden hallinta on siirtynyt [Hallinta-asetuksiin](../administration/settings.md#tags) (Omistaja/Ylläpitäjä vain). Katso [Tunnisteet](tags.md) siitä, miten tunnisteita käytetään.

### Yläosapalkki

Jokaisen sivun yläosassa on:

- **Lisää** (plus-kuvake, näkyvissä myötävaikuttajille ja sitä korkeammille) – avaa valikon uuden objektin luomiseksi: Henkilö, Perhe, Tapahtuma, Paikka, Lähde, Viittaus, Arkisto, Muistiinpano, Mediakohde tai Tehtävä
- **Haku** (suurenennuslasi) – avaa hakusivun
- **Käyttäjäkuvake** – avaa asetusten valikon: Käyttäjäasetukset, Hallinta (vain omistajille), Käyttäjien hallinta (vain omistajille), Järjestelmän tiedot

## Etusivu (hallintapaneeli)

Hallintapaneeli näkyy, kun kirjaudut ensimmäisen kerran sisään. Siinä on kaksi saraketta:

**Vasen sarake:**

- **Kotihenkilön kortti** – näyttää valitun kotihenkilön nimen, valokuvan (jos saatavilla) ja keskeiset tiedot, sekä linkin heidän täydelliseen profiiliinsa ja nopean navigoinnin perhepuuhun. Napsauta **Aseta kotihenkilö** -painiketta kortissa etsiäksesi ja valitaksesi toisen henkilön.
- **Merkkipäivät** – tulevat syntymäpäivät ja merkkipäivät puusta, perustuen tämän päivän päivämäärään.
- **Äskettäin muutetut** – lyhyt luettelo äskettäin muokatuista objekteista, hyödyllinen yhteistyömuokkauksen seuraamiseen.

**Oikea sarake:**

- **Äskettäin julkaistut blogikirjoitukset** – uusimmat merkinnät [blogista](blog.md), jos sellaisia on.
- **Tilastot** – yhteenveto objektien määrästä puussa (ihmisten, perheiden, tapahtumien jne. määrä).

Jos puun ylläpitäjä on määrittänyt **etusivun muistiinpanon** ja/tai **etusivun kuvan**, ne näkyvät selvästi pääsarakkeiden yläpuolella. Kuva näkyy muistiinpanotekstin vieressä, kun molemmat on asetettu. Katso [Hallinta-asetukset](../administration/settings.md#customization) siitä, miten nämä määritetään.

!!! tip
    Jos puu on tyhjillään ja sinulla on muokkausoikeudet, hallintapaneeli näyttää "Aloita" -kehotteen, jossa on painikkeet ensimmäisen henkilön lisäämiseksi tai perhepuutiedoston tuomiseksi.
