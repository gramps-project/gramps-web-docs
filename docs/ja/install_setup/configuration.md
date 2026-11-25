# サーバー設定

デフォルトの Docker イメージを使用する場合、必要な設定はすべてブラウザーから行えます。ただし、デプロイ方法によっては、サーバー設定をカスタマイズする必要があります。

このページでは、設定を変更するすべての方法と、既存のすべての設定オプションを一覧にしています。


## 設定ファイルと環境変数

設定には、設定ファイルまたは環境変数を使用できます。

[Docker Compose ベースのセットアップ](deployment.md)を使用する場合は、`grampsweb:` ブロックの `volumes:` キーの下に次のリスト項目を追加することで、設定ファイルを含めることができます。

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
ここで、`/path/to/config.cfg` はサーバーのファイルシステム上の設定ファイルへのパスです（右辺はコンテナ内のパスを指しており、変更してはいけません）。

環境変数を使用する場合は、

- すべての設定名の先頭に `GRAMPSWEB_` を付けて、環境変数の名前にします
- ネストされた辞書設定には二重アンダースコアを使用します。たとえば、`GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` を設定すると、`THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` 設定オプションの値が設定されます

環境を介して設定された設定オプションは、設定ファイル内の設定よりも優先されることに注意してください。両方が存在する場合は、環境変数が優先されます。

!!! warning "プレフィックスのない環境変数は非推奨です"
    歴史的な理由により、一部の設定（`TREE`、`SECRET_KEY`、`USER_DB_URI`、`POSTGRES_USER`、`POSTGRES_PASSWORD`、`MEDIA_BASE_DIR`、`SEARCH_INDEX_DIR`、`EMAIL_HOST`、`EMAIL_PORT`、`EMAIL_HOST_USER`、`EMAIL_HOST_PASSWORD`、`DEFAULT_FROM_EMAIL`、`BASE_URL`、`STATIC_PATH`）は、`GRAMPSWEB_` プレフィックスなしの環境変数でも設定できます。これは非推奨であり、起動時に警告がログに記録され、将来のリリースでは機能しなくなります。常にプレフィックス付きの形式を使用してください。たとえば、`TREE` の代わりに `GRAMPSWEB_TREE` を使用します。

    これは環境変数にのみ関係します。設定ファイルでは、設定名は常にプレフィックスなしで使用します。

!!! tip "非推奨オプションの確認"
    サーバーが依然として使用している非推奨の設定オプション（プレフィックスのない環境変数、`SEARCH_INDEX_DIR`、`EMAIL_USE_TLS` など）は、起動時に警告としてログに記録されます。Gramps Web API 3.22 以降では、管理者としてログインしている場合、これらのオプションは、置き換え先およびサポートが削除されるバージョンとともに、**システム情報**ページ（上部のアプリバーにあるユーザーアイコンからアクセス可能）の上部にも一覧表示されます。

    旧バージョンの初回起動ウィザードがデータベースに保存したメール設定とベース URL も、ここに一覧表示されます。保存されている値を設定に指定してください。値が一致すると、警告は表示されなくなります。

## 既存の設定

次の設定オプションが存在します。

### 必須設定

キー | 説明
----|-------------
`TREE` | 使用する家系図データベースの名前です。`gramps -l` で利用可能な家系図を表示できます。この名前の家系図が存在しない場合は、新しい空の家系図が作成されます。
`SECRET_KEY` | Flask 用の秘密鍵です。秘密鍵を公開してはいけません。変更すると、すべてのアクセストークンが無効になります。
`USER_DB_URI` | ユーザーデータベースのデータベース URL です。SQLAlchemy と互換性のある任意の URL を使用できます。

!!! info
    次のコマンドなどを使用して、安全な秘密鍵を生成できます。

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### オプション設定

