---
hide:
  - toc
---

# Gramps Web-Entwicklung: Übersicht

Gramps Web ist eine Webanwendung, die aus zwei Komponenten besteht, die separat entwickelt werden:

- **Gramps Web API** ist eine RESTful API, die in Python geschrieben und auf Flask basiert. Der Quellcode ist unter [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/) gehostet. Sie verwaltet den Datenbankzugriff und genealogische Funktionen direkt unter Verwendung der Gramps Python-Bibliothek. Sie dient als Backend von Gramps Web. Für die Entwicklungsdokumentation siehe [Backend](backend/index.md).
- **Gramps Web Frontend** ist eine Javascript-Webanwendung, die als Frontend für Gramps Web dient. Der Quellcode ist unter [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/) gehostet. Für die Entwicklungsdokumentation siehe [Frontend](frontend/index.md).

Eine Anmerkung zur Versionierung: Gramps Web API und das Gramps Web-Frontend werden unabhängig versioniert. Derzeit hat "Gramps Web" – die kombinierte Anwendung – keine separate Versionsnummer. Beide Projekte halten sich an [SemVer](https://semver.org/).

Wenn Sie kein Python- oder Javascript-Entwickler sind, aber dennoch zu Gramps Web beitragen möchten, schauen Sie sich [Contribute](../contribute/contribute.md) an.
