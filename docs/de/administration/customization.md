# Baum anpassen

Baumeigentümer und Administratoren können den Namen und das Aussehen des Baums sowie dessen Startseite für alle Benutzer anpassen. Diese Einstellungen befinden sich im Abschnitt **Baumeinstellungen** und **Anpassung** der [Administrations-Einstellungen](settings.md).

## Name des Stammbaums

!!! note
    Das Umbenennen des Baums funktioniert nur in einer [Multi-Baum-Konfiguration](../install_setup/multi-tree.md) oder wenn `TREE_ID` explizit in der [Serverkonfiguration](../install_setup/configuration.md) gesetzt ist. Bei einer Standardinstallation mit nur einem Baum ohne gesetztes `TREE_ID` wird ein Fehler angezeigt.

Dies ermöglicht das Ändern des Namens der zugrunde liegenden Gramps-Stammbaum-Datenbank. Geben Sie einen neuen Namen ein und klicken Sie auf **Umbenennen**, um die Änderungen anzuwenden.

!!! tip
    Wenn Sie nur den Namen ändern möchten, der in der App-Leiste angezeigt wird, ohne die Datenbank umzubenennen, verwenden Sie stattdessen die Einstellung [App-Titel](#app-title).

## Informationen zum Forscher

Legen Sie den Namen, die Adresse und die Kontaktdaten des Hauptforschers fest. Diese Informationen sind in Exporten (z.B. GEDCOM-Dateien) eingebettet.

## Farbthemen

Legen Sie eine benutzerdefinierte **Primärfarbe** und **Akzentfarbe** für die Gramps-Weboberfläche fest. Diese Farben werden für alle Benutzer dieses Baums angewendet und treten sofort nach dem Speichern in Kraft.

Verwenden Sie die Farbauswähler, um Farben auszuwählen, und klicken Sie dann auf **Speichern**. Klicken Sie auf **Zurücksetzen**, um die Standardwerte wiederherzustellen.

## App-Titel

Legen Sie einen benutzerdefinierten Titel für die Anwendung fest. Wenn festgelegt, überschreibt dies den Namen des Stammbaums in der Titelleiste des Browsers und der oberen App-Leiste.

Geben Sie einen Titel ein und klicken Sie auf **Speichern**. Lassen Sie das Feld leer, um den Standardwert (den Namen des Stammbaums) zu verwenden.

## Hinweis zur Startseite

Wählen Sie ein Gramps **Notiz**-Objekt aus, das auf der Startseite des Dashboards angezeigt werden soll. Der Inhalt der Notiz wird unter den Hauptspalten des Dashboards angezeigt und ist für alle Benutzer sichtbar, die Zugriff auf den Baum haben.

Verwenden Sie den Objektwähler, um nach einer Notiz zu suchen und eine auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um den aktuellen Hinweis auf der Startseite zu löschen.

## Bild der Startseite

Wählen Sie ein Gramps **Medien**-Objekt aus, das als Bild auf der Startseite des Dashboards angezeigt werden soll. In Kombination mit einem Hinweis auf der Startseite erscheint das Bild neben dem Notiztext. Ohne eine Notiz wird nur das Bild angezeigt.

Verwenden Sie den Objektwähler, um nach einem Medienobjekt zu suchen und eines auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um das aktuelle Bild auf der Startseite zu löschen.

## Export-/Importeinstellungen

Baumebene Einstellungen (App-Titel, Farbthemen, Hinweis/Bild der Startseite usw.) können als JSON-Datei zur Sicherung oder zum Kopieren in eine andere Gramps-Webinstanz exportiert werden.

- Klicken Sie auf **Einstellungen exportieren**, um die aktuellen Einstellungen als JSON-Datei herunterzuladen.
- Klicken Sie auf **Baumeinstellungen importieren**, um eine zuvor exportierte JSON-Datei hochzuladen und die Einstellungen anzuwenden.
