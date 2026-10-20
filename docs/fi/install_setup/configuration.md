# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittavat asetukset voidaan tehdä selaimesta. Kuitenkin käyttöönotosta riippuen voi olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseen ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfigurointitiedosto vs. ympäristömuuttujat

Asetuksille voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimen tiedostojärjestelmässä (oikealla puolella viitataan polkuun säiliössä, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen nimeen etuliite `GRAMPSWEB_` saadaksesi ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot menevät edelle konfigurointitiedostossa olevista. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

!!! warning "Ilman etuliitettä olevat ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä joukko asetuksia – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujan kautta *ilman* `GRAMPSWEB_` etuliitettä. Tämä on vanhentunutta, lokittaa varoituksen käynnistyksessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esim. `GRAMPSWEB_TREE` sen sijaan, että käyttäisit `TREE`.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Konfigurointitiedostossa asetusten nimet käytetään aina ilman etuliitettä.

!!! tip "Vanhentuneiden vaihtoehtojen tarkistaminen"
    Vanhentuneet konfigurointivaihtoehdot, joista palvelimesi edelleen riippuu – kuten ilman etuliitettä olevat ympäristömuuttujat, `SEARCH_INDEX_DIR` tai `EMAIL_USE_TLS` – lokitetaan varoituksina käynnistyksessä. Gramps Web API 3.22:sta alkaen ne myös listataan, yhdessä niiden korvausten ja version kanssa, jolloin tuki poistetaan, **Järjestelmätiedot** -sivun yläosassa (johon pääsee käyttäjäkuvakkeesta ylävalikossa), kun olet kirjautuneena sisään järjestelmänvalvojana.

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuuyhteyden tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta, jolla on tämä nimi, ei ole, luodaan uusi tyhjää puuta.
`SECRET_KEY` | Salainen avain Flaskille. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki käyttöoikeustunnukset.
`USER_DB_URI` | Käyttäjä tietokannan URL-osoite. Mikä tahansa SQLAlchemy-yhteensopiva URL-osoite on sallittu.

!!! info
    Voit luoda turvallisen salaisen avaimen esim. komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Polku, jota käytetään media-tiedostojen peruskansiona, ohittaen Grampsissa asetetun media-peruskansion. Käytettäessä [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `*`). Kun se on asetettu, palvelin tunnistaa puun sen hakemiston nimen perusteella eikä sen näyttönimen perusteella, mikä on kestävämpää uudelleennimeämisille. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimen voi löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Hakemiston URL-osoite. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvoisesti `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston kansioon `indexdir`, suhteessa polkuun, josta skripti ajetaan.
`SEARCH_INDEX_DIR` | **Vanhentunut** (käytä `SEARCH_INDEX_DB_URI` sen sijaan). Hakemisto, joka sisältää hakemiston. Jos se on asetettu, kun `SEARCH_INDEX_DB_URI` on asettamatta, hakemiston URL-osoite johdetaan muodosta `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta tarjoillaan staattisia tiedostoja (esim. staattinen verkkosivuston etuosa)
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan nollauslinkkien rakentamiseksi. Web Push vaatii myös julkisesti saavutettavan HTTPS-URL-osoitteen; oletusarvoinen `http://localhost/` poistaa käytöstä Web Pushin. Kun määrität tämän asetuksen ympäristön kautta, käytä `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki on estetty. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan nollaus-sähköpostien lähettämiseen)
`EMAIL_PORT` | SMTP-palvelimen portti. Oletusarvoisesti 465
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana
`EMAIL_USE_TLS` | **Vanhentunut** (käytä `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS` sen sijaan). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvoisesti `True`. Käytettäessä STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `True`, jos `EMAIL_USE_TLS` ei ole nimenomaan asetettu. Käytetään tyypillisesti portilla 465.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `False`. Käytetään tyypillisesti portilla 587 tai 25.
`DEFAULT_FROM_EMAIL` | "Lähettäjä" osoite automatisoiduille sähköposteille
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvien välimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriassa. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan
`BACKUP_DIR` | Hakemisto, johon [varmuuskopiot](../administration/settings.md#backups) tallennetaan, jokaiselle puulle oma alihakemisto (v3.24.0+). Jos ei ole asetettu (oletusarvo), varmuuskopioita ei voida tallentaa palvelimelle, mutta ne voidaan silti palauttaa ladatusta tiedostosta. Käytä pysyvää sijaintia, esim. Docker-tilavuutta, ja mieluiten sellaista, joka varmuuskopioidaan tai synkronoidaan muualle.
`BACKUP_KEEP` | Tallennettujen varmuuskopioiden määrä per puu; vanhemmat poistetaan, kun uusi varmuuskopio luodaan (v3.24.0+). Oletusarvoisesti `5`
`RATE_LIMIT_BACKUP` | Varmuuskopioiden luomisen nopeusrajoitus, per puu (v3.24.0+). Oletusarvoisesti `"10 päivässä"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Media-arkistojen luomisen nopeusrajoitus Vienti-sivulla. Oletusarvoisesti `"1 tunnissa"`
`REGISTRATION_DISABLED` | Jos `True`, estä uusi käyttäjärekisteröinti (oletusarvo `False`)
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastollinen telemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS -parametrin, joka osoittaa, kuinka monta pikseliä käsitellyssä kuvassa voi olla. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovaksi maksimi tiedostokoon pikkukuville. Oletusarvoisesti `50 * 1024 * 1024` (50 MB). Sen nostaminen voi suuresti lisätä muistinkäyttöä ja voi johtaa muistivaroja loppumaan tai tietojen menetykseen, jos suuria tiedostoja purkautuu muistiin.


!!! info
    Kun käytät ympäristömuuttujia konfiguroinnissa, boolean-asetusten, kuten `EMAIL_USE_SSL`, on oltava joko merkkijono `true` tai `false` (kokoherkkä!).


### Asetukset PostgreSQL-tietokannoille

Nämä asetukset ovat pakollisia, jos sukupuutasi isännöidään [PostgreSQL-tietokannassa](postgres.md) käyttäen SharedPostgreSQL-lisäosaa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Tietokantayhteyden käyttäjänimi
`POSTGRES_PASSWORD` | Tietokannan käyttäjän salasana


### Asetukset, jotka liittyvät useiden puiden isännöintiin

Seuraavat asetukset ovat tärkeitä, kun [isännöidään useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media-tiedostoille. Oletusarvoisesti `False`, mutta suositellaan vahvasti käytettäväksi `True` usean puun asetuksessa
`NEW_DB_BACKEND` | Tietokannan taustajärjestelmä, jota käytetään uusille sukupuulle. Sen on oltava joko `sqlite` tai `sharedpostgresql`. Oletusarvoisesti `sqlite`. Arvo `postgresql` on edelleen hyväksyttävä, mutta vanhentunut, koska PostgreSQL-taustajärjestelmä poistetaan Gramps Web API 4.0:ssä.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, käytetäänkö OIDC-todennusta. Oletusarvoisesti `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjä-URL (muille OIDC-palveluntarjoajille)
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (muille OIDC-palveluntarjoajille)
`OIDC_CLIENT_SECRET` | OAuth-asiakassalasana (muille OIDC-palveluntarjoajille)
`OIDC_NAME` | Mukautettu näyttönimi tarjoajalle. Oletusarvoisesti "OIDC"
`OIDC_SCOPES` | OAuth-alueet. Oletusarvoisesti "openid email profile"
`OIDC_USERNAME_CLAIM` | Väite, jota käytetään käyttäjänimenä. Oletusarvoisesti "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`)
`OIDC_PKCE` | Boolean, käytetäänkö PKCE:tä. Jos ei ole asetettu, PKCE:tä käytetään, kun tarjoajan löytödokumentissa on lueteltu `S256`. Katso [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, käytetäänkö paikallista käyttäjänimi/salasana-todennusta. Oletusarvoisesti `False`
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi tarjoaja on määritetty. Oletusarvoisesti `False`

#### Sisäänrakennetut OIDC-palveluntarjoajat

Sisäänrakennettuja tarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalasana Google OAuth:lle
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalasana Microsoft OAuth:lle
`OIDC_GOOGLE_PKCE` | Boolean, PKCE-asetus Googlelle, katso [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolean, PKCE-asetus Microsoftille, katso [PKCE](oidc.md#pkce)

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoittamisen identiteettipalveluntarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Väitteen nimi OIDC-tunnuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvoisesti "groups"
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Admin"-roolia
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Owner"-roolia
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Editor"-roolia
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Contributor"-roolia
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Member"-roolia
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Guest"-roolia

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää AI-pohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua. Katso [AI-keskustelun asettaminen](chat.md) lisätietoja varten.

!!! warning "Semanttinen haku on vanhentunut"
    Semanttinen haku, ja sen mukana `VECTOR_EMBEDDING_*` -asetukset, on vanhentunut ja poistetaan Gramps Web API 3.25:ssä. Tämän jälkeen `VECTOR_EMBEDDING_MODEL` hyväksytään edelleen, mutta sitä ei käytetä. Gramps Web API 3.24:stä alkaen AI-keskustelu tarvitsee vain `LLM_MODEL`.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvoisesti `None`, joka käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei ole asetettu (oletusarvo), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-avustaja käyttää Pydantic AI:ta työkalukutsukyvykkyyksillä.
`VECTOR_EMBEDDING_MODEL` | **Vanhentunut**, poistetaan 3.25:ssä. Malli, jota käytetään semanttisen haun vektoriupotuksille. Käytettäessä paikallista mallia, tämän on oltava [Sentence Transformers](https://sbert.net/) -mallin nimi. Käytettäessä etä-API:a (katso `VECTOR_EMBEDDING_BASE_URL`), tämä on mallin nimi, joka välitetään etäpalveluntarjoajalle. Jos ei ole asetettu (oletusarvo), semanttinen haku on pois käytöstä. Ennen Gramps Web API 3.24:ää keskustelu oli myös pois käytöstä.
`VECTOR_EMBEDDING_BASE_URL` | **Vanhentunut**, poistetaan 3.25:ssä. Perus-URL etä OpenAI-yhteensopivalle upotustyökalulle (esim. Ollama, OpenAI, LiteLLM). Jos ei ole asetettu (oletusarvo), käytetään paikallista Sentence Transformers -mallia. Katso [Etäupotustyökalun käyttö](chat.md#using-a-remote-embedding-api) lisätietoja varten.
`VECTOR_EMBEDDING_API_KEY` | **Vanhentunut**, poistetaan 3.25:ssä. API-avain todennetuille etäupotustarjoajille. Tarvitaan vain, kun `VECTOR_EMBEDDING_BASE_URL` on asetettu ja tarjoaja vaatii todennusta.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvoisesti 50000.
`LLM_SYSTEM_PROMPT` | Mukautettu järjestelmäkehotus LLM-keskusteluavustajalle (v3.6.0+). Jos ei ole asetettu, käytetään oletusarvoista sukututkimukseen optimoitua kehotusta.


## Esimerkkikonfigurointitiedosto

Minimalistinen konfigurointitiedosto tuotantokäyttöön voisi näyttää tältä:
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
