# Налаштування HTTPS з Let's Encrypt та Docker Compose

Коли Gramps Web надається публічно в інтернеті, він **повинен** використовувати шифрування HTTPS.

Особливо зручним варіантом є використання контейнеризованого зворотного проксі Nginx з автоматизованою генерацією сертифікатів Let's Encrypt. Це досягається за допомогою цього [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(Файл [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) потрібно зберігати в тій же директорії, щоб дозволити завантаження великих медіафайлів до Gramps Web.)

Будь ласка, ознайомтеся з документацією [acme-companion](https://github.com/nginx-proxy/acme-companion) для налаштування вашого домену.
