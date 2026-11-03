# Benutzereinstellungen

Benutzereinstellungen sind über das Benutzersymbol in der oberen App-Leiste zugänglich, dann **Benutzereinstellungen**. Die Seite ist in zusammenklappbare Abschnitte organisiert. Änderungen treten sofort in Kraft, sofern nicht anders angegeben.

!!! Hinweis
    Änderungen in den Benutzereinstellungen betreffen nur Ihr eigenes Konto. Einstellungen, die alle Benutzer des Baums betreffen, werden in den [Verwaltungseinstellungen](../administration/settings.md) verwaltet.

## Konto

Beinhaltet Ihre Profilinformationen, Anmeldeinformationen und Kontosicherheit.

### Benutzerinformationen

Zeigt Ihren **Benutzernamen** und Ihre aktuelle **Benutzerrolle** (z. B. Gast, Mitglied, Redakteur). Diese sind schreibgeschützt.

### E-Mail ändern

Geben Sie eine neue E-Mail-Adresse ein und klicken Sie auf **Absenden**, um die mit Ihrem Konto verknüpfte Adresse zu aktualisieren. Die E-Mail-Adresse wird für Passwortzurücksetzungen und (wenn konfiguriert) Benachrichtigungen verwendet.

### Passwort ändern

Geben Sie Ihr aktuelles Passwort und ein neues Passwort ein und klicken Sie dann auf **Absenden**. Sie bleiben auf dem aktuellen Gerät angemeldet, während Ihre Sitzungen auf anderen Geräten und Browsern innerhalb von 15 Minuten enden. Wenn Sie Ihr aktuelles Passwort vergessen haben, verwenden Sie stattdessen den Link **Passwort vergessen** auf der Anmeldeseite.

Dieser Abschnitt ist verborgen, wenn der Server nur die Anmeldung über einen externen Anbieter zulässt (siehe [OIDC-Authentifizierung](../install_setup/oidc.md)).

### Verknüpfte Anmeldemethoden

Wenn Ihr Server eine Single Sign-On-Funktion anbietet (siehe [OIDC-Authentifizierung](../install_setup/oidc.md)), können Sie ein Konto von einem Anbieter, wie Google oder dem Login Ihrer Organisation, mit Ihrem Gramps Web-Konto verknüpfen. Sie können sich dann mit diesem Anbieter anmelden und gelangen in Ihr bestehendes Konto, mit Ihrer Rolle und Ihren Änderungen. Dieser Abschnitt erscheint nur, wenn Single Sign-On aktiviert ist und der Server das Verknüpfen unterstützt (Gramps Web API 3.24 und höher).

Um ein Konto zu verknüpfen, klicken Sie auf **Verknüpfen mit** und dem Namen des Anbieters, melden Sie sich beim Anbieter an, und Sie werden zurück zu Ihren Einstellungen geleitet. Wenn Sie sich in letzter Zeit nicht angemeldet haben, werden Sie zuerst aufgefordert, sich erneut anzumelden.

Ein Anbieter-Konto kann nur mit einem Gramps Web-Konto verknüpft werden. Wenn Sie "Diese Anmeldung ist bereits mit einem anderen Konto verknüpft" sehen, ist es anderswo verknüpft, zum Beispiel mit einem Konto, das erstellt wurde, als Sie sich zum ersten Mal mit diesem Anbieter angemeldet haben. Ein Administrator kann dieses andere Konto löschen, nach dem Sie es mit Ihrem verknüpfen können.

Um ein Konto zu trennen, klicken Sie auf **Trennen**. Wenn es Ihre letzte verknüpfte Anmeldemethode ist, müssen Sie auch Ihr Passwort eingeben, damit Sie sich danach weiterhin anmelden können. Wenn Ihr Konto über Single Sign-On erstellt wurde und Sie nie ein Passwort festgelegt haben, verwenden Sie **Passwort vergessen** auf der Anmeldeseite, um zuerst eines festzulegen (dies erfordert, dass der Server E-Mails sendet). Wenn der Server nur die Anmeldung über einen Anbieter zulässt, kann das letzte verknüpfte Konto nicht getrennt werden.

## Erscheinungsbild

Steuert die Anzeigeeinstellungen, die auf Ihrem Gerät gespeichert sind.

### Sprache

Wählen Sie die Sprache für die Gramps Web-Oberfläche. Die Spracheinstellung wird im lokalen Speicher des Browsers gespeichert und gilt nur für das aktuelle Gerät.

### Thema

Wählen Sie zwischen:

- **System** – folgt der Licht-/Dunkel-Präferenz des Betriebssystems (Standard)
- **Hell** – immer das helle Thema verwenden
- **Dunkel** – immer das dunkle Thema verwenden

Die Themen-Einstellung wird im lokalen Speicher des Browsers gespeichert.

### Familienbaum-Einstellungen

#### Standardansicht des Familienbaums

Legt fest, welcher Diagrammtyp standardmäßig geöffnet wird, wenn Sie zur [Familienbaum](tree.md)-Seite navigieren. Optionen sind Ahnenbaum, Nachkommenbaum, Sanduhrgrafik, Beziehungsgrafik und Fandiagramm.

Diese Präferenz wird im lokalen Speicher des Browsers gespeichert.

## Entwicklertools

### API-Token

Kopiert Ihr aktuelles Sitzungstoken in die Zwischenablage. Das Token kann verwendet werden, um sich direkt gegen die REST-API zu authentifizieren, zum Beispiel in der interaktiven Swagger UI, die von Ihrer Gramps Web-Instanz unter `/api/swagger-ui` bereitgestellt wird.

Klicken Sie auf **Swagger starten**, um die Swagger UI in einem neuen Tab zu öffnen, wobei Ihre Sitzung bereits verfügbar ist.

!!! Hinweis
    Das Sitzungstoken ist kurzlebig. Kopieren Sie es sofort, bevor Sie es in Swagger verwenden, da es ablaufen kann.
