# Palvelimen konfigurointi

Oletusarvoista Docker-kuvaa käyttäen kaikki tarvittava konfigurointi voidaan tehdä selaimesta. Kuitenkin, riippuen käyttöönotosta, voi olla tarpeen mukauttaa palvelimen konfigurointia.

Tällä sivulla luetellaan kaikki menetelmät konfiguroinnin muuttamiseksi ja kaikki olemassa olevat konfigurointivaihtoehdot.

## Konfigurointitiedosto vs. ympäristömuuttujat

Asetusten osalta voit käyttää joko konfigurointitiedostoa tai ympäristömuuttujia.

Kun käytät [Docker Compose -pohjaista asetusta](deployment.md), voit sisällyttää konfigurointitiedoston lisäämällä seuraavan luettelokohdan `volumes:`-avaimen alle `grampsweb:`-lohkoon:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
missä `/path/to/config.cfg` on polku konfigurointitiedostoon palvelimen tiedostojärjestelmässä (oikealla puolella viitataan polkuun säilössä, eikä sitä saa muuttaa).

Kun käytät ympäristömuuttujia,

- lisää jokaisen asetuksen nimeen etuliite `GRAMPSWEB_` saadaksesi ympäristömuuttujan nimen
- Käytä kaksoisalaviivoja sisäkkäisille sanakirja-asetuksille, esim. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` asettaa arvon `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` konfigurointivaihtoehdolle

Huomaa, että ympäristön kautta asetetut konfigurointivaihtoehdot menevät edelle konfigurointitiedostossa olevista. Jos molemmat ovat läsnä, ympäristömuuttuja "voittaa".

## Olemassa olevat konfigurointiasetukset
Seuraavat konfigurointivaihtoehdot ovat olemassa.

### Pakolliset asetukset

Avain | Kuvaus
----|-------------
`TREE` | Käytettävän sukupuun tietokannan nimi. Näytä käytettävissä olevat puut komennolla `gramps -l`. Jos puuta tällä nimellä ei ole, uusi tyhjää puuta luodaan.
`SECRET_KEY` | Salainen avain Flaskille. Salaisuutta ei saa jakaa julkisesti. Sen muuttaminen mitätöi kaikki käyttöoikeustunnukset.
`USER_DB_URI` | Käyttäjätietokannan tietokanta-URL. Mikä tahansa SQLAlchemyn kanssa yhteensopiva URL on sallittu.

!!! info
    Voit luoda turvallisen salaisen avaimen esim. komennolla

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Valinnaiset asetukset

Avain | Kuvaus
----|-------------
`MEDIA_BASE_DIR` | Polku, jota käytetään media-tiedostojen perushakemistona, joka ohittaa Grampsissa asetetun media-perushakemiston. Kun käytetään [S3](s3.md), sen on oltava muotoa `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | Tietokannan URL hakemistolle. Vain `sqlite` tai `postgresql` ovat sallittuja taustajärjestelminä. Oletusarvo on `sqlite:///indexdir/search_index.db`, joka luo SQLite-tiedoston kansioon `indexdir` suhteessa polkuun, josta skripti ajetaan
`STATIC_PATH` | Polku, josta staattisia tiedostoja tarjoillaan (esim. staattinen verkkosivuston etuosa)
`BASE_URL` | Perus-URL, josta API on saavutettavissa (esim. `https://mygramps.mydomain.com/`). Tämä on tarpeen esim. oikeiden salasanan palautuslinkkien rakentamiseksi
`CORS_ORIGINS` | Alkuperät, joista CORS-pyynnöt ovat sallittuja. Oletusarvoisesti kaikki on estetty. Käytä `"*"` salliaksesi pyynnöt mistä tahansa verkkotunnuksesta.
`EMAIL_HOST` | SMTP-palvelimen isäntä (esim. salasanan palautus-sähköpostien lähettämiseen)
`EMAIL_PORT` | SMTP-palvelimen portti. oletusarvo on 465
`EMAIL_HOST_USER` | SMTP-palvelimen käyttäjänimi
`EMAIL_HOST_PASSWORD` | SMTP-palvelimen salasana
`EMAIL_USE_TLS` | Boolean, käytetäänkö TLS:ää sähköpostien lähettämiseen. Oletusarvo on `True`. Kun käytetään STARTTLS:ää, aseta tämä `False` ja käytä eri porttia kuin 25.
`DEFAULT_FROM_EMAIL` | "From" -osoite automaattisille sähköposteille
`THUMBNAIL_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pikkukuvavälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`REQUEST_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pyyntövälimuistille. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`PERSISTENT_CACHE_CONFIG` | Sanakirja, jossa on asetuksia pysyvälle välimuistille, jota käytetään esim. telemetriaan. Katso [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) mahdollisista asetuksista.
`CELERY_CONFIG` | Asetukset Celery-taustatehtäväjonolle. Katso [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) mahdollisista asetuksista.
`REPORT_DIR` | Väliaikainen hakemisto, johon Gramps-raporttien suorittamisen tulokset tallennetaan
`EXPORT_DIR` | Väliaikainen hakemisto, johon Gramps-tietokannan vientitulokset tallennetaan
`REGISTRATION_DISABLED` | Jos `True`, estä uusien käyttäjien rekisteröinti (oletusarvo `False`)
`DISABLE_TELEMETRY` | Jos `True`, poista käytöstä tilastotelemetria (oletusarvo `False`). Katso [telemetria](telemetry.md) lisätietoja varten.

