# Serverkonfiguration

Mit dem standardmäßigen Docker-Image kann die gesamte erforderliche Konfiguration über den Browser vorgenommen werden. Je nach Bereitstellung kann es jedoch erforderlich sein, die Serverkonfiguration anzupassen.

Diese Seite listet alle Methoden zum Ändern der Konfiguration sowie alle vorhandenen Konfigurationsoptionen auf.


## Konfigurationsdatei vs. Umgebungsvariablen

Für die Einstellungen kannst du entweder eine Konfigurationsdatei oder Umgebungsvariablen verwenden.

Wenn du die [auf Docker Compose basierende Einrichtung](deployment.md) verwendest, kannst du eine Konfigurationsdatei einbinden, indem du unter dem Schlüssel `volumes:` im Block `grampsweb:` den folgenden Listeneintrag hinzufügst:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
Dabei ist `/path/to/config.cfg` der Pfad zur Konfigurationsdatei im Dateisystem deines Servers (die rechte Seite verweist auf den Pfad im Container und darf nicht geändert werden).

Bei der Verwendung von Umgebungsvariablen gilt:

- Stelle jedem Einstellungsnamen `GRAMPSWEB_` voran, um den Namen der Umgebungsvariablen zu erhalten.
- Verwende doppelte Unterstriche für verschachtelte Dictionary-Einstellungen, z. B. setzt `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` den Wert der Konfigurationsoption `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`.

Beachte, dass über die Umgebung gesetzte Konfigurationsoptionen Vorrang vor den Optionen in der Konfigurationsdatei haben. Wenn beide vorhanden sind, „gewinnt“ die Umgebungsvariable.

