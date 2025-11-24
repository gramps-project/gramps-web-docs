---
hide:
  - toc
---

# Sviluppo Web di Gramps: panoramica

Gramps Web è un'applicazione web che consiste in due componenti sviluppati separatamente:

- **Gramps Web API** è un'API RESTful scritta in Python e basata su Flask. Il codice sorgente è ospitato su [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Gestisce l'accesso al database e le funzioni genealogiche sfruttando direttamente la libreria Gramps per Python. Funziona come il backend di Gramps Web. Per la documentazione sullo sviluppo, vedere [Backend](backend/index.md).
- **Gramps Web Frontend** è un'applicazione web Javascript che funge da frontend per Gramps Web. Il codice sorgente è ospitato su [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Per la documentazione sullo sviluppo, vedere [Frontend](frontend/index.md).

Una nota sulla versione: Gramps Web API e il frontend di Gramps Web sono versionati in modo indipendente. Attualmente, "Gramps Web" &ndash; l'applicazione combinata &ndash; non ha un numero di versione separato. Entrambi i progetti seguono [SemVer](https://semver.org/).

Se non sei uno sviluppatore Python o Javascript ma desideri comunque contribuire a Gramps Web, dai un'occhiata a [Contribuire](../contribute/contribute.md).
