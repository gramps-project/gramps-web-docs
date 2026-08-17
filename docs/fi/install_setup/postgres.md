# PostgreSQL-tietokannan käyttäminen

Oletuksena Gramps käyttää tiedostopohjaista SQLite-tietokantaa perhesuvun tallentamiseen. Tämä toimii erinomaisesti Gramps Webille ja on suositeltavaa useimmille käyttäjille. Kuitenkin Gramps Web API -version 0.3.0 alkaen myös PostgreSQL-palvelinta, jossa on yksi perhesuku per tietokanta, tuetaan, ja sen taustalla on [Gramps PostgreSQL -lisäosa](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). [Version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) myötä myös SharedPostgreSQL-lisäosa on tuettu, mikä mahdollistaa useiden perhesukujen isännöimisen yhdessä tietokannassa, mikä on erityisen hyödyllistä käytettäessä yhdessä Gramps Web API:n [monisuvutukea](multi-tree.md).

## PostgreSQL-palvelimen määrittäminen

Jos haluat määrittää uuden tietokannan käytettäväksi PostgreSQLAddonin kanssa, voit seurata [ohjeita Gramps Wikissä](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) palvelimen määrittämiseksi.

Vaihtoehtoisesti voit myös käyttää Docker Composea PostgreSQL-palvelimen ajamiseen kontissa samalla docker-isännällä kuin Gramps Web.

Dockerisoidun PostgreSQL:n käyttäminen Grampsin kanssa on vain monimutkaisempaa sen vuoksi, että oletus PostgreSQL-kuvat eivät sisällä mitään paikallisia asetuksia, joita Gramps kuitenkin tarvitsee objektien lokalisoituun lajitteluun. Helpoin vaihtoehto on käyttää `gramps-postgres` -kuvaa, joka on julkaistu [tässä repositoriossa](https://github.com/DavidMStraub/gramps-postgres-docker/). Käyttääksesi sitä, lisää seuraava osio `docker-compose.yml`-tiedostoosi:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
ja lisää myös `postgres_data:` avaimena `volumes:`-osion alle tässä YAML-tiedostossa. Tämä kuva sisältää erillisen tietokannan Grampsin sukututkimustiedoille ja Grampsin käyttäjädatabankille; niillä voi olla erilliset salasanat.

## Gramps-perhesuvun tuominen

Jos olet itse määrittänyt PostgreSQL-palvelimen, voit seurata [ohjeita Gramps Wikissä](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) tuodaksesi perhesuvun tietokantaan.

Vaihtoehtoisesti, jos olet seurannut yllä olevia Docker Compose -ohjeita, voit käyttää seuraavaa komentoa tuodaksesi Gramps XML -tiedoston, joka sijaitsee docker-isännälläsi:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Web API:n määrittäminen käytettäväksi tietokannan kanssa

Määrittääksesi Web API:n käytettäväksi PostgreSQL-tietokannan kanssa, lisää seuraava `environment:`-avaimen alle `grampsweb`-palvelussa `docker-compose.yml`-tiedostossa:

```yaml
      # PostgreSQL-lisäosa olettaa, että puun nimi on
      # sama kuin tietokannan nimi ja täällä käytetään oletus
      # tietokannan nimeä PostgreSQL-kuvasta
      GRAMPSWEB_TREE: postgres
      # Tunnistetietojen on vastattava PostgreSQL-kontissa
      # käytettyjä
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## Jaetun PostgreSQL-tietokannan käyttäminen monisuvun asennuksessa

Kun käytetään [monisuvun asetusta](multi-tree.md), SharedPostgreSQL-lisäosa on kätevä vaihtoehto isännöidä kaikkia puita, myös API:n kautta uusia, yhdessä PostgreSQL-tietokannassa ilman, että yksityisyys tai turvallisuus vaarantuu.

Tämän saavuttamiseksi määritä kontti `gramps-postgres` -kuvan perusteella kuten yllä on kuvattu ja aseta vain konfiguraatioasetukseksi `NEW_DB_BACKEND` arvo `sharedpostgresql`, esimerkiksi `GRAMPSWEB_NEW_DB_BACKEND` ympäristömuuttujan kautta.

## PostgreSQL-tietokannan käyttäminen käyttäjädatabankille

Riippumatta siitä, mitä tietokannan taustaa käytetään sukututkimustiedoille, käyttäjädatabankki voidaan isännöidä PostgreSQL-tietokannassa antamalla sopiva tietokannan URL-osoite. Yllä mainittu `gramps-postgres` docker-kuva sisältää erillisen tietokannan `grampswebuser`, jota voidaan käyttää tähän tarkoitukseen. Tällöin sopiva arvo `USER_DB_URI` konfiguraatioasetukselle olisi
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## PostgreSQL-tietokannan käyttäminen hakemistoindeksille

Gramps Web API -version 2.4.0 alkaen hakemistoindeksi isännöidään joko SQLite-tietokannassa (oletus) tai PostgreSQL-tietokannassa. Myös tätä tarkoitusta varten voidaan käyttää `gramps-postgres` -kuvaa. Hakemistoindeksiä varten voimme käyttää kuvan tarjoamaa `gramps`-tietokantaa riippumatta siitä, isännöimmekö sukututkimustietojamme PostgreSQL:ssä vai ei (hakemistoindeksi ja sukututkimustiedot voivat olla samassa tietokannassa). Tämä voidaan saavuttaa yllä olevassa esimerkissä asettamalla `SEARCH_INDEX_DB_URI` konfiguraatioasetukseksi
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Ongelmat

Ongelmatilanteissa seuraa Gramps Webin ja PostgreSQL-palvelimen lokitulostusta. Dockerin tapauksessa tämä onnistuu komennolla

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Jos epäilet, että Gramps Webissä (tai dokumentaatiossa) on ongelma, voit ilmoittaa ongelmasta [Githubissa](https://github.com/gramps-project/gramps-web-api/issues).
