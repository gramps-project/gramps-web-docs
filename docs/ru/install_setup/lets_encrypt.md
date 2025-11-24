# Настройка HTTPS с Let's Encrypt и Docker Compose

Когда Gramps Web предоставляется в публичный интернет, он **должен** использовать шифрование HTTPS.

Особенно удобным вариантом является использование контейнерного обратного прокси Nginx с автоматической генерацией сертификатов Let's Encrypt. Это достигается с помощью этого [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(Файл [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) необходимо сохранить в той же директории, чтобы позволить загружать большие медиафайлы в Gramps Web.)

Пожалуйста, ознакомьтесь с документацией [acme-companion](https://github.com/nginx-proxy/acme-companion) для настройки вашего домена.
