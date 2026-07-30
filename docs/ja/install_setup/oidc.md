# OIDC 認証

Gramps Web は OpenID Connect (OIDC) 認証をサポートしており、ユーザーが外部のアイデンティティプロバイダーを使用してログインできるようにします。これには、組み込みのプロバイダーである Google や Microsoft、そして Keycloak、Authentik、Authelia のようなカスタム OIDC プロバイダーが含まれます。

!!! warning "GitHub を OIDC プロバイダーとして使用することはもはやサポートされていません"
    以前のバージョンから `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` を設定している場合は、それらを削除してください – 現在は無視されており、以前に GitHub 経由でサインインしたユーザーはその方法でログインできなくなります。GitHub は OAuth 2.0 プロバイダーであり、OpenID Connect プロバイダーではなく、Gramps Web がアイデンティティのために依存しているクレームを返すことはなかったため、完全には信頼できませんでした。

## 概要

OIDC 認証を使用すると、次のことが可能になります：

- ユーザー認証のために外部アイデンティティプロバイダーを使用する
- 複数の認証プロバイダーを同時にサポートする
- OIDC グループ/ロールを Gramps Web ユーザーロールにマッピングする
- シングルサインオン (SSO) とシングルサインアウトを実装する
- 必要に応じてローカルのユーザー名/パスワード認証を無効にする

## 設定

