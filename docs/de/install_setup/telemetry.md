# Telemetrie

Ab der Gramps Web API-Version 3.2.0 sendet Gramps Web standardmäßig alle 24 Stunden vollständig anonymisierte Telemetriedaten an einen vom Gramps-Web-Team kontrollierten Analyseendpunkt. Diese Seite enthält Informationen zu den erhobenen Telemetriedaten, ihrer Verwendung und dazu, wie du die Telemetrie bei Bedarf deaktivieren kannst.

## Welche Daten werden erhoben?

Bei den Telemetriedaten handelt es sich um eine kleine JSON-Nutzlast der folgenden Form:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Wie du selbst [im Quellcode](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87) überprüfen kannst, sind die Server- und Baumkennungen für den Server bzw. Baum eindeutig, enthalten jedoch keine personenbezogenen Daten. Der `timestamp` ist die aktuelle Zeit als Unix-Zeitstempel.

## Warum werden die Daten erhoben?

Das einmal tägliche Senden einer eindeutigen Kennung ermöglicht es dem Gramps-Web-Team, zu verfolgen, wie viele eindeutige Server Gramps Web ausführen und wie viele eindeutige Bäume verwendet werden.

Dies ist wichtig, um die Auswirkungen auf externe Dienste zu verstehen, die von Gramps Web verwendet werden, beispielsweise Kartenkacheln.

## Wie werden die Daten erhoben?

Wenn eine Anfrage an deinen Gramps-Web-API-Server gestellt wird, wird geprüft, ob in den letzten 24 Stunden Telemetriedaten gesendet wurden (indem ein Schlüssel im lokalen Cache überprüft wird). Falls nicht, wird die oben aufgeführte Nutzlast an einen Endpunkt gesendet, der die Daten protokolliert.

Der Protokollierungsendpunkt wird auf Google Cloud Run gehostet und direkt aus einem [Open-Source-Repository](https://github.com/DavidMStraub/cloud-run-telemetry) bereitgestellt, sodass du überprüfen kannst, wie die Daten verarbeitet werden.

## Was geschieht mit den Daten?

In erster Linie wird vom Gramps-Web-Team keinerlei Daten verwendet, die über die anonymisierte Nutzlast hinausgehen und theoretisch erhoben werden könnten (beispielsweise die IP-Adresse des Servers).

Die erhobenen anonymisierten IDs und der Zeitstempel werden aggregiert, um Diagramme wie die folgenden zu erstellen:

- Anzahl der aktiven Gramps-Web-Installationen im Zeitverlauf
- Anzahl der aktiven Gramps-Web-Bäume im Zeitverlauf

Diese Diagramme werden auf der Gramps-Web-Dokumentationsseite veröffentlicht.

## Wie kann die Telemetrie deaktiviert werden?

Da die Statistikdaten für das Gramps-Web-Team nützlich sind und wir sichergestellt haben, dass keine personenbezogenen Daten gesendet werden, **wären wir dir dankbar, wenn du die Telemetrie nicht deaktivierst!**

Dennoch gibt Gramps Web den Benutzern die vollständige Kontrolle, sodass du die Funktion natürlich deaktivieren kannst, wenn du möchtest.

Setze dazu einfach die Konfigurationsoption `DISABLE_TELEMETRY` auf `True` (z. B. indem du die Umgebungsvariable `GRAMPSWEB_DISABLE_TELEMETRY` auf `true` setzt &ndash; Einzelheiten findest du in der [Konfigurationsdokumentation](configuration.md)).
