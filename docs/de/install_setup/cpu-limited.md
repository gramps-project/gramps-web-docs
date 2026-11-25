# CPU- und Speichernutzung begrenzen

Im empfohlenen Docker-basierten Setup verwendet Gramps Web [Gunicorn](https://gunicorn.org/), um das
Backend bereitzustellen, und [Celery](https://docs.celeryq.dev) für Hintergrundaufgaben. In beiden Fällen können mehrere
Worker-Prozesse parallel ausgeführt werden, wodurch die Anwendung aus Sicht der Benutzer reaktionsschneller wird.
Eine Erhöhung der Anzahl der Worker erhöht jedoch auch die Menge des verwendeten Arbeitsspeichers (selbst wenn die Anwendung
inaktiv ist), und die parallele Verarbeitung von Anfragen kann zu einer hohen CPU-Auslastung führen (insbesondere wenn viele Benutzer
die Anwendung gleichzeitig verwenden). Sowohl Gunicorn als auch Celery ermöglichen es, die Anzahl der parallelen Worker zu begrenzen.

## Informationen über dein System abrufen

Unter Linux kannst du die Anzahl der auf deinem System verfügbaren Kerne mit dem folgenden Befehl überprüfen:

```bash
lscpu | grep CPU
```

Um zu sehen, wie viel Arbeitsspeicher und Swap-Speicher dir zur Verfügung stehen, verwende

```bash
free -h
```


## Anzahl der Gunicorn-Worker begrenzen

Am einfachsten lässt sich die Anzahl der Gunicorn-Worker bei Verwendung des standardmäßigen Gramps-Web-
Docker-Images festlegen, indem du die Umgebungsvariable `GUNICORN_NUM_WORKERS` setzt, z. B. indem du sie
in der Datei `docker-compose.yml` unter „environment“ definierst.

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Siehe [die Gunicorn-Dokumentation](https://docs.gunicorn.org/en/stable/design.html#how-many-workers), um die
ideale Anzahl der Worker festzulegen.

!!! info
    Das Docker-Image startet Gunicorn mit der Option `--preload`, sodass die Worker den Speicher der geladenen Anwendung gemeinsam nutzen und jeder zusätzliche Worker weniger Speicher benötigt. Wenn du den Gunicorn-Befehl überschreibst, behalte `--preload` bei, um davon zu profitieren.



## Anzahl der Celery-Worker begrenzen

Um die Anzahl der Celery-Worker festzulegen, passe die Einstellung `concurrency` in der Docker-Compose-Datei an:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Siehe [die Celery-Dokumentation](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency), um die
ideale Anzahl der Worker festzulegen.

!!! info
    Wenn das Flag `concurrency` weggelassen wird (was bis v2.5.0 in der Gramps-Web-Dokumentation der Fall war), wird
    standardmäßig die Anzahl der auf dem System verfügbaren CPU-Kerne verwendet, was eine beträchtliche Menge an Speicher verbrauchen kann.
