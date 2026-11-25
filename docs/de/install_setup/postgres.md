# Verwenden einer PostgreSQL-Datenbank

Standardmäßig speichert Gramps Web jeden Familienstammbaum in einer eigenen SQLite-Datenbankdatei. Dafür ist kein zusätzlicher Dienst erforderlich, Backups sind so einfach wie das Kopieren von Dateien, und diese Lösung funktioniert für die meisten Installationen gut, auch für solche, die [mehrere Stammbäume hosten](multi-tree.md).

Alternativ können Familienstammbäume auf einem PostgreSQL-Server gehostet werden. Dazu wird das SharedPostgreSQL-Add-on verwendet, das alle Stammbäume in einer einzigen Datenbank speichert. Dies kann sinnvoll sein, wenn du bereits einen PostgreSQL-Server betreibst und Backups sowie Überwachung dort verwalten möchtest oder wenn du damit rechnest, dass viele Benutzer gleichzeitig Änderungen vornehmen. PostgreSQL kann außerdem unabhängig davon, wo die Familienstammbäume gespeichert sind, die [Benutzerdatenbank](#verwenden-einer-postgresql-datenbank-für-die-benutzerdatenbank) und den [Suchindex](#verwenden-einer-postgresql-datenbank-für-den-suchindex) hosten.

!!! warning "PostgreSQL-Add-on veraltet"
    Das ältere PostgreSQL-Add-on, das einen einzelnen Familienstammbaum pro Datenbank speichert, ist seit Gramps Web API 3.24 veraltet und wird in Gramps Web API 4.0 nicht mehr unterstützt, da es nicht mit dem Hosting mehrerer Stammbäume kompatibel ist, das in dieser Version zum Standard wird. Wenn du es verwendest, siehe [Verschieben eines Stammbaums vom PostgreSQL-Add-on zu SharedPostgreSQL](#verschieben-eines-stammbaums-vom-postgresql-add-on-zu-sharedpostgresql).

## Einrichten des PostgreSQL-Servers

Die einfachste Möglichkeit besteht darin, den PostgreSQL-Server mithilfe von Docker Compose in einem Container auf demselben Docker-Host wie Gramps Web auszuführen.

Gramps benötigt auf dem PostgreSQL-Server installierte Locales, um Objekte in verschiedenen Sprachen korrekt zu sortieren. Die standardmäßigen PostgreSQL-Images enthalten jedoch keine. Das Image [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) fügt diese hinzu. Um es zu verwenden, füge den folgenden Abschnitt zu deiner `docker-compose.yml` hinzu:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
Füge außerdem `postgres_data:` als Schlüssel unter dem Abschnitt `volumes:` dieser YAML-Datei hinzu. Das Image enthält zwei Datenbanken, jeweils mit eigenem Benutzer und Passwort: `gramps` für die genealogischen Daten und `grampswebuser` für die Gramps-Web-Benutzerdatenbank.

Wenn du stattdessen deinen eigenen PostgreSQL-Server verwendest, erstelle eine Datenbank namens `gramps`, in der der konfigurierte Benutzer Tabellen erstellen kann, und stelle sicher, dass die von deinen Benutzern benötigten Locales installiert sind.

## Konfigurieren von Gramps Web

Neue Familienstammbäume werden in der SharedPostgreSQL-Datenbank erstellt, wenn Gramps Web im [Modus für mehrere Stammbäume](multi-tree.md) ausgeführt wird und die Konfigurationsoption `NEW_DB_BACKEND` auf `sharedpostgresql` gesetzt ist. Füge bei der oben beschriebenen Docker-Compose-Einrichtung Folgendes unter dem Schlüssel `environment:` des Dienstes `grampsweb` in `docker-compose.yml` hinzu:

```yaml
      # enable multi-tree mode
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # create new trees in the SharedPostgreSQL database
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # The host and port of the PostgreSQL server. The
      # host is the name of the PostgreSQL service above
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # The credentials must agree with the ones used for
      # the PostgreSQL container
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Eine Beschreibung all dieser Optionen findest du unter [Konfiguration](configuration.md). Beachte, dass Host und Port beim Erstellen mit jedem Stammbaum gespeichert werden. Eine spätere Änderung wirkt sich daher nur auf neue Stammbäume aus.

## Erstellen eines Stammbaums und Importieren von Daten

Um einen neuen Stammbaum zu erstellen, sende wie unter [Einrichtung für das Hosting mehrerer Stammbäume](multi-tree.md#create-a-new-tree) beschrieben eine POST-Anfrage an den Endpunkt `/trees/`. Die Antwort enthält die ID des neuen Stammbaums. Diese benötigst du, um [das Konto des Stammbaumbesitzers zu erstellen](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Sobald sich der Stammbaumbesitzer angemeldet hat, kann er über die Weboberfläche einen vorhandenen Familienstammbaum [importieren](../administration/import.md), beispielsweise eine aus Gramps Desktop exportierte Gramps-XML-Datei.

## Verwenden einer PostgreSQL-Datenbank für die Benutzerdatenbank

Die Benutzerdatenbank ist normalerweise eine SQLite-Datei, unabhängig davon, wo die Familienstammbäume gehostet werden. Um stattdessen PostgreSQL zu verwenden, setze die Konfigurationsoption `USER_DB_URI` auf eine PostgreSQL-Datenbank-URL. Mit dem oben beschriebenen Image `gramps-postgres` verwendest du dessen Datenbank `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Verwenden einer PostgreSQL-Datenbank für den Suchindex

Auch der Suchindex wird standardmäßig in SQLite gespeichert. Um stattdessen PostgreSQL zu verwenden, setze die Konfigurationsoption `SEARCH_INDEX_DB_URI` auf eine PostgreSQL-Datenbank-URL. Mit dem oben beschriebenen Image `gramps-postgres` kannst du dessen Datenbank `gramps` verwenden, unabhängig davon, ob deine Familienstammbäume ebenfalls dort gehostet werden:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

Der Suchindex benötigt PostgreSQL 12 oder neuer.

## Verschieben eines Stammbaums vom PostgreSQL-Add-on zu SharedPostgreSQL

Ältere Installationen hosten möglicherweise ihren Familienstammbaum mit dem PostgreSQL-Add-on, das einen einzelnen Stammbaum pro Datenbank speichert und veraltet ist. Um herauszufinden, welches Add-on ein Stammbaum verwendet, sieh dir die Datei `database.txt` im Unterverzeichnis des Stammbaums im Gramps-Datenbankverzeichnis an: Sie enthält `postgresql` für das veraltete PostgreSQL-Add-on und `sharedpostgresql` für SharedPostgreSQL.

Um einen Stammbaum innerhalb derselben Installation vom PostgreSQL-Add-on zu SharedPostgreSQL zu verschieben und dabei deine Benutzerkonten sowie Mediendateien beizubehalten:

1. [Exportiere deinen Familienstammbaum](../administration/export.md#export-the-family-tree-as-gramps-xml) als Gramps-XML-Datei (`.gramps`) mit einem Konto, das private Datensätze anzeigen kann.
2. Ändere deine Konfiguration wie unter [Konfigurieren von Gramps Web](#konfigurieren-von-gramps-web) beschrieben. Du kannst deinen vorhandenen `gramps-postgres`-Container weiterverwenden.
3. [Erstelle einen neuen Stammbaum](multi-tree.md#create-a-new-tree) und notiere dir dessen Stammbaum-ID.
4. Weise deine vorhandenen Benutzerkonten dem neuen Stammbaum zu, wie unter [Vorhandene Benutzerdatenbank migrieren](multi-tree.md#migrate-existing-user-database) beschrieben.
5. Verschiebe deine Mediendateien an den für den neuen Stammbaum erwarteten Speicherort, wie unter [Vorhandene Mediendateien migrieren](multi-tree.md#migrate-existing-media-files) beschrieben.
6. Melde dich an und [importiere](../administration/import.md) die Gramps-XML-Datei in den neuen Stammbaum.

Bewahre die Gramps-XML-Datei auf, bis du überprüft hast, dass der neue Stammbaum vollständig ist.

Wenn du stattdessen zu einer separaten Gramps-Web-Installation wechselst, befolge die Schritte unter [Zu einer anderen Gramps-Web-Instanz wechseln](../administration/export.md#move-to-a-different-gramps-web-instance).

## Probleme

Bei Problemen überwache bitte die Protokollausgabe von Gramps Web und dem PostgreSQL-Server. Bei Docker erreichst du dies mit

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Wenn du vermutest, dass ein Problem mit Gramps Web (oder der Dokumentation) vorliegt, melde bitte ein Problem [auf Github](https://github.com/gramps-project/gramps-web-api/issues).
