# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittava konfigurointi voidaan tehdä selaimesta. Käyttöympäristöstä riippuen voi kuitenkin olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseen ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfigurointitiedosto vs. ympäristömuuttujat

Asetusten osalta voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimesi tiedostojärjestelmässä (oikealla puolella viitataan polkuun kontissa, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- etuliite jokaiselle asetuksen nimelle on `GRAMPSWEB_`, jotta saat ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot ovat etusijalla konfigurointitiedostossa oleviin verrattuna. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

!!! warning "Etuliitteettömät ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä joukko asetuksia – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujan kautta *ilman* `GRAMPSWEB_` etuliitettä. Tämä on vanhentunut, lokittaa varoituksen käynnistyksessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esim. `GRAMPSWEB_TREE` sen sijaan, että käyttäisit `TREE`.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Konfigurointitiedostossa asetusten nimet käytetään aina ilman etuliitettä.

!!! tip "Vanhojen vaihtoehtojen tarkistaminen"
    Vanhoja konfigurointivaihtoehtoja, joista palvelimesi edelleen riippuu – kuten etuliitteettömät ympäristömuuttujat, `SEARCH_INDEX_DIR` tai `EMAIL_USE_TLS` – lokitetaan varoituksina käynnistyksessä. Gramps Web API 3.22:sta alkaen ne myös luetellaan, yhdessä niiden korvausten ja version kanssa, jolloin tuki poistetaan, **Järjestelmän tiedot** -sivun yläosassa (johon pääsee käyttäjäkuvakkeen kautta sovelluksen ylävalikossa), kun olet kirjautuneena sisään järjestelmänvalvojana.

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuun tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta tällä nimellä ei ole, uusi tyhjää puuta luodaan.
`SECRET_KEY` | Flaskin salainen avain. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki pääsytunnukset.
`USER_DB_URI` | Käyttäjä tietokannan URL-osoite. Mikä tahansa SQLAlchemyn kanssa yhteensopiva URL-osoite on sallittu.

!!! info
    Voit luoda turvallisen salaisen avaimen esim. komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Polku, jota käytetään media-tiedostojen peruskansiona, ohittaen Grampsissa asetetun media-peruskansion. Kun käytetään [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `*`). Kun asetettu, palvelin tunnistaa puun hakemiston nimen perusteella sen näyttönimen sijaan, mikä on kestävämpää uudelleennimeämisille. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimen voi löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Hakemiston tietokannan URL-osoite. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvoisesti `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston kansioon `indexdir`, suhteessa polkuun, josta skripti ajetaan.
`SEARCH_INDEX_DIR` | **Vanhentunut** (käytä sen sijaan `SEARCH_INDEX_DB_URI`). Hakemisto, joka sisältää hakemiston. Jos asetettu, kun `SEARCH_INDEX_DB_URI` on asetettu, hakemiston URL-osoite johdetaan muodosta `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta palvellaan staattisia tiedostoja (esim. staattinen verkkosivuston etupää).
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan palautuslinkkien rakentamiseksi.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki ovat kiellettyjä. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan palautus-sähköpostien lähettämiseen).
`EMAIL_PORT` | SMTP-palvelimen portti. Oletusarvoisesti 465.
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi.
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana.
`EMAIL_USE_TLS` | **Vanhentunut** (käytä sen sijaan `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvoisesti `True`. Kun käytetään STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `True`, jos `EMAIL_USE_TLS` ei ole nimenomaisesti asetettu. Käytetään tyypillisesti portilla 465.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:ssä (v3.6.0+). Oletusarvoisesti `False`. Käytetään tyypillisesti portilla 587 tai 25.
`DEFAULT_FROM_EMAIL` | "Lähettäjä" osoite automaattisille sähköposteille.
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvien välimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriassa. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan.
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan.
`REGISTRATION_DISABLED` | Jos `True`, estä uusien käyttäjien rekisteröinti (oletusarvo `False`).
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastotelemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS-parametrin, joka osoittaa, kuinka monta pikseliä käsitellyssä kuvassa voi olla. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovaksi maksimi tiedostokooksi pikkukuville. Oletusarvoisesti `50 * 1024 * 1024` (50 MB). Sen nostaminen voi huomattavasti lisätä muistin käyttöä ja voi johtaa muistivaurioihin tai tietojen menetykseen, jos suuria tiedostoja purkautuu muistiin.


!!! info
    Kun käytetään ympäristömuuttujia konfiguroinnissa, boolean-vaihtoehtojen kuten `EMAIL_USE_SSL` on oltava joko merkkijono `true` tai `false` (kirjainten koko on tärkeä!).


### Asetukset vain PostgreSQL-taustatietokannalle

Tämä on tarpeen, jos olet konfiguroinut Gramps-tietokannan toimimaan [PostgreSQL-lisäosan](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) kanssa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Käyttäjänimi tietokantayhteydelle.
`POSTGRES_PASSWORD` | Salasana tietokannan käyttäjälle.


### Asetukset, jotka liittyvät useiden puiden isännöimiseen

Seuraavat asetukset ovat merkityksellisiä, kun [isännöidään useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media-tiedostoille. Oletusarvoisesti `False`, mutta suositellaan vahvasti käytettäväksi `True` monipuu-asetuksessa.
`NEW_DB_BACKEND` | Tietokantatausta, jota käytetään uusille sukupuulle. Sen on oltava yksi seuraavista: `sqlite`, `postgresql` tai `sharedpostgresql`. Oletusarvoisesti `sqlite`.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään monipuu-asetusta SharedPostgreSQL-taustalla.
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään monipuu-asetusta SharedPostgreSQL-taustalla.


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, onko OIDC-todennus käytössä. Oletusarvoisesti `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjä-URL (muille OIDC-palveluntarjoajille).
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (muille OIDC-palveluntarjoajille).
`OIDC_CLIENT_SECRET` | OAuth-asiakassalaisuus (muille OIDC-palveluntarjoajille).
`OIDC_NAME` | Mukautettu näyttönimi palveluntarjoajalle. Oletusarvoisesti "OIDC".
`OIDC_SCOPES` | OAuth-alueet. Oletusarvoisesti "openid email profile".
`OIDC_USERNAME_CLAIM` | Vaatimus, jota käytetään käyttäjänimen määrittämiseen. Oletusarvoisesti "preferred_username".
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä vakiota `/.well-known/openid-configuration`).
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, onko paikallinen käyttäjänimi/salasana-todennus poistettu käytöstä. Oletusarvoisesti `False`.
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi palveluntarjoaja on määritetty. Oletusarvoisesti `False`.

