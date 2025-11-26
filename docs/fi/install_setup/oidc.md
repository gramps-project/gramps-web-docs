# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, joka mahdollistaa käyttäjien kirjautumisen ulkoisten identiteettipalveluntarjoajien avulla. Tämä sisältää sekä suosittuja palveluntarjoajia, kuten Google, Microsoft ja GitHub, että mukautettuja OIDC-palveluntarjoajia, kuten Keycloak, Authentik ja muita.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalveluntarjoajien käytön käyttäjätodennuksessa
- Useiden todennuspalveluntarjoajien tukemisen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Webin käyttäjärooleihin
- Yksinkertaisen sisäänkirjautumisen (SSO) ja yksinkertaisen uloskirjautumisen toteuttamisen
- Paikallisen käyttäjänimen/salasanan todennuksen valinnaisen poistamisen käytöstä

## Konfigurointi

OIDC-todennuksen mahdollistamiseksi sinun on määritettävä asianmukaiset asetukset Gramps Webin konfigurointitiedostossa tai ympäristömuuttujissa. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo käytettävissä olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista lisätä jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfigurointitiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) lisätietoja varten.

### Sisäänrakennetut palveluntarjoajat

Gramps Webillä on sisäänrakennettu tuki suosituimmille identiteettipalveluntarjoajille. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` ja `OIDC_GITHUB_CLIENT_SECRET`

Voit määrittää useita palveluntarjoajia samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä palveluntarjoajat ovat käytettävissä konfigurointiarvojen perusteella.

### Mukautetut OIDC-palveluntarjoajat

Mukautettuja OIDC-palveluntarjoajia (kuten Keycloak, Authentik tai mikä tahansa standardin OIDC-yhteensopiva palveluntarjoaja) varten käytä näitä asetuksia:

| Avain                | Kuvaus                                                  |
|---------------------|--------------------------------------------------------|
| `OIDC_ENABLED`      | Boolean, onko OIDC-todennus käytössä. Aseta `True`.   |
| `OIDC_ISSUER`      | Palveluntarjoajasi myöntäjän URL-osoite               |
| `OIDC_CLIENT_ID`    | Asiakastunnus OIDC-palveluntarjoajallesi              |
| `OIDC_CLIENT_SECRET` | Asiakassalaisuus OIDC-palveluntarjoajallesi           |
| `OIDC_NAME`         | Mukautettu näyttönimi (valinnainen, oletusarvo "OIDC")|
| `OIDC_SCOPES`       | OAuth-alueet (valinnainen, oletusarvo "openid email profile")|

## Vaaditut uudelleenohjaus-URI:t

Kun määrität OIDC-palveluntarjoajaasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URI:

**OIDC-palveluntarjoajille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Riippuen palveluntarjoajasi regex-tulkista tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos palveluntarjoajasi vaatii sitä (esim. Authentik).

**OIDC-palveluntarjoajille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai rooleja identiteettipalveluntarjoajaltasi Gramps Webin käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalveluntarjoajassasi.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen määrittämiseen:

| Avain                  | Kuvaus                                                  |
|-----------------------|--------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | OIDC-tokenin väite, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo "groups" |
| `OIDC_GROUP_ADMIN`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`   | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`   | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

- Jos roolikartoitusta ei ole määritetty (ei asetettu `OIDC_GROUP_*` -muuttujia), olemassa olevat käyttäjäroolit säilytetään
- Käyttäjille myönnetään korkein rooli, johon heillä on oikeus ryhmän jäsenyyden perusteella
- Roolikartoitus on oletusarvoisesti kirjainkooltaan herkkä (riippuu OIDC-palveluntarjoajastasi)

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksinkertaista uloskirjautumista (SSO-ulosskirjautumista) OIDC-palveluntarjoajille. Kun käyttäjä kirjautuu ulos Gramps Webistä OIDC:n kautta, hänet ohjataan automaattisesti identiteettipalveluntarjoajan uloskirjautumissivulle, jos palveluntarjoaja tukee `end_session_endpoint` -pistettä.

### Takakanavan uloskirjautuminen

Gramps Web toteuttaa OpenID Connect Back-Channel Logout -määrityksen. Tämä mahdollistaa identiteettipalveluntarjoajien ilmoittaa Gramps Webille, kun käyttäjä kirjautuu ulos toisesta sovelluksesta tai itse identiteettipalveluntarjoajasta.

#### Konfigurointi

Määritä takakanavan uloskirjautuminen identiteettipalveluntarjoajasi kanssa:

1. **Rekisteröi takakanavan uloskirjautumispiste** identiteettipalveluntarjoajasi asiakaskonfiguraatiossa:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Määritä palveluntarjoajasi** lähettämään uloskirjautumisilmoituksia. Tarkat vaiheet riippuvat palveluntarjoajastasi:

   **Keycloak:**

   - Siirry asiakaskonfiguraatiossa kohtaan "Asetukset"
   - Aseta "Takakanavan uloskirjautumis-URL" arvoksi `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Ota käyttöön "Takakanavan uloskirjautumisen istuntovaatimus", jos haluat istuntopohjaisen uloskirjautumisen

   **Authentik:**

   - Lisää palveluntarjoajan konfiguraatiossa takakanavan uloskirjautumis-URL
   - Varmista, että palveluntarjoaja on määritetty lähettämään uloskirjautumistokenit

