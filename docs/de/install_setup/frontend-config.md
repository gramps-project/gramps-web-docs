# Anpassen des Frontends

Das Gramps Web-Frontend ist eine Javascript-Anwendung, die als eine Sammlung von statischen HTML-, CSS- und Javascript-Dateien bereitgestellt wird. Normalerweise ist keine spezielle Konfiguration für das Frontend erforderlich. Einige Verhaltensweisen können jedoch durch das Setzen entsprechender Optionen in der Datei `config.js` im Stammverzeichnis der Verteilung geändert werden.

Die Datei sollte die folgende Struktur haben:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Die folgenden Optionsschlüssel existieren.

Key |Typ | Beschreibung 
----|-----|-----------
`hideDNALink` | boolean | Wenn wahr, den DNA-Link in der Navigationsleiste ausblenden.
`hideRegisterLink` | boolean | Wenn wahr, den Registrierungslink auf der Anmeldeseite ausblenden. Dies sollte für Multi-Baum-Bereitstellungen verwendet werden.
`loginRedirect` | string | URL, zu der umgeleitet wird, wenn nicht eingeloggt und zu einer anderen Seite als "login" oder "register" navigiert wird.
`leafletTileUrl` | string | Benutzerdefinierte Kachel-URL für Leaflet-Karten
`leafletTileSize` | number | Benutzerdefinierte Kachelgröße für Leaflet-Karten
`leafletZoomOffset` | number | Benutzerdefinierter Zoom-Offset für Leaflet-Karten
`leafletTileAttribution` | string | Benutzerdefinierte Attribution für Leaflet-Karten
