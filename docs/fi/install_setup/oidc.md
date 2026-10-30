# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, joka mahdollistaa käyttäjien kirjautuvan sisään ulkoisten identiteettipalveluntarjoajien avulla. Tämä sisältää sisäänrakennetut tarjoajat Google ja Microsoft sekä mukautetut OIDC-tarjoajat, kuten Keycloak, Authentik ja Authelia.

!!! warning "GitHubia OIDC-tarjoajana ei enää tueta"
    Jos sinulla on asetettu `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` aikaisemmasta versiosta, poista ne – ne on nyt ohitettu, ja käyttäjät, jotka aiemmin kirjautuivat GitHubin kautta, eivät voi enää kirjautua tällä tavalla. GitHub on OAuth 2.0 -tarjoaja, ei OpenID Connect -tarjoaja, eikä se koskaan palauttanut väitettä, johon Gramps Web luottaa identiteetissä, joten se ei ollut koskaan täysin luotettava.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalveluntarjoajien käytön käyttäjätodennuksessa
- Useiden todennuspalveluntarjoajien tukemisen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Webin käyttäjärooleihin
- Yksinkertaisen sisäänkirjautumisen (SSO) ja yksinkertaisen uloskirjautumisen toteuttamisen
- Valinnaisesti paikallisen käyttäjätunnuksen/salasanan todennuksen poistamisen käytöstä

## Konfigurointi

OIDC-todennuksen käyttöönotto edellyttää, että määrität asianmukaiset asetukset Gramps Webin konfiguraatiotiedostoon tai ympäristömuuttujiin. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo käytettävissä olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista lisätä jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfiguraatiotiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) lisätietoja varten.

### Sisäänrakennetut tarjoajat

