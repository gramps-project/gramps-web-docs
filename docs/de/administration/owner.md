# Konto für den Baumbesitzer erstellen

Bevor du Gramps Web verwenden kannst, musst du ein Konto für den Baumbesitzer erstellen. Wenn für einen bestimmten Stammbaum kein Benutzerkonto vorhanden ist, wird ein Formular zum Erstellen eines Kontos angezeigt. Das Formular hängt davon ab, ob der Server für einen einzelnen Stammbaum oder für mehrere Stammbäume eingerichtet ist.

## Einrichtung für einen einzelnen Stammbaum: Administratorkonto erstellen

Bei einem Server mit einer Einrichtung für einen einzelnen Stammbaum wird beim Öffnen von Gramps Web ein Formular zum Erstellen eines Administratorkontos angezeigt, wenn noch kein Benutzerkonto vorhanden ist. Der Administrator ist sowohl der Besitzer des (einzelnen) Stammbaums als auch der Administrator der Installation. Über das Formular kannst du außerdem die E-Mail-Konfiguration festlegen, die für E-Mail-Benachrichtigungen benötigt wird (z. B. zum Zurücksetzen eines Benutzerpassworts). Wenn die E-Mail-Konfiguration bereits über eine Konfigurationsdatei oder Umgebungsvariablen auf dem Server hinzugefügt wurde, kann dieser Teil des Formulars leer gelassen werden.

Das Passwort muss zweimal eingegeben werden; das Formular kann nur abgeschickt werden, wenn beide Eingaben übereinstimmen.

Wenn die Instanz bereits eingerichtet wurde, wird beim Öffnen der Adresse des Formulars eine Meldung angezeigt, die dich auffordert, dich stattdessen mit einem vorhandenen Konto anzumelden.

## Einrichtung für mehrere Stammbäume: Administratorkonto erstellen

Bei einer Einrichtung für mehrere Stammbäume wird dasselbe Formular zum Erstellen eines Administratorkontos angezeigt, wenn keine Benutzer *in irgendeinem Stammbaum* vorhanden sind, also wenn der Server gerade erst erstellt wurde.

## Einrichtung für mehrere Stammbäume: Konto für den Baumbesitzer erstellen

Bei einer Einrichtung für mehrere Stammbäume ist jeder Benutzer an einen einzelnen Stammbaum gebunden. Auch wenn bereits Benutzer in anderen Stammbäumen vorhanden sind, kann im Webinterface ein Baumbesitzer erstellt werden, wenn für *diesen Stammbaum* noch kein Besitzer existiert.

Das Formular zum Erstellen des Besitzers wird jedoch nicht automatisch auf der Gramps-Web-Startseite angezeigt, die für alle Stammbäume gleich ist. Stattdessen ist es unter `https://my-gramps-instance/firstrun/my-tree-id` erreichbar, wobei `https://my-gramps-instance` die Basisadresse deiner Gramps-Web-Installation und `my-tree-id` die ID deines Stammbaums ist.

Ein möglicher Ablauf für einen Site-Administrator zum Erstellen eines neuen Stammbaums besteht darin,

- Einen Stammbaum über die REST-API erstellen und dabei die Stammbaum-ID des neuen Stammbaums abrufen
- Den Link zum Formular zum Erstellen des Besitzers mit der entsprechenden Stammbaum-ID an den vorgesehenen Baumbesitzer weitergeben

Das Formular zum Erstellen des Baumbesitzers entspricht dem oben beschriebenen Formular zum Erstellen des Administrators, mit der Ausnahme, dass es keine Möglichkeit bietet, die E-Mail-Konfiguration zu ändern (dies ist nur Administratoren erlaubt).
