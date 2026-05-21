# Setting up HTTPS with Traefik [sic] and (Implicty an SSL certificate)

When served to the public internet, Gramps Web **must** use HTTPS encryption.

HTTPS (requiring an SLL certificate: issued by a commercial provider or self-issued).

Prequisites:

1. An HTTP URL resolved by by browser (i.e. http://my.domain.eg) (that's a subdomain there) must NOT return a 404 error.
    --WAIT: If http://my.domain.eg does not match your IP in ping and your IP record in your host provider, AND other web-based lookup tools, you have to wait.

1b. After tou your IP can be resolved by reasonably creditiable DNS lookup tools, see Step 2.

2. For HTTPS, you need a commerically-signed certificate (money) or avself-issued certificate for my.domain.org.
 2b.-1: traefik will attempt to assign a self signed certificate so, no money).

Foe example (https://github.com/mpfl)

services:
  grampsweb: &grampsweb
    image: ghcr.io/gramps-project/grampsweb:latest
    restart: always
    ports:
      - "8200:5000"  # host:docker
    environment:
      GRAMPSWEB_TREE: "Gramps Web"  # will create a new tree if not exists
      GRAMPSWEB_CELERY_CONFIG__broker_url: "redis://grampsweb_redis:6379/0"
      GRAMPSWEB_CELERY_CONFIG__result_backend: "redis://grampsweb_redis:6379/0"
      GRAMPSWEB_RATELIMIT_STORAGE_URI: redis://grampsweb_redis:6379/1
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.grampsweb.entrypoints=http"
      - "traefik.http.routers.grampsweb.rule=Host(`***.de`)"
      - "traefik.http.middlewares.grampsweb-https-redirect.redirectscheme.scheme=https"
      - "traefik.http.routers.grampsweb.middlewares=grampsweb-https-redirect"
      - "traefik.http.routers.grampsweb-secure.entrypoints=https"
      - "traefik.http.routers.grampsweb-secure.rule=Host(`***.de`)"
      - "traefik.http.routers.grampsweb-secure.tls=true"
      - "traefik.http.routers.grampsweb-secure.service=grampsweb"
      - "traefik.http.services.grampsweb.loadbalancer.server.port=8200"
      - "traefik.docker.network=traefik_proxy"
      #- "com.centurylinklabs.watchtower.monitor-only=true"
    depends_on:
      - grampsweb_redis
    volumes:
      - gramps_users:/app/users  # persist user database
      - gramps_index:/app/indexdir  # persist search index
      - gramps_thumb_cache:/app/thumbnail_cache  # persist thumbnails
      - gramps_cache:/app/cache  # persist export and report caches
      - gramps_secret:/app/secret  # persist flask secret
      - gramps_db:/root/.gramps/grampsdb  # persist Gramps database
      - gramps_media:/app/media  # persist media files
      - gramps_tmp:/tmp
    networks:
      - traefik_proxy

  grampsweb_celery:
    <<: *grampsweb  # YAML merge key copying the entire grampsweb service config
    ports: []
    container_name: grampsweb_celery
    depends_on:
      - grampsweb_redis
    command: celery -A gramps_webapi.celery worker --loglevel=INFO
    networks:
      - traefik_proxy

  grampsweb_redis:
    image: redis:alpine
    container_name: grampsweb_redis
    restart: always
    networks:
      - traefik_proxy

volumes:
  gramps_users:
  gramps_index:
  gramps_thumb_cache:
  gramps_cache:
  gramps_secret:
  gramps_db:
  gramps_media:
    driver: local
    driver_opts:
      type: "nfs"
      o: "nfsvers=4,addr=10.10.10.40,rw"
      device: ":/volume1/docker-volumes/gramps-web"
  gramps_tmp:

networks:
  traefik_proxy:
    external: true