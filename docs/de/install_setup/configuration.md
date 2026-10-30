# Serverkonfiguration

Mit dem Standard-Docker-Image kann die gesamte erforderliche Konfiguration über den Browser vorgenommen werden. Je nach Bereitstellung kann es jedoch notwendig sein, die Serverkonfiguration anzupassen.

Diese Seite listet alle Methoden zur Änderung der Konfiguration und alle vorhandenen Konfigurationsoptionen auf.


## Konfigurationsdatei vs. Umgebungsvariablen

Für die Einstellungen können Sie entweder eine Konfigurationsdatei oder Umgebungsvariablen verwenden.

Wenn Sie das [Docker Compose-basierte Setup](deployment.md) verwenden, können Sie eine Konfigurationsdatei einfügen, indem Sie den folgenden Listeneintrag unter dem Schlüssel `volumes:` im Block `grampsweb:` hinzufügen:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
wobei `/path/to/config.cfg` der Pfad zur Konfigurationsdatei im Dateisystem Ihres Servers ist (die rechte Seite bezieht sich auf den Pfad im Container und darf nicht geändert werden).

Bei der Verwendung von Umgebungsvariablen,

- prefixen Sie jeden Einstellungsnamen mit `GRAMPSWEB_`, um den Namen der Umgebungsvariablen zu erhalten
- Verwenden Sie doppelte Unterstriche für verschachtelte Dictionary-Einstellungen, z. B. wird `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` den Wert der Konfigurationsoption `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` setzen

Bitte beachten Sie, dass Konfigurationsoptionen, die über die Umgebung festgelegt werden, Vorrang vor denen in der Konfigurationsdatei haben. Wenn beide vorhanden sind, "gewinnt" die Umgebungsvariable.