キー | 説明
----|-------------
`MEDIA_BASE_DIR` | メディアファイルのベースディレクトリとして使用するパスです。Gramps で設定されたメディアのベースディレクトリを上書きします。[S3](s3.md) を使用する場合は、`s3://<bucket_name>` の形式で指定する必要があります。
`TREE_ID` | シングルツリーモード（`TREE` が `*` に設定されていない場合）で使用する家系図データベースのディレクトリ名です。設定すると、サーバーは表示名ではなくディレクトリ名で家系図を識別するため、名前変更に対してより堅牢になります。API を介して家系図の名前を変更する場合に必要です。ディレクトリ名は `GET /api/trees/-` の `id` フィールドで確認できます。
`SEARCH_INDEX_DB_URI` | 検索インデックスのデータベース URL です。バックエンドとして使用できるのは `sqlite` または `postgresql` のみです。デフォルトは `sqlite:///indexdir/search_index.db` で、スクリプトの実行場所を基準とした `indexdir` フォルダー内に SQLite ファイルを作成します。
`SEARCH_INDEX_DIR` | **非推奨**（代わりに `SEARCH_INDEX_DB_URI` を使用してください）。検索インデックスを含むディレクトリです。`SEARCH_INDEX_DB_URI` が未設定の状態でこの値を設定すると、検索インデックス URL は `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` から生成されます。
`STATIC_PATH` | 静的ファイル（静的 Web フロントエンドなど）を提供するパスです。
`BASE_URL` | API に到達できるベース URL です（例: `https://mygramps.mydomain.com/`）。正しいパスワードリセットリンクを作成するためなどに必要です。Web Push には、公開到達可能な HTTPS URL も必要です。デフォルトの `http://localhost/` では Web Push が無効になります。環境を介してこの設定を行う場合は、`GRAMPSWEB_BASE_URL` を使用してください。
`CORS_ORIGINS` | CORS リクエストを許可するオリジンです。デフォルトでは、すべてのオリジンが拒否されます。任意のドメインからのリクエストを許可するには、`"*"` を使用します。
`EMAIL_HOST` | SMTP サーバーのホストです（パスワードリセットメールの送信などに使用します）。
`EMAIL_PORT` | SMTP サーバーのポートです。デフォルトは 465 です。
`EMAIL_HOST_USER` | SMTP サーバーのユーザー名です。
`EMAIL_HOST_PASSWORD` | SMTP サーバーのパスワードです。
`EMAIL_USE_TLS` | **非推奨**（代わりに `EMAIL_USE_SSL` または `EMAIL_USE_STARTTLS` を使用してください）。メール送信時に TLS を使用するかどうかを示すブール値です。デフォルトは `True` です。STARTTLS を使用する場合は、これを `False` に設定し、25 以外のポートを使用してください。
`EMAIL_USE_SSL` | SMTP に暗黙的な SSL/TLS を使用するかどうかを示すブール値です（v3.6.0 以降）。`EMAIL_USE_TLS` が明示的に設定されていない場合のデフォルトは `True` です。通常はポート 465 と組み合わせて使用します。
`EMAIL_USE_STARTTLS` | SMTP に明示的な STARTTLS を使用するかどうかを示すブール値です（v3.6.0 以降）。デフォルトは `False` です。通常はポート 587 または 25 と組み合わせて使用します。
`DEFAULT_FROM_EMAIL` | 自動送信メールの「From」アドレスです。
`THUMBNAIL_CACHE_CONFIG` | サムネイルキャッシュの設定を含む辞書です。使用可能な設定については、[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) を参照してください。
`REQUEST_CACHE_CONFIG` | リクエストキャッシュの設定を含む辞書です。使用可能な設定については、[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) を参照してください。
`PERSISTENT_CACHE_CONFIG` | 永続キャッシュの設定を含む辞書です。テレメトリなどに使用されます。使用可能な設定については、[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) を参照してください。
`CELERY_CONFIG` | Celery バックグラウンドタスクキューの設定です。使用可能な設定については、[Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) を参照してください。
`REPORT_DIR` | Gramps レポートの実行結果が保存される一時ディレクトリです。
`EXPORT_DIR` | Gramps データベースのエクスポート結果が保存される一時ディレクトリです。
`BACKUP_DIR` | [バックアップ](../administration/backups.md)がツリーごとのサブディレクトリに保存されるディレクトリです（v3.24.0 以降）。未設定（デフォルト）の場合、バックアップをサーバーに保存することはできませんが、アップロードしたファイルから復元することはできます。Docker ボリュームなどの永続的な場所を使用し、できればその場所自体もバックアップまたは別の場所と同期してください。
`BACKUP_KEEP` | ツリーごとに保持する保存済みバックアップの数です。新しいバックアップが作成されると、古いバックアップが削除されます（v3.24.0 以降）。デフォルトは `5` です。
`RATE_LIMIT_BACKUP` | ツリーごとのバックアップ作成のレート制限です（v3.24.0 以降）。デフォルトは `"10 per day"` です。
`RATE_LIMIT_MEDIA_ARCHIVE` | エクスポートページでメディアアーカイブを作成する際のレート制限です。デフォルトは `"1 per hour"` です。
`REGISTRATION_DISABLED` | `True` の場合、新規ユーザー登録を禁止します（デフォルトは `False`）。Gramps Web API 3.26 以降では、ログインページの登録リンクも非表示になります。
`PROXY_FIX_X_FOR` | Gramps Web の前段にある信頼できるリバースプロキシの数です（v3.26.0 以降）。単一のリバースプロキシの背後では `1` に設定すると、レート制限がすべてのユーザーに一括で適用されず、クライアントごとに適用されます。デフォルトは `0` です。サーバーがこれらのプロキシ経由でのみ到達可能な場合に限り設定してください。
`DISABLE_TELEMETRY` | `True` の場合、統計テレメトリを無効にします（デフォルトは `False`）。詳細については、[テレメトリ](telemetry.md)を参照してください。
`PILLOW_MAX_IMAGE_PIXELS` | 処理可能な画像に含められるピクセル数を示す `PIL.Image.MAX_IMAGE_PIXELS` パラメーターを設定します。詳細については、[ドキュメント](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS)を参照してください。
`MAX_THUMBNAIL_FILE_BYTES` | サムネイルのファイルサイズにハード上限を設定します。デフォルトは `50 * 1024 * 1024`（50 MB）です。値を大きくするとメモリ使用量が大幅に増加し、大きなファイルがメモリ内で展開された場合に、メモリ不足によるクラッシュやデータ損失につながる可能性があります。