!!! info
    Kun käytetään ympäristömuuttujia konfiguroinnissa, boolean-asetusten kuten `EMAIL_USE_TLS` on oltava joko merkkijono `true` tai `false` (merkkikoolla on merkitystä!).

### Asetukset vain PostgreSQL-taustatietokannalle

Tämä on tarpeen, jos olet konfiguroinut Gramps-tietokannan toimimaan [PostgreSQL-lisäosan](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) kanssa.

Avain | Kuvaus
----|-------------
`POSTGRES_USER` | Käyttäjänimi tietokantayhteydelle
`POSTGRES_PASSWORD` | Tietokannan käyttäjän salasana

### Asetukset useiden puiden isännöimiseen liittyen

Seuraavat asetukset ovat tärkeitä, kun [isännöidään useita puita](multi-tree.md).

Avain | Kuvaus
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, käytetäänkö erillistä alikansiota jokaisen puun media-tiedostoille. Oletusarvo on `False`, mutta suositellaan vahvasti käytettäväksi `True` usean puun asetuksessa
`NEW_DB_BACKEND` | Tietokannan taustajärjestelmä, jota käytetään uusille sukupuulle. Sen on oltava yksi seuraavista: `sqlite`, `postgresql` tai `sharedpostgresql`. Oletusarvo on `sqlite`.
`POSTGRES_HOST` | PostgreSQL-palvelimen isäntänimi, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä
`POSTGRES_PORT` | PostgreSQL-palvelimen portti, jota käytetään uusien puiden luomiseen, kun käytetään usean puun asetusta SharedPostgreSQL-taustajärjestelmällä

### Asetukset OIDC-todennusta varten

Nämä asetukset ovat tarpeen, jos haluat käyttää OpenID Connect (OIDC) -todennusta ulkoisten tarjoajien kanssa. Yksityiskohtaisia asennusohjeita ja esimerkkejä varten katso [OIDC-todennus](oidc.md).

