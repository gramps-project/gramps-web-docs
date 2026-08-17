Gramps Webin kokeileminen paikallisella tietokoneellasi (Linux, Mac tai Windows) ilman, että se vaikuttaa Gramps Desktop -asennukseesi, onnistuu käyttämällä Dockeria seuraavalla komennolla:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Tämä tekee uuden, tyhjän Gramps Web -instanssin saataville osoitteessa [http://localhost:5055](http://localhost:5055), jossa voit luoda ylläpitäjäkäyttäjän ja tuoda Gramps XML -tiedoston.

!!! info
    Koska tämä yksinkertainen asennus ei salli pitkien tehtävien suorittamista erillisessä prosessissa, suuren Gramps XML -tiedoston tuonti saattaa epäonnistua aikakatkaisun vuoksi ensimmäisen käynnistysavustajan aikana.


Käyttääksesi mediafilejä tietokoneeltasi voit liittää Grampsin mediahakemiston konttiin seuraavalla komennolla

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Huomaa, että tämä ei tallenna tekemäsi muutoksia tietokantaan, kun käynnistät kontin uudelleen. Jotta voit oikein asentaa Gramps Webin, jatka lukemista [Käyttöönotosta](deployment.md).
