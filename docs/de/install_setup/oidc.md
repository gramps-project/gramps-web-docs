# OIDC-Authentifizierung

Gramps Web unterstützt die Authentifizierung über OpenID Connect (OIDC), sodass Benutzer sich mit externen Identitätsanbietern anmelden können. Dazu gehören die integrierten Anbieter Google und Microsoft sowie benutzerdefinierte OIDC-Anbieter wie Keycloak, Authentik und Authelia.

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

Um die OIDC-Authentifizierung zu aktivieren, müssen Sie die entsprechenden Einstellungen in Ihrer Gramps Web-Konfigurationsdatei oder den Umgebungsvariablen konfigurieren. Siehe die Seite [Serverkonfiguration](configuration.md#settings-for-oidc-authentication) für eine vollständige Liste der verfügbaren OIDC-Einstellungen.

!!! info
    Wenn Sie Umgebungsvariablen verwenden, denken Sie daran, jeden Einstellungsnamen mit `GRAMPSWEB_` zu kennzeichnen (z. B. `GRAMPSWEB_OIDC_ENABLED`). Siehe [Konfigurationsdatei vs. Umgebungsvariablen](configuration.md#configuration-file-vs-environment-variables) für weitere Details.

### Integrierte Anbieter

Gramps Web bietet integrierte Unterstützung für beliebte Identitätsanbieter. Um sie zu verwenden, müssen Sie nur die Client-ID und das Client-Geheimnis angeben:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` und `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` und `OIDC_MICROSOFT_CLIENT_SECRET`

Sie können mehrere Anbieter gleichzeitig konfigurieren. Das System erkennt automatisch, welche Anbieter basierend auf den Konfigurationswerten verfügbar sind.

!!! tip "Microsoft: Single-Tenant-Bereitstellungen"
    Der integrierte Microsoft-Anbieter verwendet den Multi-Tenant-Endpoint `/common` und akzeptiert von Haus aus Anmeldungen von jedem Microsoft-Konto. Wenn Sie nur Benutzer aus Ihrem eigenen Mandanten zulassen möchten, verwenden Sie stattdessen den [benutzerdefinierten OIDC-Anbieter](#custom-oidc-providers) mit Ihrer mandantenspezifischen Aussteller-URL, wodurch die Ausstellervalidierung aktiv bleibt und die Anmeldungen auf diesen Mandanten beschränkt werden.

### Benutzerdefinierte OIDC-Anbieter

Für benutzerdefinierte OIDC-Anbieter (wie Keycloak, Authentik, Authelia oder einen Single-Tenant Microsoft Entra-Mandanten) verwenden Sie diese Einstellungen:

Key | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Auf `True` setzen.
`OIDC_ISSUER` | Die Aussteller-URL Ihres Anbieters. Die Entdeckung wird von `<issuer>/.well-known/openid-configuration` abgerufen.
`OIDC_CLIENT_ID` | Client-ID für Ihren OIDC-Anbieter
`OIDC_CLIENT_SECRET` | Client-Geheimnis für Ihren OIDC-Anbieter
`OIDC_NAME` | Benutzerdefinierter Anzeigename (optional, standardmäßig "OIDC")
`OIDC_SCOPES` | OAuth-Scopes (optional, standardmäßig "openid email profile")
`OIDC_USERNAME_CLAIM` | Anspruch, der zur Generierung des Benutzernamens verwendet wird (optional, standardmäßig "preferred_username")
`OIDC_PKCE` | Ob PKCE verwendet werden soll, siehe [PKCE](#pkce) (optional, automatisch aktiviert, wenn der Anbieter dies unterstützt)

### PKCE

Seit Gramps Web API 3.23 unterstützt Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256`-Methode) für den Autorisierungscodefluss. Einige Identitätsanbieter, wie Pocket ID, können so konfiguriert werden, dass sie PKCE für einen Client *erfordern* und Anmeldungen ablehnen, die es nicht verwenden. Ältere Versionen der Gramps Web API verwenden niemals PKCE, sodass Anmeldungen mit einem solchen Client fehlschlagen.

Ob PKCE verwendet wird, wird bei der Anmeldung wie folgt entschieden:

- Wenn `OIDC_PKCE` auf `True` gesetzt ist, wird PKCE verwendet.
- Wenn `OIDC_PKCE` auf `False` gesetzt ist, wird PKCE nicht verwendet, auch wenn der Anbieter es unterstützt.
- Wenn `OIDC_PKCE` nicht gesetzt oder gesetzt, aber leer ist, wird PKCE verwendet, wenn das Entdeckungsdokument des Anbieters (`/.well-known/openid-configuration`) `S256` in `code_challenge_methods_supported` auflistet, andernfalls wird es nicht verwendet.

Für die meisten Setups müssen Sie nichts setzen. Setzen Sie `OIDC_PKCE` auf `True`, wenn Ihr Anbieter PKCE erfordert, aber `S256` nicht in seinem Entdeckungsdokument bewirbt, und auf `False`, wenn Ihr Anbieter `S256` bewirbt, es aber falsch behandelt. Als Umgebungsvariablen müssen Booleans klein geschrieben werden (`GRAMPSWEB_OIDC_PKCE=true`), siehe [Konfiguration](configuration.md).

Für die integrierten Anbieter sind die entsprechenden Optionen `OIDC_GOOGLE_PKCE` und `OIDC_MICROSOFT_PKCE`.

Der PKCE-Codeverifier wird in der Benutzersitzung zwischen der Weiterleitung zum Anbieter und dem Callback gespeichert, sodass dies keine Änderung der Weiterleitungs-URIs erfordert.

### Multi-Tree-Setups

Auf einem Multi-Tree-Server muss der Baum, in den sich der Benutzer anmeldet, bekannt sein, bevor Gramps Web zu dem Identitätsanbieter umleitet, sodass die Anmeldung mit Folgendem beginnt:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` ist in Multi-Tree-Setups erforderlich; das Weglassen oder das Übergeben der ID eines nicht existierenden Baums führt zum Fehlschlagen der Anmeldung. Auf einem Single-Tree-Server ist `tree` optional, muss aber, wenn angegeben, mit dem konfigurierten `TREE` übereinstimmen.

Eine OIDC-Identität ist genau einem Gramps Web-Konto zugeordnet, das wiederum genau zu einem Baum gehört – die Anmeldung gegen einen anderen Baum schlägt fehl, anstatt das Konto zu verschieben. Es gibt keine Möglichkeit, eine einzelne Identität beim Anbieter mit Konten in mehreren Bäumen zu verknüpfen; Benutzer, die Zugriff auf mehrere Bäume benötigen, benötigen separate Identitäten beim Anbieter (z. B. unterschiedliche Benutzernamen oder Konten).

!!! warning
    Ein Site-Administrator-Konto ohne zugeordneten Baum (siehe [Erstellen eines Administratorkontos](../administration/owner.md)) kann sich nicht über OIDC anmelden, da die OIDC-Anmeldung immer einen Baum erfordert. Solche Konten müssen stattdessen mit einem lokalen Benutzername/Passwort erstellt und authentifiziert werden.

## Erforderliche Weiterleitungs-URIs

Beim Konfigurieren Ihres OIDC-Anbieters müssen Sie die folgende Weiterleitungs-URI registrieren:

**Für OIDC-Anbieter, die Wildcards unterstützen: (z. B. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Dabei ist `*` ein Regex-Wildcard. Je nach Regex-Interpreter Ihres Anbieters könnte dies auch ein `.*` oder ähnlich sein. Stellen Sie sicher, dass Regex aktiviert ist, wenn Ihr Anbieter dies erfordert (z. B. Authentik).

**Für OIDC-Anbieter, die keine Wildcards unterstützen: (z. B. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Der Baum ist niemals Teil der Weiterleitungs-URI, selbst auf Multi-Tree-Servern – er wird separat in der Sitzung übertragen, da Anbieter erfordern, dass die Weiterleitungs-URI genau mit der registrierten übereinstimmt.

## Rollenabbildung

Gramps Web kann OIDC-Gruppen oder -Rollen von Ihrem Identitätsanbieter automatisch auf Gramps Web-Benutzerrollen abbilden. Dies ermöglicht es Ihnen, Benutzerberechtigungen zentral in Ihrem Identitätsanbieter zu verwalten. Die Rollenabbildung funktioniert für alle Anbieter, ob integriert oder benutzerdefiniert, gleich.

### Konfiguration

Verwenden Sie diese Einstellungen, um die Rollenabbildung zu konfigurieren:

Key | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Anspruchsname im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standardmäßig "groups". Punktierte Pfade werden unterstützt, z. B. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Admin"-Rolle abgebildet wird
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Owner"-Rolle abgebildet wird
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Editor"-Rolle abgebildet wird
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Contributor"-Rolle abgebildet wird
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Member"-Rolle abgebildet wird
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollename von Ihrem OIDC-Anbieter, der auf die Gramps "Guest"-Rolle abgebildet wird

### Verhalten der Rollenabbildung

Wenn keine `OIDC_GROUP_*`-Einstellung überhaupt konfiguriert ist, ist die Rollenabbildung deaktiviert und Rollen werden manuell in Gramps Web verwaltet; neue OIDC-Konten werden dann deaktiviert erstellt und müssen von einem bestehenden Eigentümer oder Administrator genehmigt werden (siehe [Erster Login und Bootstrapping](#first-login-and-bootstrapping) unten).

Sobald die Rollenabbildung konfiguriert ist, bei jeder Anmeldung:

- Wenn der Rollenanspruch vorhanden ist und der Benutzer zu einer abgebildeten Gruppe gehört, erhält er die entsprechende Rolle.
- Wenn der Rollenanspruch vorhanden ist, der Benutzer jedoch keiner abgebildeten Gruppe angehört, wird seine Rolle auf deaktiviert gesetzt. Dies ist ein fail-closed Standard, kein Fehler – Gramps Web kann keine Rolle für eine Gruppe ableiten, die es nicht erkennt.
- Wenn der Rollenanspruch im Token vollständig fehlt, bleibt die bestehende Rolle unverändert; ein neues Konto wird weiterhin standardmäßig deaktiviert.

!!! warning "Google sendet keinen Gruppenanspruch"
    Die Tokens von Google enthalten niemals einen `groups`-Anspruch, sodass bei aktivierter Rollenabbildung Google-Anmeldungen unter "Anspruch fehlt" fallen: bestehende Benutzer behalten ihre Rolle, aber neue Google-Benutzer werden deaktiviert erstellt und benötigen eine manuelle Genehmigung. Behalten Sie dies im Hinterkopf, bevor Sie die Rollenabbildung nur für einen anderen Anbieter aktivieren – sie deaktiviert nicht automatisch bestehende Google-Benutzer.

Microsoft Entra gibt App-Rollen und Gruppenmitgliedschaften nur im ID-Token zurück, nicht vom Userinfo-Endpunkt. Gramps Web fügt die Ansprüche des ID-Tokens in die Userinfo-Antwort ein, sodass `OIDC_ROLE_CLAIM` auf die gleiche Weise funktioniert wie bei anderen Anbietern; wo beide einen Anspruch enthalten, hat der Userinfo-Wert Vorrang.

## Erster Login und Bootstrapping

Neue Konten, die über OIDC erstellt werden, starten deaktiviert, es sei denn, die Rollenabbildung weist ihnen eine Rolle zu (siehe oben). Bei einer brandneuen Instanz kann niemand ein deaktiviertes Konto genehmigen, und wenn `OIDC_DISABLE_LOCAL_AUTH` ebenfalls aktiviert ist, gibt es auch keinen Passwort-Login, auf den man zurückgreifen könnte.

!!! warning "Konfigurieren Sie eine Eigentümer-/Admin-Gruppe vor dem ersten Login"
    Bevor sich jemand zum ersten Mal über OIDC anmeldet, setzen Sie `OIDC_GROUP_OWNER` (oder `OIDC_GROUP_ADMIN`) und stellen Sie sicher, dass der erste Benutzer zu dieser Gruppe beim Anbieter gehört. Andernfalls kann die Instanz überhaupt nicht über OIDC bootstrapped werden.

## Konten und Benutzernamen

Konten, die über OIDC erstellt werden, erhalten einen generierten Benutzernamen, der einmal bei der Kontoerstellung zugewiesen wird und sich bei späteren Anmeldungen nie ändert:

- Integrierte Anbieter: `<provider>_<claim value>`, z. B. `microsoft_alice@contoso.com`
- Benutzerdefinierter Anbieter: der nackte Anspruchswert, z. B. `alice`

Ein numerisches Suffix wird bei Kollisionen angehängt. Es gibt keine Möglichkeit, den Benutzernamen eines über OIDC erstellten Kontos danach umzubenennen; der vollständige Name und die E-Mail-Adresse hingegen werden bei jeder Anmeldung aktualisiert.

Eine OIDC-Anmeldung wird niemals an ein bestehendes lokales Konto angehängt, das zufällig dieselbe E-Mail-Adresse teilt – dies ist absichtlich, da die Verknüpfung von Konten über E-Mail ein Vektor für Kontenübernahmen ist. Ein Benutzer, der bereits ein lokales Konto hat, erhält beim ersten Login über OIDC ein zweites, separates Konto.

E-Mail-Adressen vom Anbieter werden nur gespeichert, wenn der Anbieter sie als verifiziert markiert (oder den `email_verified`-Anspruch vollständig weglässt); andernfalls erfolgt die Anmeldung, ohne eine E-Mail-Adresse zu speichern. Da E-Mail-Adressen nicht einzigartig sein müssen (seit Gramps Web API 3.22), wird eine Adresse gespeichert, selbst wenn ein anderes Konto sie bereits verwendet.

## OIDC-Abmeldung

Gramps Web unterstützt Single Sign-Out (SSO-Abmeldung) für OIDC-Anbieter. `GET /api/oidc/logout/` sucht den `end_session_endpoint` des Anbieters und gibt ihn als `logout_url` in der Antwort zurück; es ist das Gramps Web-Frontend, das den Browser dorthin navigiert, um die Sitzung beim Identitätsanbieter tatsächlich zu beenden. `logout_url` ist `null`, wenn der Anbieter keinen `end_session_endpoint` hat.

!!! warning "Tokens werden bei der Abmeldung nicht widerrufen"
    Die Abmeldung beendet nur die Browsersitzung; es gibt derzeit keine Möglichkeit, ein bereits ausgegebenes Gramps Web-Token zu widerrufen. Tokens bleiben gültig, bis sie ablaufen (`JWT_ACCESS_TOKEN_EXPIRES`, standardmäßig 15 Minuten für Zugriffstokens), unabhängig davon, ob der Benutzer sich seitdem bei Gramps Web oder beim Identitätsanbieter abgemeldet hat.

## Fehlersuche

Beginnen Sie an dem Punkt, an dem die Anmeldung stoppt, und folgen Sie dem Zweig. Gramps Web protokolliert den Grund für einen fehlgeschlagenen Callback (suchen Sie nach `OIDC callback error for provider` im Serverprotokoll), der in der Regel spezifischer ist als die im Browser angezeigte Nachricht.

**1. Fehlt die Schaltfläche zum Anmelden?**

- Überprüfen Sie `<BASE_URL>/api/oidc/config/`. Wenn `enabled` `false` oder `providers` leer ist, ist OIDC nicht konfiguriert: `OIDC_ENABLED` muss auf `True` gesetzt sein, und ein benutzerdefinierter Anbieter benötigt sowohl `OIDC_ISSUER` als auch `OIDC_CLIENT_ID`.
- Ein integrierter Anbieter (Google, Microsoft) ist nur registriert, wenn sowohl seine Client-ID als auch sein Client-Geheimnis gesetzt sind.
- Überprüfen Sie im Serverprotokoll beim Start auf `Could not load discovery document`. Das bedeutet, dass der Server `<issuer>/.well-known/openid-configuration` (oder `OIDC_OPENID_CONFIG_URL`) nicht erreichen konnte. Es wird beim ersten Gebrauch erneut versucht, aber der Gramps Web-Container muss die Aussteller-URL selbst auflösen und erreichen können, nicht nur Ihr Browser.

**2. Erhält der Browser einen Fehler, direkt nachdem er an den Anbieter gesendet wurde?**

Der Fehler wird vom Identitätsanbieter angezeigt, bevor Sie sich anmelden.

- *"redirect URI mismatch"* (oder ähnlich): Die beim Anbieter registrierte Weiterleitungs-URI muss genau übereinstimmen, einschließlich Schema, Host, Port und Anbieter-ID. Siehe [Erforderliche Weiterleitungs-URIs](#required-redirect-uris). Beachten Sie, dass sie aus `BASE_URL` erstellt wird, sodass ein falsches `BASE_URL` eine falsche Weiterleitungs-URI ergibt.
- *Ein PKCE-Fehler* (zum Beispiel `invalid_request`, "code challenge required" oder ein fehlender `code_challenge`-Parameter): Der Anbieter erfordert PKCE, aber Gramps Web hat es nicht gesendet. Gehen Sie zum [PKCE-Zweig](#pkce-branch) unten.

**3. Akzeptiert der Anbieter die Anmeldung, zeigt Gramps Web dann aber einen Fehler an?**

- *`mismatching_state`, oder der Fehler erwähnt die Sitzung oder den Zustand*: Der Browser hat das Sitzungscookie, das Gramps Web gesetzt hat, als die Anmeldung begann, nicht zurückgesendet. Dieses Cookie trägt auch den PKCE-Codeverifier. Stellen Sie sicher, dass die Adresse im Browser mit `BASE_URL` übereinstimmt (gleiches Schema und Host), dass ein Reverse-Proxy Cookies und den ursprünglichen Host weitergibt und dass die Anmeldung im selben Browser-Tab oder -Fenster gestartet und abgeschlossen wird.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: Überprüfen Sie das Serverprotokoll auf den zugrunde liegenden Grund. Häufige Ursachen sind ein falsches Client-Geheimnis, eine Aussteller-URL, die nicht mit dem `iss`-Anspruch der Tokens übereinstimmt, und der Anbieter, der einen Fehler an den Callback zurückgibt (zum Beispiel PKCE, siehe unten).
- *Zu viele Versuche*: Die Anmelde- und Callback-Endpunkte sind drosselungsbeschränkt (5 Anfragen pro Minute). Warten Sie eine Minute und versuchen Sie es erneut.

**4. Erfolgt die Anmeldung, aber Sie sehen "Konto wird überprüft" oder können nichts tun?**

Neue Konten werden deaktiviert erstellt, es sei denn, die Rollenabbildung weist ihnen eine Rolle zu. Siehe [Erster Login und Bootstrapping](#first-login-and-bootstrapping) und [Verhalten der Rollenabbildung](#role-mapping-behavior). Ein Administrator kann das Konto auch unter Einstellungen > Verwaltung > Benutzer verwalten aktivieren.

### PKCE-Zweig

Gramps Web entscheidet, ob PKCE verwendet wird, wenn eine Anmeldung gestartet wird (siehe [PKCE](#pkce)). Um herauszufinden, was für Ihr Setup passiert ist, arbeiten Sie diese Fragen der Reihe nach durch:

1. **Ist `OIDC_PKCE` gesetzt?** (Für integrierte Anbieter, `OIDC_GOOGLE_PKCE` oder `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE wird verwendet. Überspringen Sie zu Frage 3.
    - `False`: PKCE ist absichtlich deaktiviert, und das Entdeckungsdokument des Anbieters wird ignoriert. Wenn Ihr Anbieter PKCE erfordert, entfernen Sie die Einstellung oder setzen Sie sie auf `True`.
    - Nicht gesetzt oder leer: Fahren Sie mit Frage 2 fort.
2. **Listet das Entdeckungsdokument `S256`?** Öffnen Sie `<issuer>/.well-known/openid-configuration` und suchen Sie nach `S256` in `code_challenge_methods_supported`.
    - Ja: PKCE wird automatisch verwendet. Fahren Sie mit Frage 3 fort.
    - Nein oder das Feld fehlt: PKCE wird **nicht** verwendet. Setzen Sie `OIDC_PKCE` auf `True`, wenn Ihr Anbieter es erfordert. Überprüfen Sie auch das Serverprotokoll auf `Could not check the provider for PKCE support`, was bedeutet, dass das Entdeckungsdokument nicht abgerufen werden konnte und PKCE daher deaktiviert wurde.
3. **Wurde PKCE wirklich gesendet?** Starten Sie eine Anmeldung und sehen Sie sich die Adresse der Anmeldeseite des Anbieters (oder die erste Weiterleitung im Netzwerk-Tab Ihres Browsers) an. Sie sollte `code_challenge=` und `code_challenge_method=S256` enthalten.
    - Vorhanden, aber die Anmeldung schlägt beim Callback immer noch fehl: Der Anbieter hat den Codeverifier abgelehnt. Das Sitzungscookie könnte zwischen der Weiterleitung und dem Callback verloren gegangen sein (siehe Zweig 3 oben), oder der Anbieter unterstützt `S256` nicht, in diesem Fall setzen Sie `OIDC_PKCE` auf `False`, wenn der Anbieter PKCE nicht erfordert.
    - Abwesend: Die obigen Einstellungen wurden nicht angewendet. Überprüfen Sie, dass die Umgebungsvariable das richtige Präfix und einen Kleinbuchstabenwert hat (zum Beispiel `GRAMPSWEB_OIDC_PKCE=true` in Docker; `True` wird nicht als Boolean gelesen), starten Sie den Server neu und sehen Sie sich die Konfiguration erneut an.

!!! note
    Mit PKCE, das beim Anbieter als *optional* aktiviert ist oder gar nicht aktiviert ist, funktionieren Anmeldungen, unabhängig davon, ob Gramps Web eine Herausforderung sendet oder nicht. Nur Anbieter (oder Clients), die so konfiguriert sind, dass sie PKCE *erfordern*, machen diese Einstellung wichtig.

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
OIDC_ROLE_CLAIM="groups"  # oder "roles", je nach Anbieter
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

### Pocket ID

Erstellen Sie einen OIDC-Client in Pocket ID mit der Weiterleitungs-URI `<BASE_URL>/api/oidc/callback/custom` (siehe [Erforderliche Weiterleitungs-URIs](#required-redirect-uris)). Wenn Sie "PKCE erforderlich" für den Client aktivieren, sind keine zusätzlichen Gramps Web-Konfigurationen erforderlich, da Pocket ID die PKCE-Unterstützung in seinem Entdeckungsdokument bewirbt. Konfigurieren Sie dann:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Ein von der Community erstellter OIDC-Setup-Leitfaden für Gramps Web ist auf der [offiziellen Authelia-Dokumentationswebsite](https://www.authelia.com/integration/openid-connect/clients/gramps/) verfügbar.

### Keycloak

Der Großteil der Konfiguration für Keycloak kann auf den Standardeinstellungen belassen werden (*Client → Client erstellen → Client-Authentifizierung EIN*). Es gibt einige Ausnahmen:

1. **OpenID-Scopes** – Der `openid`-Scope ist in allen Keycloak-Versionen standardmäßig nicht enthalten. Um Probleme zu vermeiden, fügen Sie ihn manuell hinzu: *Client → [Gramps-Client] → Client-Scopes → Scope hinzufügen → Name: `openid` → Als Standard festlegen.*
2. **Rollen** – Rollen können entweder auf Client-Ebene oder global pro Realm zugewiesen werden.

    * Wenn Sie Client-Rollen verwenden, setzen Sie die Konfigurationsoption `OIDC_ROLE_CLAIM` auf: `resource_access.[gramps-client-name].roles`
    * Um Rollen für Gramps sichtbar zu machen, navigieren Sie zu *Client-Scopes* (der oberste Abschnitt, nicht unter dem spezifischen Client), dann: *Rollen → Mapper → Client-Rollen → Zu Userinfo hinzufügen → EIN.*
