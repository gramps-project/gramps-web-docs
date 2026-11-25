# Anpassen des Frontends

Das Gramps-Web-Frontend ist eine Javascript-Anwendung, die als Sammlung statischer HTML-, CSS- und Javascript-Dateien bereitgestellt wird. Normalerweise ist für das Frontend keine spezielle Konfiguration erforderlich. Einige Verhaltensweisen können jedoch durch das Festlegen entsprechender Optionen in der Datei `config.js` im Stammverzeichnis der Distribution geändert werden.

Die Datei sollte die folgende Struktur haben:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Die folgenden Optionsschlüssel sind verfügbar.

Schlüssel |Typ | Beschreibung 
----|-----|-----------
`hideDNALink` | boolean | Wenn true, wird der DNA-Link in der Navigationsleiste ausgeblendet.
`hideRegisterLink` | boolean | Wenn true, wird der Registrierungslink auf der Anmeldeseite ausgeblendet. Dies sollte für Bereitstellungen mit mehreren Stammbäumen verwendet werden.
`loginRedirect` | string | URL, zu der weitergeleitet wird, wenn du nicht angemeldet bist und zu einer beliebigen Seite außer „login“ oder „register“ navigierst.
`mapBaseStyleLight` | string | MapLibre-Stil-URL für die Basiskarte im hellen Design (Standard: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | MapLibre-Stil-URL für die Basiskarte im dunklen Design (Standard: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | MapLibre-Stil-URL für das OpenHistoricalMap-Overlay (Standard: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
`mapWikidata` | boolean | Wenn false, wird die Ebene [Wikidata-Gebäude](../user-guide/map.md#wikidata-buildings) aus der Karte entfernt (Standard: true)
