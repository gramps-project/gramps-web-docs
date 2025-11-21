# Let's Encrypt ve Docker Compose ile HTTPS Kurulumu

Halka açık internete sunulduğunda, Gramps Web **mutlaka** HTTPS şifrelemesi kullanmalıdır.

Özellikle kullanışlı bir seçenek, otomatik Let's Encrypt sertifika üretimi ile dockerize edilmiş bir Nginx ters proxy kullanmaktır. Bu, bu [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) ile sağlanmaktadır.
([nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) büyük medya dosyalarını Gramps Web'e yüklemeye izin vermek için aynı dizinde saklanmalıdır.)

Alan adınızı nasıl kuracağınız hakkında daha fazla bilgi için lütfen [acme-companion](https://github.com/nginx-proxy/acme-companion) belgelerine bakın.
