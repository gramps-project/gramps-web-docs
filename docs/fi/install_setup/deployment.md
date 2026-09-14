# Gramps Webin käyttöönotto Dockerilla

Käytännöllisin vaihtoehto isännöidä Gramps Webiä omalla palvelimellasi (tai virtuaalipalvelimella) on Docker Compose.

Oletamme, että Docker ja Docker Compose on jo asennettu järjestelmääsi. Voit käyttää isäntäjärjestelmänä Windowsia, Mac OS:ää tai Linuxia. Tuetut arkkitehtuurit sisältävät paitsi x86-64 (työpöytäkoneet), myös ARM-järjestelmät, kuten Raspberry Pi, joka voi toimia edullisena, mutta riittävän tehokkaana verkkopalvelimena.

!!! note
    Sinun ei tarvitse asentaa Grampsia palvelimelle, koska se on sisällytetty Docker-kuvaan.


## Vaihe 1: Docker-konfiguraatio

Luo palvelimelle uusi tiedosto nimeltä `docker-compose.yml` ja lisää seuraavat sisällöt: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Tämä luo kuusi nimettyä volyymia varmistaakseen, että kaikki olennaiset tiedot säilyvät, kun säiliö käynnistetään uudelleen.

!!! warning
    Yllä oleva tekee API:sta saatavilla olevan isäntäjärjestelmän portissa 80 **ilman SSL/TLS-suojausta**. Voit käyttää tätä paikalliseen testaukseen, mutta älä altista tätä suoraan internetille, se on täysin turvaton!

## Vaihe 2: Suojatun pääsyn varmistaminen SSL/TLS:llä

Verkkosovellusohjelma **täytyy** toimittaa julkiselle internetille HTTPS:n yli. On useita vaihtoehtoja, esim.

- Käyttämällä Docker-isännöintiä, joka sisältää SSL/TLS:n automaattisesti
- Käyttämällä Nginx-käänteistä välityspalvelinta Let's Encrypt -sertifikaatilla

Katso [Docker ja Let's Encrypt](lets_encrypt.md) siitä, miten edellinen asetetaan.

Jos suunnittelet Gramps Webin käyttöä vain paikallisessa verkossasi, voit ohittaa tämän vaiheen.

## Vaihe 3: Palvelimen käynnistäminen

Suorita

```
docker compose up -d
```

Ensimmäisellä käynnistyskerralla sovellus näyttää ensimmäisen käynnistyksen ohjauksen, joka sallii sinun

- Luoda tilin omistajalle (admin) käyttäjälle
- Asettaa joitakin tarvittavia konfiguraatioasetuksia
- Tuoda perhesuhteet Gramps XML (`.gramps`) -muodossa

## Vaihe 4: Median tiedostojen lataaminen

Median tiedostojen lataamiseen on useita vaihtoehtoja.

- Kun käytät tiedostoja, jotka on tallennettu samalle palvelimelle kuin Gramps Web, voit liittää hakemiston Docker-säiliöön sen sijaan, että käyttäisit nimettyä volyymia, eli `/home/server_user/gramps_media/:/app/media` sen sijaan, että käyttäisit `gramps_media:/app/media`, ja ladata median tiedostosi sinne.
- Kun käytät median tiedostoja [S3:lla isännöityinä](s3.md), voit käyttää S3 Media Uploader -lisäosaa.
- Ehkä kätevin vaihtoehto on käyttää [Gramps Web Sync](../administration/sync.md).
