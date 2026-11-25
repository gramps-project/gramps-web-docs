# Palvelimen määritys

Oletusarvoista Docker-vedosta käytettäessä kaikki tarvittavat määritykset voidaan tehdä selaimella. Käyttöönotosta riippuen palvelimen määrityksiä voi kuitenkin olla tarpeen mukauttaa.

Tällä sivulla luetellaan kaikki määritysten muuttamiseen käytettävissä olevat menetelmät ja kaikki olemassa olevat määritysvaihtoehdot.


## Määritystiedosto vs. ympäristömuuttujat

Voit käyttää asetuksiin joko määritystiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää määritystiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on määritystiedoston polku palvelimesi tiedostojärjestelmässä (oikeanpuoleinen puoli viittaa kontin sisäiseen polkuun, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen nimen eteen etuliite `GRAMPSWEB_`, jolloin saat ympäristömuuttujan nimen
- Käytä sisäkkäisten sanakirja-asetusten yhteydessä kahta alaviivaa, esimerkiksi `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa määritysvaihtoehdon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` arvon

Huomaa, että ympäristön kautta asetetut määritysvaihtoehdot ovat etusijalla määritystiedoston asetuksiin nähden. Jos molemmat ovat olemassa, ympäristömuuttuja ”voittaa”.

!!! warning "Etuliitteettömät ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä kourallinen asetuksia – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujalla *ilman* `GRAMPSWEB_`-etuliitettä. Tämä on vanhentunutta, aiheuttaa varoituksen käynnistyksen yhteydessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esimerkiksi `GRAMPSWEB_TREE` muuttujan `TREE` sijaan.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Määritystiedostossa asetusten nimet ovat aina ilman etuliitettä.

!!! tip "Vanhentuneiden asetusten tarkistaminen"
    Vanhentuneet määritysvaihtoehdot, joihin palvelimesi edelleen tukeutuu – kuten etuliitteettömät ympäristömuuttujat, `SEARCH_INDEX_DIR` tai `EMAIL_USE_TLS` – kirjataan varoituksina käynnistyksen yhteydessä. Gramps Web API 3.22:sta lähtien ne luetellaan myös korvaavan asetuksensa ja tuen poistavan version kanssa **Järjestelmätiedot**-sivun yläosassa (sivulle pääsee yläpalkin käyttäjäkuvakkeesta), kun olet kirjautuneena ylläpitäjänä.

    Myös vanhempien versioiden ensimmäisen käynnistyksen ohjatun toiminnon tietokantaan tallentamat sähköpostiasetukset ja perus-URL-osoite luetellaan siellä. Aseta ne määrityksiisi tallennettujen arvojen mukaisesti; varoitus katoaa, kun arvot täsmäävät.

## Olemassa olevat määritysasetukset
Seuraavat määritysvaihtoehdot ovat käytettävissä.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuutietokannan nimi. Näytä käytettävissä olevat puut komennolla `gramps -l`. Jos tämännimistä puuta ei ole olemassa, luodaan uusi tyhjä puu.
`SECRET_KEY` | Flaskin salainen avain. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki käyttöoikeustunnukset.
`USER_DB_URI` | Käyttäjätietokannan tietokanta-URL-osoite. Kaikki SQLAlchemyn kanssa yhteensopivat URL-osoitteet ovat sallittuja.

!!! info
    Voit luoda turvallisen salaisen avaimen esimerkiksi komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Mediatiedostojen perushakemistona käytettävä polku, joka ohittaa Grampsissa asetetun median perushakemiston. [S3:ää](s3.md) käytettäessä muodon on oltava `s3://<bucket_name>`
`TREE_ID` | Yhden puun tilassa (kun `TREE`-asetuksen arvona ei ole `*`) käytettävän sukupuutietokannan hakemiston nimi. Kun tämä on asetettu, palvelin tunnistaa puun hakemistonimen eikä näyttönimen perusteella, mikä kestää nimenmuutoksia paremmin. Vaaditaan, jos haluat nimetä puun uudelleen API:n kautta. Hakemistonimi löytyy kutsulla `GET /api/trees/-` (`id`-kenttä).
`SEARCH_INDEX_DB_URI` | Hakuhakemiston tietokanta-URL-osoite. Taustajärjestelminä sallitaan vain `sqlite` tai `postgresql`. Oletusarvo on `sqlite:///indexdir/search_index.db`, jolloin SQLite-tiedosto luodaan `indexdir`-kansioon suhteessa komentosarjan suorituspolkuun
`SEARCH_INDEX_DIR` | **Vanhentunut** (käytä sen sijaan asetusta `SEARCH_INDEX_DB_URI`). Hakuhakemiston sisältävä hakemisto. Jos tämä on asetettu mutta `SEARCH_INDEX_DB_URI` ei ole, hakuhakemiston URL johdetaan muodossa `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta staattiset tiedostot tarjotaan (esimerkiksi staattinen verkkokäyttöliittymä)
`BASE_URL` | Perus-URL-osoite, josta API on tavoitettavissa (esimerkiksi `https://mygramps.mydomain.com/`). Tätä tarvitaan esimerkiksi oikeiden salasanan palautuslinkkien muodostamiseen. Web Push vaatii myös julkisesti tavoitettavan HTTPS-osoitteen; oletusarvo `http://localhost/` poistaa Web Pushin käytöstä. Kun määrität tämän asetuksen ympäristön kautta, käytä muotoa `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt sallitaan. Oletusarvoisesti kaikki estetään. Käytä arvoa `"*"` salliaksesi pyynnöt mistä tahansa toimialueesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esimerkiksi salasanan palautussähköpostien lähettämiseen)
`EMAIL_PORT` | SMTP-palvelimen portti. Oletusarvo on 465
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana
`EMAIL_USE_TLS` | **Vanhentunut** (käytä sen sijaan asetusta `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Totuusarvo, joka määrittää, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvo on `True`. Kun käytät STARTTLS:ää, aseta tämän arvoksi `False` ja käytä muuta porttia kuin porttia 25.
`EMAIL_USE_SSL` | Totuusarvo, joka määrittää, käytetäänkö SMTP:ssä implisiittistä SSL/TLS:ää (v3.6.0+). Oletusarvo on `True`, jos `EMAIL_USE_TLS`-asetusta ei ole nimenomaisesti asetettu. Käytetään yleensä portin 465 kanssa.
`EMAIL_USE_STARTTLS` | Totuusarvo, joka määrittää, käytetäänkö SMTP:ssä eksplisiittistä STARTTLS:ää (v3.6.0+). Oletusarvo on `False`. Käytetään yleensä portin 587 tai 25 kanssa.
`DEFAULT_FROM_EMAIL` | Automaattisten sähköpostien ”Lähettäjä”-osoite
`THUMBNAIL_CACHE_CONFIG` | Pikkukuvavälimuistin asetukset sisältävä sanakirja. Katso mahdolliset asetukset [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)-dokumentaatiosta.
`REQUEST_CACHE_CONFIG` | Pyyntövälimuistin asetukset sisältävä sanakirja. Katso mahdolliset asetukset [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)-dokumentaatiosta.
`PERSISTENT_CACHE_CONFIG` | Pysyvän välimuistin asetukset sisältävä sanakirja; välimuistia käytetään esimerkiksi telemetriaan. Katso mahdolliset asetukset [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)-dokumentaatiosta.
`CELERY_CONFIG` | Celery-taustatehtäväjonon asetukset. Katso mahdolliset asetukset [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)-dokumentaatiosta.
`REPORT_DIR` | Tilapäinen hakemisto, johon suoritettujen Gramps-raporttien tuloste tallennetaan
`EXPORT_DIR` | Tilapäinen hakemisto, johon Gramps-tietokannan viennin tuloste tallennetaan
`BACKUP_DIR` | Hakemisto, johon [varmuuskopiot](../administration/backups.md) tallennetaan puukohtaiseen alihakemistoon (v3.24.0+). Jos asetusta ei ole määritetty (oletus), varmuuskopioita ei voi tallentaa palvelimelle, mutta ne voidaan edelleen palauttaa ladatusta tiedostosta. Käytä pysyvää sijaintia, esimerkiksi Docker-taltiota, ja mielellään sijaintia, joka itse varmuuskopioidaan tai synkronoidaan muualle.
`BACKUP_KEEP` | Puukohtaisten säilytettävien varmuuskopioiden määrä; vanhemmat poistetaan uuden varmuuskopion luonnin yhteydessä (v3.24.0+). Oletusarvo on `5`
`RATE_LIMIT_BACKUP` | Varmuuskopioiden luonnin nopeusrajoitus puuta kohden (v3.24.0+). Oletusarvo on `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Mediatiedostojen arkistojen luonnin nopeusrajoitus Vienti-sivulla. Oletusarvo on `"1 per hour"`
`REGISTRATION_DISABLED` | Jos arvo on `True`, uusien käyttäjien rekisteröityminen estetään (oletusarvo `False`). Gramps Web API 3.26:sta lähtien kirjautumissivulla piilotetaan tällöin myös rekisteröitymislinkki.
`PROXY_FIX_X_FOR` | Gramps Webin edessä olevien luotettujen käänteisten välityspalvelinten määrä (v3.26.0+). Aseta arvoksi `1`, jos yhden käänteisen välityspalvelimen takana, jotta nopeusrajoitukset koskevat asiakasta eivätkä kaikkia käyttäjiä yhdessä. Oletusarvo on `0`. Aseta tämä vain, jos palvelimeen pääsee yksinomaan näiden välityspalvelinten kautta.
`DISABLE_TELEMETRY` | Jos arvo on `True`, tilastotelemetria poistetaan käytöstä (oletusarvo `False`). Lisätietoja on [telemetriaa](telemetry.md) käsittelevällä sivulla.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa parametrin PIL.Image.MAX_IMAGE_PIXELS, joka ilmaisee käsiteltävän kuvan sisältämien pikselien määrän. Lisätietoja on [dokumentaatiossa](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS).
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa pikkukuvien tiedostokoolle ehdottoman enimmäisarvon. Oletusarvo on `50 * 1024 * 1024` (50 Mt). Arvon suurentaminen voi lisätä muistin käyttöä huomattavasti ja johtaa muistin loppumisesta johtuviin kaatumisiin tai tietojen menetykseen, jos suuria tiedostoja puretaan muistiin.


!!! info
    Kun käytät ympäristömuuttujia määrityksiin, totuusarvoisten asetusten, kuten `EMAIL_USE_SSL`, arvon on oltava merkkijono `true` tai `false` (kirjainkoko on merkitsevä!).


### PostgreSQL-tietokantojen asetukset

Nämä asetukset vaaditaan, jos sukupuusi sijaitsevat [PostgreSQL-tietokannassa](postgres.md), jossa käytetään SharedPostgreSQL-lisäosaa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Tietokantayhteyden käyttäjänimi
`POSTGRES_PASSWORD` | Tietokannan käyttäjän salasana


### Useiden puiden isännöintiin liittyvät asetukset

Seuraavat asetukset liittyvät tilanteeseen, jossa [isännöit useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Totuusarvo, joka määrittää, käytetäänkö kunkin puun mediatiedostoille erillistä alikansiota. Oletusarvo on `False`, mutta usean puun asetuksessa on erittäin suositeltavaa käyttää arvoa `True`
`NEW_DB_BACKEND` | Uusille sukupuille käytettävä tietokantataustajärjestelmä. Arvon on oltava joko `sqlite` tai `sharedpostgresql`. Oletusarvo on `sqlite`. Arvo `postgresql` hyväksytään edelleen, mutta se on vanhentunut, koska PostgreSQL-taustajärjestelmä poistetaan Gramps Web API 4.0:ssa.
`POSTGRES_HOST` | Uusien puiden luomiseen käytettävän PostgreSQL-palvelimen isäntänimi, kun käytössä on usean puun asetus ja SharedPostgreSQL-taustajärjestelmä
`POSTGRES_PORT` | Uusien puiden luomiseen käytettävän PostgreSQL-palvelimen portti, kun käytössä on usean puun asetus ja SharedPostgreSQL-taustajärjestelmä


### OIDC-todennuksen asetukset

Näitä asetuksia tarvitaan, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten palveluntarjoajien kanssa. Katso yksityiskohtaiset asennusohjeet ja esimerkit sivulta [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Totuusarvo, joka määrittää, otetaanko OIDC-todennus käyttöön. Oletusarvo on `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjän URL-osoite (mukautettuja OIDC-palveluntarjoajia varten)
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (mukautettuja OIDC-palveluntarjoajia varten)
`OIDC_CLIENT_SECRET` | OAuth-asiakassalaisuus (mukautettuja OIDC-palveluntarjoajia varten)
`OIDC_NAME` | Palveluntarjoajan mukautettu näyttönimi. Oletusarvo on ”OIDC”
`OIDC_SCOPES` | OAuth-laajuudet. Oletusarvo on ”openid email profile”
`OIDC_USERNAME_CLAIM` | Käyttäjänimeen käytettävä claim. Oletusarvo on ”preferred_username”
`OIDC_OPENID_CONFIG_URL` | Valinnainen: OpenID Connect -määrityksen päätepisteen URL-osoite (jos vakiomuotoista `/.well-known/openid-configuration`-osoitetta ei käytetä)
`OIDC_PKCE` | Totuusarvo, joka määrittää, käytetäänkö PKCE:tä. Jos arvoa ei ole asetettu, PKCE:tä käytetään, kun palveluntarjoajan discovery-asiakirja luettelee `S256`:n. Katso [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Totuusarvo, joka määrittää, poistetaanko paikallinen käyttäjänimi-/salasanatodennus käytöstä. Oletusarvo on `False`
`OIDC_AUTO_REDIRECT` | Totuusarvo, joka määrittää, ohjataanko käyttäjä automaattisesti OIDC:hen, kun vain yksi palveluntarjoaja on määritetty. Oletusarvo on `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Luettelo `https`-URI-osoitteista, joissa natiivisovellukset voivat vastaanottaa kirjautumistuloksen (v3.26.0+); asetetaan ympäristömuuttujassa JSON-luettelona. Oletusarvoisesti tyhjä. Tarvitaan vain, jos natiivisovelluksen dokumentaatio pyytää sitä. Katso [natiivisovellukset](oidc.md#native-apps)

#### Sisäänrakennetut OIDC-palveluntarjoajat

Käytä sisäänrakennettuja palveluntarjoajia (Google, Microsoft) varten seuraavia asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth -asiakastunnus
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth -asiakassalaisuus
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth -asiakastunnus
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth -asiakassalaisuus
`OIDC_GOOGLE_PKCE` | Googlen PKCE-asetus, katso [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Microsoftin PKCE-asetus, katso [PKCE](oidc.md#pkce)

#### OIDC-roolien yhdistäminen

Näiden asetusten avulla voit yhdistää tunnistetietopalveluntarjoajasi OIDC-ryhmät/roolit Gramps Webin käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | OIDC-tunnisteessa olevan käyttäjän ryhmät/roolit sisältävän claimin nimi. Oletusarvo on ”groups”
`OIDC_GROUP_ADMIN` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Admin”-rooliin
`OIDC_GROUP_OWNER` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Owner”-rooliin
`OIDC_GROUP_EDITOR` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Editor”-rooliin
`OIDC_GROUP_CONTRIBUTOR` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Contributor”-rooliin
`OIDC_GROUP_MEMBER` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Member”-rooliin
`OIDC_GROUP_GUEST` | OIDC-palveluntarjoajan ryhmän/roolin nimi, joka yhdistetään Grampsin ”Guest”-rooliin

### Vain tekoälyominaisuuksiin liittyvät asetukset

Näitä asetuksia tarvitaan, jos haluat käyttää tekoälykeskustelua. Lisätietoja on sivulla [Tekoälykeskustelun määrittäminen](chat.md).

!!! note
    Semanttisen haun asetukset `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ja `VECTOR_EMBEDDING_API_KEY` ohitetaan Gramps Web API 3.25:stä lähtien, koska semanttinen haku poistettiin. Tekoälykeskustelu tarvitsee vain asetuksen `LLM_MODEL`.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | OpenAI-yhteensopivan keskustelu-API:n perus-URL-osoite. Oletusarvo on `None`, jolloin käytetään OpenAI API:a.
`LLM_MODEL` | OpenAI-yhteensopivalle keskustelu-API:lle käytettävä malli. Jos arvoa ei ole asetettu (oletus), keskustelu poistetaan käytöstä. Versiosta v3.6.0 lähtien tekoälyavustaja käyttää Pydantic AI:ta, joka tukee työkalukutsuja.
`LLM_MAX_OUTPUT_TOKENS` | Suurin tokenien määrä, jonka malli voi tuottaa yhdessä vastauksessa. Oletusarvoisesti asetusta ei ole määritetty, jolloin rajoitus jää mallipalvelimen päätettäväksi. Hyödyllinen mallipalvelimille, joilla ei ole omaa rajoitusta ja joiden vastaus voisi muuten jatkua loputtomasti.
`LLM_MAX_CONTEXT_LENGTH` | LLM:lle annettavan sukupuun kontekstin merkkiraja. Oletusarvo on 50000.
`LLM_SYSTEM_PROMPT` | LLM-keskusteluavustajan mukautettu järjestelmäkehote (v3.6.0+). Jos arvoa ei ole asetettu, käytetään sukututkimukseen optimoitua oletuskehotetta.
`LLM_VISION` | Totuusarvo, joka määrittää, voivatko käyttäjät liittää kuvia kysymyksiinsä (v3.26.0+). Ota tämä käyttöön vain, jos malli hyväksyy kuvia. Oletusarvo on `False`. Katso [Kuvat kysymyksissä](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Totuusarvo, joka määrittää, voiko avustaja ehdottaa puuhun muutoksia käyttäjien tarkistettaviksi ja sovellettaviksi (v3.26.0+). Oletusarvo on `False`. Katso [Avustajan salliminen ehdottaa muutoksia](chat.md#letting-the-assistant-propose-changes)


## Esimerkkimääritystiedosto

Tuotantokäyttöön tarkoitettu vähimmäismääritystiedosto voisi näyttää tältä:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avaimesi
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portille 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasanasi
DEFAULT_FROM_EMAIL="gramps@example.com"
```
