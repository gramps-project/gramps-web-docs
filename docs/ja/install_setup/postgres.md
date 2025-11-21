# PostgreSQLデータベースの使用

デフォルトでは、Grampsは家系図を保存するためにファイルベースのSQLiteデータベースを使用します。これはGramps Webにとっては完全に機能し、ほとんどのユーザーに推奨されます。しかし、Gramps Web APIバージョン0.3.0以降、[Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)によって、データベースごとに単一の家系図を持つPostgreSQLサーバーもサポートされています。[バージョン1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0)以降、SharedPostgreSQL Addonもサポートされており、これにより単一のデータベース内で複数の家系図をホストすることが可能になり、特にGramps Web APIの[multi-tree support](multi-tree.md)と一緒に使用する際に便利です。

## PostgreSQLサーバーの設定

PostgreSQLAddonで使用する新しいデータベースを設定したい場合は、[Gramps Wikiの指示](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)に従ってサーバーを設定できます。

また、Docker Composeを使用して、Gramps Webと同じDockerホスト上のコンテナでPostgreSQLサーバーを実行することもできます。

GrampsでのDocker化されたPostgreSQLの使用は、デフォルトのPostgreSQLイメージにロケールがインストールされていないために複雑になりますが、これはGrampsがオブジェクトのローカライズされた照合に必要とします。最も簡単なオプションは、[このリポジトリ](https://github.com/DavidMStraub/gramps-postgres-docker/)でリリースされた`gramps-postgres`イメージを使用することです。これを使用するには、`docker-compose.yml`に次のセクションを追加します：
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
また、このYAMLファイルの`volumes:`セクションの下に`postgres_data:`をキーとして追加します。このイメージには、Grampsの系譜データ用の別のデータベースとGrampsユーザーデータベースが含まれており、それぞれに別々のパスワードを設定できます。

## Gramps家系図のインポート

再度、PostgreSQLサーバーを自分で設定した場合は、[Gramps Wikiの指示](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)に従ってデータベースに家系図をインポートできます。

また、上記のDocker Composeの指示に従った場合は、次のコマンドを使用してDockerホスト上にあるGramps XMLファイルをインポートできます：

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
      # データベース名と等しいと仮定します。
      # ここではPostgreSQLイメージのデフォルト
      # データベース名が使用されています。
      TREE: postgres
      # 認証情報は
      # PostgreSQLコンテナで使用されるものと一致する必要があります。
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## マルチツリーインストールでの共有PostgreSQLデータベースの使用

[multi-tree setup](multi-tree.md)を使用する場合、SharedPostgreSQLアドオンは、APIを介して新しく作成されたものを含むすべてのツリーを単一のPostgreSQLデータベースでホストする便利なオプションです。これにより、プライバシーやセキュリティを損なうことなく運用できます。

これを実現するには、上記で説明したように`gramps-postgres`イメージに基づいたコンテナを設定し、単に設定オプション`NEW_DB_BACKEND`を`sharedpostgresql`に設定します。例えば、`GRAMPSWEB_NEW_DB_BACKEND`環境変数を介して設定します。

## ユーザーデータベース用のPostgreSQLデータベースの使用

系譜データにどのデータベースバックエンドを使用しているかに関係なく、適切なデータベースURLを提供することで、ユーザーデータベースをPostgreSQLデータベースでホストできます。上記の`gramps-postgres` Dockerイメージには、この目的のために使用できる別のデータベース`grampswebuser`が含まれています。その場合、`USER_DB_URI`設定オプションの適切な値は次のようになります。
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 検索インデックス用のPostgreSQLデータベースの使用

Gramps Web APIバージョン2.4.0以降、検索インデックスはSQLiteデータベース（デフォルト）またはPostgreSQLデータベースのいずれかにホストされます。この目的のためにも、`gramps-postgres`イメージを使用できます。検索インデックスには、系譜データをPostgreSQLでホストしているかどうかに関係なく、イメージが提供する`gramps`データベースを使用できます（検索インデックスと系譜データは同じデータベースに共存できます）。これは、上記の例で`SEARCH_INDEX_DB_URI`設定オプションを次のように設定することで実現できます。
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## 問題

問題が発生した場合は、Gramps WebとPostgreSQLサーバーのログ出力を監視してください。Dockerの場合、これは次のコマンドで実行できます。

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Gramps Web（またはドキュメント）に問題があると思われる場合は、[Github](https://github.com/gramps-project/gramps-web-api/issues)で問題を報告してください。
