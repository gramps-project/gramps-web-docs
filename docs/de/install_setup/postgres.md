# Verwendung einer PostgreSQL-Datenbank

Standardmäßig verwendet Gramps eine dateibasierte SQLite-Datenbank zur Speicherung des Stammbaums. Dies funktioniert für Gramps Web einwandfrei und wird für die meisten Benutzer empfohlen. Ab Gramps Web API Version 0.3.0 wird jedoch auch ein PostgreSQL-Server mit einem einzelnen Stammbaum pro Datenbank unterstützt, ermöglicht durch das [Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Seit [Version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) wird auch das SharedPostgreSQL Addon unterstützt, das das Hosting mehrerer Stammbäume in einer einzigen Datenbank ermöglicht, was besonders nützlich ist, wenn es zusammen mit der [Multi-Tree-Unterstützung](multi-tree.md) von Gramps Web API verwendet wird.

!!! warning "PostgreSQL-Backend veraltet"
    Die Unterstützung für das PostgreSQL-Backend (ein Stammbaum pro Datenbank) wird in einer zukünftigen Version von Gramps Web API entfernt, da es nicht mit dem Hosting mehrerer Bäume kompatibel ist. Die Backends SharedPostgreSQL und SQLite bleiben vollständig unterstützt. Für neue Installationen verwenden Sie SharedPostgreSQL.

## Einrichten des PostgreSQL-Servers

Wenn Sie eine neue Datenbank für die Verwendung mit dem PostgreSQLAddon einrichten möchten, können Sie die [Anweisungen im Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) befolgen, um den Server einzurichten.

Alternativ können Sie auch Docker Compose verwenden, um den PostgreSQL-Server in einem Container auf demselben Docker-Host wie Gramps Web auszuführen.

Die Verwendung eines dockerisierten PostgreSQL mit Gramps wird nur dadurch kompliziert, dass die Standard-PostgreSQL-Images keine Locales installiert haben, die jedoch von Gramps für die lokalisierte Sortierung von Objekten benötigt werden. Die einfachste Option ist die Verwendung des `gramps-postgres`-Images, das in [diesem Repository](https://github.com/DavidMStraub/gramps-postgres-docker/) veröffentlicht wurde. Um es zu verwenden, fügen Sie den folgenden Abschnitt zu Ihrer `docker-compose.yml` hinzu:
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
und fügen Sie auch `postgres_data:` als Schlüssel unter dem Abschnitt `volumes:` dieser YAML-Datei hinzu. Dieses Image enthält eine separate Datenbank für Gramps genealogische Daten und für die Gramps-Benutzerdatenbank; jede kann separate Passwörter haben.

## Importieren eines Gramps-Stammbaums

Wenn Sie den PostgreSQL-Server selbst eingerichtet haben, können Sie die [Anweisungen im Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) befolgen, um einen Stammbaum in die Datenbank zu importieren.

Alternativ, wenn Sie die oben genannten Docker Compose-Anweisungen befolgt haben, können Sie den folgenden Befehl verwenden, um eine Gramps XML-Datei zu importieren, die sich auf Ihrem Docker-Host befindet:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Konfigurieren der Web-API zur Verwendung mit der Datenbank

Um die Web-API für die Verwendung mit der PostgreSQL-Datenbank zu konfigurieren, fügen Sie Folgendes unter dem Schlüssel `environment:` des `grampsweb`-Dienstes in `docker-compose.yml` hinzu:

```yaml
      # Das PostgreSQL-Addon geht davon aus, dass der Baumname
      # dem Datenbanknamen entspricht, und hier wird der Standard-
      # Datenbankname des PostgreSQL-Images verwendet
      GRAMPSWEB_TREE: postgres
      # Die Anmeldedaten müssen mit denen übereinstimmen, die für
      # den PostgreSQL-Container verwendet werden
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## Verwendung einer gemeinsamen PostgreSQL-Datenbank in einer Multi-Tree-Installation

Bei der Verwendung eines [Multi-Tree-Setups](multi-tree.md) ist das SharedPostgreSQL-Addon eine praktische Option, um alle Bäume, auch neu erstellte über die API, in einer einzigen PostgreSQL-Datenbank zu hosten, ohne die Privatsphäre oder Sicherheit zu gefährden.

Um dies zu erreichen, richten Sie einen Container basierend auf dem `gramps-postgres`-Image wie oben beschrieben ein und setzen Sie einfach die Konfigurationsoption `NEW_DB_BACKEND` auf `sharedpostgresql`, z.B. über die Umgebungsvariable `GRAMPSWEB_NEW_DB_BACKEND`.

## Verwendung einer PostgreSQL-Datenbank für die Benutzerdatenbank

Unabhängig davon, welches Datenbank-Backend für die genealogischen Daten verwendet wird, kann die Benutzerdatenbank in einer PostgreSQL-Datenbank gehostet werden, indem eine entsprechende Datenbank-URL bereitgestellt wird. Das oben erwähnte `gramps-postgres`-Docker-Image enthält eine separate Datenbank `grampswebuser`, die für diesen Zweck verwendet werden kann. In diesem Fall wäre der entsprechende Wert für die Konfigurationsoption `USER_DB_URI`
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Verwendung einer PostgreSQL-Datenbank für den Suchindex

Seit Gramps Web API Version 2.4.0 wird der Suchindex entweder in einer SQLite-Datenbank (Standard) oder in einer PostgreSQL-Datenbank gehostet. Auch für diesen Zweck kann das `gramps-postgres`-Image verwendet werden. Für den Suchindex können wir die von dem Image bereitgestellte `gramps`-Datenbank verwenden, unabhängig davon, ob wir unsere genealogischen Daten in PostgreSQL hosten oder nicht (der Suchindex und die genealogischen Daten können in derselben Datenbank coexistieren). Dies kann im obigen Beispiel erreicht werden, indem die Konfigurationsoption `SEARCH_INDEX_DB_URI` auf
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```
gesetzt wird.

## Probleme

Bei Problemen überwachen Sie bitte die Protokollausgaben von Gramps Web und dem PostgreSQL-Server. Im Falle von Docker erreichen Sie dies mit

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Wenn Sie vermuten, dass es ein Problem mit Gramps Web (oder der Dokumentation) gibt, reichen Sie bitte ein Problem [auf Github](https://github.com/gramps-project/gramps-web-api/issues) ein.
