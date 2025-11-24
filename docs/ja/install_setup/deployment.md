# Gramps WebのDockerによるデプロイ

Gramps Webを自分のサーバー（または仮想サーバー）でホストする最も便利なオプションは、Docker Composeを使用することです。

DockerとDocker Composeがすでにシステムにインストールされていると仮定します。ホストシステムとしてWindows、Mac OS、またはLinuxを使用できます。サポートされているアーキテクチャには、x86-64（デスクトップシステム）だけでなく、Raspberry PiのようなARMシステムも含まれており、低コストでありながら十分に強力なウェブサーバーとして機能します。

!!! note
    サーバーにGrampsをインストールする必要はありません。これはdockerイメージに含まれています。


## ステップ1: Dockerの設定

サーバー上に`docker-compose.yml`という名前の新しいファイルを作成し、以下の内容を挿入します: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml)。

これにより、コンテナを再起動する際にすべての関連データが持続することを保証するために、6つの名前付きボリュームが生成されます。

!!! warning
    上記の設定により、ホストマシンのポート80でAPIが**SSL/TLS保護なし**で利用可能になります。これはローカルテスト用に使用できますが、インターネットに直接公開しないでください。これは完全に安全ではありません！

## ステップ2: SSL/TLSによる安全なアクセス

ウェブAPIは**必ず**HTTPS経由で公開インターネットに提供されなければなりません。いくつかのオプションがあります。例えば、

- SSL/TLSを自動的に含むDockerホスティングを使用する
- Let's Encrypt証明書を使用したNginxリバースプロキシを使用する

前者の設定方法については、[Docker with Let's Encrypt](lets_encrypt.md)を参照してください。

Gramps Webをローカルネットワークのみで使用する予定の場合は、このステップをスキップできます。

## ステップ3: サーバーの起動

次のコマンドを実行します。

```
docker compose up -d
```

初回実行時、アプリは初回ウィザードを表示し、次のことを行うことができます。

- オーナー（管理者）ユーザーのアカウントを作成する
- 必要な設定オプションを設定する
- Gramps XML（`.gramps`）形式の家系図をインポートする

## ステップ4: メディアファイルのアップロード

メディアファイルをアップロードするためのいくつかのオプションがあります。

- Gramps Webと同じサーバーに保存されているファイルを使用する場合、名前付きボリュームの代わりにDockerコンテナにディレクトリをマウントできます。つまり、`gramps_media:/app/media`の代わりに`/home/server_user/gramps_media/:/app/media`を使用し、そこにメディアファイルをアップロードします。
- [S3にホストされているメディアファイル](s3.md)を使用する場合、S3メディアアップローダーアドオンを使用できます。
- おそらく最も便利なオプションは、[Gramps Web Sync](../administration/sync.md)を使用することです。
