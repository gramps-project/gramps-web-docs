# Frontendin mukauttaminen

Gramps Web -frontend on Javascript-sovellus, joka on otettu käyttöön joukkona staattisia HTML-, CSS- ja Javascript-tiedostoja. Normaalisti frontendille ei tarvita erityistä konfiguraatiota. Kuitenkin, joitakin käyttäytymisiä voidaan muuttaa asettamalla asianmukaiset vaihtoehdot `config.js`-tiedostoon jakelun juureen.

Tiedoston tulisi olla seuraavanlainen:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Seuraavat vaihtoehtoavaimet ovat olemassa.

Avain | Tyyppi | Kuvaus 
-----|-------|-----------
`hideDNALink` | boolean | Jos tosi, piilota DNA-linkki navigointipalkista.
`hideRegisterLink` | boolean | Jos tosi, piilota rekisteröintilinkki kirjautumissivulta. Tätä tulisi käyttää monipuun käyttöönottojen yhteydessä.
`loginRedirect` | string | URL, johon ohjataan, kun ei ole kirjautunut sisään ja navigoi mihin tahansa muuhun sivuun kuin "login" tai "register"
`leafletTileUrl` | string | Mukautettu laattojen URL Leaflet-kartoille
`leafletTileSize` | number | Mukautettu laattojen koko Leaflet-kartoille
`leafletZoomOffset` | number | Mukautettu zoom-offset Leaflet-kartoille
`leafletTileAttribution` | string | Mukautettu attribuutio Leaflet-kartoille
