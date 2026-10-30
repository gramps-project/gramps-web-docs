# TrueNAS-asennus

Tämä opas selittää, kuinka Gramps Web asetetaan TrueNAS Community Edition 25.04:ssä.

!!! warning
    Tämä opas on tarkoitettu TrueNAS Community Edition 25.04:lle tai uudemmille versioille, jotka esittelivät uuden Docker Compose -pohjaisen sovellusten järjestelmän. Se ei koske aikaisempia TrueNAS-versioita.

## Esivaatimukset

- TrueNAS Community Edition 25.04 tai uudempi
- Perustietämys TrueNASin verkkoliittymästä
- Dataset Gramps Web -datan tallentamista varten

## Yleiskatsaus

TrueNAS Community Edition 25.04 esitteli uuden Docker Compose -pohjaisen sovellusten järjestelmän, joka korvasi aikaisemman Helm-kaavapohjaisen lähestymistavan. Tämä opas opastaa sinut luomaan mukautetun sovelluksen Gramps Webille Docker Composea käyttäen.

## Vaihe 1: Valmistele tallennustila

1. Siirry kohtaan **Datasets** TrueNASin verkkoliittymässä
2. Luo uusi dataset Gramps Webille (esim. `grampsweb`). Huomaa tämän datasetin koko polku, esim. `/mnt/storage/grampsweb`, sillä tarvitset sitä myöhemmin.

Luo alikansioita eri komponentteja varten:
- `users` - Käyttäjä tietokanta
- `database` - Gramps tietokanta tiedosto(t)
- `media` - Mediatiilaat

## Vaihe 2: Luo Docker Compose -sovellus

1. Siirry kohtaan **Apps** TrueNASin verkkoliittymässä
2. Napsauta **Discover Apps**
3. Etsi "Gramps Web" ja napsauta sitä
4. Napsauta "Install"

Tämä vie sinut sovelluksen konfigurointisivulle.

## Vaihe 3: Määritä sovellus

### Gramps Web -konfigurointi

- **Aikavyöhyke:** Aseta paikalliseksi aikavyöhykkeeksi (esim. `Europe/Berlin`)
- **Redis-salasana:** Aseta salasana Redisille. Tätä käytetään vain sovelluksen sisäisesti.
- **Poista telemetria käytöstä:** jätä tämä ruutu valitsematta – katso [täältä lisätietoja](telemetry.md).
- **Salainen avain:** on tärkeää, että asetat tämän vahvaksi, ainutlaatuiseksi arvoksi. Katso [palvelimen konfigurointi](configuration.md#existing-configuration-settings) ohjeita satunnaisen avaimen luomiseksi.
- **Lisäympäristömuuttujat:** Sinun on asetettava kaikki lisä [konfigurointivaihtoehdot](configuration.md) ympäristömuuttujina, jotka alkavat `GRAMPSWEB_`. Tarkista [konfigurointidokumentaatio](configuration.md) tarkasti – esimerkiksi se, että boolean-arvot on asetettava `true` tai `false` (kaikki pienellä) ympäristömuuttujina, mikä on yleinen sudenkuoppa.

Aseta **vähintään** `GRAMPSWEB_BASE_URL` URL-osoitteeksi, josta Gramps Web -instanssisi on saavutettavissa – tämä on tarpeen asianmukaisen toiminnan varmistamiseksi.

Saatat myös haluta määrittää sähköpostikonfiguraation tässä vaiheessa, mikä on tarpeen esimerkiksi salasanan palautuksia varten. Relevantit ympäristömuuttujat ovat:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Kaikkia konfigurointiasetuksia voidaan muuttaa myöhemmin napsauttamalla "Edit" TrueNAS Apps -liittymässä.

### Tallennuskonfigurointi

- **Käyttäjätallennus:** Valitse polku `users`-hakemistoon, jonka loit aiemmin.
- **Indeksitallennus:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Pienennöskuvavälimuisti:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Välimuisti:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Mediatallennus:** Valitse polku `media`-hakemistoon, jonka loit aiemmin.
- **Gramps-tietokannan tallennus:** Valitse polku `database`-hakemistoon, jonka loit aiemmin.

### Resurssien konfigurointi

Suosittelemme, että varaat vähintään 2 CPU:ta ja 4096 MB RAM-muistia sujuvan toiminnan varmistamiseksi.

## Vaihe 4: Pääsy Gramps Webiin

Kun sovellus on otettu käyttöön, voit käyttää Gramps Webiä napsauttamalla "Web UI" -painiketta TrueNAS Apps -liittymässä. Sinun pitäisi nähdä käyttöönotto-opas "Welcome to Gramps Web".

Jos haluat sallia käyttäjien käyttää Gramps Web -liittymääsi, **älä** altista sovellusta suoraan internetiin, vaan siirry seuraavaan vaiheeseen.

## Vaihe 5: Määritä käänteinen välityspalvelin

Jotta voit turvallisesti altistaa Gramps Web -instanssisi käyttäjille, on suositeltavaa määrittää käänteinen välityspalvelin. Tämä mahdollistaa SSL/TLS-sertifikaattien hallinnan ja pääsyn hallinnan.

Helpoin vaihtoehto on käyttää virallista TrueNAS Nginx Proxy Manager -sovellusta. Etsi sovellusta TrueNAS Apps -liittymästä ja asenna se. Voit jättää kaikki asetukset oletusarvoihinsa, mutta suosittelemme, että asetat yhden lisäympäristömuuttujan: `DISABLE_IPV6` arvolla `true` välttääksesi mahdollisia IPv6:een liittyviä ongelmia.

Kun se on otettu käyttöön, avaa Nginx Proxy Managerin verkkoliittymä ja luo uusi välityspalvelin seuraavilla asetuksilla:

- Scheme: `http`
- Forward Hostname / IP: TrueNAS-palvelimesi isäntänimi (esim. `truenas`)
- Forward Port: portti, joka on määritetty Gramps Web -sovelluksellesi (tarkista TrueNAS Apps -liittymästä tarkka portti)
- "SSL"-välilehdellä, valitse "Force SSL"
- "SSL Certificates" -kohdassa, valitse "Add SSL Certificate" > "Let's Encrypt" luodaksesi uuden Let's Encrypt -sertifikaatin verkkotunnuksellesi.

Katso [Nginx Proxy Manager -dokumentaatio](https://nginxproxymanager.com/guide/) saadaksesi lisätietoja reitittimesi konfiguroinnista ja SSL-sertifikaattien hankkimisesta.
