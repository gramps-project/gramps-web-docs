# Configurazione di HTTPS con Let's Encrypt e Docker Compose

Quando viene servito al pubblico su Internet, Gramps Web **deve** utilizzare la crittografia HTTPS.

Un'opzione particolarmente conveniente è utilizzare un proxy inverso Nginx dockerizzato con generazione automatizzata di certificati Let's Encrypt. Questo si ottiene con questo [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
Il file [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) deve essere memorizzato nella stessa directory per consentire il caricamento di file multimediali di grandi dimensioni su Gramps Web.

Si prega di consultare la documentazione di [acme-companion](https://github.com/nginx-proxy/acme-companion) per informazioni su come configurare il proprio dominio.
