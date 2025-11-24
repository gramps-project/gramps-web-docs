# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, jolloin käyttäjät voivat kirjautua sisään käyttäen ulkoisia identiteettipalveluja. Tämä sisältää sekä suosittuja palveluja kuten Google, Microsoft ja GitHub, että mukautettuja OIDC-palveluja kuten Keycloak, Authentik ja muita.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalvelujen käyttäminen käyttäjätodennuksessa
- Useiden todennuspalvelujen tukeminen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Webin käyttäjärooleihin
- Yksinkertaisen sisäänkirjautumisen (SSO) ja yksinkertaisen uloskirjautumisen toteuttamisen
- Paikallisen käyttäjänimen/salasanan todennuksen valinnaisen poistamisen käytöstä

## Konfigurointi

OIDC-todennuksen mahdollistamiseksi sinun on määritettävä asianmukaiset asetukset Gramps Webin konfiguraatiotiedostossa tai ympäristömuuttujissa. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo käytettävissä olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista lisätä jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfiguraatiotiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) -sivulta lisätietoja.

### Sisäänrakennetut palvelut

Gramps Webillä on sisäänrakennettu tuki suosituimmille identiteettipalveluille. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` ja `OIDC_GITHUB_CLIENT_SECRET`

Voit määrittää useita palveluja samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä palvelut ovat käytettävissä konfiguraatiotietojen perusteella.

### Mukautetut OIDC-palvelut

Mukautettuja OIDC-palveluja (kuten Keycloak, Authentik tai mikä tahansa standardin OIDC-yhteensopiva palvelu) varten käytä näitä asetuksia:

| Avain               | Kuvaus                                                       |
|---------------------|-------------------------------------------------------------|
| `OIDC_ENABLED`      | Boolean, onko OIDC-todennus käytössä. Aseta arvoon `True`. |
| `OIDC_ISSUER`       | Palvelusi myöntäjän URL-osoite                             |
| `OIDC_CLIENT_ID`    | Asiakastunnus OIDC-palvelullesi                            |
| `OIDC_CLIENT_SECRET` | Asiakassalaisuus OIDC-palvelullesi                         |
| `OIDC_NAME`         | Mukautettu näyttönimi (valinnainen, oletusarvo "OIDC")    |
| `OIDC_SCOPES`       | OAuth-alueet (valinnainen, oletusarvo "openid email profile") |

## Vaaditut uudelleenohjaus-URI:t

Kun määrität OIDC-palveluasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URI:

**OIDC-palveluille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Riippuen palvelusi regex-tulkista tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos palvelusi vaatii sen (esim. Authentik).

**OIDC-palveluille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai rooleja identiteettipalvelustasi Gramps Webin käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalvelussasi.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen määrittämiseen:

| Avain                   | Kuvaus                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`      | OIDC-tokenissa olevan vaatimuksen nimi, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo "groups" |
| `OIDC_GROUP_ADMIN`     | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`     | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`    | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`    | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`     | OIDC-palvelustasi tuleva ryhmän/roolin nimi, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

- Jos roolikartoitusta ei ole määritetty (ei asetettu `OIDC_GROUP_*` -muuttujia), olemassa olevat käyttäjäroolit säilytetään
- Käyttäjille annetaan korkein rooli, johon heillä on oikeus ryhmän jäsenyyden perusteella
- Roolikartoitus on oletusarvoisesti kirjainkooltaan herkkä (riippuu OIDC-palvelustasi)

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksinkertaista uloskirjautumista (SSO-ulosskirjautuminen) OIDC-palveluille. Kun käyttäjä kirjautuu ulos Gramps Webistä OIDC:n kautta, heidät ohjataan automaattisesti identiteettipalvelun uloskirjautumissivulle, jos palvelu tukee `end_session_endpoint` -pistettä.

### Takakanavan uloskirjautuminen

Gramps Web toteuttaa OpenID Connect Back-Channel Logout -määritelmän. Tämä mahdollistaa identiteettipalvelujen ilmoittaa Gramps Webille, kun käyttäjä kirjautuu ulos toisesta sovelluksesta tai identiteettipalvelusta itsestään.

#### Konfigurointi

Määrittääksesi takakanavan uloskirjautumisen identiteettipalvelusi kanssa:

1. **Rekisteröi takakanavan uloskirjautumispiste** identiteettipalvelusi asiakaskonfiguraatiossa:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Määritä palvelusi** lähettämään uloskirjautumisilmoituksia. Tarkat vaiheet riippuvat palvelustasi:

   **Keycloak:**

   - Siirry asiakaskonfiguraatiossa kohtaan "Asetukset"
   - Aseta "Takakanavan uloskirjautumis-URL" arvoksi `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Ota käyttöön "Takakanavan uloskirjautumisen istunto vaaditaan", jos haluat istuntopohjaisen uloskirjautumisen

   **Authentik:**

   - Lisää palvelusi konfiguraatiossa takakanavan uloskirjautumis-URL
   - Varmista, että palvelu on määritetty lähettämään uloskirjautumistunnuksia

!!! warning "Tokenin vanheneminen"
    Koska JWT-tunnusten tilattomuus, takakanavan uloskirjautuminen kirjaa tällä hetkellä uloskirjautumistapahtuman, mutta ei voi välittömästi peruuttaa jo myönnettyjä JWT-tunnuksia. Tunnukset pysyvät voimassa, kunnes ne vanhenevat (oletusarvo: 15 minuuttia käyttöoikeustunnuksille).

    Parannetun turvallisuuden vuoksi harkitse:

    - JWT-tunnusten vanhenemisaikojen lyhentämistä (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Käyttäjien kouluttamista kirjautumaan ulos manuaalisesti Gramps Webistä, kun he kirjautuvat ulos identiteettipalvelustaan

!!! tip "Kuinka se toimii"
    Kun käyttäjä kirjautuu ulos identiteettipalvelustasi tai muusta sovelluksesta:

    1. Palvelu lähettää `logout_token` JWT:n Gramps Webin takakanavan uloskirjautumispisteeseen
    2. Gramps Web validoi tunnuksen ja kirjaa uloskirjautumistapahtuman
    3. Uloskirjautumistunnuksen JTI lisätään estolistalle estämään toistohyökkäykset
    4. Kaikki uudet API-pyynnöt käyttäjän JWT:llä hylätään, kun tunnukset vanhenevat

## Esimerkkikonfiguraatiot

### Mukautettu OIDC-palvelu (Keycloak)

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Mukautettu OIDC-konfigurointi
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Perhe SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Valinnainen: ohjaa automaattisesti SSO-kirjautumiseen
OIDC_DISABLE_LOCAL_AUTH=True  # Valinnainen: poista käyttäjänimi/salasana -kirjautuminen käytöstä

# Valinnainen: Roolikartoitus OIDC-ryhmistä Grampsin rooleihin
OIDC_ROLE_CLAIM="groups"  # tai "roles" riippuen palvelustasi
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

### Sisäänrakennettu palvelu (Google)

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Useita palveluja

Voit ottaa käyttöön useita OIDC-palveluja samanaikaisesti:

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Mukautettu palvelu
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Yritys SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Yhteisön tekemä OIDC-asennusopas Gramps Webille on saatavilla [virallisella Authelia-dokumentaatiosivustolla](https://www.authelia.com/integration/openid-connect/clients/gramps/).
