---
hide:
  - toc
---

# Gramps-Web-Entwicklung: Übersicht

Gramps Web ist eine Webanwendung, die aus zwei Komponenten besteht, die unabhängig voneinander entwickelt werden:

- **Gramps Web API** ist eine in Python geschriebene RESTful-API, die auf Flask basiert. Der Quellcode wird unter [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/) gehostet. Sie verwaltet den Datenbankzugriff und genealogische Funktionen direkt unter Verwendung der Gramps-Python-Bibliothek. Sie dient als Backend von Gramps Web. Die Entwicklungsdokumentation findest du unter [Backend](backend/index.md).
- **Gramps Web Frontend** ist eine JavaScript-Webanwendung, die als Frontend für Gramps Web dient. Der Quellcode wird unter [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/) gehostet. Die Entwicklungsdokumentation findest du unter [Frontend](frontend/index.md).

Ein Hinweis zur Versionierung: Die Gramps Web API und das Gramps Web Frontend werden unabhängig voneinander versioniert. Derzeit hat „Gramps Web“ &ndash; die kombinierte Anwendung &ndash; keine eigene Versionsnummer. Beide Projekte halten sich an [SemVer](https://semver.org/).

Wenn du kein Python- oder JavaScript-Entwickler bist, aber trotzdem zu Gramps Web beitragen möchtest, sieh dir [Beitragen](../contribute/contribute.md) an.

Übersetztes Dokument auf Deutsch:
