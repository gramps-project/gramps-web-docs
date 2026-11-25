# Gramps Web installieren / einrichten

In diesem Abschnitt geht es um die Installation und Einrichtung von Gramps Web sowie um weitere Möglichkeiten für den Einstieg.

## Erste Schritte mit Gramps Web

Gramps Web ist eine Web-App, die auf einem Server läuft und über den Webbrowser aufgerufen wird. Sie ist dafür vorgesehen, authentifizierten Benutzern über das Internet zugänglich gemacht zu werden.

Wenn du Gramps Web für deine genealogischen Forschungsdaten verwenden möchtest, musst du eine der folgenden Optionen wählen:

1. Selbsthosting auf deiner eigenen Hardware
2. Selbsthosting in der Cloud
3. Registrierung für eine gehostete Instanz

Während die erste Option maximale Flexibilität und Kontrolle bietet, kann sie auch technisch anspruchsvoll sein.

!!! tip
    Eines der Hauptprinzipien von Gramps Web besteht darin, dass du jederzeit die Kontrolle über deine eigenen Daten behältst. Daher ist die Migration von Daten von einer Instanz zu einer anderen einfach. Mach dir keine Sorgen, nach der Wahl einer der Optionen an diese gebunden zu sein!

## Selbsthosting auf deiner eigenen Hardware

Die bequemste Möglichkeit, Gramps Web selbst zu hosten, ist Docker Compose. Wir stellen auch Docker-Images für die ARM-Architektur bereit, sodass du Gramps Web auf einem Raspberry Pi in deinem Keller ausführen kannst.

Eine Anleitung zur Einrichtung findest du unter [Mit Docker bereitstellen](deployment.md).


## Selbsthosting in der Cloud

Die Installation von Gramps Web kann anspruchsvoller sein als die anderer, einfacher Webanwendungen und ist mit gewöhnlichen „Shared-Hosting“-Anbietern nicht kompatibel. Du kannst dich für einen virtuellen Server registrieren und Gramps Web [manuell](deployment.md) installieren.

Eine einfachere Möglichkeit besteht darin, ein vorinstalliertes Cloud-Image zu verwenden. Ein Beispiel ist unsere [DigitalOcean-1-Klick-App](digital_ocean.md).

## Für eine gehostete Instanz registrieren

Ein gehostetes Gramps Web ist der einfachste Weg, mit Gramps Web zu beginnen, da keine Installation oder Konfiguration erforderlich ist.

Hier ist eine Liste dedizierter Hosting-Anbieter für Gramps Web (die Open-Source-Community von Gramps übernimmt keine Verantwortung für deren Dienste):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), angeboten von einem der Hauptbeitragenden von Gramps Web

Wenn du eine gehostete Option für Gramps Web verwendest, kannst du den Rest dieses Abschnitts überspringen und direkt zum Abschnitt [Administration](../administration/admin.md) wechseln.
