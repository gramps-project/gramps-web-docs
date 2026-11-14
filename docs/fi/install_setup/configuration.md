# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittavat asetukset voidaan tehdä selaimesta. Kuitenkin, riippuen käyttöönotosta, voi olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseksi ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfigurointitiedosto vs. ympäristömuuttujat

Asetuksille voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkossa:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimen tiedostojärjestelmässä (oikealla puolella viitataan polkuun säilössä, eikä sitä saa muuttaa).

Ympäristömuuttujia käytettäessä,

- etuliite jokaisen asetuksen nimen edessä on `GRAMPSWEB_`, jotta saadaan ympäristömuuttujan nimi
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot ovat etusijalla konfigurointitiedostossa oleviin verrattuna. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

!!! warning "Ilman etuliitettä olevat ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä johtuen joukko asetuksia – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujan kautta *ilman* `GRAMPSWEB_` etuliitettä. Tämä on vanhentunutta, lokittaa varoituksen käynnistyksessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esim. `GRAMPSWEB_TREE` sen sijaan, että käyttäisit `TREE`.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Konfigurointitiedostossa asetusten nimiä käytetään aina ilman etuliitettä.

!!! tip "Vanhenneiden vaihtoehtojen tarkistaminen"
    Vanhenneita konfigurointivaihtoehtoja, joista palvelimesi edelleen riippuu – kuten ilman etuliitettä olevat ympäristömuuttujat, `SEARCH_INDEX_DIR` tai `EMAIL_USE_TLS` – lokitetaan varoituksina käynnistyksessä. Gramps Web API 3.22:sta lähtien ne myös listataan, yhdessä niiden korvausten ja version kanssa, jolloin tuki poistetaan, **Järjestelmätiedot** -sivun yläosassa (johon pääsee kirjautumalla sisään ylläpitäjänä käyttäjäkuvakkeesta).

    Sähköpostiasetukset ja perus-URL, jotka vanhempien versioiden ensimmäisen käynnistyksen ohjain tallensi tietokantaan, luetellaan siellä myös. Aseta ne konfigurointiisi tallennettuihin arvoihin; varoitus katoaa, kun ne vastaavat.

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuun tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta, jonka nimi on tämä, ei ole olemassa, uusi tyhjää puuta luodaan.
`SECRET_KEY` | Salainen avain flaskille. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki käyttöoikeustunnukset.
`USER_DB_URI` | Käyttäjä tietokannan URL-osoite. Mikä tahansa SQLAlchemyn kanssa yhteensopiva URL-osoite on sallittu.

