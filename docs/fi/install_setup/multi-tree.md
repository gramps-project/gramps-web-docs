# Monien puiden isännöinnin asetukset

Oletusarvoisesti Gramps Web sallii pääsyn vain yhteen perhepuu-tietokantaan (&ldquo;puu&rdquo;), joka on määritelty asetustiedostossa.

Kuitenkin Gramps Web API -palvelimen version 0.7.0 myötä on myös mahdollista palvella useita puita yhdestä asennuksesta. Kuitenkin jokainen käyttäjä on (tällä hetkellä) sidottu yhteen puuhun, joten tämä asetus ei sovellu puiden jakamiseen käyttäjien kesken, vaan useiden eristettyjen Gramps Web -instanssien isännöimiseen.

## Ota käyttöön monipuu-tuki

Ottaaksesi monipuu-tuen käyttöön, `TREE`-asetuksen on oltava asetettu yhdeksi asteriskiksi `*`, esim. asetustiedostossa:

```python
TREE = "*"
```

Tämä tekee kaikki puut palvelimen Gramps-tietokantahakemistossa saavutettaviksi (riittävien käyttäjäoikeuksien ollessa voimassa). Puiden tunnus on alihakemiston nimi. Voit luetella olemassa olevat puut (nimet ja tunnukset) komennolla

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Lisäksi sinun tulisi asettaa `MEDIA_PREFIX_TREE` -asetuksen arvo `True`, jotta varmistat, että mediasisältö tallennetaan erillisiin alihakemistoihin. Muuten käyttäjät voivat käyttää mediasisältöjä, jotka kuuluvat puulle, johon heillä ei ole oikeuksia!

## Lisää käyttäjätili tiettyyn puuhun

Lisätäksesi käyttäjän tiettyyn puuhun, lisää vain `--tree TREEID` komentorivivaihtoehto käyttäjän lisäämis -komentoon. Voit myös POSTata `/users/`-päätepisteeseen, jossa `tree`-ominaisuus on asetettu JSON-kuormassa.

Käyttäjänimet ja sähköpostiosoitteet on oltava ainutlaatuisia *kaikissa* puissa.

## Luo uusi puu

Uuden puun luomiseen on suositeltavaa POSTata `/trees/`-päätepisteeseen sen sijaan, että käyttäisit Gramps CLI:tä. Tämä käyttää UUIDv4:ää puun tunnuksena, mikä lisää turvallisuutta, koska nimeä ei voi arvata. Tällä hetkellä vain SQLite on tuettu uusille puille.

## Validoi

Validoidaksesi (hakeaksesi tokenin) tarvitset vain käyttäjänimen ja salasanan, kuten yksittäisen puun tilassa, koska puun tunnus on tiedossa jokaiselle käyttäjälle, joten sitä ei tarvitse antaa.

## Siirrä olemassa olevat mediasisällöt

Jos haluat siirtää olemassa olevan Gramps Web -instanssin monipuu-tukeen ja käytät paikallisia mediasisältöjä, voit yksinkertaisesti siirtää ne alkuperäisen sijainnin alihakemistoon puun tunnuksena.

Jos käytät S3:lla isännöityjä mediasisältöjä, voit käyttää `gramps-web-api`-varaston `scripts`-hakemistossa olevaa skriptiä:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Tämä edellyttää, että asiaankuuluvat pääsytunnukset on asetettu ympäristömuuttujiksi.

## Siirrä olemassa oleva käyttäjätietokanta

Jos haluat ottaa käyttöön monipuu-tuen ja käyttää olemassa olevia käyttäjiä, sinun on määritettävä heidät tiettyyn puuhun. Voit käyttää seuraavaa komentoa tätä tarkoitusta varten,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Mukauta etupään

Rekisteröitymissivu, joka on saatavilla kirjautumissivulta, ei toimi monipuu-asetuksessa, koska puu on määritettävä rekisteröitymistä varten. On siis suositeltavaa asettaa `hideRegisterLink` arvoksi `true` [etupään asetuksissa](frontend-config.md).
