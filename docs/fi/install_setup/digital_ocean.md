# Gramps Web DigitalOcean 1-Click App

Sen sijaan, että [asentaisit Gramps Webin itse](deployment.md), voit myös käyttää [Gramps Web DigitalOcean 1-Click Appia](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean isännöi Gramps Webin demoversiota.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Osana asennusprosessia sinun on rekisteröidyttävä DigitalOceanille ja valittava maksullinen suunnitelma "droplet" (virtuaalikone) käyttöä varten.

Väitetysti tämä on tällä hetkellä yksinkertaisin tapa ottaa käyttöön oma, itse isännöity Gramps Web -instanssi, joka on suojattu SSL:llä, ilman omaa laitteistoa.

!!! info
    Huomaa, että maksat DigitalOceanille isännöintipalveluista. Grampsin avoimen lähdekoodin projekti ei tarjoa maksullista tukea.

## Vaihe 1: Luo DigitalOcean-tili

Luo tili [DigitalOceanissa](https://www.digitalocean.com/), jos sinulla ei vielä ole sellaista.

## Vaihe 2: Luo droplet

- Siirry [Gramps Web 1-Click Appiin](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) ja napsauta "Luo Gramps Web Droplet".
- Valitse suunnitelma, jossa on vähintään 2 GB RAM-muistia.
- Aseta todennus dropletillesi
- Napsauta "Luo Droplet"

!!! info
    Saatat joutua odottamaan jopa kymmenen minuuttia, jotta 1-Click App asentaa viimeisimmän `docker-compose`-version.
    Viimeisimmän `docker-compose`-version käyttäminen voi vähentää virheitä, jotka viittaavat `firstlogin.sh`:hon.
    
## Vaihe 3: Aseta verkkotunnus

Tarvitset verkkotunnuksen (tai aliverkkotunnuksen). Jos omistat verkkotunnuksen, osoita se dropletisi IP-osoitteeseen. Muussa tapauksessa voit käyttää ilmaista palvelua, kuten [DuckDNS](https://www.duckdns.org/).

## Vaihe 4: Kirjaudu dropletillesi

SSH:lla dropletillesi. Sinulle pitäisi näkyä viesti "Tervetuloa Gramps Web DigitalOcean 1-click app -asennukseen!". Jos näin ei ole, odota muutama minuutti ja yritä uudelleen (asennus ei ole vielä valmis).

Asennusskripti kysyy sinulta verkkotunnusta (esim. `mygrampswebinstance.duckdns.org`) ja sähköpostiosoitetta (tarvitaan Let's Encrypt -sertifikaattia varten).

Kun tämä on tehty, odota, että asennus valmistuu taustalla.

## Vaihe 5: Käynnistä Gramps Web

Gramps Web -instanssisi pitäisi nyt olla käytettävissä verkkotunnuksesi juuresta, voimassa olevan SSL-sertifikaatin kanssa, ja sen pitäisi näyttää ensimmäisen käytön avustaja.
