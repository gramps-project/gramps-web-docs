# OIDC-Authentifizierung

Gramps Web unterstützt die OpenID Connect (OIDC) Authentifizierung, die es Benutzern ermöglicht, sich über externe Identitätsanbieter anzumelden. Dazu gehören sowohl beliebte Anbieter wie Google, Microsoft und GitHub als auch benutzerdefinierte OIDC-Anbieter wie Keycloak, Authentik und andere.

## Übersicht

Die OIDC-Authentifizierung ermöglicht Ihnen:

- Externe Identitätsanbieter für die Benutzerauthentifizierung zu verwenden
- Mehrere Authentifizierungsanbieter gleichzeitig zu unterstützen
- OIDC-Gruppen/Rollen den Gramps Web-Benutzerrollen zuzuordnen
- Single Sign-On (SSO) und Single Sign-Out zu implementieren
- Optional die lokale Benutzername/Passwort-Authentifizierung zu deaktivieren

## Konfiguration

Um die OIDC-Authentifizierung zu aktivieren, müssen Sie die entsprechenden Einstellungen in Ihrer Gramps Web-Konfigurationsdatei oder in Umgebungsvariablen konfigurieren. Siehe die [Serverkonfiguration](configuration.md#settings-for-oidc-authentication) Seite für eine vollständige Liste der verfügbaren OIDC-Einstellungen.

!!! info
    Wenn Sie Umgebungsvariablen verwenden, denken Sie daran, jeden Einstellungsnamen mit `GRAMPSWEB_` zu prefixen (z. B. `GRAMPSWEB_OIDC_ENABLED`). Siehe [Konfigurationsdatei vs. Umgebungsvariablen](configuration.md#configuration-file-vs-environment-variables) für Details.

### Eingebaute Anbieter

Gramps Web hat integrierte Unterstützung für beliebte Identitätsanbieter. Um sie zu verwenden, müssen Sie nur die Client-ID und das Client-Geheimnis angeben:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` und `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` und `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` und `OIDC_GITHUB_CLIENT_SECRET`

Sie können mehrere Anbieter gleichzeitig konfigurieren. Das System erkennt automatisch, welche Anbieter basierend auf den Konfigurationswerten verfügbar sind.

### Benutzerdefinierte OIDC-Anbieter

Für benutzerdefinierte OIDC-Anbieter (wie Keycloak, Authentik oder jeden standardkonformen OIDC-Anbieter) verwenden Sie diese Einstellungen:

Key | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Auf `True` setzen.
`OIDC_ISSUER` | Die Issuer-URL Ihres Anbieters
`OIDC_CLIENT_ID` | Client-ID für Ihren OIDC-Anbieter
`OIDC_CLIENT_SECRET` | Client-Geheimnis für Ihren OIDC-Anbieter
`OIDC_NAME` | Benutzerdefinierter Anzeigename (optional, Standardwert ist "OIDC")
`OIDC_SCOPES` | OAuth-Bereiche (optional, Standardwert ist "openid email profile")

## Erforderliche Umleitungs-URIs

Beim Konfigurieren Ihres OIDC-Anbieters müssen Sie die folgende Umleitungs-URI registrieren:

**Für OIDC-Anbieter, die Wildcards unterstützen: (z. B. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Wo `*` ein Regex-Wildcard ist. Abhängig vom Regex-Interpreter Ihres Anbieters könnte dies auch ein `.*` oder ähnliches sein. Stellen Sie sicher, dass Regex aktiviert ist, wenn Ihr Anbieter dies erfordert (z. B. Authentik).

**Für OIDC-Anbieter, die keine Wildcards unterstützen: (z. B. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

## Rollen-Zuordnung

Gramps Web kann OIDC-Gruppen oder -Rollen von Ihrem Identitätsanbieter automatisch den Gramps Web-Benutzerrollen zuordnen. Dies ermöglicht es Ihnen, Benutzerberechtigungen zentral in Ihrem Identitätsanbieter zu verwalten.

### Konfiguration

Verwenden Sie diese Einstellungen, um die Rollen-Zuordnung zu konfigurieren:

Key | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardwert ist "groups"
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Admin"-Rolle zugeordnet ist
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Owner"-Rolle zugeordnet ist
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Editor"-Rolle zugeordnet ist
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Contributor"-Rolle zugeordnet ist
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Member"-Rolle zugeordnet ist
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Guest"-Rolle zugeordnet ist

### Verhalten der Rollen-Zuordnung

- Wenn keine Rollen-Zuordnung konfiguriert ist (keine `OIDC_GROUP_*` Variablen gesetzt), werden die bestehenden Benutzerrollen beibehalten
- Benutzern wird die höchste Rolle zugewiesen, die sie basierend auf ihrer Gruppenmitgliedschaft haben
- Die Rollen-Zuordnung ist standardmäßig groß-/kleinschreibungsempfindlich (hängt von Ihrem OIDC-Anbieter ab)

## OIDC-Abmeldung

Gramps Web unterstützt Single Sign-Out (SSO-Abmeldung) für OIDC-Anbieter. Wenn ein Benutzer sich nach der Authentifizierung über OIDC von Gramps Web abmeldet, wird er automatisch zur Abmeldeseite des Identitätsanbieters weitergeleitet, sofern der Anbieter den `end_session_endpoint` unterstützt.

### Backchannel-Abmeldung

Gramps Web implementiert die OpenID Connect Back-Channel Logout-Spezifikation. Dies ermöglicht es Identitätsanbietern, Gramps Web zu benachrichtigen, wenn sich ein Benutzer von einer anderen Anwendung oder dem Identitätsanbieter selbst abmeldet.

#### Konfiguration

Um die Backchannel-Abmeldung mit Ihrem Identitätsanbieter zu konfigurieren:

1. **Registrieren Sie den Backchannel-Abmelde-Endpunkt** in der Client-Konfiguration Ihres Identitätsanbieters:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Konfigurieren Sie Ihren Anbieter**, um Abmeldbenachrichtigungen zu senden. Die genauen Schritte hängen von Ihrem Anbieter ab:

   **Keycloak:**

   - Navigieren Sie in Ihrer Client-Konfiguration zu "Einstellungen"
   - Setzen Sie die "Backchannel Logout URL" auf `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Aktivieren Sie "Backchannel Logout Session Required", wenn Sie eine sitzungsbasierte Abmeldung wünschen

   **Authentik:**

   - Fügen Sie in Ihrer Anbieter-Konfiguration die Backchannel-Abmelde-URL hinzu
   - Stellen Sie sicher, dass der Anbieter konfiguriert ist, um Abmeldetoken zu senden

!!! warning "Token-Ablauf"
    Aufgrund der zustandslosen Natur von JWT-Tokens protokolliert die Backchannel-Abmeldung derzeit das Abmeldeereignis, kann jedoch bereits ausgegebene JWT-Tokens nicht sofort widerrufen. Tokens bleiben gültig, bis sie ablaufen (Standard: 15 Minuten für Zugriffstokens).

    Für erhöhte Sicherheit sollten Sie in Betracht ziehen:

    - Die Ablaufzeit von JWT-Tokens zu reduzieren (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Benutzer zu schulen, sich manuell von Gramps Web abzumelden, wenn sie sich von Ihrem Identitätsanbieter abmelden

!!! tip "So funktioniert es"
    Wenn sich ein Benutzer von Ihrem Identitätsanbieter oder einer anderen Anwendung abmeldet:

    1. Sendet der Anbieter ein `logout_token` JWT an den Backchannel-Abmelde-Endpunkt von Gramps Web
    2. Gramps Web validiert das Token und protokolliert das Abmeldeereignis
    3. Die JTI des Abmeldetokens wird zu einer Blockliste hinzugefügt, um Wiederholungsangriffe zu verhindern
    4. Alle neuen API-Anfragen mit dem JWT des Benutzers werden abgelehnt, sobald die Tokens ablaufen

## Beispielkonfigurationen

### Benutzerdefinierter OIDC-Anbieter (Keycloak)

```python
TREE="Mein Familienstammbaum"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # Ihr geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Benutzerdefinierte OIDC-Konfiguration
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Familien-SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Optional: automatisch zur SSO-Anmeldung umleiten
OIDC_DISABLE_LOCAL_AUTH=True  # Optional: Benutzername/Passwort-Anmeldung deaktivieren

# Optional: Rollen-Zuordnung von OIDC-Gruppen zu Gramps-Rollen
OIDC_ROLE_CLAIM="groups"  # oder "roles" je nach Anbieter
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # Ihr SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Eingebauter Anbieter (Google)

```python
TREE="Mein Familienstammbaum"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # Ihr geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Mehrere Anbieter

Sie können mehrere OIDC-Anbieter gleichzeitig aktivieren:

```python
TREE="Mein Familienstammbaum"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # Ihr geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Benutzerdefinierter Anbieter
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Unternehmens-SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Ein von der Community erstellter OIDC-Setup-Leitfaden für Gramps Web ist auf der [offiziellen Authelia-Dokumentationswebsite](https://www.authelia.com/integration/openid-connect/clients/gramps/) verfügbar.

### Keycloak

Die meisten Konfigurationen für Keycloak können auf ihren Standardwerten belassen werden (*Client → Client erstellen → Client-Authentifizierung AN*). Es gibt einige Ausnahmen:

1. **OpenID-Bereich** – Der `openid`-Bereich ist nicht standardmäßig in allen Keycloak-Versionen enthalten. Um Probleme zu vermeiden, fügen Sie ihn manuell hinzu: *Client → [Gramps-Client] → Client-Bereiche → Bereich hinzufügen → Name: `openid` → Als Standard festlegen.*
2. **Rollen** – Rollen können entweder auf Client-Ebene oder global pro Realm zugewiesen werden.

    * Wenn Sie Client-Rollen verwenden, setzen Sie die Konfigurationsoption `OIDC_ROLE_CLAIM` auf: `resource_access.[gramps-client-name].roles`
    * Um Rollen für Gramps sichtbar zu machen, navigieren Sie zu *Client-Bereichen* (der oberste Abschnitt, nicht unter dem spezifischen Client), dann: *Rollen → Mapper → Client-Rollen → Zu Benutzerinformationen hinzufügen → AN.*
