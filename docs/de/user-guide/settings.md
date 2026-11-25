# Benutzereinstellungen

Die Benutzereinstellungen sind über das Benutzersymbol in der oberen App-Leiste und anschließend über **Benutzereinstellungen** erreichbar. Die Seite ist in auf- und zuklappbare Abschnitte gegliedert. Änderungen werden sofort wirksam, sofern nicht anders angegeben.

!!! note
    Änderungen in den Benutzereinstellungen betreffen nur dein eigenes Konto. Einstellungen, die alle Benutzer des Stammbaums betreffen, werden in den [Administrationseinstellungen](../administration/settings.md) verwaltet.

## Konto

Enthält deine Profilinformationen, Zugangsdaten und Kontosicherheit.

### Benutzerinformationen

Zeigt deinen **Benutzernamen** und deine aktuelle **Benutzerrolle** (z. B. Gast, Mitglied, Bearbeiter). Diese Angaben sind schreibgeschützt.

### E-Mail-Adresse ändern

Gib eine neue E-Mail-Adresse ein und klicke auf **Absenden**, um die mit deinem Konto verknüpfte Adresse zu aktualisieren. Die E-Mail-Adresse wird zum Zurücksetzen des Passworts und (falls konfiguriert) für Benachrichtigungen verwendet.

### Passwort ändern

Gib dein aktuelles Passwort und ein neues Passwort ein und klicke anschließend auf **Absenden**. Du bleibst auf dem aktuellen Gerät angemeldet, während deine Sitzungen auf anderen Geräten und in anderen Browsern innerhalb von 15 Minuten beendet werden. Wenn du dein aktuelles Passwort vergessen hast, verwende stattdessen den Link **Passwort vergessen** auf der Anmeldeseite.

Dieser Abschnitt ist ausgeblendet, wenn der Server die Anmeldung nur über einen externen Anbieter erlaubt (siehe [OIDC-Authentifizierung](../install_setup/oidc.md)).

### Verknüpfte Anmeldemethoden

Wenn dein Server Single Sign-on anbietet (siehe [OIDC-Authentifizierung](../install_setup/oidc.md)), kannst du ein Konto bei einem Anbieter, beispielsweise Google oder dem Anmeldesystem deiner Organisation, mit deinem Gramps-Web-Konto verknüpfen. Du kannst dich dann mit diesem Anbieter anmelden und gelangst zu deinem bestehenden Konto, einschließlich deiner Rolle und deiner Änderungen. Dieser Abschnitt wird nur angezeigt, wenn Single Sign-on aktiviert ist und der Server die Verknüpfung unterstützt (Gramps Web API 3.24 und höher).

Um ein Konto zu verknüpfen, klicke auf **Verknüpfen mit** und den Namen des Anbieters, melde dich beim Anbieter an und kehre anschließend zu deinen Einstellungen zurück. Wenn du dich nicht vor Kurzem angemeldet hast, wirst du zunächst aufgefordert, dich erneut anzumelden.

Ein Anbieterkonto kann nur mit einem Gramps-Web-Konto verknüpft werden. Wenn du die Meldung „Diese Anmeldung ist bereits mit einem anderen Konto verknüpft“ siehst, ist sie bereits an anderer Stelle verknüpft, beispielsweise mit einem Konto, das bei deiner ersten Anmeldung mit diesem Anbieter erstellt wurde. Ein Administrator kann das andere Konto löschen. Danach kannst du es mit deinem Konto verknüpfen.

Um die Verknüpfung eines Kontos aufzuheben, klicke auf **Verknüpfung aufheben**. Wenn es sich um deine letzte verknüpfte Anmeldemethode handelt, musst du außerdem dein Passwort eingeben, damit du dich anschließend weiterhin anmelden kannst. Wenn dein Konto über Single Sign-on erstellt wurde und du nie ein Passwort festgelegt hast, verwende **Passwort vergessen** auf der Anmeldeseite, um zunächst eines festzulegen (dazu muss der Server E-Mails versenden können). Wenn der Server die Anmeldung nur über einen Anbieter erlaubt, kann die Verknüpfung des letzten Kontos nicht aufgehoben werden.

## Darstellung

Steuert die auf deinem Gerät gespeicherten Anzeigeeinstellungen.

### Sprache

Wähle die Sprache für die Gramps-Web-Oberfläche aus. Die Spracheinstellung wird im lokalen Speicher des Browsers gespeichert und gilt nur für das aktuelle Gerät.

### Design

Wähle zwischen:

- **System** – folgt der Hell-/Dunkel-Einstellung des Betriebssystems (Standard)
- **Hell** – verwendet immer das helle Design
- **Dunkel** – verwendet immer das dunkle Design

Die Design-Einstellung wird im lokalen Speicher des Browsers gespeichert.

### Einstellungen zum Stammbaum

#### Standardansicht des Stammbaums

Legt fest, welcher Diagrammtyp standardmäßig geöffnet wird, wenn du zur Seite [Stammbaum](tree.md) navigierst. Die Optionen sind Vorfahrenbaum, Nachkommenbaum, Sanduhrdiagramm, Beziehungsdiagramm und Fächerdiagramm.

Diese Einstellung wird im lokalen Speicher des Browsers gespeichert.

## Entwicklerwerkzeuge

### API-Token

Kopiert dein aktuelles Sitzungstoken in die Zwischenablage. Das Token kann zur direkten Authentifizierung gegenüber der REST-API verwendet werden, beispielsweise in der interaktiven Swagger-Benutzeroberfläche, die von deiner Gramps-Web-Instanz unter `/api/swagger-ui` bereitgestellt wird.

Klicke auf **Swagger starten**, um die Swagger-Benutzeroberfläche in einem neuen Tab zu öffnen, wobei deine Sitzung bereits verfügbar ist.

!!! note
    Das Sitzungstoken ist nur kurzzeitig gültig. Kopiere es unmittelbar vor der Verwendung in Swagger, da es ablaufen kann.
