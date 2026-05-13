# Benutzereinstellungen

Die Benutzereinstellungen sind über das Benutzersymbol in der oberen App-Leiste zugänglich, dann **Benutzereinstellungen**. Änderungen treten sofort in Kraft, sofern nicht anders angegeben.

## Benutzerinformationen

Zeigt Ihren **Benutzernamen** und die aktuelle **Benutzerrolle** (z. B. Gast, Mitglied, Redakteur). Diese sind schreibgeschützt.

## Sprache

Wählen Sie die Sprache für die Gramps Web-Oberfläche. Die Spracheinstellung wird im lokalen Speicher des Browsers gespeichert und gilt nur für das aktuelle Gerät.

## Design

Wählen Sie zwischen:

- **System** – folgt der Licht-/Dunkel-Präferenz des Betriebssystems (Standard)
- **Hell** – immer das helle Design verwenden
- **Dunkel** – immer das dunkle Design verwenden

Die Design-Einstellung wird im lokalen Speicher des Browsers gespeichert.

## E-Mail ändern

Geben Sie eine neue E-Mail-Adresse ein und klicken Sie auf **Absenden**, um die mit Ihrem Konto verknüpfte Adresse zu aktualisieren. Die E-Mail-Adresse wird für Passwortzurücksetzungen und (falls konfiguriert) Benachrichtigungen verwendet.

## Passwort ändern

Geben Sie Ihr aktuelles Passwort und ein neues Passwort ein und klicken Sie dann auf **Absenden**. Wenn Sie Ihr aktuelles Passwort vergessen haben, verwenden Sie stattdessen den Link **Passwort vergessen** auf der Anmeldeseite.

## Familienbaum-Einstellungen

### Standardansicht des Familienbaums

Legt fest, welcher Diagrammtyp standardmäßig geöffnet wird, wenn Sie zur [Familienbaum](tree.md) Seite navigieren. Optionen sind Ahnenbaum, Nachkommenbaum, Sanduhr-Diagramm, Beziehungsdiagramm und Fächerdiagramm.

Diese Einstellung wird im lokalen Speicher des Browsers gespeichert.

## Entwicklertools

### API-Token

Kopiert Ihr aktuelles Sitzungstoken in die Zwischenablage. Das Token kann verwendet werden, um sich direkt gegen die REST-API zu authentifizieren, zum Beispiel in der interaktiven Swagger UI, die von Ihrer Gramps Web-Instanz unter `/api/swagger-ui` bereitgestellt wird.

Klicken Sie auf **Swagger starten**, um die Swagger UI in einem neuen Tab zu öffnen, wobei Ihre Sitzung bereits verfügbar ist.

!!! Hinweis
    Das Sitzungstoken ist kurzlebig. Kopieren Sie es sofort, bevor Sie es in Swagger verwenden, da es ablaufen kann.
