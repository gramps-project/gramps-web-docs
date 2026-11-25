# Gramps Web DigitalOcean 1-Click -sovellus

Sen sijaan, että [määrittäisit Gramps Webin itse](deployment.md), voit myös käyttää [Gramps Web DigitalOcean 1-Click -sovellusta](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean isännöi Gramps Webin demoversiota.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Osana määritysprosessia sinun on luotava tili DigitalOcean-palveluun ja valittava maksullinen palvelupaketti käytettävää ”dropletia” (virtuaalikonetta) varten.

Tätä voidaan pitää tällä hetkellä yksinkertaisimpana tapana ottaa käyttöön oma, itse ylläpidetty Gramps Web -instanssi SSL-suojauksella ilman omien laitteistojen käyttöä.

!!! info
    Huomaa, että maksat DigitalOceanille isännöintipalveluista. Grampsin avoimen lähdekoodin projekti ei tarjoa maksullista tukea.

## Vaihe 1: Luo DigitalOcean-tili

Luo tili [DigitalOcean-palvelussa](https://www.digitalocean.com/), jos sinulla ei vielä ole tiliä.

## Vaihe 2: Luo droplet

- Siirry [Gramps Web 1-Click -sovellukseen](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) ja napsauta ”Create Gramps Web Droplet”.
- Valitse palvelupaketti, jossa on vähintään 2 Gt RAM-muistia.
- Määritä dropletin todennus
- Napsauta ”Create Droplet”

## Vaihe 3: Määritä verkkotunnus

Tarvitset verkkotunnuksen (tai aliverkkotunnuksen). Jos omistat verkkotunnuksen, osoita se dropletin IP-osoitteeseen. Muussa tapauksessa voit käyttää ilmaista palvelua, kuten [DuckDNS](https://www.duckdns.org/).

## Vaihe 4: Kirjaudu dropletiin

Muodosta SSH-yhteys dropletiin. Sinulle pitäisi näkyä viesti ”Welcome to the Gramps Web DigitalOcean 1-click app setup!”. Jos näin ei ole, odota muutama minuutti ja yritä uudelleen (asennus ei ole vielä valmis).

Asennuskomentosarja pyytää sinulta verkkotunnuksen (esim. `mygrampswebinstance.duckdns.org`) ja sähköpostiosoitteen (jota tarvitaan Let's Encrypt -varmenteeseen). Lisäksi se kysyy valinnaisesti SMTP-asetuksia, joita Gramps Web käyttää sähköpostien lähettämiseen, esimerkiksi salasanan palautuksia varten; ohita tämä jättämällä SMTP-isäntä tyhjäksi.

Kun tämä on tehty, odota, että määritys valmistuu taustalla

## Vaihe 5: Käynnistä Gramps Web

Gramps Web -instanssisi pitäisi nyt olla käytettävissä verkkotunnuksesi juuressa kelvollisella SSL-varmenteella, ja siinä pitäisi näkyä ensimmäisen käynnistyksen avustaja.

## Määrityksen muuttaminen myöhemmin

Asennuskomentosarja tallentaa perus-URL-osoitteen ja sähköpostiasetukset tiedostoon `/root/letsencrypt.env` [määritysasetuksina](configuration.md), joiden etuliitteenä on `GRAMPSWEB_`, esimerkiksi

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Voit lisätä asetuksia tai muuttaa niitä muokkaamalla tätä tiedostoa dropletissa ja ottamalla muutoksen käyttöön komennolla

```bash
cd /opt/grampsweb && docker compose up -d
```
