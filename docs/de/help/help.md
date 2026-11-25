---
hide:
  - navigation
---

Wenn du auf Probleme stößt oder Hilfe bei Gramps Web benötigst, wähle bitte eine der folgenden Optionen.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Probleme im Backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Probleme im Frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Weiter unten findest du Hinweise dazu, wohin du dich zuerst wenden solltest.

## Fragen stellen

Das offizielle Gramps-Discourse-Forum hat eine [eigene Kategorie für Gramps Web](https://gramps.discourse.group/c/gramps-web/). Bitte nutze sie, um Fragen zu Gramps Web zu stellen, zum Beispiel

- Fragen zur Nutzung von Gramps Web
- Fragen zur Konfiguration von Gramps Web
- Fehlerbehebung bei einer Bereitstellung von Gramps Web
- Ideen für Verbesserungen von Gramps Web
- ...

## Probleme melden

Wenn du auf ein Problem stößt, bei dem es sich deiner Meinung nach um einen Fehler in Gramps Web handelt, melde es bitte über GitHub.

Für den in Gramps Web verwendeten Code gibt es zwei separate GitHub-Repositorys: eines für die Benutzeroberfläche („Frontend“) und eines für den Servercode („Backend“):

- [Probleme im Frontend](https://github.com/gramps-project/gramps-web/issues)
- [Probleme im Backend](https://github.com/gramps-project/gramps-web-api/issues)


Wenn du unsicher bist, wo du ein Problem melden solltest, mach dir keine Sorgen und wähle einfach eines der beiden aus – die Maintainer können das Problem bei Bedarf verschieben.

Füge deinem Bericht in jedem Fall immer die folgenden Informationen hinzu:

- Details zu deiner Einrichtung (z. B. eine docker-compose-Datei, bei der vertrauliche Werte unkenntlich gemacht wurden, oder ob du eine gehostete Version wie Grampshub oder ein vorkonfiguriertes Image wie DigitalOcean verwendest)
- Versionsinformationen. Um sie abzurufen, gehe in Gramps Web auf der Einstellungsseite zum Tab „Systeminformationen“ und kopiere die Werte aus dem Feld. Sie sollten ungefähr so aussehen:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Verbesserungen vorschlagen

Für allgemeine Ideen und Diskussionen über zukünftige Verbesserungen kannst du gerne eine Diskussion im [Forum](https://gramps.discourse.group/c/gramps-web/) eröffnen. Du kannst auch die Problemseiten prüfen (siehe Links oben), um herauszufinden, ob eine bestimmte Funktion bereits geplant ist oder daran gearbeitet wird.

Für konkrete Verbesserungen mit begrenztem Umfang kannst du gerne direkt ein Problem mit einem Funktionswunsch im entsprechenden GitHub-Repository für das Frontend oder Backend eröffnen.
