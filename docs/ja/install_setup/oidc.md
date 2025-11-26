# OIDC 認証

Gramps Web は OpenID Connect (OIDC) 認証をサポートしており、ユーザーが外部のアイデンティティプロバイダーを使用してログインできるようにします。これには、Google、Microsoft、GitHub などの人気のあるプロバイダーや、Keycloak、Authentik などのカスタム OIDC プロバイダーが含まれます。

## 概要

OIDC 認証を使用すると、次のことが可能になります。

- ユーザー認証のために外部のアイデンティティプロバイダーを使用する
- 複数の認証プロバイダーを同時にサポートする
- OIDC グループ/ロールを Gramps Web ユーザーロールにマッピングする
- シングルサインオン (SSO) とシングルサインアウトを実装する
- 必要に応じてローカルのユーザー名/パスワード認証を無効にする

## 設定

OIDC 認証を有効にするには、Gramps Web の設定ファイルまたは環境変数に適切な設定を構成する必要があります。利用可能な OIDC 設定の完全なリストについては、[サーバー設定](configuration.md#settings-for-oidc-authentication) ページを参照してください。

!!! info
    環境変数を使用する場合は、各設定名の前に `GRAMPSWEB_` を付けることを忘れないでください (例: `GRAMPSWEB_OIDC_ENABLED`)。詳細については、[設定ファイルと環境変数](configuration.md#configuration-file-vs-environment-variables) を参照してください。

### 組み込みプロバイダー

Gramps Web は人気のあるアイデンティティプロバイダーに対する組み込みサポートを提供しています。これらを使用するには、クライアント ID とクライアントシークレットを提供するだけです。

- **Google**: `OIDC_GOOGLE_CLIENT_ID` と `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` と `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` と `OIDC_GITHUB_CLIENT_SECRET`

複数のプロバイダーを同時に構成することができます。システムは、設定値に基づいて利用可能なプロバイダーを自動的に検出します。

### カスタム OIDC プロバイダー

カスタム OIDC プロバイダー (Keycloak、Authentik、または任意の標準 OIDC 準拠プロバイダーなど) の場合は、次の設定を使用します。

| キー | 説明 |
|----|-------------|
| `OIDC_ENABLED` | OIDC 認証を有効にするかどうかのブール値。`True` に設定します。 |
| `OIDC_ISSUER` | プロバイダーの発行者 URL |
| `OIDC_CLIENT_ID` | OIDC プロバイダーのクライアント ID |
| `OIDC_CLIENT_SECRET` | OIDC プロバイダーのクライアントシークレット |
| `OIDC_NAME` | カスタム表示名 (オプション、デフォルトは "OIDC") |
| `OIDC_SCOPES` | OAuth スコープ (オプション、デフォルトは "openid email profile") |

## 必要なリダイレクト URI

OIDC プロバイダーを構成する際には、次のリダイレクト URI を登録する必要があります。

**ワイルドカードをサポートする OIDC プロバイダーの場合: (例: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

ここで `*` は正規表現のワイルドカードです。プロバイダーの正規表現インタープリターによっては、これが `.*` または類似のものである可能性もあります。
プロバイダーが必要とする場合は、正規表現が有効になっていることを確認してください (例: Authentik)。

**ワイルドカードをサポートしない OIDC プロバイダーの場合: (例: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## ロールマッピング

Gramps Web は、アイデンティティプロバイダーからの OIDC グループまたはロールを Gramps Web ユーザーロールに自動的にマッピングできます。これにより、アイデンティティプロバイダーでユーザーの権限を中央管理できます。

### 設定

ロールマッピングを構成するには、次の設定を使用します。

| キー | 説明 |
|----|-------------|
| `OIDC_ROLE_CLAIM` | ユーザーのグループ/ロールを含む OIDC トークン内のクレーム名。デフォルトは "groups" |
| `OIDC_GROUP_ADMIN` | Gramps の "Admin" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_OWNER` | Gramps の "Owner" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_EDITOR` | Gramps の "Editor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_CONTRIBUTOR` | Gramps の "Contributor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_MEMBER` | Gramps の "Member" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |
| `OIDC_GROUP_GUEST` | Gramps の "Guest" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名 |

### ロールマッピングの動作

- ロールマッピングが構成されていない場合 (設定された `OIDC_GROUP_*` 変数がない場合)、既存のユーザーロールは保持されます
- ユーザーは、グループメンバーシップに基づいて与えられる最高のロールが割り当てられます
- ロールマッピングはデフォルトで大文字と小文字を区別します (OIDC プロバイダーによります)

## OIDC ログアウト

Gramps Web は OIDC プロバイダーのためのシングルサインアウト (SSO ログアウト) をサポートしています。ユーザーが OIDC を介して認証された後に Gramps Web からログアウトすると、プロバイダーが `end_session_endpoint` をサポートしている場合、アイデンティティプロバイダーのログアウトページに自動的にリダイレクトされます。

### バックチャネルログアウト

Gramps Web は OpenID Connect バックチャネルログアウト仕様を実装しています。これにより、アイデンティティプロバイダーは、ユーザーが別のアプリケーションまたはアイデンティティプロバイダー自体からログアウトしたときに Gramps Web に通知できます。

#### 設定

アイデンティティプロバイダーでバックチャネルログアウトを構成するには：

1. **アイデンティティプロバイダーのクライアント設定でバックチャネルログアウトエンドポイントを登録します**：
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **プロバイダーを構成して** ログアウト通知を送信します。具体的な手順はプロバイダーによって異なります：

   **Keycloak:**

   - クライアント設定で「設定」に移動します
   - 「バックチャネルログアウト URL」を `https://your-gramps-backend.com/api/oidc/backchannel-logout/` に設定します
   - セッションベースのログアウトを希望する場合は「バックチャネルログアウトセッションが必要」を有効にします

   **Authentik:**

   - プロバイダー設定でバックチャネルログアウト URL を追加します
   - プロバイダーがログアウトトークンを送信するように設定されていることを確認します

!!! warning "トークンの有効期限"
    JWT トークンのステートレスな性質のため、バックチャネルログアウトは現在ログアウトイベントを記録することはできますが、既に発行された JWT トークンを即座に取り消すことはできません。トークンは有効期限が切れるまで有効です (デフォルト: アクセストークンは 15 分)。

    セキュリティを強化するために、次のことを検討してください：

    - JWT トークンの有効期限を短くする (`JWT_ACCESS_TOKEN_EXPIRES`)
    - アイデンティティプロバイダーからログアウトする際に、Gramps Web から手動でログアウトするようにユーザーに教育する

!!! tip "動作の仕組み"
    ユーザーがアイデンティティプロバイダーまたは別のアプリケーションからログアウトすると：

    1. プロバイダーは Gramps Web のバックチャネルログアウトエンドポイントに `logout_token` JWT を送信します
    2. Gramps Web はトークンを検証し、ログアウトイベントを記録します
    3. ログアウトトークンの JTI がブロックリストに追加され、リプレイ攻撃を防ぎます
    4. ユーザーの JWT を使用した新しい API リクエストは、トークンが期限切れになると拒否されます

## 設定例

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

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Gramps Web のためのコミュニティ製 OIDC セットアップガイドは、[公式 Authelia ドキュメントウェブサイト](https://www.authelia.com/integration/openid-connect/clients/gramps/) で入手できます。

### Keycloak

Keycloak の設定のほとんどはデフォルトのままで問題ありません (*クライアント → クライアントを作成 → クライアント認証 ON*)。
いくつかの例外があります：

1. **OpenID スコープ** – `openid` スコープはすべての Keycloak バージョンでデフォルトで含まれているわけではありません。問題を避けるために手動で追加してください: *クライアント → [Gramps クライアント] → クライアントスコープ → スコープを追加 → 名前: `openid` → デフォルトとして設定。*
2. **ロール** – ロールはクライアントレベルまたはレルムごとにグローバルに割り当てることができます。

    * クライアントロールを使用している場合は、`OIDC_ROLE_CLAIM` 設定オプションを次のように設定します: `resource_access.[gramps-client-name].roles`
    * Gramps にロールを表示させるには、*クライアントスコープ* (特定のクライアントの下ではなく、トップレベルのセクション) に移動し、次に: *ロール → マッパー → クライアントロール → ユーザー情報に追加 → ON.*
