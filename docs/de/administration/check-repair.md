# Überprüfen und Verifizieren von Daten

Der Abschnitt **Familienstammbaumverarbeitung** der [Verwaltungseinstellungen](settings.md) enthält zwei Werkzeuge, die den Familienstammbaum überprüfen: eines auf technische Probleme in der Datenbank und eines auf unplausible Daten.

## Datenbank überprüfen und reparieren

Dieses Werkzeug überprüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt die, die es kann – analog zum [Werkzeug Datenbank überprüfen und reparieren](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicken Sie auf **Überprüfen und Reparieren** und warten Sie, bis der Fortschrittsindikator abgeschlossen ist. Das Ergebnis wird unter dem Button angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsnachricht angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der durchgeführten Korrekturen angezeigt.

Führen Sie dieses Werkzeug aus, wenn Sie unerwartete Fehler oder Verhaltensweisen feststellen, die durch Datenbankinkonsistenzen verursacht werden könnten, wie z. B. fehlende Beziehungen zwischen Objekten.

## Daten verifizieren

Während [Datenbank überprüfen und reparieren](#check-and-repair-database) nach *technischen* Inkonsistenzen sucht, sucht dieses Werkzeug nach *unplausiblen* Daten – analog zum [Werkzeug Daten verifizieren](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Es berichtet über Dinge, die nicht unmöglich sind, aber unwahrscheinlich genug, um einen zweiten Blick wert zu sein, wie eine Mutter im Alter von 12 oder eine Person, die 130 Jahre alt wurde.

Unter **Optionen** können Sie die Schwellenwerte anpassen, die die Tests verwenden – maximales Alter, Mindest- und Höchstalter für die Ehe oder für Kinder, maximale Anzahl von Kindern usw. – sowie ob fehlende oder ungenaue Daten geschätzt werden sollen und ob ungültige Daten wie den 31. Februar gemeldet werden sollen. Die von Ihnen geänderten Optionen werden in Ihrem Browser für den nächsten Durchlauf gespeichert; **Zurücksetzen** stellt die Standardwerte wieder her.

Klicken Sie auf **Daten verifizieren**, um zu beginnen. Die Überprüfung läuft als Hintergrundaufgabe, und die Ergebnisse werden dann unter **Ergebnisse der Datenverifizierung** aufgelistet. Dieses Werkzeug ändert nichts: Es berichtet nur, was es findet.

!!! Hinweis
    Ein Befund ist kein Beweis für einen Fehler. Lange Leben und große Altersunterschiede kommen vor, behandeln Sie die Ergebnisse daher als eine Liste von Dingen, die überprüft werden sollten, und nicht als eine Liste von Dingen, die behoben werden müssen.
