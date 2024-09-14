# Setting up HTTPS with Let's Encrypt and Docker Compose

When served to the public internet, Gramps Web **must** use HTTPS encryption.

A particularly convenient option is to use a dockerized Nginx reverse proxy with automated Let's Encrypt certificate generation. This is achieved with this [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(The [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) needs to be stored in the same directory to allow uploading large media files to Gramps Web.)

Please see the [acme-companion](https://github.com/nginx-proxy/acme-companion) docs for how to set up your domain.
