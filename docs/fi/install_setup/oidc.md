# OIDC-todennus

Gramps Web tukee OpenID Connect (OIDC) -todennusta, jonka avulla käyttäjät voivat kirjautua sisään käyttäen ulkoisia identiteettipalveluja. Tämä sisältää sisäänrakennetut palveluntarjoajat Google ja Microsoft sekä mukautetut OIDC-palveluntarjoajat, kuten Keycloak, Authentik ja Authelia.

!!! warning "GitHubia OIDC-palveluntarjoajana ei enää tueta"
    Jos sinulla on asetettu `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` aikaisemmasta versiosta, poista ne – niitä ei enää huomioida, ja käyttäjät, jotka kirjautuivat aiemmin GitHubin kautta, eivät voi enää kirjautua sillä tavalla. GitHub on OAuth 2.0 -palveluntarjoaja, ei OpenID Connect -palveluntarjoaja, eikä se koskaan palauttanut vaatimusta, johon Gramps Web luottaa identiteetissä, joten se ei ollut koskaan täysin luotettava.

## Yleiskatsaus

OIDC-todennus mahdollistaa:

- Ulkoisten identiteettipalvelujen käyttö käyttäjätodennuksessa
- Useiden todennuspalveluntarjoajien tukeminen samanaikaisesti
- OIDC-ryhmien/roolien kartoittamisen Gramps Webin käyttäjärooleihin
- Yksinkertaisen sisäänkirjautumisen (SSO) ja yksinkertaisen uloskirjautumisen toteuttamisen
- Paikallisen käyttäjänimen/salasanan todennuksen valinnaisen poistamisen

## Konfigurointi

