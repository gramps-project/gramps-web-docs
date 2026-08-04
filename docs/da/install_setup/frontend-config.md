# Tilpasning af frontend

Gramps Web frontend er en Javascript-applikation, der distribueres som et sæt af statiske HTML-, CSS- og Javascript-filer. Normalt er der ikke behov for nogen særlig konfiguration af frontend. Dog kan nogle adfærd ændres ved at indstille passende muligheder i `config.js`-filen i roden af distributionen.

Filens struktur skal være som følger:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Følgende mulighedsnøgler eksisterer.

Nøgle | Type | Beskrivelse 
----|-----|-----------
`hideDNALink` | boolean | Hvis sandt, skjul DNA-linket på navigationslinjen.
`hideRegisterLink` | boolean | Hvis sandt, skjul registreringslinket på login-siden. Dette bør bruges til multi-træ distributioner.
`loginRedirect` | string | URL at omdirigere til, når man ikke er logget ind og navigerer til en hvilken som helst side, der ikke er "login" eller "register"
`mapBaseStyleLight` | string | MapLibre stil URL for basiskortet i lys tema (standard: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | MapLibre stil URL for basiskortet i mørkt tema (standard: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | MapLibre stil URL for OpenHistoricalMap overlay (standard: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
