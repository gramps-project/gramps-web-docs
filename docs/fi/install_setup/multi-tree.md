# Monien puiden isännöinnin asetukset

Oletusarvoisesti Gramps Web sallii vain yhden perhepuun tietokannan (&ldquo;puu&rdquo;) käytön, joka on määritelty asetustiedostossa.

Kuitenkin Gramps Web API -taustajärjestelmän versiosta 0.7.0 alkaen on mahdollista palvella useita puita yhdestä asennuksesta. Kuitenkin jokainen käyttäjä on (tällä hetkellä) sidottu yhteen puuhun, joten tämä asetus ei sovellu puiden jakamiseen käyttäjien kesken, vaan useiden eristettyjen Gramps Web -instanssien isännöimiseen.

## Ota käyttöön monipuu-tuki

Ottaaksesi monipuu-tuen käyttöön, `TREE`-asetuksen on oltava asetettu yhdeksi asteriskiksi `*`, esimerkiksi asetustiedostossa:

```python
TREE = "*"
```

Tämä tekee kaikki puut palvelimen Gramps-tietokantahakemistossa saataville (olettaen riittävät käyttäjäoikeudet). Puun ID on alihakemiston nimi. Voit listata olemassa olevat puut (nimet ja ID:t) komennolla

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Lisäksi sinun tulisi asettaa `MEDIA_PREFIX_TREE` -asetuksen arvo `True`, jotta media tiedostot tallennetaan erillisiin alihakemistoihin. Muuten käyttäjät voivat käyttää media tiedostoja, jotka kuuluvat puulle, johon heillä ei ole oikeuksia!

## Lisää käyttäjätili tiettyyn puuhun

Lisätäksesi käyttäjän tiettyyn puuhun, lisää vain `--tree TREEID` komentorivivaihtoehto käyttäjän lisäämis -komentoon. Voit myös POSTATA `/users/` -päätepisteeseen, jossa `tree`-ominaisuus on asetettu JSON-kuormassa.

Käyttäjänimien on oltava ainutlaatuisia *kaikissa* puissa. Sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (Gramps Web API 3.22:sta alkaen), joten sama henkilö voi esimerkiksi olla tilejä useissa puissa käyttäen yhtä sähköpostiosoitetta.

## Luo uusi puu

Uuden puun luomiseksi on suositeltavaa POSTATA `/trees/` -päätepisteeseen sen sijaan, että käyttäisit Gramps CLI:tä. Tämä käyttää UUIDv4:ää puun ID:nä, mikä lisää turvallisuutta, koska nimeä ei voi arvata. Uudelleen luodut puut käyttävät `NEW_DB_BACKEND` -asetuksessa määriteltyä tietokantataustaa: SQLite (oletusarvo) tai SharedPostgreSQL. Katso [PostgreSQL-tietokannan käyttö](postgres.md) lisätietoja varten.

## Valtuuta

Valtuuttaaksesi (hakeaksesi tokenin) tarvitset vain käyttäjänimen ja salasanan, kuten yksittäisen puun tilassa, koska puun ID tunnetaan jokaiselle käyttäjälle, joten sitä ei tarvitse antaa.

## Siirrä olemassa olevat media tiedostot

Jos haluat siirtää olemassa olevan Gramps Web -instanssin monipuu-tukeen ja käytät paikallisia media tiedostoja, voit yksinkertaisesti siirtää ne alkuperäisen sijainnin alihakemistoon, jonka nimi on puun ID.

Jos käytät S3:lle isännöityjä media tiedostoja, voit käyttää `gramps-web-api`-varaston `scripts`-hakemistossa olevaa skriptiä:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Oletetaan, että asiaankuuluvat pääsytunnukset on jo asetettu ympäristömuuttujiksi.

## Siirrä olemassa oleva käyttäjätietokanta

Jos haluat ottaa käyttöön monipuu-tuen ja käyttää olemassa olevia käyttäjiä, sinun on määritettävä heidät tiettyyn puuhun. Voit käyttää seuraavaa komentoa tätä tarkoitusta varten,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Mukauta etupäätä

Rekisteröintisivu, joka on saatavilla kirjautumissivulta, ei toimi monipuu-asetuksessa, koska puu on määritettävä rekisteröintiä varten. On siis suositeltavaa asettaa `hideRegisterLink` arvoksi `true` [etupään asetuksissa](frontend-config.md).