!!! warning "Nicht präfixierte Umgebungsvariablen sind veraltet"
    Aus historischen Gründen können eine Handvoll Einstellungen – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` und `STATIC_PATH` – weiterhin über eine Umgebungsvariable *ohne* das Präfix `GRAMPSWEB_` festgelegt werden. Dies ist veraltet, protokolliert beim Start eine Warnung und wird in einer zukünftigen Version nicht mehr funktionieren. Verwenden Sie immer die präfixierte Form, z. B. `GRAMPSWEB_TREE` anstelle von `TREE`.

    Beachten Sie, dass dies nur Umgebungsvariablen betrifft. In einer Konfigurationsdatei werden die Einstellungsnamen immer unpräfixiert verwendet.

!!! tip "Überprüfen auf veraltete Optionen"
    Veraltete Konfigurationsoptionen, auf die Ihr Server weiterhin angewiesen ist – wie nicht präfixierte Umgebungsvariablen, `SEARCH_INDEX_DIR` oder `EMAIL_USE_TLS` – werden beim Start als Warnungen protokolliert. Seit Gramps Web API 3.22 werden sie auch zusammen mit ihrem Ersatz und der Version, in der die Unterstützung entfernt wird, oben auf der **Systeminformationen**-Seite (erreichbar über das Benutzersymbol in der oberen App-Leiste), angezeigt, wenn Sie als Administrator angemeldet sind.

    Die E-Mail-Einstellungen und die Basis-URL, die der Einrichtungsassistent älterer Versionen in der Datenbank gespeichert hat, werden dort ebenfalls aufgelistet. Setzen Sie sie in Ihrer Konfiguration auf die gespeicherten Werte; die Warnung verschwindet, sobald sie übereinstimmen.

## Vorhandene Konfigurationseinstellungen
Die folgenden Konfigurationsoptionen existieren.

### Erforderliche Einstellungen

Schlüssel | Beschreibung
----|-------------
`TREE` | Der Name der zu verwendenden Familienstammbaum-Datenbank. Zeigen Sie verfügbare Bäume mit `gramps -l` an. Wenn ein Baum mit diesem Namen nicht existiert, wird ein neuer leerer Baum erstellt.
`SECRET_KEY` | Der geheime Schlüssel für Flask. Der Schlüssel darf nicht öffentlich geteilt werden. Eine Änderung macht alle Zugriffstoken ungültig.
`USER_DB_URI` | Die Datenbank-URL der Benutzerdatenbank. Jede URL, die mit SQLAlchemy kompatibel ist, ist erlaubt.

!!! info
    Sie können einen sicheren geheimen Schlüssel z. B. mit dem Befehl generieren

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optionale Einstellungen

Schlüssel | Beschreibung
----|-------------
`MEDIA_BASE_DIR` | Pfad, der als Basisverzeichnis für Mediendateien verwendet wird und das in Gramps festgelegte Medienbasisverzeichnis überschreibt. Bei Verwendung von [S3](s3.md) muss es die Form `s3://<bucket_name>` haben.
`TREE_ID` | Der Verzeichnisname der Familienstammbaum-Datenbank, die im Einzelbaum-Modus verwendet werden soll (wenn `TREE` nicht auf `*` gesetzt ist). Wenn gesetzt, identifiziert der Server den Baum anhand seines Verzeichnisnamens anstelle seines Anzeigenamens, was robuster gegenüber Umbenennungen ist. Erforderlich, wenn Sie den Baum über die API umbenennen möchten. Der Verzeichnisname kann über `GET /api/trees/-` (das `id`-Feld) gefunden werden.
`SEARCH_INDEX_DB_URI` | Datenbank-URL für den Suchindex. Nur `sqlite` oder `postgresql` sind als Backends erlaubt. Standardmäßig auf `sqlite:///indexdir/search_index.db` gesetzt, wodurch eine SQLite-Datei im Ordner `indexdir` relativ zu dem Pfad erstellt wird, von dem das Skript ausgeführt wird.
`SEARCH_INDEX_DIR` | **Veraltet** (verwenden Sie stattdessen `SEARCH_INDEX_DB_URI`). Verzeichnis, das den Suchindex enthält. Wenn gesetzt, während `SEARCH_INDEX_DB_URI` nicht gesetzt ist, wird die Suchindex-URL als `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` abgeleitet.
`STATIC_PATH` | Pfad, von dem statische Dateien bereitgestellt werden (z. B. ein statisches Web-Frontend)
`BASE_URL` | Basis-URL, unter der die API erreichbar ist (z. B. `https://mygramps.mydomain.com/`). Dies ist notwendig, um z. B. korrekte Links zum Zurücksetzen des Passworts zu erstellen. Web Push erfordert ebenfalls eine öffentlich erreichbare HTTPS-URL; die Standard-URL `http://localhost/` deaktiviert Web Push. Wenn Sie diese Einstellung über die Umgebung konfigurieren, verwenden Sie `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Ursprünge, von denen CORS-Anfragen erlaubt sind. Standardmäßig sind alle nicht erlaubt. Verwenden Sie `"*"`, um Anfragen von jeder Domain zuzulassen.
`EMAIL_HOST` | SMTP-Server-Host (z. B. zum Senden von E-Mails zum Zurücksetzen des Passworts)
`EMAIL_PORT` | SMTP-Server-Port. Standardmäßig auf 465 gesetzt.
`EMAIL_HOST_USER` | SMTP-Server-Benutzername
`EMAIL_HOST_PASSWORD` | SMTP-Server-Passwort
`EMAIL_USE_TLS` | **Veraltet** (verwenden Sie stattdessen `EMAIL_USE_SSL` oder `EMAIL_USE_STARTTLS`). Boolean, ob TLS zum Senden von E-Mails verwendet werden soll. Standardmäßig auf `True` gesetzt. Bei Verwendung von STARTTLS setzen Sie dies auf `False` und verwenden einen anderen Port als 25.
`EMAIL_USE_SSL` | Boolean, ob implizites SSL/TLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig auf `True` gesetzt, wenn `EMAIL_USE_TLS` nicht explizit festgelegt ist. Typischerweise mit Port 465 verwendet.
`EMAIL_USE_STARTTLS` | Boolean, ob explizites STARTTLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig auf `False` gesetzt. Typischerweise mit Port 587 oder 25 verwendet.
`DEFAULT_FROM_EMAIL` | "Von"-Adresse für automatisierte E-Mails
`THUMBNAIL_CACHE_CONFIG` | Dictionary mit Einstellungen für den Thumbnail-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`REQUEST_CACHE_CONFIG` | Dictionary mit Einstellungen für den Anfrage-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`PERSISTENT_CACHE_CONFIG` | Dictionary mit Einstellungen für den persistenten Cache, der z. B. für Telemetrie verwendet wird. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`CELERY_CONFIG` | Einstellungen für die Celery-Hintergrundaufgabenwarteschlange. Siehe [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) für mögliche Einstellungen.
`REPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgaben von ausgeführten Gramps-Berichten gespeichert werden
`EXPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgaben des Exports der Gramps-Datenbank gespeichert werden
`BACKUP_DIR` | Verzeichnis, in dem [Backups](../administration/settings.md#backups) gespeichert werden, in einem Unterverzeichnis pro Baum (v3.24.0+). Wenn nicht gesetzt (Standard), können keine Backups auf dem Server gespeichert werden, aber sie können weiterhin aus einer hochgeladenen Datei wiederhergestellt werden. Verwenden Sie einen dauerhaften Speicherort, z. B. ein Docker-Volume, und vorzugsweise einen, der selbst gesichert oder an anderer Stelle synchronisiert wird.
`BACKUP_KEEP` | Anzahl der pro Baum aufbewahrten Backups; ältere werden gelöscht, wenn ein neues Backup erstellt wird (v3.24.0+). Standardmäßig auf `5` gesetzt.
`RATE_LIMIT_BACKUP` | Ratenlimit für die Erstellung von Backups, pro Baum (v3.24.0+). Standardmäßig auf `"10 pro Tag"` gesetzt.
`RATE_LIMIT_MEDIA_ARCHIVE` | Ratenlimit für die Erstellung von Medienarchiven auf der Exportseite. Standardmäßig auf `"1 pro Stunde"` gesetzt.
`REGISTRATION_DISABLED` | Wenn `True`, keine neue Benutzerregistrierung zulassen (Standard `False`).
`DISABLE_TELEMETRY` | Wenn `True`, Statistiktelemetrie deaktivieren (Standard `False`). Siehe [Telemetrie](telemetry.md) für Details.
`PILLOW_MAX_IMAGE_PIXELS` | Setzt den Parameter PIL.Image.MAX_IMAGE_PIXELS, der die Anzahl der Pixel angibt, die das verarbeitete Bild enthalten kann. Siehe [Dokumentation](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) für Details.
`MAX_THUMBNAIL_FILE_BYTES` | Setzt eine harte maximale Dateigröße für Thumbnails. Standardmäßig auf `50 * 1024 * 1024` (50 MB) gesetzt. Eine Erhöhung kann den Speicherverbrauch erheblich erhöhen und zu Speicherüberläufen oder Datenverlust führen, wenn große Dateien im Speicher dekomprimiert werden.


!!! info
    Bei der Verwendung von Umgebungsvariablen für die Konfiguration müssen boolesche Optionen wie `EMAIL_USE_SSL` entweder den String `true` oder `false` (groß- und kleinschreibungssensitiv!) haben.


### Einstellungen für PostgreSQL-Datenbanken

Diese Einstellungen sind erforderlich, wenn Ihre Familienstammbäume in einer [PostgreSQL-Datenbank](postgres.md) mit dem SharedPostgreSQL-Addon gehostet werden.

Schlüssel | Beschreibung
----|-------------
`POSTGRES_USER` | Der Benutzername für die Datenbankverbindung
`POSTGRES_PASSWORD` | Das Passwort für den Datenbankbenutzer


### Einstellungen, die für das Hosting mehrerer Bäume relevant sind

Die folgenden Einstellungen sind relevant, wenn [mehrere Bäume gehostet werden](multi-tree.md).


Schlüssel | Beschreibung
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, ob ein separates Unterverzeichnis für die Mediendateien jedes Baumes verwendet werden soll. Standardmäßig auf `False` gesetzt, wird jedoch dringend empfohlen, in einem Multi-Baum-Setup `True` zu verwenden.
`NEW_DB_BACKEND` | Das Datenbank-Backend, das für neu erstellte Familienstammbäume verwendet werden soll. Muss eines von `sqlite` oder `sharedpostgresql` sein. Standardmäßig auf `sqlite` gesetzt. Der Wert `postgresql` wird weiterhin akzeptiert, ist jedoch veraltet, da das PostgreSQL-Backend in Gramps Web API 4.0 entfernt wird.
`POSTGRES_HOST` | Der Hostname des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Baum-Setup mit dem SharedPostgreSQL-Backend verwendet wird.
`POSTGRES_PORT` | Der Port des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Baum-Setup mit dem SharedPostgreSQL-Backend verwendet wird.


### Einstellungen für OIDC-Authentifizierung

Diese Einstellungen sind erforderlich, wenn Sie die OpenID Connect (OIDC)-Authentifizierung mit externen Anbietern verwenden möchten. Für detaillierte Einrichtungsanweisungen und Beispiele siehe [OIDC-Authentifizierung](oidc.md).

Schlüssel | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Standardmäßig auf `False`.
`OIDC_ISSUER` | OIDC-Anbieter-Aussteller-URL (für benutzerdefinierte OIDC-Anbieter)
`OIDC_CLIENT_ID` | OAuth-Client-ID (für benutzerdefinierte OIDC-Anbieter)
`OIDC_CLIENT_SECRET` | OAuth-Client-Geheimnis (für benutzerdefinierte OIDC-Anbieter)
`OIDC_NAME` | Benutzerdefinierter Anzeigename für den Anbieter. Standardmäßig auf "OIDC" gesetzt.
`OIDC_SCOPES` | OAuth-Scopes. Standardmäßig auf "openid email profile" gesetzt.
`OIDC_USERNAME_CLAIM` | Der Anspruch, der für den Benutzernamen verwendet werden soll. Standardmäßig auf "preferred_username" gesetzt.
`OIDC_OPENID_CONFIG_URL` | Optional: URL zum OpenID Connect-Konfigurationsendpunkt (wenn nicht der Standard `/.well-known/openid-configuration` verwendet wird)
`OIDC_PKCE` | Boolean, ob PKCE verwendet werden soll. Wenn nicht gesetzt, wird PKCE verwendet, wenn das Entdeckungsdokument des Anbieters `S256` auflistet. Siehe [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, ob die lokale Benutzername/Passwort-Authentifizierung deaktiviert werden soll. Standardmäßig auf `False`.
`OIDC_AUTO_REDIRECT` | Boolean, ob automatisch zu OIDC umgeleitet werden soll, wenn nur ein Anbieter konfiguriert ist. Standardmäßig auf `False`.

#### Eingebaute OIDC-Anbieter

Für integrierte Anbieter (Google, Microsoft) verwenden Sie diese Einstellungen:

Schlüssel | Beschreibung
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Client-ID für Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Client-Geheimnis für Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | Client-ID für Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Client-Geheimnis für Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Boolean, PKCE-Einstellung für Google, siehe [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolean, PKCE-Einstellung für Microsoft, siehe [PKCE](oidc.md#pkce)

#### OIDC-Rollenabbildung

Diese Einstellungen ermöglichen es Ihnen, OIDC-Gruppen/Rollen von Ihrem Identitätsanbieter auf Gramps Web-Benutzerrollen abzubilden:

Schlüssel | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig auf "groups" gesetzt.
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Admin"-Rolle zugeordnet ist.
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Owner"-Rolle zugeordnet ist.
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Editor"-Rolle zugeordnet ist.
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Contributor"-Rolle zugeordnet ist.
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Member"-Rolle zugeordnet ist.
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Guest"-Rolle zugeordnet ist.

### Einstellungen nur für KI-Funktionen

Diese Einstellungen sind erforderlich, wenn Sie KI-gestützte Funktionen wie Chat oder semantische Suche verwenden möchten. Siehe [Einrichten des KI-Chats](chat.md) für Details.

!!! warning "Semantische Suche ist veraltet"
    Die semantische Suche und damit die Einstellungen `VECTOR_EMBEDDING_*` sind veraltet und werden in Gramps Web API 3.25 entfernt. Danach wird `VECTOR_EMBEDDING_MODEL` weiterhin akzeptiert, aber ignoriert. Seit Gramps Web API 3.24 benötigt der KI-Chat nur `LLM_MODEL`.

Schlüssel | Beschreibung
----|-------------
`LLM_BASE_URL` | Basis-URL für die OpenAI-kompatible Chat-API. Standardmäßig auf `None`, was die OpenAI-API verwendet.
`LLM_MODEL` | Das Modell, das für die OpenAI-kompatible Chat-API verwendet werden soll. Wenn nicht gesetzt (Standard), ist der Chat deaktiviert. Ab v3.6.0 verwendet der KI-Assistent Pydantic AI mit Tool-Calling-Funktionen.
`VECTOR_EMBEDDING_MODEL` | **Veraltet**, wird in 3.25 entfernt. Das Modell, das für semantische Suchvektor-Einbettungen verwendet werden soll. Bei Verwendung eines lokalen Modells muss dies ein [Sentence Transformers](https://sbert.net/) Modellname sein. Bei Verwendung einer Remote-API (siehe `VECTOR_EMBEDDING_BASE_URL`) ist dies der Modellname, der dem Remote-Anbieter übergeben wird. Wenn nicht gesetzt (Standard), ist die semantische Suche deaktiviert. Vor Gramps Web API 3.24 war auch der Chat deaktiviert.
`VECTOR_EMBEDDING_BASE_URL` | **Veraltet**, wird in 3.25 entfernt. Basis-URL für eine Remote-OpenAI-kompatible Einbettungs-API (z. B. Ollama, OpenAI, LiteLLM). Wenn nicht gesetzt (Standard), wird ein lokales Sentence Transformers-Modell verwendet. Siehe [Verwendung einer Remote-Einbettungs-API](chat.md#using-a-remote-embedding-api) für Details.
`VECTOR_EMBEDDING_API_KEY` | **Veraltet**, wird in 3.25 entfernt. API-Schlüssel für authentifizierte Remote-Einbettungsanbieter. Nur erforderlich, wenn `VECTOR_EMBEDDING_BASE_URL` gesetzt ist und der Anbieter eine Authentifizierung erfordert.
`LLM_MAX_CONTEXT_LENGTH` | Zeichenlimit für den Familienstammbaumkontext, der dem LLM bereitgestellt wird. Standardmäßig auf 50000 gesetzt.
`LLM_SYSTEM_PROMPT` | Benutzerdefinierter System-Prompt für den LLM-Chat-Assistenten (v3.6.0+). Wenn nicht gesetzt, wird der standardmäßige genealogieoptimierte Prompt verwendet.


## Beispielkonfigurationsdatei

Eine minimale Konfigurationsdatei für die Produktion könnte so aussehen:
```python
TREE="Mein Familienstammbaum"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # Ihr geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Verwenden Sie implizites SSL für Port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # Ihr SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
