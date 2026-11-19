---
hide:
  - toc
  - navigation
---

# Funktionen

Gramps Web ist eine Webanwendung für kollaborative Genealogie. Es basiert auf [Gramps](https://gramps-project.org/), dem Open-Source-Genealogieprogramm, und arbeitet mit denselben Daten. Sie können es auf Ihrem eigenen Server ausführen oder einen Hosting-Anbieter nutzen.

[Demo ausprobieren](#demo){ .md-button .md-button--primary } [Loslegen](../install_setup/setup.md){ .md-button }

## Erkunden Sie Ihren Stammbaum { .feature-group }

![Fächerdiagramm, das sieben Generationen von Vorfahren zeigt](screenshots/fan.png){ align=right width="400"}

### Interaktive Stammbaumgrafiken

Navigieren Sie durch Ihren Stammbaum als Ahnenbaum, Nachkommenbaum, Sanduhrdiagramm, Beziehungsdiagramm oder Fächerdiagramm, mit hochwertigen interaktiven Grafiken und einer konfigurierbaren Anzahl von Generationen.

Fahren Sie mit der Maus über eine Person, um eine Vorschaukarte mit ihren wichtigsten Fakten zu sehen, und springen Sie direkt vom Diagramm zur vollständigen Detailseite.

<div style="clear:both;"></div>

---

![Zeitleiste der Familienereignisse zwischen den 1940er und 1970er Jahren](screenshots/timeline.png){ align=left width="400"}

### Chronologische Zeitleiste

Sehen Sie jedes Ereignis in Ihrem Stammbaum auf einer horizontalen, zoombaren Zeitleiste. Scrollen und zoomen Sie durch die Jahrhunderte, filtern Sie dann nach einer einzelnen Person – oder nach allen ihren Vorfahren oder Nachkommen – oder nach allem, was an einem bestimmten Ort passiert ist.

Siehe [Zeitleiste](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Karte von London mit einem ausgewählten Ort, der sein Foto und Ereignisse zeigt](screenshots/map.png){ align=right width="400"}

### Interaktive Karte

Zeigen Sie alle Orte in Ihrem Stammbaum auf einer interaktiven, durchsuchbaren Karte an. Suchen Sie nach neuen Orten direkt auf OpenStreetMap, wenn Sie einen Ort erstellen, plotten Sie die Personen in Ihrer Datenbank geografisch und verfolgen Sie das Leben einer einzelnen Person, indem Sie ihre Ereignisse mit Linien auf der Karte verbinden.

<div style="clear:both;"></div>

---

![London auf der OpenHistoricalMap-Ebene, mit dem Zeitregler auf 1707 eingestellt](screenshots/ohm.png){ align=left width="400"}

### Historische Karten

Verwandeln Sie eine historische Karte, die als Medienobjekt in Gramps gespeichert ist, in eine benutzerdefinierte Kartenüberlagerung.

Sie können auch zu den historischen Vektorkarten des [OpenHistoricalMap](https://www.openhistoricalmap.org/) Projekts wechseln. Verwenden Sie den Zeitregler, um durch die Entwicklung der Orte in Ihrer Familiengeschichte zu scrollen und die Orte anzuzeigen, an denen Vorfahren lebten oder Ereignisse stattfanden.

<div style="clear:both;"></div>

---

![Suchergebnisse für "Albert" über Personen, Ereignisse und Medien](screenshots/search.png){ align=right width="400"}

### Alles finden

Die Volltext-Suchmaschine deckt alle Gramps-Objekttypen ab, einschließlich des Inhalts von Textnotizen, und unterstützt Platzhalter und logische Operatoren.

Für präzise Abfragen bieten die Objektlistenansichten einen erweiterten Filtermodus basierend auf der [Gramps Object Query Language](../user-guide/goql.md), neben schnellen Filtern nach Text, Etikett und Datenschutz.

Von der Seite jeder Person aus öffnet die [Externe Suche](../user-guide/external-search.md) eine vorab ausgefüllte Suche auf FamilySearch, Ancestry, CompGen und anderen Seiten – und Sie können Ihre eigenen hinzufügen.

<div style="clear:both;"></div>

## Erstellen und Forschen { .feature-group }

![Ahnenbaum im Bearbeitungsmodus mit dem Dialog zum Hinzufügen eines Familienmitglieds](screenshots/tree-edit.png){ align=left width="400"}

### Erstellen Sie Ihren Baum direkt im Diagramm

Schalten Sie die Baumansicht in den Bearbeitungsmodus und erweitern Sie Ihren Stammbaum, ohne das Diagramm zu verlassen. Jede Personenkarte erhält einen **+**-Button, um einen Vater, eine Mutter, ein Kind oder einen Ehepartner hinzuzufügen – entweder indem Sie jemanden verlinken, der bereits in Ihrer Datenbank ist, oder indem Sie sofort eine ganz neue Person erstellen. Jede Änderung wird sofort gespeichert.

Siehe [Bearbeiten des Stammbaums](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![Der KI-Assistent liest eine Geburtsurkunde und schlägt neue Datensätze vor](screenshots/chat.png){ align=right width="400"}

### Integrierter KI-Assistent

Stellen Sie Fragen zu Ihrem Stammbaum in Ihrer eigenen Sprache und erhalten Sie Antworten basierend auf Ihren Daten.

Der Assistent sucht nicht nur: Er fragt Ihre Datenbank direkt mit einer Reihe von Werkzeugen ab, filtert Personen, Ereignisse, Familien und Orte und berechnet Beziehungen zwischen Individuen. Sie können beobachten, welche Werkzeuge er verwendet, während er eine Antwort erstellt, und längere Fragen werden als Hintergrundaufgaben ausgeführt, sodass Sie navigieren und später zurückkommen können.

Der Assistent ist optional und muss [vom Serveradministrator eingerichtet werden](../install_setup/chat.md) mit einem KI-Modellanbieter.

<div style="clear:both;"></div>

---

![Chromosomenbrowser, der die gemeinsamen DNA-Segmente von elf Übereinstimmungen anzeigt](screenshots/dna.png){ align=left width="400"}

### DNA-Übereinstimmungen, Chromosomenbrowser & Y-DNA

Laden Sie DNA-Übereinstimmungsdaten von Ihrem DNA-Testanbieter hoch, speichern Sie sie zusammen mit Ihrem Stammbaum und sehen Sie Ihre Übereinstimmungen in einem interaktiven Chromosomenbrowser.

Rohdaten zu Y-Chromosomen-SNPs können verwendet werden, um die wahrscheinlichste [Y-DNA-Haplogruppe](../user-guide/y-dna.md) einer Person zu bestimmen und ihre patrilinearen Vorfahren im menschlichen Y-Chromosomenbaum mit Zeitangaben anzuzeigen. Die Analyse erfolgt vollständig auf Ihrem eigenen Server – keine Daten werden an Dritte gesendet.

<div style="clear:both;"></div>

---

![Gemälde mit zwei markierten Personen und den anderen erkannten Gesichtern umrandet](screenshots/tag.png){ align=right width="400"}

### Personen in Fotos mit automatischer Gesichtserkennung markieren

Identifizieren Sie Vorfahren in alten Familienfotos zusammen mit Ihren Verwandten. Gesichter werden automatisch erkannt, sodass das Markieren einer Person nur zwei Klicks benötigt.

<div style="clear:both;"></div>

---

![Liste der Forschungsaufgaben mit Status, Priorität und Etiketten](screenshots/tasks.png){ align=left width="400"}

### Integrierte Aufgabenverwaltungs-App

Gramps Web kommt mit einer integrierten Aufgabenverwaltungs-App, um Ihre genealogische Forschung zu organisieren und zu planen. Geben Sie jeder Aufgabe einen Status, eine Priorität und Etiketten, dokumentieren Sie Ihren Fortschritt in einer Rich-Text-Beschreibung und fügen Sie die Medien hinzu, die Sie unterwegs gesammelt haben.

Die Aufgaben werden als Quellen in der Gramps-Datenbank gespeichert, sodass sie Teil Ihrer genealogischen Daten sind und auch in Gramps Desktop zugegriffen und bearbeitet werden können.

<div style="clear:both;"></div>

---

![Blogbeitrag über die Identifizierung der Personen in einem Familienfoto](screenshots/blog.png){ align=right width="400"}

### Genealogie-Blog enthalten

Fassen Sie Ihre Forschung in Form von Bloggeschichten mit Bildern zusammen und teilen Sie sie mit Ihren Verwandten. Ein spezieller Editor macht das Schreiben eines neuen Beitrags einfach. Alle Daten werden in der Gramps-Datenbank gespeichert.

<div style="clear:both;"></div>

## Gemeinsam arbeiten { .feature-group }

![Liste der Personen im Stammbaum](screenshots/list.png){ align=left width="400"}

### Datenschutzeinstellungen & Benutzerzugriff

Sie können [Datensätze als privat markieren](../user-guide/privacy.md) – bis hin zu einem einzelnen Namen, Ereignislink oder DNA-Übereinstimmung – und steuern, welche Benutzer private Datensätze einsehen dürfen. Private Datensätze werden auf der Datenbankebene für maximale Sicherheit herausgefiltert. Darüber hinaus können Sie steuern, was Benutzer hinzufügen und bearbeiten dürfen.

Benutzer können sich mit einem Passwort anmelden oder über einen externen Identitätsanbieter mit [OpenID Connect](../install_setup/oidc.md) – Google und Microsoft sofort, sowie benutzerdefinierte Anbieter wie Keycloak, Authentik und Authelia.

<div style="clear:both;"></div>

---

![Eine Revision, die die geänderten Felder in einem Personen-Datensatz zeigt](screenshots/revisions.png){ align=right width="400"}

### Vollständige Revisionshistorie – mit Rückgängig

Jede Bearbeitung Ihres Stammbaums wird aufgezeichnet. Durchsuchen Sie die vollständige Historie, gruppiert nach Transaktion, und tauchen Sie in jede einzelne Änderung ein, um genau zu sehen, welche Felder hinzugefügt, entfernt oder geändert wurden, und machen Sie eine Transaktion rückgängig, wenn sich herausstellt, dass es ein Fehler war. Jede Objektseite hat auch ihren eigenen Reiter für Revisionen, der zeigt, wer es wann geändert hat.

Siehe [Revisionshistorie](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Das Menü "Werkzeuge" von Gramps Desktop mit dem Eintrag "Gramps Web Sync"](screenshots/sync.png){ align=left width="300"}

### Vollständige Integration mit Gramps Desktop

Gramps Web verwendet dasselbe Datenmodell und dieselbe Datenbank wie [Gramps Desktop](https://gramps-project.org/). Sie können alle gleichen [Datensatztypen](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) durchsuchen und bearbeiten: Personen, Familien, Ereignisse, Orte, Archive, Quellen, Zitationen, Medienobjekte und Notizen.

Mit dem [Gramps Web Sync-Add-on](../administration/sync.md) für Gramps Desktop können Sie Ihre Daten in beide Richtungen synchronisieren, sodass Sie sowohl in Gramps Desktop als auch in Gramps Web gleichzeitig weiterarbeiten können.

<div style="clear:both;"></div>

## Berichte und Datenexport { .feature-group }

![Ahnenbericht, der als PDF generiert wurde](screenshots/report.png){ align=right width="400"}

### Erstellen Sie druckbare Berichte

Gramps Web basiert auf demselben Kern wie Gramps Desktop, sodass Sie fast alle [Berichte](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) der Desktop-App direkt im Browser generieren können, einschließlich Beziehungsdiagrammen oder Buchberichten als PDF.

<div style="clear:both;"></div>

---

![Exportseite mit der Liste der verfügbaren Dateiformate](screenshots/export.png){ align=left width="300"}

### Kein Lock-in – Datenimport und -export

Importieren Sie Daten in verschiedenen Formaten, einschließlich Gramps XML und GEDCOM, und laden Sie jederzeit alle Ihre Daten herunter – Stammbaumdaten, Mediendateien und Benutzerkonten – für Backups oder um zu einem anderen Server zu wechseln.

Importe können als Trockenlauf vor dem Schreiben angezeigt werden, und ein vollständiges Backup kann wieder in den Baum zurückgestellt werden.

<div style="clear:both;"></div>

## Überall verwenden { .feature-group }

![Die gleiche Personenseite auf einem Desktop und auf einem Telefon](screenshots/mobile.png){ align=right width="400"}

### Funktioniert auf jedem Gerät

Verwenden Sie Gramps Web auf jedem Gerät mit einem Webbrowser: Laden Sie Fotos hoch, erstellen oder bearbeiten Sie Datensätze oder zeigen Sie Ihren Stammbaum Verwandten beim nächsten Familientreffen.

Gramps Web ist eine progressive Webanwendung: Installieren Sie es auf Ihrem Startbildschirm oder Desktop, und es verhält sich wie eine native App. Auf dem Desktop bringen Sie [Tastenkombinationen](../user-guide/shortcuts.md) überallhin in wenigen Tastenanschlägen – drücken Sie `?`, um sie alle zu sehen.

<div style="clear:both;"></div>

---

![Spracheauswahlmenü](screenshots/lang.png){ align=left width="300"}

### Vollständig internationalisiert

Verwenden Sie die Benutzeroberfläche in einer von mehr als 50 Sprachen, die von der Gramps-Community übersetzt wurden.

<div style="clear:both;"></div>

## Und mehr

- **Benachrichtigungen und Hintergrundaufgaben** – Importe, Exporte, Berichte und Indexerneuerungen laufen im Hintergrund, mit Fortschritten und Fehlern, die an einem Ort gesammelt werden
- **Etiketten, Lesezeichen und Verlauf** – Organisieren Sie Objekte mit farbcodierten Etiketten und kehren Sie zu dem zurück, woran Sie gearbeitet haben
- **Massenbearbeitung** – Wählen Sie mehrere Objekte in den Listenansichten aus, um sie auf einmal zu löschen oder doppelte Objekte zusammenzuführen
- **Anpassbare Listenansichten** – Wählen Sie, welche Spalten angezeigt werden sollen, und filtern Sie nach Text, Etikett oder Datenschutz
- **Texterkennung (OCR)** – Extrahieren Sie Text aus gescannten Dokumenten in Ihrer Mediathek
- **Datenüberprüfung** – Überprüfen Sie Ihren Baum auf unplausible Daten und andere Datenprobleme
- **Kalender** – Geben Sie Daten im Gregorianischen, Julianischen, Hebräischen, Französischen Republik, Persischen, Islamischen oder Schwedischen Kalender ein
- **Gestalten Sie es nach Ihren Wünschen** – Geben Sie Ihrer Website einen eigenen Namen, Themenfarben sowie Text und Bild für die Startseite

## Demo

Um sich in die Demo einzuloggen, verwenden Sie eines der folgenden Benutzername/Passwort-Paare. Jedes repräsentiert eine der Benutzerrollen in Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

Die Demo wird alle zwei Stunden zurückgesetzt, sodass alle Änderungen, die Sie vornehmen, vorübergehend sind.

[Zur Demo-Anmeldung gehen](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Danke

Die Demo wird freundlicherweise von DigitalOcean unterstützt.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
