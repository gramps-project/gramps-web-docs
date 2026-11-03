# PostgreSQLデータベースの使用

デフォルトでは、Gramps Webは各家系図を独自のSQLiteデータベースファイルに保存します。これには追加のサービスは必要なく、バックアップはファイルをコピーするだけで簡単に行え、ほとんどのインストールに適しており、[複数の木をホストする](multi-tree.md)場合にも対応しています。

代わりに、SharedPostgreSQLアドオンを使用して家系図をPostgreSQLサーバーにホストすることもできます。これにより、すべての木が単一のデータベースに保存されます。すでにPostgreSQLサーバーを運用していて、そこでバックアップや監視を管理したい場合や、多くのユーザーが同時に編集することを期待する場合には、この方法が適しています。PostgreSQLは、家系図が保存されている場所に関係なく、[ユーザーデータベース](#using-a-postgresql-database-for-the-user-database)や[検索インデックス](#using-a-postgresql-database-for-the-search-index)もホストできます。

!!! warning "PostgreSQLアドオンの非推奨"
    単一の家系図をデータベースごとに保存する古いPostgreSQLアドオンは、Gramps Web API 3.24以降非推奨となり、Gramps Web API 4.0ではサポートされなくなります。これは、複数の木をホストすることがそのバージョンのデフォルトとなるためです。これを使用している場合は、[PostgreSQLアドオンからSharedPostgreSQLへの木の移動](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql)を参照してください。

## PostgreSQLサーバーの設定

最も簡単なオプションは、Docker Composeを使用してGramps Webと同じDockerホスト上のコンテナでPostgreSQLサーバーを実行することです。

Grampsは、異なる言語でオブジェクトを正しくソートするためにPostgreSQLサーバーにロケールがインストールされている必要があり、デフォルトのPostgreSQLイメージにはそれが含まれていません。[`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/)イメージはそれを追加します。これを使用するには、`docker-compose.yml`に以下のセクションを追加します：
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
また、このYAMLファイルの`volumes:`セクションの下に`postgres_data:`をキーとして追加します。このイメージには、各自のユーザーとパスワードを持つ2つのデータベースが含まれています：系譜データ用の`gramps`と、Gramps Webユーザーデータベース用の`grampswebuser`です。

代わりに独自のPostgreSQLサーバーを使用する場合は、設定されたユーザーがテーブルを作成できる`gramps`という名前のデータベースを作成し、ユーザーが必要とするロケールがインストールされていることを確認してください。

## Gramps Webの設定

新しい家系図は、Gramps Webが[マルチツリー モード](multi-tree.md)で実行され、`NEW_DB_BACKEND`設定オプションが`sharedpostgresql`に設定されていると、SharedPostgreSQLデータベースに作成されます。上記のDocker Composeセットアップを使用して、`docker-compose.yml`の`grampsweb`サービスの`environment:`キーの下に以下を追加します：

```yaml
      # マルチツリー モードを有効にする
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # SharedPostgreSQLデータベースに新しい木を作成する
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQLサーバーのホストとポート。ホストは上記のPostgreSQLサービスの名前です
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # 認証情報はPostgreSQLコンテナで使用されるものと一致する必要があります
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

これらのオプションの説明については、[設定](configuration.md)を参照してください。ホストとポートは、木が作成されるときに各木と共に保存されるため、後で変更しても新しい木にのみ影響します。

## 木の作成とデータのインポート

新しい木を作成するには、[複数の木をホストするためのセットアップ](multi-tree.md#create-a-new-tree)で説明されているように、`/trees/`エンドポイントにPOSTします。レスポンスには新しい木のIDが含まれており、それが[木の所有者アカウントを作成する](../administration/owner.md#multi-tree-setup-create-tree-owner-account)のに必要です。

木の所有者がログインすると、ウェブインターフェースを介して既存の家系図（例：Gramps DesktopからエクスポートされたGramps XMLファイル）を[インポート](../administration/import.md)できます。

## ユーザーデータベースのためのPostgreSQLデータベースの使用

ユーザーデータベースは通常、家系図がホストされている場所に関係なくSQLiteファイルです。代わりにPostgreSQLを使用するには、`USER_DB_URI`設定オプションをPostgreSQLデータベースのURLに設定します。上記の`gramps-postgres`イメージを使用する場合は、その`grampswebuser`データベースを使用します：
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 検索インデックスのためのPostgreSQLデータベースの使用

検索インデックスもデフォルトではSQLiteに保存されます。代わりにPostgreSQLを使用するには、`SEARCH_INDEX_DB_URI`設定オプションをPostgreSQLデータベースのURLに設定します。上記の`gramps-postgres`イメージを使用する場合、家系図がそこにホストされているかどうかに関係なく、その`gramps`データベースを使用できます：
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

検索インデックスにはPostgreSQL 12以降が必要です。

## PostgreSQLアドオンからSharedPostgreSQLへの木の移動

古いインストールでは、単一の木をデータベースごとに保存するPostgreSQLアドオンで家系図をホストしている場合があります。木がどのアドオンを使用しているかを確認するには、Grampsデータベースディレクトリの木のサブディレクトリにある`database.txt`ファイルを見てください。非推奨のPostgreSQLアドオンの場合は`postgresql`、SharedPostgreSQLの場合は`sharedpostgresql`が含まれています。

同じインストール内でPostgreSQLアドオンからSharedPostgreSQLに木を移動するには、ユーザーアカウントとメディアファイルを保持しながら、次の手順を実行します：

1. [家系図をバックアップ](../administration/export.md#back-up-your-family-tree)としてGramps XML（`.gramps`）ファイルに保存します。プライベートレコードを表示できるアカウントを使用してください。
2. [Gramps Webの設定](#configuring-gramps-web)で説明されているように、設定を変更します。既存の`gramps-postgres`コンテナを引き続き使用できます。
3. [新しい木を作成](multi-tree.md#create-a-new-tree)し、その木のIDをメモします。
4. [既存のユーザーデータベースを移行](multi-tree.md#migrate-existing-user-database)で説明されているように、既存のユーザーアカウントを新しい木に割り当てます。
5. [既存のメディアファイルを移行](multi-tree.md#migrate-existing-media-files)で説明されているように、新しい木に期待される場所にメディアファイルを移動します。
6. ログインし、Gramps XMLファイルを新しい木に[インポート](../administration/import.md)します。

新しい木が完全であることを確認するまで、Gramps XMLファイルを保持してください。

別のGramps Webインストールに移動する場合は、[別のGramps Webインスタンスへの移動](../administration/export.md#move-to-a-different-gramps-web-instance)の手順に従ってください。

## 問題

問題が発生した場合は、Gramps WebとPostgreSQLサーバーのログ出力を監視してください。Dockerの場合、以下のコマンドで実行できます：

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Gramps Web（またはドキュメント）に問題があると思われる場合は、[Github](https://github.com/gramps-project/gramps-web-api/issues)に問題を報告してください。
