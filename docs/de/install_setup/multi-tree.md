# Einrichtung zum Hosten mehrerer Stammbäume


Standardmäßig erlaubt Gramps Web nur den Zugriff auf eine einzelne Stammbaumdatenbank (&ldquo;Stammbaum&rdquo;), die in der Konfigurationsdatei angegeben wird.

Ab Version 0.7.0 des Gramps-Web-API-Backends ist es jedoch auch möglich, mehrere Stammbäume über eine einzige Installation bereitzustellen. Jeder Benutzer ist (derzeit) an einen einzelnen Stammbaum gebunden. Diese Einrichtung eignet sich daher nicht zum gemeinsamen Nutzen von Stammbäumen durch mehrere Benutzer, sondern zum Hosten mehrerer isolierter Gramps-Web-Instanzen.

## Unterstützung für mehrere Stammbäume aktivieren

Um die Unterstützung für mehrere Stammbäume zu aktivieren, muss die Konfigurationsoption `TREE` auf ein einzelnes Sternchen `*` gesetzt werden, z. B. in einer Konfigurationsdatei:

```python
TREE = "*"
```

Dadurch werden alle Stammbäume im Gramps-Datenbankverzeichnis des Servers zugänglich (sofern ausreichende Benutzerberechtigungen vorhanden sind). Die ID des Stammbaums ist der Name des Unterverzeichnisses. Mit dem folgenden Befehl kannst du vorhandene Stammbäume (Namen und IDs) auflisten:

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Zusätzlich solltest du die Konfigurationsoption `MEDIA_PREFIX_TREE` auf `True` setzen, damit Mediendateien in separaten Unterordnern gespeichert werden. Andernfalls können Benutzer auf Mediendateien zugreifen, die zu einem Stammbaum gehören, für den sie keine Berechtigung haben!

## Ein Benutzerkonto einem bestimmten Stammbaum hinzufügen

Um einen Benutzer einem bestimmten Stammbaum hinzuzufügen, füge dem Befehl zum Hinzufügen eines Benutzers einfach die Befehlszeilenoption `--tree TREEID` hinzu. Du kannst auch einen POST an den Endpunkt `/users/` senden und dabei die Eigenschaft `tree` in der JSON-Nutzlast setzen.

Benutzernamen müssen über *alle* Stammbäume hinweg eindeutig sein. E-Mail-Adressen müssen nicht eindeutig sein (seit Gramps Web API 3.22), sodass dieselbe Person beispielsweise mit einer einzigen E-Mail-Adresse Konten in mehreren Stammbäumen haben kann.

## Einen neuen Stammbaum erstellen

Um einen neuen Stammbaum zu erstellen, wird empfohlen, einen POST an den Endpunkt `/trees/` zu senden, statt die Gramps-CLI zu verwenden. Dadurch wird eine UUIDv4 als Stammbaum-ID verwendet, was zusätzliche Sicherheit bietet, da der Name nicht erraten werden kann. Neu erstellte Stammbäume verwenden das in der Konfigurationsoption `NEW_DB_BACKEND` festgelegte Datenbank-Backend: SQLite (Standard) oder SharedPostgreSQL. Einzelheiten findest du unter [Eine PostgreSQL-Datenbank verwenden](postgres.md).


## Autorisieren

Zum Autorisieren (Abrufen eines Tokens) sind wie im Einzelstammbaum-Modus nur Benutzername und Passwort erforderlich, da die Stammbaum-ID für jeden Benutzer bekannt ist und daher nicht angegeben werden muss.


## Vorhandene Mediendateien migrieren

Wenn du eine vorhandene Gramps-Web-Instanz auf die Unterstützung mehrerer Stammbäume umstellen möchtest und lokale Mediendateien verwendest, kannst du sie einfach in einen Unterordner des ursprünglichen Speicherorts verschieben, der die Stammbaum-ID als Namen trägt.

Wenn du Mediendateien verwendest, die auf S3 gehostet werden, kannst du das Skript verwenden, das im Verzeichnis `scripts` des Repositorys `gramps-web-api` bereitgestellt wird:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Dies setzt voraus, dass die entsprechenden Zugriffsschlüssel bereits als Umgebungsvariablen festgelegt sind.


## Vorhandene Benutzerdatenbank migrieren

Wenn du die Unterstützung für mehrere Stammbäume aktivieren und vorhandene Benutzer wiederverwenden möchtest, musst du sie einem bestimmten Stammbaum zuweisen. Zu diesem Zweck kannst du den folgenden Befehl verwenden:

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```


## Frontend anpassen

Die über die Anmeldeseite zugängliche Registrierungsseite funktioniert in einer Einrichtung mit mehreren Stammbäumen nicht, da für die Registrierung ein Stammbaum angegeben werden muss. Daher empfiehlt es sich, `hideRegisterLink` in der [Frontend-Konfiguration](frontend-config.md) auf `true` zu setzen.
