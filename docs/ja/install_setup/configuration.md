# サーバー設定

デフォルトのDockerイメージを使用する場合、すべての必要な設定はブラウザから行うことができます。ただし、デプロイメントによっては、サーバー設定をカスタマイズする必要がある場合があります。

このページでは、設定を変更するためのすべての方法と、すべての既存の設定オプションを一覧表示します。

## 設定ファイルと環境変数

設定には、設定ファイルまたは環境変数のいずれかを使用できます。

[Docker Composeベースのセットアップ](deployment.md)を使用する場合、`grampsweb:`ブロックの`volumes:`キーの下に次のリスト項目を追加することで、設定ファイルを含めることができます。

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
ここで、`/path/to/config.cfg`はサーバーのファイルシステムにおける設定ファイルのパスです（右側はコンテナ内のパスを指し、変更してはいけません）。

環境変数を使用する場合、

- 各設定名の前に`GRAMPSWEB_`を付けて環境変数の名前を取得します
- ネストされた辞書設定には二重アンダースコアを使用します。例えば、`GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`は、`THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`設定オプションの値を設定します

環境変数で設定された設定オプションは、設定ファイル内のものよりも優先されることに注意してください。両方が存在する場合、環境変数が「勝ち」ます。

## 既存の設定

以下の設定オプションが存在します。

### 必須設定

キー | 説明
----|-------------
`TREE` | 使用する家系図データベースの名前。`gramps -l`で利用可能なツリーを表示します。この名前のツリーが存在しない場合、新しい空のツリーが作成されます。
`SECRET_KEY` | Flaskのための秘密鍵。秘密は公開されてはいけません。これを変更すると、すべてのアクセストークンが無効になります。
`USER_DB_URI` | ユーザーデータベースのデータベースURL。SQLAlchemyに互換性のある任意のURLが許可されます。

!!! info
    安全な秘密鍵を生成するには、次のコマンドを使用できます。

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### 任意設定

