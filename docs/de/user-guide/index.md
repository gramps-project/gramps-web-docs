---
hide:
  - toc
---

# Benutzerhandbuch

Dieser Abschnitt dokumentiert die Funktionen, die den Benutzern von Gramps Web zur Verfügung stehen.

!!! note "Sie sehen nicht alle Funktionen?"
    Gramps Web verwendet ein rollenbasiertes Berechtigungssystem. Einige Funktionen – wie das Bearbeiten von Daten, das Verwalten von Etiketten oder das Anzeigen von privaten Datensätzen – sind nur für Benutzer mit ausreichenden Berechtigungen verfügbar. Sie können Ihre aktuelle Rolle in den [Benutzereinstellungen](settings.md) überprüfen. Wenn Sie mehr Zugriff benötigen, wenden Sie sich an den Eigentümer oder Administrator Ihres Baums. Siehe [Benutzersystem](../install_setup/users.md) für eine Beschreibung aller Rollen.

## Navigation in der Benutzeroberfläche

### Hauptnavigation

Die Seitenleiste (oder das Hamburger-Menü auf mobilen Geräten) ist der primäre Weg, um zwischen den Abschnitten zu wechseln:

- **Startseite** – das Dashboard (siehe unten)
- **Blog** – Geschichten zur Familiengeschichte, die als Blogbeiträge verfasst wurden
- **Familienbaum** – interaktive Baumdiagramme
- **Zeitachse** – chronologische Ansicht der Ereignisse im Baum (benötigt eine ausreichend aktuelle Gramps Web API-Version)
- **Karte** – geografische Ansicht der Orte im Baum
- **DNA** – Werkzeuge zur Analyse von DNA-Übereinstimmungen
- **Listen** – Durchsuchen aller Objekte jedes Typs: Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen
- **Medien** – Durchsuchen aller Mediendateien (Fotos, Dokumente usw.)
- **Assistent** – KI-Chat-Assistent (wenn vom Administrator aktiviert)
- **Verlauf** – kürzlich geänderte Objekte
- **Lesezeichen** – Ihre gespeicherten Lesezeichen
- **Aufgaben** – Forschung Aufgaben
- **Berichte** – Berichte erstellen
- **Export** – den Familienbaum exportieren
- **Revisionen** – vollständige Transaktionshistorie (sichtbar für Mitglieder und darüber)
- **Benachrichtigungen** – vergangene Benachrichtigungen

!!! note
    Etiketten werden nicht mehr über die Seitenleiste verwaltet – die Etikettenverwaltung wurde zu den [Administrationseinstellungen](../administration/settings.md#tags) verschoben (nur Eigentümer/Administratoren). Siehe [Etiketten](tags.md) für die Verwendung von Etiketten.

### Obere App-Leiste

Die Leiste oben auf jeder Seite enthält:

- **Hinzufügen** (Plus-Symbol, sichtbar für Mitwirkende und darüber) – öffnet ein Menü zum Erstellen eines neuen Objekts: Person, Familie, Ereignis, Ort, Quelle, Zitation, Repository, Notiz, Medienobjekt oder Aufgabe
- **Suche** (Lupe) – öffnet die Suchseite
- **Benutzersymbol** – öffnet das Einstellungsmenü: Benutzereinstellungen, Verwaltung (nur Eigentümer), Benutzer verwalten (nur Eigentümer), Systeminformationen

## Die Startseite (Dashboard)

Das Dashboard wird angezeigt, wenn Sie sich zum ersten Mal anmelden. Es hat zwei Spalten:

**Linke Spalte:**

- **Hauptperson-Karte** – zeigt den Namen, das Foto (falls verfügbar) und die wichtigsten Fakten Ihrer gewählten Hauptperson, mit einem Link zu ihrem vollständigen Profil und schneller Navigation zum Familienbaum. Klicken Sie auf die Schaltfläche **Hauptperson festlegen** auf der Karte, um nach einer anderen Person zu suchen und diese auszuwählen.
- **Jubiläen** – bevorstehende Geburtstage und Jubiläen aus dem Baum, basierend auf dem heutigen Datum.
- **Kürzlich geändert** – eine kurze Liste der zuletzt modifizierten Objekte, nützlich zur Verfolgung gemeinschaftlicher Bearbeitungen.

**Rechte Spalte:**

- **Aktuelle Blogbeiträge** – die neuesten Einträge aus dem [Blog](blog.md), falls vorhanden.
- **Statistiken** – eine Zusammenfassung der Objektzahlen im Baum (Anzahl der Personen, Familien, Ereignisse usw.).

Wenn der Baumadministrator eine **Startseitennotiz** und/oder ein **Startseitenbild** konfiguriert hat, werden diese prominent über den Hauptspalten angezeigt. Das Bild erscheint neben dem Notiztext, wenn beide festgelegt sind. Siehe [Administrationseinstellungen](../administration/settings.md#customization) für die Konfiguration dieser.

!!! tip
    Wenn der Baum leer ist und Sie Bearbeitungsberechtigungen haben, zeigt das Dashboard eine "Loslegen"-Aufforderung mit Schaltflächen zum Hinzufügen Ihrer ersten Person oder zum Importieren einer Familienbaumdatei.

## Gramps Web als App installieren

Gramps Web ist eine progressive Web-App (PWA), was bedeutet, dass Ihr Browser es neben Ihren anderen Anwendungen installieren kann, anstatt es in einem Browser-Tab zu belassen. Es erhält dann ein eigenes Symbol und öffnet sich in einem eigenen Fenster, ohne die Adressleiste und die Browser-Toolbars.

Wie Sie es installieren, hängt von Ihrem Browser ab:

- **Android (Chrome)** – öffnen Sie das Menü und wählen Sie "App installieren" oder "Zum Startbildschirm hinzufügen".
- **iOS/iPadOS (Safari)** – tippen Sie auf die Teilen-Schaltfläche und wählen Sie "Zum Home-Bildschirm hinzufügen".
- **Desktop (Chrome, Edge)** – klicken Sie auf das Installationssymbol am rechten Ende der Adressleiste oder verwenden Sie den Menüeintrag "Installieren".
- **Desktop (Firefox, Safari)** – die Installation wird nicht unterstützt; verwenden Sie einen normalen Browser-Tab oder ein Fenster.

Es ändert sich nichts daran, wie Gramps Web funktioniert, und keine Daten werden anders gespeichert – es ist dieselbe Anwendung, nur als eigenständige App präsentiert.

!!! note
    Gramps Web muss weiterhin Ihren Server erreichen, um Ihre Daten anzuzeigen, sodass eine installierte App Ihnen nicht ermöglicht, Ihren Familienbaum offline zu durchsuchen.