!!! info
    環境変数を使用して設定する場合、`EMAIL_USE_SSL` などのブール型オプションは、文字列 `true` または `false`（大文字と小文字を区別）で指定する必要があります。


### PostgreSQL データベースの設定

[SharedPostgreSQL アドオン](postgres.md)を使用して家系図を [PostgreSQL データベース](postgres.md)にホスティングする場合、これらの設定が必要です。

キー | 説明
----|-------------
`POSTGRES_USER` | データベース接続のユーザー名です。
`POSTGRES_PASSWORD` | データベースユーザーのパスワードです。


### 複数の家系図をホスティングする場合に関係する設定

[複数の家系図をホスティングする](multi-tree.md)場合、次の設定が関係します。


キー | 説明
----|-------------
`MEDIA_PREFIX_TREE` | 各家系図のメディアファイルに個別のサブフォルダーを使用するかどうかを示すブール値です。デフォルトは `False` ですが、複数の家系図を使用する構成では `True` にすることを強く推奨します。
`NEW_DB_BACKEND` | 新しく作成する家系図に使用するデータベースバックエンドです。`sqlite` または `sharedpostgresql` のいずれかである必要があります。デフォルトは `sqlite` です。値 `postgresql` も引き続き受け付けられますが、非推奨です。PostgreSQL バックエンドは Gramps Web API 4.0 で削除される予定です。
`POSTGRES_HOST` | SharedPostgreSQL バックエンドを使用する複数家系図構成で、新しい家系図の作成に使用する PostgreSQL サーバーのホスト名です。
`POSTGRES_PORT` | SharedPostgreSQL バックエンドを使用する複数家系図構成で、新しい家系図の作成に使用する PostgreSQL サーバーのポートです。


### OIDC 認証の設定

外部プロバイダーによる OpenID Connect（OIDC）認証を使用する場合は、これらの設定が必要です。詳細なセットアップ手順と例については、[OIDC 認証](oidc.md)を参照してください。

