# Configurando HTTPS com Let's Encrypt e Docker Compose

Quando servido para a internet pública, o Gramps Web **deve** usar criptografia HTTPS.

Uma opção particularmente conveniente é usar um proxy reverso Nginx dockerizado com geração automática de certificados Let's Encrypt. Isso é alcançado com este [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(O [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) precisa ser armazenado no mesmo diretório para permitir o upload de arquivos de mídia grandes para o Gramps Web.)

Por favor, consulte a documentação do [acme-companion](https://github.com/nginx-proxy/acme-companion) para saber como configurar seu domínio.
