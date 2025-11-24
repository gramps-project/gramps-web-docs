# Update Gramps Web

Wenn Sie eine der Installationsmethoden basierend auf Docker Compose verwenden, ist das Aktualisieren von Gramps Web auf die neueste Version einfach. Führen Sie im Ordner, in dem sich Ihre `docker-compose.yml` befindet, die folgenden Befehle aus

```bash
docker compose pull
docker compose up -d
```

Für kleinere Versionssprünge der [Gramps Web API](https://github.com/gramps-project/gramps-web-api) ist dies alles, was benötigt wird. Beachten Sie jedoch die [Versionshinweise der Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), da es möglicherweise Breaking Changes gibt, die zusätzliche Aufmerksamkeit oder Konfigurationsänderungen erfordern.

Bitte beachten Sie, dass das Standard-Docker-Image `grampsweb:latest` immer die neueste Version der API mit der neuesten Version des Frontends kombiniert. Wenn Sie die beiden Komponenten separat aktualisieren möchten - was möglich ist - ist eine aufwendigere Einrichtung als hier beschrieben erforderlich.