OIDC 認証を有効にするには、Gramps Web の設定ファイルまたは環境変数で適切な設定を構成する必要があります。利用可能な OIDC 設定の完全なリストについては、[サーバー設定](configuration.md#settings-for-oidc-authentication) ページを参照してください。

!!! info
    環境変数を使用する場合は、各設定名の前に `GRAMPSWEB_` を付けることを忘れないでください（例：`GRAMPSWEB_OIDC_ENABLED`）。詳細については、[設定ファイルと環境変数](configuration.md#configuration-file-vs-environment-variables) を参照してください。

### 組み込みプロバイダー

Gramps Web は、人気のあるアイデンティティプロバイダーの組み込みサポートを提供しています。これらを使用するには、クライアント ID とクライアントシークレットを提供するだけです：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` と `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` と `OIDC_MICROSOFT_CLIENT_SECRET`

複数のプロバイダーを同時に構成することができます。システムは、設定値に基づいてどのプロバイダーが利用可能かを自動的に検出します。

!!! tip "Microsoft: シングルテナントデプロイメント"
    組み込みの Microsoft プロバイダーはマルチテナントの `/common` エンドポイントを使用し、設計上、任意の Microsoft アカウントからのログインを受け入れます。自分のテナントのユーザーのみを許可したい場合は、テナント固有の発行者 URL を使用した [カスタム OIDC プロバイダー](#custom-oidc-providers) を使用してください。これにより、発行者の検証がアクティブになり、そのテナントへのログインが制限されます。

### カスタム OIDC プロバイダー

カスタム OIDC プロバイダー（Keycloak、Authentik、Authelia、またはシングルテナントの Microsoft Entra テナントなど）には、次の設定を使用します：

| キー                      | 説明                                                                 |
|-------------------------|----------------------------------------------------------------------|
| `OIDC_ENABLED`         | OIDC 認証を有効にするかどうかのブール値。`True` に設定します。              |
| `OIDC_ISSUER`         | プロバイダーの発行者 URL。ディスカバリーは `<issuer>/.well-known/openid-configuration` から取得されます。 |
| `OIDC_CLIENT_ID`      | OIDC プロバイダーのクライアント ID                                   |
| `OIDC_CLIENT_SECRET`   | OIDC プロバイダーのクライアントシークレット                             |
| `OIDC_NAME`           | カスタム表示名（オプション、デフォルトは "OIDC"）                     |
| `OIDC_SCOPES`         | OAuth スコープ（オプション、デフォルトは "openid email profile"）      |
| `OIDC_USERNAME_CLAIM`  | ユーザー名を生成するために使用されるクレーム（オプション、デフォルトは "preferred_username"） |

### マルチツリーセットアップ

マルチツリーサーバーでは、ユーザーがログインするツリーを Gramps Web がアイデンティティプロバイダーにリダイレクトする前に知っている必要があるため、ログインは次のように始まります：

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` はマルチツリーセットアップでは必須です。これを省略したり、存在しないツリーの ID を渡したりすると、ログインは失敗します。シングルツリーサーバーでは `tree` はオプションですが、指定された場合は構成された `TREE` と一致する必要があります。

OIDC アイデンティティは、正確に 1 つの Gramps Web アカウントにバインドされており、そのアカウントは正確に 1 つのツリーに属します – 異なるツリーに対してログインすると失敗し、アカウントが移動することはありません。プロバイダーの単一のアイデンティティを複数のツリーのアカウントにリンクする方法はなく、複数のツリーにアクセスする必要があるユーザーは、プロバイダーで別々のアイデンティティを持つ必要があります（例：異なるユーザー名またはアカウント）。

!!! warning
    関連するツリーがないサイト管理者アカウント（[管理者アカウントの作成](../administration/owner.md)を参照）は OIDC 経由でログインできません。なぜなら、OIDC ログインは常にツリーを必要とするからです。そのようなアカウントは、ローカルのユーザー名/パスワードで作成および認証する必要があります。

## 必要なリダイレクト URI

OIDC プロバイダーを構成する際には、次のリダイレクト URI を登録する必要があります：

**ワイルドカードをサポートする OIDC プロバイダーの場合：（例：Authentik）**

- `https://your-gramps-backend.com/api/oidc/callback/*`

ここで `*` は正規表現のワイルドカードです。プロバイダーの正規表現インタープリターによっては、これが `.*` または類似のものになることもあります。
プロバイダーが必要とする場合は、正規表現が有効になっていることを確認してください（例：Authentik）。

**ワイルドカードをサポートしない OIDC プロバイダーの場合：（例：Authelia）**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

ツリーはリダイレクト URI の一部にはならず、マルチツリーサーバーでも同様です – セッション内で別に移動します。プロバイダーは、リダイレクト URI が登録されたものと正確に一致することを要求します。

## ロールマッピング

Gramps Web は、アイデンティティプロバイダーからの OIDC グループまたはロールを Gramps Web ユーザーロールに自動的にマッピングできます。これにより、アイデンティティプロバイダーでユーザーの権限を中央で管理できます。ロールマッピングは、組み込みまたはカスタムのすべてのプロバイダーで同じように機能します。

### 設定

ロールマッピングを構成するには、次の設定を使用します：

| キー                     | 説明                                                                 |
|------------------------|----------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | ユーザーのグループ/ロールを含む OIDC トークン内のクレーム名。デフォルトは "groups"。ドットパスがサポートされています（例：`realm_access.roles`）。 |
| `OIDC_GROUP_ADMIN`    | Gramps の "Admin" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_OWNER`    | Gramps の "Owner" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_EDITOR`   | Gramps の "Editor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_CONTRIBUTOR` | Gramps の "Contributor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_MEMBER`   | Gramps の "Member" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_GUEST`    | Gramps の "Guest" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |

### ロールマッピングの動作

`OIDC_GROUP_*` 設定が全く構成されていない場合、ロールマッピングはオフになり、ロールは Gramps Web で手動で管理されます。この場合、新しい OIDC アカウントは無効として作成され、既存のオーナーまたは管理者によって承認される必要があります（以下の [初回ログインとブートストラップ](#first-login-and-bootstrapping) を参照）。

ロールマッピングが構成されると、毎回のログイン時に次のようになります：

- ロールクレームが存在し、ユーザーがマッピングされたグループに属している場合、対応するロールが付与されます。
- ロールクレームが存在するが、ユーザーがマッピングされたグループに属していない場合、そのロールは無効に設定されます。これはデフォルトのフェイルクローズであり、バグではありません – Gramps Web は認識していないグループのロールを推測できません。
- トークンからロールクレームが完全に欠如している場合、既存のロールは変更されず、新しいアカウントは依然として無効としてデフォルト設定されます。

!!! warning "Google はグループクレームを送信しません"
    Google のトークンには決して `groups` クレームが含まれないため、ロールマッピングが有効な場合、Google ログインは上記の "クレームが欠如" に該当します：既存のユーザーはそのロールを保持しますが、新しい Google ユーザーは無効として作成され、手動での承認が必要です。他のプロバイダーのためだけにロールマッピングを有効にする前にこれを考慮してください – それ自体では既存の Google ユーザーを無効にすることはありません。

Microsoft Entra は、アプリロールとグループメンバーシップを ID トークンでのみ返し、ユーザー情報エンドポイントからは返しません。Gramps Web は ID トークンのクレームをユーザー情報応答にマージし、`OIDC_ROLE_CLAIM` が他のプロバイダーと同じように機能するようにします；両方にクレームが含まれている場合、ユーザー情報の値が優先されます。

## 初回ログインとブートストラップ

OIDC 経由で作成された新しいアカウントは、ロールマッピングがロールを割り当てない限り無効から始まります（上記を参照）。真新しいインスタンスでは、誰も無効なアカウントを承認できず、`OIDC_DISABLE_LOCAL_AUTH` も有効になっている場合、パスワードログインにフォールバックすることもできません。

!!! warning "初回ログイン前にオーナー/管理者グループを構成してください"
    誰かが初めて OIDC 経由でログインする前に、`OIDC_GROUP_OWNER`（または `OIDC_GROUP_ADMIN`）を設定し、最初のユーザーがプロバイダーでそのグループに属していることを確認してください。そうしないと、インスタンスは OIDC 経由でブートストラップできなくなります。

## アカウントとユーザー名

OIDC 経由で作成されたアカウントには、生成されたユーザー名が付与され、アカウント作成時に一度割り当てられ、その後のログインでは変更されません：

- 組み込みプロバイダー：`<provider>_<claim value>`、例：`microsoft_alice@contoso.com`
- カスタムプロバイダー：ベアクレーム値、例：`alice`

衝突時には数値のサフィックスが追加されます。OIDC で作成されたアカウントのユーザー名を後から変更する方法はありません；対照的に、フルネームとメールアドレスは、毎回のログイン時に更新されます。

OIDC ログインは、たまたまメールアドレスを共有する既存のローカルアカウントに自動的に関連付けられることはありません – これは意図的であり、メールによるアカウントリンクはアカウント乗っ取りのベクトルです。すでにローカルアカウントを持っているユーザーは、初めて OIDC 経由でログインする際に、別の独立したアカウントを取得します。

プロバイダーからのメールアドレスは、プロバイダーがそれを確認済みとしてマークする場合（または `email_verified` クレームを完全に省略する場合）にのみ保存され、他のアカウントですでに使用されていない場合に限ります。それ以外の場合、ログインはメールアドレスを保存せずに進行します。

## OIDC ログアウト

Gramps Web は OIDC プロバイダーのためのシングルサインアウト (SSO ログアウト) をサポートしています。`GET /api/oidc/logout/` はプロバイダーの `end_session_endpoint` を調べ、応答の `logout_url` として返します；実際にアイデンティティプロバイダーでセッションを終了するために、ブラウザをそこにナビゲートするのは Gramps Web フロントエンドです。プロバイダーに `end_session_endpoint` がない場合、`logout_url` は `null` になります。

!!! warning "ログアウト時にトークンは無効になりません"
    ログアウトはブラウザセッションを終了するだけであり、すでに発行された Gramps Web トークンを無効にする方法は現在ありません。トークンは、ユーザーが Gramps Web またはアイデンティティプロバイダーでログアウトしたかどうかに関係なく、有効期限が切れるまで有効です（`JWT_ACCESS_TOKEN_EXPIRES`、デフォルトはアクセストークンの 15 分）。

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
OIDC_AUTO_REDIRECT=True  # オプション：SSO ログインに自動的にリダイレクト
OIDC_DISABLE_LOCAL_AUTH=True  # オプション：ユーザー名/パスワードログインを無効にする

# オプション：OIDC グループから Gramps ロールへのロールマッピング
OIDC_ROLE_CLAIM="groups"  # またはプロバイダーに応じて "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
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

複数の OIDC プロバイダーを同時に有効にすることができます：

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

### Authelia

Gramps Web 用のコミュニティ製 OIDC セットアップガイドは、[公式 Authelia ドキュメントウェブサイト](https://www.authelia.com/integration/openid-connect/clients/gramps/) で入手できます。

### Keycloak

Keycloak の設定のほとんどはデフォルトのままにしておくことができます（*クライアント → クライアントを作成 → クライアント認証 ON*）。
いくつかの例外があります：

1. **OpenID スコープ** – `openid` スコープはすべての Keycloak バージョンでデフォルトで含まれていません。問題を避けるために手動で追加してください：*クライアント → [Gramps クライアント] → クライアントスコープ → スコープを追加 → 名前: `openid` → デフォルトとして設定。*
2. **ロール** – ロールはクライアントレベルまたはレルムごとにグローバルに割り当てることができます。

    * クライアントロールを使用している場合、`OIDC_ROLE_CLAIM` 設定オプションを次のように設定します：`resource_access.[gramps-client-name].roles`
    * Gramps にロールを表示させるには、*クライアントスコープ*（特定のクライアントの下ではなく、トップレベルのセクション）に移動し、次に：*ロール → マッパー → クライアントロール → ユーザー情報に追加 → ON.*
