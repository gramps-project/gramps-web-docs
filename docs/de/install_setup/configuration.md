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

- prefixen Sie jeden Einstellungsnamen mit `GRAMPSWEB_`, um den Namen der Umgebungsvariable zu erhalten
- Verwenden Sie doppelte Unterstriche für verschachtelte Dictionary-Einstellungen, z. B. wird `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` den Wert der Konfigurationsoption `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` setzen

Beachten Sie, dass Konfigurationsoptionen, die über die Umgebung festgelegt werden, Vorrang vor denen in der Konfigurationsdatei haben. Wenn beide vorhanden sind, "gewinnt" die Umgebungsvariable.

## Vorhandene Konfigurationseinstellungen
Die folgenden Konfigurationsoptionen existieren.

### Erforderliche Einstellungen

Schlüssel | Beschreibung
----|-------------
`TREE` | Der Name der zu verwendenden Familienstammbaum-Datenbank. Zeigen Sie verfügbare Bäume mit `gramps -l` an. Wenn ein Baum mit diesem Namen nicht existiert, wird ein neuer leerer Baum erstellt.
`SECRET_KEY` | Der geheime Schlüssel für Flask. Der Schlüssel darf nicht öffentlich geteilt werden. Eine Änderung macht alle Zugriffstoken ungültig.
`USER_DB_URI` | Die Datenbank-URL der Benutzerdatenbank. Jede URL, die mit SQLAlchemy kompatibel ist, ist zulässig.

!!! info
    Sie können einen sicheren geheimen Schlüssel z. B. mit dem Befehl

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optionale Einstellungen

Schlüssel | Beschreibung
----|-------------
`MEDIA_BASE_DIR` | Pfad, der als Basisverzeichnis für Mediendateien verwendet wird, das das in Gramps festgelegte Medienbasisverzeichnis überschreibt. Bei Verwendung von [S3](s3.md) muss es die Form `s3://<bucket_name>` haben.
`SEARCH_INDEX_DB_URI` | Datenbank-URL für den Suchindex. Nur `sqlite` oder `postgresql` sind als Backends zulässig. Standardmäßig `sqlite:///indexdir/search_index.db`, was eine SQLite-Datei im Ordner `indexdir` erstellt, relativ zu dem Pfad, von dem das Skript ausgeführt wird.
`STATIC_PATH` | Pfad, um statische Dateien bereitzustellen (z. B. ein statisches Web-Frontend).
`BASE_URL` | Basis-URL, unter der die API erreichbar ist (z. B. `https://mygramps.mydomain.com/`). Dies ist notwendig, um z. B. korrekte Links zum Zurücksetzen des Passworts zu erstellen.
`CORS_ORIGINS` | Ursprünge, von denen CORS-Anfragen erlaubt sind. Standardmäßig sind alle nicht erlaubt. Verwenden Sie `"*"`, um Anfragen von jeder Domain zuzulassen.
`EMAIL_HOST` | SMTP-Server-Host (z. B. zum Senden von E-Mails zum Zurücksetzen des Passworts).
`EMAIL_PORT` | SMTP-Server-Port. Standardmäßig 465.
`EMAIL_HOST_USER` | SMTP-Server-Benutzername.
`EMAIL_HOST_PASSWORD` | SMTP-Server-Passwort.
`EMAIL_USE_TLS` | Boolean, ob TLS zum Senden von E-Mails verwendet werden soll. Standardmäßig `True`. Bei Verwendung von STARTTLS setzen Sie dies auf `False` und verwenden einen anderen Port als 25.
`DEFAULT_FROM_EMAIL` | "Von"-Adresse für automatisierte E-Mails.
`THUMBNAIL_CACHE_CONFIG` | Dictionary mit Einstellungen für den Thumbnail-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`REQUEST_CACHE_CONFIG` | Dictionary mit Einstellungen für den Anfrage-Cache. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`PERSISTENT_CACHE_CONFIG` | Dictionary mit Einstellungen für den persistenten Cache, der z. B. für Telemetrie verwendet wird. Siehe [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) für mögliche Einstellungen.
`CELERY_CONFIG` | Einstellungen für die Celery-Hintergrundaufgabenwarteschlange. Siehe [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) für mögliche Einstellungen.
`REPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgabe von ausgeführten Gramps-Berichten gespeichert wird.
`EXPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgabe des Exports der Gramps-Datenbank gespeichert wird.
`REGISTRATION_DISABLED` | Wenn `True`, wird die Registrierung neuer Benutzer nicht erlaubt (Standard `False`).
`DISABLE_TELEMETRY` | Wenn `True`, wird die Statistiktelemetrie deaktiviert (Standard `False`). Siehe [Telemetrie](telemetry.md) für Details.

!!! info
    Bei der Verwendung von Umgebungsvariablen für die Konfiguration müssen boolesche Optionen wie `EMAIL_USE_TLS` entweder den String `true` oder `false` (groß- und kleinschreibungssensitiv!) haben.

### Einstellungen nur für PostgreSQL-Backend-Datenbank

Dies ist erforderlich, wenn Sie Ihre Gramps-Datenbank so konfiguriert haben, dass sie mit dem [PostgreSQL-Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) funktioniert.

Schlüssel | Beschreibung
----|-------------
`POSTGRES_USER` | Der Benutzername für die Datenbankverbindung.
`POSTGRES_PASSWORD` | Das Passwort für den Datenbankbenutzer.

