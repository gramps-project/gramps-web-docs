---
hide:
  - toc
---

# Benutzerhandbuch

Dieser Abschnitt dokumentiert die Funktionen, die den Benutzern von Gramps Web zur Verfügung stehen.

!!! note "Sehen Sie nicht alle Funktionen?"
    Gramps Web verwendet ein rollenbasiertes Berechtigungssystem. Einige Funktionen – wie das Bearbeiten von Daten, das Verwalten von Etiketten oder das Anzeigen von privaten Datensätzen – sind nur für Benutzer mit ausreichenden Berechtigungen verfügbar. Sie können Ihre aktuelle Rolle in den [Benutzereinstellungen](settings.md) überprüfen. Wenn Sie mehr Zugriff benötigen, wenden Sie sich an den Eigentümer Ihres Baums oder an den Administrator. Siehe [Benutzersystem](../install_setup/users.md) für eine Beschreibung aller Rollen.

## Navigation in der Benutzeroberfläche

### Hauptnavigation

Die Seitenleiste (oder das Hamburger-Menü auf Mobilgeräten) ist der primäre Weg, um zwischen den Abschnitten zu wechseln:

- **Startseite** – das Dashboard (siehe unten)
- **Blog** – Familiengeschichten, die als Blogbeiträge verfasst wurden
- **Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Archive, Notizen** – durchsuchen Sie alle Objekte jedes Typs
- **Medien** – durchsuchen Sie alle Mediendateien (Fotos, Dokumente usw.)
- **Karte** – geografische Ansicht der Orte im Baum
- **Familienstammbaum** – interaktive Stammbaumdiagramme
- **DNA** – DNA-Match-Analysewerkzeuge
- **Chat** – KI-Chat-Assistent (wenn vom Administrator aktiviert)
- **Verlauf** – kürzlich geänderte Objekte
- **Lesezeichen** – Ihre gespeicherten Lesezeichen
- **Aufgaben** – Forschungsaufgaben
- **Export** – exportieren Sie den Familienstammbaum
- **Berichte** – Berichte generieren
- **Revisionen** – vollständige Transaktionshistorie (sichtbar für Mitglieder und höher)
- **Etiketten** – Etiketten verwalten (sichtbar für Redakteure und höher)
- **Benachrichtigungen** – vergangene Benachrichtigungen

### Oben in der App-Leiste

Die Leiste oben auf jeder Seite enthält:

- **Hinzufügen** (Plus-Symbol, sichtbar für Mitwirkende und höher) – öffnet ein Menü zum Erstellen eines neuen Objekts: Person, Familie, Ereignis, Ort, Quelle, Zitation, Archiv, Notiz, Medienobjekt oder Aufgabe
- **Suche** (Lupe) – öffnet die Suchseite
- **Benutzersymbol** – öffnet das Einstellungsmenü: Benutzereinstellungen, Verwaltung (nur für Eigentümer), Benutzer verwalten (nur für Eigentümer), Systeminformationen

## Die Startseite (Dashboard)

Das Dashboard wird angezeigt, wenn Sie sich zum ersten Mal anmelden. Es hat zwei Spalten:

**Linke Spalte:**

- **Hauptperson-Karte** – zeigt den Namen, das Foto (falls verfügbar) und wichtige Fakten Ihrer gewählten Hauptperson an, mit einem Link zu ihrem vollständigen Profil und einer schnellen Navigation zum Familienstammbaum. Klicken Sie auf die Schaltfläche **Hauptperson festlegen** auf der Karte, um nach einer anderen Person zu suchen und diese auszuwählen.
- **Jubiläen** – bevorstehende Geburtstage und Jubiläen aus dem Baum, basierend auf dem heutigen Datum.
- **Kürzlich geändert** – eine kurze Liste der zuletzt modifizierten Objekte, nützlich zur Verfolgung gemeinschaftlicher Bearbeitungen.

**Rechte Spalte:**

- **Aktuelle Blogbeiträge** – die neuesten Einträge aus dem [Blog](blog.md), falls vorhanden.
- **Statistiken** – eine Zusammenfassung der Objektzahlen im Baum (Anzahl der Personen, Familien, Ereignisse usw.).

Wenn der Baumadministrator eine **Startseitennotiz** und/oder ein **Startseitenbild** konfiguriert hat, werden diese prominent über den Hauptspalten angezeigt. Das Bild erscheint neben dem Notiztext, wenn beide festgelegt sind. Siehe [Verwaltungseinstellungen](../administration/settings.md#customization) für Informationen zur Konfiguration dieser.

!!! tip
    Wenn der Baum leer ist und Sie Bearbeitungsberechtigungen haben, zeigt das Dashboard einen "Loslegen"-Hinweis mit Schaltflächen an, um Ihre erste Person hinzuzufügen oder eine Familienstammbaumdatei zu importieren.
