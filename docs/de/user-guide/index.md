---
hide:
  - toc
---

# Benutzerhandbuch

Dieser Abschnitt dokumentiert die Funktionen, die den Benutzern von Gramps Web zur Verfügung stehen.

!!! note "Sie sehen nicht alle Funktionen?"
    Gramps Web verwendet ein rollenbasiertes Berechtigungssystem. Einige Funktionen – wie das Bearbeiten von Daten, das Verwalten von Etiketten oder das Anzeigen von privaten Datensätzen – sind nur für Benutzer mit ausreichenden Berechtigungen verfügbar. Sie können Ihre aktuelle Rolle in den [Benutzereinstellungen](settings.md) überprüfen. Wenn Sie mehr Zugriff benötigen, wenden Sie sich an den Eigentümer Ihres Baums oder den Administrator. Siehe [Benutzersystem](../install_setup/users.md) für eine Beschreibung aller Rollen.

## Navigation in der Benutzeroberfläche

### Hauptnavigation

Die Seitenleiste (oder das Hamburger-Menü auf Mobilgeräten) ist der primäre Weg, um zwischen den Abschnitten zu wechseln:

- **Startseite** – das Dashboard (siehe unten)
- **Blog** – Familiengeschichten, die als Blogbeiträge verfasst wurden
- **Familienstammbaum** – interaktive Baumdiagramme
- **Zeitachse** – chronologische Ansicht der Ereignisse im Baum (benötigt eine ausreichend aktuelle Gramps Web API-Version)
- **Karte** – geografische Ansicht der Orte im Baum
- **DNA** – Werkzeuge zur Analyse von DNA-Übereinstimmungen
- **Listen** – Durchsuchen aller Objekte jedes Typs: Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen
- **Medien** – Durchsuchen aller Mediendateien (Fotos, Dokumente usw.)
- **Assistent** – KI-Chat-Assistent (wenn vom Administrator aktiviert)
- **Historie** – kürzlich geänderte Objekte
- **Lesezeichen** – Ihre gespeicherten Lesezeichen
- **Aufgaben** – Forschungsaufgaben
- **Berichte** – Berichte erstellen
- **Export** – den Familienstammbaum exportieren
- **Revisionen** – vollständige Transaktionshistorie (sichtbar für Mitglieder und höher)
- **Benachrichtigungen** – vergangene Benachrichtigungen

!!! note
    Etiketten werden nicht mehr über die Seitenleiste verwaltet – die Etikettenverwaltung wurde zu den [Verwaltungseinstellungen](../administration/settings.md#tags) verschoben (nur Eigentümer/Administrator). Siehe [Etiketten](tags.md) für die Verwendung von Etiketten.

### Obere App-Leiste

Die Leiste oben auf jeder Seite enthält:

- **Hinzufügen** (Plus-Symbol, sichtbar für Mitwirkende und höher) – öffnet ein Menü zum Erstellen eines neuen Objekts: Person, Familie, Ereignis, Ort, Quelle, Zitation, Repository, Notiz, Medienobjekt oder Aufgabe
- **Suche** (Lupe) – öffnet die Suchseite
- **Benutzersymbol** – öffnet das Einstellungsmenü: Benutzereinstellungen, Verwaltung (nur Eigentümer), Benutzer verwalten (nur Eigentümer), Systeminformationen

## Die Startseite (Dashboard)

Das Dashboard wird angezeigt, wenn Sie sich zum ersten Mal anmelden. Es hat zwei Spalten:

**Linke Spalte:**

- **Hauptperson-Karte** – zeigt den Namen, das Foto (falls verfügbar) und die wichtigsten Fakten Ihrer gewählten Hauptperson an, mit einem Link zu ihrem vollständigen Profil und einer schnellen Navigation zum Familienstammbaum. Klicken Sie auf die Schaltfläche **Hauptperson festlegen** auf der Karte, um nach einer anderen Person zu suchen und diese auszuwählen.
- **Jubiläen** – bevorstehende Geburtstage und Jubiläen aus dem Baum, basierend auf dem heutigen Datum.
- **Kürzlich geändert** – eine kurze Liste der zuletzt modifizierten Objekte, nützlich zur Verfolgung gemeinschaftlicher Bearbeitungen.

**Rechte Spalte:**

- **Aktuelle Blogbeiträge** – die neuesten Einträge aus dem [Blog](blog.md), sofern vorhanden.
- **Statistiken** – eine Zusammenfassung der Objektzahlen im Baum (Anzahl der Personen, Familien, Ereignisse usw.).

Wenn der Baumadministrator eine **Startseitennotiz** und/oder ein **Startseitenbild** konfiguriert hat, werden diese prominent über den Hauptspalten angezeigt. Das Bild erscheint neben dem Notiztext, wenn beide festgelegt sind. Siehe [Verwaltungseinstellungen](../administration/settings.md#customization) für die Konfiguration dieser.

!!! tip
    Wenn der Baum leer ist und Sie Bearbeitungsberechtigungen haben, zeigt das Dashboard eine "Loslegen"-Aufforderung mit Schaltflächen zum Hinzufügen Ihrer ersten Person oder zum Importieren einer Familienstammbaumdatei an.
