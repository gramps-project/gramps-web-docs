# PostgreSQL-tietokannan käyttäminen

Oletusarvoisesti Gramps käyttää tiedostopohjaista SQLite-tietokantaa perhesuunnitelman tallentamiseen. Tämä toimii erinomaisesti Gramps Webille ja on suositeltavaa useimmille käyttäjille. Kuitenkin alkaen Gramps Web API -version 0.3.0, myös PostgreSQL-palvelin, jossa on yksi perhesuunnitelma per tietokanta, on tuettu, ja sen taustalla on [Gramps PostgreSQL -lisäosa](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Alkaen [versiosta 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), myös SharedPostgreSQL-lisäosa on tuettu, mikä mahdollistaa useiden perhesuunnitelmien isännöinnin yhdessä tietokannassa, mikä on erityisen hyödyllistä käytettäessä yhdessä Gramps Web API:n [monipuustukea](multi-tree.md).

!!! warning "PostgreSQL-taustajärjestelmä poistettu käytöstä"
    Tuki PostgreSQL-taustajärjestelmälle (yksi perhesuunnitelma per tietokanta) poistetaan tulevassa Gramps Web API -versiossa, koska se ei ole yhteensopiva useiden puiden isännöinnin kanssa. SharedPostgreSQL- ja SQLite-taustajärjestelmiä tuetaan edelleen täysin. Uusissa asennuksissa käytä SharedPostgreSQL:ää.

## PostgreSQL-palvelimen määrittäminen

Jos haluat määrittää uuden tietokannan käytettäväksi PostgreSQLAddonin kanssa, voit seurata [ohjeita Gramps Wikin](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) mukaan palvelimen määrittämiseksi.

Vaihtoehtoisesti voit myös käyttää Docker Composea PostgreSQL-palvelimen ajamiseen säiliössä samalla docker-isännällä kuin Gramps Web.

Dockerisoitu PostgreSQL Grampsin kanssa on vain monimutkaista sen vuoksi, että oletusarvoisissa PostgreSQL-kuvissa ei ole asennettu mitään paikallisia asetuksia, joita Gramps kuitenkin tarvitsee objektien lokalisoituun lajitteluun. Helpoin vaihtoehto on käyttää `gramps-postgres` -kuvaa, joka on julkaistu [tässä repositoriossa](https://github.com/DavidMStraub/gramps-postgres-docker/). Käyttääksesi sitä, lisää seuraava osa `docker-compose.yml`-tiedostoon:
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
ja lisää myös `postgres_data:` avaimena `volumes:`-osion alle tässä YAML-tiedostossa. Tämä kuva sisältää erillisen tietokannan Grampsin sukututkimustiedoille ja Grampsin käyttäjätietokannalle; kummallakin voi olla erilliset salasanat.

## Grampsin perhesuunnitelman tuominen

Jos olet määrittänyt PostgreSQL-palvelimen itse, voit seurata [ohjeita Gramps Wikin](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) mukaan tuodaksesi perhesuunnitelman tietokantaan.

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
      # sama kuin tietokannan nimi, ja täällä käytetään
      # PostgreSQL-kuvan oletustietokannan nimeä
      GRAMPSWEB_TREE: postgres
      # Tunnistetietojen on oltava samat kuin
      # PostgreSQL-säiliössä käytetyt
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## Jaetun PostgreSQL-tietokannan käyttäminen monipuustekniikassa

Kun käytetään [monipuustekniikkaa](multi-tree.md), SharedPostgreSQL-lisäosa on kätevä vaihtoehto isännöidä kaikkia puita, myös API:n kautta uusia, yhdessä PostgreSQL-tietokannassa ilman, että yksityisyys tai turvallisuus vaarantuu.

Tämän saavuttamiseksi määritä säiliö `gramps-postgres` -kuvan perusteella kuten yllä on kuvattu ja aseta yksinkertaisesti konfiguraatioasetukseksi `NEW_DB_BACKEND` arvo `sharedpostgresql`, esimerkiksi `GRAMPSWEB_NEW_DB_BACKEND` ympäristömuuttujan kautta.

## PostgreSQL-tietokannan käyttäminen käyttäjätietokannan kanssa

Riippumatta siitä, mikä tietokantataustajärjestelmä käytetään sukututkimustiedoille, käyttäjätietokanta voidaan isännöidä PostgreSQL-tietokannassa antamalla sopiva tietokannan URL-osoite. Yllä mainittu `gramps-postgres` -docker-kuva sisältää erillisen tietokannan `grampswebuser`, jota voidaan käyttää tähän tarkoitukseen. Tällöin sopiva arvo `USER_DB_URI` -konfiguraatioasetukselle olisi
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## PostgreSQL-tietokannan käyttäminen hakemiston kanssa

Koska Gramps Web API -versio 2.4.0, hakemisto isännöidään joko SQLite-tietokannassa (oletusarvo) tai PostgreSQL-tietokannassa. Myös tätä tarkoitusta varten voidaan käyttää `gramps-postgres` -kuvaa. Hakemiston osalta voimme käyttää kuvan tarjoamaa `gramps`-tietokantaa, riippumatta siitä, isännöimmekö sukututkimustietojamme PostgreSQL:ssä vai ei (hakemisto ja sukututkimustiedot voivat olla samassa tietokannassa). Tämä voidaan saavuttaa yllä olevassa esimerkissä asettamalla `SEARCH_INDEX_DB_URI` -konfiguraatioasetukseksi
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Ongelmat

Ongelmatilanteissa seuraa Gramps Webin ja PostgreSQL-palvelimen lokitulosteita. Dockerin tapauksessa tämä saavutetaan komennolla

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Jos epäilet, että Gramps Webissä (tai dokumentaatiossa) on ongelma, ilmoita ongelmasta [Githubissa](https://github.com/gramps-project/gramps-web-api/issues).
