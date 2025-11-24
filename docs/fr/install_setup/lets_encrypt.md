# Configuration de HTTPS avec Let's Encrypt et Docker Compose

Lorsqu'il est servi sur Internet public, Gramps Web **doit** utiliser le chiffrement HTTPS.

Une option particulièrement pratique est d'utiliser un proxy inverse Nginx dockerisé avec génération automatique de certificats Let's Encrypt. Cela est réalisé avec ce [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(Le [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) doit être stocké dans le même répertoire pour permettre le téléchargement de fichiers multimédias volumineux sur Gramps Web.)

Veuillez consulter la documentation de l'[acme-companion](https://github.com/nginx-proxy/acme-companion) pour savoir comment configurer votre domaine.
