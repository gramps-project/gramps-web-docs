Gramps Webin kokeileminen paikallisella tietokoneellasi (Linux, Mac tai Windows) ilman, että se häiritsee Gramps Desktop -asennustasi, onnistuu käyttämällä Dockeria seuraavalla komennolla:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Tämä tekee uuden, tyhjän Gramps Web -instanssin saataville osoitteessa [http://localhost:5055](http://localhost:5055), jossa voit luoda ylläpitäjäkäyttäjän ja tuoda Gramps XML -tiedoston.

!!! info
    Koska tämä yksinkertainen asennus ei salli pitkien tehtävien suorittamista erillisessä prosessissa, suuren Gramps XML -tiedoston tuonti saattaa epäonnistua aikakatkaisun vuoksi ensimmäisen käytön avustajassa.

Käyttääksesi tietokoneesi mediasisältöjä voit liittää Grampsin mediasivuston konttiin seuraavalla komennolla

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Huomaa, että tämä ei tallenna tekemäsi muutoksia tietokantaan, kun käynnistät kontin uudelleen. Jotta Gramps Web olisi oikein asetettu, jatka lukemista [Deployment](deployment.md).
