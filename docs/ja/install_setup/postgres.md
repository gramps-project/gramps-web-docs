# PostgreSQLデータベースの使用

デフォルトでは、Grampsは家系図を保存するためにファイルベースのSQLiteデータベースを使用します。これはGramps Webにとって完全に機能し、ほとんどのユーザーに推奨されます。しかし、Gramps Web APIバージョン0.3.0以降、[Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)によって、データベースごとに単一の家系図を持つPostgreSQLサーバーもサポートされています。[バージョン1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0)以降、複数の家系図を単一のデータベースにホストできるSharedPostgreSQL Addonもサポートされており、これはGramps Web APIの[multi-tree support](multi-tree.md)と一緒に使用する際に特に便利です。

!!! warning "PostgreSQLバックエンドの非推奨"
    PostgreSQLバックエンド（データベースごとに1つの家系図）のサポートは、複数のツリーをホストすることと互換性がないため、将来のGramps Web APIのバージョンで削除されます。SharedPostgreSQLおよびSQLiteバックエンドは引き続き完全にサポートされます。新しいインストールには、SharedPostgreSQLを使用してください。

## PostgreSQLサーバーの設定

PostgreSQLAddonで使用する新しいデータベースを設定したい場合は、[Gramps Wikiの指示](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)に従ってサーバーを設定できます。

また、Docker Composeを使用して、Gramps Webと同じdockerホスト上でコンテナ内にPostgreSQLサーバーを実行することもできます。

Grampsでdocker化されたPostgreSQLを使用する際の唯一の複雑さは、デフォルトのPostgreSQLイメージにはロケールがインストールされていないため、Grampsがオブジェクトのローカライズされた照合に必要とすることです。最も簡単なオプションは、[このリポジトリ](https://github.com/DavidMStraub/gramps-postgres-docker/)でリリースされた`gramps-postgres`イメージを使用することです。これを使用するには、`docker-compose.yml`に次のセクションを追加します：
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
また、このYAMLファイルの`volumes:`セクションの下に`postgres_data:`をキーとして追加します。このイメージには、Grampsの系譜データ用とGrampsユーザーデータベース用の別々のデータベースが含まれており、それぞれ異なるパスワードを持つことができます。

## Gramps家系図のインポート

再度、PostgreSQLサーバーを自分で設定した場合は、[Gramps Wikiの指示](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)に従ってデータベースに家系図をインポートできます。

また、上記のDocker Composeの指示に従った場合は、dockerホスト上にあるGramps XMLファイルをインポートするために次のコマンドを使用できます：

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## データベース用にWeb APIを構成する

PostgreSQLデータベース用にWeb APIを構成するには、`docker-compose.yml`の`grampsweb`サービスの`environment:`キーの下に次の内容を追加します：

```yaml
      # PostgreSQLアドオンはツリー名が
      # データベース名と等しいと仮定しており、
      # ここではPostgreSQLイメージのデフォルト
      # データベース名が使用されます
      GRAMPSWEB_TREE: postgres
      # 認証情報はPostgreSQLコンテナで使用されるものと一致する必要があります
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## マルチツリーインストールでの共有PostgreSQLデータベースの使用

[multi-tree setup](multi-tree.md)を使用する場合、SharedPostgreSQLアドオンは、APIを介して新しく作成されたものも含めて、すべてのツリーを単一のPostgreSQLデータベースにホストする便利なオプションです。プライバシーやセキュリティを損なうことなく。

これを実現するために、上記の説明に従って`gramps-postgres`イメージに基づくコンテナを設定し、単に`NEW_DB_BACKEND`の設定オプションを`sharedpostgresql`に設定します。例えば、`GRAMPSWEB_NEW_DB_BACKEND`環境変数を介して設定します。

## ユーザーデータベース用のPostgreSQLデータベースの使用

系譜データにどのデータベースバックエンドを使用するかに関係なく、適切なデータベースURLを提供することで、ユーザーデータベースをPostgreSQLデータベースにホストできます。上記の`gramps-postgres`dockerイメージには、この目的のために使用できる別のデータベース`grampswebuser`が含まれています。その場合、`USER_DB_URI`設定オプションの適切な値は次のようになります。
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 検索インデックス用のPostgreSQLデータベースの使用

Gramps Web APIバージョン2.4.0以降、検索インデックスはSQLiteデータベース（デフォルト）またはPostgreSQLデータベースのいずれかにホストされます。この目的のためにも、`gramps-postgres`イメージを使用できます。検索インデックスには、系譜データをPostgreSQLでホストしているかどうかに関係なく、イメージによって提供される`gramps`データベースを使用できます（検索インデックスと系譜データは同じデータベース内に共存できます）。これは、上記の例で`SEARCH_INDEX_DB_URI`設定オプションを次のように設定することで実現できます。
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## 問題

問題が発生した場合は、Gramps WebとPostgreSQLサーバーのログ出力を監視してください。Dockerの場合、これは次のコマンドで実行できます。

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Gramps Web（またはドキュメント）に問題があると思われる場合は、[Githubに問題を報告してください](https://github.com/gramps-project/gramps-web-api/issues)。
