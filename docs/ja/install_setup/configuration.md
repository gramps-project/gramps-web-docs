# サーバー構成

デフォルトのDockerイメージを使用すると、すべての必要な構成をブラウザから行うことができます。ただし、デプロイメントによっては、サーバー構成をカスタマイズする必要がある場合があります。

このページでは、構成を変更するためのすべての方法と、すべての既存の構成オプションをリストします。


## 構成ファイルと環境変数

設定には、構成ファイルまたは環境変数のいずれかを使用できます。

[Docker Composeベースのセットアップ](deployment.md)を使用する場合、`grampsweb:`ブロックの`volumes:`キーの下に次のリスト項目を追加することで、構成ファイルを含めることができます。

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
ここで、`/path/to/config.cfg`はサーバーのファイルシステム内の構成ファイルへのパスです（右側はコンテナ内のパスを指し、変更してはいけません）。

環境変数を使用する場合、

- 各設定名の前に`GRAMPSWEB_`を付けて環境変数の名前を取得します。
- ネストされた辞書設定には二重アンダースコアを使用します。例えば、`GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`は、`THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`構成オプションの値を設定します。

環境を介して設定された構成オプションは、構成ファイル内のものよりも優先されることに注意してください。両方が存在する場合、環境変数が「勝ちます」。

!!! warning "プレフィックスなしの環境変数は非推奨です"
    歴史的な理由から、いくつかの設定 – `TREE`、`SECRET_KEY`、`USER_DB_URI`、`POSTGRES_USER`、`POSTGRES_PASSWORD`、`MEDIA_BASE_DIR`、`SEARCH_INDEX_DIR`、`EMAIL_HOST`、`EMAIL_PORT`、`EMAIL_HOST_USER`、`EMAIL_HOST_PASSWORD`、`DEFAULT_FROM_EMAIL`、`BASE_URL`、および`STATIC_PATH` – は、`GRAMPSWEB_`プレフィックスなしで環境変数を介して設定することができます。これは非推奨であり、起動時に警告がログに記録され、将来のリリースで動作しなくなります。常にプレフィックス付きの形式を使用してください。例：`GRAMPSWEB_TREE`ではなく`TREE`を使用します。

    これは環境変数にのみ関係します。構成ファイルでは、設定名は常にプレフィックスなしで使用されます。

!!! tip "非推奨オプションの確認"
    サーバーがまだ依存している非推奨の構成オプション – プレフィックスなしの環境変数、`SEARCH_INDEX_DIR`、または`EMAIL_USE_TLS`など – は、起動時に警告としてログに記録されます。Gramps Web API 3.22以降、これらは、管理者としてログインしているときに、**システム情報**ページの上部に、置き換えとサポートが削除されるバージョンとともにリストされます（アプリの上部バーのユーザーアイコンからアクセス可能）。

## 既存の構成設定
以下の構成オプションが存在します。

### 必須設定

キー | 説明
----|-------------
`TREE` | 使用するファミリーツリーのデータベースの名前。`gramps -l`で利用可能なツリーを表示します。この名前のツリーが存在しない場合は、新しい空のツリーが作成されます。
`SECRET_KEY` | Flaskのための秘密鍵。秘密は公に共有してはいけません。これを変更すると、すべてのアクセストークンが無効になります。
`USER_DB_URI` | ユーザーデータベースのデータベースURL。SQLAlchemyと互換性のある任意のURLが許可されています。

!!! info
    安全な秘密鍵を生成するには、次のコマンドを使用できます。

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### オプション設定

