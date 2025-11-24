# Telemetria

Aloittaen Gramps Web API version 3.2.0, Gramps Web lähettää oletusarvoisesti täysin anonymisoitua telemetriadataa 24 tunnin välein analytiikkapisteeseen, jota hallitsee Gramps Web -tiimi. Tämä sivu sisältää tietoa kerätystä telemetriadatasta, sen käytöstä ja siitä, kuinka se voidaan halutessa poistaa käytöstä.

## Mitä tietoja kerätään?

Telemetriadata on pieni JSON-muotoista tietoa seuraavassa muodossa:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Kuten voit tarkistaa [lähdekoodista](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), palvelimen ja puun tunnisteet ovat ainutlaatuisia palvelimelle ja puulle, mutta ne eivät sisällä mitään henkilökohtaisesti tunnistettavaa tietoa. `timestamp` on nykyinen aika Unix-aikaleimana.

## Miksi tietoja kerätään?

Ainutlaatuisen tunnisteen lähettäminen kerran päivässä mahdollistaa Gramps Web -tiimille seurata, kuinka monta ainutlaatuista palvelinta käyttää Gramps Webiä ja kuinka monta ainutlaatuista puuta käytetään.

Tämä on tärkeää ymmärtää, jotta voidaan arvioida Gramps Webin käyttämien ulkoisten palveluiden, kuten karttapalveluiden, vaikutusta.

## Miten tietoja kerätään?

Kun pyyntö tehdään Gramps Web API -palvelimellesi, se tarkistaa, onko telemetriaa lähetetty viimeisten 24 tunnin aikana (tarkistamalla avaimen paikallisessa välimuistissa). Jos ei, yllä oleva tietokuorma lähetetään päätepisteeseen, joka kirjaa tiedot.

Kirjauspäätepiste sijaitsee Google Cloud Runissa ja se on suoraan otettu käyttöön [avointa lähdekoodia olevasta arkistosta](https://github.com/DavidMStraub/cloud-run-telemetry), joten voit tarkastella, miten tietoja käsitellään.

## Mitä tiedoilla tehdään?

Ensinnäkin, mitään tietoja anonymisoidun tietokuorman ulkopuolelta, joita voitaisiin hypoteettisesti kerätä (kuten palvelimen IP-osoite), ei käytetä Gramps Web -tiimin toimesta.

Kerätyt anonymisoidut tunnisteet ja aikaleima yhdistetään graafien tuottamiseksi, kuten:

- Aktiivisten Gramps Web -asennusten määrä ajan funktiona
- Aktiivisten Gramps Web -puiden määrä ajan funktiona

Nämä grafiikat julkaistaan Gramps Webin dokumentaatiosivustolla.

## Miten telemetria poistetaan käytöstä?

Koska tilastotiedot ovat hyödyllisiä Gramps Web -tiimille ja olemme varmistaneet, että mitään henkilökohtaisesti tunnistettavaa tietoa ei lähetetä, **olisimme kiitollisia, jos et poistaisi telemetriaa käytöstä!**

Kuitenkin Gramps Web antaa käyttäjille täyden hallinnan, joten voit tietenkin valita poistaa ominaisuuden käytöstä, jos haluat.

Tätä varten aseta yksinkertaisesti `DISABLE_TELEMETRY` -konfiguraatioasetukseksi `True` (esim. asettamalla `GRAMPSWEB_DISABLE_TELEMETRY` -ympäristömuuttuja arvoksi `true` &ndash; katso [konfiguraatiosivut](configuration.md) lisätietoja varten).
