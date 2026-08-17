Um Gramps Web auf Ihrem lokalen Computer (Linux, Mac oder Windows) auszuprobieren, ohne Ihre Gramps Desktop-Installation zu beeinträchtigen, können Sie Docker mit dem folgenden Befehl verwenden:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Dies macht eine neue, leere Gramps Web-Instanz unter [http://localhost:5055](http://localhost:5055) zugänglich, wo Sie einen Admin-Benutzer erstellen und eine Gramps XML-Datei importieren können.

!!! info
    Da dieses einfache Setup nicht erlaubt, lange Aufgaben in einem separaten Prozess auszuführen, könnte der Import einer großen Gramps XML-Datei aufgrund eines Timeouts im Erstlaufassistenten fehlschlagen.

Um Mediendateien von Ihrem Computer zu verwenden, können Sie den Gramps-Medienordner in den Container einbinden mit

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Bitte beachten Sie, dass dies die Änderungen, die Sie an der Datenbank vornehmen, nicht speichert, wenn Sie den Container neu starten. Um Gramps Web richtig einzurichten, lesen Sie weiter über [Bereitstellung](deployment.md).
