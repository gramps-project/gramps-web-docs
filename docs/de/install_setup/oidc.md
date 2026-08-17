# OIDC-Authentifizierung

Gramps Web unterstützt die OpenID Connect (OIDC) Authentifizierung, die es Benutzern ermöglicht, sich mit externen Identitätsanbietern anzumelden. Dazu gehören die integrierten Anbieter Google und Microsoft sowie benutzerdefinierte OIDC-Anbieter wie Keycloak, Authentik und Authelia.

!!! warning "GitHub als OIDC-Anbieter wird nicht mehr unterstützt"
    Wenn Sie `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` aus einer früheren Version gesetzt haben, entfernen Sie diese – sie werden jetzt ignoriert, und Benutzer, die sich zuvor über GitHub angemeldet haben, können sich nicht mehr auf diese Weise anmelden. GitHub ist ein OAuth 2.0-Anbieter, kein OpenID Connect-Anbieter, und hat nie den Anspruch zurückgegeben, auf den Gramps Web für die Identität angewiesen ist, sodass es nie vollständig zuverlässig war.

## Übersicht

Die OIDC-Authentifizierung ermöglicht es Ihnen:

- Externe Identitätsanbieter für die Benutzeranmeldung zu verwenden
- Mehrere Authentifizierungsanbieter gleichzeitig zu unterstützen
- OIDC-Gruppen/Rollen auf Gramps Web-Benutzerrollen abzubilden
- Single Sign-On (SSO) und Single Sign-Out zu implementieren
- Optional die lokale Benutzername/Passwort-Authentifizierung zu deaktivieren

## Konfiguration