!!! warning "Nicht vorangestellte Umgebungsvariablen sind veraltet"
    Aus historischen Gründen können einige Einstellungen – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` und `STATIC_PATH` – weiterhin über eine Umgebungsvariable *ohne* das Präfix `GRAMPSWEB_` gesetzt werden. Dies ist veraltet, wird beim Start protokolliert und wird in einer zukünftigen Version nicht mehr funktionieren. Verwende immer die Form mit Präfix, z. B. `GRAMPSWEB_TREE` statt `TREE`.

    Beachte, dass dies nur Umgebungsvariablen betrifft. In einer Konfigurationsdatei werden die Einstellungsnamen immer ohne Präfix verwendet.

!!! tip "Auf veraltete Optionen prüfen"
    Veraltete Konfigurationsoptionen, von denen dein Server weiterhin abhängt – etwa Umgebungsvariablen ohne Präfix, `SEARCH_INDEX_DIR` oder `EMAIL_USE_TLS` – werden beim Start als Warnungen protokolliert. Seit Gramps Web API 3.22 werden sie außerdem zusammen mit ihrem Ersatz und der Version, in der die Unterstützung entfernt wird, oben auf der Seite **Systeminformationen** aufgelistet (erreichbar über das Benutzersymbol in der oberen App-Leiste), wenn du als Administrator angemeldet bist.

    Die E-Mail-Einstellungen und die Basis-URL, die der Assistent für die Ersteinrichtung älterer Versionen in der Datenbank gespeichert hat, werden dort ebenfalls aufgelistet. Übernimm die gespeicherten Werte in deine Konfiguration; die Warnung verschwindet, sobald sie übereinstimmen.

## Vorhandene Konfigurationseinstellungen
Die folgenden Konfigurationsoptionen sind vorhanden.

### Erforderliche Einstellungen

Key | Beschreibung
----|-------------
`TREE` | Der Name der zu verwendenden Familienbaumdatenbank. Zeige verfügbare Bäume mit `gramps -l` an. Wenn kein Baum mit diesem Namen vorhanden ist, wird ein neuer leerer Baum erstellt.
`SECRET_KEY` | Der geheime Schlüssel für Flask. Das Geheimnis darf nicht öffentlich geteilt werden. Durch eine Änderung werden alle Zugriffstoken ungültig.
`USER_DB_URI` | Die Datenbank-URL der Benutzerdatenbank. Jede mit SQLAlchemy kompatible URL ist zulässig.

!!! info
    Du kannst beispielsweise mit folgendem Befehl einen sicheren geheimen Schlüssel erzeugen:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optionale Einstellungen

Key | Beschreibung
----|-------------
`MEDIA_BASE_DIR` | Als Basisverzeichnis für Mediendateien zu verwendender Pfad, der das in Gramps festgelegte Medienbasisverzeichnis überschreibt. Bei Verwendung von [S3](s3.md) muss die Form `s3://<bucket_name>` verwendet werden.
`TREE_ID` | Der Verzeichnisname der zu verwendenden Familienbaumdatenbank im Einzelbaum-Modus (wenn `TREE` nicht auf `*` gesetzt ist). Wenn dieser Wert gesetzt ist, identifiziert der Server den Baum anhand seines Verzeichnisnamens statt anhand seines Anzeigenamens, was bei Umbenennungen robuster ist. Erforderlich, wenn du den Baum über die API umbenennen möchtest. Der Verzeichnisname kann über `GET /api/trees/-` (das Feld `id`) ermittelt werden.
`SEARCH_INDEX_DB_URI` | Datenbank-URL für den Suchindex. Als Backends sind nur `sqlite` oder `postgresql` zulässig. Standardmäßig `sqlite:///indexdir/search_index.db`; dabei wird eine SQLite-Datei im Ordner `indexdir` relativ zum Pfad erstellt, von dem aus das Skript ausgeführt wird.
`SEARCH_INDEX_DIR` | **Veraltet** (verwende stattdessen `SEARCH_INDEX_DB_URI`). Verzeichnis, das den Suchindex enthält. Wenn dieser Wert gesetzt ist, während `SEARCH_INDEX_DB_URI` nicht gesetzt ist, wird die URL des Suchindex als `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` abgeleitet.
`STATIC_PATH` | Pfad, von dem statische Dateien bereitgestellt werden (z. B. ein statisches Web-Frontend).
`BASE_URL` | Basis-URL, unter der die API erreichbar ist (z. B. `https://mygramps.mydomain.com/`). Dies ist beispielsweise erforderlich, um korrekte Links zum Zurücksetzen von Passwörtern zu erstellen. Web Push erfordert ebenfalls eine öffentlich erreichbare HTTPS-URL; der Standardwert `http://localhost/` deaktiviert Web Push. Wenn du diese Einstellung über die Umgebung konfigurierst, verwende `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Ursprünge, von denen CORS-Anfragen zulässig sind. Standardmäßig sind alle nicht zulässig. Verwende `"*"`, um Anfragen von jeder Domain zu erlauben.
`EMAIL_HOST` | Host des SMTP-Servers (z. B. zum Senden von E-Mails zum Zurücksetzen des Passworts).
`EMAIL_PORT` | Port des SMTP-Servers. Standardmäßig 465.
`EMAIL_HOST_USER` | Benutzername des SMTP-Servers.
`EMAIL_HOST_PASSWORD` | Passwort des SMTP-Servers.
`EMAIL_USE_TLS` | **Veraltet** (verwende stattdessen `EMAIL_USE_SSL` oder `EMAIL_USE_STARTTLS`). Boolescher Wert, ob TLS zum Senden von E-Mails verwendet werden soll. Standardmäßig `True`. Bei Verwendung von STARTTLS setze diesen Wert auf `False` und verwende einen anderen Port als 25.
`EMAIL_USE_SSL` | Boolescher Wert, ob implizites SSL/TLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig `True`, wenn `EMAIL_USE_TLS` nicht ausdrücklich gesetzt ist. Wird typischerweise mit Port 465 verwendet.
`EMAIL_USE_STARTTLS` | Boolescher Wert, ob explizites STARTTLS für SMTP verwendet werden soll (v3.6.0+). Standardmäßig `False`. Wird typischerweise mit Port 587 oder 25 verwendet.
`DEFAULT_FROM_EMAIL` | „Von“-Adresse für automatisierte E-Mails.
`THUMBNAIL_CACHE_CONFIG` | Dictionary mit Einstellungen für den Vorschaubild-Cache. Informationen zu möglichen Einstellungen findest du unter [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/).
`REQUEST_CACHE_CONFIG` | Dictionary mit Einstellungen für den Anfrage-Cache. Informationen zu möglichen Einstellungen findest du unter [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/).
`PERSISTENT_CACHE_CONFIG` | Dictionary mit Einstellungen für den persistenten Cache, der z. B. für Telemetrie verwendet wird. Informationen zu möglichen Einstellungen findest du unter [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/).
`CELERY_CONFIG` | Einstellungen für die Celery-Hintergrundaufgabenwarteschlange. Informationen zu möglichen Einstellungen findest du unter [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html).
`REPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgabe ausgeführter Gramps-Berichte gespeichert wird.
`EXPORT_DIR` | Temporäres Verzeichnis, in dem die Ausgabe des Exports der Gramps-Datenbank gespeichert wird.
`BACKUP_DIR` | Verzeichnis, in dem [Sicherungen](../administration/backups.md) in einem Unterverzeichnis pro Baum gespeichert werden (v3.24.0+). Wenn dieser Wert nicht gesetzt ist (Standard), können Sicherungen nicht auf dem Server gespeichert werden, sie können jedoch weiterhin aus einer hochgeladenen Datei wiederhergestellt werden. Verwende einen persistenten Speicherort, z. B. ein Docker-Volume, und vorzugsweise einen, der selbst gesichert oder an einen anderen Ort synchronisiert wird.
`BACKUP_KEEP` | Anzahl der pro Baum aufzubewahrenden Sicherungen; ältere Sicherungen werden gelöscht, wenn eine neue Sicherung erstellt wird (v3.24.0+). Standardmäßig `5`.
`RATE_LIMIT_BACKUP` | Ratenbegrenzung für das Erstellen von Sicherungen pro Baum (v3.24.0+). Standardmäßig `"10 per day"`.
`RATE_LIMIT_MEDIA_ARCHIVE` | Ratenbegrenzung für das Erstellen von Medienarchiven auf der Exportseite. Standardmäßig `"1 per hour"`.
`REGISTRATION_DISABLED` | Wenn `True`, wird die Registrierung neuer Benutzer verhindert (Standard `False`). Seit Gramps Web API 3.26 wird auf der Anmeldeseite dann auch der Registrierungslink ausgeblendet.
`PROXY_FIX_X_FOR` | Anzahl vertrauenswürdiger Reverse-Proxys vor Gramps Web (v3.26.0+). Setze den Wert hinter einem einzelnen Reverse-Proxy auf `1`, damit Ratenbegrenzungen pro Client statt für alle Benutzer gemeinsam gelten. Standardmäßig `0`. Setze den Wert nur, wenn der Server ausschließlich über diese Proxys erreichbar ist.
`DISABLE_TELEMETRY` | Wenn `True`, wird die Statistik-Telemetrie deaktiviert (Standard `False`). Einzelheiten findest du unter [Telemetrie](telemetry.md).
`PILLOW_MAX_IMAGE_PIXELS` | Setzt den Parameter PIL.Image.MAX_IMAGE_PIXELS, der angibt, wie viele Pixel das verarbeitete Bild enthalten darf. Einzelheiten findest du in der [Dokumentation](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS).
`MAX_THUMBNAIL_FILE_BYTES` | Legt eine harte maximale Dateigröße für Vorschaubilder fest. Standardmäßig `50 * 1024 * 1024` (50 MB). Eine Erhöhung kann die Speichernutzung stark steigern und zu Abstürzen wegen unzureichenden Speichers oder Datenverlust führen, wenn große Dateien im Speicher dekomprimiert werden.


