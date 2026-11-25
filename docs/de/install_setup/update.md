# Gramps Web aktualisieren

Wenn du eine der auf Docker Compose basierenden Installationsmethoden verwendest, ist das Aktualisieren von Gramps Web auf die neueste Version einfach. Führe in dem Ordner, in dem sich deine `docker-compose.yml` befindet, die folgenden Befehle aus:

```bash
docker compose pull
docker compose up -d
```

Bei Sprüngen zwischen kleineren Versionen der [Gramps Web API](https://github.com/gramps-project/gramps-web-api) ist dies alles, was erforderlich ist. Beachte jedoch die [Versionshinweise der Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), da es möglicherweise inkompatible Änderungen gibt, die zusätzliche Aufmerksamkeit oder Konfigurationsänderungen erfordern.

Beachte, dass das standardmäßige Docker-Image `grampsweb:latest` immer die neueste Version der API mit der neuesten Version des Frontends kombiniert. Wenn du die beiden Komponenten getrennt aktualisieren möchtest – was möglich ist –, ist eine aufwendigere Einrichtung als hier beschrieben erforderlich.
