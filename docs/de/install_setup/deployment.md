# Gramps Web mit Docker bereitstellen

Die bequemste Möglichkeit, Gramps Web auf deinem eigenen Server (oder virtuellen Server) zu hosten, ist Docker Compose.

Wir gehen davon aus, dass Docker und Docker Compose bereits auf deinem System installiert sind. Du kannst Windows, Mac OS oder Linux als Hostsystem verwenden. Zu den unterstützten Architekturen gehören nicht nur x86-64 (Desktop-Systeme), sondern auch ARM-Systeme wie ein Raspberry Pi, der als kostengünstiger, aber dennoch ausreichend leistungsfähiger Webserver dienen kann.

!!! note
    Du musst Gramps nicht auf dem Server installieren, da es im Docker-Image enthalten ist.


## Schritt 1: Docker-Konfiguration

Erstelle auf dem Server eine neue Datei mit dem Namen `docker-compose.yml` und füge den folgenden Inhalt ein: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).



Dadurch werden sechs benannte Volumes erstellt, um sicherzustellen, dass alle relevanten Daten beim Neustart des Containers erhalten bleiben.

Setze `GRAMPSWEB_BASE_URL` auf die Adresse, unter der Gramps Web erreichbar sein wird, z. B. `https://gramps.mydomain.com`. Diese wird verwendet, um Links in E-Mails zu erstellen, beispielsweise für das Zurücksetzen von Passwörtern. Um E-Mails zu versenden, füge außerdem die in der [Konfiguration](configuration.md) beschriebenen E-Mail-Einstellungen hinzu.

!!! warning
    Dadurch wird die API an Port 80 des Hostcomputers **ohne SSL/TLS-Schutz** verfügbar gemacht. Du kannst dies für lokale Tests verwenden, darfst die API jedoch nicht direkt dem Internet aussetzen, da dies vollkommen unsicher ist!

## Schritt 2: Zugriff mit SSL/TLS absichern

Die Web-API **muss** über HTTPS für das öffentliche Internet bereitgestellt werden. Dafür gibt es mehrere Möglichkeiten, z. B.

- Verwendung eines Docker-Hostings, das SSL/TLS automatisch beinhaltet
- Verwendung eines Nginx-Reverse-Proxys mit einem Let's-Encrypt-Zertifikat

Eine Anleitung zur Einrichtung der ersten Möglichkeit findest du unter [Docker mit Let's Encrypt](lets_encrypt.md).

Wenn du Gramps Web nur in deinem lokalen Netzwerk verwenden möchtest, kannst du diesen Schritt überspringen.

## Schritt 3: Server starten

Führe Folgendes aus:

```
docker compose up -d
```

Beim ersten Start zeigt die App einen Assistenten für die Ersteinrichtung an, mit dem du

- ein Konto für den Besitzer (Administrator) erstellen kannst
- einen Familienstammbaum im Gramps-XML-Format (`.gramps`) importieren kannst

## Schritt 4: Mediendateien hochladen

Für das Hochladen von Mediendateien gibt es mehrere Möglichkeiten.

- Wenn du Dateien verwendest, die auf demselben Server wie Gramps Web gespeichert sind, kannst du ein Verzeichnis in den Docker-Container einbinden, anstatt ein benanntes Volume zu verwenden, also `/home/server_user/gramps_media/:/app/media` anstelle von `gramps_media:/app/media`, und deine Mediendateien dort hochladen.
- Wenn du Mediendateien [auf S3 gehostet](s3.md) verwendest, kannst du das S3 Media Uploader Addon verwenden.
- Die vermutlich bequemste Möglichkeit ist die Verwendung von [Gramps Web Sync](../administration/sync.md).
