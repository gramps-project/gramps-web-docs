# サーバー設定

デフォルトのDockerイメージを使用することで、すべての必要な設定をブラウザから行うことができます。しかし、デプロイメントによっては、サーバー設定をカスタマイズする必要がある場合があります。

このページでは、設定を変更するためのすべての方法と、すべての既存の設定オプションをリストします。


## 設定ファイルと環境変数

設定には、設定ファイルまたは環境変数のいずれかを使用できます。

[Docker Composeベースのセットアップ](deployment.md)を使用する場合、`grampsweb:`ブロックの`volumes:`キーの下に次のリスト項目を追加することで、設定ファイルを含めることができます。

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
ここで、`/path/to/config.cfg`はサーバーのファイルシステムにおける設定ファイルのパスです（右側はコンテナ内のパスを指し、変更してはいけません）。

環境変数を使用する場合、

- 各設定名の前に`GRAMPSWEB_`を付けて環境変数名を取得します。
- ネストされた辞書設定には二重アンダースコアを使用します。例えば、`GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`は、`THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`設定オプションの値を設定します。

環境を介して設定された設定オプションは、設定ファイル内のものよりも優先されることに注意してください。両方が存在する場合、環境変数が「勝ちます」。

!!! warning "接頭辞なしの環境変数は非推奨です"
    歴史的な理由から、いくつかの設定 – `TREE`、`SECRET_KEY`、`USER_DB_URI`、`POSTGRES_USER`、`POSTGRES_PASSWORD`、`MEDIA_BASE_DIR`、`SEARCH_INDEX_DIR`、`EMAIL_HOST`、`EMAIL_PORT`、`EMAIL_HOST_USER`、`EMAIL_HOST_PASSWORD`、`DEFAULT_FROM_EMAIL`、`BASE_URL`、および`STATIC_PATH` – は、`GRAMPSWEB_`接頭辞なしで環境変数を介して設定することができます。これは非推奨であり、起動時に警告がログに記録され、将来のリリースで動作しなくなります。常に接頭辞付きの形式を使用してください。例えば、`TREE`の代わりに`GRAMPSWEB_TREE`を使用してください。

    これは環境変数のみに関係していることに注意してください。設定ファイルでは、設定名は常に接頭辞なしで使用されます。

!!! tip "非推奨オプションの確認"
    サーバーがまだ依存している非推奨の設定オプション – 接頭辞なしの環境変数、`SEARCH_INDEX_DIR`、または`EMAIL_USE_TLS`など – は、起動時に警告としてログに記録されます。Gramps Web API 3.22以降、これらは、管理者としてログインしているときに、**システム情報**ページの最上部に、置き換えとサポートが削除されるバージョンとともにリストされます（アプリの上部バーのユーザーアイコンからアクセス可能）。

## 既存の設定オプション
以下の設定オプションが存在します。

### 必須設定

キー | 説明
----|-------------
`TREE` | 使用する家系図データベースの名前。`gramps -l`で利用可能な木を表示します。この名前の木が存在しない場合、新しい空の木が作成されます。
`SECRET_KEY` | Flaskのための秘密鍵。秘密は公開されてはいけません。これを変更すると、すべてのアクセストークンが無効になります。
`USER_DB_URI` | ユーザーデータベースのデータベースURL。SQLAlchemyと互換性のある任意のURLが許可されます。

!!! info
    安全な秘密鍵を生成するには、次のコマンドを使用できます。

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### 任意設定

