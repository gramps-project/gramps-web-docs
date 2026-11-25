# Daten prüfen und verifizieren

Der Abschnitt **Stammbaumverarbeitung** in den [Administrationseinstellungen](settings.md) enthält zwei Werkzeuge zur Prüfung des Stammbaums: eines für technische Probleme in der Datenbank und eines für unplausible Daten.

## Datenbank prüfen und reparieren

Dieses Werkzeug prüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt diejenigen, die behoben werden können – analog zum [Werkzeug „Datenbank prüfen und reparieren“](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicke auf **Prüfen und reparieren** und warte, bis die Fortschrittsanzeige abgeschlossen ist. Das Ergebnis wird unterhalb der Schaltfläche angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsmeldung angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der angewendeten Korrekturen angezeigt.

Führe dieses Werkzeug aus, wenn unerwartete Fehler oder Verhaltensweisen auftreten, die durch Inkonsistenzen in der Datenbank verursacht sein könnten, z. B. fehlende Beziehungen zwischen Objekten.

## Daten verifizieren

Während [Datenbank prüfen und reparieren](#check-and-repair-database) nach *technischen* Inkonsistenzen sucht, sucht dieses Werkzeug nach *unplausiblen* Daten – analog zum [Werkzeug „Daten verifizieren“](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Es meldet Dinge, die nicht unmöglich, aber unwahrscheinlich genug sind, um sie genauer zu prüfen, z. B. eine 12-jährige Mutter oder eine Person, die 130 Jahre alt wurde.

Unter **Optionen** kannst du die Schwellenwerte für die Tests anpassen – Höchstalter, Mindest- und Höchstalter für die Eheschließung oder das Bekommen von Kindern, maximale Kinderzahl und so weiter – sowie festlegen, ob fehlende oder ungenaue Datumsangaben geschätzt und ob ungültige Datumsangaben wie der 31. Februar gemeldet werden sollen. Die von dir geänderten Optionen werden für den nächsten Durchlauf in deinem Browser gespeichert; **Zurücksetzen** stellt die Standardwerte wieder her.

Klicke zum Starten auf **Daten verifizieren**. Die Prüfung läuft als Hintergrundaufgabe, und die Ergebnisse werden anschließend unter **Ergebnisse der Datenverifizierung** aufgelistet. Dieses Werkzeug nimmt keine Änderungen vor: Es meldet lediglich, was es findet.

!!! note
    Ein Ergebnis ist kein Beweis für einen Fehler. Lange Lebensspannen und große Altersunterschiede kommen tatsächlich vor. Betrachte die Ergebnisse daher als Liste von Dingen, die geprüft werden sollten, und nicht als Liste von Dingen, die korrigiert werden müssen.
