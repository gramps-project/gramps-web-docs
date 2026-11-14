# Suchindex

Der **Suchindex**-Bereich der [Verwaltungseinstellungen](settings.md) zeigt den Zustand des Volltextsuchindex und ermöglicht es Ihnen, ihn neu zu erstellen.

## Suchindex verwalten

Gramps Web verwaltet einen Volltextsuchindex, der normalerweise automatisch aktualisiert wird, wann immer sich Daten ändern. Der Statusindikator zeigt, wie viele Objekte derzeit indiziert sind im Vergleich zur Gesamtanzahl der Objekte.

Klicken Sie auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Ein Fortschrittsindikator wird angezeigt, während die Aufgabe im Hintergrund ausgeführt wird. Dies ist selten erforderlich.

Wenn ein Baum noch keinen Suchindex hat, zum Beispiel nach einem Server-Upgrade, das das Indexformat geändert hat, erstellt Gramps Web ihn im Hintergrund, wenn der Baum zum ersten Mal geöffnet wird. Während er erstellt wird, zeigt der Abschnitt "Der Suchindex wird erstellt." anstelle der Zählungen, **Suchindex aktualisieren** ist deaktiviert, und die Suchergebnisse können unvollständig sein. Der Aufbau wird in [Benachrichtigungen](../user-guide/notifications.md) als Aufgabe "Suchindex aktualisieren" angezeigt.
