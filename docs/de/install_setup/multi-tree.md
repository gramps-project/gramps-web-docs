# Einrichtung für das Hosting mehrerer Bäume

Standardmäßig erlaubt Gramps Web den Zugriff auf eine einzelne Familienstammbaum-Datenbank („Baum“), die in der Konfigurationsdatei angegeben ist.

Mit der Version 0.7.0 des Gramps Web API-Backends ist es jedoch auch möglich, mehrere Bäume aus einer einzigen Installation bereitzustellen. Jeder Benutzer ist jedoch (derzeit) an einen einzelnen Baum gebunden, sodass dieses Setup nicht für das Teilen von Bäumen zwischen Benutzern geeignet ist, sondern für das Hosting mehrerer isolierter Gramps Web-Instanzen.

## Aktivieren der Unterstützung für mehrere Bäume

Um die Unterstützung für mehrere Bäume zu aktivieren, muss die `TREE`-Konfigurationsoption auf einen einzelnen Stern `*` gesetzt werden, z. B. in einer Konfigurationsdatei:

```python
TREE = "*"
```

Dies macht alle Bäume im Gramps-Datenbankverzeichnis des Servers zugänglich (vorausgesetzt, die Benutzer haben ausreichende Berechtigungen). Die ID des Baums ist der Name des Unterverzeichnisses. Sie können vorhandene Bäume (Namen und IDs) mit dem Befehl auflisten

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Darüber hinaus sollten Sie die Konfigurationsoption `MEDIA_PREFIX_TREE` auf `True` setzen, um sicherzustellen, dass Mediendateien in separaten Unterordnern gespeichert werden. Andernfalls können Benutzer auf Mediendateien zugreifen, die zu einem Baum gehören, für den sie keine Berechtigung haben!

## Benutzerkonto zu einem bestimmten Baum hinzufügen

Um einen Benutzer zu einem bestimmten Baum hinzuzufügen, fügen Sie einfach die `--tree TREEID`-Befehlszeilenoption zum Befehl zum Hinzufügen von Benutzern hinzu. Sie können auch eine POST-Anfrage an den `/users/`-Endpunkt mit der `tree`-Eigenschaft im JSON-Payload senden.

Benutzernamen und E-Mail-Adressen müssen in *allen* Bäumen eindeutig sein.

## Neuen Baum erstellen

Um einen neuen Baum zu erstellen, wird empfohlen, eine POST-Anfrage an den `/trees/`-Endpunkt zu senden, anstatt die Gramps-CLI zu verwenden. Dies verwendet eine UUIDv4 als Baum-ID, was zusätzliche Sicherheit bietet, da der Name nicht erraten werden kann. Derzeit wird nur SQLite für neu erstellte Bäume unterstützt.

## Autorisieren

Um sich zu autorisieren (einen Token abzurufen), sind nur Benutzername und Passwort erforderlich, wie im Einzelbaum-Modus, da die Baum-ID für jeden Benutzer bekannt ist und daher nicht angegeben werden muss.

## Vorhandene Mediendateien migrieren

Wenn Sie eine vorhandene Gramps Web-Instanz auf die Unterstützung mehrerer Bäume migrieren möchten und lokale Mediendateien verwenden, können Sie diese einfach in einen Unterordner des ursprünglichen Standorts mit der Baum-ID als Namen verschieben.

Wenn Sie Mediendateien verwenden, die auf S3 gehostet werden, können Sie das im Verzeichnis `scripts` des `gramps-web-api`-Repositories bereitgestellte Skript verwenden:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Dies setzt voraus, dass die relevanten Zugriffsschlüssel bereits als Umgebungsvariablen festgelegt sind.

## Vorhandene Benutzerdatenbank migrieren

Wenn Sie die Unterstützung für mehrere Bäume aktivieren und vorhandene Benutzer wiederverwenden möchten, müssen Sie sie einem bestimmten Baum zuweisen. Sie können den folgenden Befehl verwenden, der zu diesem Zweck bereitgestellt wird,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Frontend anpassen

Die Registrierungsseite, die von der Anmeldeseite aus zugänglich ist, funktioniert in einem Setup mit mehreren Bäumen nicht, da ein Baum für die Registrierung angegeben werden muss. Es ist daher ratsam, `hideRegisterLink` auf `true` in der [Frontend-Konfiguration](frontend-config.md) zu setzen.
