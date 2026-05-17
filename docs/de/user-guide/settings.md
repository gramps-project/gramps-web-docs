# Benutzereinstellungen

Benutzereinstellungen sind über das Benutzersymbol in der oberen App-Leiste zugänglich, dann **Benutzereinstellungen**. Die Seite ist in einklappbare Abschnitte organisiert. Änderungen treten sofort in Kraft, sofern nicht anders angegeben.

!!! Hinweis
    Änderungen in den Benutzereinstellungen betreffen nur Ihr eigenes Konto. Einstellungen, die alle Benutzer des Baums betreffen, werden in den [Verwaltungseinstellungen](../administration/settings.md) verwaltet.

## Konto

Beinhaltet Ihre Profilinformationen, Anmeldeinformationen und Kontosicherheit.

### Benutzerinformationen

Zeigt Ihren **Benutzernamen** und die aktuelle **Benutzerrolle** (z. B. Gast, Mitglied, Redakteur). Diese sind schreibgeschützt.

### E-Mail ändern

Geben Sie eine neue E-Mail-Adresse ein und klicken Sie auf **Absenden**, um die mit Ihrem Konto verknüpfte Adresse zu aktualisieren. Die E-Mail-Adresse wird für Passwortzurücksetzungen und (falls konfiguriert) Benachrichtigungen verwendet.

### Passwort ändern

Geben Sie Ihr aktuelles Passwort und ein neues Passwort ein und klicken Sie dann auf **Absenden**. Wenn Sie Ihr aktuelles Passwort vergessen haben, verwenden Sie stattdessen den Link **Passwort vergessen** auf der Anmeldeseite.

## Erscheinungsbild

Steuert die Anzeigeeinstellungen, die auf Ihrem Gerät gespeichert sind.

### Sprache

Wählen Sie die Sprache für die Gramps-Weboberfläche. Die Spracheinstellung wird im lokalen Speicher des Browsers gespeichert und gilt nur für das aktuelle Gerät.

### Thema

Wählen Sie zwischen:

- **System** – folgt der Licht-/Dunkelpräferenz des Betriebssystems (Standard)
- **Hell** – immer das helle Thema verwenden
- **Dunkel** – immer das dunkle Thema verwenden

Die Themen-Einstellung wird im lokalen Speicher des Browsers gespeichert.

### Präferenzen für den Stammbaum

#### Standardansicht des Stammbaums

Legt fest, welcher Diagrammtyp standardmäßig geöffnet wird, wenn Sie zur [Stammbaum](tree.md)-Seite navigieren. Optionen sind Ahnenbaum, Nachkommenbaum, Sanduhr-Diagramm, Beziehungsgrafik und Fandiagramm.

Diese Präferenz wird im lokalen Speicher des Browsers gespeichert.

## Entwicklertools

### API-Token

Kopiert Ihr aktuelles Sitzungstoken in die Zwischenablage. Das Token kann verwendet werden, um sich direkt gegen die REST-API zu authentifizieren, beispielsweise in der interaktiven Swagger-Benutzeroberfläche, die von Ihrer Gramps-Webinstanz unter `/api/swagger-ui` bereitgestellt wird.

Klicken Sie auf **Swagger starten**, um die Swagger-Benutzeroberfläche in einem neuen Tab zu öffnen, in dem Ihre Sitzung bereits verfügbar ist.

!!! Hinweis
    Das Sitzungstoken ist kurzlebig. Kopieren Sie es sofort, bevor Sie es in Swagger verwenden, da es ablaufen kann.
