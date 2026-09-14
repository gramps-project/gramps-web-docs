# Erstellen Sie ein Konto für die Hauptperson des Baums

Bevor Sie Gramps Web nutzen können, müssen Sie ein Konto für die Hauptperson des Baums erstellen. Wenn kein Benutzerkonto für einen bestimmten Baum existiert, wird ein Formular angezeigt, um ein Konto zu erstellen. Das Formular hängt von der Serverkonfiguration ab, ob es sich um einen Einzelbaum oder um mehrere Bäume handelt.

## Einzelbaum-Setup: Admin-Konto erstellen

Auf einem Server mit Einzelbaum-Setup, wenn noch kein Benutzerkonto existiert, zeigt das Öffnen von Gramps Web ein Formular zum Erstellen eines Admin-Kontos an. Der Admin-Benutzer wird sowohl der Eigentümer des (einzelnen) Baums als auch der Administrator der Installation sein. Das Formular ermöglicht auch die Konfiguration der E-Mail-Einstellungen, die für E-Mail-Benachrichtigungen benötigt werden (z. B. zum Zurücksetzen eines Benutzerpassworts). Wenn die E-Mail-Konfiguration bereits über eine Konfigurationsdatei oder Umgebungsvariablen auf dem Server hinzugefügt wurde, kann dieser Teil des Formulars leer gelassen werden.

Das Passwort muss zweimal eingegeben werden; das Formular kann nur abgeschickt werden, wenn beide Eingaben übereinstimmen.

Wenn die Instanz bereits eingerichtet wurde, zeigt das Öffnen der Adresse des Formulars eine Nachricht an, die Sie auffordert, sich stattdessen mit einem vorhandenen Konto anzumelden.

## Mehrbaum-Setup: Admin-Konto erstellen

In einem Mehrbaum-Setup wird dasselbe Formular zum Erstellen eines Admin-Kontos angezeigt, wenn keine Benutzer *in irgendeinem Baum* existieren, d. h. wenn der Server gerade erstellt wurde.

## Mehrbaum-Setup: Konto für die Hauptperson des Baums erstellen

In einem Mehrbaum-Setup ist jeder Benutzer an einen einzelnen Baum gebunden. Selbst wenn Benutzer bereits in anderen Bäumen existieren, kann eine Hauptperson über die Weboberfläche erstellt werden, wenn noch kein Eigentümer *für diesen Baum* existiert.

Das Formular zur Erstellung des Eigentümers wird jedoch nicht automatisch auf der Startseite von Gramps Web angezeigt, die für alle Bäume gleich ist. Stattdessen kann es unter `https://my-gramps-instance/firstrun/my-tree-id` erreicht werden, wobei `https://my-gramps-instance` die Basisadresse Ihrer Gramps Web-Installation ist und `my-tree-id` die ID Ihres Baums ist.

Ein möglicher Arbeitsablauf für einen Site-Administrator zur Erstellung eines neuen Baums besteht darin, 

- einen Baum über die REST API zu erstellen und die Baum-ID des neuen Baums zu erhalten
- den Link zum Formular zur Erstellung des Eigentümers mit der entsprechenden Baum-ID an die potenzielle Hauptperson des Baums zu teilen

Das Formular zur Erstellung der Hauptperson des Baums ist analog zum oben beschriebenen Formular zur Erstellung des Admins, mit der Ausnahme, dass es nicht erlaubt ist, die E-Mail-Konfiguration zu ändern (was nur für Admins erlaubt ist).
