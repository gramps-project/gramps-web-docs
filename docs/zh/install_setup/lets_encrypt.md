# 使用 Let's Encrypt 和 Docker Compose 设置 HTTPS

当 Gramps Web 公开提供到互联网时，**必须**使用 HTTPS 加密。

一个特别方便的选项是使用 dockerized Nginx 反向代理，并自动生成 Let's Encrypt 证书。这可以通过这个 [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) 实现。
（[nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) 需要存储在同一目录中，以允许将大媒体文件上传到 Gramps Web。）

请参阅 [acme-companion](https://github.com/nginx-proxy/acme-companion) 文档，以了解如何设置您的域名。