### Einstellungen, die für das Hosting mehrerer Bäume relevant sind

Die folgenden Einstellungen sind relevant, wenn [mehrere Bäume gehostet werden](multi-tree.md).

Schlüssel | Beschreibung
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, ob ein separates Unterverzeichnis für die Mediendateien jedes Baumes verwendet werden soll. Standardmäßig `False`, aber es wird dringend empfohlen, `True` in einem Multi-Tree-Setup zu verwenden.
`NEW_DB_BACKEND` | Das Datenbank-Backend, das für neu erstellte Familienstammbäume verwendet werden soll. Muss eines von `sqlite`, `postgresql` oder `sharedpostgresql` sein. Standardmäßig `sqlite`.
`POSTGRES_HOST` | Der Hostname des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Tree-Setup mit dem SharedPostgreSQL-Backend verwendet wird.
`POSTGRES_PORT` | Der Port des PostgreSQL-Servers, der zum Erstellen neuer Bäume verwendet wird, wenn ein Multi-Tree-Setup mit dem SharedPostgreSQL-Backend verwendet wird.

### Einstellungen für OIDC-Authentifizierung

Diese Einstellungen sind erforderlich, wenn Sie die OpenID Connect (OIDC) Authentifizierung mit externen Anbietern verwenden möchten. Für detaillierte Installationsanweisungen und Beispiele siehe [OIDC-Authentifizierung](oidc.md).

Schlüssel | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Standardmäßig `False`.
`OIDC_ISSUER` | OIDC-Anbieter-Issuer-URL (für benutzerdefinierte OIDC-Anbieter).
`OIDC_CLIENT_ID` | OAuth-Client-ID (für benutzerdefinierte OIDC-Anbieter).
`OIDC_CLIENT_SECRET` | OAuth-Client-Geheimnis (für benutzerdefinierte OIDC-Anbieter).
`OIDC_NAME` | Benutzerdefinierter Anzeigename für den Anbieter. Standardmäßig "OIDC".
`OIDC_SCOPES` | OAuth-Scopes. Standardmäßig "openid email profile".
`OIDC_USERNAME_CLAIM` | Der Anspruch, der für den Benutzernamen verwendet werden soll. Standardmäßig "preferred_username".
`OIDC_OPENID_CONFIG_URL` | Optional: URL zum OpenID Connect-Konfigurationsendpunkt (wenn nicht der Standard `/.well-known/openid-configuration` verwendet wird).
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, ob die lokale Benutzername/Passwort-Authentifizierung deaktiviert werden soll. Standardmäßig `False`.
`OIDC_AUTO_REDIRECT` | Boolean, ob automatisch zu OIDC umgeleitet werden soll, wenn nur ein Anbieter konfiguriert ist. Standardmäßig `False`.

#### Eingebaute OIDC-Anbieter

Für integrierte Anbieter (Google, Microsoft, GitHub) verwenden Sie diese Einstellungen:

Schlüssel | Beschreibung
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Client-ID für Google OAuth.
`OIDC_GOOGLE_CLIENT_SECRET` | Client-Geheimnis für Google OAuth.
`OIDC_MICROSOFT_CLIENT_ID` | Client-ID für Microsoft OAuth.
`OIDC_MICROSOFT_CLIENT_SECRET` | Client-Geheimnis für Microsoft OAuth.
`OIDC_GITHUB_CLIENT_ID` | Client-ID für GitHub OAuth.
`OIDC_GITHUB_CLIENT_SECRET` | Client-Geheimnis für GitHub OAuth.

#### OIDC-Rollen-Zuordnung

Diese Einstellungen ermöglichen es Ihnen, OIDC-Gruppen/Rollen von Ihrem Identitätsanbieter auf Gramps Web-Benutzerrollen abzubilden:

Schlüssel | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig "groups".
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Admin"-Rolle zugeordnet ist.
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Owner"-Rolle zugeordnet ist.
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Editor"-Rolle zugeordnet ist.
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Contributor"-Rolle zugeordnet ist.
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Member"-Rolle zugeordnet ist.
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps-"Guest"-Rolle zugeordnet ist.

### Einstellungen nur für KI-Funktionen

Diese Einstellungen sind erforderlich, wenn Sie KI-gestützte Funktionen wie Chat oder semantische Suche verwenden möchten.

Schlüssel | Beschreibung
----|-------------
`LLM_BASE_URL` | Basis-URL für die OpenAI-kompatible Chat-API. Standardmäßig `None`, was die OpenAI-API verwendet.
`LLM_MODEL` | Das Modell, das für die OpenAI-kompatible Chat-API verwendet werden soll. Wenn nicht festgelegt (Standard), ist der Chat deaktiviert.
`VECTOR_EMBEDDING_MODEL` | Das [Sentence Transformers](https://sbert.net/) Modell, das für semantische Suchvektor-Einbettungen verwendet werden soll. Wenn nicht festgelegt (Standard), sind semantische Suche und Chat deaktiviert.
`LLM_MAX_CONTEXT_LENGTH` | Zeichenlimit für den Familienstammbaumkontext, der dem LLM bereitgestellt wird. Standardmäßig 50000.

## Beispielkonfigurationsdatei

Eine minimale Konfigurationsdatei für die Produktion könnte so aussehen:
```python
TREE="Mein Familienstammbaum"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # Ihr geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # Ihr SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
