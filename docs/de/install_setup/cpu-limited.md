# Begrenzung der CPU- und Speichernutzung

In der empfohlenen docker-basierten Einrichtung verwendet Gramps Web [Gunicorn](https://gunicorn.org/), um das
Backend bereitzustellen, und [Celery](https://docs.celeryq.dev) für Hintergrundaufgaben. In beiden Fällen können mehrere Worker-Prozesse parallel ausgeführt werden, was die Anwendung aus Sicht des Benutzers reaktionsschneller macht. Allerdings erhöht sich die Menge des verwendeten RAM, wenn die Anzahl der Worker steigt (auch wenn die Anwendung im Leerlauf ist), und das gleichzeitige Verarbeiten von Anfragen kann zu einer hohen CPU-Auslastung führen (insbesondere wenn viele Benutzer die Anwendung gleichzeitig nutzen). Sowohl Gunicorn als auch Celery ermöglichen es, die Anzahl der parallelen Worker zu begrenzen.

## Informationen über Ihr System abrufen

Unter Linux können Sie die Anzahl der verfügbaren Kerne auf Ihrem System mit dem folgenden Befehl überprüfen:

```bash
lscpu | grep CPU
```

Um zu sehen, wie viel Speicher und Swap-Speicher Ihnen zur Verfügung steht, verwenden Sie

```bash
free -h
```


## Begrenzung der Anzahl der Gunicorn-Worker

Der einfachste Weg, die Anzahl der Gunicorn-Worker beim Verwenden des Standard-Gramps-Web-Docker-Images festzulegen, besteht darin, die Umgebungsvariable `GUNICORN_NUM_WORKERS` zu setzen, z. B. indem Sie sie in der `docker-compose.yml`-Datei unter "environment" deklarieren.

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Siehe [die Gunicorn-Dokumentation](https://docs.gunicorn.org/en/stable/design.html#how-many-workers), um die ideale Anzahl von Workern zu bestimmen.



## Begrenzung der Anzahl der Celery-Worker

Um die Anzahl der Celery-Worker festzulegen, passen Sie die `concurrency`-Einstellung in der Docker-Compose-Datei an:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Siehe [die Celery-Dokumentation](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency), um die ideale Anzahl von Workern zu bestimmen.

!!! info
    Wenn das `concurrency`-Flag weggelassen wird (was bis zur Version 2.5.0 in der Gramps-Web-Dokumentation der Fall war), wird es standardmäßig auf die Anzahl der verfügbaren CPU-Kerne im System gesetzt, was einen erheblichen Speicherverbrauch zur Folge haben kann.
