# Serverkonfiguration

Mit dem standardmäßigen Docker-Image kann die gesamte erforderliche Konfiguration über den Browser vorgenommen werden. Je nach Bereitstellung kann es jedoch notwendig sein, die Serverkonfiguration anzupassen.

Diese Seite listet alle Methoden zur Änderung der Konfiguration und alle vorhandenen Konfigurationsoptionen auf.


## Konfigurationsdatei vs. Umgebungsvariablen

Für die Einstellungen können Sie entweder eine Konfigurationsdatei oder Umgebungsvariablen verwenden.

Wenn Sie das [Docker Compose basierte Setup](deployment.md) verwenden, können Sie eine Konfigurationsdatei einfügen, indem Sie den folgenden Listeneintrag unter dem Schlüssel `volumes:` im Block `grampsweb:` hinzufügen:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
wobei `/path/to/config.cfg` der Pfad zur Konfigurationsdatei im Dateisystem Ihres Servers ist (die rechte Seite bezieht sich auf den Pfad im Container und darf nicht geändert werden).

Bei der Verwendung von Umgebungsvariablen,

- prefixen Sie jeden Einstellungsnamen mit `GRAMPSWEB_`, um den Namen der Umgebungsvariablen zu erhalten
- Verwenden Sie doppelte Unterstriche für verschachtelte Dictionary-Einstellungen, z.B. `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` setzt den Wert der Konfigurationsoption `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Bitte beachten Sie, dass Konfigurationsoptionen, die über die Umgebung festgelegt werden, Vorrang vor denjenigen in der Konfigurationsdatei haben. Wenn beide vorhanden sind, "gewinnt" die Umgebungsvariable.

!!! warning "Nicht präfixierte Umgebungsvariablen sind veraltet"
    Aus historischen Gründen können eine Handvoll von Einstellungen – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` und `STATIC_PATH` – weiterhin über eine Umgebungsvariable *ohne* das Präfix `GRAMPSWEB_` gesetzt werden. Dies ist veraltet, protokolliert eine Warnung beim Start und wird in einer zukünftigen Version nicht mehr funktionieren. Verwenden Sie immer die präfixierte Form, z.B. `GRAMPSWEB_TREE` anstelle von `TREE`.

    Beachten Sie, dass dies nur Umgebungsvariablen betrifft. In einer Konfigurationsdatei werden die Einstellungsnamen immer unpräfixiert verwendet.

!!! tip "Überprüfung auf veraltete Optionen"
    Veraltete Konfigurationsoptionen, von denen Ihr Server noch abhängt – wie nicht präfixierte Umgebungsvariablen, `SEARCH_INDEX_DIR` oder `EMAIL_USE_TLS` – werden beim Start als Warnungen protokolliert. Seit Gramps Web API 3.22 werden sie auch zusammen mit ihrem Ersatz und der Version, in der die Unterstützung entfernt wird, oben auf der **Systeminformationen**-Seite (erreichbar über das Benutzersymbol in der oberen App-Leiste), angezeigt, wenn Sie als Administrator angemeldet sind.

    Die E-Mail-Einstellungen und die Basis-URL, die der Einrichtungsassistent älterer Versionen in der Datenbank gespeichert hat, werden dort ebenfalls aufgeführt. Stellen Sie sie in Ihrer Konfiguration auf die gespeicherten Werte ein; die Warnung verschwindet, sobald sie übereinstimmen.

## Vorhandene Konfigurationseinstellungen
Die folgenden Konfigurationsoptionen existieren.

### Erforderliche Einstellungen

Schlüssel | Beschreibung
----|-------------
`TREE` | Der Name der zu verwendenden Familienstammbaum-Datenbank. Zeigen Sie verfügbare Bäume mit `gramps -l` an. Wenn ein Baum mit diesem Namen nicht existiert, wird ein neuer leerer Baum erstellt.
`SECRET_KEY` | Der geheime Schlüssel für Flask. Der Schlüssel darf nicht öffentlich geteilt werden. Eine Änderung macht alle Zugriffstoken ungültig.
`USER_DB_URI` | Die Datenbank-URL der Benutzerdatenbank. Jede URL, die mit SQLAlchemy kompatibel ist, ist erlaubt.

!!! info
    Sie können einen sicheren geheimen Schlüssel z.B. mit dem Befehl generieren

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optionale Einstellungen

