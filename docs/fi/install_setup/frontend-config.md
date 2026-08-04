# Etusivun muokkaaminen

Gramps Web etusivu on Javascript-sovellus, joka on otettu käyttöön joukkona staattisia HTML-, CSS- ja Javascript-tiedostoja. Normaalisti etusivulle ei tarvitse tehdä erityistä konfigurointia. Kuitenkin, joitakin käyttäytymisiä voidaan muuttaa asettamalla asianmukaiset vaihtoehdot `config.js` -tiedostoon jakelun juureen.

Tiedoston tulisi olla seuraavanlainen:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Seuraavat vaihtoehtoavaimet ovat käytössä.

Avaimen nimi | Tyyppi | Kuvaus 
----|-----|-----------
`hideDNALink` | boolean | Jos tosi, piilota DNA-linkki navigointipalkista.
`hideRegisterLink` | boolean | Jos tosi, piilota rekisteröintilinkki kirjautumissivulta. Tätä tulisi käyttää monipuun käyttöönottojen yhteydessä.
`loginRedirect` | string | URL, johon ohjataan, kun ei ole kirjautunut sisään ja navigoi mille tahansa muulle sivulle kuin "login" tai "register"
`mapBaseStyleLight` | string | MapLibre-tyylin URL peruskartalle vaaleassa teemassa (oletus: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | MapLibre-tyylin URL peruskartalle tummassa teemassa (oletus: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | MapLibre-tyylin URL OpenHistoricalMap-peitteelle (oletus: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
