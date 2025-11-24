# Opsætning af HTTPS med Let's Encrypt og Docker Compose

Når Gramps Web serveres til det offentlige internet, **skal** det bruge HTTPS-kryptering.

En særlig bekvem mulighed er at bruge en dockeriseret Nginx reverse proxy med automatisk generering af Let's Encrypt-certifikater. Dette opnås med denne [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(Filen [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) skal gemmes i den samme mappe for at tillade upload af store mediefiler til Gramps Web.)

Se venligst dokumentationen for [acme-companion](https://github.com/nginx-proxy/acme-companion) for hvordan du opsætter dit domæne.
