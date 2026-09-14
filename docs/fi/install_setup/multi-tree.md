# Monien puiden isännöinnin asetukset

Oletusarvoisesti Gramps Web sallii vain yhden perhepuun tietokannan (&ldquo;puu&rdquo;) käytön, joka on määritelty konfiguraatiotiedostossa.

Kuitenkin Gramps Web API -palvelimen version 0.7.0 myötä on myös mahdollista palvella useita puita yhdestä asennuksesta. Kuitenkin jokainen käyttäjä on (tällä hetkellä) sidottu yhteen puuhun, joten tämä asetus ei sovellu puiden jakamiseen käyttäjien kesken, vaan useiden eristettyjen Gramps Web -instanssien isännöimiseen.

## Ota käyttöön monipuu-tuki

Ottaaksesi monipuu-tuen käyttöön, `TREE` konfiguraatioasetuksen on oltava asetettu yhdeksi asteriskiksi `*`, esim. konfiguraatiotiedostossa:

```python
TREE = "*"
```

Tämä tekee kaikki puut palvelimen Gramps-tietokantahakemistossa saavutettaviksi (riittävien käyttäjäoikeuksien myötä). Puu ID on alihakemiston nimi. Voit luetella olemassa olevat puut (nimet ja ID:t) komennolla

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Lisäksi sinun tulisi asettaa `MEDIA_PREFIX_TREE` konfiguraatioasetukseksi `True` varmistaaksesi, että media tiedostot tallennetaan erillisiin alihakemistoihin. Muuten käyttäjät voivat päästä käsiksi media tiedostoihin, jotka kuuluvat puulle, johon heillä ei ole oikeuksia!

## Lisää käyttäjätili tiettyyn puuhun

Lisätäksesi käyttäjän tiettyyn puuhun, lisää vain `--tree TREEID` komentorivivaihtoehto käyttäjän lisäämis -komentoon. Voit myös POSTata `/users/` päätepisteeseen, jossa `tree` ominaisuus on asetettu JSON-kuormassa.

Käyttäjänimien on oltava ainutlaatuisia *kaikissa* puissa. Sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (koska Gramps Web API 3.22), joten sama henkilö voi esimerkiksi omistaa tilejä useissa puissa käyttäen yhtä sähköpostiosoitetta.

## Luo uusi puu

Uuden puun luomiseen suositellaan POSTamista `/trees/` päätepisteeseen sen sijaan, että käytetään Gramps CLI:tä. Tämä käyttää UUIDv4:ää puu ID:nä, mikä lisää turvallisuutta, koska nimeä ei voi arvata. Tällä hetkellä vain SQLitea tuetaan uusille puille.

## Validoi

Validoidaksesi (hakeaksesi tokenin) tarvitaan vain käyttäjänimi ja salasana, kuten yksittäisen puun tilassa, koska puu ID on tunnettu jokaiselle käyttäjälle, joten sitä ei tarvitse antaa.

## Siirrä olemassa olevat media tiedostot

Jos haluat siirtää olemassa olevan Gramps Web -instanssin monipuu-tukeen ja käytät paikallisia media tiedostoja, voit yksinkertaisesti siirtää ne alkuperäisen sijainnin alihakemistoon, jonka nimi on puu ID.

Jos käytät media tiedostoja, jotka on isännöity S3:ssa, voit käyttää `gramps-web-api`-varaston `scripts`-hakemistossa olevaa skriptiä:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Tämä edellyttää, että asiaankuuluvat pääsyoikeusavaimet on jo asetettu ympäristömuuttujiksi.

## Siirrä olemassa oleva käyttäjätietokanta

Jos haluat ottaa käyttöön monipuu-tuen ja käyttää olemassa olevia käyttäjiä, sinun on määritettävä heidät tiettyyn puuhun. Voit käyttää seuraavaa komentoa tätä tarkoitusta varten,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Mukauta etupään

Rekisteröintisivu, joka on saatavilla kirjautumissivulta, ei toimi monipuu-asetuksessa, koska puu on määritettävä rekisteröintiä varten. On siis suositeltavaa asettaa `hideRegisterLink` arvoksi `true` [etupään konfiguraatiossa](frontend-config.md).
