---
hide:
  - navigation
---

Wenn Sie auf Probleme stoßen oder Hilfe mit Gramps Web benötigen, wählen Sie bitte eine der folgenden Optionen aus.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Backend-Probleme :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Frontend-Probleme :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Siehe unten für einige Hinweise, wo Sie zuerst hingehen sollten.

## Fragen stellen

Das offizielle Gramps Discourse-Forum hat eine [separate Kategorie für Gramps Web](https://gramps.discourse.group/c/gramps-web/). Bitte nutzen Sie diese, um Fragen zu Gramps Web zu stellen, zum Beispiel

- Fragen zur Nutzung von Gramps Web
- Fragen zur Konfiguration von Gramps Web
- Fehlersuche bei einer Bereitstellung von Gramps Web
- Ideen zur Verbesserung von Gramps Web
- ...

## Probleme melden

Wenn Sie auf ein Problem stoßen, von dem Sie glauben, dass es ein Fehler in Gramps Web ist, unterstützen Sie es bitte über Github.

Es gibt zwei separate Github-Repositories für den Code, der in Gramps Web verwendet wird, eines für die Benutzeroberfläche („Frontend“) und eines für den Servercode („Backend“):

- [Frontend-Probleme](https://github.com/gramps-project/gramps-web/issues)
- [Backend-Probleme](https://github.com/gramps-project/gramps-web-api/issues)

Wenn Sie sich nicht sicher sind, wo Sie ein Problem melden sollen, machen Sie sich keine Sorgen und wählen Sie einfach eines der beiden – die Maintainer können das Problem bei Bedarf übertragen.

In jedem Fall sollten Sie immer die folgenden Informationen in Ihrem Bericht angeben:

- Details zu Ihrer Konfiguration (z. B. eine docker-compose-Datei mit anonymisierten sensiblen Werten oder ob Sie eine gehostete Version wie Grampshub oder ein vorkonfiguriertes Image wie DigitalOcean verwenden)
- Versionsinformationen. Um diese zu erhalten, gehen Sie zum Tab „Systeminformationen“ auf der Einstellungsseite in Gramps Web und kopieren Sie die Werte aus dem Feld, das ungefähr so aussehen sollte:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: de
multi-tree: false
task queue: true
```

## Verbesserungsvorschläge

Für allgemeine Ideen und Diskussionen über zukünftige Verbesserungen können Sie gerne eine Diskussion im [Forum](https://gramps.discourse.group/c/gramps-web/) eröffnen. Sie möchten möglicherweise auch die Problembereiche (siehe Links oben) überprüfen, ob eine bestimmte Funktion bereits geplant oder in Arbeit ist.

Für spezifische Verbesserungen mit begrenztem Umfang können Sie direkt ein Problem mit einem Funktionswunsch im entsprechenden Frontend- oder Backend-Github-Repository eröffnen.