キー | 説明
----|-------------
`MEDIA_BASE_DIR` | メディアファイルのベースディレクトリとして使用するパス。Grampsで設定されたメディアベースディレクトリを上書きします。[S3](s3.md)を使用する場合は、`s3://<bucket_name>`の形式である必要があります。
`TREE_ID` | シングルツリーモードで使用するファミリーツリーのデータベースのディレクトリ名（`TREE`が`*`に設定されていない場合）。設定すると、サーバーは表示名ではなくディレクトリ名でツリーを識別します。これはリネームに対してより堅牢です。APIを介してツリーの名前を変更したい場合は必須です。ディレクトリ名は`GET /api/trees/-`（`id`フィールド）で見つけることができます。
`SEARCH_INDEX_DB_URI` | 検索インデックスのデータベースURL。バックエンドとしては`sqlite`または`postgresql`のみが許可されています。デフォルトは`sqlite:///indexdir/search_index.db`で、スクリプトが実行されるパスに対して相対的に`indexdir`フォルダ内にSQLiteファイルを作成します。
`SEARCH_INDEX_DIR` | **非推奨**（代わりに`SEARCH_INDEX_DB_URI`を使用してください）。検索インデックスを含むディレクトリ。`SEARCH_INDEX_DB_URI`が設定されていない場合に設定すると、検索インデックスURLは`sqlite:///<SEARCH_INDEX_DIR>/search_index.db`として導出されます。
`STATIC_PATH` | 静的ファイルを提供するためのパス（例：静的なWebフロントエンド）
`BASE_URL` | APIにアクセスできるベースURL（例：`https://mygramps.mydomain.com/`）。これは、正しいパスワードリセットリンクを構築するために必要です。
`CORS_ORIGINS` | CORSリクエストが許可されるオリジン。デフォルトでは、すべてが拒否されます。`"*"`を使用して、任意のドメインからのリクエストを許可します。
`EMAIL_HOST` | SMTPサーバーのホスト（例：パスワードリセットメールの送信用）
`EMAIL_PORT` | SMTPサーバーのポート。デフォルトは465です。
`EMAIL_HOST_USER` | SMTPサーバーのユーザー名
`EMAIL_HOST_PASSWORD` | SMTPサーバーのパスワード
`EMAIL_USE_TLS` | **非推奨**（代わりに`EMAIL_USE_SSL`または`EMAIL_USE_STARTTLS`を使用してください）。ブール値、メール送信にTLSを使用するかどうか。デフォルトは`True`です。STARTTLSを使用する場合は、これを`False`に設定し、25以外のポートを使用してください。
`EMAIL_USE_SSL` | ブール値、SMTP用に暗黙のSSL/TLSを使用するかどうか（v3.6.0+）。`EMAIL_USE_TLS`が明示的に設定されていない場合、デフォルトは`True`です。通常はポート465で使用されます。
`EMAIL_USE_STARTTLS` | ブール値、SMTP用に明示的なSTARTTLSを使用するかどうか（v3.6.0+）。デフォルトは`False`です。通常はポート587または25で使用されます。
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
`MAX_THUMBNAIL_FILE_BYTES` | サムネイルの最大ファイルサイズを設定します。デフォルトは`50 * 1024 * 1024`（50 MB）です。これを上げると、メモリ使用量が大幅に増加し、大きなファイルがメモリ内で解凍されると、メモリ不足のクラッシュやデータ損失が発生する可能性があります。

!!! info
    構成のために環境変数を使用する場合、`EMAIL_USE_SSL`のようなブールオプションは、文字列`true`または`false`（大文字と小文字を区別）でなければなりません。

### PostgreSQLデータベース用の設定

これらの設定は、ファミリーツリーが[PostgreSQLデータベース](postgres.md)にホストされている場合に必要です。SharedPostgreSQLアドオンを使用します。

キー | 説明
----|-------------
`POSTGRES_USER` | データベース接続のためのユーザー名
`POSTGRES_PASSWORD` | データベースユーザーのパスワード

### 複数のツリーをホストするための設定

以下の設定は、[複数のツリーをホストする](multi-tree.md)際に関連します。

キー | 説明
----|-------------
`MEDIA_PREFIX_TREE` | ブール値、各ツリーのメディアファイル用に別のサブフォルダを使用するかどうか。デフォルトは`False`ですが、マルチツリーセットアップでは`True`を使用することを強く推奨します。
`NEW_DB_BACKEND` | 新しく作成されたファミリーツリーに使用するデータベースバックエンド。`sqlite`または`sharedpostgresql`のいずれかでなければなりません。デフォルトは`sqlite`です。値`postgresql`は依然として受け入れられますが、将来のバージョンでPostgreSQLバックエンドが削除されるため、非推奨です。
`POSTGRES_HOST` | SharedPostgreSQLバックエンドを使用してマルチツリーセットアップで新しいツリーを作成する際に使用されるPostgreSQLサーバーのホスト名
`POSTGRES_PORT` | SharedPostgreSQLバックエンドを使用してマルチツリーセットアップで新しいツリーを作成する際に使用されるPostgreSQLサーバーのポート

### OIDC認証用の設定

これらの設定は、外部プロバイダーとのOpenID Connect（OIDC）認証を使用する場合に必要です。詳細なセットアップ手順と例については、[OIDC認証](oidc.md)を参照してください。