!!! info
    Bei der Verwendung von Umgebungsvariablen für die Konfiguration müssen boolesche Optionen wie `EMAIL_USE_SSL` entweder die Zeichenfolge `true` oder `false` sein (Groß-/Kleinschreibung beachten!).


### Einstellungen für PostgreSQL-Datenbanken

Diese Einstellungen sind erforderlich, wenn deine Familienbäume in einer [PostgreSQL-Datenbank](postgres.md) unter Verwendung des SharedPostgreSQL-Add-ons gehostet werden.

Key | Beschreibung
----|-------------
`POSTGRES_USER` | Der Benutzername für die Datenbankverbindung.
`POSTGRES_PASSWORD` | Das Passwort für den Datenbankbenutzer.


### Einstellungen für das Hosten mehrerer Bäume

Die folgenden Einstellungen sind relevant, wenn du [mehrere Bäume hostest](multi-tree.md).


Key | Beschreibung
----|-------------
`MEDIA_PREFIX_TREE` | Boolescher Wert, ob ein separates Unterverzeichnis für die Mediendateien jedes Baums verwendet werden soll. Standardmäßig `False`; bei einer Einrichtung mit mehreren Bäumen wird jedoch dringend empfohlen, `True` zu verwenden.
`NEW_DB_BACKEND` | Das Datenbank-Backend, das für neu erstellte Familienbäume verwendet werden soll. Muss `sqlite` oder `sharedpostgresql` sein. Standardmäßig `sqlite`. Der Wert `postgresql` wird noch akzeptiert, ist jedoch veraltet, da das PostgreSQL-Backend in Gramps Web API 4.0 entfernt wird.
`POSTGRES_HOST` | Der Hostname des PostgreSQL-Servers, der beim Erstellen neuer Bäume verwendet wird, wenn eine Einrichtung mit mehreren Bäumen und dem SharedPostgreSQL-Backend genutzt wird.
`POSTGRES_PORT` | Der Port des PostgreSQL-Servers, der beim Erstellen neuer Bäume verwendet wird, wenn eine Einrichtung mit mehreren Bäumen und dem SharedPostgreSQL-Backend genutzt wird.


