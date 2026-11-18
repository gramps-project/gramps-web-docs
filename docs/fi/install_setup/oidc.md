# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, joka mahdollistaa käyttäjien kirjautuvan sisään käyttäen ulkoisia identiteettipalveluja. Tämä sisältää sisäänrakennetut palveluntarjoajat Google ja Microsoft sekä mukautetut OIDC-palveluntarjoajat, kuten Keycloak, Authentik ja Authelia.

!!! warning "GitHubia OIDC-palveluntarjoajana ei enää tueta"
    Jos sinulla on asetettuna `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` aikaisemmasta versiosta, poista ne – niitä ei enää oteta huomioon, ja käyttäjät, jotka ovat aiemmin kirjautuneet GitHubin kautta, eivät voi enää kirjautua tällä tavalla. GitHub on OAuth 2.0 -palveluntarjoaja, ei OpenID Connect -palveluntarjoaja, eikä se koskaan palauttanut väitettä, johon Gramps Web luottaa identiteetissä, joten se ei ollut koskaan täysin luotettava.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalvelujen käytön käyttäjätodennuksessa
- Useiden todennuspalveluntarjoajien tukemisen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Web -käyttäjärooleihin
- Yksittäisen sisäänkirjautumisen (SSO) ja yksittäisen uloskirjautumisen toteuttamisen
- Paikallisen käyttäjänimen/salasanan todennuksen valinnaisen poistamisen käytöstä

## Konfigurointi

OIDC-todennuksen mahdollistamiseksi sinun on määritettävä asianmukaiset asetukset Gramps Web -konfiguraatiotiedostossasi tai ympäristömuuttujissa. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo käytettävissä olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista liittää jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfiguraatiotiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) lisätietoja varten.

### Sisäänrakennetut palveluntarjoajat

