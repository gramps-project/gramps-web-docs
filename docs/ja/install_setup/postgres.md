# PostgreSQLデータベースの使用

デフォルトでは、Gramps Webは各家系図を独自のSQLiteデータベースファイルに保存します。これには追加のサービスは必要なく、バックアップはファイルをコピーするだけで簡単であり、ほとんどのインストールにおいてうまく機能します。複数の家系図を[ホスティングする](multi-tree.md)場合も含まれます。

代わりに、家系図はSharedPostgreSQLアドオンを使用してPostgreSQLサーバー上にホストすることができ、すべての家系図を単一のデータベースに保持します。これは、すでにPostgreSQLサーバーを運用していて、そこでバックアップや監視を管理したい場合や、多くのユーザーが同時に編集することを期待する場合に意味があります。PostgreSQLは、家系図が保存されている場所に関係なく、[ユーザーデータベース](#using-a-postgresql-database-for-the-user-database)や[検索インデックス](#using-a-postgresql-database-for-the-search-index)もホストできます。

!!! warning "PostgreSQLアドオンの非推奨"
    単一の家系図をデータベースごとに保存する古いPostgreSQLアドオンは非推奨であり、今後のGramps Web APIのバージョンではサポートされなくなります。これを使用している場合は、[PostgreSQLアドオンからSharedPostgreSQLへの移行](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql)を参照してください。

## PostgreSQLサーバーの設定

最も簡単なオプションは、Docker Composeを使用してGramps Webと同じDockerホスト上のコンテナでPostgreSQLサーバーを実行することです。

Grampsは、異なる言語でオブジェクトを正しくソートするためにPostgreSQLサーバーにロケールがインストールされている必要があり、デフォルトのPostgreSQLイメージにはそれが含まれていません。[`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/)イメージはそれらを追加します。これを使用するには、`docker-compose.yml`に以下のセクションを追加します：
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
また、このYAMLファイルの`volumes:`セクションの下に`postgres_data:`をキーとして追加します。このイメージには、各自のユーザーとパスワードを持つ2つのデータベースが含まれています：系譜データ用の`gramps`とGramps Webユーザーデータベース用の`grampswebuser`です。

代わりに独自のPostgreSQLサーバーを使用する場合は、設定されたユーザーがテーブルを作成できる`gramps`という名前のデータベースを作成し、ユーザーが必要とするロケールがインストールされていることを確認してください。

## Gramps Webの設定

新しい家系図は、Gramps Webが[multi-treeモード](multi-tree.md)で実行され、`NEW_DB_BACKEND`設定オプションが`sharedpostgresql`に設定されているときにSharedPostgreSQLデータベースに作成されます。上記のDocker Composeセットアップを使用して、`docker-compose.yml`の`grampsweb`サービスの`environment:`キーの下に以下を追加します：

```yaml
      # マルチツリー モードを有効にする
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # SharedPostgreSQLデータベースに新しいツリーを作成する
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQLサーバーのホストとポート。ホストは上記のPostgreSQLサービスの名前です
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # 認証情報はPostgreSQLコンテナで使用されるものと一致する必要があります
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

これらのオプションの説明については[設定](configuration.md)を参照してください。ホストとポートは、ツリーが作成されるときに各ツリーと共に保存されるため、後で変更しても新しいツリーにのみ影響します。

## ツリーの作成とデータのインポート

新しいツリーを作成するには、[複数のツリーをホスティングするためのセットアップ](multi-tree.md#create-a-new-tree)で説明されているように`/trees/`エンドポイントにPOSTします。レスポンスには新しいツリーのIDが含まれており、これが[ツリーオーナーアカウントの作成](../administration/owner.md#multi-tree-setup-create-tree-owner-account)に必要です。

ツリーオーナーがログインすると、既存の家系図（例えば、Gramps DesktopからエクスポートされたGramps XMLファイル）をウェブインターフェースを介して[インポート](../administration/import.md)できます。

## ユーザーデータベース用のPostgreSQLデータベースの使用

ユーザーデータベースは通常、家系図がホスティングされている場所に関係なくSQLiteファイルです。代わりにPostgreSQLを使用するには、`USER_DB_URI`設定オプションをPostgreSQLデータベースのURLに設定します。上記の`gramps-postgres`イメージを使用する場合は、その`grampswebuser`データベースを使用します：
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 検索インデックス用のPostgreSQLデータベースの使用

検索インデックスもデフォルトではSQLiteに保存されます。代わりにPostgreSQLを使用するには、`SEARCH_INDEX_DB_URI`設定オプションをPostgreSQLデータベースのURLに設定します。上記の`gramps-postgres`イメージを使用する場合、家系図がそこにホストされているかどうかに関係なく、その`gramps`データベースを使用できます：
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## PostgreSQLアドオンからSharedPostgreSQLへのツリーの移行

古いインストールでは、単一のツリーをデータベースごとに保存するPostgreSQLアドオンを使用して家系図をホストしている場合があります。ツリーがどのアドオンを使用しているかを確認するには、Grampsデータベースディレクトリのツリーのサブディレクトリにある`database.txt`ファイルを見てください。そこには、非推奨のPostgreSQLアドオンの場合は`postgresql`、SharedPostgreSQLの場合は`sharedpostgresql`が含まれています。

同じインストール内でPostgreSQLアドオンからSharedPostgreSQLにツリーを移行し、ユーザーアカウントとメディアファイルを保持するには：

1. プライベートレコードを表示できるアカウントを使用して、Gramps XML（`.gramps`）ファイルとして[家系図をバックアップ](../administration/export.md#back-up-your-family-tree)します。
2. [Gramps Webの設定](#configuring-gramps-web)で説明されているように構成を変更します。既存の`gramps-postgres`コンテナを引き続き使用できます。
3. [新しいツリーを作成](multi-tree.md#create-a-new-tree)し、そのツリーIDをメモします。
4. [既存のユーザーデータベースを移行](multi-tree.md#migrate-existing-user-database)で説明されているように、既存のユーザーアカウントを新しいツリーに割り当てます。
5. [既存のメディアファイルを移行](multi-tree.md#migrate-existing-media-files)で説明されているように、メディアファイルを新しいツリーに期待される場所に移動します。
6. ログインして、Gramps XMLファイルを新しいツリーに[インポート](../administration/import.md)します。

新しいツリーが完全であることを確認するまで、Gramps XMLファイルを保持してください。

別のGramps Webインストールに移行する場合は、[別のGramps Webインスタンスに移動](../administration/export.md#move-to-a-different-gramps-web-instance)の手順に従ってください。

## 問題

問題が発生した場合は、Gramps WebおよびPostgreSQLサーバーのログ出力を監視してください。Dockerの場合、これは次のコマンドで実行できます。

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Gramps Web（またはドキュメント）に問題があると思われる場合は、[Github](https://github.com/gramps-project/gramps-web-api/issues)に問題を報告してください。