キー | 説明
----|-------------
`OIDC_ENABLED` | ブール値、OIDC認証を有効にするかどうか。デフォルトは`False`です。
`OIDC_ISSUER` | OIDCプロバイダーの発行者URL（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_ID` | OAuthクライアントID（カスタムOIDCプロバイダー用）
`OIDC_CLIENT_SECRET` | OAuthクライアントシークレット（カスタムOIDCプロバイダー用）
`OIDC_NAME` | プロバイダーのカスタム表示名。デフォルトは「OIDC」です。
`OIDC_SCOPES` | OAuthスコープ。デフォルトは「openid email profile」です。
`OIDC_USERNAME_CLAIM` | ユーザー名に使用するクレーム。デフォルトは「preferred_username」です。
`OIDC_OPENID_CONFIG_URL` | オプション：OpenID Connect構成エンドポイントへのURL（標準の`/.well-known/openid-configuration`を使用しない場合）
`OIDC_DISABLE_LOCAL_AUTH` | ブール値、ローカルのユーザー名/パスワード認証を無効にするかどうか。デフォルトは`False`です。
`OIDC_AUTO_REDIRECT` | ブール値、プロバイダーが1つだけ設定されている場合に自動的にOIDCにリダイレクトするかどうか。デフォルトは`False`です。

#### 組み込みOIDCプロバイダー

組み込みプロバイダー（Google、Microsoft）には、次の設定を使用します。

キー | 説明
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuthのクライアントID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuthのクライアントシークレット
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuthのクライアントID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuthのクライアントシークレット

#### OIDCロールマッピング

これらの設定を使用すると、アイデンティティプロバイダーからのOIDCグループ/ロールをGramps Webユーザーロールにマッピングできます。

キー | 説明
----|-------------
`OIDC_ROLE_CLAIM` | ユーザーのグループ/ロールを含むOIDCトークン内のクレーム名。デフォルトは「groups」です。
`OIDC_GROUP_ADMIN` | Grampsの「Admin」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_OWNER` | Grampsの「Owner」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_EDITOR` | Grampsの「Editor」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_CONTRIBUTOR` | Grampsの「Contributor」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_MEMBER` | Grampsの「Member」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名
`OIDC_GROUP_GUEST` | Grampsの「Guest」ロールにマッピングされるOIDCプロバイダーからのグループ/ロール名

### AI機能専用の設定

これらの設定は、チャットやセマンティック検索などのAI駆動の機能を使用する場合に必要です。

キー | 説明
----|-------------
`LLM_BASE_URL` | OpenAI互換のチャットAPIのベースURL。デフォルトは`None`で、OpenAI APIを使用します。
`LLM_MODEL` | OpenAI互換のチャットAPIで使用するモデル。未設定の場合（デフォルト）、チャットは無効になります。v3.6.0以降、AIアシスタントはツール呼び出し機能を持つPydantic AIを使用します。
`VECTOR_EMBEDDING_MODEL` | セマンティック検索のベクトル埋め込みに使用するモデル。ローカルモデルを使用する場合、これは[Sentence Transformers](https://sbert.net/)のモデル名である必要があります。リモートAPIを使用する場合（`VECTOR_EMBEDDING_BASE_URL`を参照）、これはリモートプロバイダーに渡されるモデル名です。未設定の場合（デフォルト）、セマンティック検索とチャットは無効になります。
`VECTOR_EMBEDDING_BASE_URL` | リモートOpenAI互換の埋め込みAPIのベースURL（例：Ollama、OpenAI、LiteLLM）。未設定の場合（デフォルト）、ローカルのSentence Transformersモデルが使用されます。詳細については[リモート埋め込みAPIの使用](chat.md#using-a-remote-embedding-api)を参照してください。
`VECTOR_EMBEDDING_API_KEY` | 認証されたリモート埋め込みプロバイダーのAPIキー。`VECTOR_EMBEDDING_BASE_URL`が設定されていて、プロバイダーが認証を必要とする場合にのみ必要です。
`LLM_MAX_CONTEXT_LENGTH` | LLMに提供されるファミリーツリーコンテキストの文字制限。デフォルトは50000です。
`LLM_SYSTEM_PROMPT` | LLMチャットアシスタント用のカスタムシステムプロンプト（v3.6.0+）。未設定の場合、デフォルトの系譜最適化プロンプトが使用されます。

## 例の構成ファイル

本番用の最小限の構成ファイルは次のようになります。
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # ポート465用に暗黙のSSLを使用
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # あなたのSMTPパスワード
DEFAULT_FROM_EMAIL="gramps@example.com"
