# Configuración de HTTPS con Let's Encrypt y Docker Compose

Cuando se sirve a Internet público, Gramps Web **debe** usar cifrado HTTPS.

Una opción particularmente conveniente es utilizar un proxy inverso Nginx dockerizado con generación automática de certificados Let's Encrypt. Esto se logra con este [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(El [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) debe almacenarse en el mismo directorio para permitir la carga de archivos multimedia grandes en Gramps Web.)

Por favor, consulta la documentación de [acme-companion](https://github.com/nginx-proxy/acme-companion) para saber cómo configurar tu dominio.
