# PostgreSQL-tietokannan käyttäminen

Oletusarvoisesti Gramps Web tallentaa jokaisen sukupuun omaan SQLite-tietokantatiedostoon. Tämä ei vaadi lisäpalvelua, varmuuskopiot ovat yhtä yksinkertaisia kuin tiedostojen kopioiminen, ja se toimii hyvin useimmissa asennuksissa, mukaan lukien [useita puita isännöivät](multi-tree.md).

Vaihtoehtoisesti sukupuita voidaan isännöidä PostgreSQL-palvelimella käyttämällä SharedPostgreSQL-lisäosaa, joka pitää kaikki puut yhdessä tietokannassa. Tämä voi olla järkevää, jos sinulla on jo PostgreSQL-palvelin ja haluat hallita varmuuskopioita ja seurantaa siellä, tai jos odotat monia käyttäjiä muokkaamassa samanaikaisesti. PostgreSQL voi myös isännöidä [käyttäjätietokantaa](#using-a-postgresql-database-for-the-user-database) ja [hakemistoa](#using-a-postgresql-database-for-the-search-index), riippumatta siitä, missä sukupuut ovat tallennettu.

!!! warning "PostgreSQL-lisäosa poistettu käytöstä"
    Vanhempi PostgreSQL-lisäosa, joka tallentaa yhden sukupuun per tietokanta, on poistettu käytöstä eikä sitä tueta enää tulevassa versiossa Gramps Web API:sta. Jos käytät sitä, katso [Puun siirtäminen PostgreSQL-lisäosasta SharedPostgreSQL:ään](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## PostgreSQL-palvelimen asetukset

Helpoin vaihtoehto on ajaa PostgreSQL-palvelinta säilössä samalla Docker-isännällä kuin Gramps Web, käyttäen Docker Composea.

Gramps tarvitsee paikalliset asetukset asennettuna PostgreSQL-palvelimelle, jotta objektit voidaan lajitella oikein eri kielillä, ja oletusarvoiset PostgreSQL-kuvat eivät sisällä mitään. [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) -kuva lisää ne. Käyttääksesi sitä, lisää seuraava osio `docker-compose.yml`-tiedostoosi:
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
Lisää myös `postgres_data:` avaimena `volumes:`-osion alle tässä YAML-tiedostossa. Kuva sisältää kaksi tietokantaa, joista kummallakin on oma käyttäjä ja salasana: `gramps` sukututkimustietoja varten ja `grampswebuser` Gramps Web -käyttäjätietokantaa varten.

Jos käytät omaa PostgreSQL-palvelintasi, luo tietokanta nimeltä `gramps`, johon määritetty käyttäjä voi luoda tauluja, ja varmista, että käyttäjiesi tarvitsema paikallinen asetus on asennettu.

## Gramps Webin konfigurointi

Uudet sukupuut luodaan SharedPostgreSQL-tietokantaan, kun Gramps Web toimii [usean puun tilassa](multi-tree.md) ja `NEW_DB_BACKEND`-konfigurointivaihtoehto on asetettu arvoon `sharedpostgresql`. Yllä olevan Docker Compose -asetuksen kanssa lisää seuraava `environment:`-avaimen alle `grampsweb`-palvelussa `docker-compose.yml`-tiedostossa:

```yaml
      # ota käyttöön usean puun tila
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # luo uusia puita SharedPostgreSQL-tietokantaan
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQL-palvelimen isäntä ja portti. 
      # isäntä on yllä olevan PostgreSQL-palvelun nimi
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Tunnistetietojen on vastattava PostgreSQL-säilössä käytettyjä
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Katso [Konfigurointi](configuration.md) saadaksesi kuvauksen kaikista näistä vaihtoehdoista. Huomaa, että isäntä ja portti tallennetaan jokaisen puun yhteydessä, kun se luodaan, joten niiden muuttaminen myöhemmin vaikuttaa vain uusiin puihin.

## Puun luominen ja tietojen tuominen

Uuden puun luomiseksi POSTaa `/trees/`-pisteeseen kuten on kuvattu [Useiden puiden isännöinnin asetuksissa](multi-tree.md#create-a-new-tree). Vastaus sisältää uuden puun ID:n, jota tarvitset [puun omistajan tilin luomiseen](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Kun puun omistaja on kirjautunut sisään, hän voi [tuoda](../administration/import.md) olemassa olevan sukupuun, esim. Gramps XML -tiedoston, joka on viety Gramps Desktopista, verkkoliittymän kautta.

## PostgreSQL-tietokannan käyttäminen käyttäjätietokannan varten

Käyttäjätietokanta on yleensä SQLite-tiedosto, riippumatta siitä, missä sukupuut isännöidään. Käyttääksesi PostgreSQL:ää sen sijaan, aseta `USER_DB_URI`-konfigurointivaihtoehto PostgreSQL-tietokannan URL-osoitteeksi. Yllä olevan `gramps-postgres`-kuvan kanssa käytä sen `grampswebuser`-tietokantaa:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## PostgreSQL-tietokannan käyttäminen hakemistoa varten

Hakemisto tallennetaan oletusarvoisesti myös SQLiteen. Käyttääksesi PostgreSQL:ää sen sijaan, aseta `SEARCH_INDEX_DB_URI`-konfigurointivaihtoehto PostgreSQL-tietokannan URL-osoitteeksi. Yllä olevan `gramps-postgres`-kuvan kanssa voit käyttää sen `gramps`-tietokantaa, riippumatta siitä, isännöidäänkö sukupuitasi siellä myös:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Puun siirtäminen PostgreSQL-lisäosasta SharedPostgreSQL:ään

Vanhemmat asennukset saattavat isännöidä sukupuuta PostgreSQL-lisäosalla, joka tallentaa yhden puun per tietokanta ja on poistettu käytöstä. Selvittääksesi, mitä lisäosaa puu käyttää, tarkista tiedosto `database.txt` sukupuun alihakemistosta Gramps-tietokantahakemistossa: se sisältää `postgresql` poistettavasta PostgreSQL-lisäosasta ja `sharedpostgresql` SharedPostgreSQL:stä.

Siirtääksesi puun PostgreSQL-lisäosasta SharedPostgreSQL:ään saman asennuksen sisällä, säilyttäen käyttäjätilisi ja mediasi:

1. [Varmuuskopioi sukupuusi](../administration/export.md#back-up-your-family-tree) Gramps XML (`.gramps`) -tiedostona, käyttäen tiliä, joka voi nähdä yksityiset tiedot.
2. Muuta asetuksiasi kuten on kuvattu [Gramps Webin konfiguroinnissa](#configuring-gramps-web). Voit jatkaa olemassa olevan `gramps-postgres`-säilön käyttöä.
3. [Luo uusi puu](multi-tree.md#create-a-new-tree) ja huomaa sen puun ID.
4. Määritä olemassa olevat käyttäjätilisi uudelle puulle, kuten on kuvattu [Siirrä olemassa oleva käyttäjätietokanta](multi-tree.md#migrate-existing-user-database).
5. Siirrä mediasi uusiin odotettuihin sijainteihin, kuten on kuvattu [Siirrä olemassa olevat mediasi](multi-tree.md#migrate-existing-media-files).
6. Kirjaudu sisään ja [tuo](../administration/import.md) Gramps XML -tiedosto uuteen puuhun.

Pidä Gramps XML -tiedostoa, kunnes olet tarkistanut, että uusi puu on täydellinen.

Jos siirryt erilliseen Gramps Web -asennukseen, noudata vaiheita [Siirrä toiseen Gramps Web -instanssiin](../administration/export.md#move-to-a-different-gramps-web-instance).

## Ongelmat

Ongelmatilanteissa seuraa Gramps Webin ja PostgreSQL-palvelimen lokitulostetta. Dockerin tapauksessa tämä saavutetaan seuraavasti:

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Jos epäilet, että Gramps Webissä (tai dokumentaatiossa) on ongelma, ilmoita siitä [Githubissa](https://github.com/gramps-project/gramps-web-api/issues).
