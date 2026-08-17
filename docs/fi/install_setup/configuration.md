# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittavat asetukset voidaan tehdä selaimesta. Kuitenkin, riippuen käyttöönotosta, voi olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguraation muuttamiseen ja kaikki olemassa olevat konfigurointivaihtoehdot.


## Konfiguraatiotiedosto vs. ympäristömuuttujat

Asetusten osalta voit käyttää joko konfiguraatiotiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asennusta](deployment.md), voit sisällyttää konfiguraatiotiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfiguraatiotiedostoon palvelimesi tiedostojärjestelmässä (oikeanpuoleinen viittaa polkuun säilössä, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen eteen `GRAMPSWEB_` saadaksesi ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfiguraatioasetukselle

Huomaa, että ympäristön kautta asetetut konfiguraatioasetukset menevät edelle konfiguraatiotiedostossa olevista. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

!!! warning "Ilman etuliitettä olevat ympäristömuuttujat ovat vanhentuneita"
    Historiallisista syistä muutama asetus – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, ja `STATIC_PATH` – voidaan edelleen asettaa ympäristömuuttujan kautta *ilman* `GRAMPSWEB_` etuliitettä. Tämä on vanhentunutta, lokittaa varoituksen käynnistyksessä ja lakkaa toimimasta tulevassa julkaisussa. Käytä aina etuliitteellistä muotoa, esim. `GRAMPSWEB_TREE` sen sijaan, että käyttäisit `TREE`.

    Huomaa, että tämä koskee vain ympäristömuuttujia. Konfiguraatiotiedostossa asetusten nimet käytetään aina ilman etuliitettä.

## Olemassa olevat konfiguraatioasetukset
Seuraavat konfiguraatioasetukset ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuun tietokannan nimi. Näytä saatavilla olevat puut komennolla `gramps -l`. Jos puuta tällä nimellä ei ole, uusi tyhjää puuta luodaan.
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
`MEDIA_BASE_DIR` | Polku, jota käytetään media tiedostojen perushakemistona, ohittaen Grampsissa asetetun media perushakemiston. Kun käytetään [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`TREE_ID` | Sukupuun tietokannan hakemiston nimi, jota käytetään yksittäisen puun tilassa (kun `TREE` ei ole asetettu `*`). Kun asetettu, palvelin tunnistaa puun sen hakemiston nimen perusteella sen sijaan, että käyttäisi sen näyttönimeä, mikä on kestävämpää uudelleennimeämiselle. Pakollinen, jos haluat nimetä puun uudelleen API:n kautta. Hakemiston nimen voi löytää komennolla `GET /api/trees/-` (kenttä `id`).
`SEARCH_INDEX_DB_URI` | Hakemistoindeksin tietokannan URL-osoite. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvo on `sqlite:///indexdir/search_index.db`, luoden SQLite-tiedoston hakemistoon `indexdir` suhteessa polkuun, jossa skripti ajetaan.
`SEARCH_INDEX_DIR` | **Vanhentunut** (käytä sen sijaan `SEARCH_INDEX_DB_URI`). Hakemisto, joka sisältää hakemistoindeksin. Jos asetetaan, kun `SEARCH_INDEX_DB_URI` on asetettu, hakemistoindeksin URL-osoite johdetaan muodosta `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Polku, josta palvellaan staattisia tiedostoja (esim. staattinen verkkosivuston etupää).
`BASE_URL` | Perus URL-osoite, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan nollauslinkkien rakentamiseksi.
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki on kielletty. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan nollaus sähköpostien lähettämiseen).
`EMAIL_PORT` | SMTP-palvelimen portti. Oletusarvo on 465.
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi.
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana.
`EMAIL_USE_TLS` | **Vanhentunut** (käytä sen sijaan `EMAIL_USE_SSL` tai `EMAIL_USE_STARTTLS`). Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvo on `True`. Käytettäessä STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`EMAIL_USE_SSL` | Boolean, käytetäänkö implisiittistä SSL/TLS:ää SMTP:ssä (v3.6.0+). Oletusarvo on `True`, jos `EMAIL_USE_TLS` ei ole nimenomaisesti asetettu. Tyypillisesti käytetään portin 465 kanssa.
`EMAIL_USE_STARTTLS` | Boolean, käytetäänkö eksplisiittistä STARTTLS:ää SMTP:ssä (v3.6.0+). Oletusarvo on `False`. Tyypillisesti käytetään portilla 587 tai 25.
`DEFAULT_FROM_EMAIL` | "From" osoite automatisoiduille sähköposteille.
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvien välimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriassa. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan.
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan.
`REGISTRATION_DISABLED` | Jos `True`, estä uusien käyttäjien rekisteröinti (oletusarvo `False`).
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastollinen telemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.
`PILLOW_MAX_IMAGE_PIXELS` | Asettaa PIL.Image.MAX_IMAGE_PIXELS -parametrin, joka osoittaa, kuinka monta pikseliä käsitellyssä kuvassa voi olla. Katso [dokumentaatio](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) lisätietoja varten.
`MAX_THUMBNAIL_FILE_BYTES` | Asettaa kovaksi maksimi tiedostokooksi pikkukuville. Oletusarvo on `50 * 1024 * 1024` (50 MB). Sen nostaminen voi huomattavasti lisätä muistinkäyttöä ja voi johtaa muistivaurioihin tai tietojen menetykseen, jos suuria tiedostoja purkautuu muistiin.


!!! info
    Kun käytetään ympäristömuuttujia konfiguraatiossa, boolean-asetusten kuten `EMAIL_USE_SSL` on oltava joko merkkijono `true` tai `false` (isot ja pienet kirjaimet huomioiden!).


### Asetukset vain PostgreSQL-taustatietokannalle

Tämä on tarpeen, jos olet konfiguroinut Gramps-tietokannan toimimaan [PostgreSQL-lisäosan](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) kanssa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Käyttäjänimi tietokantayhteydelle.
`POSTGRES_PASSWORD` | Salasana tietokannan käyttäjälle.


### Asetukset, jotka ovat merkityksellisiä useiden puiden isännöinnissä

Seuraavat asetukset ovat merkityksellisiä, kun [isännöidään useita puita](multi-tree.md).


Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alihakemistoa jokaisen puun media tiedostoille. Oletusarvo on `False`, mutta suositellaan vahvasti käyttämään `True` usean puun asennuksessa.
`NEW_DB_BACKEND` | Tietokannan taustajärjestelmä, jota käytetään uusille sukupuulle. Sen on oltava yksi seuraavista: `sqlite`, `postgresql` tai `sharedpostgresql`. Oletusarvo on `sqlite`.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asennusta SharedPostgreSQL-taustajärjestelmällä.
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asennusta SharedPostgreSQL-taustajärjestelmällä.


### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, sallitaanko OIDC-todennus. Oletusarvo on `False`.
`OIDC_ISSUER` | OIDC-palveluntarjoajan myöntäjä URL-osoite (muille OIDC-palveluntarjoajille).
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (muille OIDC-palveluntarjoajille).
`OIDC_CLIENT_SECRET` | OAuth-asiakassalasana (muille OIDC-palveluntarjoajille).
`OIDC_NAME` | Mukautettu näyttönimi palveluntarjoajalle. Oletusarvo on "OIDC".
`OIDC_SCOPES` | OAuth-alueet. Oletusarvo on "openid email profile".
`OIDC_USERNAME_CLAIM` | Väite, jota käytetään käyttäjänimenä. Oletusarvo on "preferred_username".
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL-osoite OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`).
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, estetäänkö paikallinen käyttäjänimi/salasana-todennus. Oletusarvo on `False`.
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi palveluntarjoaja on konfiguroitu. Oletusarvo on `False`.

#### Sisäänrakennetut OIDC-palveluntarjoajat

Sisäänrakennettuja palveluntarjoajia (Google, Microsoft) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle.
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalasana Google OAuth:lle.
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle.
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalasana Microsoft OAuth:lle.

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoittamisen identiteettipalveluntarjoajaltasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Väite, joka sisältää käyttäjän ryhmät/roolit OIDC-tunnuksessa. Oletusarvo on "groups".
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Admin" -roolia.
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Owner" -roolia.
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Editor" -roolia.
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Contributor" -roolia.
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Member" -roolia.
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Guest" -roolia.

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää tekoälypohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus URL-osoite OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvo on `None`, joka käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei asetettu (oletusarvo), keskustelu on pois käytöstä. Versiosta v3.6.0 alkaen AI-avustaja käyttää Pydantic AI:ta työkalukutsukyvykkyyksillä.
`VECTOR_EMBEDDING_MODEL` | [Sentence Transformers](https://sbert.net/) -malli, jota käytetään semanttisen haun vektori-integraatioihin. Jos ei asetettu (oletusarvo), semanttinen haku ja keskustelu ovat pois käytöstä.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja sukupuun kontekstille, joka annetaan LLM:lle. Oletusarvo on 50000.
`LLM_SYSTEM_PROMPT` | Mukautettu järjestelmäkehotus LLM-keskusteluavustajalle (v3.6.0+). Jos ei asetettu, käytetään oletusarvoista sukututkimukseen optimoitua kehotusta.


## Esimerkkikonfiguraatiotiedosto

Minimalistinen konfiguraatiotiedosto tuotantoa varten voisi näyttää tältä:
```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portissa 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
