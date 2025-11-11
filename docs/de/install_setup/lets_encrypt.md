# Einrichtung von HTTPS mit Let's Encrypt und Docker Compose

Wenn Gramps Web im öffentlichen Internet bereitgestellt wird, **muss** HTTPS-Verschlüsselung verwendet werden.

Eine besonders bequeme Option ist die Verwendung eines dockerisierten Nginx-Reverse-Proxy mit automatisierter Let's Encrypt-Zertifikatserstellung. Dies wird mit dieser [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) erreicht.  
(Die [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) muss im selben Verzeichnis gespeichert werden, um das Hochladen großer Mediendateien zu Gramps Web zu ermöglichen.)

Bitte siehe die [acme-companion](https://github.com/nginx-proxy/acme-companion) Dokumentation, um zu erfahren, wie du deine Domain einrichtest.
