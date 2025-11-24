# Gramps Web Installation / Einrichtung

Dieser Abschnitt behandelt die Installation und Einrichtung von Gramps Web sowie andere Optionen, um zu beginnen.

## Erste Schritte mit Gramps Web

Gramps Web ist eine Webanwendung, die auf einem Server läuft und über den Webbrowser aufgerufen wird. Sie soll authentifizierten Benutzern über das Internet zugänglich gemacht werden.

Wenn Sie Gramps Web für Ihre genealogischen Forschungsdaten verwenden möchten, müssen Sie eine der folgenden Optionen wählen:

1. Selbsthosting auf eigener Hardware
2. Selbsthosting in der Cloud
3. Anmeldung für eine gehostete Instanz

Während die erste Option maximale Flexibilität und Kontrolle bietet, kann sie auch technisch herausfordernd sein.

!!! tip
    Eines der Hauptprinzipien von Gramps Web ist es, die Benutzer jederzeit die Kontrolle über ihre eigenen Daten zu geben, sodass das Migrieren von Daten von einer Instanz zur anderen einfach ist. Machen Sie sich keine Sorgen, dass Sie nach der Wahl einer der Optionen festgelegt sind!

## Selbsthosting auf eigener Hardware

Der bequemste Weg, Gramps Web selbst zu hosten, ist über Docker Compose. Wir bieten auch Docker-Images für die ARM-Architektur an, sodass Sie Gramps Web auf einem Raspberry Pi in Ihrem Keller ausführen können.

Siehe [Bereitstellung mit Docker](deployment.md) für Installationsanweisungen.

## Selbsthosting in der Cloud

Die Installation von Gramps Web kann herausfordernder sein als bei anderen, einfachen Webanwendungen und ist nicht mit gewöhnlichen "Shared Hosting"-Anbietern kompatibel. Sie können sich für einen virtuellen Server anmelden und Gramps Web [manuell](deployment.md) installieren.

Eine einfachere Option ist die Verwendung eines vorinstallierten Cloud-Images. Ein Beispiel ist unsere [DigitalOcean 1-Klick-App](digital_ocean.md).

## Anmeldung für eine gehostete Instanz

Ein gehostetes Gramps Web ist der einfachste Weg, um mit Gramps Web zu beginnen, da keine Installation oder Konfiguration erforderlich ist.

Hier ist eine Liste von dedizierten Hosting-Anbietern für Gramps Web (die Gramps Open-Source-Community übernimmt keine Verantwortung für deren Dienste):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), angeboten von einem der Hauptbeiträger von Gramps Web

Wenn Sie eine gehostete Option für Gramps Web verwenden, können Sie den Rest dieses Abschnitts überspringen und direkt zum Abschnitt [Administration](../administration/admin.md) springen.
