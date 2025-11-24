# HTTPS:n määrittäminen Let's Encryptin ja Docker Composen avulla

Kun Gramps Web palvelee julkista internetiä, sen **täytyy** käyttää HTTPS-salausta.

Erityisen kätevä vaihtoehto on käyttää dockerisoitua Nginx-käänteistä proxyä, jossa on automaattinen Let's Encrypt -sertifikaatin generointi. Tämä saavutetaan tämän [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) avulla.  
([nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) on tallennettava samaan hakemistoon, jotta suurten mediasisältöjen lataaminen Gramps Webiin on mahdollista.)

Katso [acme-companion](https://github.com/nginx-proxy/acme-companion) -dokumentaatiosta, miten voit määrittää verkkotunnuksesi.