Schlüssel | Beschreibung
----|-------------
`MEDIA_BASE_DIR` | Pfad, der als Basisverzeichnis für Mediendateien verwendet wird, überschreibt das in Gramps festgelegte Medienbasisverzeichnis. Bei Verwendung von [S3](s3.md) muss es die Form `s3://<bucket_name>` haben.
`TREE_ID` | Der Verzeichnisname der Familienstammbaum-Datenbank, die im Einzelbaum-Modus verwendet werden soll (wenn `TREE` nicht auf `*` gesetzt ist). Wenn gesetzt, identifiziert der Server den Baum anhand seines Verzeichnisnamens anstelle seines Anzeigenamens, was robuster gegenüber Umbenennungen ist. Erforderlich, wenn Sie den Baum über die API umbenennen möchten. Der Verzeichnisname kann über `GET /api/trees/-` (das `id`-Feld) gefunden werden.
`SEARCH_INDEX_DB_URI` | Datenbank-URL für den Suchindex. Nur `sqlite` oder `postgresql` sind als Backends erlaubt. Standardmäßig `sqlite:///indexdir/search_index.db`, wodurch eine SQLite-Datei im Ordner `indexdir` relativ zu dem Pfad erstellt wird, von dem das Skript ausgeführt wird.
`SEARCH_INDEX_DIR` | **Veraltet** (verwenden Sie stattdessen `SEARCH_INDEX_DB_URI`). Verzeichnis, das den Suchindex enthält. Wenn gesetzt, während `SEARCH_INDEX_DB_URI` nicht gesetzt ist, wird die Suchindex-URL als `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` abgeleitet.
`STATIC_PATH` | Pfad zum Bereitstellen von statischen Dateien (z.B. ein statisches Web-Frontend)
`BASE_URL` | Basis-URL, unter der die API erreichbar ist (z.B. `https://mygramps.mydomain.com/`). Dies ist notwendig, um z.B. korrekte Links zum Zurücksetzen des Passworts zu erstellen. Web Push erfordert ebenfalls eine öffentlich erreichbare HTTPS-URL; die Standard-URL `http://localhost/` deaktiviert Web Push. Wenn Sie diese Einstellung über die Umgebung konfigurieren, verwenden Sie `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Ursprünge, von denen CORS-Anfragen erlaubt sind. Standardmäßig sind alle nicht erlaubt. Verwenden Sie `"*"`, um Anfragen von jeder Domain zuzulassen.
`EMAIL_HOST` | SMTP-Server-Host (z.B. zum Senden von E-Mails zum Zurücksetzen des Passworts)
`EMAIL_PORT` | SMTP-Server-Port. Standardmäßig 465
`EMAIL_HOST_USER` | SMTP-Server-Benutzername
`EMAIL_HOST_PASSWORD` | SMTP-Server-Passwort
`EMAIL_USE_TLS` | **Veraltet** (verwenden Sie stattdessen `EMAIL_USE_SSL` oder `EMAIL_USE_STARTTLS`). Boolean, ob TLS zum Senden von E-Mails verwendet werden soll. Standardmäßig `True`. Bei Verwendung von STARTTLS setzen Sie dies auf `False` und verwenden einen anderen Port als 25.
`EMAIL_USE_SSL` | Boolean, ob implizites SSL/TLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig `True`, wenn `EMAIL_USE_TLS` nicht explizit gesetzt ist. Wird typischerweise mit Port 465 verwendet.
`EMAIL_USE_STARTTLS` | Boolean, ob explizites STARTTLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig `False`. Wird typischerweise mit Port 587 oder 25 verwendet.
`DEFAULT_FROM_EMAIL` | "Von"-Adresse für automatisierte E-Mails
`THUMBNAIL_CACHE_CONFIG` | Dictionary mit Einstellungen für den Thumbnail-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`REQUEST_CACHE_CONFIG` | Dictionary mit Einstellungen für den Anfrage-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`PERSISTENT_CACHE_CONFIG` | Dictionary mit Einstellungen für den persistenten Cache, der z.B. für Telemetrie verwendet wird. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`CELERY_CONFIG` | Einstellungen für die Celery-Hintergrundaufgabenwarteschlange. Siehe [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) für mögliche Einstellungen.
`REPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgaben von ausgeführten Gramps-Berichten gespeichert werden
`EXPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgaben des Exports der Gramps-Datenbank gespeichert werden
`BACKUP_DIR` | Verzeichnis, in dem [Backups](../administration/backups.md) gespeichert werden, in einem Unterverzeichnis pro Baum (v3.24.0+). Wenn nicht gesetzt (Standard), können Backups nicht auf dem Server gespeichert werden, können aber weiterhin aus einer hochgeladenen Datei wiederhergestellt werden. Verwenden Sie einen persistenten Speicherort, z.B. ein Docker-Volume, und vorzugsweise einen, der selbst gesichert oder an anderer Stelle synchronisiert wird.
`BACKUP_KEEP` | Anzahl der pro Baum gespeicherten Backups; ältere werden gelöscht, wenn ein neues Backup erstellt wird (v3.24.0+). Standardmäßig `5`
`RATE_LIMIT_BACKUP` | Ratenlimit für die Erstellung von Backups, pro Baum (v3.24.0+). Standardmäßig `"10 pro Tag"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Ratenlimit für die Erstellung von Medienarchiven auf der Exportseite. Standardmäßig `"1 pro Stunde"`
`REGISTRATION_DISABLED` | Wenn `True`, keine neue Benutzerregistrierung zulassen (Standard `False`). Seit Gramps Web API 3.26 wird die Anmeldeseite dann auch ihren Registrierungslink ausblenden.
`PROXY_FIX_X_FOR` | Anzahl der vertrauenswürdigen Reverse-Proxys vor Gramps Web (v3.26.0+). Setzen Sie auf `1` hinter einem einzelnen Reverse-Proxy, damit die Ratenlimits pro Client und nicht für alle Benutzer zusammen gelten. Standardmäßig `0`. Setzen Sie es nur, wenn der Server ausschließlich über diese Proxys erreichbar ist.
`DISABLE_TELEMETRY` | Wenn `True`, Statistik-Telemetrie deaktivieren (Standard `False`). Siehe [Telemetrie](telemetry.md) für Details.
`PILLOW_MAX_IMAGE_PIXELS` | Setzt den Parameter PIL.Image.MAX_IMAGE_PIXELS, der die Anzahl der Pixel angibt, die das verarbeitete Bild enthalten kann. Siehe [Dokumentation](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) für Details.
`MAX_THUMBNAIL_FILE_BYTES` | Setzt eine harte maximale Dateigröße für Thumbnails. Standardmäßig `50 * 1024 * 1024` (50 MB). Eine Erhöhung kann den Speicherverbrauch erheblich steigern und zu Speichermangelabstürzen oder Datenverlust führen, wenn große Dateien im Speicher dekomprimiert werden.


