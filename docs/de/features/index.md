---
hide:
  - toc
  - navigation
---

# Funktionen

Gramps Web ist eine Webanwendung für kollaborative Genealogie. Sie basiert auf [Gramps](https://gramps-project.org/), dem quelloffenen Genealogieprogramm, und verwendet dieselben Daten. Du kannst sie auf deinem eigenen Server betreiben oder einen Hosting-Anbieter nutzen.

[Demo ausprobieren](#demo){ .md-button .md-button--primary } [Erste Schritte](../install_setup/setup.md){ .md-button }

## Deinen Stammbaum erkunden { .feature-group }

![Fächerdiagramm mit sieben Generationen von Vorfahren](screenshots/fan.png){ align=right width="400"}

### Interaktive Stammbaumdiagramme

Navigiere durch deinen Stammbaum als Vorfahrenbaum, Nachkommenbaum, Sanduhrdiagramm, Verwandtschaftsdiagramm oder Fächerdiagramm – mit hochwertigen interaktiven Grafiken und einer konfigurierbaren Anzahl von Generationen.

Bewege den Mauszeiger über eine beliebige Person, um eine Vorschaukarte mit den wichtigsten Fakten zu sehen, und springe direkt vom Diagramm zur vollständigen Detailseite.

<div style="clear:both;"></div>

---

![Zeitleiste von Familienereignissen zwischen den 1940er- und 1970er-Jahren](screenshots/timeline.png){ align=left width="400"}

### Chronologische Zeitleiste

Sieh dir jedes Ereignis in deinem Stammbaum auf einer horizontalen, zoombaren Zeitleiste an. Scrolle und zoome durch die Jahrhunderte und filtere dann auf eine einzelne Person – oder auf alle ihre Vorfahren oder Nachkommen – oder auf alles, was an einem Ort geschehen ist.

Siehe [Zeitleiste](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Karte von London mit ausgewähltem Ort, seinem Foto und seinen Ereignissen](screenshots/map.png){ align=right width="400"}

### Interaktive Karte

Zeige alle Orte in deinem Stammbaum auf einer interaktiven, durchsuchbaren Karte an. Suche beim Erstellen eines Ortes direkt auf OpenStreetMap nach neuen Orten, stelle die Personen in deiner Datenbank geografisch dar und verfolge das Leben einer einzelnen Person, indem du ihre Ereignisse auf der Karte mit Linien verbindest.

<div style="clear:both;"></div>

---

![London auf der OpenHistoricalMap-Ebene mit dem auf 1707 eingestellten Zeitschieberegler](screenshots/ohm.png){ align=left width="400"}

### Historische Karten

Verwandle eine in Gramps als Medienobjekt gespeicherte historische Karte in eine benutzerdefinierte Kartenebene.

Du kannst auch zu den historischen Vektorkarten des Projekts [OpenHistoricalMap](https://www.openhistoricalmap.org/) wechseln. Verwende den Zeitschieberegler, um die Entwicklung der Orte in deiner Familiengeschichte zu verfolgen und die Orte anzuzeigen, an denen Vorfahren gelebt haben oder Ereignisse stattgefunden haben.

<div style="clear:both;"></div>

---

![Suchergebnisse für „Albert“ in Personen, Ereignissen und Medien](screenshots/search.png){ align=right width="400"}

### Alles finden

Die Volltextsuche umfasst alle Gramps-Objekttypen, einschließlich des Inhalts von Textnotizen, und unterstützt Platzhalter sowie logische Operatoren.

Für präzise Abfragen bieten die Ansichten der Objektlisten einen erweiterten Filtermodus auf Grundlage der [Gramps Object Query Language](../user-guide/goql.md), zusätzlich zu Schnellfiltern nach Text, Etikett und Privatsphäre.

Auf der Seite jeder Person öffnet die [externe Suche](../user-guide/external-search.md) eine vorausgefüllte Suche auf FamilySearch, Ancestry, CompGen und anderen Websites – und du kannst eigene hinzufügen.

<div style="clear:both;"></div>

## Aufbauen und forschen { .feature-group }

![Vorfahrenbaum im Bearbeitungsmodus mit dem Dialog zum Hinzufügen eines Familienmitglieds](screenshots/tree-edit.png){ align=left width="400"}

### Deinen Stammbaum direkt im Diagramm aufbauen

Wechsle die Stammbaumansicht in den Bearbeitungsmodus und erweitere deinen Stammbaum, ohne das Diagramm zu verlassen. Jede Personenkarte erhält eine **+**-Schaltfläche zum Hinzufügen eines Vaters, einer Mutter, eines Kindes oder eines Ehepartners – entweder durch Verknüpfen einer bereits in deiner Datenbank vorhandenen Person oder durch sofortiges Erstellen einer völlig neuen Person. Jede Änderung wird sofort gespeichert.

Siehe [Stammbaum bearbeiten](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![Der KI-Assistent liest eine Geburtsurkunde und schlägt neue Datensätze vor](screenshots/chat.png){ align=right width="400"}

### Integrierter KI-Assistent

Stelle Fragen zu deinem Stammbaum in deiner eigenen Sprache und erhalte Antworten auf Grundlage deiner Daten.

Der Assistent sucht nicht nur: Er fragt deine Datenbank direkt mit einer Reihe von Werkzeugen ab, filtert Personen, Ereignisse, Familien und Orte und berechnet Verwandtschaftsbeziehungen zwischen Personen. Du kannst beobachten, welche Werkzeuge er verwendet, während er eine Antwort erstellt. Längere Fragen werden als Hintergrundaufgaben ausgeführt, sodass du weg navigieren und später zurückkehren kannst.

Der Assistent ist optional und muss vom [Serveradministrator eingerichtet](../install_setup/chat.md) werden, einschließlich eines KI-Modellanbieters.

<div style="clear:both;"></div>

---

![Chromosomen-Browser mit den gemeinsamen DNA-Segmenten von elf Übereinstimmungen](screenshots/dna.png){ align=left width="400"}

### DNA-Übereinstimmungen, Chromosomen-Browser & Y-DNA

Lade DNA-Übereinstimmungsdaten von deinem DNA-Testanbieter hoch, speichere sie zusammen mit deinem Stammbaum und sieh dir deine Übereinstimmungen in einem interaktiven Chromosomen-Browser an.

Rohdaten zu SNPs des Y-Chromosoms können verwendet werden, um die wahrscheinlichste [Y-DNA-Haplogruppe](../user-guide/y-dna.md) einer Person zu bestimmen und ihre väterlichen Vorfahren im menschlichen Y-Chromosomenbaum mit Zeitschätzungen anzuzeigen. Die Analyse läuft vollständig auf deinem eigenen Server – es werden keine Daten an Dritte gesendet.

<div style="clear:both;"></div>

---

![Gemälde mit zwei etikettierten Personen und den Umrissen weiterer erkannter Gesichter](screenshots/tag.png){ align=right width="400"}

### Personen in Fotos mit automatischer Gesichtserkennung etikettieren

Identifiziere gemeinsam mit deinen Verwandten Vorfahren auf alten Familienfotos. Gesichter werden automatisch erkannt, sodass das Etikettieren einer Person zwei Klicks erfordert.

<div style="clear:both;"></div>

---

![Liste von Forschungsaufgaben mit Status, Priorität und Etiketten](screenshots/tasks.png){ align=left width="400"}

### Integrierte Aufgabenverwaltung

Gramps Web verfügt über eine integrierte Aufgabenverwaltung, mit der du deine genealogische Forschung organisieren und planen kannst. Weise jeder Aufgabe einen Status, eine Priorität und Etiketten zu, dokumentiere deinen Fortschritt in einer Rich-Text-Beschreibung und füge die dabei gesammelten Medien hinzu.

Die Aufgaben werden als Quellen in der Gramps-Datenbank gespeichert und sind somit Teil deiner genealogischen Daten. Sie können auch in Gramps Desktop aufgerufen und bearbeitet werden.

<div style="clear:both;"></div>

---

![Blogbeitrag über die Identifizierung der Personen auf einem Familienfoto](screenshots/blog.png){ align=right width="400"}

### Genealogie-Blog inklusive

Fasse deine Forschung in Form von Bloggeschichten mit Bildern zusammen und teile sie mit deinen Verwandten. Ein eigener Editor macht das Schreiben eines neuen Beitrags unkompliziert. Alle Daten werden in der Gramps-Datenbank gespeichert.

<div style="clear:both;"></div>

## Zusammenarbeiten { .feature-group }

![Liste der Personen im Stammbaum](screenshots/list.png){ align=left width="400"}

### Privatsphärestufen und Benutzerzugriff

Du kannst [Datensätze als privat markieren](../user-guide/privacy.md) – bis hin zu einem einzelnen Namen, einer Ereignisverknüpfung oder einer DNA-Übereinstimmung – und festlegen, welche Benutzer private Datensätze anzeigen dürfen. Private Datensätze werden für maximale Sicherheit auf Datenbankebene herausgefiltert. Außerdem kannst du steuern, was Benutzer hinzufügen und bearbeiten dürfen.

Benutzer können sich mit einem Passwort oder über einen externen Identitätsanbieter mit [OpenID Connect](../install_setup/oidc.md) anmelden – Google und Microsoft sind sofort verfügbar, ebenso benutzerdefinierte Anbieter wie Keycloak, Authentik und Authelia.

<div style="clear:both;"></div>

---

![Eine Revision mit den in einem Personendatensatz geänderten Feldern](screenshots/revisions.png){ align=right width="400"}

### Vollständiger Revisionsverlauf – mit Rückgängig-Funktion

Jede Bearbeitung deines Stammbaums wird aufgezeichnet. Durchsuche den vollständigen Verlauf, nach Transaktionen gruppiert, und sieh dir jede einzelne Änderung genau an, um festzustellen, welche Felder hinzugefügt, entfernt oder geändert wurden. Mache eine Transaktion rückgängig, wenn sie sich als Fehler herausstellt. Die Seite jedes Objekts verfügt außerdem über einen eigenen Revisionstab, der anzeigt, wer es wann geändert hat.

Siehe [Revisionsverlauf](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Das Menü „Werkzeuge“ von Gramps Desktop mit dem Eintrag „Gramps Web Sync“](screenshots/sync.png){ align=left width="300"}

### Vollständige Integration mit Gramps Desktop

Gramps Web verwendet dasselbe Datenmodell und dieselbe Datenbank wie [Gramps Desktop](https://gramps-project.org/). Du kannst dieselben [Datensatztypen](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) durchsuchen und bearbeiten: Personen, Familien, Ereignisse, Orte, Repositorien, Quellen, Quellenangaben, Medienobjekte und Notizen.

Mit dem [Gramps-Web-Sync-Add-on](../administration/sync.md) für Gramps Desktop kannst du deine Daten in beide Richtungen synchronisieren und so parallel in Gramps Desktop und Gramps Web arbeiten.

<div style="clear:both;"></div>

## Berichte und Datenexport { .feature-group }

![Als PDF erstellter Vorfahrenbericht](screenshots/report.png){ align=right width="400"}

### Druckbare Berichte erstellen

Gramps Web basiert auf demselben Kern wie Gramps Desktop. Daher kannst du fast alle vom Desktopprogramm unterstützten [Berichte](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) direkt im Browser erstellen, einschließlich Verwandtschaftsdiagrammen oder Buchberichten als PDF.

<div style="clear:both;"></div>

---

![Exportseite mit der Liste der verfügbaren Dateiformate](screenshots/export.png){ align=left width="300"}

### Keine Bindung – Datenimport und -export

Importiere Daten in verschiedenen Formaten, einschließlich Gramps XML und GEDCOM, und lade jederzeit alle deine Daten herunter – Stammbaumdaten, Mediendateien und Benutzerkonten – für Sicherungen oder zum Umzug auf einen anderen Server.

Importe können vor dem Schreiben als Probelauf in der Vorschau angezeigt werden, und eine vollständige Sicherung kann wieder in den Stammbaum eingespielt werden.

<div style="clear:both;"></div>

## Überall verwenden { .feature-group }

![Dieselbe Personenseite auf einem Desktopcomputer und einem Smartphone](screenshots/mobile.png){ align=right width="400"}

### Funktioniert auf jedem Gerät

Verwende Gramps Web auf jedem Gerät mit einem Webbrowser: Lade Fotos hoch, erstelle oder bearbeite Datensätze oder zeige deinen Verwandten beim nächsten Familientreffen deinen Stammbaum.

Gramps Web ist eine progressive Web-App: Installiere sie auf deinem Startbildschirm oder Desktop, und sie verhält sich wie eine native App. Auf dem Desktop bringen dich [Tastenkürzel](../user-guide/shortcuts.md) mit wenigen Tastenanschlägen überallhin – drücke `?`, um alle anzuzeigen.

<div style="clear:both;"></div>

---

![Menü zur Sprachauswahl](screenshots/lang.png){ align=left width="300"}

### Vollständig internationalisiert

Verwende die Benutzeroberfläche in jeder der mehr als 50 Sprachen, die von der Gramps-Community übersetzt wurden.

<div style="clear:both;"></div>

## Und vieles mehr

- **Benachrichtigungen und Hintergrundaufgaben** – Importe, Exporte, Berichte und Indexneuerstellungen werden im Hintergrund ausgeführt; Fortschritt und Fehler werden an einer Stelle gesammelt
- **Etiketten, Lesezeichen und Verlauf** – Organisiere Objekte mit farbcodierten Etiketten und kehre zu deiner letzten Arbeit zurück
- **Massenbearbeitung** – Wähle in den Listenansichten mehrere Objekte aus, um sie auf einmal zu löschen oder doppelte Objekte zusammenzuführen
- **Anpassbare Listenansichten** – Wähle die anzuzeigenden Spalten und filtere nach Text, Etikett oder Privatsphäre
- **Texterkennung (OCR)** – Extrahiere Text aus gescannten Dokumenten in deiner Mediengalerie
- **Datenüberprüfung** – Überprüfe deinen Stammbaum auf unplausible Datumsangaben und andere Datenprobleme
- **Kalender** – Gib Datumsangaben im gregorianischen, julianischen, hebräischen, französisch-republikanischen, persischen, islamischen oder schwedischen Kalender ein
- **Mach es zu deinem eigenen** – Gib deiner Website einen eigenen Namen, eigene Designfarben sowie einen eigenen Text und ein eigenes Bild für die Startseite

## Demo

Um dich bei der Demo anzumelden, verwende eines der folgenden Benutzername-/Passwort-Paare. Jedes steht für eine der Benutzerrollen in Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

Die Demo wird alle zwei Stunden zurückgesetzt, daher sind alle von dir vorgenommenen Änderungen vorübergehend.

[Zur Demo-Anmeldung](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Danke

Die Demo wird freundlicherweise von DigitalOcean unterstützt.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
