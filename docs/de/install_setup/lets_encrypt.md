# Einrichten von HTTPS mit Let's Encrypt und Docker Compose

Wenn Gramps Web im öffentlichen Internet bereitgestellt wird, **muss** HTTPS-Verschlüsselung verwendet werden.

Eine besonders praktische Option ist die Verwendung eines containerisierten Nginx-Reverse-Proxys mit automatisierter Generierung von Let's-Encrypt-Zertifikaten. Dies wird mit dieser [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) erreicht.
Die Datei [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) muss im selben Verzeichnis gespeichert werden, damit das Hochladen großer Mediendateien in Gramps Web möglich ist.

Informationen zum Einrichten deiner Domain findest du in der Dokumentation zu [acme-companion](https://github.com/nginx-proxy/acme-companion).