キー | 説明
----|-------------
`MEDIA_BASE_DIR` | メディアファイルのベースディレクトリとして使用するパス。Grampsで設定されたメディアベースディレクトリを上書きします。[S3](s3.md)を使用する場合、`s3://<bucket_name>`の形式である必要があります。
`TREE_ID` | シングルツリーモードで使用する家系図データベースのディレクトリ名（`TREE`が`*`に設定されていない場合）。設定すると、サーバーは表示名ではなくディレクトリ名で木を識別します。これは、名前変更に対してより堅牢です。APIを介して木を名前変更したい場合は必須です。ディレクトリ名は`GET /api/trees/-`（`id`フィールド）を介して見つけることができます。
`SEARCH_INDEX_DB_URI` | 検索インデックスのデータベースURL。バックエンドとして`sqlite`または`postgresql`のみが許可されます。デフォルトは`sqlite:///indexdir/search_index.db`で、スクリプトが実行されるパスに対して相対的に`indexdir`フォルダ内にSQLiteファイルを作成します。
`SEARCH_INDEX_DIR` | **非推奨**（代わりに`SEARCH_INDEX_DB_URI`を使用してください）。検索インデックスを含むディレクトリ。`SEARCH_INDEX_DB_URI`が設定されていない場合に設定すると、検索インデックスURLは`sqlite:///<SEARCH_INDEX_DIR>/search_index.db`として導出されます。
`STATIC_PATH` | 静的ファイルを提供するためのパス（例：静的なWebフロントエンド）
`BASE_URL` | APIにアクセスできるベースURL（例：`https://mygramps.mydomain.com/`）。これは、正しいパスワードリセットリンクを構築するために必要です。
`CORS_ORIGINS` | CORSリクエストが許可されるオリジン。デフォルトでは、すべてが禁止されています。`"*"`を使用して、任意のドメインからのリクエストを許可します。
`EMAIL_HOST` | SMTPサーバーホスト（例：パスワードリセットメールを送信するため）
`EMAIL_PORT` | SMTPサーバーポート。デフォルトは465です。
`EMAIL_HOST_USER` | SMTPサーバーユーザー名
`EMAIL_HOST_PASSWORD` | SMTPサーバーパスワード
`EMAIL_USE_TLS` | **非推奨**（代わりに`EMAIL_USE_SSL`または`EMAIL_USE_STARTTLS`を使用してください）。ブール値、メール送信にTLSを使用するかどうか。デフォルトは`True`です。STARTTLSを使用する場合は、これを`False`に設定し、ポート25とは異なるポートを使用します。
`EMAIL_USE_SSL` | ブール値、SMTPに対して暗黙的なSSL/TLSを使用するかどうか（v3.6.0以降）。`EMAIL_USE_TLS`が明示的に設定されていない場合、デフォルトは`True`です。通常、ポート465で使用されます。
`EMAIL_USE_STARTTLS` | ブール値、SMTPに対して明示的なSTARTTLSを使用するかどうか（v3.6.0以降）。デフォルトは`False`です。通常、ポート587または25で使用されます。
`DEFAULT_FROM_EMAIL` | 自動メールの「From」アドレス
`THUMBNAIL_CACHE_CONFIG` | サムネイルキャッシュの設定を含む辞書。可能な設定については[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照してください。
`REQUEST_CACHE_CONFIG` | リクエストキャッシュの設定を含む辞書。可能な設定については[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照してください。
`PERSISTENT_CACHE_CONFIG` | 永続キャッシュの設定を含む辞書。例えば、テレメトリに使用されます。可能な設定については[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)を参照してください。
`CELERY_CONFIG` | Celeryバックグラウンドタスクキューの設定。可能な設定については[Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)を参照してください。
`REPORT_DIR` | Grampsレポートの出力が保存される一時ディレクトリ
`EXPORT_DIR` | Grampsデータベースのエクスポート出力が保存される一時ディレクトリ
`REGISTRATION_DISABLED` | `True`の場合、新しいユーザー登録を禁止します（デフォルトは`False`）。
`DISABLE_TELEMETRY` | `True`の場合、統計テレメトリを無効にします（デフォルトは`False`）。詳細については[telemetry](telemetry.md)を参照してください。
`PILLOW_MAX_IMAGE_PIXELS` | 処理された画像が含むことができるピクセル数を示すPIL.Image.MAX_IMAGE_PIXELSパラメータを設定します。詳細については[docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS)を参照してください。
`MAX_THUMBNAIL_FILE_BYTES` | サムネイルの最大ファイルサイズを設定します。デフォルトは`50 * 1024 * 1024`（50 MB）です。これを上げるとメモリ使用量が大幅に増加し、大きなファイルがメモリ内で解凍されると、メモリ不足によるクラッシュやデータ損失が発生する可能性があります。

!!! info
    設定のために環境変数を使用する場合、`EMAIL_USE_SSL`のようなブールオプションは、文字列`true`または`false`（大文字と小文字を区別します）でなければなりません。

### PostgreSQLデータベースの設定

これらの設定は、家系図が[PostgreSQLデータベース](postgres.md)にホストされている場合に必要です。

キー | 説明
----|-------------
`POSTGRES_USER` | データベース接続のためのユーザー名
`POSTGRES_PASSWORD` | データベースユーザーのパスワード

### 複数の木をホストするための設定

以下の設定は、[複数の木をホストする](multi-tree.md)場合に関連します。

キー | 説明
----|-------------
`MEDIA_PREFIX_TREE` | 各木のメディアファイル用に別のサブフォルダを使用するかどうかのブール値。デフォルトは`False`ですが、マルチツリーセットアップでは`True`を使用することを強く推奨します。
`NEW_DB_BACKEND` | 新しく作成された家系図に使用するデータベースバックエンド。`sqlite`または`sharedpostgresql`のいずれかでなければなりません。デフォルトは`sqlite`です。値`postgresql`はまだ受け入れられますが、将来のバージョンでPostgreSQLバックエンドが削除されるため、非推奨です。
`POSTGRES_HOST` | SharedPostgreSQLバックエンドを使用したマルチツリーセットアップで新しい木を作成するために使用されるPostgreSQLサーバーのホスト名
`POSTGRES_PORT` | SharedPostgreSQLバックエンドを使用したマルチツリーセットアップで新しい木を作成するために使用されるPostgreSQLサーバーのポート

### OIDC認証の設定

これらの設定は、外部プロバイダーとのOpenID Connect (OIDC) 認証を使用する場合に必要です。詳細な設定手順と例については、[OIDC認証](oidc.md)を参照してください。

キー | 説明
----|-------------
`OIDC_ENABLED` | OIDC認証を有効にするかどうかのブール値。デフォルトは`False`。
`OIDC_ISSUER` | OIDCプロバイダーの発行者URL（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_ID` | OAuthクライアントID（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_SECRET` | OAuthクライアントシークレット（カスタムOIDCプロバイダー用）
`OIDC_NAME` | プロバイダーのカスタム表示名。デフォルトは「OIDC」
`OIDC_SCOPES` | OAuthスコープ。デフォルトは「openid email profile」
`OIDC_USERNAME_CLAIM` | ユーザー名に使用するクレーム。デフォルトは「preferred_username」
`OIDC_OPENID_CONFIG_URL` | オプション：OpenID Connect設定エンドポイントのURL（標準の`/.well-known/openid-configuration`を使用しない場合）
`OIDC_PKCE` | PKCEを使用するかどうかのブール値。設定されていない場合、プロバイダーのディスカバリードキュメントが`S256`をリストしているときにPKCEが使用されます。詳細については[PKCE](oidc.md#pkce)を参照してください。
`OIDC_DISABLE_LOCAL_AUTH` | ローカルのユーザー名/パスワード認証を無効にするかどうかのブール値。デフォルトは`False`
`OIDC_AUTO_REDIRECT` | プロバイダーが1つだけ設定されている場合に自動的にOIDCにリダイレクトするかどうかのブール値。デフォルトは`False`

#### 組み込みOIDCプロバイダー

組み込みプロバイダー（Google、Microsoft）の場合、これらの設定を使用します。

キー | 説明
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuthのクライアントID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuthのクライアントシークレット
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuthのクライアントID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuthのクライアントシークレット
`OIDC_GOOGLE_PKCE` | GoogleのPKCE設定、詳細は[PKCE](oidc.md#pkce)を参照
`OIDC_MICROSOFT_PKCE` | MicrosoftのPKCE設定、詳細は[PKCE](oidc.md#pkce)を参照

#### OIDCロールマッピング

これらの設定を使用すると、アイデンティティプロバイダーからのOIDCグループ/ロールをGramps Webユーザーロールにマッピングできます。

キー | 説明
----|-------------
`OIDC_ROLE_CLAIM` | ユーザーのグループ/ロールを含むOIDCトークン内のクレーム名。デフォルトは「groups」
`OIDC_GROUP_ADMIN` | Grampsの「Admin」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名
`OIDC_GROUP_OWNER` | Grampsの「Owner」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名
`OIDC_GROUP_EDITOR` | Grampsの「Editor」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名
`OIDC_GROUP_CONTRIBUTOR` | Grampsの「Contributor」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名
`OIDC_GROUP_MEMBER` | Grampsの「Member」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名
`OIDC_GROUP_GUEST` | Grampsの「Guest」ロールにマッピングされるOIDCプロバイダーのグループ/ロール名

### AI機能専用の設定

これらの設定は、チャットやセマンティック検索などのAI駆動機能を使用する場合に必要です。

キー | 説明
----|-------------
`LLM_BASE_URL` | OpenAI互換のチャットAPIのベースURL。デフォルトは`None`で、OpenAI APIを使用します。
`LLM_MODEL` | OpenAI互換のチャットAPIに使用するモデル。設定されていない場合（デフォルト）、チャットは無効になります。v3.6.0以降、AIアシスタントはツール呼び出し機能を持つPydantic AIを使用します。
`VECTOR_EMBEDDING_MODEL` | セマンティック検索のベクトル埋め込みに使用するモデル。ローカルモデルを使用する場合、これは[Sentence Transformers](https://sbert.net/)モデル名でなければなりません。リモートAPIを使用する場合（`VECTOR_EMBEDDING_BASE_URL`を参照）、これはリモートプロバイダーに渡されるモデル名です。設定されていない場合（デフォルト）、セマンティック検索とチャットは無効になります。
`VECTOR_EMBEDDING_BASE_URL` | リモートOpenAI互換の埋め込みAPIのベースURL（例：Ollama、OpenAI、LiteLLM）。設定されていない場合（デフォルト）、ローカルのSentence Transformersモデルが使用されます。詳細については[リモート埋め込みAPIの使用](chat.md#using-a-remote-embedding-api)を参照してください。
`VECTOR_EMBEDDING_API_KEY` | 認証されたリモート埋め込みプロバイダーのAPIキー。`VECTOR_EMBEDDING_BASE_URL`が設定されていて、プロバイダーが認証を必要とする場合のみ必要です。
`LLM_MAX_CONTEXT_LENGTH` | LLMに提供される家系図コンテキストの文字数制限。デフォルトは50000です。
`LLM_SYSTEM_PROMPT` | LLMチャットアシスタントのカスタムシステムプロンプト（v3.6.0以降）。設定されていない場合、デフォルトの系譜最適化プロンプトが使用されます。

## 設定ファイルの例

本番用の最小限の設定ファイルは次のようになります。
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # ポート465のために暗黙的なSSLを使用
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # あなたのSMTPパスワード
DEFAULT_FROM_EMAIL="gramps@example.com"
