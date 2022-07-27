# Setting up HTTPS with Let's Encrypt and Docker Compose

When served to the public internet, Gramps Web **must** use HTTPS encryption.

A particularly convenient option is to use a dockerized Nginx reverse proxy with automated Let's Encrypt certificate generation. This is achieved with the following `docker-compose.yml`:

```yaml
version: "3.7"

services:
  grampsweb:
    image: ghcr.io/gramps-project/grampsweb:latest
    restart: always
    environment:
      VIRTUAL_PORT: "5000"
      VIRTUAL_HOST: ...  # e.g. gramps.mydomain.com
      LETSENCRYPT_HOST: ...   # e.g. gramps.mydomain.com
      LETSENCRYPT_EMAIL: ...  # your email
    volumes:
      - gramps_users:/app/users
      - gramps_index:/app/indexdir
      - gramps_thumb_cache:/app/thumbnail_cache
      - gramps_secret:/app/secret/secret
      - gramps_db:/root/.gramps/grampsdb
      - gramps_media:/app/media
    networks:
      - proxy-tier
      - default

  proxy:
    image: nginxproxy/nginx-proxy
    restart: always
    ports:
      - 80:80
      - 443:443
    environment:
      ENABLE_IPV6: "true"
    volumes:
      - conf:/etc/nginx/conf.d
      - dhparam:/etc/nginx/dhparam
      - certs:/etc/nginx/certs:ro
      - vhost.d:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - /var/run/docker.sock:/tmp/docker.sock:ro
    networks:
      - proxy-tier

  acme-companion:
    image: nginxproxy/acme-companion
    container_name: nginx-proxy-acme
    restart: always
    volumes_from:
      - proxy
    volumes:
      - certs:/etc/nginx/certs:rw
      - acme:/etc/acme.sh
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - proxy-tier
    depends_on:
      - proxy

volumes:
  acme:
  certs:
  conf:
  dhparam:
  vhost.d:
  html:
  gramps_users:
  gramps_index:
  gramps_thumb_cache:
  gramps_secret:
  gramps_db:
  gramps_media:

networks:
  proxy-tier:
```

Please see the [acme-companion](https://github.com/nginx-proxy/acme-companion) docs for how to set up your domain.
