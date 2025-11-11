# Bereitstellung von Gramps Web mit Docker

Die bequemste Option, Gramps Web auf Ihrem eigenen Server (oder virtuellen Server) zu hosten, ist mit Docker Compose.

Wir gehen davon aus, dass Docker und Docker Compose bereits auf Ihrem System installiert sind. Sie können Windows, Mac OS oder Linux als Host-System verwenden. Die unterstützten Architekturen umfassen nicht nur x86-64 (Desktop-Systeme), sondern auch ARM-Systeme wie einen Raspberry Pi, der als kostengünstiger, aber leistungsfähiger (genug) Webserver dienen kann.

!!! note
    Sie müssen Gramps nicht auf dem Server installieren, da es im Docker-Image enthalten ist.


## Schritt 1: Docker-Konfiguration

Erstellen Sie eine neue Datei auf dem Server mit dem Namen `docker-compose.yml` und fügen Sie die folgenden Inhalte ein: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Dies wird sechs benannte Volumes generieren, um sicherzustellen, dass alle relevanten Daten beim Neustart des Containers erhalten bleiben.

!!! warning
    Das oben Genannte macht die API auf Port 80 der Hostmaschine **ohne SSL/TLS-Schutz** verfügbar. Sie können dies für lokale Tests verwenden, aber setzen Sie dies nicht direkt dem Internet aus, es ist völlig unsicher!

## Schritt 2: Sicheren Zugriff mit SSL/TLS

Die Web-API **muss** über HTTPS für das öffentliche Internet bereitgestellt werden. Es gibt mehrere Optionen, z.B.

- Verwendung von Docker-Hosting, das SSL/TLS automatisch einschließt
- Verwendung eines Nginx Reverse Proxy mit einem Let's Encrypt-Zertifikat

Siehe [Docker mit Let's Encrypt](lets_encrypt.md) für Informationen zur Einrichtung der ersteren.

Wenn Sie planen, Gramps Web nur in Ihrem lokalen Netzwerk zu verwenden, können Sie diesen Schritt überspringen.

## Schritt 3: Server starten

Führen Sie aus

```
docker compose up -d
```

Beim ersten Start zeigt die App einen Einrichtungsassistenten an, der es Ihnen ermöglicht,

- Ein Konto für den Eigentümer (Admin) Benutzer zu erstellen
- Einige notwendige Konfigurationsoptionen festzulegen
- Ein Familienstammbaum im Gramps XML (`.gramps`) Format zu importieren

## Schritt 4: Mediendateien hochladen

Es gibt mehrere Optionen zum Hochladen von Mediendateien.

- Wenn Sie Dateien verwenden, die auf demselben Server wie Gramps Web gespeichert sind, können Sie ein Verzeichnis in den Docker-Container einbinden, anstatt ein benanntes Volume zu verwenden, d.h. `/home/server_user/gramps_media/:/app/media` anstelle von `gramps_media:/app/media`, und Ihre Mediendateien dort hochladen.
- Wenn Sie Mediendateien [auf S3 gehostet](s3.md) verwenden, können Sie das S3 Media Uploader Addon verwenden.
- Die wohl bequemste Option ist die Verwendung von [Gramps Web Sync](../administration/sync.md).