OIDC-todennuksen mahdollistamiseksi sinun on määritettävä asianmukaiset asetukset Gramps Webin konfigurointitiedostossa tai ympäristömuuttujissa. Katso [Palvelimen konfigurointi](configuration.md#settings-for-oidc-authentication) -sivulta täydellinen luettelo käytettävissä olevista OIDC-asetuksista.

!!! info
    Kun käytät ympäristömuuttujia, muista lisätä jokaisen asetuksen nimen eteen `GRAMPSWEB_` (esim. `GRAMPSWEB_OIDC_ENABLED`). Katso [Konfigurointitiedosto vs. ympäristömuuttujat](configuration.md#configuration-file-vs-environment-variables) lisätietoja varten.

### Sisäänrakennetut palveluntarjoajat

Gramps Webillä on sisäänrakennettu tuki suosituimmille identiteettipalveluntarjoajille. Käyttääksesi niitä, sinun tarvitsee vain antaa asiakastunnus ja asiakassalaisuus:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ja `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ja `OIDC_MICROSOFT_CLIENT_SECRET`

Voit määrittää useita palveluntarjoajia samanaikaisesti. Järjestelmä tunnistaa automaattisesti, mitkä palveluntarjoajat ovat käytettävissä konfigurointiarvojen perusteella.

!!! tip "Microsoft: yksittäisen vuokralaisen käyttöönotot"
    Sisäänrakennettu Microsoft-palveluntarjoaja käyttää monivuokralaisen `/common` -päätepistettä ja hyväksyy kirjautumiset mistä tahansa Microsoft-tilistä suunnitellusti. Jos haluat sallia vain oman vuokralaisesi käyttäjät, käytä [mukautettua OIDC-palveluntarjoajaa](#custom-oidc-providers) vuokralaisesi erityisellä myöntäjä-URL-osoitteella, joka pitää myöntäjän vahvistuksen aktiivisena ja rajoittaa kirjautumiset kyseiseen vuokralaisuuteen.

### Mukautetut OIDC-palveluntarjoajat

Mukautetuille OIDC-palveluntarjoajille (kuten Keycloak, Authentik, Authelia tai yksittäinen Microsoft Entra -vuokralainen) käytä näitä asetuksia:

| Avain                | Kuvaus                                                                 |
|---------------------|------------------------------------------------------------------------|
| `OIDC_ENABLED`      | Boolean, onko OIDC-todennus käytössä. Aseta `True`.                   |
| `OIDC_ISSUER`      | Palveluntarjoajasi myöntäjän URL-osoite. Löydettävyys haetaan `<issuer>/.well-known/openid-configuration`. |
| `OIDC_CLIENT_ID`    | Asiakastunnus OIDC-palveluntarjoajallesi                               |
| `OIDC_CLIENT_SECRET` | Asiakassalaisuus OIDC-palveluntarjoajallesi                           |
| `OIDC_NAME`         | Mukautettu näyttönimi (valinnainen, oletuksena "OIDC")                |
| `OIDC_SCOPES`       | OAuth-alueet (valinnainen, oletuksena "openid email profile")         |
| `OIDC_USERNAME_CLAIM` | Vaatimus, jota käytetään käyttäjänimen luomiseen (valinnainen, oletuksena "preferred_username") |
| `OIDC_PKCE`         | Käytetäänkö PKCE:tä, katso [PKCE](#pkce) (valinnainen, otetaan käyttöön automaattisesti, jos palveluntarjoaja tukee sitä) |

### PKCE

Gramps Web API 3.23:sta lähtien Gramps Web tukee [PKCE:tä](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256`-menetelmä) valtuutuskoodin virrassa. Jotkin identiteettipalveluntarjoajat, kuten Pocket ID, voidaan määrittää *vaatimaan* PKCE:tä asiakkaalta, ja ne hylkäävät kirjautumiset, jotka eivät käytä sitä. Vanhemmat versiot Gramps Web API:sta eivät koskaan käytä PKCE:tä, joten kirjautumiset tällaisella asiakkaalla epäonnistuvat.

Onko PKCE:tä käytetty, päätetään kirjautumisen yhteydessä seuraavasti:

- Jos `OIDC_PKCE` on asetettu `True`, PKCE:tä käytetään.
- Jos `OIDC_PKCE` on asetettu `False`, PKCE:tä ei käytetä, vaikka palveluntarjoaja tukisi sitä.
- Jos `OIDC_PKCE` ei ole asetettu tai se on asetettu tyhjäksi, PKCE:tä käytetään, jos palveluntarjoajan löytämisdokumentti (`/.well-known/openid-configuration`) listaa `S256` arvossa `code_challenge_methods_supported`, eikä sitä käytetä muuten.

Useimmissa asetuksissa sinun ei tarvitse asettaa mitään. Aseta `OIDC_PKCE` arvoksi `True`, jos palveluntarjoajasi vaatii PKCE:tä mutta ei mainitse `S256`:ta löytämisdokumentissaan, ja `False`, jos palveluntarjoajasi mainitsee `S256`:n mutta käsittelee sen väärin. Ympäristömuuttujina boolean-arvojen on oltava pienillä kirjaimilla (`GRAMPSWEB_OIDC_PKCE=true`), katso [Konfigurointi](configuration.md).

Sisäänrakennetuissa palveluntarjoajissa vastaavat vaihtoehdot ovat `OIDC_GOOGLE_PKCE` ja `OIDC_MICROSOFT_PKCE`.

PKCE-koodin vahvistin säilytetään käyttäjän istunnossa uudelleenohjauksen ja palautteen välillä, joten tämä ei vaadi muutoksia uudelleenohjaus-URL-osoitteisiin.

### Monipuuasetukset

Monipuisessa palvelimessa puu, johon käyttäjä kirjautuu, on tiedettävä ennen kuin Gramps Web ohjaa identiteettipalveluntarjoajaan, joten kirjautuminen alkaa seuraavasti:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` on pakollinen monipuusasetuksissa; sen poistaminen tai olemattoman puun ID:n antaminen epäonnistuttaa kirjautumisen. Yksittäisessä puupalvelimessa `tree` on valinnainen, mutta jos se annetaan, sen on vastattava määritettyä `TREE`:tä.

OIDC-identiteetti on sidottu tarkalleen yhteen Gramps Web -tiliin, joka puolestaan kuuluu tarkalleen yhteen puuhun – kirjautuminen eri puuhun epäonnistuu sen sijaan, että tili siirtyisi. Ei ole mahdollista liittää yhtä identiteettiä palveluntarjoajalla useisiin tiliin; käyttäjät, jotka tarvitsevat pääsyn useisiin puihin, tarvitsevat erilliset identiteetit palveluntarjoajalla (esim. erilliset käyttäjänimet tai tilit).

!!! warning
    Sivuston ylläpitäjän tili, jolla ei ole liitettyä puuta (katso [ylläpitäjätilin luominen](../administration/owner.md)), ei voi kirjautua OIDC:n kautta, koska OIDC-kirjautuminen vaatii aina puun. Tällaiset tilit on luotava ja todennettava paikallisella käyttäjänimellä/salasanalla.

## Vaaditut uudelleenohjaus-URL-osoitteet

Kun määrität OIDC-palveluntarjoajaasi, sinun on rekisteröitävä seuraava uudelleenohjaus-URL-osoite:

**OIDC-palveluntarjoajille, jotka tukevat jokerimerkkejä: (esim. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Missä `*` on regex-jokerimerkki. Palveluntarjoajan regex-tulkista riippuen tämä voi olla myös `.*` tai vastaava. Varmista, että regex on käytössä, jos palveluntarjoajasi vaatii sitä (esim. Authentik).

**OIDC-palveluntarjoajille, jotka eivät tue jokerimerkkejä: (esim. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Puu ei koskaan ole osa uudelleenohjaus-URL-osoitetta, edes monipuuspalvelimilla – se kulkee erikseen istunnossa, koska palveluntarjoajat vaativat, että uudelleenohjaus-URL-osoitteen on vastattava tarkasti rekisteröityä.

## Roolikartoitus

Gramps Web voi automaattisesti kartoittaa OIDC-ryhmiä tai -rooleja identiteettipalveluntarjoajaltasi Gramps Webin käyttäjärooleihin. Tämä mahdollistaa käyttäjäoikeuksien hallinnan keskitetysti identiteettipalveluntarjoajassasi. Roolikartoitus toimii samalla tavalla kaikille palveluntarjoajille, sekä sisäänrakennetuille että mukautetuille.

### Konfigurointi

Käytä näitä asetuksia roolikartoituksen määrittämiseen:

| Avain                | Kuvaus                                                                 |
|---------------------|------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`   | Vaatimuksen nimi OIDC-todistuksessa, joka sisältää käyttäjän ryhmät/roolit. Oletuksena "groups". Pisteelliset polut ovat tuettuja, esim. `realm_access.roles`. |
| `OIDC_GROUP_ADMIN`   | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Admin" -roolia |
| `OIDC_GROUP_OWNER`   | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Owner" -roolia |
| `OIDC_GROUP_EDITOR`  | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Editor" -roolia |
| `OIDC_GROUP_CONTRIBUTOR` | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Contributor" -roolia |
| `OIDC_GROUP_MEMBER`  | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Member" -roolia |
| `OIDC_GROUP_GUEST`   | OIDC-palveluntarjoajaltasi peräisin oleva ryhmän/roolin nimi, joka vastaa Grampsin "Guest" -roolia |

### Roolikartoituksen käyttäytyminen

Jos mitään `OIDC_GROUP_*` -asetusta ei ole määritetty, roolikartoitus on pois päältä ja rooleja hallitaan manuaalisesti Gramps Webissä; uusia OIDC-tilejä luodaan sitten pois päältä ja ne tarvitsevat hyväksynnän olemassa olevalta omistajalta tai ylläpitäjältä (katso [Ensimmäinen kirjautuminen ja käynnistys](#first-login-and-bootstrapping) alla).

Kun roolikartoitus on määritetty, jokaisessa kirjautumisessa:

- Jos roolivaatimus on läsnä ja käyttäjä kuuluu kartoitettuun ryhmään, hän saa vastaavan roolin.
- Jos roolivaatimus on läsnä mutta käyttäjä ei kuulu kartoitettuun ryhmään, hänen roolinsa asetetaan pois päältä. Tämä on oletusarvoinen sulkeva tila, ei virhe – Gramps Web ei voi päätellä roolia ryhmälle, jota se ei tunnista.
- Jos roolivaatimusta ei ole lainkaan tokenissa, olemassa olevaa roolia ei muuteta; uusi tili on silti oletusarvoisesti pois päältä.

!!! warning "Google ei lähetä ryhmiä koskevaa vaatimusta"
    Googlen tokenit eivät koskaan sisällä `groups`-vaatimusta, joten roolikartoituksen ollessa käytössä Google-kirjautumiset kuuluvat yllä olevaan "vaatimus puuttuu" -kategoriaan: olemassa olevat käyttäjät säilyttävät roolinsa, mutta uudet Google-käyttäjät luodaan pois päältä ja tarvitsevat manuaalista hyväksyntää. Pidä tämä mielessä ennen kuin otat roolikartoituksen käyttöön vain toista palveluntarjoajaa varten – se ei itsessään poista olemassa olevia Google-käyttäjiä.

Microsoft Entra palauttaa sovellustasot ja ryhmän jäsenyydet vain ID-tokenissa, ei käyttäjätietopisteestä. Gramps Web yhdistää ID-tokenin vaatimukset käyttäjätietovastaukseen, jotta `OIDC_ROLE_CLAIM` toimii samalla tavalla kuin muilla palveluntarjoajilla; missä molemmat sisältävät vaatimuksen, käyttäjätietojen arvo on etusijalla.

## Ensimmäinen kirjautuminen ja käynnistys

Uudet tilit, jotka on luotu OIDC:n kautta, alkavat olla pois päältä, ellei roolikartoitus myönnä niille roolia (katso yllä). Uudessa instanssissa kukaan ei voi hyväksyä pois päältä olevaa tiliä, ja jos `OIDC_DISABLE_LOCAL_AUTH` on myös käytössä, ei ole salasanaa, johon turvautua.

!!! warning "Määritä omistaja/ylläpitäjäryhmä ennen ensimmäistä kirjautumista"
    Ennen kuin kukaan kirjautuu OIDC:n kautta ensimmäistä kertaa, aseta `OIDC_GROUP_OWNER` (tai `OIDC_GROUP_ADMIN`) ja varmista, että ensimmäinen käyttäjä kuuluu kyseiseen ryhmään palveluntarjoajalla. Muuten instanssia ei voida käynnistää OIDC:n kautta lainkaan.

## Tilit ja käyttäjänimet

OIDC:n kautta luodut tilit saavat luodun käyttäjänimen, joka määritetään kerran tilin luomisen yhteydessä eikä sitä muuteta myöhemmissä kirjautumisissa:

- Sisäänrakennetut palveluntarjoajat: `<provider>_<claim value>`, esim. `microsoft_alice@contoso.com`
- Mukautettu palveluntarjoaja: pelkkä vaatimusarvo, esim. `alice`

Numeroinen liite lisätään, jos on törmäys. OIDC:n kautta luodun tilin käyttäjänimeä ei voi myöhemmin muuttaa; sen sijaan koko nimi ja sähköpostiosoite päivitetään jokaisessa kirjautumisessa.

OIDC-kirjautuminen ei koskaan liity olemassa olevaan paikalliseen tiliin, jolla on sama sähköpostiosoite – tämä on tahallista, koska tilien yhdistäminen sähköpostin perusteella on tilin kaappaamisen vektori. Käyttäjä, jolla on jo paikallinen tili, saa toisen, erillisen tilin ensimmäisellä kerralla, kun hän kirjautuu OIDC:n kautta.

Palveluntarjoajalta saadut sähköpostiosoitteet tallennetaan vain, jos palveluntarjoaja merkitsee ne vahvistetuiksi (tai jättää `email_verified`-vaatimuksen kokonaan pois); muuten kirjautuminen etenee ilman sähköpostiosoitteen tallentamista. Koska sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (Gramps Web API 3.22:sta lähtien), osoite tallennetaan, vaikka toinen tili käyttäisi sitä jo.

## OIDC-ulosskirjautuminen

Gramps Web tukee Yksinkertaista uloskirjautumista (SSO-ulosskirjautumista) OIDC-palveluntarjoajille. `GET /api/oidc/logout/` etsii palveluntarjoajan `end_session_endpoint` -päätepisteen ja palauttaa sen `logout_url` -arvona vastauksessa; Gramps Webin etupään on navigoitava selaimessa sinne, jotta istunto voidaan todella päättää identiteettipalveluntarjoajalla. `logout_url` on `null`, kun palveluntarjoajalla ei ole `end_session_endpoint` -päätepistettä.

!!! warning "Tokenit eivät vanhene uloskirjautuessa"
    Uloskirjautuminen päättää vain selainistunnon; tällä hetkellä ei ole tapaa peruuttaa jo myönnettyä Gramps Web -tokenia. Tokenit pysyvät voimassa, kunnes ne vanhenevat (`JWT_ACCESS_TOKEN_EXPIRES`, oletus 15 minuuttia pääsytokeneille), riippumatta siitä, onko käyttäjä sen jälkeen kirjautunut ulos Gramps Webistä tai identiteettipalveluntarjoajalta.

## Vianetsintä

Aloita kohdasta, jossa kirjautuminen pysähtyy, ja seuraa haaraa. Gramps Web kirjaa epäonnistuneen palautteen syyn (etsi `OIDC callback error for provider` palvelinlokista), joka on yleensä tarkempi kuin selainikkunassa näkyvä viesti.

**1. Puuttuuko kirjautumispainike?**

- Tarkista `<BASE_URL>/api/oidc/config/`. Jos `enabled` on `false` tai `providers` on tyhjää, OIDC:tä ei ole määritetty: `OIDC_ENABLED` on oltava `True`, ja mukautetun palveluntarjoajan on oltava sekä `OIDC_ISSUER` että `OIDC_CLIENT_ID`.
- Sisäänrakennettu palveluntarjoaja (Google, Microsoft) rekisteröidään vain, jos sekä sen asiakastunnus että asiakassalaisuus on asetettu.
- Tarkista palvelinlokista käynnistyksen yhteydessä `Could not load discovery document`. Tämä tarkoittaa, että palvelin ei voinut saavuttaa `<issuer>/.well-known/openid-configuration` (tai `OIDC_OPENID_CONFIG_URL`). Se yrittää uudelleen ensimmäisellä käytöllä, mutta Gramps Web -kontin on pystyttävä ratkaisemaan ja saavuttamaan myöntäjän URL-osoite itse, ei vain selaimellasi.

**2. Saako selain virheen heti, kun se lähetetään palveluntarjoajalle?**

Virhe näytetään identiteettipalveluntarjoajan toimesta ennen kuin kirjaudut sisään.

- *"uudelleenohjaus-URL-osoitteen yhteensopimattomuus"* (tai vastaava): palveluntarjoajalla rekisteröity uudelleenohjaus-URL-osoitteen on vastattava tarkasti, mukaan lukien protokolla, isäntä, portti ja palveluntarjoajan ID. Katso [Vaaditut uudelleenohjaus-URL-osoitteet](#required-redirect-uris). Huomaa, että se on rakennettu `BASE_URL`:sta, joten väärä `BASE_URL` antaa väärän uudelleenohjaus-URL-osoitteen.
- *PKCE-virhe* (esimerkiksi `invalid_request`, "koodivaatimus vaaditaan" tai puuttuva `code_challenge` -parametri): palveluntarjoaja vaatii PKCE:tä, mutta Gramps Web ei lähettänyt sitä. Siirry [PKCE-haaraan](#pkce-branch) alla.

**3. Hyväksyykö palveluntarjoaja kirjautumisen, mutta Gramps Web näyttää sitten virheen?**

- *`mismatching_state`, tai virhe mainitsee istunnon tai tilan*: selain ei lähettänyt takaisin Gramps Webin asettamaa istuntokeksiä, kun kirjautuminen alkoi. Tämä keksi sisältää myös PKCE-koodin vahvistimen. Varmista, että selaimen osoite vastaa `BASE_URL`:ia (sama protokolla ja isäntä), että käänteinen välityspalvelin välittää keksejä ja alkuperäisen isännän, ja että kirjautuminen aloitetaan ja päätetään samassa selainvälilehdessä tai ikkunassa.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: tarkista palvelinlokista taustasyy. Yleisiä syitä ovat väärä asiakassalaisuus, myöntäjän URL-osoite, joka ei vastaa tokenien `iss`-vaatimusta, ja palveluntarjoajan palauttama virhe palautteeseen (esimerkiksi PKCE, katso alla).
- *Liian monta yritystä*: kirjautumis- ja palautepisteet ovat rajoitettuja (5 pyyntöä minuutissa). Odota minuutti ja yritä uudelleen.

**4. Onko kirjautuminen onnistunut, mutta näet "Tili tarkistuksessa" tai et voi tehdä mitään?**

Uudet tilit luodaan pois päältä, ellei roolikartoitus myönnä roolia. Katso [Ensimmäinen kirjautuminen ja käynnistys](#first-login-and-bootstrapping) ja [Roolikartoituksen käyttäytyminen](#role-mapping-behavior). Ylläpitäjä voi myös aktivoida tilin kohdassa Asetukset > Hallinta > Hallitse käyttäjiä.

### PKCE-haara

Gramps Web päättää, käytetäänkö PKCE:tä, kun kirjautuminen alkaa (katso [PKCE](#pkce)). Selvittääksesi, mitä tapahtui asetuksillesi, käy läpi nämä kysymykset järjestyksessä:

1. **Onko `OIDC_PKCE` asetettu?** (Sisäänrakennetuissa palveluntarjoajissa `OIDC_GOOGLE_PKCE` tai `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE:tä käytetään. Siirry kysymykseen 3.
    - `False`: PKCE on tahallisesti pois päältä, ja palveluntarjoajan löytämisdokumenttia ei huomioida. Jos palveluntarjoajasi vaatii PKCE:tä, poista asetus tai aseta se arvoksi `True`.
    - Ei asetettu tai tyhjää: jatka kysymykseen 2.
2. **Sisältääkö löytämisdokumentti `S256`:n?** Avaa `<issuer>/.well-known/openid-configuration` ja etsi `S256` arvosta `code_challenge_methods_supported`.
    - Kyllä: PKCE:tä käytetään automaattisesti. Jatka kysymykseen 3.
    - Ei, tai kenttä puuttuu: PKCE:tä **ei** käytetä. Aseta `OIDC_PKCE` arvoksi `True`, jos palveluntarjoajasi vaatii sitä. Tarkista myös palvelinlokista `Could not check the provider for PKCE support`, mikä tarkoittaa, että löytämisdokumenttia ei voitu noutaa ja PKCE:tä ei siksi otettu käyttöön.
3. **Lähetettiinkö PKCE todella?** Aloita kirjautuminen ja katso palveluntarjoajan kirjautumissivun osoitetta (tai ensimmäistä uudelleenohjausta selaimesi verkko-välilehdessä). Sen tulisi sisältää `code_challenge=` ja `code_challenge_method=S256`.
    - Läsnä, mutta kirjautuminen epäonnistuu edelleen palautteessa: palveluntarjoaja hylkäsi koodin vahvistimen. Istuntokeksi on saattanut kadota uudelleenohjauksen ja palautteen välillä (katso haara 3 yllä), tai palveluntarjoaja ei tue `S256`:ta, jolloin aseta `OIDC_PKCE` arvoksi `False`, jos palveluntarjoaja ei vaadi PKCE:tä.
    - Poissa: yllä olevia asetuksia ei sovellettu. Tarkista, että ympäristömuuttujalla on oikea etuliite ja pienet kirjaimet (esimerkiksi `GRAMPSWEB_OIDC_PKCE=true` Dockerissa; `True` ei lueta boolean-arvona), käynnistä palvelin uudelleen ja tarkista konfigurointi uudelleen.

!!! note
    Kun PKCE on otettu käyttöön palveluntarjoajalla *valinnaisena* tai ei ole lainkaan käytössä, kirjautumiset toimivat riippumatta siitä, lähetetäänkö Gramps Web haaste. Vain palveluntarjoajat (tai asiakkaat), jotka on määritetty *vaatimaan* PKCE:tä, tekevät tästä asetuksesta merkityksellisen.

## Esimerkkikonfiguraatiot

### Mukautettu OIDC-palveluntarjoaja (Keycloak)

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
OIDC_ROLE_CLAIM="groups"  # tai "roles" riippuen palveluntarjoajastasi
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Käytä salausta portissa 465
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

Luo OIDC-asiakas Pocket ID:ssä uudelleenohjaus-URL-osoitteella `<BASE_URL>/api/oidc/callback/custom` (katso [Vaaditut uudelleenohjaus-URL-osoitteet](#required-redirect-uris)). Jos otat käyttöön "Vaadi PKCE" asiakkaalle, ylimääräistä Gramps Web -konfigurointia ei tarvita, koska Pocket ID mainitsee PKCE-tuen löytämisdokumentissaan. Määritä sitten:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Yhteisön tekemä OIDC-asennusopas Gramps Webille on saatavilla [virallisella Authelia-dokumentaatiosivustolla](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Suurin osa Keycloakin konfiguroinnista voidaan jättää oletusarvoihinsa (*Asiakas → Luo asiakas → Asiakkaan todennus PÄÄLLÄ*).
On muutamia poikkeuksia:

1. **OpenID-alue** – `openid`-aluetta ei oletusarvoisesti sisällytetä kaikkiin Keycloak-versioihin. Ongelmien välttämiseksi lisää se manuaalisesti: *Asiakas → [Gramps-asiakas] → Asiakkaan alueet → Lisää alue → Nimi: `openid` → Aseta oletusarvoksi.*
2. **Roolit** – Roolit voidaan määrittää joko asiakastason tai globaalisti alueen mukaan.

    * Jos käytät asiakasrooleja, aseta `OIDC_ROLE_CLAIM` -konfigurointivaihtoehto: `resource_access.[gramps-client-name].roles`
    * Jotta roolit näkyvät Grampsille, siirry *Asiakkaan alueet* (ylätason osio, ei tietyn asiakkaan alla), sitten: *Roolit → Mappers → asiakasroolit → Lisää käyttäjätietoihin → PÄÄLLÄ.*