Um die OIDC-Authentifizierung zu aktivieren, müssen Sie die entsprechenden Einstellungen in Ihrer Gramps Web-Konfigurationsdatei oder in Umgebungsvariablen konfigurieren. Siehe die [Serverkonfiguration](configuration.md#settings-for-oidc-authentication) Seite für eine vollständige Liste der verfügbaren OIDC-Einstellungen.

!!! info
    Wenn Sie Umgebungsvariablen verwenden, denken Sie daran, jeden Einstellungsnamen mit `GRAMPSWEB_` zu präfixieren (z. B. `GRAMPSWEB_OIDC_ENABLED`). Siehe [Konfigurationsdatei vs. Umgebungsvariablen](configuration.md#configuration-file-vs-environment-variables) für Details.

### Integrierte Anbieter

Gramps Web hat integrierte Unterstützung für beliebte Identitätsanbieter. Um sie zu verwenden, müssen Sie nur die Client-ID und das Client-Geheimnis angeben:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` und `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` und `OIDC_MICROSOFT_CLIENT_SECRET`

Sie können mehrere Anbieter gleichzeitig konfigurieren. Das System erkennt automatisch, welche Anbieter basierend auf den Konfigurationswerten verfügbar sind.

!!! tip "Microsoft: Single-Tenant-Bereitstellungen"
    Der integrierte Microsoft-Anbieter verwendet den Multi-Tenant `/common` Endpunkt und akzeptiert Anmeldungen von jedem Microsoft-Konto. Wenn Sie nur Benutzer aus Ihrem eigenen Mandanten zulassen möchten, verwenden Sie stattdessen den [benutzerdefinierten OIDC-Anbieter](#custom-oidc-providers) mit Ihrer mandantenspezifischen Aussteller-URL, die die Aussteller-Validierung aktiv hält und die Anmeldungen auf diesen Mandanten beschränkt.

### Benutzerdefinierte OIDC-Anbieter

Für benutzerdefinierte OIDC-Anbieter (wie Keycloak, Authentik, Authelia oder einen Single-Tenant Microsoft Entra-Mandanten) verwenden Sie diese Einstellungen:

Key | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Auf `True` setzen.
`OIDC_ISSUER` | Die Aussteller-URL Ihres Anbieters. Die Entdeckung wird von `<issuer>/.well-known/openid-configuration` abgerufen.
`OIDC_CLIENT_ID` | Client-ID für Ihren OIDC-Anbieter
`OIDC_CLIENT_SECRET` | Client-Geheimnis für Ihren OIDC-Anbieter
`OIDC_NAME` | Benutzerdefinierter Anzeigename (optional, standardmäßig "OIDC")
`OIDC_SCOPES` | OAuth-Bereiche (optional, standardmäßig "openid email profile")
`OIDC_USERNAME_CLAIM` | Anspruch, der zur Generierung des Benutzernamens verwendet wird (optional, standardmäßig "preferred_username")

### Multi-Tree-Setups

Auf einem Multi-Tree-Server muss der Baum, in den sich der Benutzer anmeldet, bekannt sein, bevor Gramps Web zum Identitätsanbieter umleitet, sodass die Anmeldung mit Folgendem beginnt:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` ist in Multi-Tree-Setups erforderlich; das Weglassen oder das Übergeben der ID eines Baums, der nicht existiert, führt zum Scheitern der Anmeldung. Auf einem Single-Tree-Server ist `tree` optional, muss jedoch, wenn angegeben, mit dem konfigurierten `TREE` übereinstimmen.

Eine OIDC-Identität ist genau einem Gramps Web-Konto zugeordnet, das wiederum genau zu einem Baum gehört – die Anmeldung gegen einen anderen Baum schlägt fehl, anstatt das Konto zu verschieben. Es gibt keine Möglichkeit, eine einzelne Identität beim Anbieter mit Konten in mehreren Bäumen zu verknüpfen; Benutzer, die Zugriff auf mehrere Bäume benötigen, benötigen separate Identitäten beim Anbieter (z. B. unterschiedliche Benutzernamen oder Konten).

!!! warning
    Ein Konto eines Site-Administrators ohne zugeordneten Baum (siehe [Erstellen eines Administratorkontos](../administration/owner.md)) kann sich nicht über OIDC anmelden, da die OIDC-Anmeldung immer einen Baum erfordert. Solche Konten müssen stattdessen mit einem lokalen Benutzername/Passwort erstellt und authentifiziert werden.

## Erforderliche Umleitungs-URIs

Beim Konfigurieren Ihres OIDC-Anbieters müssen Sie die folgende Umleitungs-URI registrieren:

**Für OIDC-Anbieter, die Wildcards unterstützen: (z. B. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Wo `*` ein Regex-Wildcard ist. Je nach Regex-Interpreter Ihres Anbieters könnte dies auch ein `.*` oder ähnliches sein. Stellen Sie sicher, dass Regex aktiviert ist, wenn Ihr Anbieter dies erfordert (z. B. Authentik).

**Für OIDC-Anbieter, die keine Wildcards unterstützen: (z. B. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Der Baum ist niemals Teil der Umleitungs-URI, selbst auf Multi-Tree-Servern – er wird separat in der Sitzung übertragen, da Anbieter erfordern, dass die Umleitungs-URI genau mit der registrierten übereinstimmt.

## Rollenabbildung

Gramps Web kann OIDC-Gruppen oder -Rollen von Ihrem Identitätsanbieter automatisch auf Gramps Web-Benutzerrollen abbilden. Dies ermöglicht es Ihnen, Benutzerberechtigungen zentral in Ihrem Identitätsanbieter zu verwalten. Die Rollenabbildung funktioniert für alle Anbieter, ob integriert oder benutzerdefiniert, gleich.

### Konfiguration

Verwenden Sie diese Einstellungen zur Konfiguration der Rollenabbildung:

Key | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig auf "groups". Punktierte Pfade werden unterstützt, z. B. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Admin"-Rolle zugeordnet ist
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Owner"-Rolle zugeordnet ist
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Editor"-Rolle zugeordnet ist
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Contributor"-Rolle zugeordnet ist
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Member"-Rolle zugeordnet ist
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der der Gramps "Guest"-Rolle zugeordnet ist

### Verhalten der Rollenabbildung

Wenn keine `OIDC_GROUP_*`-Einstellung konfiguriert ist, ist die Rollenabbildung deaktiviert und Rollen werden manuell in Gramps Web verwaltet; neue OIDC-Konten werden dann deaktiviert erstellt und müssen von einem bestehenden Eigentümer oder Administrator genehmigt werden (siehe [Erster Login und Bootstrap](#first-login-and-bootstrapping) unten).

Sobald die Rollenabbildung konfiguriert ist, erfolgt bei jeder Anmeldung:

- Wenn der Rollenanspruch vorhanden ist und der Benutzer zu einer abgebildeten Gruppe gehört, erhält er die entsprechende Rolle.
- Wenn der Rollenanspruch vorhanden ist, der Benutzer jedoch keiner abgebildeten Gruppe angehört, wird seine Rolle auf deaktiviert gesetzt. Dies ist ein fail-closed Standard, kein Fehler – Gramps Web kann keine Rolle für eine Gruppe ableiten, die es nicht erkennt.
- Wenn der Rollenanspruch im Token völlig fehlt, bleibt die bestehende Rolle unverändert; ein neues Konto wird weiterhin standardmäßig deaktiviert.

!!! warning "Google sendet keinen Gruppenanspruch"
    Googles Tokens enthalten niemals einen `groups`-Anspruch, sodass bei aktivierter Rollenabbildung Google-Anmeldungen unter "Anspruch fehlt" fallen: Bestehende Benutzer behalten ihre Rolle, aber neue Google-Benutzer werden deaktiviert erstellt und benötigen eine manuelle Genehmigung. Behalten Sie dies im Hinterkopf, bevor Sie die Rollenabbildung nur für einen anderen Anbieter aktivieren – sie deaktiviert nicht von sich aus bestehende Google-Benutzer.

Microsoft Entra gibt App-Rollen und Gruppenmitgliedschaften nur im ID-Token zurück, nicht vom Benutzerinfo-Endpunkt. Gramps Web fügt die Ansprüche des ID-Tokens in die Benutzerinfo-Antwort ein, sodass `OIDC_ROLE_CLAIM` auf die gleiche Weise funktioniert wie bei anderen Anbietern; wo beide einen Anspruch enthalten, hat der Benutzerinfo-Wert Vorrang.

## Erster Login und Bootstrap

Neue Konten, die über OIDC erstellt werden, starten deaktiviert, es sei denn, die Rollenabbildung weist ihnen eine Rolle zu (siehe oben). In einer brandneuen Instanz kann niemand ein deaktiviertes Konto genehmigen, und wenn `OIDC_DISABLE_LOCAL_AUTH` ebenfalls aktiviert ist, gibt es keinen Passwort-Login, auf den man zurückgreifen kann.

!!! warning "Konfigurieren Sie eine Eigentümer-/Admin-Gruppe vor dem ersten Login"
    Bevor sich jemand zum ersten Mal über OIDC anmeldet, setzen Sie `OIDC_GROUP_OWNER` (oder `OIDC_GROUP_ADMIN`) und stellen Sie sicher, dass der erste Benutzer zu dieser Gruppe beim Anbieter gehört. Andernfalls kann die Instanz überhaupt nicht über OIDC gebootstrapped werden.

## Konten und Benutzernamen

Konten, die über OIDC erstellt werden, erhalten einen generierten Benutzernamen, der einmal bei der Kontoerstellung zugewiesen wird und sich bei späteren Anmeldungen nie ändert:

- Integrierte Anbieter: `<provider>_<claim value>`, z. B. `microsoft_alice@contoso.com`
- Benutzerdefinierter Anbieter: der nackte Anspruchswert, z. B. `alice`

Ein numerisches Suffix wird bei Kollisionen angehängt. Es gibt keine Möglichkeit, den Benutzernamen eines über OIDC erstellten Kontos später umzubenennen; der vollständige Name und die E-Mail-Adresse hingegen werden bei jeder Anmeldung aktualisiert.

Eine OIDC-Anmeldung wird niemals an ein bestehendes lokales Konto angehängt, das zufällig die gleiche E-Mail-Adresse hat – dies ist absichtlich, da die Verknüpfung von Konten über E-Mail ein Vektor für Kontoübernahmen ist. Ein Benutzer, der bereits ein lokales Konto hat, erhält beim ersten Mal, wenn er sich über OIDC anmeldet, ein zweites, separates Konto.

E-Mail-Adressen vom Anbieter werden nur gespeichert, wenn der Anbieter sie als verifiziert markiert (oder den `email_verified`-Anspruch ganz weglässt) und wenn die Adresse nicht bereits von einem anderen Konto verwendet wird; andernfalls erfolgt die Anmeldung, ohne eine E-Mail-Adresse zu speichern.

## OIDC-Abmeldung

Gramps Web unterstützt Single Sign-Out (SSO-Abmeldung) für OIDC-Anbieter. `GET /api/oidc/logout/` sucht den `end_session_endpoint` des Anbieters und gibt ihn als `logout_url` in der Antwort zurück; es ist das Gramps Web-Frontend, das den Browser dorthin navigiert, um die Sitzung beim Identitätsanbieter tatsächlich zu beenden. `logout_url` ist `null`, wenn der Anbieter keinen `end_session_endpoint` hat.

!!! warning "Tokens werden bei der Abmeldung nicht widerrufen"
    Das Abmelden beendet nur die Browsersitzung; es gibt derzeit keine Möglichkeit, ein bereits ausgegebenes Gramps Web-Token zu widerrufen. Tokens bleiben gültig, bis sie ablaufen (`JWT_ACCESS_TOKEN_EXPIRES`, standardmäßig 15 Minuten für Zugriffstokens), unabhängig davon, ob der Benutzer sich seitdem bei Gramps Web oder beim Identitätsanbieter abgemeldet hat.

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

# Optional: Rollenabbildung von OIDC-Gruppen zu Gramps-Rollen
OIDC_ROLE_CLAIM="groups"  # oder "roles" je nach Anbieter
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Verwenden Sie implizites SSL für Port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # Ihr SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Integrierter Anbieter (Google)

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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Ein von der Community erstellter OIDC-Setup-Leitfaden für Gramps Web ist auf der [offiziellen Authelia-Dokumentationswebsite](https://www.authelia.com/integration/openid-connect/clients/gramps/) verfügbar.

### Keycloak

Die meisten Konfigurationen für Keycloak können auf ihren Standardwerten belassen werden (*Client → Client erstellen → Client-Authentifizierung EIN*). Es gibt einige Ausnahmen:

1. **OpenID-Bereich** – Der `openid`-Bereich ist in allen Keycloak-Versionen nicht standardmäßig enthalten. Um Probleme zu vermeiden, fügen Sie ihn manuell hinzu: *Client → [Gramps-Client] → Client-Bereiche → Bereich hinzufügen → Name: `openid` → Als Standard festlegen.*
2. **Rollen** – Rollen können entweder auf der Client-Ebene oder global pro Realm zugewiesen werden.

    * Wenn Sie Client-Rollen verwenden, setzen Sie die Konfigurationsoption `OIDC_ROLE_CLAIM` auf: `resource_access.[gramps-client-name].roles`
    * Um Rollen für Gramps sichtbar zu machen, navigieren Sie zu *Client-Bereichen* (dem obersten Abschnitt, nicht unter dem spezifischen Client), dann: *Rollen → Mapper → Client-Rollen → Zu Benutzerinfo hinzufügen → EIN.*
