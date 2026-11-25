# OIDC-Authentifizierung

Gramps Web unterstützt die OpenID-Connect-(OIDC-)Authentifizierung und ermöglicht es Benutzern, sich über externe Identitätsanbieter anzumelden. Dazu gehören die integrierten Anbieter Google und Microsoft sowie benutzerdefinierte OIDC-Anbieter wie Keycloak, Authentik und Authelia.

!!! warning "GitHub wird nicht mehr als OIDC-Anbieter unterstützt"
    Falls du aus einer früheren Version noch `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` gesetzt hast, entferne diese Einstellungen – sie werden jetzt ignoriert, und Benutzer, die sich zuvor über GitHub angemeldet haben, können sich auf diesem Weg nicht mehr anmelden. GitHub ist ein OAuth-2.0-Anbieter, kein OpenID-Connect-Anbieter, und hat den Claim, auf den Gramps Web zur Identifizierung angewiesen ist, nie zurückgegeben. Daher war diese Integration nie vollständig zuverlässig.

## Übersicht

Die OIDC-Authentifizierung ermöglicht dir:

- Externe Identitätsanbieter zur Benutzerauthentifizierung zu verwenden
- Mehrere Authentifizierungsanbieter gleichzeitig zu unterstützen
- OIDC-Gruppen/Rollen den Gramps-Web-Benutzerrollen zuzuordnen
- Single Sign-On (SSO) und Single Sign-Out zu implementieren
- Optional die lokale Authentifizierung mit Benutzername/Passwort zu deaktivieren

## Konfiguration

