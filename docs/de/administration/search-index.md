# Suchindex

Der Abschnitt **Suchindex** in den [Administrationseinstellungen](settings.md) zeigt den Status des Volltextsuchindex an und ermöglicht dir, ihn neu aufzubauen.

## Suchindex verwalten

Gramps Web verwaltet einen Volltextsuchindex, der normalerweise automatisch aktualisiert wird, sobald sich Daten ändern. Die Statusanzeige zeigt, wie viele Objekte derzeit indiziert sind, im Vergleich zur Gesamtzahl der Objekte.

Klicke auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Während der Vorgang im Hintergrund ausgeführt wird, wird eine Fortschrittsanzeige eingeblendet. Dies ist nur selten erforderlich.

Wenn für einen Stammbaum noch kein Suchindex vorhanden ist, beispielsweise nach einem Server-Upgrade, durch das sich das Indexformat geändert hat, erstellt Gramps Web den Index beim ersten Öffnen des Stammbaums im Hintergrund. Während der Erstellung wird im Abschnitt anstelle der Anzahl „Der Suchindex wird erstellt.“ angezeigt, **Suchindex aktualisieren** ist deaktiviert und die Suchergebnisse sind möglicherweise unvollständig. Die Erstellung wird unter [Benachrichtigungen](../user-guide/notifications.md) als Aufgabe „Suchindex aktualisieren“ angezeigt.
