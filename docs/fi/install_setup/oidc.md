# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, joka mahdollistaa käyttäjien kirjautumisen ulkoisten identiteettipalveluntarjoajien avulla. Tämä sisältää sisäänrakennetut palveluntarjoajat Google ja Microsoft sekä mukautetut OIDC-palveluntarjoajat kuten Keycloak, Authentik ja Authelia.

!!! warning "GitHubia OIDC-palveluntarjoajana ei enää tueta"
    Jos sinulla on asetettuna `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` aikaisemmasta versiosta, poista ne – niitä ei enää oteta huomioon, ja käyttäjät, jotka ovat aiemmin kirjautuneet GitHubin kautta, eivät voi enää kirjautua tällä tavalla. GitHub on OAuth 2.0 -palveluntarjoaja, ei OpenID Connect -palveluntarjoaja, eikä se koskaan palauttanut väitettä, johon Gramps Web luottaa identiteetissä, joten se ei ollut koskaan täysin luotettava.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalveluntarjoajien käytön käyttäjätodennuksessa
- Useiden todennuspalveluntarjoajien tukemisen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Web -käyttäjärooleihin
- Yksinkertaisen kirjautumisen (SSO) ja yksinkertaisen uloskirjautumisen toteuttamisen
- Paikallisen käyttäjänimen/salasana-todennuksen valinnaisen poistamisen käytöstä

## Konfigurointi

OIDC-todennuksen käyttöönotto edellyttää, että määrität asianmukaiset asetukset Gramps Web -konfiguraatiotiedostossasi tai ympäristömuuttujissa. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo saatavilla olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista lisätä jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfiguraatiotiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) -sivulta lisätietoja.

### Sisäänrakennetut palveluntarjoajat

Gramps Webillä on sisäänrakennettu tuki suosituimmille identiteettipalveluntarjoajille. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`

Voit määrittää useita palveluntarjoajia samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä palveluntarjoajat ovat käytettävissä konfiguraatioarvojen perusteella.

!!! tip "Microsoft: yksittäiset käyttöönotot"
    Sisäänrakennettu Microsoft-palveluntarjoaja käyttää monivuotista `/common`-päätepistettä ja hyväksyy kirjautumisia mistä tahansa Microsoft-tilistä suunnitellusti. Jos haluat sallia vain oman vuokrasi käyttäjät, käytä [mukautettua OIDC-palveluntarjoajaa](#custom-oidc-providers) vuokrallesi spesifisellä myöntäjä-URL-osoitteella, joka pitää myöntäjävalidaation aktiivisena ja rajoittaa kirjautumiset kyseiseen vuokralle.

### Mukautetut OIDC-palveluntarjoajat

Mukautetuille OIDC-palveluntarjoajille (kuten Keycloak, Authentik, Authelia tai yksittäinen Microsoft Entra -vuokra) käytä näitä asetuksia:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ENABLED`        | Boolean, määrittää, otetaanko OIDC-todennus käyttöön. Aseta `True`.   |
| `OIDC_ISSUER`        | Palveluntarjoajasi myöntäjä-URL-osoite. Löydetään `<issuer>/.well-known/openid-configuration`. |
| `OIDC_CLIENT_ID`     | Asiakastunnus OIDC-palveluntarjoajallesi                               |
| `OIDC_CLIENT_SECRET`  | Asiakassalaisuus OIDC-palveluntarjoajallesi                           |
| `OIDC_NAME`          | Mukautettu näyttönimi (valinnainen, oletusarvo "OIDC")                |
| `OIDC_SCOPES`        | OAuth-alueet (valinnainen, oletusarvo "openid email profile")         |
| `OIDC_USERNAME_CLAIM`| Väite, jota käytetään käyttäjänimen luomiseen (valinnainen, oletusarvo "preferred_username") |

### Monipuu-asetukset