### Einstellungen für die OIDC-Authentifizierung

Diese Einstellungen werden benötigt, wenn du die OpenID-Connect-Authentifizierung (OIDC) mit externen Anbietern verwenden möchtest. Detaillierte Einrichtungsanweisungen und Beispiele findest du unter [OIDC-Authentifizierung](oidc.md).

Key | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolescher Wert, ob die OIDC-Authentifizierung aktiviert werden soll. Standardmäßig `False`.
`OIDC_ISSUER` | Aussteller-URL des OIDC-Anbieters (für benutzerdefinierte OIDC-Anbieter).
`OIDC_CLIENT_ID` | OAuth-Client-ID (für benutzerdefinierte OIDC-Anbieter).
`OIDC_CLIENT_SECRET` | OAuth-Client-Geheimnis (für benutzerdefinierte OIDC-Anbieter).
`OIDC_NAME` | Benutzerdefinierter Anzeigename für den Anbieter. Standardmäßig „OIDC“.
`OIDC_SCOPES` | OAuth-Scopes. Standardmäßig „openid email profile“.
`OIDC_USERNAME_CLAIM` | Der Claim, der für den Benutzernamen verwendet werden soll. Standardmäßig „preferred_username“.
`OIDC_OPENID_CONFIG_URL` | Optional: URL zum OpenID-Connect-Konfigurationsendpunkt (wenn nicht der Standard `/.well-known/openid-configuration` verwendet wird).
`OIDC_PKCE` | Boolescher Wert, ob PKCE verwendet werden soll. Wenn nicht gesetzt, wird PKCE verwendet, wenn das Discovery-Dokument des Anbieters `S256` aufführt. Siehe [PKCE](oidc.md#pkce).
`OIDC_DISABLE_LOCAL_AUTH` | Boolescher Wert, ob die lokale Authentifizierung mit Benutzername/Passwort deaktiviert werden soll. Standardmäßig `False`.
`OIDC_AUTO_REDIRECT` | Boolescher Wert, ob automatisch zu OIDC weitergeleitet werden soll, wenn nur ein Anbieter konfiguriert ist. Standardmäßig `False`.
`OIDC_ALLOWED_REDIRECT_URIS` | Liste von `https`-URIs, unter denen native Apps das Anmeldeergebnis empfangen können (v3.26.0+), als JSON-Liste in einer Umgebungsvariablen festgelegt. Standardmäßig leer. Nur erforderlich, wenn die Dokumentation einer nativen App dies verlangt. Siehe [Native Apps](oidc.md#native-apps).

#### Integrierte OIDC-Anbieter

Für integrierte Anbieter (Google, Microsoft) verwendest du diese Einstellungen:

Key | Beschreibung
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Client-ID für Google OAuth.
`OIDC_GOOGLE_CLIENT_SECRET` | Client-Geheimnis für Google OAuth.
`OIDC_MICROSOFT_CLIENT_ID` | Client-ID für Microsoft OAuth.
`OIDC_MICROSOFT_CLIENT_SECRET` | Client-Geheimnis für Microsoft OAuth.
`OIDC_GOOGLE_PKCE` | Boolesche PKCE-Einstellung für Google, siehe [PKCE](oidc.md#pkce).
`OIDC_MICROSOFT_PKCE` | Boolesche PKCE-Einstellung für Microsoft, siehe [PKCE](oidc.md#pkce).

#### OIDC-Rollenzuordnung

Mit diesen Einstellungen kannst du OIDC-Gruppen/Rollen deines Identitätsanbieters den Gramps-Web-Benutzerrollen zuordnen:

Key | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Claim-Name im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig „groups“.
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Admin“ zugeordnet wird.
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Owner“ zugeordnet wird.
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Editor“ zugeordnet wird.
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Contributor“ zugeordnet wird.
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Member“ zugeordnet wird.
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Guest“ zugeordnet wird.

### Einstellungen nur für KI-Funktionen

Diese Einstellungen werden benötigt, wenn du den KI-Chat verwenden möchtest. Einzelheiten findest du unter [KI-Chat einrichten](chat.md).

!!! note
    Die Einstellungen `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` und `VECTOR_EMBEDDING_API_KEY` für die semantische Suche werden seit Gramps Web API 3.25 ignoriert, da die semantische Suche entfernt wurde. Der KI-Chat benötigt nur `LLM_MODEL`.

Key | Beschreibung
----|-------------
`LLM_BASE_URL` | Basis-URL für die OpenAI-kompatible Chat-API. Standardmäßig `None`, wodurch die OpenAI-API verwendet wird.
`LLM_MODEL` | Das für die OpenAI-kompatible Chat-API zu verwendende Modell. Wenn dieser Wert nicht gesetzt ist (Standard), ist der Chat deaktiviert. Seit v3.6.0 verwendet der KI-Assistent Pydantic AI mit Tool-Aufruffunktionen.
`LLM_MAX_OUTPUT_TOKENS` | Maximale Anzahl von Tokens, die das Modell in einer einzelnen Antwort erzeugen darf. Standardmäßig nicht gesetzt, sodass das Limit dem Modellserver überlassen wird. Nützlich für Modellserver ohne eigenes Limit, bei denen eine Antwort andernfalls unbegrenzt fortgesetzt werden könnte.
`LLM_MAX_CONTEXT_LENGTH` | Zeichenbegrenzung für den Familienbaumkontext, der dem LLM bereitgestellt wird. Standardmäßig 50000.
`LLM_SYSTEM_PROMPT` | Benutzerdefinierte Systemaufforderung für den LLM-Chatassistenten (v3.6.0+). Wenn nicht gesetzt, wird die standardmäßige, für Genealogie optimierte Aufforderung verwendet.
`LLM_VISION` | Boolescher Wert, ob Benutzer Bilder an ihre Fragen anhängen können (v3.26.0+). Aktiviere diese Option nur, wenn das Modell Bilder akzeptiert. Standardmäßig `False`. Siehe [Bilder in Fragen](chat.md#images-in-questions).
`LLM_ALLOW_WRITE_PROPOSALS` | Boolescher Wert, ob der Assistent Benutzern Änderungen am Baum zur Überprüfung und Anwendung vorschlagen kann (v3.26.0+). Standardmäßig `False`. Siehe [Den Assistenten Änderungen vorschlagen lassen](chat.md#letting-the-assistant-propose-changes).


## Beispiel für eine Konfigurationsdatei

Eine minimale Konfigurationsdatei für den Produktivbetrieb könnte folgendermaßen aussehen:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # dein geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Implizites SSL für Port 465 verwenden
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # dein SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
```
