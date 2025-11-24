# Telemetrie

Seit der Gramps Web API Version 3.2.0 sendet Gramps Web standardmäßig alle 24 Stunden vollständig anonymisierte Telemetriedaten an einen von dem Gramps Web-Team kontrollierten Analyse-Endpunkt. Diese Seite enthält Informationen über die gesammelten Telemetriedaten, wie sie verwendet werden und wie man sie bei Bedarf deaktivieren kann.

## Welche Daten werden gesammelt?

Die Telemetriedaten sind eine kleine JSON-Nutzlast in folgendem Format:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Wie Sie selbst [im Quellcode](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87) überprüfen können, sind die Server- und Baum-Identifikatoren einzigartig für den Server und den Baum, enthalten jedoch keine personenbezogenen Daten. Der `timestamp` ist die aktuelle Zeit als Unix-Zeitstempel.

## Warum werden die Daten gesammelt?

Das Senden eines eindeutigen Identifikators einmal täglich ermöglicht es dem Gramps Web-Team, nachzuvollziehen, wie viele eindeutige Server Gramps Web ausführen und wie viele eindeutige Bäume verwendet werden.

Dies ist wichtig, um die Auswirkungen auf externe Dienste zu verstehen, die von Gramps Web verwendet werden, wie z. B. Kartenkacheln.

## Wie werden die Daten gesammelt?

Wenn eine Anfrage an Ihren Gramps Web API-Server gestellt wird, überprüft dieser, ob in den letzten 24 Stunden Telemetrie gesendet wurde (indem ein Schlüssel im lokalen Cache überprüft wird). Wenn nicht, wird die oben genannte Nutzlast an einen Endpunkt gesendet, der die Daten protokolliert.

Der Protokollierungsendpunkt wird auf Google Cloud Run gehostet und direkt aus einem [Open-Source-Repository](https://github.com/DavidMStraub/cloud-run-telemetry) bereitgestellt, sodass Sie überprüfen können, wie die Daten verarbeitet werden.

## Was wird mit den Daten gemacht?

Zunächst einmal wird das Gramps Web-Team keine Daten über die anonymisierte Nutzlast hinaus verwenden, die hypothetisch gesammelt werden könnten (wie z. B. die IP-Adresse des Servers).

Die gesammelten anonymisierten IDs und der Zeitstempel werden aggregiert, um Grafiken zu erstellen, wie zum Beispiel:

- Anzahl der aktiven Gramps Web-Installationen in Abhängigkeit von der Zeit
- Anzahl der aktiven Gramps Web-Bäume in Abhängigkeit von der Zeit

Diese Grafiken werden auf der Dokumentationsseite von Gramps Web veröffentlicht.

## Wie deaktiviert man die Telemetrie?

Da die Statistikdaten für das Gramps Web-Team nützlich sind und wir sichergestellt haben, dass keine personenbezogenen Daten gesendet werden, **wären wir dankbar, wenn Sie die Telemetrie nicht deaktivieren!**

Dennoch gibt Gramps Web den Benutzern die volle Kontrolle, sodass Sie die Funktion selbstverständlich deaktivieren können, wenn Sie möchten.

Um dies zu tun, setzen Sie einfach die Konfigurationsoption `DISABLE_TELEMETRY` auf `True` (z. B. indem Sie die Umgebungsvariable `GRAMPSWEB_DISABLE_TELEMETRY` auf `true` setzen – siehe die [Konfigurationsdokumentation](configuration.md) für Details).
