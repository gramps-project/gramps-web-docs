Um Gramps Web auf deinem lokalen Computer (Linux, Mac oder Windows) auszuprobieren, ohne deine Gramps-Desktop-Installation zu beeinträchtigen, kannst du Docker mit dem folgenden Befehl verwenden:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Dadurch wird eine neue, leere Gramps-Web-Instanz unter [http://localhost:5055](http://localhost:5055) verfügbar, wo du einen Admin-Benutzer erstellen und eine Gramps-XML-Datei importieren kannst.

!!! info
    Da diese einfache Einrichtung das Ausführen langer Aufgaben in einem separaten Prozess nicht ermöglicht, kann der Import einer großen Gramps-XML-Datei aufgrund einer Zeitüberschreitung im Assistenten für die Ersteinrichtung fehlschlagen.


Um Mediendateien von deinem Computer zu verwenden, kannst du den Gramps-Medienordner mit folgendem Befehl in den Container einbinden:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Beachte, dass die von dir an der Datenbank vorgenommenen Änderungen beim Neustart des Containers nicht dauerhaft gespeichert werden. Um Gramps Web ordnungsgemäß einzurichten, lies weiter unter [Bereitstellung](deployment.md).
