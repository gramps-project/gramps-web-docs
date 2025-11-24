# Gramps Webin päivitys

Jos käytät yhtä Docker Composeen perustuvaa asennusmenetelmää, Gramps Webin päivittäminen uusimpaan versioon on yksinkertaista. Siirry kansioon, jossa `docker-compose.yml` sijaitsee, ja suorita seuraavat komennot

```bash
docker compose pull
docker compose up -d
```

Pienissä versiomuutoksissa [Gramps Web API](https://github.com/gramps-project/gramps-web-api) -sovelluksessa tämä on kaikki, mitä tarvitaan. Seuraa kuitenkin [Gramps Web API:n julkaisumuistiinpanoja](https://github.com/gramps-project/gramps-web-api/releases), sillä voi olla rikkomisia aiheuttavia muutoksia, jotka vaativat lisähuomiota tai konfiguraatiomuutoksia.

Huomaa, että oletusarvoinen `grampsweb:latest` docker-kuva yhdistää aina API:n uusimman version ja frontendin uusimman version. Jos haluat päivittää kaksi komponenttia erikseen - mikä on mahdollista - tarvitaan monimutkaisempi asennus kuin mitä tässä on kuvattu.