Um die OIDC-Authentifizierung zu aktivieren, musst du die entsprechenden Einstellungen in deiner Gramps-Web-Konfigurationsdatei oder als Umgebungsvariablen konfigurieren. Eine vollständige Liste der verfügbaren OIDC-Einstellungen findest du auf der Seite [Serverkonfiguration](configuration.md#settings-for-oidc-authentication).

!!! info
    Bei der Verwendung von Umgebungsvariablen musst du jedem Einstellungsnamen das Präfix `GRAMPSWEB_` voranstellen (z. B. `GRAMPSWEB_OIDC_ENABLED`). Einzelheiten findest du unter [Konfigurationsdatei im Vergleich zu Umgebungsvariablen](configuration.md#configuration-file-vs-environment-variables).

### Integrierte Anbieter

Gramps Web bietet integrierte Unterstützung für beliebte Identitätsanbieter. Um sie zu verwenden, musst du lediglich die Client-ID und das Client-Geheimnis angeben:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` und `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` und `OIDC_MICROSOFT_CLIENT_SECRET`

Du kannst mehrere Anbieter gleichzeitig konfigurieren. Das System erkennt automatisch anhand der Konfigurationswerte, welche Anbieter verfügbar sind.

!!! tip "Microsoft: Bereitstellungen mit einem Mandanten"
    Der integrierte Microsoft-Anbieter verwendet den mandantenübergreifenden Endpunkt `/common` und akzeptiert absichtlich Anmeldungen von jedem Microsoft-Konto. Wenn du nur Benutzer aus deinem eigenen Mandanten zulassen möchtest, verwende stattdessen den [benutzerdefinierten OIDC-Anbieter](#custom-oidc-providers) mit der mandantenspezifischen Issuer-URL. Dadurch bleibt die Issuer-Validierung aktiv und Anmeldungen werden auf diesen Mandanten beschränkt.

### Benutzerdefinierte OIDC-Anbieter

Für benutzerdefinierte OIDC-Anbieter (wie Keycloak, Authentik, Authelia oder einen Microsoft-Entra-Mandanten mit einem Mandanten) verwende diese Einstellungen:

Key | Beschreibung
----|-------------
`OIDC_ENABLED` | Boolean, ob die OIDC-Authentifizierung aktiviert werden soll. Auf `True` setzen.
`OIDC_ISSUER` | Die Issuer-URL deines Anbieters. Die Discovery-Informationen werden von `<issuer>/.well-known/openid-configuration` abgerufen.
`OIDC_CLIENT_ID` | Client-ID deines OIDC-Anbieters
`OIDC_CLIENT_SECRET` | Client-Geheimnis deines OIDC-Anbieters
`OIDC_NAME` | Benutzerdefinierter Anzeigename (optional, Standard ist „OIDC“)
`OIDC_SCOPES` | OAuth-Scopes (optional, Standard ist „openid email profile“)
`OIDC_USERNAME_CLAIM` | Claim, der zur Erzeugung des Benutzernamens verwendet wird (optional, Standard ist „preferred_username“)
`OIDC_PKCE` | Ob PKCE verwendet werden soll, siehe [PKCE](#pkce) (optional, wird automatisch aktiviert, wenn der Anbieter dies unterstützt)

### PKCE

Seit Gramps Web API 3.23 unterstützt Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, Methode `S256`) für den Authorization-Code-Flow. Einige Identitätsanbieter, beispielsweise Pocket ID, können so konfiguriert werden, dass sie PKCE für einen Client *verlangen* und Anmeldungen ohne PKCE ablehnen. Ältere Versionen der Gramps Web API verwenden PKCE nie, weshalb Anmeldungen mit einem solchen Client fehlschlagen.

Ob PKCE verwendet wird, wird bei der Anmeldung folgendermaßen entschieden:

- Wenn `OIDC_PKCE` auf `True` gesetzt ist, wird PKCE verwendet.
- Wenn `OIDC_PKCE` auf `False` gesetzt ist, wird PKCE nicht verwendet, selbst wenn der Anbieter dies unterstützt.
- Wenn `OIDC_PKCE` nicht gesetzt oder leer gesetzt ist, wird PKCE verwendet, wenn das Discovery-Dokument des Anbieters (`/.well-known/openid-configuration`) `S256` in `code_challenge_methods_supported` aufführt, andernfalls nicht.

Für die meisten Konfigurationen musst du nichts festlegen. Setze `OIDC_PKCE` auf `True`, wenn dein Anbieter PKCE verlangt, aber `S256` in seinem Discovery-Dokument nicht ankündigt, und auf `False`, wenn dein Anbieter `S256` ankündigt, es aber fehlerhaft verarbeitet. Als Umgebungsvariablen müssen boolesche Werte kleingeschrieben werden (`GRAMPSWEB_OIDC_PKCE=true`); siehe [Konfiguration](configuration.md).

Für die integrierten Anbieter lauten die entsprechenden Optionen `OIDC_GOOGLE_PKCE` und `OIDC_MICROSOFT_PKCE`.

Der PKCE-Codeprüfer wird während der Weiterleitung zum Anbieter und dem Callback in der Sitzung des Benutzers gespeichert. Daher ist keine Änderung an den Weiterleitungs-URIs erforderlich.

### Konfigurationen mit mehreren Stammverzeichnissen

Auf einem Server mit mehreren Stammverzeichnissen wird ein Benutzer, der sich mit einer Identität anmeldet, die bereits mit einem Gramps-Web-Konto verknüpft ist, beim Stammverzeichnis dieses Kontos angemeldet. Für diesen Benutzer funktioniert daher die einfache Anmeldeseite.

Um ein *neues* Konto mit einer OIDC-Identität zu erstellen, muss Gramps Web wissen, zu welchem Stammverzeichnis es gehören soll. Neue Benutzer müssen daher über den Registrierungslink des Stammverzeichnisses (`/register/<tree_id>`, siehe [Registrierungslink](../administration/users.md#registration-link-multi-tree-setup-only)) oder über die Anmeldeseite des Stammverzeichnisses (`/login/<tree_id>`) beginnen. Beide bieten die konfigurierten Anbieter an. Die Anmeldung mit einer unbekannten Identität über die einfache Anmeldeseite wird mit einer Meldung abgelehnt, die auf den Registrierungslink verweist. Dies erfordert Gramps Web API 3.25.3 und Gramps Web 26.11.2 oder neuer.

Im Hintergrund beginnt die Anmeldung mit:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

Dabei ist `tree` optional, außer wenn ein neues Konto erstellt wird. Die Übergabe der ID eines nicht vorhandenen Stammverzeichnisses führt zu einem fehlgeschlagenen Anmeldeversuch. Auf einem Server mit nur einem Stammverzeichnis ist `tree` optional; falls angegeben, muss es mit dem konfigurierten `TREE` übereinstimmen.

Eine OIDC-Identität ist genau an ein Gramps-Web-Konto gebunden, das wiederum genau zu einem Stammverzeichnis gehört. Eine Anmeldung bei einem anderen Stammverzeichnis schlägt daher fehl, anstatt das Konto zu verschieben. Es gibt keine Möglichkeit, eine einzelne Identität beim Anbieter mit Konten in mehreren Stammverzeichnissen zu verknüpfen. Benutzer, die Zugriff auf mehrere Stammverzeichnisse benötigen, brauchen beim Anbieter separate Identitäten (z. B. unterschiedliche Benutzernamen oder Konten).

!!! warning
    Ein Administratorkonto der Website ohne zugeordnetes Stammverzeichnis (siehe [Administratorkonto erstellen](../administration/owner.md)) kann nicht über OIDC erstellt werden, da ein durch eine OIDC-Anmeldung erstelltes Konto immer zu einem Stammverzeichnis gehört. Erstelle solche Konten mit einem lokalen Benutzernamen und Passwort.

### Native Apps

Native Apps, beispielsweise mobile Apps für Gramps Web, können dem Benutzer ermöglichen, sich im Systembrowser anzumelden und das Ergebnis über einen `https`-Link der App zu empfangen. Seit Gramps Web API 3.26 funktioniert dies, wenn der Link in `OIDC_ALLOWED_REDIRECT_URIS` aufgeführt ist, z. B.

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

Die Dokumentation der App teilt dir mit, welchen Link du hinzufügen musst. Die beim Identitätsanbieter registrierten Weiterleitungs-URIs bleiben unverändert.

## Erforderliche Weiterleitungs-URIs

Bei der Konfiguration deines OIDC-Anbieters musst du die folgende Weiterleitungs-URI registrieren:

**Für OIDC-Anbieter, die Wildcards unterstützen: (z. B. Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Dabei ist `*` eine reguläre Wildcard. Je nach Regex-Interpreter deines Anbieters kann dies auch `.*` oder ähnlich sein. Stelle sicher, dass Regex aktiviert ist, wenn dein Anbieter dies verlangt (z. B. Authentik).

**Für OIDC-Anbieter, die keine Wildcards unterstützen: (z. B. Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Das Stammverzeichnis ist nie Bestandteil der Weiterleitungs-URI, auch nicht auf Servern mit mehreren Stammverzeichnissen. Es wird separat in der Sitzung übertragen, da Anbieter verlangen, dass die Weiterleitungs-URI exakt mit der registrierten URI übereinstimmt.

## Rollenzuordnung

Gramps Web kann OIDC-Gruppen oder -Rollen deines Identitätsanbieters automatisch den Gramps-Web-Benutzerrollen zuordnen. Dadurch kannst du Benutzerberechtigungen zentral in deinem Identitätsanbieter verwalten. Die Rollenzuordnung funktioniert für alle Anbieter gleich, unabhängig davon, ob sie integriert oder benutzerdefiniert sind.

### Konfiguration

Verwende diese Einstellungen, um die Rollenzuordnung zu konfigurieren:

Key | Beschreibung
----|-------------
`OIDC_ROLE_CLAIM` | Der Claim-Name im OIDC-Token, der die Gruppen/Rollen des Benutzers enthält. Standard ist „groups“. Punktpfade werden unterstützt, z. B. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Admin“ zugeordnet wird
`OIDC_GROUP_OWNER` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Owner“ zugeordnet wird
`OIDC_GROUP_EDITOR` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Editor“ zugeordnet wird
`OIDC_GROUP_CONTRIBUTOR` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Contributor“ zugeordnet wird
`OIDC_GROUP_MEMBER` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Member“ zugeordnet wird
`OIDC_GROUP_GUEST` | Der Gruppen-/Rollenname deines OIDC-Anbieters, der der Gramps-Rolle „Guest“ zugeordnet wird

### Verhalten der Rollenzuordnung

Wenn überhaupt keine `OIDC_GROUP_*`-Einstellung konfiguriert ist, ist die Rollenzuordnung deaktiviert und die Rollen werden manuell in Gramps Web verwaltet. Neue OIDC-Konten werden dann deaktiviert erstellt und müssen von einem bereits vorhandenen Besitzer oder Administrator genehmigt werden (siehe [Erste Anmeldung und erstmalige Einrichtung](#first-login-and-bootstrapping) weiter unten).

Sobald die Rollenzuordnung konfiguriert ist, geschieht bei jeder Anmeldung Folgendes:

- Wenn der Rollen-Claim vorhanden ist und der Benutzer zu einer zugeordneten Gruppe gehört, erhält er die entsprechende Rolle.
- Wenn der Rollen-Claim vorhanden ist, der Benutzer aber keiner zugeordneten Gruppe angehört, wird seine Rolle auf deaktiviert gesetzt. Dies ist ein ausfallsicherer Standardwert und kein Fehler – Gramps Web kann für eine unbekannte Gruppe keine Rolle ableiten.
- Wenn der Rollen-Claim vollständig im Token fehlt, bleibt die bestehende Rolle unverändert; ein neues Konto wird weiterhin standardmäßig deaktiviert.

!!! warning "Google sendet keinen groups-Claim"
    Die Tokens von Google enthalten niemals einen `groups`-Claim. Bei aktivierter Rollenzuordnung fallen Google-Anmeldungen daher unter „Claim fehlt“: Bestehende Benutzer behalten ihre Rolle, neue Google-Benutzer werden jedoch deaktiviert erstellt und benötigen eine manuelle Genehmigung. Beachte dies, bevor du die Rollenzuordnung nur für einen anderen Anbieter aktivierst – dadurch werden bestehende Google-Benutzer nicht automatisch deaktiviert.

Microsoft Entra gibt App-Rollen und Gruppenmitgliedschaften nur im ID-Token und nicht über den Userinfo-Endpunkt zurück. Gramps Web führt die Claims des ID-Tokens mit der Userinfo-Antwort zusammen, sodass `OIDC_ROLE_CLAIM` wie bei anderen Anbietern funktioniert. Wenn beide einen Claim enthalten, hat der Userinfo-Wert Vorrang.

## Erste Anmeldung und erstmalige Einrichtung

Neue über OIDC erstellte Konten sind zunächst deaktiviert, sofern ihnen die Rollenzuordnung keine Rolle zuweist (siehe oben). Auf einer vollständig neuen Instanz kann niemand ein deaktiviertes Konto genehmigen. Wenn außerdem `OIDC_DISABLE_LOCAL_AUTH` aktiviert ist, gibt es auch keine Anmeldung per Passwort als Ausweichmöglichkeit.

!!! warning "Vor der ersten Anmeldung eine Besitzer-/Administratorgruppe konfigurieren"
    Bevor sich jemand zum ersten Mal über OIDC anmeldet, setze `OIDC_GROUP_OWNER` (oder `OIDC_GROUP_ADMIN`) und stelle sicher, dass der erste Benutzer beim Anbieter zu dieser Gruppe gehört. Andernfalls kann die Instanz über OIDC überhaupt nicht erstmalig eingerichtet werden.

## Konten und Benutzernamen

Über OIDC erstellte Konten erhalten einen generierten Benutzernamen. Dieser wird bei der Kontoerstellung einmalig vergeben und bei späteren Anmeldungen nie geändert:

- Integrierte Anbieter: `<provider>_<claim value>`, z. B. `microsoft_alice@contoso.com`
- Benutzerdefinierter Anbieter: der reine Claim-Wert, z. B. `alice`

Bei einer Kollision wird ein numerisches Suffix angehängt. Es gibt keine Möglichkeit, den Benutzernamen eines über OIDC erstellten Kontos nachträglich umzubenennen. Der vollständige Name und die E-Mail-Adresse werden dagegen bei jeder Anmeldung aktualisiert.

Eine OIDC-Anmeldung verknüpft sich niemals mit einem bestehenden lokalen Konto, das zufällig dieselbe E-Mail-Adresse verwendet. Dies ist beabsichtigt, da die Verknüpfung von Konten per E-Mail-Adresse einen Angriffsvektor zur Kontoübernahme darstellt. Ein Benutzer mit einem bereits vorhandenen lokalen Konto erhält bei der ersten OIDC-Anmeldung ein zweites, separates Konto, sofern er den Anbieter nicht zuvor mit seinem Konto verknüpft.

Seit Gramps Web API 3.24 können Benutzer OIDC-Identitäten unter [Benutzereinstellungen > Verknüpfte Anmeldemethoden](../user-guide/settings.md#linked-sign-in-methods) mit ihrem bestehenden Konto verknüpfen sowie diese auflisten und die Verknüpfung aufheben. Die Verknüpfung erfordert eine aktuelle Anmeldung und wird mit dem eigenen Token des Benutzers bestätigt. Daher funktioniert sie auch, wenn sich das Frontend auf einer anderen Origin als die API befindet. Eine Identität kann nur zu einem Konto gehören. Um eine Identität zu verknüpfen, die bereits ein eigenes Konto besitzt, muss ein Administrator dieses Konto zuerst löschen (seine Bearbeitungen bleiben erhalten, aber in der Versionshistorie wird sein Name nicht mehr angezeigt). Die letzte verknüpfte Identität kann nur mit dem aktuellen Passwort des Kontos entfernt werden und überhaupt nicht, wenn `OIDC_DISABLE_LOCAL_AUTH` gesetzt ist.

E-Mail-Adressen des Anbieters werden nur gespeichert, wenn der Anbieter sie als bestätigt kennzeichnet (oder den Claim `email_verified` vollständig weglässt). Andernfalls wird die Anmeldung ohne Speicherung einer E-Mail-Adresse fortgesetzt. Da E-Mail-Adressen seit Gramps Web API 3.22 nicht eindeutig sein müssen, wird eine Adresse auch dann gespeichert, wenn ein anderes Konto sie bereits verwendet.

## OIDC-Abmeldung

Gramps Web unterstützt Single Sign-Out (SSO-Abmeldung) für OIDC-Anbieter. `GET /api/oidc/logout/` sucht den `end_session_endpoint` des Anbieters und gibt ihn als `logout_url` in der Antwort zurück. Das Gramps-Web-Frontend navigiert den Browser dorthin, um die Sitzung beim Identitätsanbieter tatsächlich zu beenden. `logout_url` ist `null`, wenn der Anbieter keinen `end_session_endpoint` besitzt.

!!! warning "Tokens werden bei der Abmeldung nicht widerrufen"
    Die Abmeldung beendet nur die Browsersitzung. Derzeit gibt es keine Möglichkeit, ein bereits ausgegebenes Gramps-Web-Token zu widerrufen. Tokens bleiben bis zu ihrem Ablauf gültig (`JWT_ACCESS_TOKEN_EXPIRES`, standardmäßig 15 Minuten für Zugriffstokens), unabhängig davon, ob sich der Benutzer inzwischen bei Gramps Web oder beim Identitätsanbieter abgemeldet hat.

## Fehlerbehebung

Beginne an der Stelle, an der die Anmeldung stoppt, und folge dem entsprechenden Zweig. Gramps Web protokolliert den Grund für einen fehlgeschlagenen Callback (suche im Serverprotokoll nach `OIDC callback error for provider`). Dieser Grund ist normalerweise genauer als die im Browser angezeigte Meldung.

**1. Fehlt die Anmeldeschaltfläche?**

- Prüfe `<BASE_URL>/api/oidc/config/`. Wenn `enabled` den Wert `false` hat oder `providers` leer ist, ist OIDC nicht konfiguriert: `OIDC_ENABLED` muss `True` sein, und ein benutzerdefinierter Anbieter benötigt sowohl `OIDC_ISSUER` als auch `OIDC_CLIENT_ID`.
- Ein integrierter Anbieter (Google, Microsoft) wird nur registriert, wenn sowohl seine Client-ID als auch sein Client-Geheimnis gesetzt sind.
- Suche beim Start im Serverprotokoll nach `Could not load discovery document`. Dies bedeutet, dass der Server `<issuer>/.well-known/openid-configuration` (oder `OIDC_OPENID_CONFIG_URL`) nicht erreichen konnte. Beim ersten Einsatz wird ein erneuter Versuch unternommen. Der Gramps-Web-Container muss die Issuer-URL jedoch selbst auflösen und erreichen können, nicht nur dein Browser.

**2. Erhält der Browser direkt nach der Weiterleitung zum Anbieter einen Fehler?**

Der Fehler wird vom Identitätsanbieter angezeigt, bevor du dich anmeldest.

- *„redirect URI mismatch“* (oder ähnlich): Die beim Anbieter registrierte Weiterleitungs-URI muss exakt übereinstimmen, einschließlich Schema, Host, Port und Anbieter-ID. Siehe [Erforderliche Weiterleitungs-URIs](#required-redirect-uris). Beachte, dass sie aus `BASE_URL` gebildet wird. Ein falsches `BASE_URL` führt daher zu einer falschen Weiterleitungs-URI.
- *Ein PKCE-Fehler* (zum Beispiel `invalid_request`, „code challenge required“ oder ein fehlender `code_challenge`-Parameter): Der Anbieter verlangt PKCE, aber Gramps Web hat es nicht gesendet. Wechsle zum [PKCE-Zweig](#pkce-branch) weiter unten.

**3. Akzeptiert der Anbieter die Anmeldung, zeigt Gramps Web anschließend aber einen Fehler?**

- *`mismatching_state` oder ein Fehler, der die Sitzung oder den Status erwähnt*: Der Browser hat das Sitzungscookie nicht zurückgesendet, das Gramps Web beim Start der Anmeldung gesetzt hat. Dieses Cookie enthält auch den PKCE-Codeprüfer. Stelle sicher, dass die Adresse im Browser mit `BASE_URL` übereinstimmt (gleiches Schema und gleicher Host), dass ein Reverse-Proxy Cookies und den ursprünglichen Host weitergibt und dass die Anmeldung im selben Browser-Tab oder -Fenster begonnen und abgeschlossen wird.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: Prüfe das Serverprotokoll auf den zugrunde liegenden Grund. Häufige Ursachen sind ein falsches Client-Geheimnis, eine Issuer-URL, die nicht mit dem `iss`-Claim der Tokens übereinstimmt, sowie ein Fehler des Anbieters beim Callback (z. B. PKCE, siehe unten).
- *Zu viele Versuche*: Die Anmelde- und Callback-Endpunkte sind auf 5 Anfragen pro Minute begrenzt. Warte eine Minute und versuche es erneut.

**4. Ist die Anmeldung erfolgreich, siehst du aber „Account Under Review“ oder kannst nichts tun?**

Neue Konten werden deaktiviert erstellt, sofern die Rollenzuordnung ihnen keine Rolle zuweist. Siehe [Erste Anmeldung und erstmalige Einrichtung](#first-login-and-bootstrapping) und [Verhalten der Rollenzuordnung](#role-mapping-behavior). Ein Administrator kann das Konto außerdem unter Einstellungen > Administration > Benutzer verwalten aktivieren.

### PKCE-Zweig

Gramps Web entscheidet beim Start einer Anmeldung, ob PKCE verwendet wird (siehe [PKCE](#pkce)). Um herauszufinden, was in deiner Konfiguration geschehen ist, arbeite diese Fragen in der angegebenen Reihenfolge durch:

1. **Ist `OIDC_PKCE` gesetzt?** (Bei integrierten Anbietern `OIDC_GOOGLE_PKCE` oder `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE wird verwendet. Fahre mit Frage 3 fort.
    - `False`: PKCE ist absichtlich deaktiviert und das Discovery-Dokument des Anbieters wird ignoriert. Wenn dein Anbieter PKCE verlangt, entferne die Einstellung oder setze sie auf `True`.
    - Nicht gesetzt oder leer: Fahre mit Frage 2 fort.
2. **Führt das Discovery-Dokument `S256` auf?** Öffne `<issuer>/.well-known/openid-configuration` und suche in `code_challenge_methods_supported` nach `S256`.
    - Ja: PKCE wird automatisch verwendet. Fahre mit Frage 3 fort.
    - Nein oder Feld fehlt: PKCE wird **nicht** verwendet. Setze `OIDC_PKCE` auf `True`, wenn dein Anbieter PKCE verlangt. Prüfe außerdem das Serverprotokoll auf `Could not check the provider for PKCE support`. Dies bedeutet, dass das Discovery-Dokument nicht abgerufen werden konnte und PKCE deshalb deaktiviert blieb.
3. **Wurde PKCE tatsächlich gesendet?** Starte eine Anmeldung und prüfe die Adresse der Anmeldeseite des Anbieters (oder die erste Weiterleitung im Netzwerk-Tab deines Browsers). Sie sollte `code_challenge=` und `code_challenge_method=S256` enthalten.
    - Vorhanden, die Anmeldung schlägt beim Callback aber weiterhin fehl: Der Anbieter hat den Codeprüfer abgelehnt. Das Sitzungscookie könnte zwischen Weiterleitung und Callback verloren gegangen sein (siehe Zweig 3 oben), oder der Anbieter unterstützt `S256` nicht. Setze in diesem Fall `OIDC_PKCE` auf `False`, sofern der Anbieter PKCE nicht verlangt.
    - Nicht vorhanden: Die obigen Einstellungen wurden nicht übernommen. Prüfe, ob die Umgebungsvariable das richtige Präfix und einen kleingeschriebenen Wert besitzt (z. B. `GRAMPSWEB_OIDC_PKCE=true` in Docker; `True` wird nicht als boolescher Wert eingelesen), starte den Server neu und prüfe die Konfiguration erneut.

!!! note
    Wenn PKCE beim Anbieter *optional* aktiviert oder überhaupt nicht aktiviert ist, funktionieren Anmeldungen unabhängig davon, ob Gramps Web eine Challenge sendet. Nur Anbieter (oder Clients), die PKCE als *erforderlich* konfigurieren, machen diese Einstellung relevant.

## Beispielkonfigurationen

### Benutzerdefinierter OIDC-Anbieter (Keycloak)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # dein geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Benutzerdefinierte OIDC-Konfiguration
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Optional: automatisch zur SSO-Anmeldung weiterleiten
OIDC_DISABLE_LOCAL_AUTH=True  # Optional: Anmeldung mit Benutzername/Passwort deaktivieren

# Optional: Rollenzuordnung von OIDC-Gruppen zu Gramps-Rollen
OIDC_ROLE_CLAIM="groups"  # oder "roles", abhängig von deinem Anbieter
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Implizites SSL für Port 465 verwenden
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # dein SMTP-Passwort
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Integrierter Anbieter (Google)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # dein geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Mehrere Anbieter

Du kannst mehrere OIDC-Anbieter gleichzeitig aktivieren:

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # dein geheimer Schlüssel
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Benutzerdefinierter Anbieter
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Company SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

Erstelle in Pocket ID einen OIDC-Client mit der Weiterleitungs-URI `<BASE_URL>/api/oidc/callback/custom` (siehe [Erforderliche Weiterleitungs-URIs](#required-redirect-uris)). Wenn du für den Client „Require PKCE“ aktivierst, ist keine zusätzliche Gramps-Web-Konfiguration erforderlich, da Pocket ID die PKCE-Unterstützung in seinem Discovery-Dokument ankündigt. Konfiguriere anschließend:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Eine von der Community erstellte Anleitung zur OIDC-Einrichtung von Gramps Web ist auf der [offiziellen Authelia-Dokumentationswebsite](https://www.authelia.com/integration/openid-connect/clients/gramps/) verfügbar.

### Keycloak

Der größte Teil der Keycloak-Konfiguration kann auf den Standardwerten belassen werden (*Client → Create client → Client authentication ON*). Es gibt einige Ausnahmen:

1. **OpenID-Scope** – Der Scope `openid` ist standardmäßig nicht in allen Keycloak-Versionen enthalten. Um Probleme zu vermeiden, füge ihn manuell hinzu: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Rollen** – Rollen können entweder auf Clientebene oder global pro Realm zugewiesen werden.

    * Wenn du Client-Rollen verwendest, setze die Konfigurationsoption `OIDC_ROLE_CLAIM` auf: `resource_access.[gramps-client-name].roles`
    * Damit Rollen für Gramps sichtbar werden, navigiere zu *Client Scopes* (dem Abschnitt der obersten Ebene, nicht innerhalb des jeweiligen Clients) und anschließend zu: *Roles → Mappers → client roles → Add to userinfo → ON.*
