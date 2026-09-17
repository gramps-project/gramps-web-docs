# Verwendung einer PostgreSQL-Datenbank

Standardmäßig speichert Gramps Web jeden Familienstammbaum in seiner eigenen SQLite-Datenbankdatei. Dies erfordert keinen zusätzlichen Dienst, Backups sind so einfach wie das Kopieren von Dateien, und es funktioniert gut für die meisten Installationen, einschließlich solcher, die [mehrere Bäume hosten](multi-tree.md).

Alternativ können Familienstammbäume auf einem PostgreSQL-Server mit dem SharedPostgreSQL-Addon gehostet werden, das alle Bäume in einer einzigen Datenbank speichert. Dies kann sinnvoll sein, wenn Sie bereits einen PostgreSQL-Server betreiben und Backups und Überwachung dort verwalten möchten, oder wenn Sie erwarten, dass viele Benutzer gleichzeitig bearbeiten. PostgreSQL kann auch die [Benutzerdatenbank](#using-a-postgresql-database-for-the-user-database) und den [Suchindex](#using-a-postgresql-database-for-the-search-index) hosten, unabhängig davon, wo die Familienstammbäume gespeichert sind.

!!! warning "PostgreSQL-Addon veraltet"
    Das ältere PostgreSQL-Addon, das einen einzelnen Familienstammbaum pro Datenbank speichert, ist veraltet und wird in einer zukünftigen Version der Gramps Web API nicht mehr unterstützt. Wenn Sie es verwenden, siehe [Verschieben eines Baums vom PostgreSQL-Addon zu SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Einrichtung des PostgreSQL-Servers

Die einfachste Option ist, den PostgreSQL-Server in einem Container auf demselben Docker-Host wie Gramps Web mit Docker Compose auszuführen.

Gramps benötigt installierte Locale auf dem PostgreSQL-Server, um Objekte in verschiedenen Sprachen korrekt zu sortieren, und die Standard-PostgreSQL-Images enthalten keine. Das [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) Image fügt diese hinzu. Um es zu verwenden, fügen Sie den folgenden Abschnitt zu Ihrer `docker-compose.yml` hinzu:
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
Fügen Sie auch `postgres_data:` als Schlüssel unter dem Abschnitt `volumes:` dieser YAML-Datei hinzu. Das Image enthält zwei Datenbanken, jede mit ihrem eigenen Benutzer und Passwort: `gramps` für die genealogischen Daten und `grampswebuser` für die Gramps Web-Benutzerdatenbank.

Wenn Sie stattdessen Ihren eigenen PostgreSQL-Server verwenden, erstellen Sie eine Datenbank mit dem Namen `gramps`, in der der konfigurierte Benutzer Tabellen erstellen kann, und stellen Sie sicher, dass die benötigten Locales Ihrer Benutzer installiert sind.

## Konfiguration von Gramps Web

Neue Familienstammbäume werden in der SharedPostgreSQL-Datenbank erstellt, wenn Gramps Web im [Multi-Tree-Modus](multi-tree.md) läuft und die Konfigurationsoption `NEW_DB_BACKEND` auf `sharedpostgresql` gesetzt ist. Mit der oben beschriebenen Docker-Compose-Einrichtung fügen Sie Folgendes unter dem Schlüssel `environment:` des `grampsweb`-Dienstes in `docker-compose.yml` hinzu:

```yaml
      # Multi-Tree-Modus aktivieren
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # Neue Bäume in der SharedPostgreSQL-Datenbank erstellen
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # Der Host und Port des PostgreSQL-Servers. Der
      # Host ist der Name des oben genannten PostgreSQL-Dienstes
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Die Anmeldeinformationen müssen mit denen übereinstimmen,
      # die für den PostgreSQL-Container verwendet werden
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Siehe [Konfiguration](configuration.md) für eine Beschreibung all dieser Optionen. Beachten Sie, dass Host und Port mit jedem Baum gespeichert werden, wenn er erstellt wird, sodass Änderungen später nur neue Bäume betreffen.

## Erstellen eines Baums und Importieren von Daten

Um einen neuen Baum zu erstellen, POSTen Sie an den Endpunkt `/trees/`, wie in [Einrichtung zum Hosten mehrerer Bäume](multi-tree.md#create-a-new-tree) beschrieben. Die Antwort enthält die ID des neuen Baums, die Sie benötigen, um [das Konto des Baum-Eigentümers zu erstellen](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Sobald der Baum-Eigentümer sich angemeldet hat, kann er einen bestehenden Familienstammbaum [importieren](../administration/import.md), z.B. eine Gramps XML-Datei, die aus Gramps Desktop exportiert wurde, über die Weboberfläche.

## Verwendung einer PostgreSQL-Datenbank für die Benutzerdatenbank

Die Benutzerdatenbank ist normalerweise eine SQLite-Datei, unabhängig davon, wo die Familienstammbäume gehostet werden. Um stattdessen PostgreSQL zu verwenden, setzen Sie die Konfigurationsoption `USER_DB_URI` auf eine PostgreSQL-Datenbank-URL. Mit dem oben genannten `gramps-postgres`-Image verwenden Sie dessen `grampswebuser`-Datenbank:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Verwendung einer PostgreSQL-Datenbank für den Suchindex

Der Suchindex wird standardmäßig ebenfalls in SQLite gespeichert. Um stattdessen PostgreSQL zu verwenden, setzen Sie die Konfigurationsoption `SEARCH_INDEX_DB_URI` auf eine PostgreSQL-Datenbank-URL. Mit dem oben genannten `gramps-postgres`-Image können Sie dessen `gramps`-Datenbank verwenden, unabhängig davon, ob Ihre Familienstammbäume dort ebenfalls gehostet werden:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Verschieben eines Baums vom PostgreSQL-Addon zu SharedPostgreSQL

Ältere Installationen können ihren Familienstammbaum mit dem PostgreSQL-Addon hosten, das einen einzelnen Baum pro Datenbank speichert und veraltet ist. Um herauszufinden, welches Addon ein Baum verwendet, schauen Sie sich die Datei `database.txt` im Unterverzeichnis des Baums im Gramps-Datenverzeichnis an: Sie enthält `postgresql` für das veraltete PostgreSQL-Addon und `sharedpostgresql` für SharedPostgreSQL.

Um einen Baum vom PostgreSQL-Addon zu SharedPostgreSQL innerhalb derselben Installation zu verschieben, während Sie Ihre Benutzerkonten und Mediendateien beibehalten:

1. [Sichern Sie Ihren Familienstammbaum](../administration/export.md#back-up-your-family-tree) als Gramps XML (`.gramps`) Datei, unter Verwendung eines Kontos, das private Datensätze anzeigen kann.
2. Ändern Sie Ihre Konfiguration wie in [Konfiguration von Gramps Web](#configuring-gramps-web) beschrieben. Sie können Ihren vorhandenen `gramps-postgres`-Container weiterhin verwenden.
3. [Erstellen Sie einen neuen Baum](multi-tree.md#create-a-new-tree) und notieren Sie sich die Baum-ID.
4. Weisen Sie Ihre vorhandenen Benutzerkonten dem neuen Baum zu, wie in [Migration vorhandener Benutzerdatenbank](multi-tree.md#migrate-existing-user-database) beschrieben.
5. Verschieben Sie Ihre Mediendateien an den für den neuen Baum erwarteten Speicherort, wie in [Migration vorhandener Mediendateien](multi-tree.md#migrate-existing-media-files) beschrieben.
6. Melden Sie sich an und [importieren](../administration/import.md) Sie die Gramps XML-Datei in den neuen Baum.

Bewahren Sie die Gramps XML-Datei auf, bis Sie überprüft haben, dass der neue Baum vollständig ist.

Wenn Sie zu einer separaten Gramps Web-Installation wechseln, folgen Sie den Schritten in [Wechsel zu einer anderen Gramps Web-Instanz](../administration/export.md#move-to-a-different-gramps-web-instance).

## Probleme

Im Falle von Problemen überwachen Sie bitte die Protokollausgaben von Gramps Web und dem PostgreSQL-Server. Im Falle von Docker erreichen Sie dies mit

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Wenn Sie vermuten, dass es ein Problem mit Gramps Web (oder der Dokumentation) gibt, reichen Sie bitte ein Problem [auf Github](https://github.com/gramps-project/gramps-web-api/issues) ein.
