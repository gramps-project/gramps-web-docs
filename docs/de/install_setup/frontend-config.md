# Anpassen des Frontends

Das Gramps Web-Frontend ist eine Javascript-Anwendung, die als eine Sammlung von statischen HTML-, CSS- und Javascript-Dateien bereitgestellt wird. Normalerweise ist keine spezielle Konfiguration für das Frontend erforderlich. Einige Verhaltensweisen können jedoch durch das Setzen entsprechender Optionen in der Datei `config.js` im Stammverzeichnis der Distribution geändert werden.

Die Datei sollte die folgende Struktur haben:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Die folgenden Optionsschlüssel existieren.

Schlüssel | Typ | Beschreibung 
----|-----|-----------
`hideDNALink` | boolean | Wenn wahr, den DNA-Link in der Navigationsleiste ausblenden.
`hideRegisterLink` | boolean | Wenn wahr, den Registrierungslink auf der Anmeldeseite ausblenden. Dies sollte für Multi-Baum-Bereitstellungen verwendet werden.
`loginRedirect` | string | URL, zu der umgeleitet wird, wenn nicht angemeldet und zu einer anderen Seite als "login" oder "register" navigiert wird.
`mapBaseStyleLight` | string | MapLibre-Stil-URL für die Basis-Karte im hellen Thema (Standard: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | MapLibre-Stil-URL für die Basis-Karte im dunklen Thema (Standard: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | MapLibre-Stil-URL für das OpenHistoricalMap-Overlay (Standard: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