Monipuisella palvelimella puu, johon käyttäjä kirjautuu, on tiedettävä ennen kuin Gramps Web ohjaa identiteettipalveluntarjoajaan, joten kirjautuminen alkaa:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` on pakollinen monipuu-asetuksissa; sen jättämättä jättäminen tai olemattoman puun ID:n antaminen epäonnistuttaa kirjautumisen. Yksittäisellä puupalvelimella `tree` on valinnainen, mutta jos se annetaan, sen on vastattava määritettyä `TREE`:tä.

OIDC-identiteetti on sidottu tarkalleen yhteen Gramps Web -tiliin, joka puolestaan kuuluu tarkalleen yhteen puuhun – kirjautuminen eri puuhun epäonnistuu sen sijaan, että tili siirrettäisiin. Ei ole mahdollista liittää yhtä identiteettiä palveluntarjoajalla useisiin tiliin; käyttäjät, jotka tarvitsevat pääsyä useisiin puihin, tarvitsevat erilliset identiteetit palveluntarjoajalla (esim. erilliset käyttäjänimet tai tilit).

!!! warning
    Sivuston ylläpitäjätilillä, jolla ei ole liitettyä puuta (katso [ylläpitäjätilin luominen](../administration/owner.md)), ei voi kirjautua OIDC:n kautta, koska OIDC-kirjautuminen vaatii aina puun. Tällaiset tilit on luotava ja todennettava paikallisella käyttäjänimellä/salasanalla sen sijaan.

## Vaaditut uudelleenohjaus-URI:t

Kun määrität OIDC-palveluntarjoajaasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URI:

**OIDC-palveluntarjoajille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Riippuen palveluntarjoajasi regex-tulkista tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos palveluntarjoajasi vaatii sen (esim. Authentik).

**OIDC-palveluntarjoajille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Puu ei koskaan ole osa uudelleenohjaus-URI:a, edes monipuisilla palvelimilla – se kulkee erikseen istunnossa, koska palveluntarjoajat vaativat, että rekisteröity uudelleenohjaus-URI vastaa tarkasti rekisteröityä.

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai -rooleja identiteettipalveluntarjoajaltasi Gramps Web -käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalveluntarjoajassasi. Roolikartoitus toimii samalla tavalla kaikille palveluntarjoajille, sekä sisäänrakennuille että mukautetuille.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen määrittämiseen:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | Väitteen nimi OIDC-todistuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo "groups". Pistepolut ovat tuettuja, esim. `realm_access.roles`. |
| `OIDC_GROUP_ADMIN`    | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`    | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`   | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`   | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`    | OIDC-palveluntarjoajaltasi tuleva ryhmä/rooli, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

Jos `OIDC_GROUP_*` -asetusta ei ole määritetty lainkaan, roolikartoitus on pois päältä ja rooleja hallitaan manuaalisesti Gramps Webissä; uusia OIDC-tilejä luodaan tällöin pois päältä ja ne on hyväksyttävä olemassa olevan omistajan tai ylläpitäjän toimesta (katso [Ensimmäinen kirjautuminen ja käynnistäminen](#first-login-and-bootstrapping) alla).

Kun roolikartoitus on määritetty, jokaisessa kirjautumisessa:

- Jos rooliväite on läsnä ja käyttäjä kuuluu kartoitettuun ryhmään, hän saa vastaavan roolin.
- Jos rooliväite on läsnä, mutta käyttäjä ei kuulu kartoitettuun ryhmään, hänen roolinsa asetetaan pois päältä. Tämä on oletusarvoinen sulkeutuva tila, ei virhe – Gramps Web ei voi päätellä roolia ryhmälle, jota se ei tunnista.
- Jos rooliväite puuttuu kokonaan tokenista, olemassa oleva rooli pysyy muuttumattomana; uusi tili oletusarvoisesti pysyy pois päältä.

!!! warning "Google ei lähetä ryhmäväitettä"
    Googlen tokenit eivät koskaan sisällä `groups`-väitettä, joten roolikartoituksen ollessa käytössä, Google-kirjautumiset kuuluvat yllä olevaan "väite puuttuu" -tilaan: olemassa olevat käyttäjät säilyttävät roolinsa, mutta uudet Google-käyttäjät luodaan pois päältä ja tarvitsevat manuaalisen hyväksynnän. Pidä tämä mielessä ennen kuin otat roolikartoituksen käyttöön vain toiselle palveluntarjoajalle – se ei itsessään poista olemassa olevia Google-käyttäjiä.

Microsoft Entra palauttaa sovelluksen roolit ja ryhmäjäsenyydet vain ID-tokenissa, ei käyttäjätietopäätepisteestä. Gramps Web yhdistää ID-tokenin väitteet käyttäjätietovastaukseen, jotta `OIDC_ROLE_CLAIM` toimii samalla tavalla kuin muilla palveluntarjoajilla; missä molemmat sisältävät väitteen, käyttäjätietojen arvo on etusijalla.

## Ensimmäinen kirjautuminen ja käynnistäminen

Uudet tilit, jotka on luotu OIDC:n kautta, aloittavat pois päältä, ellei roolikartoitus myönnä niille roolia (katso yllä). Uudessa instanssissa kukaan ei voi hyväksyä pois päältä olevaa tiliä, ja jos `OIDC_DISABLE_LOCAL_AUTH` on myös käytössä, ei ole salasana-kirjautumista, johon turvautua.

!!! warning "Määritä omistaja/ylläpitäjäryhmä ennen ensimmäistä kirjautumista"
    Ennen kuin kukaan kirjautuu OIDC:n kautta ensimmäistä kertaa, määritä `OIDC_GROUP_OWNER` (tai `OIDC_GROUP_ADMIN`) ja varmista, että ensimmäinen käyttäjä kuuluu kyseiseen ryhmään palveluntarjoajalla. Muuten instanssia ei voida käynnistää OIDC:n kautta lainkaan.

## Tilit ja käyttäjänimet

OIDC:n kautta luodut tilit saavat generoitu käyttäjänimen, joka annetaan kerran tilin luomisen yhteydessä eikä sitä muuteta myöhemmissä kirjautumisissa:

- Sisäänrakennetut palveluntarjoajat: `<provider>_<claim value>`, esim. `microsoft_alice@contoso.com`
- Mukautettu palveluntarjoaja: pelkkä väitearvo, esim. `alice`

Numeroinen liite lisätään, jos on törmäys. OIDC:n kautta luodun tilin käyttäjänimeä ei voi myöhemmin muuttaa; sen sijaan koko nimi ja sähköpostiosoite päivitetään jokaisessa kirjautumisessa.

OIDC-kirjautuminen ei koskaan liity olemassa olevaan paikalliseen tiliin, joka sattuu jakamaan sen sähköpostiosoitteen – tämä on tarkoituksellista, koska tilien liittäminen sähköpostin kautta on tilin haltuunotto-uhka. Käyttäjä, jolla on jo paikallinen tili, saa toisen, erillisen tilin ensimmäisellä kerralla, kun hän kirjautuu OIDC:n kautta.

Palveluntarjoajan sähköpostiosoitteet tallennetaan vain, jos palveluntarjoaja merkitsee ne vahvistetuiksi (tai jättää `email_verified`-väitteen kokonaan pois) ja jos osoitetta ei jo käytetä toisella tilillä; muuten kirjautuminen etenee ilman sähköpostiosoitteen tallentamista.

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksinkertaista uloskirjautumista (SSO-ulosskirjautuminen) OIDC-palveluntarjoajille. `GET /api/oidc/logout/` etsii palveluntarjoajan `end_session_endpoint`-päätepisteen ja palauttaa sen `logout_url`-muodossa vastauksessa; Gramps Web -frontend navigoi selaimessa sinne, jotta istunto voidaan todella päättää identiteettipalveluntarjoajalla. `logout_url` on `null`, kun palveluntarjoajalla ei ole `end_session_endpoint`-päätepistettä.

!!! warning "Tokenit eivät vanhene uloskirjautuessa"
    Uloskirjautuminen päättää vain selaimen istunnon; tällä hetkellä ei ole tapaa peruuttaa Gramps Web -tokenia, joka on jo myönnetty. Tokenit pysyvät voimassa, kunnes ne vanhenevat (`JWT_ACCESS_TOKEN_EXPIRES`, oletusarvo 15 minuuttia käyttöoikeustokenille), riippumatta siitä, onko käyttäjä sittemmin kirjautunut ulos Gramps Webistä tai identiteettipalveluntarjoajalta.

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
OIDC_DISABLE_LOCAL_AUTH=True  # Valinnainen: poista käyttäjänimi/salasana-kirjautuminen käytöstä

# Valinnainen: Roolikartoitus OIDC-ryhmistä Grampsin rooleihin
OIDC_ROLE_CLAIM="groups"  # tai "roles" riippuen palveluntarjoajastasi
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä salaista SSL:ää portissa 465
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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Yhteisön tekemä OIDC-asetusten opas Gramps Webille on saatavilla [virallisella Authelia-dokumentaatiosivustolla](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Suurin osa Keycloak-konfiguraatiosta voidaan jättää oletusarvoihinsa (*Asiakas → Luo asiakas → Asiakastodennus PÄÄLLÄ*). On kuitenkin muutamia poikkeuksia:

1. **OpenID-alue** – `openid`-aluetta ei oletuksena sisällytetä kaikkiin Keycloak-versioihin. Ongelmien välttämiseksi lisää se manuaalisesti: *Asiakas → [Gramps-asiakas] → Asiakasalueet → Lisää alue → Nimi: `openid` → Aseta oletukseksi.*
2. **Roolit** – Roolit voidaan määrittää joko asiakastasolla tai globaalisti per alue.

    * Jos käytät asiakasrooleja, aseta `OIDC_ROLE_CLAIM` -konfiguraatioasetukseksi: `resource_access.[gramps-client-name].roles`
    * Jotta roolit näkyvät Grampsille, siirry *Asiakasalueet* (ylätason osio, ei tietyn asiakkaan alla), sitten: *Roolit → Mapperit → asiakasroolit → Lisää käyttäjätietoihin → PÄÄLLÄ.*
