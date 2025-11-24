# Gramps Webin käyttöönotto Dockerilla

Kätevintä isännöidä Gramps Webiä omalla palvelimellasi (tai virtuaalipalvelimella) on käyttää Docker Composea.

Oletamme, että Docker ja Docker Compose on jo asennettu järjestelmääsi. Voit käyttää Windowsia, Mac OS:ää tai Linuxia isäntänä. Tuetut arkkitehtuurit sisältävät ei vain x86-64 (työpöytäsysteemit), vaan myös ARM-järjestelmät, kuten Raspberry Pi, joka voi toimia edullisena, mutta riittävän tehokkaana verkkopalvelimena.

!!! note
    Sinun ei tarvitse asentaa Grampsia palvelimelle, sillä se on sisällytetty Docker-kuvaan.


## Vaihe 1: Docker-konfigurointi

Luo palvelimelle uusi tiedosto nimeltä `docker-compose.yml` ja lisää seuraavat sisällöt: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Tämä luo kuusi nimettyä volyymia varmistaakseen, että kaikki olennaiset tiedot säilyvät, kun säiliö käynnistetään uudelleen.

!!! warning
    Yllä oleva tekee API:n saataville isäntäkoneen portissa 80 **ilman SSL/TLS-suojausta**. Voit käyttää tätä paikalliseen testaukseen, mutta älä altista tätä suoraan internetille, se on täysin epävarmaa!

## Vaihe 2: Suojattu pääsy SSL/TLS:llä

Verkkosovellusliittymän **täytyy** olla saatavilla julkisessa internetissä HTTPS:n yli. On useita vaihtoehtoja, esim.

- Käyttämällä Docker-isännöintiä, joka sisältää SSL/TLS:n automaattisesti
- Käyttämällä Nginx-käänteistä välityspalvelinta Let's Encrypt -sertifikaatilla

Katso [Docker Let's Encryptin kanssa](lets_encrypt.md) siitä, miten edellinen asetetaan.

Jos aiot käyttää Gramps Webiä vain paikallisessa verkossasi, voit ohittaa tämän vaiheen.

## Vaihe 3: Käynnistä palvelin

Suorita

```
docker compose up -d
```

Ensimmäisellä käynnistämällä sovellus näyttää ensimmäisen käynnistyksen ohjauksen, joka sallii sinun

- Luoda tilin omistaja (admin) käyttäjälle
- Asettaa joitakin tarpeellisia konfigurointivaihtoehtoja
- Tuoda perhepuun Gramps XML (`.gramps`) -muodossa

## Vaihe 4: Lataa mediasisältöjä

On useita vaihtoehtoja mediasisältöjen lataamiseen.

- Kun käytät tiedostoja, jotka on tallennettu samalle palvelimelle kuin Gramps Web, voit liittää hakemiston Docker-säiliöön sen sijaan, että käyttäisit nimettyä volyymia, eli `/home/server_user/gramps_media/:/app/media` sen sijaan, että käyttäisit `gramps_media:/app/media`, ja ladata mediasisältösi sinne.
- Kun käytät mediasisältöjä, jotka on [isännöity S3:ssa](s3.md), voit käyttää S3 Media Uploader -lisäosaa.
- Kenties kätevin vaihtoehto on käyttää [Gramps Web Sync](../administration/sync.md).
