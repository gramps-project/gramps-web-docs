# Gramps Web DigitalOcean 1-Click App

Sen sijaan, että [asetat Gramps Webin itse](deployment.md), voit myös käyttää [Gramps Web DigitalOcean 1-Click Appia](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean isännöi Gramps Webin demo versiota.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Osana asennusprosessia sinun on rekisteröidyttävä DigitalOceanissa ja valittava maksullinen suunnitelma "dropletia" (virtuaalikonetta) varten.

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

## Vaihe 3: Aseta verkkotunnus

Tarvitset verkkotunnuksen (tai aliverkkotunnuksen). Jos omistat verkkotunnuksen, osoita se dropletisi IP-osoitteeseen. Muussa tapauksessa voit käyttää ilmaista palvelua, kuten [DuckDNS](https://www.duckdns.org/).

## Vaihe 4: Kirjaudu dropletillesi

SSH:lla dropletillesi. Sinulle pitäisi esittää viesti "Tervetuloa Gramps Web DigitalOcean 1-click appin asennukseen!". Jos näin ei ole, odota muutama minuutti ja yritä uudelleen (asennus ei ole vielä valmis).

Asennusskripti kysyy sinulta verkkotunnusta (esim. `mygrampswebinstance.duckdns.org`) ja sähköpostiosoitetta (tarvitaan Let's Encrypt -sertifikaattiin). Valinnaisesti se kysyy myös SMTP-asetuksia, joita Gramps Web käyttää sähköpostien lähettämiseen, esim. salasanojen nollaamiseen; jätä SMTP-isäntä tyhjäksi ohittaaksesi tämän.

Kun tämä on tehty, odota, että asennus valmistuu taustalla.

## Vaihe 5: Käynnistä Gramps Web

Gramps Web -instanssisi pitäisi nyt olla käytettävissä verkkotunnuksesi juuresta, voimassa olevan SSL-sertifikaatin kanssa, ja sen pitäisi näyttää ensimmäisen käytön avustaja.

## Muuttaminen myöhemmin

Asennusskripti tallentaa perus-URL:n ja sähköpostiasetukset tiedostoon `/root/letsencrypt.env` [konfiguraatioasetuksina](configuration.md), jotka alkavat `GRAMPSWEB_`, esim.

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Asetusten lisäämiseksi tai muuttamiseksi muokkaa tätä tiedostoa dropletilla ja sovella muutosta komennolla

```bash
cd /opt/grampsweb && docker compose up -d