!!! info
    Bei der Verwendung von Umgebungsvariablen für die Konfiguration müssen boolesche Optionen wie `EMAIL_USE_SSL` entweder die Zeichenfolge `true` oder `false` sein (groß-/kleinschreibungssensitiv!).


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
`MEDIA_PREFIX_TREE` | Boolean, ob ein separates Unterverzeichnis für die Mediendateien jedes Baums verwendet werden soll. Standardmäßig `False`, wird jedoch dringend empfohlen, in einem Multi-Tree-Setup `True` zu verwenden.
`NEW_DB_BACKEND` | Das Datenbank-Backend, das für neu erstellte Familienstammbäume verwendet werden soll. Muss eines von `sqlite` oder `sharedpostgresql` sein. Standardmäßig `sqlite`. Der Wert `postgresql` wird weiterhin akzeptiert, ist jedoch veraltet, da das PostgreSQL-Backend in Gramps Web API 4.0 entfernt wird.
`POSTGRES_HOST` | Der Hostname des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Tree-Setup mit dem SharedPostgreSQL-Backend verwendet wird.
`POSTGRES_PORT` | Der Port des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Tree-Setup mit dem SharedPostgreSQL-Backend verwendet wird.


### Einstellungen für OIDC-Authentifizierung

Diese Einstellungen sind erforderlich, wenn Sie die OpenID Connect (OIDC) Authentifizierung mit externen Anbietern verwenden möchten. Für detaillierte Einrichtungsanleitungen und Beispiele siehe [OIDC-Authentifizierung](oidc.md).