!!! warning "Tokenin vanheneminen"
    JWT-tokenien tilattoman luonteen vuoksi takakanavan uloskirjautuminen kirjaa tällä hetkellä uloskirjautumistapahtuman, mutta ei voi heti peruuttaa jo myönnettyjä JWT-tokeneita. Tokenit pysyvät voimassa, kunnes ne vanhenevat (oletusarvo: 15 minuuttia pääsytokeneille).

    Parannetun turvallisuuden vuoksi harkitse:

    - JWT-tokenin vanhenemisaikojen lyhentämistä (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Käyttäjien opastamista kirjautumaan ulos manuaalisesti Gramps Webistä, kun he kirjautuvat ulos identiteettipalveluntarjoajastaan

!!! tip "Kuinka se toimii"
    Kun käyttäjä kirjautuu ulos identiteettipalveluntarjoajastaan tai muusta sovelluksesta:

    1. Palveluntarjoaja lähettää `logout_token` JWT:n Gramps Webin takakanavan uloskirjautumispisteeseen
    2. Gramps Web validoi tokenin ja kirjaa uloskirjautumistapahtuman
    3. Uloskirjautumistokenin JTI lisätään estolistalle, jotta replay-hyökkäykset estetään
    4. Kaikki uudet API-pyynnöt käyttäjän JWT:llä hylätään, kun tokenit vanhenevat

## Esimerkkikonfiguraatiot

### Mukautettu OIDC-palveluntarjoaja (Keycloak)

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Mukautettu OIDC-konfiguraatio
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Perhe SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Valinnainen: ohjaa automaattisesti SSO-kirjautumiseen
OIDC_DISABLE_LOCAL_AUTH=True  # Valinnainen: poista käyttäjänimi/salasana -kirjautuminen käytöstä

# Valinnainen: Roolikartoitus OIDC-ryhmistä Grampsin rooleihin
OIDC_ROLE_CLAIM="groups"  # tai "roles" riippuen palveluntarjoajastasi
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Sisäänrakennettu palveluntarjoaja (Google)

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Useita palveluntarjoajia

Voit ottaa käyttöön useita OIDC-palveluntarjoajia samanaikaisesti:

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Mukautettu palveluntarjoaja
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Yrityksen SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Yhteisön tekemä OIDC-asennusopas Gramps Webille on saatavilla [virallisella Authelia-dokumentaatiosivustolla](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Suurin osa Keycloakin konfiguraatiosta voidaan jättää oletusasetuksiin (*Asiakas → Luo asiakas → Asiakasautentikointi PÄÄLLÄ*). On muutamia poikkeuksia:

1. **OpenID-alue** – `openid`-aluetta ei ole oletuksena mukana kaikissa Keycloak-versioissa. Ongelmien välttämiseksi lisää se manuaalisesti: *Asiakas → [Gramps-asiakas] → Asiakasalueet → Lisää alue → Nimi: `openid` → Aseta oletukseksi.*
2. **Roolit** – Roolit voidaan määrittää joko asiakastasolla tai globaalisti per alue.

    * Jos käytät asiakasrooleja, aseta `OIDC_ROLE_CLAIM` -konfiguraatioasetukseksi: `resource_access.[gramps-client-name].roles`
    * Jotta roolit näkyisivät Grampsille, siirry *Asiakasalueet* (ylätason osio, ei tietyn asiakkaan alla), sitten: *Roolit → Mapperit → asiakasroolit → Lisää käyttäjätietoihin → PÄÄLLÄ.*
