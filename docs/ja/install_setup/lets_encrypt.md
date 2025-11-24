# Let's Encrypt と Docker Compose を使用した HTTPS の設定

公開インターネットに提供される場合、Gramps Web **は** HTTPS 暗号化を使用する必要があります。

特に便利なオプションは、Docker 化された Nginx リバースプロキシを使用して、自動的に Let's Encrypt 証明書を生成することです。これは、この [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml) を使用して実現されます。
（[nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) は、大きなメディアファイルを Gramps Web にアップロードできるようにするために、同じディレクトリに保存する必要があります。）

ドメインの設定方法については、[acme-companion](https://github.com/nginx-proxy/acme-companion) のドキュメントを参照してください。
