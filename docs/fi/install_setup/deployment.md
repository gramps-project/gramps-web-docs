# Gramps Webin käyttöönotto Dockerilla

Kätevintä isännöidä Gramps Webiä omalla palvelimellasi (tai virtuaalipalvelimella) on käyttää Docker Composea.

Oletamme, että Docker ja Docker Compose ovat jo asennettuna järjestelmääsi. Voit käyttää Windowsia, Mac OS:ää tai Linuxia isäntäjärjestelmänä. Tuetut arkkitehtuurit sisältävät paitsi x86-64 (työpöytäsysteemit), myös ARM-järjestelmät, kuten Raspberry Pi, joka voi toimia edullisena, mutta riittävän tehokkaana verkkopalvelimena.

!!! note
    Sinun ei tarvitse asentaa Grampsia palvelimelle, sillä se on sisällytetty Docker-kuvaan.


## Vaihe 1: Docker-konfigurointi

Luo palvelimelle uusi tiedosto nimeltä `docker-compose.yml` ja lisää seuraavat sisällöt: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Tämä luo kuusi nimettyä volyymia varmistaakseen, että kaikki olennaiset tiedot säilyvät, kun säiliö käynnistetään uudelleen.

Aseta `GRAMPSWEB_BASE_URL` osoitteeksi, josta Gramps Webiin pääsee, esim. `https://gramps.mydomain.com`. Tätä käytetään linkkien rakentamiseen sähköposteissa, kuten salasanojen palautuksissa. Sähköpostien lähettämistä varten lisää myös sähköpostiasetukset, jotka on kuvattu [konfiguraatiossa](configuration.md).

!!! warning
    Edellä mainittu tekee API:sta saatavilla isäntäkäyttöjärjestelmän portissa 80 **ilman SSL/TLS-suojaa**. Voit käyttää tätä paikalliseen testaukseen, mutta älä altista tätä suoraan internetiin, se on täysin epävarmaa!

## Vaihe 2: Suojattu pääsy SSL/TLS:llä

Verkko-API **täytyy** tarjota julkiselle internetille HTTPS:n kautta. On useita vaihtoehtoja, esim.

- Käyttämällä Docker-isännöintiä, joka sisältää SSL/TLS:n automaattisesti
- Käyttämällä Nginx-käänteistä välityspalvelinta Let's Encrypt -sertifikaatilla

Katso [Docker Let's Encryptin kanssa](lets_encrypt.md) saadaksesi ohjeet edellisen asettamiseen.

Jos suunnittelet Gramps Webin käyttöä vain paikallisessa verkossasi, voit ohittaa tämän vaiheen.

## Vaihe 3: Käynnistä palvelin

Suorita

```
docker compose up -d
```

Ensimmäisellä käynnistämisellä sovellus näyttää ensimmäisen käynnistysohjelman, joka mahdollistaa sinulle

- Tilin luomisen omistajalle (admin) käyttäjälle
- Perhepuun tuomisen Gramps XML (`.gramps`) -muodossa

## Vaihe 4: Lataa mediasisältöjä

On useita vaihtoehtoja mediasisältöjen lataamiseen.

- Kun käytät tiedostoja, jotka on tallennettu samalle palvelimelle kuin Gramps Web, voit liittää hakemiston Docker-säiliöön sen sijaan, että käyttäisit nimettyä volyymia, eli `/home/server_user/gramps_media/:/app/media` sen sijaan, että käyttäisit `gramps_media:/app/media`, ja ladata mediasisältösi sinne.
- Kun käytät mediasisältöjä, jotka on [isännöity S3:ssa](s3.md), voit käyttää S3 Media Uploader -lisäosaa.
- Kenties kätevin vaihtoehto on käyttää [Gramps Web Syncia](../administration/sync.md).