キー | 説明
----|-------------
`MEDIA_BASE_DIR` | メディアファイルのベースディレクトリとして使用するパス。Grampsで設定されたメディアベースディレクトリを上書きします。[S3](s3.md)を使用する場合、`s3://<bucket_name>`の形式である必要があります。
`SEARCH_INDEX_DB_URI` | 検索インデックスのデータベースURL。バックエンドとして`sqlite`または`postgresql`のみが許可されます。デフォルトは`sqlite:///indexdir/search_index.db`で、スクリプトが実行されるパスに対して相対的に`indexdir`フォルダーにSQLiteファイルを作成します。
`STATIC_PATH` | 静的ファイルを提供するためのパス（例：静的Webフロントエンド）
`BASE_URL` | APIにアクセスできるベースURL（例：`https://mygramps.mydomain.com/`）。これは、正しいパスワードリセットリンクを構築するために必要です。
`CORS_ORIGINS` | CORSリクエストが許可されるオリジン。デフォルトでは、すべてが拒否されます。任意のドメインからのリクエストを許可するには、`"*"`を使用します。
`EMAIL_HOST` | SMTPサーバーホスト（例：パスワードリセットメールを送信するため）
`EMAIL_PORT` | SMTPサーバーポート。デフォルトは465
`EMAIL_HOST_USER` | SMTPサーバーユーザー名
`EMAIL_HOST_PASSWORD` | SMTPサーバーパスワード
`EMAIL_USE_TLS` | メール送信にTLSを使用するかどうかのブール値。デフォルトは`True`です。STARTTLSを使用する場合は、これを`False`に設定し、ポート25とは異なるポートを使用します。
`DEFAULT_FROM_EMAIL` | 自動メールの「From」アドレス
`THUMBNAIL_CACHE_CONFIG` | サムネイルキャッシュの設定を含む辞書。[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照して、可能な設定を確認してください。
`REQUEST_CACHE_CONFIG` | リクエストキャッシュの設定を含む辞書。[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照して、可能な設定を確認してください。
`PERSISTENT_CACHE_CONFIG` | 永続キャッシュの設定を含む辞書。例えば、テレメトリに使用されます。[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照して、可能な設定を確認してください。
`CELERY_CONFIG` | Celeryバックグラウンドタスクキューの設定。[Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)を参照して、可能な設定を確認してください。
`REPORT_DIR` | Grampsレポートの出力が保存される一時ディレクトリ
`EXPORT_DIR` | Grampsデータベースのエクスポート出力が保存される一時ディレクトリ
`REGISTRATION_DISABLED` | `True`の場合、新しいユーザー登録を禁止します（デフォルトは`False`）
`DISABLE_TELEMETRY` | `True`の場合、統計テレメトリを無効にします（デフォルトは`False`）。詳細については[telemetry](telemetry.md)を参照してください。

!!! info
    環境変数を使用して設定する場合、`EMAIL_USE_TLS`のようなブールオプションは、文字列`true`または`false`（大文字と小文字が区別されます）でなければなりません。

### PostgreSQLバックエンドデータベース専用の設定

これは、Grampsデータベースを[PostgreSQLアドオン](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)で動作するように設定した場合に必要です。

キー | 説明
----|-------------
`POSTGRES_USER` | データベース接続のためのユーザー名
`POSTGRES_PASSWORD` | データベースユーザーのパスワード

### 複数のツリーをホスティングするための設定

以下の設定は、[複数のツリーをホスティングする](multi-tree.md)際に関連します。

キー | 説明
----|-------------
`MEDIA_PREFIX_TREE` | 各ツリーのメディアファイル用に別のサブフォルダーを使用するかどうかのブール値。デフォルトは`False`ですが、マルチツリーセットアップでは`True`を使用することを強く推奨します。
`NEW_DB_BACKEND` | 新しく作成された家系図に使用するデータベースバックエンド。`sqlite`、`postgresql`、または`sharedpostgresql`のいずれかでなければなりません。デフォルトは`sqlite`です。
`POSTGRES_HOST` | SharedPostgreSQLバックエンドを使用してマルチツリーセットアップで新しいツリーを作成する際に使用されるPostgreSQLサーバーのホスト名
`POSTGRES_PORT` | SharedPostgreSQLバックエンドを使用してマルチツリーセットアップで新しいツリーを作成する際に使用されるPostgreSQLサーバーのポート

### OIDC認証のための設定

これらの設定は、外部プロバイダーとOpenID Connect (OIDC) 認証を使用したい場合に必要です。詳細な設定手順と例については、[OIDC Authentication](oidc.md)を参照してください。

キー | 説明
----|-------------
`OIDC_ENABLED` | OIDC認証を有効にするかどうかのブール値。デフォルトは`False`です。
`OIDC_ISSUER` | OIDCプロバイダーの発行者URL（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_ID` | OAuthクライアントID（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_SECRET` | OAuthクライアントシークレット（カスタムOIDCプロバイダー用）
`OIDC_NAME` | プロバイダーのカスタム表示名。デフォルトは「OIDC」
`OIDC_SCOPES` | OAuthスコープ。デフォルトは「openid email profile」
`OIDC_USERNAME_CLAIM` | ユーザー名に使用するクレーム。デフォルトは「preferred_username」
`OIDC_OPENID_CONFIG_URL` | オプション：OpenID Connect構成エンドポイントへのURL（標準の`/.well-known/openid-configuration`を使用しない場合）
`OIDC_DISABLE_LOCAL_AUTH` | ローカルのユーザー名/パスワード認証を無効にするかどうかのブール値。デフォルトは`False`
`OIDC_AUTO_REDIRECT` | プロバイダーが1つだけ設定されている場合に自動的にOIDCにリダイレクトするかどうかのブール値。デフォルトは`False`

#### 組み込みOIDCプロバイダー

組み込みプロバイダー（Google、Microsoft、GitHub）には、次の設定を使用します。

キー | 説明
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuthのクライアントID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuthのクライアントシークレット
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuthのクライアントID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuthのクライアントシークレット
`OIDC_GITHUB_CLIENT_ID` | GitHub OAuthのクライアントID
`OIDC_GITHUB_CLIENT_SECRET` | GitHub OAuthのクライアントシークレット

#### OIDCロールマッピング

これらの設定を使用すると、アイデンティティプロバイダーからのOIDCグループ/ロールをGramps Webユーザーロールにマッピングできます。

キー | 説明
----|-------------
`OIDC_ROLE_CLAIM` | ユーザーのグループ/ロールを含むOIDCトークン内のクレーム名。デフォルトは「groups」
`OIDC_GROUP_ADMIN` | Grampsの「Admin」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_OWNER` | Grampsの「Owner」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_EDITOR` | Grampsの「Editor」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_CONTRIBUTOR` | Grampsの「Contributor」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_MEMBER` | Grampsの「Member」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_GUEST` | Grampsの「Guest」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名

### AI機能専用の設定

これらの設定は、チャットやセマンティック検索などのAI駆動の機能を使用したい場合に必要です。

キー | 説明
----|-------------
`LLM_BASE_URL` | OpenAI互換のチャットAPIのベースURL。デフォルトは`None`で、OpenAI APIを使用します。
`LLM_MODEL` | OpenAI互換のチャットAPIで使用するモデル。未設定の場合（デフォルト）、チャットは無効になります。
`VECTOR_EMBEDDING_MODEL` | セマンティック検索のベクトル埋め込みに使用する[Sentence Transformers](https://sbert.net/)モデル。未設定の場合（デフォルト）、セマンティック検索とチャットは無効になります。
`LLM_MAX_CONTEXT_LENGTH` | LLMに提供される家系図コンテキストの文字数制限。デフォルトは50000です。

## 設定ファイルの例

本番用の最小限の設定ファイルは次のようになります。
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # あなたのSMTPパスワード
DEFAULT_FROM_EMAIL="gramps@example.com"
