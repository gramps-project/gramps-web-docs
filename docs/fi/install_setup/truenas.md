# TrueNAS-asennus

Tämä opas selittää, kuinka Gramps Web asennetaan TrueNAS Community Edition 25.04:lle.

!!! warning
    Tämä opas on tarkoitettu TrueNAS Community Edition 25.04:lle tai uudemmille versioille, jotka esittelivät uuden Docker Compose -pohjaisen sovellusten järjestelmän. Se ei koske aikaisempia TrueNAS-versioita.

## Esivaatimukset

- TrueNAS Community Edition 25.04 tai uudempi
- Perustietämys TrueNASin verkkoliittymästä
- Dataset Gramps Web -datan tallentamista varten

## Yleiskatsaus

TrueNAS Community Edition 25.04 esitteli uuden Docker Compose -pohjaisen sovellusten järjestelmän, joka korvasi aikaisemman Helm-kaavio-pohjaisen lähestymistavan. Tämä opas opastaa sinua luomaan mukautetun sovelluksen Gramps Webille Docker Composen avulla.

## Vaihe 1: Valmistele tallennustila

1. Siirry kohtaan **Datasets** TrueNASin verkkoliittymässä
2. Luo uusi dataset Gramps Webille (esim. `grampsweb`). Huomaa tämän datasetin koko polku, esim. `/mnt/storage/grampsweb`, sillä tarvitset sitä myöhemmin.

Luo alikansioita eri komponentteja varten:
- `users` - Käyttäjä tietokanta
- `database` - Gramps tietokanta tiedostot
- `media` - Media tiedostot

## Vaihe 2: Luo Docker Compose -sovellus

1. Siirry kohtaan **Apps** TrueNASin verkkoliittymässä
2. Napsauta **Discover Apps**
3. Etsi "Gramps Web" ja napsauta sitä
4. Napsauta "Install"

Tämä vie sinut sovelluksen konfigurointisivulle.

## Vaihe 3: Määritä sovellus

### Gramps Webin konfigurointi

- **Aikavyöhyke:** Aseta paikalliseksi aikavyöhykkeeksi (esim. `Europe/Berlin`)
- **Redis salasana:** Aseta salasana Redisille. Tätä käytetään vain sovelluksen sisäisesti.
- **Poista telemetria käytöstä:** jätä tämä ruutu valitsematta – katso [täältä lisätietoja](telemetry.md).
- **Salainen avain:** on erittäin tärkeää, että asetat tämän vahvaksi, ainutlaatuiseksi arvoksi. Katso [palvelimen konfigurointi](configuration.md#existing-configuration-settings) ohjeet satunnaisen avaimen luomiseen.
- **Lisäympäristömuuttujat:** Sinun on asetettava kaikki lisä [konfigurointivaihtoehdot](configuration.md) ympäristömuuttujina, joiden etuliite on `GRAMPSWEB_`. Tarkista [konfigurointidokumentaatio](configuration.md) huolellisesti – esimerkiksi se, että boolean-arvot on asetettava `true` tai `false` (kaikki pienillä kirjaimilla) ympäristömuuttujina, mikä on yleinen ansa.

Aseta **vähintään** `GRAMPSWEB_BASE_URL` URL-osoitteeksi, josta Gramps Web -instanssisi on käytettävissä – tämä on tarpeen asianmukaisen toiminnan varmistamiseksi.

Saatat myös haluta määrittää sähköpostikonfiguraation tässä vaiheessa. Jos teet niin, voit ohittaa sähköpostikonfiguraatiovaiheen käyttöönotto-ohjelmassa. Relevantit ympäristömuuttujat ovat:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Kaikkia konfigurointiasetuksia voidaan muuttaa myöhemmin napsauttamalla "Edit" TrueNAS Apps -liittymässä.

### Tallennuskonfigurointi

- **Käyttäjätallennus:** Valitse polku aiemmin luomaasi `users`-hakemistoon.
- **Indeksitallennus:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Pienennöskuvavälimuisti:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Välimuisti:** Voit jättää oletusasetuksen "ixVolume (Dataset created automatically by the system)"
- **Media tallennus:** Valitse polku aiemmin luomaasi `media`-hakemistoon.
- **Gramps-tietokannan tallennus:** Valitse polku aiemmin luomaasi `database`-hakemistoon.

### Resurssien konfigurointi

Suosittelemme, että varaat vähintään 2 CPU:ta ja 4096 MB RAM:ia sujuvan toiminnan varmistamiseksi.

## Vaihe 4: Pääsy Gramps Webiin

Kun sovellus on otettu käyttöön, voit käyttää Gramps Webiä napsauttamalla "Web UI" -painiketta TrueNAS Apps -liittymässä. Sinun pitäisi nähdä käyttöönotto-ohjelma "Tervetuloa Gramps Webiin".

Jos haluat sallia käyttäjien pääsyn Gramps Web -liittymääsi, **älä** altista sovellusta suoraan internetiin, vaan siirry seuraavaan vaiheeseen.

## Vaihe 5: Aseta käänteinen välityspalvelin

Jotta voit turvallisesti altistaa Gramps Web -instanssisi käyttäjille, on suositeltavaa asettaa käänteinen välityspalvelin. Tämä mahdollistaa SSL/TLS-sertifikaattien hallinnan ja pääsyn hallinnan.

Helpoin vaihtoehto on käyttää virallista TrueNAS Nginx Proxy Manager -sovellusta. Etsi sovellus TrueNAS Apps -liittymästä ja asenna se. Voit jättää kaikki asetukset oletusarvoihinsa, mutta suosittelemme, että asetat yhden lisäympäristömuuttujan: `DISABLE_IPV6` arvolla `true` välttääksesi mahdolliset IPv6:een liittyvät ongelmat.

Kun se on otettu käyttöön, avaa Nginx Proxy Managerin verkkoliittymä ja luo uusi välityspalvelin seuraavilla asetuksilla:

- Kaavio: `http`
- Välitä isäntänimi / IP: TrueNAS-palvelimesi isäntänimi (esim. `truenas`)
- Välitä portti: portti, joka on määritetty Gramps Web -sovelluksellesi (tarkista TrueNAS Apps -liittymästä tarkka portti)
- "SSL"-välilehdellä, valitse "Force SSL"
- "SSL Certificates" -kohdassa, valitse "Add SSL Certificate" > "Let's Encrypt" luodaksesi uuden Let's Encrypt -sertifikaatin verkkotunnuksellesi.

Katso [Nginx Proxy Manager -dokumentaatio](https://nginxproxymanager.com/guide/) saadaksesi lisätietoja reitittimesi konfiguroimisesta ja SSL-sertifikaattien hankkimisesta.
