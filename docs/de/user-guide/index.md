---
hide:
  - toc
---

# Benutzerhandbuch

Dieser Abschnitt dokumentiert die für Benutzer von Gramps Web verfügbaren Funktionen.

!!! note "Werden nicht alle Funktionen angezeigt?"
    Gramps Web verwendet ein rollenbasiertes Berechtigungssystem. Einige Funktionen – wie das Bearbeiten von Daten, Verwalten von Etiketten oder Anzeigen privater Datensätze – sind nur für Benutzer mit ausreichenden Berechtigungen verfügbar. Du kannst deine aktuelle Rolle in den [Benutzereinstellungen](settings.md) überprüfen. Wenn du mehr Zugriff benötigst, wende dich an den Eigentümer deines Stammbaums oder an den Administrator. Eine Beschreibung aller Rollen findest du unter [Benutzersystem](../install_setup/users.md).

## Navigieren in der Benutzeroberfläche

### Hauptnavigation

Die Seitenleiste (oder das Hamburger-Menü auf Mobilgeräten) ist die wichtigste Möglichkeit, zwischen den Abschnitten zu wechseln:

- **Startseite** – das Dashboard (siehe unten)
- **Blog** – als Blogbeiträge verfasste Geschichten zur Familiengeschichte
- **Stammbaum** – interaktive Stammbaumdiagramme
- **Zeitleiste** – chronologische Ansicht der Ereignisse im gesamten Stammbaum (erfordert eine ausreichend aktuelle Version der Gramps-Web-API)
- **Karte** – geografische Ansicht der Orte im Stammbaum
- **DNA** – Werkzeuge zur Analyse von DNA-Übereinstimmungen
- **Listen** – alle Objekte jedes Typs durchsuchen: Personen, Familien, Ereignisse, Orte, Quellen, Zitate, Archive, Notizen
- **Medien** – alle Mediendateien durchsuchen (Fotos, Dokumente usw.)
- **Assistent** – KI-Chatassistent (falls vom Administrator aktiviert)
- **Verlauf** – kürzlich geänderte Objekte
- **Lesezeichen** – deine gespeicherten Lesezeichen
- **Aufgaben** – Forschungsaufgaben
- **Berichte** – Berichte erstellen
- **Export** – den Stammbaum exportieren
- **Revisionen** – vollständiger Transaktionsverlauf (für Mitglieder und höhere Rollen sichtbar)

!!! note
    Etiketten werden nicht mehr über die Seitenleiste verwaltet – die Verwaltung von Etiketten wurde in die [Administrationseinstellungen](../administration/settings.md#tags) verschoben (nur für Eigentümer/Administratoren). Unter [Etiketten](tags.md) erfährst du, wie Etiketten verwendet werden.

### Obere App-Leiste

Die Leiste am oberen Rand jeder Seite enthält:

- **Hinzufügen** (Plus-Symbol, für Mitwirkende und höhere Rollen sichtbar) – öffnet ein Menü zum Erstellen eines neuen Objekts: Person, Familie, Ereignis, Ort, Quelle, Zitat, Archiv, Notiz, Medienobjekt oder Aufgabe
- **Suchen** (Lupensymbol) – öffnet die Suchseite
- **Glocke** – öffnet die [Benachrichtigungen](notifications.md), einschließlich Änderungen durch andere Benutzer und abgeschlossener Hintergrundaufgaben
- **Benutzersymbol** – öffnet das Einstellungsmenü: Benutzereinstellungen, Administration (nur für Eigentümer), Benutzer verwalten (nur für Eigentümer), Systeminformationen

## Die Startseite (Dashboard)

Das Dashboard wird angezeigt, wenn du dich zum ersten Mal anmeldest. Es besteht aus zwei Spalten:

**Linke Spalte:**

- **Karte der Hauptperson** – zeigt den Namen, das Foto (falls vorhanden) und wichtige Fakten der von dir ausgewählten Hauptperson, mit einem Link zu ihrem vollständigen Profil und einer Schnellnavigation zum Stammbaum. Klicke auf der Karte auf die Schaltfläche **Hauptperson festlegen**, um nach einer anderen Person zu suchen und sie auszuwählen.
- **Jahrestage** – bevorstehende Geburtstage und Jahrestage aus dem Stammbaum, basierend auf dem heutigen Datum.
- **Kürzlich geändert** – eine kurze Liste der zuletzt geänderten Objekte, die hilfreich ist, um gemeinsam vorgenommene Änderungen nachzuverfolgen.

**Rechte Spalte:**

- **Neueste Blogbeiträge** – die neuesten Einträge aus dem [Blog](blog.md), sofern vorhanden.
- **Statistiken** – eine Zusammenfassung der Objektanzahlen im Stammbaum (Anzahl der Personen, Familien, Ereignisse usw.).

Solange der Stammbaum noch leer ist, blendet das Dashboard die Bereiche aus, die keine Inhalte anzeigen könnten, und zeigt stattdessen eine Karte **Erste Schritte** für Benutzer mit Bearbeitungsberechtigungen an: Zunächst wird angeboten, eine Person zu erstellen oder eine Stammbaumdatei zu importieren. Sobald Personen vorhanden sind, wird angeboten, sie durch das Erstellen einer Familie zu verbinden. Die Karte verschwindet, sobald der Stammbaum eine Familie enthält.

Wenn der Stammbaumadministrator eine **Notiz für die Startseite** und/oder ein **Bild für die Startseite** konfiguriert hat, werden diese prominent oberhalb der Hauptspalten angezeigt. Wenn beide festgelegt sind, erscheint das Bild neben dem Text der Notiz. Unter [Administrationseinstellungen](../administration/customization.md) erfährst du, wie du diese konfigurierst.

!!! tip
    Wenn der Stammbaum leer ist und du über Bearbeitungsberechtigungen verfügst, zeigt das Dashboard eine Aufforderung "Erste Schritte" mit Schaltflächen an, über die du deine erste Person hinzufügen oder eine Stammbaumdatei importieren kannst.

## Gramps Web als App installieren

Gramps Web ist eine progressive Web-App (PWA). Das bedeutet, dass dein Browser sie zusammen mit deinen anderen Anwendungen installieren kann, anstatt sie in einem Browser-Tab geöffnet zu halten. Sie erhält dann ein eigenes Symbol und wird in einem eigenen Fenster geöffnet, ohne Adressleiste und Browser-Symbolleisten.

Wie du sie installierst, hängt von deinem Browser ab:

- **Android (Chrome)** – öffne das Menü und wähle "App installieren" oder "Zum Startbildschirm hinzufügen".
- **iOS/iPadOS (Safari)** – tippe auf die Teilen-Schaltfläche und wähle "Zum Home-Bildschirm".
- **Desktop (Chrome, Edge)** – klicke am rechten Ende der Adressleiste auf das Installationssymbol oder verwende den Menüeintrag "Installieren" im Browsermenü.
- **Desktop (Firefox, Safari)** – die Installation wird nicht unterstützt; verwende einen normalen Browser-Tab oder ein normales Browserfenster.

Die Funktionsweise von Gramps Web ändert sich nicht und es werden keine Daten anders gespeichert – es handelt sich um dieselbe Anwendung, die lediglich als eigenständige App dargestellt wird.

!!! note
    Gramps Web muss weiterhin deinen Server erreichen, um deine Daten anzuzeigen. Eine installierte App ermöglicht es dir daher nicht, deinen Stammbaum offline zu durchsuchen.