Schlüssel | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Standardmäßig `False`.
`OIDC_ISSUER` | OIDC-Anbieter-Issuer-URL (für benutzerdefinierte OIDC-Anbieter)
`OIDC_CLIENT_ID` | OAuth-Client-ID (für benutzerdefinierte OIDC-Anbieter)
`OIDC_CLIENT_SECRET` | OAuth-Client-Geheimnis (für benutzerdefinierte OIDC-Anbieter)
`OIDC_NAME` | Benutzerdefinierter Anzeigename für den Anbieter. Standardmäßig "OIDC"
`OIDC_SCOPES` | OAuth-Bereiche. Standardmäßig "openid email profile"
`OIDC_USERNAME_CLAIM` | Der Anspruch, der für den Benutzernamen verwendet werden soll. Standardmäßig "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Optional: URL zum OpenID Connect-Konfigurationsendpunkt (wenn nicht der Standard `/.well-known/openid-configuration` verwendet wird)
`OIDC_PKCE` | Boolean, ob PKCE verwendet werden soll. Wenn nicht gesetzt, wird PKCE verwendet, wenn das Entdeckungsdokument des Anbieters `S256` auflistet. Siehe [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, ob die lokale Benutzername/Passwort-Authentifizierung deaktiviert werden soll. Standardmäßig `False`
`OIDC_AUTO_REDIRECT` | Boolean, ob automatisch zu OIDC umgeleitet werden soll, wenn nur ein Anbieter konfiguriert ist. Standardmäßig `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Liste von `https`-URIs, an denen native Apps das Anmeldeergebnis empfangen können (v3.26.0+), als JSON-Liste in einer Umgebungsvariable festgelegt. Standardmäßig leer. Nur erforderlich, wenn die Dokumentation einer nativen App danach fragt. Siehe [Native Apps](oidc.md#native-apps)

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
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig "groups"
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Admin"-Rolle zugeordnet ist
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Owner"-Rolle zugeordnet ist
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Editor"-Rolle zugeordnet ist
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Contributor"-Rolle zugeordnet ist
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Member"-Rolle zugeordnet ist
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Guest"-Rolle zugeordnet ist

### Einstellungen nur für KI-Funktionen

Diese Einstellungen sind erforderlich, wenn Sie den KI-Chat verwenden möchten. Siehe [Einrichten des KI-Chats](chat.md) für Details.

!!! note
    Die Einstellungen `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` und `VECTOR_EMBEDDING_API_KEY` für die semantische Suche werden seit Gramps Web API 3.25 ignoriert, die die semantische Suche entfernt hat. Der KI-Chat benötigt nur `LLM_MODEL`.

Schlüssel | Beschreibung
----|-------------
`LLM_BASE_URL` | Basis-URL für die OpenAI-kompatible Chat-API. Standardmäßig `None`, was die OpenAI-API verwendet.
`LLM_MODEL` | Das Modell, das für die OpenAI-kompatible Chat-API verwendet werden soll. Wenn nicht gesetzt (Standard), ist der Chat deaktiviert. Ab v3.6.0 verwendet der KI-Assistent Pydantic AI mit Tool-Calling-Funktionen.
`LLM_MAX_OUTPUT_TOKENS` | Maximale Anzahl von Tokens, die das Modell in einer einzelnen Antwort generieren darf. Standardmäßig nicht gesetzt, wodurch das Limit beim Modellserver bleibt. Nützlich für Modellserver ohne eigenes Limit, bei denen eine Antwort sonst unbegrenzt weitergehen könnte.
`LLM_MAX_CONTEXT_LENGTH` | Zeichenlimit für den Familienstammbaum-Kontext, der dem LLM bereitgestellt wird. Standardmäßig 50000.
`LLM_SYSTEM_PROMPT` | Benutzerdefinierter System-Prompt für den LLM-Chat-Assistenten (v3.6.0+). Wenn nicht gesetzt, wird der standardmäßige, genealogisch optimierte Prompt verwendet.
`LLM_VISION` | Boolean, ob Benutzer Bilder an ihre Fragen anhängen können (v3.26.0+). Aktivieren Sie dies nur, wenn das Modell Bilder akzeptiert. Standardmäßig `False`. Siehe [Bilder in Fragen](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Boolean, ob der Assistent Änderungen am Baum vorschlagen kann, die die Benutzer überprüfen und anwenden können (v3.26.0+). Standardmäßig `False`. Siehe [Lassen Sie den Assistenten Änderungen vorschlagen](chat.md#letting-the-assistant-propose-changes)


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
