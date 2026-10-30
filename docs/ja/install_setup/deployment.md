# Gramps WebのDockerによるデプロイ

Gramps Webを自分のサーバー（または仮想サーバー）でホストする最も便利な方法は、Docker Composeを使用することです。

DockerとDocker Composeがすでにシステムにインストールされていると仮定します。ホストシステムとしてWindows、Mac OS、またはLinuxを使用できます。サポートされているアーキテクチャには、x86-64（デスクトップシステム）だけでなく、Raspberry PiのようなARMシステムも含まれており、これは低コストでありながら（十分に）強力なWebサーバーとして機能します。

!!! note
    サーバーにGrampsをインストールする必要はありません。これはDockerイメージに含まれています。


## ステップ1: Dockerの設定

サーバーに`docker-compose.yml`という名前の新しいファイルを作成し、以下の内容を挿入します: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml)。

これにより、コンテナを再起動してもすべての関連データが保持されるように、6つの名前付きボリュームが生成されます。

`GRAMPSWEB_BASE_URL`をGramps Webにアクセスするアドレスに設定します。例: `https://gramps.mydomain.com`。これは、パスワードリセットなどのメール内のリンクを構築するために使用されます。メールを送信するために、[設定](configuration.md)で説明されているメール設定も追加してください。

!!! warning
    上記の設定により、APIがホストマシンのポート80で**SSL/TLS保護なし**で利用可能になります。これはローカルテストには使用できますが、インターネットに直接公開しないでください。完全に安全ではありません！

## ステップ2: SSL/TLSでの安全なアクセス

Web APIは**必ず**HTTPS経由で公開インターネットに提供されなければなりません。いくつかのオプションがあります。例えば、

- SSL/TLSを自動的に含むDockerホスティングを使用する
- Let's Encrypt証明書を使用したNginxリバースプロキシを使用する

前者の設定方法については、[Let's Encryptを使用したDocker](lets_encrypt.md)を参照してください。

Gramps Webをローカルネットワークでのみ使用する予定の場合、このステップはスキップできます。

## ステップ3: サーバーの起動

次のコマンドを実行します。

```
docker compose up -d
```

初回実行時、アプリは初回ウィザードを表示し、以下の操作を行うことができます。

- オーナー（管理者）ユーザーのアカウントを作成する
- Gramps XML（`.gramps`）形式の家系図をインポートする

## ステップ4: メディアファイルのアップロード

メディアファイルをアップロードするためのいくつかのオプションがあります。

- Gramps Webと同じサーバーに保存されているファイルを使用する場合、名前付きボリュームの代わりにDockerコンテナにディレクトリをマウントできます。つまり、`gramps_media:/app/media`の代わりに`/home/server_user/gramps_media/:/app/media`を使用し、そこにメディアファイルをアップロードします。
- [S3にホストされたメディアファイル](s3.md)を使用する場合、S3メディアアップローダーアドオンを使用できます。
- おそらく最も便利なオプションは、[Gramps Web Sync](../administration/sync.md)を使用することです。
