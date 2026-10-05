# OIDC 認証

Gramps Web は OpenID Connect (OIDC) 認証をサポートしており、ユーザーは外部のアイデンティティプロバイダーを使用してログインできます。これには、組み込みのプロバイダーである Google と Microsoft、さらに Keycloak、Authentik、Authelia などのカスタム OIDC プロバイダーが含まれます。

!!! warning "GitHub を OIDC プロバイダーとして使用することはサポートされていません"
    以前のバージョンから `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` が設定されている場合は、それらを削除してください – 現在は無視され、以前に GitHub 経由でサインインしたユーザーはその方法でログインできなくなります。GitHub は OAuth 2.0 プロバイダーであり、OpenID Connect プロバイダーではなく、Gramps Web がアイデンティティに依存するクレームを返すことはなかったため、信頼性が完全ではありませんでした。

## 概要

OIDC 認証を使用すると、次のことが可能です：

- ユーザー認証のために外部アイデンティティプロバイダーを使用する
- 複数の認証プロバイダーを同時にサポートする
- OIDC グループ/ロールを Gramps Web ユーザーロールにマッピングする
- シングルサインオン (SSO) およびシングルサインアウトを実装する
- 必要に応じてローカルのユーザー名/パスワード認証を無効にする

## 設定

OIDC 認証を有効にするには、Gramps Web の設定ファイルまたは環境変数に適切な設定を構成する必要があります。利用可能な OIDC 設定の完全なリストについては、[サーバー設定](configuration.md#settings-for-oidc-authentication) ページを参照してください。

!!! info
    環境変数を使用する場合は、各設定名の前に `GRAMPSWEB_` を付けることを忘れないでください (例: `GRAMPSWEB_OIDC_ENABLED`)。詳細については、[設定ファイルと環境変数](configuration.md#configuration-file-vs-environment-variables) を参照してください。

### 組み込みプロバイダー

Gramps Web は人気のあるアイデンティティプロバイダーに対して組み込みのサポートを提供しています。それらを使用するには、クライアント ID とクライアントシークレットを提供するだけです：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` と `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` と `OIDC_MICROSOFT_CLIENT_SECRET`

複数のプロバイダーを同時に構成できます。システムは、設定値に基づいてどのプロバイダーが利用可能かを自動的に検出します。

!!! tip "Microsoft: シングルテナントデプロイメント"
    組み込みの Microsoft プロバイダーは、マルチテナントの `/common` エンドポイントを使用し、設計上、任意の Microsoft アカウントからのログインを受け入れます。自分のテナントからのユーザーのみを許可したい場合は、[カスタム OIDC プロバイダー](#custom-oidc-providers) を使用して、テナント固有の発行者 URL を指定してください。これにより、発行者の検証がアクティブになり、そのテナントへのログインが制限されます。

### カスタム OIDC プロバイダー

カスタム OIDC プロバイダー (Keycloak、Authentik、Authelia、またはシングルテナントの Microsoft Entra テナントなど) の場合は、次の設定を使用します：

| キー                     | 説明                                                                                     |
|------------------------|----------------------------------------------------------------------------------------|
| `OIDC_ENABLED`        | OIDC 認証を有効にするかどうかのブール値。`True` に設定します。                          |
| `OIDC_ISSUER`        | プロバイダーの発行者 URL。ディスカバリーは `<issuer>/.well-known/openid-configuration` から取得されます。 |
| `OIDC_CLIENT_ID`     | OIDC プロバイダーのクライアント ID                                                      |
| `OIDC_CLIENT_SECRET`  | OIDC プロバイダーのクライアントシークレット                                              |
| `OIDC_NAME`          | カスタム表示名 (オプション、デフォルトは "OIDC")                                       |
| `OIDC_SCOPES`        | OAuth スコープ (オプション、デフォルトは "openid email profile")                       |
| `OIDC_USERNAME_CLAIM` | ユーザー名を生成するために使用されるクレーム (オプション、デフォルトは "preferred_username") |
| `OIDC_PKCE`          | PKCE を使用するかどうか、[PKCE](#pkce) を参照 (オプション、プロバイダーがサポートしている場合は自動的に有効) |

### PKCE

Gramps Web API 3.23 以降、Gramps Web は [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256` メソッド) を認可コードフローに対してサポートしています。一部のアイデンティティプロバイダー (Pocket ID など) は、クライアントに対して PKCE を *要求する* ように構成でき、これを使用しないログインを拒否します。古いバージョンの Gramps Web API は PKCE を使用しないため、そのようなクライアントでのログインは失敗します。

PKCE を使用するかどうかは、ログイン時に次のように決定されます：

- `OIDC_PKCE` が `True` に設定されている場合、PKCE が使用されます。
- `OIDC_PKCE` が `False` に設定されている場合、プロバイダーがサポートしていても PKCE は使用されません。
- `OIDC_PKCE` が設定されていない、または設定されているが空の場合、プロバイダーのディスカバリードキュメント (`/.well-known/openid-configuration`) に `code_challenge_methods_supported` に `S256` がリストされている場合は PKCE が使用され、それ以外の場合は使用されません。

ほとんどのセットアップでは、何も設定する必要はありません。プロバイダーが PKCE を要求するが、ディスカバリードキュメントに `S256` を広告していない場合は `OIDC_PKCE` を `True` に設定し、プロバイダーが `S256` を広告しているがそれを誤って処理している場合は `False` に設定します。環境変数として、ブール値は小文字でなければなりません (`GRAMPSWEB_OIDC_PKCE=true`)、[設定](configuration.md) を参照してください。

組み込みプロバイダーの場合、対応するオプションは `OIDC_GOOGLE_PKCE` と `OIDC_MICROSOFT_PKCE` です。

PKCE コード検証子は、プロバイダーへのリダイレクトとコールバックの間にユーザーのセッションに保持されるため、リダイレクト URI の変更は必要ありません。

### マルチツリーセットアップ

マルチツリーサーバーでは、ユーザーがログインするツリーを Gramps Web がアイデンティティプロバイダーにリダイレクトする前に知っている必要があるため、ログインは次のように開始されます：

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` はマルチツリーセットアップでは必須です。これを省略したり、存在しないツリーの ID を渡したりすると、ログインは失敗します。シングルツリーサーバーでは `tree` はオプションですが、指定された場合は設定された `TREE` と一致する必要があります。

OIDC アイデンティティは、正確に 1 つの Gramps Web アカウントにバインドされており、そのアカウントは正確に 1 つのツリーに属します – 異なるツリーに対してログインすると失敗し、アカウントが移動することはありません。プロバイダーで単一のアイデンティティを複数のツリーのアカウントにリンクする方法はありません。複数のツリーにアクセスする必要があるユーザーは、プロバイダーで別々のアイデンティティを持つ必要があります (例: 異なるユーザー名やアカウント)。

!!! warning
    関連付けられたツリーがないサイト管理者アカウント (詳細は [管理者アカウントの作成](../administration/owner.md) を参照) は OIDC 経由でログインできません。OIDC ログインは常にツリーを必要とします。そのようなアカウントは、ローカルのユーザー名/パスワードで作成および認証する必要があります。

## 必要なリダイレクト URI

OIDC プロバイダーを構成する際は、次のリダイレクト URI を登録する必要があります：

**ワイルドカードをサポートする OIDC プロバイダーの場合: (例: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

ここで `*` は正規表現のワイルドカードです。プロバイダーの正規表現インタープリターによっては、これも `.*` やそれに類似したものになる可能性があります。
プロバイダーが必要とする場合は、正規表現が有効になっていることを確認してください (例: Authentik)。

**ワイルドカードをサポートしない OIDC プロバイダーの場合: (例: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

ツリーはリダイレクト URI の一部にはならず、マルチツリーサーバーでも同様です – リダイレクト URI は登録されたものと正確に一致する必要があるため、セッション内で別に移動します。

## ロールマッピング

Gramps Web は、アイデンティティプロバイダーからの OIDC グループまたはロールを Gramps Web ユーザーロールに自動的にマッピングできます。これにより、アイデンティティプロバイダーでユーザーの権限を中央管理できます。ロールマッピングは、すべてのプロバイダー (組み込みまたはカスタム) で同じ方法で機能します。

### 設定

ロールマッピングを構成するには、次の設定を使用します：

| キー                     | 説明                                                                                     |
|------------------------|----------------------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | ユーザーのグループ/ロールを含む OIDC トークン内のクレーム名。デフォルトは "groups"。ドットパスがサポートされています (例: `realm_access.roles`)。 |
| `OIDC_GROUP_ADMIN`     | Gramps の "Admin" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                             |
| `OIDC_GROUP_OWNER`     | Gramps の "Owner" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                             |
| `OIDC_GROUP_EDITOR`    | Gramps の "Editor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                            |
| `OIDC_GROUP_CONTRIBUTOR` | Gramps の "Contributor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                      |
| `OIDC_GROUP_MEMBER`    | Gramps の "Member" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                            |
| `OIDC_GROUP_GUEST`     | Gramps の "Guest" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                             |

### ロールマッピングの動作

`OIDC_GROUP_*` 設定が全く構成されていない場合、ロールマッピングはオフになり、ロールは Gramps Web で手動で管理されます。そのため、新しい OIDC アカウントは無効の状態で作成され、既存のオーナーまたは管理者によって承認される必要があります (詳細は [最初のログインとブートストラップ](#first-login-and-bootstrapping) を参照)。

ロールマッピングが構成されると、毎回のログイン時に次のようになります：

- ロールクレームが存在し、ユーザーがマッピングされたグループに属している場合、対応するロールが付与されます。
- ロールクレームが存在するが、ユーザーがマッピングされたグループに属していない場合、そのロールは無効に設定されます。これはデフォルトのフェイルクローズであり、バグではありません – Gramps Web は認識していないグループに対してロールを推測できません。
- ロールクレームがトークンから完全に欠落している場合、既存のロールは変更されず、新しいアカウントは無効のままです。

!!! warning "Google はグループクレームを送信しません"
    Google のトークンには決して `groups` クレームが含まれないため、ロールマッピングが有効になっている場合、Google ログインは上記の "クレームが欠落" に該当します: 既存のユーザーはロールを保持しますが、新しい Google ユーザーは無効の状態で作成され、手動での承認が必要です。別のプロバイダーのためだけにロールマッピングを有効にする前に、これを考慮してください – それ自体では既存の Google ユーザーを無効にすることはありません。

Microsoft Entra は、アプリロールとグループメンバーシップを ID トークン内でのみ返し、ユーザー情報エンドポイントからは返しません。Gramps Web は ID トークンのクレームをユーザー情報の応答に統合するため、`OIDC_ROLE_CLAIM` は他のプロバイダーと同じように機能します。両方にクレームが含まれている場合、ユーザー情報の値が優先されます。

## 最初のログインとブートストラップ

OIDC 経由で作成された新しいアカウントは、ロールマッピングがロールを割り当てない限り無効の状態で開始されます (上記を参照)。真新しいインスタンスでは、誰も無効なアカウントを承認できず、`OIDC_DISABLE_LOCAL_AUTH` も有効になっている場合、パスワードログインに頼ることもできません。

!!! warning "最初のログイン前にオーナー/管理者グループを設定する"
    誰かが初めて OIDC 経由でログインする前に、`OIDC_GROUP_OWNER` (または `OIDC_GROUP_ADMIN`) を設定し、最初のユーザーがプロバイダーのそのグループに属していることを確認してください。そうしないと、インスタンスは OIDC 経由でブートストラップできなくなります。

## アカウントとユーザー名

OIDC 経由で作成されたアカウントには、アカウント作成時に一度割り当てられ、その後のログインでは変更されない生成されたユーザー名が付与されます：

- 組み込みプロバイダー: `<provider>_<claim value>`、例: `microsoft_alice@contoso.com`
- カスタムプロバイダー: ベアクレーム値、例: `alice`

衝突が発生した場合は数値のサフィックスが追加されます。OIDC によって作成されたアカウントのユーザー名を後から変更する方法はありません。一方、フルネームとメールアドレスは、毎回のログイン時に更新されます。

OIDC ログインは、たまたま同じメールアドレスを共有する既存のローカルアカウントに結びつくことはありません – これは意図的です。メールによるアカウントリンクはアカウント乗っ取りのベクターとなるためです。すでにローカルアカウントを持っているユーザーは、OIDC 経由で初めてログインする際に、別の独立したアカウントを取得します。

プロバイダーからのメールアドレスは、プロバイダーがそれを確認済みとしてマークする場合 (または `email_verified` クレームを完全に省略する場合) にのみ保存されます。それ以外の場合、メールアドレスを保存せずにログインが進行します。メールアドレスは一意である必要はないため (Gramps Web API 3.22 以降)、他のアカウントがすでに使用している場合でもアドレスが保存されます。

## OIDC ログアウト

Gramps Web は OIDC プロバイダーに対してシングルサインアウト (SSO ログアウト) をサポートしています。`GET /api/oidc/logout/` はプロバイダーの `end_session_endpoint` を検索し、応答内の `logout_url` として返します。実際にアイデンティティプロバイダーでセッションを終了するために、ブラウザをそこにナビゲートするのは Gramps Web フロントエンドです。プロバイダーに `end_session_endpoint` がない場合、`logout_url` は `null` になります。

!!! warning "ログアウト時にトークンは無効になりません"
    ログアウトはブラウザセッションを終了するだけです。すでに発行された Gramps Web トークンを無効にする方法は現在ありません。トークンは、ユーザーが Gramps Web またはアイデンティティプロバイダーでログアウトしたかどうかに関係なく、有効期限が切れるまで有効です (`JWT_ACCESS_TOKEN_EXPIRES`、デフォルトはアクセストークンの 15 分)。

## トラブルシューティング

ログインが停止するポイントから始めて、分岐をたどります。Gramps Web は失敗したコールバックの理由をログに記録します (サーバーログで `OIDC callback error for provider` を探してください)。これは通常、ブラウザに表示されるメッセージよりも具体的です。

**1. ログインボタンが見当たりませんか？**

- `<BASE_URL>/api/oidc/config/` を確認してください。`enabled` が `false` であるか、`providers` が空である場合、OIDC は構成されていません: `OIDC_ENABLED` は `True` に設定する必要があり、カスタムプロバイダーには `OIDC_ISSUER` と `OIDC_CLIENT_ID` の両方が必要です。
- 組み込みプロバイダー (Google、Microsoft) は、クライアント ID とクライアントシークレットの両方が設定されている場合にのみ登録されます。
- サーバーログの起動時に `Could not load discovery document` を探してください。これは、サーバーが `<issuer>/.well-known/openid-configuration` (または `OIDC_OPENID_CONFIG_URL`) に到達できなかったことを意味します。最初の使用時に再試行しますが、Gramps Web コンテナは、ブラウザだけでなく、発行者 URL 自体を解決して到達できる必要があります。

**2. ブラウザがプロバイダーに送信された直後にエラーが表示されますか？**

エラーはアイデンティティプロバイダーによって表示され、ログイン前に発生します。

- *"redirect URI mismatch"* (または類似): プロバイダーに登録されたリダイレクト URI は、スキーム、ホスト、ポート、プロバイダー ID を含めて正確に一致する必要があります。[必要なリダイレクト URI](#required-redirect-uris) を参照してください。これは `BASE_URL` から構成されるため、誤った `BASE_URL` は誤ったリダイレクト URI を生成します。
- *PKCE エラー* (例: `invalid_request`、"code challenge required"、または `code_challenge` パラメーターが欠落): プロバイダーが PKCE を要求していますが、Gramps Web がそれを送信しませんでした。[PKCE ブランチ](#pkce-branch) に移動してください。

**3. プロバイダーがログインを受け入れますが、Gramps Web がエラーを表示しますか？**

- *`mismatching_state`、またはエラーがセッションまたは状態に言及している*: ブラウザがログインが開始されたときに Gramps Web が設定したセッションクッキーを返しませんでした。このクッキーには PKCE コード検証子も含まれています。ブラウザのアドレスが `BASE_URL` と一致していることを確認し (同じスキームとホスト)、リバースプロキシがクッキーと元のホストを通過させ、ログインが同じブラウザタブまたはウィンドウで開始され、完了することを確認してください。
- *`OIDC authentication failed for <provider>` (HTTP 401)*: 根本的な理由を確認するためにサーバーログをチェックしてください。一般的な原因は、誤ったクライアントシークレット、トークンの `iss` クレームと一致しない発行者 URL、およびプロバイダーがコールバックにエラーを返すことです (例: PKCE、以下を参照)。
- *試行回数が多すぎます*: ログインおよびコールバックエンドポイントはレート制限されています (1 分あたり 5 リクエスト)。1 分待ってから再試行してください。

**4. ログインは成功しますが、「アカウントがレビュー中」と表示される、または何もできませんか？**

新しいアカウントは、ロールマッピングがロールを割り当てない限り無効の状態で作成されます。[最初のログインとブートストラップ](#first-login-and-bootstrapping) および [ロールマッピングの動作](#role-mapping-behavior) を参照してください。管理者は、設定 > 管理 > ユーザー管理の下でアカウントを有効にすることもできます。

### PKCE ブランチ

Gramps Web は、ログインが開始されるときに PKCE を使用するかどうかを決定します (詳細は [PKCE](#pkce) を参照)。セットアップで何が起こったかを確認するために、次の質問を順番に確認してください：

1. **`OIDC_PKCE` は設定されていますか？** (組み込みプロバイダーの場合、`OIDC_GOOGLE_PKCE` または `OIDC_MICROSOFT_PKCE`。)
    - `True`: PKCE が使用されます。質問 3 にスキップします。
    - `False`: PKCE は意図的にオフになっており、プロバイダーのディスカバリードキュメントは無視されます。プロバイダーが PKCE を要求する場合は、設定を削除するか `True` に設定してください。
    - 設定されていない、または空: 質問 2 に進みます。
2. **ディスカバリードキュメントに `S256` がリストされていますか？** `<issuer>/.well-known/openid-configuration` を開き、`code_challenge_methods_supported` に `S256` があるか確認してください。
    - はい: PKCE が自動的に使用されます。質問 3 に進みます。
    - いいえ、またはフィールドが欠落している: PKCE は **使用されません**。プロバイダーが必要とする場合は `OIDC_PKCE` を `True` に設定してください。また、サーバーログで `Could not check the provider for PKCE support` を確認してください。これは、ディスカバリードキュメントを取得できなかったことを意味し、PKCE がオフになってしまったことを示します。
3. **PKCE は本当に送信されましたか？** ログインを開始し、プロバイダーのログインページのアドレス (またはブラウザのネットワークタブでの最初のリダイレクト) を確認してください。`code_challenge=` と `code_challenge_method=S256` が含まれている必要があります。
    - 存在するが、ログインがコールバックで失敗する: プロバイダーがコード検証子を拒否しました。リダイレクトとコールバックの間にセッションクッキーが失われた可能性があります (上記のブランチ 3 を参照) または、プロバイダーが `S256` をサポートしていない場合は、プロバイダーが PKCE を要求しない場合は `OIDC_PKCE` を `False` に設定します。
    - 欠落: 上記の設定が適用されていません。環境変数が正しいプレフィックスと小文字の値を持っていることを確認してください (例: Docker での `GRAMPSWEB_OIDC_PKCE=true`; `True` はブール値として読み取られません)、サーバーを再起動し、設定を再確認してください。

!!! note
    プロバイダーで PKCE が *オプション* として有効になっている場合、またはまったく有効になっていない場合、Gramps Web がチャレンジを送信するかどうかに関係なく、ログインは機能します。PKCE を *要求* するように構成されたプロバイダー (またはクライアント) のみが、この設定を重要にします。

## 例の設定

### カスタム OIDC プロバイダー (Keycloak)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"

# カスタム OIDC 設定
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # オプション: SSO ログインに自動的にリダイレクト
OIDC_DISABLE_LOCAL_AUTH=True  # オプション: ユーザー名/パスワードログインを無効にする

# オプション: OIDC グループから Gramps ロールへのロールマッピング
OIDC_ROLE_CLAIM="groups"  # またはプロバイダーに応じて "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # ポート 465 用の暗黙の SSL を使用
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # あなたの SMTP パスワード
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### 組み込みプロバイダー (Google)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### 複数のプロバイダー

複数の OIDC プロバイダーを同時に有効にできます：

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # あなたの秘密鍵
USER_DB_URI="sqlite:////path/to/users.sqlite"

# カスタムプロバイダー
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Company SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

Pocket ID でリダイレクト URI `<BASE_URL>/api/oidc/callback/custom` を使用して OIDC クライアントを作成します (詳細は [必要なリダイレクト URI](#required-redirect-uris) を参照)。クライアントに対して "Require PKCE" を有効にする場合、Pocket ID がディスカバリードキュメントで PKCE サポートを広告しているため、追加の Gramps Web 設定は必要ありません。その後、次のように構成します：

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Gramps Web 用のコミュニティ製 OIDC セットアップガイドは、[公式 Authelia ドキュメントウェブサイト](https://www.authelia.com/integration/openid-connect/clients/gramps/) で入手できます。

### Keycloak

Keycloak の設定の大部分はデフォルトのままにできます (*クライアント → クライアントを作成 → クライアント認証 ON*)。
いくつかの例外があります：

1. **OpenID スコープ** – `openid` スコープはすべての Keycloak バージョンでデフォルトでは含まれていません。問題を避けるために手動で追加してください: *クライアント → [Gramps クライアント] → クライアントスコープ → スコープを追加 → 名前: `openid` → デフォルトとして設定。*
2. **ロール** – ロールはクライアントレベルまたはレルムごとにグローバルに割り当てることができます。

    * クライアントロールを使用している場合、`OIDC_ROLE_CLAIM` 設定オプションを次のように設定します: `resource_access.[gramps-client-name].roles`
    * Gramps にロールを表示させるには、*クライアントスコープ* (特定のクライアントの下ではなく、トップレベルのセクション) に移動し、次に: *ロール → マッパー → クライアントロール → ユーザー情報に追加 → ON.*
