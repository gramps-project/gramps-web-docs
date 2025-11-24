Um Gramps Web auf Ihrem lokalen Computer (Linux, Mac oder Windows) auszuprobieren, ohne mit Ihrer Gramps Desktop-Installation zu stören, können Sie Docker mit dem folgenden Befehl verwenden:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Damit wird eine neue, leere Gramps Web-Instanz auf [http://localhost:5055](http://localhost:5055) zugänglich gemacht, in der Sie einen Administrator-Benutzer erstellen und eine Gramps XML-Datei importieren können.

!!! info
Da dieses einfache Setup keine langen Aufgaben in einem separaten Prozess ausführen lässt, kann die Importierung einer großen Gramps XML-Datei aufgrund eines Timeouts im ersten Assistenten scheitern.


Um Mediendateien von Ihrem Computer zu verwenden, können Sie den Gramps-Medienordner in den Container mit einfügen

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Beachten Sie, dass dies nicht die Änderungen, die Sie in der Datenbank, wenn Sie den Container neu starten. Um Gramps Web richtig einzurichten, lesen Sie weiter über [Deployment](deployment.md).