!!! info
    Voit luoda turvallisen salaisen avaimen esim. komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Polku, jota käytetään media tiedostojen peruskansiona, joka ohittaa Grampsissa asetetun media peruskansion. Käytettäessä [S3:tä](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `*`). Kun se on asetettu, palvelin tunnistaa puun sen hakemiston nimen perusteella eikä sen näyttönimen, mikä on kestävämpää uudelleennimeämisille. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimi voidaan löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Tietokannan URL-osoite hakemistoa varten. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvoisesti `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston `indexdir`-kansioon suhteessa polkuun, jossa skripti suoritetaan.
`SEARCH_INDEX_DIR` | **Vanhenneita** (käytä sen sijaan `SEARCH_INDEX_DB_URI`). Hakemisto, joka sisältää hakemiston. Jos se on asetettu, kun `SEARCH_INDEX_DB_URI` on asettamatta, hakemiston URL-osoite johdetaan muodosta `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta staattisia tiedostoja tarjotaan (esim. staattinen verkkosivusto)
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan nollauslinkkien rakentamiseksi. Web Push vaatii myös julkisesti saavutettavan HTTPS-URL-osoitteen; oletusarvoinen `http://localhost/` estää Web Pushin. Kun määrität tämän asetuksen ympäristön kautta, käytä `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki on estetty. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan nollaus sähköpostien lähettämiseen)
`EMAIL_PORT` | SMTP-palvelimen portti. oletusarvoisesti 465
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana
`EMAIL_USE_TLS` | **Vanhenneita** (käytä sen sijaan `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvoisesti `True`. Käytettäessä STARTTLS:ää, aseta tämä `False` ja käytä muuta porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `True`, jos `EMAIL_USE_TLS` ei ole nimenomaisesti asetettu. Käytetään tyypillisesti portilla 465.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `False`. Käytetään tyypillisesti portilla 587 tai 25.
`DEFAULT_FROM_EMAIL` | "Lähettäjä" osoite automatisoiduille sähköposteille
`THUMBNAIL_CACHE_CONFIG` | Sanakirja thumbnail-välimuistin asetuksille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja pyyntövälimuistin asetuksille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja pysyvän välimuistin asetuksille, joita käytetään esim. telemetriassa. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan
`BACKUP_DIR` | Hakemisto, johon [varmuuskopiot](../administration/backups.md) tallennetaan, jokaiselle puulle oma alihakemisto (v3.24.0+). Jos ei ole asetettu (oletusarvo), varmuuskopioita ei voida tallentaa palvelimelle, mutta ne voidaan silti palauttaa ladatusta tiedostosta. Käytä pysyvää sijaintia, esim. Docker-tilavuutta, ja mieluiten sellaista, joka varmuuskopioidaan tai synkronoidaan muualle.
`BACKUP_KEEP` | Tallennettujen varmuuskopioiden määrä per puu; vanhemmat poistetaan, kun uusi varmuuskopio luodaan (v3.24.0+). Oletusarvoisesti `5`
`RATE_LIMIT_BACKUP` | Varmuuskopioiden luomisen nopeusrajoitus, per puu (v3.24.0+). Oletusarvoisesti `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Media-arkistojen luomisen nopeusrajoitus Vienti-sivulla. Oletusarvoisesti `"1 per hour"`
`REGISTRATION_DISABLED` | Jos `True`, estä uusien käyttäjien rekisteröinti (oletusarvo `False`)
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastollinen telemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS -parametrin, joka osoittaa, kuinka monta pikseliä käsitellyssä kuvassa voi olla. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovaksi maksimi tiedostokooksi thumbnail-kuville. Oletusarvoisesti `50 * 1024 * 1024` (50 MB). Sen nostaminen voi suuresti lisätä muistinkäyttöä ja voi johtaa muistivaurioihin tai tietojen menetykseen, jos suuria tiedostoja puristetaan muistiin.


!!! info
    Kun käytät ympäristömuuttujia konfiguroinnissa, boolean-asetusten, kuten `EMAIL_USE_SSL`, on oltava joko merkkijono `true` tai `false` (isolla ja pienellä kirjaimella!).


### Asetukset PostgreSQL-tietokantoja varten

Nämä asetukset ovat pakollisia, jos sukupuusi isännöidään [PostgreSQL-tietokannassa](postgres.md), joka käyttää SharedPostgreSQL-lisäosaa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Käyttäjänimi tietokantayhteydelle
`POSTGRES_PASSWORD` | Salasana tietokannan käyttäjälle


### Asetukset, jotka liittyvät useiden puiden isännöimiseen

Seuraavat asetukset ovat tärkeitä, kun [isännöidään useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media tiedostoille. Oletusarvoisesti `False`, mutta suositellaan vahvasti käyttämään `True` usean puun asetuksessa
`NEW_DB_BACKEND` | Tietokannan taustajärjestelmä, jota käytetään uusille sukupuulle. Sen on oltava yksi `sqlite` tai `sharedpostgresql`. Oletusarvoisesti `sqlite`. Arvo `postgresql` hyväksytään edelleen, mutta se on vanhentunut, koska PostgreSQL-taustajärjestelmä poistetaan Gramps Web API 4.0:ssa.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, otetaanko OIDC-todennus käyttöön. Oletusarvoisesti `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjä-URL (mikäli käytetään mukautettuja OIDC-palveluntarjoajia)
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (mikäli käytetään mukautettuja OIDC-palveluntarjoajia)
`OIDC_CLIENT_SECRET` | OAuth-asiakassalasana (mikäli käytetään mukautettuja OIDC-palveluntarjoajia)
`OIDC_NAME` | Mukautettu näyttönimi palveluntarjoajalle. Oletusarvoisesti "OIDC"
`OIDC_SCOPES` | OAuth-alueet. Oletusarvoisesti "openid email profile"
`OIDC_USERNAME_CLAIM` | Vaatimus, jota käytetään käyttäjänimenä. Oletusarvoisesti "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`)
`OIDC_PKCE` | Boolean, käytetäänkö PKCE:tä. Jos ei ole asetettu, PKCE:tä käytetään, kun tarjoajan löytöasiakirja listaa `S256`. Katso [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, estetäänkö paikallinen käyttäjänimi/salasana-todennus. Oletusarvoisesti `False`
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi palveluntarjoaja on määritetty. Oletusarvoisesti `False`

#### Sisäänrakennetut OIDC-palveluntarjoajat

Sisäänrakennettuja palveluntarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalasana Google OAuth:lle
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalasana Microsoft OAuth:lle
`OIDC_GOOGLE_PKCE` | Boolean, PKCE-asetus Googlelle, katso [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolean, PKCE-asetus Microsoftille, katso [PKCE](oidc.md#pkce)

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoituksen identiteettipalveluntarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Vaatimuksen nimi OIDC-tunnuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvoisesti "groups"
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Ylläpitäjä" -roolia
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Omistaja" -roolia
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Toimittaja" -roolia
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Avustaja" -roolia
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Jäsen" -roolia
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Vieras" -roolia

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää AI-keskustelua. Katso [AI-keskustelun määrittäminen](chat.md) lisätietoja varten.

!!! note
    `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ja `VECTOR_EMBEDDING_API_KEY` -asetuksia semanttista hakua varten ei oteta huomioon Gramps Web API 3.25:stä alkaen, joka poisti semanttisen haun. AI-keskustelu tarvitsee vain `LLM_MODEL`.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvoisesti `None`, mikä käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei ole asetettu (oletusarvo), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-assistentti käyttää Pydantic AI:ta työkalukutsukyvykkyyksillä.
`LLM_MAX_OUTPUT_TOKENS` | Suurin määrä tokeneita, joita malli voi tuottaa yhdessä vastauksessa. Oletusarvoisesti ei asetettu, jolloin raja on mallipalvelimella. Hyödyllinen mallipalvelimille, joilla ei ole omaa rajaa, jolloin vastaus voisi muuten jatkua loputtomiin.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvoisesti 50000.
`LLM_SYSTEM_PROMPT` | Mukautettu järjestelmäkehotus LLM-keskusteluassistentille (v3.6.0+). Jos ei ole asetettu, käytetään oletusarvoista sukututkimusoptimoitua kehotusta.


## Esimerkkikonfigurointitiedosto

Minimalistinen konfigurointitiedosto tuotantoa varten voisi näyttää tältä:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portilla 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