Avain | Kuvaus
----|-------------
`OIDC_ENABLED` | Boolean, otetaanko OIDC-todennus käyttöön. Oletusarvo on `False`.
`OIDC_ISSUER` | OIDC-tarjoajan myöntäjä-URL (kustomoiduille OIDC-tarjoajille)
`OIDC_CLIENT_ID` | OAuth-asiakastunnus (kustomoiduille OIDC-tarjoajille)
`OIDC_CLIENT_SECRET` | OAuth-asiakassalasana (kustomoiduille OIDC-tarjoajille)
`OIDC_NAME` | Kustomoitu näyttönimi tarjoajalle. Oletusarvo on "OIDC"
`OIDC_SCOPES` | OAuth-alueet. Oletusarvo on "openid email profile"
`OIDC_USERNAME_CLAIM` | Vaatimus, jota käytetään käyttäjänimen määrittämiseen. Oletusarvo on "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Valinnainen: URL OpenID Connect -konfiguraatiopisteeseen (jos ei käytetä standardia `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, estetäänkö paikallinen käyttäjänimi/salasana-todennus. Oletusarvo on `False`
`OIDC_AUTO_REDIRECT` | Boolean, ohjataanko automaattisesti OIDC:hen, kun vain yksi tarjoaja on määritetty. Oletusarvo on `False`

#### Sisäänrakennetut OIDC-tarjoajat

Sisäänrakennettuja tarjoajia (Google, Microsoft, GitHub) varten käytä näitä asetuksia:

Avain | Kuvaus
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Asiakastunnus Google OAuth:lle
`OIDC_GOOGLE_CLIENT_SECRET` | Asiakassalasana Google OAuth:lle
`OIDC_MICROSOFT_CLIENT_ID` | Asiakastunnus Microsoft OAuth:lle
`OIDC_MICROSOFT_CLIENT_SECRET` | Asiakassalasana Microsoft OAuth:lle
`OIDC_GITHUB_CLIENT_ID` | Asiakastunnus GitHub OAuth:lle
`OIDC_GITHUB_CLIENT_SECRET` | Asiakassalasana GitHub OAuth:lle

#### OIDC-roolien kartoitus

Nämä asetukset mahdollistavat OIDC-ryhmien/roolien kartoittamisen identiteettitarjoajastasi Gramps Web -käyttäjärooleihin:

Avain | Kuvaus
----|-------------
`OIDC_ROLE_CLAIM` | Vaatimuksen nimi OIDC-tunnuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo on "groups"
`OIDC_GROUP_ADMIN` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Admin" -roolia
`OIDC_GROUP_OWNER` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Owner" -roolia
`OIDC_GROUP_EDITOR` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Editor" -roolia
`OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Contributor" -roolia
`OIDC_GROUP_MEMBER` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Member" -roolia
`OIDC_GROUP_GUEST` | Ryhmän/roolin nimi OIDC-tarjoajastasi, joka vastaa Grampsin "Guest" -roolia

### Asetukset vain AI-ominaisuuksia varten

Nämä asetukset ovat tarpeen, jos haluat käyttää tekoälypohjaisia ominaisuuksia, kuten keskustelua tai semanttista hakua.

Avain | Kuvaus
----|-------------
`LLM_BASE_URL` | Perus-URL OpenAI-yhteensopivalle keskustelu-API:lle. Oletusarvo on `None`, mikä käyttää OpenAI API:ta.
`LLM_MODEL` | Malli, jota käytetään OpenAI-yhteensopivassa keskustelu-API:ssa. Jos ei asetettu (oletusarvo), keskustelu on pois päältä.
`VECTOR_EMBEDDING_MODEL` | [Sentence Transformers](https://sbert.net/) -malli, jota käytetään semanttisen haun vektoriupotuksiin. Jos ei asetettu (oletusarvo), semanttinen haku ja keskustelu ovat pois päältä.
`LLM_MAX_CONTEXT_LENGTH` | Merkkiraja perhesuhteiden kontekstille, joka annetaan LLM:lle. Oletusarvo on 50000.

## Esimerkkikonfigurointitiedosto

Minimalistinen konfigurointitiedosto tuotantokäyttöön voisi näyttää tältä:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
