# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittavat asetukset voidaan tehdä selaimesta. Käyttöympäristöstä riippuen voi kuitenkin olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseen ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfigurointitiedosto vs. ympäristömuuttujat

Asetusten osalta voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimesi tiedostojärjestelmässä (oikealla puolella viitataan polkuun säiliössä, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen nimen eteen `GRAMPSWEB_` saadaksesi ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot ovat etusijalla konfigurointitiedostossa oleviin verrattuna. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

!!! warning "Ilman etuliitettä olevat ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä muutamia asetuksia – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujan *ilman* `GRAMPSWEB_` etuliitettä. Tämä on vanhentunut, lokittaa varoituksen käynnistyksessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esim. `GRAMPSWEB_TREE` sen sijaan, että käyttäisit `TREE`.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Konfigurointitiedostossa asetusten nimet käytetään aina ilman etuliitettä.

!!! tip "Vanhojen vaihtoehtojen tarkistaminen"
    Vanhoista konfigurointivaihtoehdoista, joihin palvelimesi edelleen luottaa – kuten ilman etuliitettä olevat ympäristömuuttujat, `SEARCH_INDEX_DIR` tai `EMAIL_USE_TLS` – lokitetaan varoituksia käynnistyksessä. Gramps Web API 3.22:sta alkaen ne myös luetellaan, yhdessä niiden korvausten ja version kanssa, jossa tuki poistetaan, **Järjestelmän tiedot** -sivun yläosassa (johon pääsee käyttäjäkuvakkeesta sovelluksen yläreunassa), kun olet kirjautuneena järjestelmänvalvojana.

    Sähköpostiasetukset ja perus-URL, jotka vanhempien versioiden ensimmäisen käynnistysvelhon tallentamat tiedot ovat myös lueteltu siellä. Aseta ne konfigurointiisi tallennettuihin arvoihin; varoitus katoaa, kun ne vastaavat.

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuun tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta, jolla on tämä nimi, ei ole, uusi tyhjää puuta luodaan.
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
`MEDIA_BASE_DIR` | Polku, jota käytetään media tiedostojen peruskansiona, joka ohittaa Grampsissa asetetun media peruskansion. Kun käytetään [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `*`). Kun asetettu, palvelin tunnistaa puun hakemiston nimen perusteella sen näyttönimen sijaan, mikä on kestävämpää uudelleennimeämiselle. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimen voi löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Hakemiston tietokannan URL-osoite. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvo on `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston `indexdir`-kansioon suhteessa polkuun, josta skripti ajetaan
`SEARCH_INDEX_DIR` | **Vanhentunut** (käytä sen sijaan `SEARCH_INDEX_DB_URI`). Hakemisto, joka sisältää hakemiston. Jos asetetaan, kun `SEARCH_INDEX_DB_URI` on asettamatta, hakemiston URL-osoite johdetaan muodossa `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta staattisia tiedostoja tarjoillaan (esim. staattinen verkkosovellus)
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan palautuslinkkien rakentamiseen. Web Push vaatii myös julkisesti saavutettavan HTTPS-URL-osoitteen; oletusarvo `http://localhost/` poistaa käytöstä Web Pushin. Kun määrität tämän asetuksen ympäristön kautta, käytä `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki on estetty. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan palautussähköpostien lähettämiseen)
`EMAIL_PORT` | SMTP-palvelimen portti. oletusarvo on 465
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana
`EMAIL_USE_TLS` | **Vanhentunut** (käytä sen sijaan `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvo on `True`. Käytettäessä STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:ssä (v3.6.0+). Oletusarvo on `True`, jos `EMAIL_USE_TLS` ei ole nimenomaan asetettu. Tyypillisesti käytetään portin 465 kanssa.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:ssä (v3.6.0+). Oletusarvo on `False`. Tyypillisesti käytetään portin 587 tai 25 kanssa.
`DEFAULT_FROM_EMAIL` | "Lähettäjä" -osoite automatisoiduille sähköposteille
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvien välimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriaan. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan
`BACKUP_DIR` | Hakemisto, johon [varmuuskopiot](../administration/settings.md#backups) tallennetaan, jokaiselle puulle oma alihakemisto (v3.24.0+). Jos ei ole asetettu (oletusarvo), varmuuskopioita ei voida tallentaa palvelimelle, mutta ne voidaan silti palauttaa ladatusta tiedostosta. Käytä pysyvää sijaintia, esim. Docker-tilavuutta, ja mieluiten sellaista, joka varmuuskopioidaan tai synkronoidaan muualle.
`BACKUP_KEEP` | Tallennettujen varmuuskopioiden määrä per puu; vanhemmat poistetaan, kun uusi varmuuskopio luodaan (v3.24.0+). Oletusarvo on `5`
`RATE_LIMIT_BACKUP` | Varmuuskopioiden luomisen nopeusrajoitus per puu (v3.24.0+). Oletusarvo on `"10 päivässä"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Media-arkistojen luomisen nopeusrajoitus Vienti-sivulla. Oletusarvo on `"1 tunnissa"`
`REGISTRATION_DISABLED` | Jos `True`, estä uusien käyttäjien rekisteröinti (oletusarvo `False`)
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastollinen telemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS -parametrin, joka osoittaa, kuinka monta pikseliä käsitelty kuva voi sisältää. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovin suurimman tiedostokoon pikkukuville. Oletusarvo on `50 * 1024 * 1024` (50 MB). Sen nostaminen voi suuresti lisätä muistinkäyttöä ja voi johtaa muistivaurioihin tai tietojen menetykseen, jos suuria tiedostoja purkautuu muistissa.


!!! info
    Kun käytät ympäristömuuttujia konfiguroinnissa, boolean-vaihtoehtojen, kuten `EMAIL_USE_SSL`, on oltava joko merkkijono `true` tai `false` (kirjainkoolla on merkitystä!).


### Asetukset PostgreSQL-tietokannoille

Nämä asetukset ovat pakollisia, jos sukupuutasi isännöidään [PostgreSQL-tietokannassa](postgres.md) käyttäen SharedPostgreSQL-lisäosaa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Tietokantayhteyden käyttäjänimi
`POSTGRES_PASSWORD` | Tietokannan käyttäjän salasana


### Asetukset, jotka liittyvät useiden puiden isännöimiseen

Seuraavat asetukset ovat tärkeitä, kun [isännöidään useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media tiedostoille. Oletusarvo on `False`, mutta suositellaan vahvasti käytettäväksi `True` usean puun asetuksessa
`NEW_DB_BACKEND` | Tietokannan taustajärjestelmä, jota käytetään uusille sukupuulle. Sen on oltava joko `sqlite` tai `sharedpostgresql`. Oletusarvo on `sqlite`. Arvo `postgresql` hyväksytään edelleen, mutta se on vanhentunut, koska PostgreSQL-taustajärjestelmä poistetaan Gramps Web API 4.0:ssä.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten palveluntarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, otetaanko OIDC-todennus käyttöön. Oletusarvo on `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjän URL-osoite (muille OIDC-palveluntarjoajille)
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (muille OIDC-palveluntarjoajille)
`OIDC_CLIENT_SECRET` | OAuth-asiakkaan salasana (muille OIDC-palveluntarjoajille)
`OIDC_NAME` | Mukautettu näyttönimi palveluntarjoajalle. Oletusarvo on "OIDC"
`OIDC_SCOPES` | OAuth-alueet. Oletusarvo on "openid email profile"
`OIDC_USERNAME_CLAIM` | Vaade, jota käytetään käyttäjänimen määrittämiseen. Oletusarvo on "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL-osoite OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`)
`OIDC_PKCE` | Boolean, käytetäänkö PKCE:tä. Jos ei ole asetettu, PKCE:tä käytetään, kun palveluntarjoajan löytöasiakirja listaa `S256`. Katso [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, käytetäänkö paikallista käyttäjänimen/salasanan todennusta. Oletusarvo on `False`
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi palveluntarjoaja on määritetty. Oletusarvo on `False`

#### Sisäänrakennetut OIDC-palveluntarjoajat

Sisäänrakennettuja palveluntarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakkaan salasana Google OAuth:lle
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakkaan salasana Microsoft OAuth:lle
`OIDC_GOOGLE_PKCE` | Boolean, PKCE-asetus Googlelle, katso [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolean, PKCE-asetus Microsoftille, katso [PKCE](oidc.md#pkce)

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoituksen identiteettipalveluntarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Vaade-nimi OIDC-tunnuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo on "groups"
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Admin" -roolia
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Owner" -roolia
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Editor" -roolia
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Contributor" -roolia
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Member" -roolia
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-palveluntarjoajastasi, joka vastaa Grampsin "Guest" -roolia

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää AI-pohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua. Katso [AI-keskustelun määrittäminen](chat.md) lisätietoja varten.

!!! warning "Semanttinen haku on vanhentunut"
    Semanttinen haku, ja sen mukana `VECTOR_EMBEDDING_*` -asetukset, on vanhentunut ja poistetaan Gramps Web API 3.25:ssä. Tämän jälkeen `VECTOR_EMBEDDING_MODEL` hyväksytään edelleen, mutta sitä ei käytetä. Gramps Web API 3.24:stä alkaen AI-keskustelu tarvitsee vain `LLM_MODEL`.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvo on `None`, joka käyttää OpenAI API:a.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei ole asetettu (oletusarvo), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-avustaja käyttää Pydantic AI:ta työkalukutsukyvykkyyksillä.
`VECTOR_EMBEDDING_MODEL` | **Vanhentunut**, poistetaan 3.25:ssä. Malli, jota käytetään semanttisen haun vektoriupotuksille. Kun käytetään paikallista mallia, tämän on oltava [Sentence Transformers](https://sbert.net/) -mallin nimi. Kun käytetään etä-API:a (katso `VECTOR_EMBEDDING_BASE_URL`), tämä on mallin nimi, joka lähetetään etäpalveluntarjoajalle. Jos ei ole asetettu (oletusarvo), semanttinen haku on pois käytöstä. Ennen Gramps Web API 3.24:ää keskustelu oli myös pois käytöstä.
`VECTOR_EMBEDDING_BASE_URL` | **Vanhentunut**, poistetaan 3.25:ssä. Perus-URL etä-OpenAI-yhteensopivalle upotus-API:lle (esim. Ollama, OpenAI, LiteLLM). Jos ei ole asetettu (oletusarvo), käytetään paikallista Sentence Transformers -mallia. Katso [Etä-upotus-API:n käyttäminen](chat.md#using-a-remote-embedding-api) lisätietoja varten.
`VECTOR_EMBEDDING_API_KEY` | **Vanhentunut**, poistetaan 3.25:ssä. API-avain todennetuille etä-upotuspalveluntarjoajille. Tarvitaan vain, kun `VECTOR_EMBEDDING_BASE_URL` on asetettu ja palveluntarjoaja vaatii todennusta.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvo on 50000.
`LLM_SYSTEM_PROMPT` | Mukautettu järjestelmäkehotus LLM-keskusteluavustajalle (v3.6.0+). Jos ei ole asetettu, käytetään oletusarvoista sukututkimusoptimoitua kehotusta.


## Esimerkkikonfigurointitiedosto

Minimalistinen konfigurointitiedosto tuotantoa varten voisi näyttää tältä:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portissa 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
