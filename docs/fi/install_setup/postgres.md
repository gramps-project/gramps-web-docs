# PostgreSQL-tietokannan käyttäminen

Oletusarvoisesti Gramps käyttää tiedostopohjaista SQLite-tietokantaa perhesuvun tallentamiseen. Tämä toimii erinomaisesti Gramps Webin kanssa ja on suositeltavaa useimmille käyttäjille. Kuitenkin Gramps Web API -version 0.3.0 alkaen tuetaan myös PostgreSQL-palvelinta, jossa on yksi perhesuku per tietokanta, jota tukee [Gramps PostgreSQL -lisäosa](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). [Version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) myötä myös SharedPostgreSQL-lisäosa on tuettu, mikä mahdollistaa useiden perhesukujen isännöimisen yhdessä tietokannassa, mikä on erityisen hyödyllistä käytettäessä yhdessä Gramps Web API:n [monisuku-tukea](multi-tree.md).

## PostgreSQL-palvelimen asetukset

Jos haluat perustaa uuden tietokannan käytettäväksi PostgreSQLAddonin kanssa, voit seurata [ohjeita Gramps Wikissä](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) palvelimen asettamiseksi.

Vaihtoehtoisesti voit myös käyttää Docker Composea PostgreSQL-palvelimen ajamiseen säilössä samalla docker-isännällä kuin Gramps Web.

Dockerisoidun PostgreSQL:n käyttäminen Grampsin kanssa on vain monimutkaista siitä syystä, että oletusarvoisissa PostgreSQL-kuvissa ei ole asennettu mitään paikallisia asetuksia, joita Gramps kuitenkin tarvitsee objektien lokalisoituun lajitteluun. Helpoin vaihtoehto on käyttää `gramps-postgres` -kuvaa, joka on julkaistu [tässä varastossa](https://github.com/DavidMStraub/gramps-postgres-docker/). Käyttääksesi sitä, lisää seuraava osio `docker-compose.yml` -tiedostoon:
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
ja lisää myös `postgres_data:` avaimena `volumes:`-osion alle tässä YAML-tiedostossa. Tämä kuva sisältää erillisen tietokannan Grampsin sukututkimustiedoille ja Grampsin käyttäjädatabankille; kummallakin voi olla erilliset salasanat.

## Gramps-perhesuvun tuominen

Jos olet itse asentanut PostgreSQL-palvelimen, voit seurata [ohjeita Gramps Wikissä](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) tuodaksesi perhesuvun tietokantaan.

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

## Web API:n konfigurointi tietokannan käyttöön

Konfiguroidaksesi Web API:n PostgreSQL-tietokannan käyttöön, lisää seuraava `environment:`-avaimen alle `grampsweb`-palvelussa `docker-compose.yml`-tiedostossa:

```yaml
      # PostgreSQL-lisäosa olettaa, että puun nimi on
      # sama kuin tietokannan nimi ja täällä käytetään oletus
      # tietokannan nimeä PostgreSQL-kuvasta
      TREE: postgres
      # Tunnistetietojen on oltava samat kuin
      # PostgreSQL-säilössä käytetyt
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Jaetun PostgreSQL-tietokannan käyttäminen monisuku-asennuksessa

Kun käytetään [monisukuasetusta](multi-tree.md), SharedPostgreSQL-lisäosa on kätevä vaihtoehto isännöidä kaikkia puita, myös API:n kautta uusia, yhdessä PostgreSQL-tietokannassa ilman, että yksityisyydestä tai turvallisuudesta tingitään.

Tämän saavuttamiseksi aseta säilö, joka perustuu `gramps-postgres` -kuvaan yllä kuvatulla tavalla, ja aseta yksinkertaisesti konfiguraatio-ominaisuus `NEW_DB_BACKEND` arvoksi `sharedpostgresql`, esimerkiksi `GRAMPSWEB_NEW_DB_BACKEND` ympäristömuuttujan kautta.

## PostgreSQL-tietokannan käyttäminen käyttäjädatabankille

Riippumatta siitä, mikä tietokannan tausta käytetään sukututkimustiedoille, käyttäjädatabankki voidaan isännöidä PostgreSQL-tietokannassa antamalla sopiva tietokannan URL. Yllä mainittu `gramps-postgres` docker-kuva sisältää erillisen tietokannan `grampswebuser`, jota voidaan käyttää tähän tarkoitukseen. Tällöin sopiva arvo `USER_DB_URI` -konfiguraatio-ominaisuudelle olisi
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## PostgreSQL-tietokannan käyttäminen hakemistoindeksille

Gramps Web API -version 2.4.0 alkaen hakemistoindeksi isännöidään joko SQLite-tietokannassa (oletusarvo) tai PostgreSQL-tietokannassa. Myös tätä tarkoitusta varten voidaan käyttää `gramps-postgres` -kuvaa. Hakemistoindeksille voimme käyttää kuvasta saatavaa `gramps`-tietokantaa riippumatta siitä, isännöimmekö sukututkimustietojamme PostgreSQL:ssä vai ei (hakemistoindeksi ja sukututkimustiedot voivat olla samassa tietokannassa). Tämä voidaan saavuttaa yllä olevassa esimerkissä asettamalla `SEARCH_INDEX_DB_URI` -konfiguraatio-ominaisuus arvoon
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```


## Ongelmat

Ongelmien ilmetessä seuraa Gramps Webin ja PostgreSQL-palvelimen lokitulosteita. Dockerin tapauksessa tämä saavutetaan komennolla

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Jos epäilet, että Gramps Webissä (tai dokumentaatiossa) on ongelma, ilmoita siitä [Githubissa](https://github.com/gramps-project/gramps-web-api/issues).