Gramps Web tukee sisäänrakennettuja suosittuja identiteettipalveluntarjoajia. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`

Voit konfiguroida useita tarjoajia samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä tarjoajat ovat käytettävissä konfiguraatioväliarvojen perusteella.

!!! tip "Microsoft: yksittäiset käyttöönotot"
    Sisäänrakennettu Microsoft-tarjoaja käyttää monikäyttäjäistä `/common`-päätepistettä ja hyväksyy kirjautumiset mistä tahansa Microsoft-tilistä suunnitellusti. Jos haluat sallia vain oman vuokralaistasi tulevat käyttäjät, käytä [mukautettua OIDC-tarjoajaa](#custom-oidc-providers) vuokralaistasi spesifisellä myöntäjä-URL:lla, mikä pitää myöntäjän vahvistuksen aktiivisena ja rajoittaa kirjautumiset kyseiseen vuokralaiseen.

### Mukautetut OIDC-tarjoajat

Mukautettuja OIDC-tarjoajia (kuten Keycloak, Authentik, Authelia tai yksittäinen Microsoft Entra -vuokralainen) varten käytä näitä asetuksia:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ENABLED`        | Boolean, onko OIDC-todennus käytössä. Aseta arvoksi `True`.           |
| `OIDC_ISSUER`        | Tarjoajan myöntäjä-URL. Löydetään `<issuer>/.well-known/openid-configuration`. |
| `OIDC_CLIENT_ID`      | Asiakastunnus OIDC-tarjoajallesi                                      |
| `OIDC_CLIENT_SECRET`  | Asiakassalaisuus OIDC-tarjoajallesi                                   |
| `OIDC_NAME`           | Mukautettu näyttönimi (valinnainen, oletusarvo "OIDC")                |
| `OIDC_SCOPES`         | OAuth-alueet (valinnainen, oletusarvo "openid email profile")         |
| `OIDC_USERNAME_CLAIM` | Väite, jota käytetään käyttäjätunnuksen luomiseen (valinnainen, oletusarvo "preferred_username") |
| `OIDC_PKCE`           | Käytetäänkö PKCE:tä, katso [PKCE](#pkce) (valinnainen, otetaan automaattisesti käyttöön, jos tarjoaja tukee sitä) |

### PKCE

Gramps Web API 3.23:sta alkaen Gramps Web tukee [PKCE:tä](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256`-menetelmä) valtuutuskoodin virrassa. Jotkut identiteettipalveluntarjoajat, kuten Pocket ID, voidaan konfiguroida *vaatimaan* PKCE:tä asiakkaalta ja hylkäämään kirjautumiset, jotka eivät käytä sitä. Vanhemmat versiot Gramps Web API:sta eivät koskaan käytä PKCE:tä, joten kirjautumiset tällaisella asiakkaalla epäonnistuvat.

PKCE:n käyttö päätetään kirjautumisen yhteydessä seuraavasti:

- Jos `OIDC_PKCE` on asetettu arvoon `True`, PKCE:tä käytetään.
- Jos `OIDC_PKCE` on asetettu arvoon `False`, PKCE:tä ei käytetä, vaikka tarjoaja tukisi sitä.
- Jos `OIDC_PKCE` ei ole asetettu tai se on asetettu mutta tyhjää, PKCE:tä käytetään, jos tarjoajan löytöasiakirja (`/.well-known/openid-configuration`) listaa `S256` arvossa `code_challenge_methods_supported`, eikä sitä käytetä muuten.

Useimmissa asetuksissa sinun ei tarvitse asettaa mitään. Aseta `OIDC_PKCE` arvoon `True`, jos tarjoajasi vaatii PKCE:tä mutta ei mainitse `S256`:ta löytöasiakirjassaan, ja arvoon `False`, jos tarjoajasi mainitsee `S256`:n mutta käsittelee sen väärin. Ympäristömuuttujina boolean-arvojen on oltava pieniä kirjaimia (`GRAMPSWEB_OIDC_PKCE=true`), katso [Konfiguraatio](configuration.md).

Sisäänrakennettujen tarjoajien osalta vastaavat vaihtoehdot ovat `OIDC_GOOGLE_PKCE` ja `OIDC_MICROSOFT_PKCE`.

PKCE-koodin vahvistin säilytetään käyttäjän istunnossa uudelleenohjauksen ja palautteen välillä, joten tämä ei vaadi muutoksia uudelleenohjaus-URI:hin.

### Monipuinen palvelin

Monipuolisella palvelimella puu, johon käyttäjä kirjautuu, on tiedettävä ennen kuin Gramps Web ohjaa identiteettipalveluntarjoajaan, joten kirjautuminen alkaa:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` on pakollinen monipuolisissa asetuksissa; sen poistaminen tai olemattoman puun ID:n antaminen epäonnistuttaa kirjautumisen. Yksittäisessä puupalvelimessa `tree` on valinnainen, mutta jos se annetaan, sen on vastattava määritettyä `TREE`:ä.

OIDC-identiteetti on sidottu tarkalleen yhteen Gramps Web -tiliin, joka puolestaan kuuluu tarkalleen yhteen puuhun – kirjautuminen eri puuhun epäonnistuu sen sijaan, että tili siirtyisi. Yhtä identiteettiä tarjoajalla ei voi liittää useisiin tiliin; käyttäjät, jotka tarvitsevat pääsyä useisiin puihin, tarvitsevat erilliset identiteetit tarjoajalla (esim. erilliset käyttäjätunnukset tai tilit).

!!! warning
    Sivuston ylläpitäjätili, jolla ei ole liitettyä puuta (katso [ylläpitäjätilin luominen](../administration/owner.md)), ei voi kirjautua OIDC:n kautta, koska OIDC-kirjautuminen vaatii aina puun. Tällaiset tilit on luotava ja todennettava paikallisella käyttäjätunnuksella/salasanalla.

## Vaaditut uudelleenohjaus-URI:t

Kun konfiguroit OIDC-tarjoajaasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URI:

**OIDC-tarjoajille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Riippuen tarjoajasi regex-tulkista tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos tarjoajasi vaatii sitä (esim. Authentik).

**OIDC-tarjoajille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Puu ei koskaan ole osa uudelleenohjaus-URI:a, edes monipuolisilla palvelimilla – se kulkee erikseen istunnossa, koska tarjoajat vaativat, että uudelleenohjaus-URI vastaa tarkasti rekisteröityä.

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai -rooleja identiteettipalveluntarjoajaltasi Gramps Webin käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalveluntarjoajassasi. Roolikartoitus toimii samalla tavalla kaikilla tarjoajilla, sekä sisäänrakennetuilla että mukautetuilla.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen konfiguroimiseen:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | Väitteen nimi OIDC-todistuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo "groups". Tuetut pisteet, esim. `realm_access.roles`. |
| `OIDC_GROUP_ADMIN`    | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`    | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`   | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`   | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`    | Ryhmän/roolin nimi OIDC-tarjoajaltasi, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

Jos mitään `OIDC_GROUP_*` -asetusta ei ole määritetty, roolikartoitus on pois päältä ja roolit hallitaan manuaalisesti Gramps Webissä; uusia OIDC-tilejä luodaan sitten pois päältä ja niiden on saatava hyväksyntä olemassa olevalta omistajalta tai ylläpitäjältä (katso [Ensimmäinen kirjautuminen ja käynnistäminen](#first-login-and-bootstrapping) alla).

Kun roolikartoitus on määritetty, jokaisessa kirjautumisessa:

- Jos rooliväite on läsnä ja käyttäjä kuuluu kartoitettuun ryhmään, hän saa vastaavan roolin.
- Jos rooliväite on läsnä mutta käyttäjä ei kuulu kartoitettuun ryhmään, hänen roolinsa asetetaan pois päältä. Tämä on oletusarvoinen sulkeva virhe, ei virhe – Gramps Web ei voi päätellä roolia ryhmälle, jota se ei tunnista.
- Jos rooliväite puuttuu kokonaan todistuksesta, olemassa olevaa roolia ei muuteta; uusi tili on silti oletusarvoisesti pois päältä.

!!! warning "Google ei lähetä ryhmiä koskevaa väitettä"
    Googlen tokenit eivät koskaan sisällä `groups`-väitettä, joten roolikartoituksen ollessa käytössä Google-kirjautumiset kuuluvat yllä olevaan "väite puuttuu": olemassa olevat käyttäjät säilyttävät roolinsa, mutta uudet Google-käyttäjät luodaan pois päältä ja tarvitsevat manuaalista hyväksyntää. Pidä tämä mielessä ennen kuin otat roolikartoituksen käyttöön vain toista tarjoajaa varten – se ei itsessään poista olemassa olevia Google-käyttäjiä.

Microsoft Entra palauttaa sovellustyöt ja ryhmän jäsenyydet vain ID-tokenissa, ei käyttäjätieto-päätepisteestä. Gramps Web yhdistää ID-tokenin väitteet käyttäjätieto-vastaukseen, jotta `OIDC_ROLE_CLAIM` toimii samalla tavalla kuin muilla tarjoajilla; missä molemmat sisältävät väitteen, käyttäjätieto-arvo on ensisijainen.

## Ensimmäinen kirjautuminen ja käynnistäminen

Uudet tilit, jotka on luotu OIDC:n kautta, alkavat olla pois päältä, ellei roolikartoitus myönnä niille roolia (katso yllä). Uudessa instanssissa kukaan ei voi hyväksyä pois päältä olevaa tiliä, ja jos `OIDC_DISABLE_LOCAL_AUTH` on myös käytössä, ei ole salasanaa, johon turvautua.

!!! warning "Määritä omistaja/ylläpitäjäryhmä ennen ensimmäistä kirjautumista"
    Ennen kuin kukaan kirjautuu OIDC:n kautta ensimmäistä kertaa, aseta `OIDC_GROUP_OWNER` (tai `OIDC_GROUP_ADMIN`) ja varmista, että ensimmäinen käyttäjä kuuluu kyseiseen ryhmään tarjoajalla. Muuten instanssia ei voida käynnistää OIDC:n kautta lainkaan.

## Tilit ja käyttäjätunnukset

OIDC:n kautta luodut tilit saavat luodun käyttäjätunnuksen, joka annetaan kerran tilin luomisen yhteydessä eikä sitä muuteta myöhemmillä kirjautumisilla:

- Sisäänrakennetut tarjoajat: `<provider>_<claim value>`, esim. `microsoft_alice@contoso.com`
- Mukautettu tarjoaja: pelkkä väitearvo, esim. `alice`

Numeroinen liite lisätään, jos on törmäys. OIDC:n kautta luodun tilin käyttäjätunnusta ei voi myöhemmin nimetä uudelleen; sen sijaan koko nimi ja sähköpostiosoite päivitetään jokaisessa kirjautumisessa.

OIDC-kirjautuminen ei koskaan liity olemassa olevaan paikalliseen tiliin, joka sattuu jakamaan sen sähköpostiosoitteen – tämä on tahallista, koska tilien yhdistäminen sähköpostin perusteella on tilin kaappaamisen vektori. Käyttäjä, jolla on jo paikallinen tili, saa toisen, erillisen tilin ensimmäisellä kerralla, kun hän kirjautuu OIDC:n kautta, ellei hän ensin yhdistä tarjoajaa tiliinsä.

Gramps Web API 3.24:stä alkaen käyttäjät voivat yhdistää OIDC-identiteettejä olemassa olevaan tiliinsä ja listata ja irrottaa niitä [Käyttäjäasetukset > Liitetyt kirjautumistavat](../user-guide/settings.md#linked-sign-in-methods) -kohdassa. Yhdistäminen vaatii äskettäisen kirjautumisen ja vahvistetaan käyttäjän omalla tokenilla, joten se toimii myös silloin, kun etupääte on eri alkuperä kuin API. Identiteetti voi kuulua vain yhteen tiliin; yhdistääkseen sellaisen, jolla on jo oma tili, ylläpitäjän on ensin poistettava se tili (sen muokkaukset säilyvät, mutta tarkistus historia ei enää näytä sen nimeä). Viimeinen yhdistetty identiteetti voidaan irrottaa vain tilin nykyisellä salasanalla, eikä lainkaan, jos `OIDC_DISABLE_LOCAL_AUTH` on asetettu.

Tarjoajalta saadut sähköpostiosoitteet tallennetaan vain, jos tarjoaja merkitsee ne vahvistetuiksi (tai jättää `email_verified`-väitteen kokonaan pois); muuten kirjautuminen etenee tallentamatta sähköpostiosoitetta. Koska sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (koska Gramps Web API 3.22), osoite tallennetaan, vaikka toinen tili käyttäisi sitä jo.

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksinkertaista uloskirjautumista (SSO-ulosskirjautumista) OIDC-tarjoajille. `GET /api/oidc/logout/` etsii tarjoajan `end_session_endpoint` ja palauttaa sen `logout_url`-vastauksena; Gramps Webin etupääte navigoi selaimessa sinne, jotta istunto päättyy todella identiteettipalveluntarjoajalla. `logout_url` on `null`, kun tarjoajalla ei ole `end_session_endpoint`-päätepistettä.

!!! warning "Tokenit eivät vanhene uloskirjautuessa"
    Uloskirjautuminen päättää vain selainistunnon; tällä hetkellä ei ole tapaa peruuttaa jo myönnettyä Gramps Web -tokenia. Tokenit pysyvät voimassa, kunnes ne vanhenevat (`JWT_ACCESS_TOKEN_EXPIRES`, oletusarvo 15 minuuttia pääsytokenille), riippumatta siitä, onko käyttäjä sen jälkeen kirjautunut ulos Gramps Webistä tai identiteettipalveluntarjoajalta.

## Vianetsintä

Aloita kohdasta, jossa kirjautuminen pysähtyy, ja seuraa haaraa. Gramps Web kirjaa epäonnistuneen palautteen syyn (etsi `OIDC callback error for provider` palvelinlokista), joka on yleensä tarkempi kuin selainikkunassa näkyvä viesti.

**1. Onko kirjautumispainike puuttuu?**

- Tarkista `<BASE_URL>/api/oidc/config/`. Jos `enabled` on `false` tai `providers` on tyhjää, OIDC:tä ei ole konfiguroitu: `OIDC_ENABLED` on asetettava arvoon `True`, ja mukautetun tarjoajan on oltava sekä `OIDC_ISSUER` että `OIDC_CLIENT_ID`.
- Sisäänrakennettu tarjoaja (Google, Microsoft) on rekisteröity vain, jos sekä sen asiakastunnus että asiakassalaisuus on asetettu.
- Tarkista palvelinlokista käynnistyksen yhteydessä `Could not load discovery document`. Tämä tarkoittaa, että palvelin ei voinut tavoittaa `<issuer>/.well-known/openid-configuration` (tai `OIDC_OPENID_CONFIG_URL`). Se yrittää uudelleen ensimmäisellä käytöllä, mutta Gramps Web -kontin on pystyttävä ratkaisemaan ja tavoittamaan myöntäjä-URL itse, ei vain selaimesi.

**2. Saako selain virheen heti, kun se lähetetään tarjoajalle?**

Virhe näkyy identiteettipalveluntarjoajalta ennen kuin kirjaudut sisään.

- *"uudelleenohjaus-URI:n yhteensopimattomuus"* (tai vastaava): tarjoajalla rekisteröidyn uudelleenohjaus-URI:n on vastattava tarkasti, mukaan lukien protokolla, isäntä, portti ja tarjoajan ID. Katso [Vaaditut uudelleenohjaus-URI:t](#required-redirect-uris). Huomaa, että se on rakennettu `BASE_URL`:sta, joten väärä `BASE_URL` antaa väärän uudelleenohjaus-URI:n.
- *PKCE-virhe* (esimerkiksi `invalid_request`, "koodivaatimus vaaditaan" tai puuttuva `code_challenge`-parametri): tarjoaja vaatii PKCE:tä, mutta Gramps Web ei lähettänyt sitä. Siirry [PKCE-haaralle](#pkce-branch) alla.

**3. Hyväksyykö tarjoaja kirjautumisen, mutta Gramps Web näyttää sitten virheen?**

- *`mismatching_state`, tai virhe mainitsee istunnon tai tilan*: selain ei lähettänyt takaisin istuntokeksejä, jotka Gramps Web asetti, kun kirjautuminen alkoi. Tämä keksi sisältää myös PKCE-koodin vahvistimen. Varmista, että selaimen osoite vastaa `BASE_URL`:ia (sama protokolla ja isäntä), että käänteinen välityspalvelin välittää keksejä ja alkuperäisen isännän läpi, ja että kirjautuminen aloitetaan ja päätetään samassa selainvälilehdessä tai ikkunassa.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: tarkista palvelinlokista taustasyy. Yleisiä syitä ovat väärä asiakassalaisuus, myöntäjä-URL, joka ei vastaa tokenien `iss`-väitettä, ja tarjoajan palauttama virhe palautteeseen (esimerkiksi PKCE, katso alla).
- *Liian monta yritystä*: kirjautumis- ja palautepisteet ovat nopeusrajoitettuja (5 pyyntöä minuutissa). Odota minuutti ja yritä uudelleen.

**4. Onko kirjautuminen onnistunut, mutta näet "Tili tarkastuksessa" tai et voi tehdä mitään?**

Uudet tilit luodaan pois päältä, ellei roolikartoitus myönnä niille roolia. Katso [Ensimmäinen kirjautuminen ja käynnistäminen](#first-login-and-bootstrapping) ja [Roolikartoituksen käyttäytyminen](#role-mapping-behavior). Ylläpitäjä voi myös aktivoida tilin kohdassa Asetukset > Hallinta > Hallitse käyttäjiä.

### PKCE-haara

Gramps Web päättää, käytetäänkö PKCE:tä, kun kirjautuminen alkaa (katso [PKCE](#pkce)). Selvittääksesi, mitä tapahtui asetuksellesi, käy läpi nämä kysymykset järjestyksessä:

1. **Onko `OIDC_PKCE` asetettu?** (Sisäänrakennettujen tarjoajien osalta `OIDC_GOOGLE_PKCE` tai `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE:tä käytetään. Siirry kysymykseen 3.
    - `False`: PKCE on tahallisesti pois päältä, ja tarjoajan löytöasiakirjaa ohitetaan. Jos tarjoajasi vaatii PKCE:tä, poista asetus tai aseta se arvoon `True`.
    - Ei asetettu tai tyhjää: jatka kysymykseen 2.
2. **Sisältääkö löytöasiakirja `S256`:n?** Avaa `<issuer>/.well-known/openid-configuration` ja etsi `S256` arvosta `code_challenge_methods_supported`.
    - Kyllä: PKCE:tä käytetään automaattisesti. Jatka kysymykseen 3.
    - Ei, tai kenttä puuttuu: PKCE:tä **ei** käytetä. Aseta `OIDC_PKCE` arvoon `True`, jos tarjoajasi vaatii sitä. Tarkista myös palvelinlokista `Could not check the provider for PKCE support`, mikä tarkoittaa, että löytöasiakirjaa ei voitu noutaa ja PKCE:tä ei siksi otettu käyttöön.
3. **Lähetettiinkö PKCE todella?** Aloita kirjautuminen ja katso tarjoajan kirjautumissivun osoitetta (tai ensimmäistä uudelleenohjausta selaimesi verkkovälilehdessä). Sen pitäisi sisältää `code_challenge=` ja `code_challenge_method=S256`.
    - Läsnä, mutta kirjautuminen epäonnistuu silti palautteessa: tarjoaja hylkäsi koodin vahvistimen. Istuntokeksi on saattanut kadota uudelleenohjauksen ja palautteen välillä (katso haara 3 yllä), tai tarjoaja ei tue `S256`:ta, jolloin aseta `OIDC_PKCE` arvoon `False`, jos tarjoaja ei vaadi PKCE:tä.
    - Poissa: yllä olevia asetuksia ei sovellettu. Tarkista, että ympäristömuuttujalla on oikea etuliite ja pieni kirjainarvo (esimerkiksi `GRAMPSWEB_OIDC_PKCE=true` Dockerissa; `True` ei lueta boolean-arvona), käynnistä palvelin uudelleen ja tarkista konfiguraatio uudelleen.

!!! note
    Kun PKCE on otettu käyttöön tarjoajalla *valinnaisena* tai ei lainkaan, kirjautumiset toimivat riippumatta siitä, lähettääkö Gramps Web haasteen vai ei. Vain tarjoajat (tai asiakkaat), jotka on määritetty *vaatimaan* PKCE:tä, tekevät tästä asetuksesta merkityksellisen.

## Esimerkkikonfiguraatiot

### Mukautettu OIDC-tarjoaja (Keycloak)

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
OIDC_DISABLE_LOCAL_AUTH=True  # Valinnainen: poista käyttäjätunnus/salasana -kirjautuminen käytöstä

# Valinnainen: Roolikartoitus OIDC-ryhmistä Grampsin rooleihin
OIDC_ROLE_CLAIM="groups"  # tai "roles" riippuen tarjoajastasi
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portissa 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP-salasana
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Sisäänrakennettu tarjoaja (Google)

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Useita tarjoajia

Voit ottaa käyttöön useita OIDC-tarjoajia samanaikaisesti:

```python
TREE="Perheeni puu"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # salainen avain
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Mukautettu tarjoaja
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

### Pocket ID

Luo OIDC-asiakas Pocket ID:ssä uudelleenohjaus-URI:lla `<BASE_URL>/api/oidc/callback/custom` (katso [Vaaditut uudelleenohjaus-URI:t](#required-redirect-uris)). Jos otat käyttöön "Vaadi PKCE" asiakkaalle, ei tarvita lisäkonfigurointia Gramps Webissä, koska Pocket ID mainitsee PKCE-tuen löytöasiakirjassaan. Konfiguroi sitten:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Yhteisön tekemä OIDC-asetusten opas Gramps Webille on saatavilla [virallisella Authelia-dokumentaatiosivustolla](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Suurin osa Keycloak-konfiguraatiosta voidaan jättää oletusarvoihinsa (*Asiakas → Luo asiakas → Asiakasautentikointi PÄÄLLÄ*).
On muutamia poikkeuksia:

1. **OpenID-alue** – `openid`-aluetta ei oletusarvoisesti sisällytetä kaikkiin Keycloak-versioihin. Ongelmien välttämiseksi lisää se manuaalisesti: *Asiakas → [Gramps-asiakas] → Asiakasalueet → Lisää alue → Nimi: `openid` → Aseta oletusarvoksi.*
2. **Roolit** – Roolit voidaan määrittää joko asiakastasolla tai globaalisti per alue.

    * Jos käytät asiakasrooleja, aseta `OIDC_ROLE_CLAIM` -konfiguraatioarvo: `resource_access.[gramps-client-name].roles`
    * Jotta roolit näkyisivät Grampsille, siirry *Asiakasalueet* (ylätason osio, ei tietyn asiakkaan alla), sitten: *Roolit → Mapperit → asiakasroolit → Lisää käyttäjätietoihin → PÄÄLLÄ.*
