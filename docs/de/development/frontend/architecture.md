# Architektur

## Komponenten

Das Frontend ist aus Webkomponenten aufgebaut. Sie sind in den JavaScript-Dateien im Verzeichnis `src` definiert.

Typischerweise definiert jede Datei eine Komponente, die mit
```javascript
class GrampsjsSomeElement extends LitElement
```
beginnt und mit
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
endet. Dadurch wird das neue HTML-Element `grampsjs-some-element` definiert, das an anderer Stelle verwendet werden kann.

Der in `index.html` eingebundene Haupteinstiegspunkt ist das in `GrampsJs.js` definierte Element `gramps-js`. Es enthält die Definition aller einzelnen Seiten (die einfach Elementen entsprechen, die abhängig von der Route/URL angezeigt oder ausgeblendet werden), des Menüs und des Routings.

Die Komponenten im Verzeichnis `src/views` entsprechen normalerweise Komponenten für vollständige Seiten, die Daten vom Backend abrufen (z. B. die Ansicht der Personenliste), während Komponenten in `src/components` normalerweise kleinere Bausteine sind, die innerhalb der Ansichten verwendet werden und ihre Daten über Attribute erhalten, die von ihrem übergeordneten Element bereitgestellt werden. Diese Trennung ist jedoch nicht strikt.

## Datenfluss

Daten werden über die Methoden `apiGet`, `apiPut` und `apiPost` in `src/api.js` mit dem Backend/API ausgetauscht, die sich automatisch um die Authentifizierung kümmern.

Daten werden von übergeordneten Komponenten über Eigenschaften an untergeordnete Komponenten weitergegeben (siehe z. B. die [Lit-Dokumentation](https://lit.dev/docs/components/properties/)).

Wenn Daten von einer untergeordneten Komponente an eine übergeordnete Komponente zurückgegeben werden müssen, werden benutzerdefinierte Ereignisse verwendet. Diese können mit der Funktion `fireEvent` in `src/api.js` ausgelöst und mithilfe der `@`-Syntax von Lit abgehört werden [(Dokumentation)](https://lit.dev/docs/components/events/).

## Authentifizierung

Das Aktualisierungstoken und das Authentifizierungstoken werden im lokalen Speicher des Browsers gespeichert. Wenn ein API-Aufruf erfolgt und das Token abgelaufen ist, wird das gespeicherte Aktualisierungstoken verwendet, um ein neues Zugriffstoken abzurufen, und der API-Aufruf wird wiederholt.

Der Autorisierungsbereich des Benutzers, der in den Ansprüchen des Zugriffstokens gespeichert ist, wird mit der Funktion `getPermissions` abgerufen und im übergeordneten Element `GrampsJs` verwendet, um die booleschen Eigenschaften `canAdd`, `canEdit`, `canManageUsers` festzulegen. Diese werden an untergeordnete Elemente weitergegeben, um autorisierungsspezifische Funktionen zu implementieren.