#### Sisäänrakennetut OIDC-palveluntarjoajat

Sisäänrakennettuja palveluntarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle.
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalaisuus Google OAuth:lle.
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle.
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalaisuus Microsoft OAuth:lle.

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoittamisen identiteettipalveluntarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Vaatimuksen nimi OIDC-tunnuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvoisesti "groups".
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Admin" -roolia.
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Owner" -roolia.
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Editor" -roolia.
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Contributor" -roolia.
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Member" -roolia.
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Guest" -roolia.

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää tekoälypohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvoisesti `None`, mikä käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei asetettu (oletusarvo), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-avustaja käyttää Pydantic AI:ta työkalukutsumahdollisuuksilla.
`VECTOR_EMBEDDING_MODEL` | Malli, jota käytetään semanttisten hakujen vektoriupotuksiin. Kun käytetään paikallista mallia, tämän on oltava [Sentence Transformers](https://sbert.net/) -mallin nimi. Kun käytetään etä-API:a (katso `VECTOR_EMBEDDING_BASE_URL`), tämä on mallin nimi, joka välitetään etäpalveluntarjoajalle. Jos ei asetettu (oletusarvo), semanttinen haku ja keskustelu ovat pois käytöstä.
`VECTOR_EMBEDDING_BASE_URL` | Perus-URL etä-OpenAI-yhteensopivalle upotus-API:lle (esim. Ollama, OpenAI, LiteLLM). Jos ei asetettu (oletusarvo), käytetään paikallista Sentence Transformers -mallia. Katso [Etä-upotus-API:n käyttö](chat.md#using-a-remote-embedding-api) lisätietoja varten.
`VECTOR_EMBEDDING_API_KEY` | API-avain todennetuille etä-upotuspalveluntarjoajille. Tarvitaan vain, kun `VECTOR_EMBEDDING_BASE_URL` on asetettu ja palveluntarjoaja vaatii todennusta.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvoisesti 50000.
`LLM_SYSTEM_PROMPT` | Mukautettu järjestelmäkehotus LLM-keskusteluavustajalle (v3.6.0+). Jos ei asetettu, käytetään oletusarvoista sukututkimusoptimoitua kehotusta.


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
