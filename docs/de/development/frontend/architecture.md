# Architektur

## Komponenten

Das Frontend besteht aus Webkomponenten. Sie sind in den Javascript-Dateien im Verzeichnis `src` definiert.

Typischerweise definiert jede Datei eine Komponente, beginnend mit
```javascript
class GrampsjsSomeElement extends LitElement
```
und endend mit
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
die das neue HTML-Element `grampsjs-some-element` definiert, das an anderer Stelle verwendet werden kann.

Der Haupt-Einstiegspunkt, der in `index.html` enthalten ist, ist das `gramps-js` Element, das in `GrampsJs.js` definiert ist. Dies enthält die Definition aller einzelnen Seiten (die einfach den Elementen entsprechen, die basierend auf der Route/URL angezeigt oder ausgeblendet werden), das Menü und das Routing.

Die Komponenten im Verzeichnis `src/views` entsprechen normalerweise Vollseitenkomponenten, die Daten vom Backend abrufen (z. B. die Personenlistenansicht), während Komponenten im Verzeichnis `src/components` normalerweise kleinere Bausteine sind, die innerhalb der Ansichten verwendet werden und ihre Daten von Attributen erhalten, die von ihrem übergeordneten Element bereitgestellt werden. Diese Trennung ist jedoch nicht strikt.

## Datenfluss

Daten werden über die Methoden `apiGet`, `apiPut` und `apiPost` in `src/api.js` mit dem Backend/API ausgetauscht, die automatisch die Authentifizierung übernehmen.

Daten werden von übergeordneten Komponenten an untergeordnete Komponenten über Eigenschaften übergeben (siehe z. B. die [Lit-Dokumentation](https://lit.dev/docs/components/properties/)).

Wenn Daten von einer untergeordneten zu einer übergeordneten Komponente zurückgegeben werden müssen, werden benutzerdefinierte Ereignisse verwendet, die mit der Funktion `fireEvent` in `src/api.js` ausgelöst werden können und mit Lits `@`-Syntax [(docs)](https://lit.dev/docs/components/events/) angehört werden.

## Authentifizierung

Das Refresh-Token und das Authentifizierungs-Token werden im lokalen Speicher des Browsers gespeichert. Jedes Mal, wenn ein API-Aufruf getätigt wird und das Token abgelaufen ist, wird das gespeicherte Refresh-Token verwendet, um ein neues Zugriffstoken abzurufen, und der API-Aufruf wird wiederholt.

Der Autorisierungsbereich des Benutzers, der in den Ansprüchen des Zugriffstokens gespeichert ist, wird mit der Funktion `getPermissions` abgerufen und im obersten `GrampsJs`-Element verwendet, um die booleschen Eigenschaften `canAdd`, `canEdit`, `canManageUsers` festzulegen, die an untergeordnete Elemente weitergegeben werden, um autorisierungsspezifische Funktionalitäten zu implementieren.
