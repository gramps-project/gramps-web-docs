# Tilpasning af frontend

Gramps Web frontend er en Javascript-applikation, der distribueres som et sæt af statiske HTML-, CSS- og Javascript-filer. Normalt er der ikke behov for nogen særlig konfiguration af frontend. Dog kan nogle adfærd ændres ved at indstille de relevante muligheder i `config.js`-filen i roden af distributionen.

Filen skal have følgende struktur:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Følgende mulighedsnøgler findes.

Nøgle | Type | Beskrivelse 
----|-----|-----------
`hideDNALink` | boolean | Hvis sand, skjul DNA-linket på navigationslinjen.
`hideRegisterLink` | boolean | Hvis sand, skjul registreringslinket på login-siden. Dette bør bruges til multi-træ distributioner.
`loginRedirect` | string | URL at omdirigere til, når man ikke er logget ind og navigerer til en hvilken som helst side, der ikke er "login" eller "register"
`leafletTileUrl` | string | Tilpasset tile-URL til Leaflet-kort
`leafletTileSize` | number | Tilpasset tile-størrelse til Leaflet-kort
`leafletZoomOffset` | number | Tilpasset zoom-offset til Leaflet-kort
`leafletTileAttribution` | string | Tilpasset attribution til Leaflet-kort
