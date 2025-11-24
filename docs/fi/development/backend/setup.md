# Taustakehityksen asetukset

Tällä sivulla luetellaan vaiheet, jotka tarvitaan [Gramps Web API:n](https://github.com/gramps-project/gramps-web-api/) kehittämisen aloittamiseen, joka on Gramps Webin taustapalvelin (palvelinosa).


## Esivaatimukset

Suositeltu kehitysympäristö käyttää Visual Studio Codea devcontainersin kanssa. Tämä lähestymistapa luo esikonfiguroidun kehitysympäristön, jossa on kaikki tarvittavat työkalut. Aloittaaksesi tarvitset seuraavat ainekset:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) asennettuna [Dev Containers -laajennuksella](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com)

Voit käyttää käyttöjärjestelmänä Linuxia, macOS:ää tai Windowsia.


## Aloittaminen

1. Avaa [Gramps Web API -varasto](https://github.com/gramps-project/gramps-web-api) ja napsauta "fork"
2. Kloonaa forkattu varasto paikalliselle koneellesi Gitin avulla
3. Avaa kloonattu varasto Visual Studio Codessa. Kun sinua kehotetaan, valitse "Avaa uudelleen säilössä" tai avaa manuaalisesti komentoikkuna (Ctrl+Shift+P tai Cmd+Shift+P) ja valitse "Dev Containers: Uudelleenrakennus ja avaa uudelleen säilössä".
4. Odota, että dev-säilö rakennetaan ja käynnistyy. Tämä voi kestää muutaman minuutin, erityisesti ensimmäisellä kerralla.


## Tehtävät

Jos muokkaat vain taustakoodia, sinun ei välttämättä tarvitse käynnistää verkkopalvelinta - yksikkötestit käyttävät Flask-testiasiakasta, joka mahdollistaa API:lle osoitettujen pyyntöjen simuloimisen ilman toimivaa palvelinta.

Kuitenkin palvelimen käynnistäminen on hyödyllistä, jos

- haluat kokeilla muutoksiasi oikeilla HTTP-pyynnöillä (katso [manuaaliset kyselyt](queries.md)),
- haluat esikatsella muutosten vaikutusta koko Gramps Web -sovellukseen, tai
- haluat myös tehdä samanaikaisia muutoksia etupäähän (katso [etupään kehityksen asetukset](../frontend/setup.md)).

Palvelimen käynnistäminen on yksinkertaistettu dev-säilössä ennalta määritellyillä tehtävillä. Voit suorittaa nämä tehtävät komentoikkunasta (Ctrl+Shift+P tai Cmd+Shift+P) valitsemalla "Tehtävät: Suorita tehtävä" ja valitsemalla sitten jonkin seuraavista:
- "Palvelin Web API" - käynnistää Flask-kehityspalvelimen portissa 5555 debug-lokitus käytössä
- "Käynnistä Celery-työntekijä" - käynnistää Celery-työntekijän taustatehtävien käsittelyä varten.


## Virheenkorjaus

Virheenkorjaus voi joskus olla haastavaa, erityisesti monimutkaisen käyttäytymisen jäljittämisessä tai hienovaraisten ongelmien tunnistamisessa. Tämän helpottamiseksi voit virheenkorjata sekä toimivaa API-instanssia että yksittäisiä testitapauksia suoraan Visual Studio Codessa.

### Gramps Web API:n virheenkorjaus

Virheenkorjataksesi toimivaa API:a:

1. Avaa Visual Studio Code ja siirry **Suorita ja virheenkorjaa** -näkymään.  
2. Valitse **"Web API"** -konfiguraatio pudotusvalikosta.  
3. Aloita virheenkorjaus.  
4. Kun lähetät pyyntöjä taustalle (joko manuaalisesti tai Gramps Web -käyttöliittymän kautta), suoritus pysähtyy kaikissa koodissa asettamissasi katkaisupisteissä.  
   Tämä mahdollistaa muuttujien tarkastelun, ohjausvirran hallinnan ja muiden ajonaikaisten yksityiskohtien tarkastelun.

### Testitapausten virheenkorjaus

Virheenkorjataksesi tietyn testitapauksen:

1. Avaa testitiedosto, jota haluat virheenkorjata (esimerkiksi `test_people.py`).  
2. Visual Studio Codessa avaa **Suorita ja virheenkorjaa** -näkymä.  
3. Valitse **"Nykyinen testitiedosto"** -konfiguraatio.  
4. Aloita virheenkorjaus — suoritus pysähtyy kaikissa katkaisupisteissä, jotka on asetettu kyseisessä testitiedostossa.  

Tämä asetus mahdollistaa testilogiikan läpikäymisen, muuttujien arvojen tarkastelun ja testivirheiden tai odottamattomien tulosten paremman ymmärtämisen.