Gramps Webillä on sisäänrakennettu tuki suosituimmille identiteettipalveluntarjoajille. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`

Voit määrittää useita palveluntarjoajia samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä palveluntarjoajat ovat käytettävissä konfiguraatiotietojen perusteella.

!!! tip "Microsoft: yksittäiset käyttöönotot"
    Sisäänrakennettu Microsoft-palveluntarjoaja käyttää monivuokraista `/common` -päätepistettä ja hyväksyy kirjautumiset mihin tahansa Microsoft-tiliin suunnitellusti. Jos haluat sallia vain oman vuokralaisesi käyttäjät, käytä [mukautettua OIDC-palveluntarjoajaa](#custom-oidc-providers) oman vuokralaisesi erityisellä myöntäjä-URL-osoitteella, joka pitää myöntäjän vahvistamisen aktiivisena ja rajoittaa kirjautumiset kyseiseen vuokralaisiin.

### Mukautetut OIDC-palveluntarjoajat

Mukautettuja OIDC-palveluntarjoajia (kuten Keycloak, Authentik, Authelia tai yksittäinen Microsoft Entra -vuokralainen) varten käytä näitä asetuksia:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ENABLED`        | Boolean, onko OIDC-todennus käytössä. Aseta arvoksi `True`.           |
| `OIDC_ISSUER`        | Palveluntarjoajasi myöntäjä-URL-osoite. Löydetään `<issuer>/.well-known/openid-configuration`. |
| `OIDC_CLIENT_ID`      | Asiakastunnus OIDC-palveluntarjoajallesi                               |
| `OIDC_CLIENT_SECRET`  | Asiakassalaisuus OIDC-palveluntarjoajallesi                           |
| `OIDC_NAME`           | Mukautettu näyttönimi (valinnainen, oletusarvo "OIDC")                 |
| `OIDC_SCOPES`         | OAuth-alueet (valinnainen, oletusarvo "openid email profile")          |
| `OIDC_USERNAME_CLAIM` | Väite, jota käytetään käyttäjänimen luomiseen (valinnainen, oletusarvo "preferred_username") |
| `OIDC_PKCE`           | Käytetäänkö PKCE:tä, katso [PKCE](#pkce) (valinnainen, otetaan automaattisesti käyttöön, jos palveluntarjoaja tukee sitä) |

### PKCE

Gramps Web API 3.23:sta alkaen Gramps Web tukee [PKCE:tä](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256`-menetelmä) valtuutuskoodin virrassa. Jotkut identiteettipalveluntarjoajat, kuten Pocket ID, voidaan määrittää *vaatimaan* PKCE:tä asiakkaalta ja hylkäämään kirjautumiset, jotka eivät käytä sitä. Vanhemmat versiot Gramps Web API:sta eivät koskaan käytä PKCE:tä, joten tällaisella asiakkaalla kirjautumiset epäonnistuvat.

Se, käytetäänkö PKCE:tä, päätetään kirjautumisen yhteydessä seuraavasti:

- Jos `OIDC_PKCE` on asetettu arvoksi `True`, PKCE:tä käytetään.
- Jos `OIDC_PKCE` on asetettu arvoksi `False`, PKCE:tä ei käytetä, vaikka palveluntarjoaja tukisi sitä.
- Jos `OIDC_PKCE` ei ole asetettu tai se on asetettu tyhjäksi, PKCE:tä käytetään, jos palveluntarjoajan löytöasiakirja (`/.well-known/openid-configuration`) listaa `S256` arvona `code_challenge_methods_supported`, eikä sitä käytetä muuten.

Useimmissa asetuksissa sinun ei tarvitse asettaa mitään. Aseta `OIDC_PKCE` arvoksi `True`, jos palveluntarjoajasi vaatii PKCE:tä, mutta ei mainitse `S256`:ta löytöasiakirjassaan, ja arvoksi `False`, jos palveluntarjoajasi mainitsee `S256`:n, mutta käsittelee sen väärin. Ympäristömuuttujina boolean-arvojen on oltava pienillä kirjaimilla (`GRAMPSWEB_OIDC_PKCE=true`), katso [Konfigurointi](configuration.md).

Sisäänrakennetuissa palveluntarjoajissa vastaavat vaihtoehdot ovat `OIDC_GOOGLE_PKCE` ja `OIDC_MICROSOFT_PKCE`.

PKCE-koodin vahvistin säilytetään käyttäjän istunnossa uudelleenohjauksen ja palautteen välillä, joten tämä ei vaadi muutoksia uudelleenohjaus-URL-osoitteisiin.

### Monipuu-asetukset

Monipuisella palvelimella käyttäjä, joka kirjautuu sisään identiteetillä, joka on jo linkitetty Gramps Web -tiliin, kirjautuu kyseisen tilin puuhun, joten tavallinen kirjautumissivu toimii heille.

Luo *uusi* tili OIDC-identiteetillä, Gramps Web tarvitsee tietää, mihin puuhun sen tulisi kuulua. Uusien käyttäjien on siksi aloitettava puun rekisteröintilinkistä (`/register/<tree_id>`, katso [Rekisteröintilinkki](../administration/users.md#registration-link-multi-tree-setup-only)) tai puun kirjautumissivulta (`/login/<tree_id>`). Molemmat tarjoavat määritetyt palveluntarjoajat. Tuntemattomalla identiteetillä kirjautuminen tavalliselta kirjautumissivulta hylätään viestillä, joka osoittaa rekisteröintilinkkiin. Tämä vaatii Gramps Web API 3.25.3:n ja Gramps Web 26.11.2:n tai uudemman.

Kulissien takana kirjautuminen alkaa seuraavasti:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

missä `tree` on valinnainen, ellei uutta tiliä luoda. Puun ID:n antaminen, joka ei ole olemassa, epäonnistuttaa kirjautumisen. Yksittäisellä puupalvelimella `tree` on valinnainen, mutta jos se annetaan, sen on vastattava määritettyä `TREE`:tä.

OIDC-identiteetti on sidottu tarkalleen yhteen Gramps Web -tiliin, joka puolestaan kuuluu tarkalleen yhteen puuhun – kirjautuminen eri puuhun epäonnistuu sen sijaan, että tiliä siirrettäisiin. Yhtä identiteettiä palveluntarjoajalla ei voi linkittää useisiin tiliin; käyttäjät, jotka tarvitsevat pääsyä useisiin puihin, tarvitsevat erilliset identiteetit palveluntarjoajalla (esim. erilliset käyttäjänimet tai tilit).

!!! warning
    Sivuston ylläpitäjätili, jolla ei ole liitettyä puuta (katso [ylläpitäjätilin luominen](../administration/owner.md)), ei voi syntyä OIDC:n kautta, koska OIDC-kirjautumisen kautta luotu tili kuuluu aina puuhun. Luo tällaiset tilit paikallisella käyttäjänimellä ja salasanalla.

### Natiivisovellukset

Natiivisovellukset, kuten Gramps Webin mobiilisovellukset, voivat antaa käyttäjän kirjautua järjestelmän selaimessa ja vastaanottaa tuloksen sovelluksen `https`-linkissä. Gramps Web API 3.26:sta alkaen tämä toimii, jos linkki on lueteltu `OIDC_ALLOWED_REDIRECT_URIS`-asetuksessa, esim.

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

Sovelluksen dokumentaatio kertoo, mikä linkki lisätään. Identiteettipalveluntarjoajalla rekisteröidyt uudelleenohjaus-URL-osoitteet pysyvät samoina.

## Vaaditut uudelleenohjaus-URL-osoitteet

Kun määrität OIDC-palveluntarjoajaasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URL-osoite:

**OIDC-palveluntarjoajille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Riippuen palveluntarjoajasi regex-tulkista tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos palveluntarjoajasi vaatii sitä (esim. Authentik).

**OIDC-palveluntarjoajille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Puu ei koskaan ole osa uudelleenohjaus-URL-osoitetta, edes monipuupalvelimilla – se kulkee erikseen istunnossa, koska palveluntarjoajat vaativat, että uudelleenohjaus-URL-osoitteen on vastattava tarkasti rekisteröityä.

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai -rooleja identiteettipalveluntarjoajaltasi Gramps Web -käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalveluntarjoajassasi. Roolikartoitus toimii samalla tavalla kaikilla palveluntarjoajilla, sekä sisäänrakennetuilla että mukautetuilla.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen määrittämiseen:

| Avain                  | Kuvaus                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | Väitteen nimi OIDC-todistuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletusarvo "groups". Pistepolut ovat tuettuja, esim. `realm_access.roles`. |
| `OIDC_GROUP_ADMIN`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`   | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`   | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`    | Ryhmän/roolin nimi OIDC-palveluntarjoajaltasi, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

Jos mitään `OIDC_GROUP_*` -asetusta ei ole määritetty, roolikartoitus on pois käytöstä ja roolit hallitaan manuaalisesti Gramps Webissä; uusia OIDC-tilejä luodaan tällöin poistettuina ja ne tarvitsevat olemassa olevan omistajan tai ylläpitäjän hyväksynnän (katso [Ensimmäinen kirjautuminen ja käynnistys](#first-login-and-bootstrapping) alla).

Kun roolikartoitus on määritetty, jokaisessa kirjautumisessa:

- Jos rooliväite on läsnä ja käyttäjä kuuluu kartoitettuun ryhmään, hän saa vastaavan roolin.
- Jos rooliväite on läsnä, mutta käyttäjä ei kuulu kartoitettuun ryhmään, hänen roolinsa asetetaan poistettuna. Tämä on oletusarvoinen sulkeva virhe, ei virhe – Gramps Web ei voi päätellä roolia ryhmälle, jota se ei tunnista.
- Jos rooliväite puuttuu kokonaan todistuksesta, olemassa olevaa roolia ei muuteta; uusi tili oletusarvoisesti jää poistettuna.

!!! warning "Google ei lähetä ryhmiä koskevaa väitettä"
    Googlen tokenit eivät koskaan sisällä `groups`-väitettä, joten roolikartoituksen ollessa käytössä Google-kirjautumiset kuuluvat yllä olevaan "väite puuttuu" -kategoriaan: olemassa olevat käyttäjät säilyttävät roolinsa, mutta uudet Google-käyttäjät luodaan poistettuina ja tarvitsevat manuaalista hyväksyntää. Pidä tämä mielessä ennen kuin otat roolikartoituksen käyttöön vain toista palveluntarjoajaa varten – se ei itsessään poista olemassa olevia Google-käyttäjiä.

Microsoft Entra palauttaa sovellustyöt ja ryhmäjäsenyydet vain ID-tokenissa, ei käyttäjätietopäätepisteestä. Gramps Web yhdistää ID-tokenin väitteet käyttäjätietovastaukseen, jotta `OIDC_ROLE_CLAIM` toimii samalla tavalla kuin muilla palveluntarjoajilla; missä molemmat sisältävät väitteen, käyttäjätietojen arvo on ensisijainen.

## Ensimmäinen kirjautuminen ja käynnistys

Uudet OIDC:n kautta luodut tilit alkavat olla poistettuina, ellei roolikartoitus myönnä niille roolia (katso yllä). Uudessa instanssissa kukaan ei voi hyväksyä poistettua tiliä, ja jos `OIDC_DISABLE_LOCAL_AUTH` on myös käytössä, ei ole salasanaa, johon turvautua.

!!! warning "Määritä omistaja/ylläpitäjäryhmä ennen ensimmäistä kirjautumista"
    Ennen kuin kukaan kirjautuu OIDC:n kautta ensimmäistä kertaa, aseta `OIDC_GROUP_OWNER` (tai `OIDC_GROUP_ADMIN`) ja varmista, että ensimmäinen käyttäjä kuuluu kyseiseen ryhmään palveluntarjoajalla. Muuten instanssia ei voida käynnistää OIDC:n kautta lainkaan.

## Tilit ja käyttäjänimet

OIDC:n kautta luoduille tileille annetaan generoitu käyttäjänimi, joka määritetään kerran tilin luomisen yhteydessä eikä sitä muuteta myöhemmillä kirjautumisilla:

- Sisäänrakennetut palveluntarjoajat: `<provider>_<claim value>`, esim. `microsoft_alice@contoso.com`
- Mukautettu palveluntarjoaja: pelkkä väitearvo, esim. `alice`

Numeroinen liite lisätään, jos on yhteensopimattomuus. OIDC:n kautta luodun tilin käyttäjänimeä ei voi muuttaa myöhemmin; sen sijaan koko nimi ja sähköpostiosoite päivitetään jokaisella kirjautumisella.

OIDC-kirjautuminen ei koskaan liity olemassa olevaan paikalliseen tiliin, joka sattuu jakamaan sen sähköpostiosoitteen – tämä on tarkoituksellista, koska tilien yhdistäminen sähköpostin perusteella on tilin kaappaamisen vektori. Käyttäjä, jolla on jo paikallinen tili, saa toisen, erillisen tilin ensimmäisellä kerralla, kun hän kirjautuu OIDC:n kautta, ellei hän ensin yhdistä palveluntarjoajaa tiliinsä.

Gramps Web API 3.24:stä alkaen käyttäjät voivat yhdistää OIDC-identiteettejä olemassa olevaan tiliinsä ja luetella ja irrottaa niitä [Käyttäjäasetukset > Liitetyt kirjautumistavat](../user-guide/settings.md#linked-sign-in-methods) -kohdassa. Yhdistäminen vaatii äskettäisen kirjautumisen ja vahvistetaan käyttäjän omalla tokenilla, joten se toimii myös silloin, kun etupääte on eri alkuperä kuin API. Identiteetti voi kuulua vain yhteen tiliin; yhdistääkseen sellaisen, jolla on jo oma tili, ylläpitäjän on ensin poistettava se tili (sen muokkaukset säilyvät, mutta versiohistoria ei enää näytä sen nimeä). Viimeistä yhdistettyä identiteettiä voidaan irrottaa vain tilin nykyisellä salasanalla, eikä lainkaan, jos `OIDC_DISABLE_LOCAL_AUTH` on asetettu.

Palveluntarjoajan sähköpostiosoitteet tallennetaan vain, jos palveluntarjoaja merkitsee ne vahvistetuiksi (tai jättää `email_verified`-väitteen kokonaan pois); muuten kirjautuminen etenee ilman sähköpostiosoitteen tallentamista. Koska sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (koska Gramps Web API 3.22), osoite tallennetaan, vaikka toinen tili käyttäisi sitä jo.

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksittäistä uloskirjautumista (SSO-ulosskirjautuminen) OIDC-palveluntarjoajille. `GET /api/oidc/logout/` etsii palveluntarjoajan `end_session_endpoint`-päätepisteen ja palauttaa sen `logout_url`-arvona vastauksessa; Gramps Webin etupääte navigoi selaimessa sinne, jotta istunto todella päättyy identiteettipalveluntarjoajalla. `logout_url` on `null`, kun palveluntarjoajalla ei ole `end_session_endpoint`-päätepistettä.

!!! warning "Tokenit eivät vanhene uloskirjautuessa"
    Uloskirjautuminen päättää vain selaimen istunnon; tällä hetkellä ei ole tapaa peruuttaa Gramps Webin tokenia, joka on jo myönnetty. Tokenit pysyvät voimassa, kunnes ne vanhenevat (`JWT_ACCESS_TOKEN_EXPIRES`, oletusarvo 15 minuuttia pääsytokeneille), riippumatta siitä, onko käyttäjä sen jälkeen kirjautunut ulos Gramps Webistä tai identiteettipalveluntarjoajalta.

## Vianetsintä

Aloita kohdasta, jossa kirjautuminen pysähtyy, ja seuraa haaraa. Gramps Web kirjaa epäonnistuneen palautteen syyn (etsi `OIDC callback error for provider` palvelinlokista), joka on yleensä tarkempi kuin selainikkunassa näkyvä viesti.

**1. Puuttuuko kirjautumispainike?**

- Tarkista `<BASE_URL>/api/oidc/config/`. Jos `enabled` on `false` tai `providers` on tyhjää, OIDC:tä ei ole määritetty: `OIDC_ENABLED` on asetettava arvoksi `True`, ja mukautetun palveluntarjoajan on oltava sekä `OIDC_ISSUER` että `OIDC_CLIENT_ID` asetettuna.
- Sisäänrakennettu palveluntarjoaja (Google, Microsoft) on rekisteröity vain, jos sekä sen asiakastunnus että asiakassalaisuus on asetettu.
- Tarkista palvelinlokista käynnistyksen yhteydessä `Could not load discovery document`. Tämä tarkoittaa, että palvelin ei voinut tavoittaa `<issuer>/.well-known/openid-configuration` (tai `OIDC_OPENID_CONFIG_URL`). Se yrittää uudelleen ensimmäisellä käytöllä, mutta Gramps Web -säilön on pystyttävä ratkaisemaan ja saavuttamaan myöntäjä-URL-osoite itse, ei vain selaimesi.

**2. Saako selain virheen heti, kun se lähetetään palveluntarjoajalle?**

Virhe näkyy identiteettipalveluntarjoajalta ennen kuin kirjaudut sisään.

- *"uudelleenohjaus-URL-osoitteen yhteensopimattomuus"* (tai vastaava): palveluntarjoajalla rekisteröity uudelleenohjaus-URL-osoitteen on vastattava tarkasti, mukaan lukien protokolla, isäntä, portti ja palveluntarjoajan ID. Katso [Vaaditut uudelleenohjaus-URL-osoitteet](#required-redirect-uris). Huomaa, että se on rakennettu `BASE_URL`:sta, joten väärä `BASE_URL` antaa väärän uudelleenohjaus-URL-osoitteen.
- *PKCE-virhe* (esimerkiksi `invalid_request`, "koodin haaste vaaditaan" tai puuttuva `code_challenge`-parametri): palveluntarjoaja vaatii PKCE:tä, mutta Gramps Web ei lähettänyt sitä. Siirry [PKCE-haaraan](#pkce-branch) alla.

**3. Hyväksyykö palveluntarjoaja kirjautumisen, mutta Gramps Web näyttää sitten virheen?**

- *`mismatching_state`, tai virhe mainitsee istunnon tai tilan*: selain ei lähettänyt takaisin Gramps Webin asettamaa istuntokekoa, kun kirjautuminen alkoi. Tämä keksi kuljettaa myös PKCE-koodin vahvistinta. Varmista, että selainosoite vastaa `BASE_URL`:ia (sama protokolla ja isäntä), että käänteinen välityspalvelin siirtää keksejä ja alkuperäisen isännän läpi, ja että kirjautuminen aloitetaan ja päätetään samassa selainvälilehdessä tai ikkunassa.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: tarkista palvelinlokista taustasyy. Yleisiä syitä ovat väärä asiakassalaisuus, myöntäjä-URL-osoite, joka ei vastaa tokenien `iss`-väitettä, ja palveluntarjoajan palauttama virhe palautteessa (esimerkiksi PKCE, katso alla).
- *Liian monta yritystä*: kirjautumis- ja palautepisteet ovat nopeusrajoitettuja (5 pyyntöä minuutissa). Odota minuutti ja yritä uudelleen.

**4. Onko kirjautuminen onnistunut, mutta näet "Tili tarkistuksessa" tai et voi tehdä mitään?**

Uudet tilit luodaan poistettuina, ellei roolikartoitus myönnä niille roolia. Katso [Ensimmäinen kirjautuminen ja käynnistys](#first-login-and-bootstrapping) ja [Roolikartoituksen käyttäytyminen](#role-mapping-behavior). Ylläpitäjä voi myös aktivoida tilin kohdassa Asetukset > Hallinta > Hallitse käyttäjiä.

### PKCE-haara

Gramps Web päättää, käytetäänkö PKCE:tä, kun kirjautuminen alkaa (katso [PKCE](#pkce)). Selvittääksesi, mitä tapahtui asetuksellesi, käy läpi nämä kysymykset järjestyksessä:

1. **Onko `OIDC_PKCE` asetettu?** (Sisäänrakennetuilla palveluntarjoajilla, `OIDC_GOOGLE_PKCE` tai `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE:tä käytetään. Siirry kysymykseen 3.
    - `False`: PKCE on tarkoituksella pois päältä, ja palveluntarjoajan löytöasiakirjaa ei oteta huomioon. Jos palveluntarjoajasi vaatii PKCE:tä, poista asetus tai aseta se arvoksi `True`.
    - Ei asetettu tai tyhjää: jatka kysymykseen 2.
2. **Sisältääkö löytöasiakirja `S256`:n?** Avaa `<issuer>/.well-known/openid-configuration` ja etsi `S256` arvosta `code_challenge_methods_supported`.
    - Kyllä: PKCE:tä käytetään automaattisesti. Jatka kysymykseen 3.
    - Ei, tai kenttä puuttuu: PKCE:tä **ei** käytetä. Aseta `OIDC_PKCE` arvoksi `True`, jos palveluntarjoajasi vaatii sitä. Tarkista myös palvelinlokista `Could not check the provider for PKCE support`, mikä tarkoittaa, että löytöasiakirjaa ei voitu noutaa ja PKCE:tä ei siksi otettu käyttöön.
3. **Lähetettiinkö PKCE todella?** Aloita kirjautuminen ja katso palveluntarjoajan kirjautumissivun osoitetta (tai ensimmäistä uudelleenohjausta selaimesi verkko-välilehdessä). Sen tulisi sisältää `code_challenge=` ja `code_challenge_method=S256`.
    - Läsnä, mutta kirjautuminen epäonnistuu edelleen palautteessa: palveluntarjoaja hylkäsi koodin vahvistimen. Istuntokeksi on voinut kadota uudelleenohjauksen ja palautteen välillä (katso haara 3 yllä), tai palveluntarjoaja ei tue `S256`:ta, jolloin aseta `OIDC_PKCE` arvoksi `False`, jos palveluntarjoaja ei vaadi PKCE:tä.
    - Poissa: yllä olevia asetuksia ei sovellettu. Tarkista, että ympäristömuuttujalla on oikea etuliite ja pienet kirjaimet (esimerkiksi `GRAMPSWEB_OIDC_PKCE=true` Dockerissa; `True` ei lueta boolean-arvona), käynnistä palvelin uudelleen ja tarkista konfiguraatio uudelleen.

!!! note
    Kun PKCE on otettu käyttöön palveluntarjoajalla *valinnaisena* tai ei ollenkaan, kirjautumiset toimivat riippumatta siitä, lähettääkö Gramps Web haasteen vai ei. Vain palveluntarjoajat (tai asiakkaat), jotka on määritetty *vaatimaan* PKCE:tä, tekevät tästä asetuksesta merkityksellisen.

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
EMAIL_USE_SSL=True  # Käytä implisiittistä SSL:ää portissa 465
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

### Pocket ID

Luo OIDC-asiakas Pocket ID:ssä uudelleenohjaus-URL-osoitteella `<BASE_URL>/api/oidc/callback/custom` (katso [Vaaditut uudelleenohjaus-URL-osoitteet](#required-redirect-uris)). Jos otat käyttöön "Vaadi PKCE" asiakkaalle, mitään lisäkonfiguraatiota Gramps Webille ei tarvita, koska Pocket ID mainitsee PKCE-tuen löytöasiakirjassaan. Määritä sitten:

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

Suurin osa Keycloak-konfiguraatiosta voidaan jättää oletusarvoihinsa (*Asiakas → Luo asiakas → Asiakastodennus PÄÄLLÄ*).
On muutamia poikkeuksia:

1. **OpenID-alue** – `openid`-aluetta ei sisällytetä oletusarvoisesti kaikissa Keycloak-versioissa. Ongelmien välttämiseksi lisää se manuaalisesti: *Asiakas → [Gramps-asiakas] → Asiakkaan alueet → Lisää alue → Nimi: `openid` → Aseta oletusarvoksi.*
2. **Roolit** – Roolit voidaan määrittää joko asiakastasolla tai globaalisti per alue.

    * Jos käytät asiakasrooleja, aseta `OIDC_ROLE_CLAIM` -konfiguraatioasetukseksi: `resource_access.[gramps-client-name].roles`
    * Jotta roolit näkyvät Grampsille, siirry *Asiakkaan alueet* (ylätason osio, ei tietyn asiakkaan alla), sitten: *Roolit → Mappers → asiakasroolit → Lisää käyttäjätietoihin → PÄÄLLÄ.*
