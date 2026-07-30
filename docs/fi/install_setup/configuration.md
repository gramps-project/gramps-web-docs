# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittava konfigurointi voidaan tehdä selaimesta. Kuitenkin, riippuen käyttöönotosta, voi olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseksi ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfigurointitiedosto vs. ympäristömuuttujat

Asetusten osalta voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asennusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimen tiedostojärjestelmässä (oikeanpuoleinen viittaa polkuun säilössä eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen nimeen etuliite `GRAMPSWEB_` saadaksesi ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot ovat etusijalla konfigurointitiedostossa oleviin verrattuna. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuuyhteyden tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta tällä nimellä ei ole, uusi tyhjää puuta luodaan.
`SECRET_KEY` | Flaskin salainen avain. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki pääsytunnukset.
`USER_DB_URI` | Käyttäjä tietokannan tietokanta-URL. Mikä tahansa SQLAlchemy-yhteensopiva URL on sallittu.

!!! info
    Voit luoda turvallisen salaisen avaimen esim. komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Polku, jota käytetään media-tiedostojen perushakemistona, ohittaen Grampsissa asetetun media-perushakemiston. Käytettäessä [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
 `TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `MULTI`). Kun se on asetettu, palvelin tunnistaa puun sen hakemiston nimen perusteella eikä sen näyttönimen perusteella, mikä on kestävämpää uudelleennimeämisille. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimen voi löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Hakemiston URL-haku. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvoisesti `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston `indexdir`-kansioon suhteessa polkuun, josta skripti ajetaan.
`STATIC_PATH` | Polku, josta staattisia tiedostoja tarjoillaan (esim. staattinen verkkosivuston etupää).
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan palautuslinkkien rakentamiseksi.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki ovat kiellettyjä. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan palautussähköpostien lähettämiseen).
`EMAIL_PORT` | SMTP-palvelimen portti. Oletusarvoisesti 465.
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi.
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana.
`EMAIL_USE_TLS` | **Vanha** (käytä sen sijaan `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvoisesti `True`. Käytettäessä STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:lle (v3.6.0+). Oletusarvoisesti `True`, jos `EMAIL_USE_TLS` ei ole nimenomaisesti asetettu. Tyypillisesti käytetään portilla 465.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:lle (v3.6.0+). Oletusarvoisesti `False`. Tyypillisesti käytetään portilla 587 tai 25.
`DEFAULT_FROM_EMAIL` | "From" osoite automatisoiduille sähköposteille.
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvavälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriaan. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan.
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan.
`REGISTRATION_DISABLED` | Jos `True`, estä uusi käyttäjärekisteröinti (oletus `False`).
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastollinen telemetria (oletus `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS-parametrin, joka osoittaa, kuinka monta pikseliä käsitelty kuva voi sisältää. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovin maksimikoko pikkukuville. Oletusarvoisesti `50 * 1024 * 1024` (50 MB). Sen nostaminen voi suuresti lisätä muistin käyttöä ja voi johtaa muistivaurioihin tai tietojen menetykseen, jos suuria tiedostoja purkautuu muistiin.

!!! info
    Kun käytät ympäristömuuttujia konfigurointiin, boolean-vaihtoehtojen, kuten `EMAIL_USE_TLS`, on oltava joko merkkijono `true` tai `false` (isot ja pienet kirjaimet huomioiden!).


### Asetukset vain PostgreSQL-taustatietokannalle

Tämä on tarpeen, jos olet konfiguroinut Gramps-tietokannan toimimaan [PostgreSQL-lisäosan](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) kanssa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Tietokantayhteyden käyttäjänimi.
`POSTGRES_PASSWORD` | Tietokantakäyttäjän salasana.


### Asetukset useiden puiden isännöimiseen

Seuraavat asetukset ovat tärkeitä, kun [isännöidään useita puita](multi-tree.md).

Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media-tiedostoille. Oletusarvoisesti `False`, mutta suositellaan vahvasti käytettäväksi `True` usean puun asennuksessa.
`NEW_DB_BACKEND` | Tietokantatausta, jota käytetään uusille sukupuulle. Sen on oltava yksi seuraavista: `sqlite`, `postgresql` tai `sharedpostgresql`. Oletusarvoisesti `sqlite`.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asennusta SharedPostgreSQL-taustalla.
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asennusta SharedPostgreSQL-taustalla.


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, käytetäänkö OIDC-todennusta. Oletusarvoisesti `False`.
`OIDC_ISSUER` | OIDC-tarjoajan myöntäjä-URL (räätälöidyille OIDC-tarjoajille).
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (räätälöidyille OIDC-tarjoajille).
`OIDC_CLIENT_SECRET` | OAuth-asiakassalaisuus (räätälöidyille OIDC-tarjoajille).
`OIDC_NAME` | Räätälöity näyttönimi tarjoajalle. Oletusarvoisesti "OIDC".
`OIDC_SCOPES` | OAuth-alueet. Oletusarvoisesti "openid email profile".
`OIDC_USERNAME_CLAIM` | Väite, jota käytetään käyttäjänimenä. Oletusarvoisesti "preferred_username".
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`).
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, estetäänkö paikallinen käyttäjänimi/salasana-todennus. Oletusarvoisesti `False`.
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi tarjoaja on määritetty. Oletusarvoisesti `False`.

#### Sisäänrakennetut OIDC-tarjoajat

Sisäänrakennettuja tarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle.
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalaisuus Google OAuth:lle.
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle.
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalaisuus Microsoft OAuth:lle.

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoittamisen identiteettitarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Väite, joka sisältää käyttäjän ryhmät/roolit OIDC-tunnuksessa. Oletusarvoisesti "groups".
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Admin" -roolia.
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Owner" -roolia.
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Editor" -roolia.
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Contributor" -roolia.
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Member" -roolia.
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Guest" -roolia.

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää AI-pohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvoisesti `None`, joka käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei asetettu (oletus), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-avustaja käyttää Pydantic AI:ta työkalukutsumahdollisuuksilla.
`VECTOR_EMBEDDING_MODEL` | [Sentence Transformers](https://sbert.net/) -malli, jota käytetään semanttisten hakusanojen vektoriupotuksiin. Jos ei asetettu (oletus), semanttinen haku ja keskustelu ovat pois käytöstä.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvoisesti 50000.
`LLM_SYSTEM_PROMPT` | Räätälöity järjestelmäkehotus LLM-keskusteluavustajalle (v3.6.0+). Jos ei asetettu, käytetään oletusarvoista sukututkimukseen optimoitua kehotusta.


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