キー | 説明
----|-------------
`OIDC_ENABLED` | OIDC 認証を有効にするかどうかを示すブール値です。デフォルトは `False` です。
`OIDC_ISSUER` | OIDC プロバイダーの発行者 URL です（カスタム OIDC プロバイダー用）。
`OIDC_CLIENT_ID` | OAuth クライアント ID です（カスタム OIDC プロバイダー用）。
`OIDC_CLIENT_SECRET` | OAuth クライアントシークレットです（カスタム OIDC プロバイダー用）。
`OIDC_NAME` | プロバイダーのカスタム表示名です。デフォルトは `"OIDC"` です。
`OIDC_SCOPES` | OAuth スコープです。デフォルトは `"openid email profile"` です。
`OIDC_USERNAME_CLAIM` | ユーザー名に使用するクレームです。デフォルトは `"preferred_username"` です。
`OIDC_OPENID_CONFIG_URL` | オプションです。標準の `/.well-known/openid-configuration` を使用しない場合の OpenID Connect 設定エンドポイントの URL です。
`OIDC_PKCE` | PKCE を使用するかどうかを示すブール値です。未設定の場合、プロバイダーのディスカバリードキュメントに `S256` が記載されているときに PKCE が使用されます。[PKCE](oidc.md#pkce)を参照してください。
`OIDC_DISABLE_LOCAL_AUTH` | ローカルのユーザー名/パスワード認証を無効にするかどうかを示すブール値です。デフォルトは `False` です。
`OIDC_AUTO_REDIRECT` | プロバイダーが 1 つだけ設定されている場合に、自動的に OIDC へリダイレクトするかどうかを示すブール値です。デフォルトは `False` です。
`OIDC_ALLOWED_REDIRECT_URIS` | ネイティブアプリがログイン結果を受け取れる `https` URI のリストです（v3.26.0 以降）。環境変数では JSON リストとして設定します。デフォルトは空です。ネイティブアプリのドキュメントで要求されている場合にのみ必要です。[ネイティブアプリ](oidc.md#native-apps)を参照してください。

#### 組み込み OIDC プロバイダー

組み込みプロバイダー（Google、Microsoft）には、次の設定を使用します。

キー | 説明
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth のクライアント ID です。
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth のクライアントシークレットです。
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth のクライアント ID です。
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth のクライアントシークレットです。
`OIDC_GOOGLE_PKCE` | Google の PKCE 設定を示すブール値です。[PKCE](oidc.md#pkce)を参照してください。
`OIDC_MICROSOFT_PKCE` | Microsoft の PKCE 設定を示すブール値です。[PKCE](oidc.md#pkce)を参照してください。

#### OIDC ロールマッピング

これらの設定を使用すると、ID プロバイダーの OIDC グループ/ロールを Gramps Web ユーザーロールにマッピングできます。

キー | 説明
----|-------------
`OIDC_ROLE_CLAIM` | ユーザーのグループ/ロールを含む OIDC トークン内のクレーム名です。デフォルトは `"groups"` です。
`OIDC_GROUP_ADMIN` | Gramps の「Admin」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。
`OIDC_GROUP_OWNER` | Gramps の「Owner」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。
`OIDC_GROUP_EDITOR` | Gramps の「Editor」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。
`OIDC_GROUP_CONTRIBUTOR` | Gramps の「Contributor」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。
`OIDC_GROUP_MEMBER` | Gramps の「Member」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。
`OIDC_GROUP_GUEST` | Gramps の「Guest」ロールに対応付ける OIDC プロバイダーのグループ/ロール名です。

### AI 機能専用の設定

AI チャットを使用する場合は、これらの設定が必要です。詳細については、[AI チャットの設定](chat.md)を参照してください。

!!! note
    セマンティック検索用の `VECTOR_EMBEDDING_MODEL`、`VECTOR_EMBEDDING_BASE_URL`、`VECTOR_EMBEDDING_API_KEY` 設定は、セマンティック検索が削除された Gramps Web API 3.25 以降では無視されます。AI チャットで必要なのは `LLM_MODEL` のみです。

キー | 説明
----|-------------
`LLM_BASE_URL` | OpenAI 互換チャット API のベース URL です。デフォルトは `None` で、OpenAI API が使用されます。
`LLM_MODEL` | OpenAI 互換チャット API に使用するモデルです。未設定（デフォルト）の場合、チャットは無効になります。v3.6.0 以降、AI アシスタントはツール呼び出し機能を備えた Pydantic AI を使用します。
`LLM_MAX_OUTPUT_TOKENS` | 1 回の応答でモデルが生成できるトークンの最大数です。デフォルトでは未設定で、上限はモデルサーバーに委ねられます。独自の上限を持たないモデルサーバーで、応答が無限に続く可能性がある場合に便利です。
`LLM_MAX_CONTEXT_LENGTH` | LLM に提供する家系図コンテキストの文字数制限です。デフォルトは 50000 です。
`LLM_SYSTEM_PROMPT` | LLM チャットアシスタント用のカスタムシステムプロンプトです（v3.6.0 以降）。未設定の場合、系譜情報に最適化されたデフォルトのプロンプトが使用されます。
`LLM_VISION` | ユーザーが質問に画像を添付できるかどうかを示すブール値です（v3.26.0 以降）。モデルが画像を受け付ける場合にのみ有効にしてください。デフォルトは `False` です。[質問内の画像](chat.md#images-in-questions)を参照してください。
`LLM_ALLOW_WRITE_PROPOSALS` | アシスタントが、ユーザーによる確認と適用のために家系図への変更を提案できるかどうかを示すブール値です（v3.26.0 以降）。デフォルトは `False` です。[アシスタントによる変更提案を許可する](chat.md#letting-the-assistant-propose-changes)を参照してください。


## 設定ファイルの例

本番環境用の最小限の設定ファイルは、次のようになります。
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
