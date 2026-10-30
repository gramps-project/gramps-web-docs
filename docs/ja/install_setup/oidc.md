# OIDC 認証

Gramps Web は OpenID Connect (OIDC) 認証をサポートしており、ユーザーが外部のアイデンティティプロバイダーを使用してログインできるようにします。これには、組み込みのプロバイダーである Google や Microsoft、そして Keycloak、Authentik、Authelia などのカスタム OIDC プロバイダーが含まれます。

!!! warning "GitHub を OIDC プロバイダーとして使用することはサポートされなくなりました"
    以前のバージョンから `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` を設定している場合は、それらを削除してください – 現在は無視されており、以前に GitHub を介してサインインしたユーザーは、その方法でログインできなくなります。GitHub は OAuth 2.0 プロバイダーであり、OpenID Connect プロバイダーではなく、Gramps Web がアイデンティティのために依存しているクレームを返さなかったため、完全に信頼できるものではありませんでした。

## 概要

OIDC 認証を使用すると、次のことが可能になります：

- ユーザー認証のために外部のアイデンティティプロバイダーを使用する
- 複数の認証プロバイダーを同時にサポートする
- OIDC グループ/ロールを Gramps Web ユーザーロールにマッピングする
- シングルサインオン (SSO) とシングルサインアウトを実装する
- オプションでローカルのユーザー名/パスワード認証を無効にする

## 設定

OIDC 認証を有効にするには、Gramps Web の設定ファイルまたは環境変数に適切な設定を構成する必要があります。利用可能な OIDC 設定の完全なリストについては、[サーバー設定](configuration.md#settings-for-oidc-authentication) ページを参照してください。

!!! info
    環境変数を使用する場合は、各設定名の前に `GRAMPSWEB_` を付けることを忘れないでください (例: `GRAMPSWEB_OIDC_ENABLED`)。詳細については、[設定ファイルと環境変数](configuration.md#configuration-file-vs-environment-variables) を参照してください。

### 組み込みプロバイダー

Gramps Web は人気のアイデンティティプロバイダーに対して組み込みサポートを提供しています。これらを使用するには、クライアント ID とクライアントシークレットを提供するだけです：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` と `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` と `OIDC_MICROSOFT_CLIENT_SECRET`

複数のプロバイダーを同時に構成できます。システムは、設定値に基づいてどのプロバイダーが利用可能かを自動的に検出します。

!!! tip "Microsoft: シングルテナントのデプロイメント"
    組み込みの Microsoft プロバイダーは、マルチテナントの `/common` エンドポイントを使用し、設計上、任意の Microsoft アカウントからのログインを受け入れます。自分のテナントのユーザーのみを許可したい場合は、[カスタム OIDC プロバイダー](#custom-oidc-providers) を使用して、テナント固有の発行者 URL を指定してください。これにより、発行者の検証が有効のままとなり、そのテナントへのログインが制限されます。

### カスタム OIDC プロバイダー

カスタム OIDC プロバイダー (Keycloak、Authentik、Authelia、またはシングルテナントの Microsoft Entra テナントなど) の場合、次の設定を使用します：

| キー                     | 説明                                                                                   |
|------------------------|--------------------------------------------------------------------------------------|
| `OIDC_ENABLED`         | OIDC 認証を有効にするかどうかのブール値。`True` に設定します。                          |
| `OIDC_ISSUER`         | プロバイダーの発行者 URL。ディスカバリーは `<issuer>/.well-known/openid-configuration` から取得されます。 |
| `OIDC_CLIENT_ID`      | OIDC プロバイダーのクライアント ID                                                  |
| `OIDC_CLIENT_SECRET`  | OIDC プロバイダーのクライアントシークレット                                          |
| `OIDC_NAME`           | カスタム表示名 (オプション、デフォルトは "OIDC")                                     |
| `OIDC_SCOPES`         | OAuth スコープ (オプション、デフォルトは "openid email profile")                     |
| `OIDC_USERNAME_CLAIM` | ユーザー名を生成するために使用されるクレーム (オプション、デフォルトは "preferred_username") |
| `OIDC_PKCE`           | PKCE を使用するかどうか、[PKCE](#pkce) を参照 (オプション、プロバイダーがサポートしている場合は自動的に有効) |

### PKCE

Gramps Web API 3.23 以降、Gramps Web は [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256` メソッド) を認可コードフローに対してサポートしています。Pocket ID などの一部のアイデンティティプロバイダーは、クライアントに PKCE を*必須*とするように設定でき、PKCE を使用しないログインを拒否します。古いバージョンの Gramps Web API は PKCE を使用しないため、そのようなクライアントでのログインは失敗します。

PKCE を使用するかどうかは、ログイン時に次のように決定されます：

- `OIDC_PKCE` が `True` に設定されている場合、PKCE が使用されます。
- `OIDC_PKCE` が `False` に設定されている場合、プロバイダーがサポートしていても PKCE は使用されません。
- `OIDC_PKCE` が設定されていない、または設定されているが空の場合、プロバイダーのディスカバリードキュメント (`/.well-known/openid-configuration`) に `code_challenge_methods_supported` に `S256` がリストされている場合は PKCE が使用され、それ以外の場合は使用されません。

ほとんどのセットアップでは、何も設定する必要はありません。プロバイダーが PKCE を必要とするが、ディスカバリードキュメントに `S256` を広告していない場合は `OIDC_PKCE` を `True` に設定し、プロバイダーが `S256` を広告しているがそれを誤って処理している場合は `False` に設定します。環境変数として、ブール値は小文字でなければなりません (`GRAMPSWEB_OIDC_PKCE=true`)。詳細は [設定](configuration.md) を参照してください。

組み込みプロバイダーの場合、対応するオプションは `OIDC_GOOGLE_PKCE` と `OIDC_MICROSOFT_PKCE` です。

PKCE コード検証子は、プロバイダーへのリダイレクトとコールバックの間にユーザーのセッションに保持されるため、リダイレクト URI に変更は必要ありません。

### マルチツリーセットアップ

マルチツリーサーバーでは、ユーザーがログインするツリーを Gramps Web がアイデンティティプロバイダーにリダイレクトする前に知っている必要があるため、ログインは次のように始まります：

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` はマルチツリーセットアップでは必須です。これを省略したり、存在しないツリーの ID を渡したりすると、ログインは失敗します。シングルツリーサーバーでは `tree` はオプションですが、指定した場合は設定された `TREE` と一致する必要があります。

OIDC アイデンティティは、正確に 1 つの Gramps Web アカウントにバインドされており、そのアカウントは正確に 1 つのツリーに属します – 異なるツリーに対してログインすることは失敗し、アカウントを移動することはありません。プロバイダーの単一のアイデンティティを複数のツリーのアカウントにリンクする方法はありません。複数のツリーにアクセスする必要があるユーザーは、プロバイダーで別々のアイデンティティを持つ必要があります (例: 異なるユーザー名またはアカウント)。

!!! warning
    関連付けられたツリーのないサイト管理者アカウント (詳細は [管理者アカウントの作成](../administration/owner.md) を参照) は OIDC を介してログインできません。OIDC ログインは常にツリーを必要とします。このようなアカウントは、ローカルのユーザー名/パスワードで作成および認証する必要があります。

## 必要なリダイレクト URI

OIDC プロバイダーを構成する際は、次のリダイレクト URI を登録する必要があります：

**ワイルドカードをサポートする OIDC プロバイダーの場合: (例: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

ここで `*` は正規表現のワイルドカードです。プロバイダーの正規表現インタープリターによっては、これも `.*` またはそれに類似したものである可能性があります。
プロバイダーがこれを必要とする場合は、正規表現が有効であることを確認してください (例: Authentik)。

**ワイルドカードをサポートしない OIDC プロバイダーの場合: (例: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

ツリーはリダイレクト URI の一部にはならず、マルチツリーサーバーでも同様です – セッション内で別途移動し、プロバイダーはリダイレクト URI が登録されたものと正確に一致することを要求します。

## ロールマッピング

Gramps Web は、アイデンティティプロバイダーからの OIDC グループまたはロールを Gramps Web ユーザーロールに自動的にマッピングできます。これにより、アイデンティティプロバイダーでユーザーの権限を中央で管理できます。ロールマッピングは、すべてのプロバイダー (組み込みまたはカスタム) で同じ方法で機能します。

### 設定

ロールマッピングを構成するには、次の設定を使用します：

| キー                     | 説明                                                                                   |
|------------------------|--------------------------------------------------------------------------------------|
| `OIDC_ROLE_CLAIM`      | ユーザーのグループ/ロールを含む OIDC トークン内のクレーム名。デフォルトは "groups"。ドットパスがサポートされています (例: `realm_access.roles`)。 |
| `OIDC_GROUP_ADMIN`     | Gramps の "Admin" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                      |
| `OIDC_GROUP_OWNER`     | Gramps の "Owner" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                      |
| `OIDC_GROUP_EDITOR`    | Gramps の "Editor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                     |
| `OIDC_GROUP_CONTRIBUTOR` | Gramps の "Contributor" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                   |
| `OIDC_GROUP_MEMBER`    | Gramps の "Member" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                      |
| `OIDC_GROUP_GUEST`     | Gramps の "Guest" ロールにマッピングされる OIDC プロバイダーのグループ/ロール名                                       |

### ロールマッピングの動作

`OIDC_GROUP_*` 設定が全く構成されていない場合、ロールマッピングはオフになり、ロールは Gramps Web で手動で管理されます。この場合、新しい OIDC アカウントは無効として作成され、既存のオーナーまたは管理者によって承認される必要があります (詳細は [最初のログインとブートストラップ](#first-login-and-bootstrapping) を参照)。

ロールマッピングが構成されると、毎回のログイン時に：

- ロールクレームが存在し、ユーザーがマッピングされたグループに属している場合、対応するロールが付与されます。
- ロールクレームが存在するが、ユーザーがマッピングされたグループに属していない場合、そのロールは無効に設定されます。これはデフォルトのフェイルクローズであり、バグではありません – Gramps Web は認識していないグループのロールを推測することはできません。
- トークンにロールクレームが全く存在しない場合、既存のロールは変更されず、新しいアカウントは依然として無効のままとなります。

!!! warning "Google はグループクレームを送信しません"
    Google のトークンには決して `groups` クレームが含まれないため、ロールマッピングが有効な場合、Google のログインは上記の「クレームが存在しない」に該当します: 既存のユーザーはロールを保持しますが、新しい Google ユーザーは無効として作成され、手動での承認が必要です。他のプロバイダーのためだけにロールマッピングを有効にする前に、これを考慮してください – それ自体が既存の Google ユーザーを無効にするわけではありません。

Microsoft Entra は、アプリロールとグループメンバーシップを ID トークンのみに返し、ユーザー情報エンドポイントからは返しません。Gramps Web は ID トークンのクレームをユーザー情報応答にマージするため、`OIDC_ROLE_CLAIM` は他のプロバイダーと同じように機能します; 両方にクレームが含まれる場合、ユーザー情報の値が優先されます。

## 最初のログインとブートストラップ

OIDC を介して作成された新しいアカウントは、ロールマッピングがロールを割り当てない限り無効から始まります (上記を参照)。まったく新しいインスタンスでは、誰も無効なアカウントを承認できず、`OIDC_DISABLE_LOCAL_AUTH` が有効な場合は、パスワードログインも利用できません。

!!! warning "最初のログイン前にオーナー/管理者グループを構成してください"
    誰かが初めて OIDC を介してログインする前に、`OIDC_GROUP_OWNER` (または `OIDC_GROUP_ADMIN`) を設定し、最初のユーザーがプロバイダーのそのグループに属していることを確認してください。そうしないと、インスタンスは OIDC を介してブートストラップできなくなります。

## アカウントとユーザー名

OIDC を介して作成されたアカウントは、生成されたユーザー名を取得し、アカウント作成時に一度割り当てられ、その後のログインでは変更されません：

- 組み込みプロバイダー: `<provider>_<claim value>`、例: `microsoft_alice@contoso.com`
- カスタムプロバイダー: ベアクレーム値、例: `alice`

衝突が発生した場合は数値のサフィックスが追加されます。OIDC によって作成されたアカウントのユーザー名を後から変更する方法はありません。一方、フルネームとメールアドレスは、毎回のログイン時に更新されます。

OIDC ログインは、たまたま同じメールアドレスを共有する既存のローカルアカウントに自動的に関連付けられることはありません – これは意図的なものであり、メールによるアカウントのリンクはアカウント乗っ取りのベクトルとなります。すでにローカルアカウントを持っているユーザーは、OIDC を介して初めてログインする際に、別の独立したアカウントを取得します。ただし、最初にプロバイダーをアカウントにリンクする場合はこの限りではありません。

Gramps Web API 3.24 以降、ユーザーは OIDC アイデンティティを既存のアカウントにリンクし、[ユーザー設定 > リンクされたサインイン方法](../user-guide/settings.md#linked-sign-in-methods) でそれらをリストおよびリンク解除できます。リンクには最近のログインが必要で、ユーザー自身のトークンで確認されるため、フロントエンドが API とは異なるオリジンにある場合でも機能します。アイデンティティは 1 つのアカウントにのみ属することができ、すでに独自のアカウントを持つアイデンティティをリンクするには、管理者が最初にそのアカウントを削除する必要があります (その編集は残りますが、リビジョン履歴にはその名前は表示されなくなります)。最後にリンクされたアイデンティティは、アカウントの現在のパスワードでのみリンク解除でき、`OIDC_DISABLE_LOCAL_AUTH` が設定されている場合はまったくリンク解除できません。

プロバイダーからのメールアドレスは、プロバイダーがそれらを検証済みとしてマークする場合にのみ保存されます (または `email_verified` クレームを完全に省略する場合); そうでない場合、ログインはメールアドレスを保存せずに進行します。メールアドレスは一意である必要がないため (Gramps Web API 3.22 以降)、他のアカウントがすでに使用している場合でもアドレスは保存されます。

## OIDC ログアウト

Gramps Web は OIDC プロバイダーのシングルサインアウト (SSO ログアウト) をサポートしています。`GET /api/oidc/logout/` はプロバイダーの `end_session_endpoint` を調べ、応答内の `logout_url` として返します; 実際にアイデンティティプロバイダーでセッションを終了するためにブラウザをそこにナビゲートするのは Gramps Web フロントエンドです。プロバイダーに `end_session_endpoint` がない場合、`logout_url` は `null` になります。

!!! warning "ログアウト時にトークンは無効になりません"
    ログアウトはブラウザセッションを終了するだけで、すでに発行された Gramps Web トークンを無効にする方法は現在ありません。トークンは、ユーザーが Gramps Web またはアイデンティティプロバイダーでログアウトしたかどうかに関係なく、有効期限が切れるまで有効のままです (`JWT_ACCESS_TOKEN_EXPIRES`、デフォルトはアクセストークンの場合 15 分)。

## トラブルシューティング

ログインが停止するポイントから始めて、分岐をたどってください。Gramps Web は失敗したコールバックの理由をログに記録します (サーバーログで `OIDC callback error for provider` を探してください)。これは通常、ブラウザに表示されるメッセージよりも具体的です。

**1. ログインボタンが見当たりませんか？**

- `<BASE_URL>/api/oidc/config/` を確認してください。`enabled` が `false` または `providers` が空の場合、OIDC は構成されていません: `OIDC_ENABLED` は `True` に設定され、カスタムプロバイダーには `OIDC_ISSUER` と `OIDC_CLIENT_ID` の両方が必要です。
- 組み込みプロバイダー (Google、Microsoft) は、そのクライアント ID とクライアントシークレットの両方が設定されている場合のみ登録されます。
- サーバーログの起動時に `Could not load discovery document` を探してください。これは、サーバーが `<issuer>/.well-known/openid-configuration` (または `OIDC_OPENID_CONFIG_URL`) に到達できなかったことを意味します。最初の使用時に再試行しますが、Gramps Web コンテナは、ブラウザだけでなく、発行者 URL 自体を解決し、到達できる必要があります。

**2. プロバイダーに送信された直後にブラウザがエラーを受け取りますか？**

エラーは、ログインする前にアイデンティティプロバイダーによって表示されます。

- *「リダイレクト URI の不一致」* (または類似): プロバイダーに登録されたリダイレクト URI は、スキーム、ホスト、ポート、プロバイダー ID を含めて正確に一致する必要があります。詳細は [必要なリダイレクト URI](#required-redirect-uris) を参照してください。これは `BASE_URL` から構築されるため、`BASE_URL` が間違っているとリダイレクト URI も間違ってしまいます。
- *PKCE エラー* (例: `invalid_request`、"code challenge required"、または `code_challenge` パラメータが欠落): プロバイダーが PKCE を必要としているが、Gramps Web がそれを送信しませんでした。次の [PKCE ブランチ](#pkce-branch) に進んでください。

**3. プロバイダーはログインを受け入れますが、Gramps Web がその後エラーを表示しますか？**

- *`mismatching_state`、またはエラーがセッションまたは状態に言及している*: ブラウザがログインが開始されたときに Gramps Web が設定したセッションクッキーを返しませんでした。このクッキーには PKCE コード検証子も含まれています。ブラウザのアドレスが `BASE_URL` と一致していること (同じスキームとホスト)、リバースプロキシがクッキーと元のホストを通過させ、ログインが同じブラウザタブまたはウィンドウで開始され、完了していることを確認してください。
- *`OIDC authentication failed for <provider>` (HTTP 401)*: 根本的な理由を確認するためにサーバーログをチェックしてください。一般的な原因は、クライアントシークレットが間違っている、発行者 URL がトークンの `iss` クレームと一致しない、プロバイダーがコールバックにエラーを返すことです (例: PKCE、下記を参照)。
- *試行回数が多すぎます*: ログインおよびコールバックエンドポイントはレート制限されています (1 分あたり 5 リクエスト)。1 分待ってから再試行してください。

**4. ログインが成功したが、「アカウントがレビュー中」と表示される、または何もできませんか？**

新しいアカウントは、ロールマッピングがロールを割り当てない限り無効として作成されます。詳細は [最初のログインとブートストラップ](#first-login-and-bootstrapping) および [ロールマッピングの動作](#role-mapping-behavior) を参照してください。管理者は、設定 > 管理 > ユーザー管理の下でアカウントを有効にすることもできます。

### PKCE ブランチ

Gramps Web は、ログインが開始されるときに PKCE を使用するかどうかを決定します (詳細は [PKCE](#pkce) を参照)。セットアップに何が起こったかを知るために、これらの質問を順に進んでください：

1. **`OIDC_PKCE` は設定されていますか？** (組み込みプロバイダーの場合、`OIDC_GOOGLE_PKCE` または `OIDC_MICROSOFT_PKCE`。)
    - `True`: PKCE が使用されます。質問 3 にスキップします。
    - `False`: PKCE は意図的にオフであり、プロバイダーのディスカバリードキュメントは無視されます。プロバイダーが PKCE を必要とする場合は、設定を削除するか `True` に設定してください。
    - 設定されていない、または空: 質問 2 に進んでください。
2. **ディスカバリードキュメントに `S256` がリストされていますか？** `<issuer>/.well-known/openid-configuration` を開き、`code_challenge_methods_supported` に `S256` を探します。
    - はい: PKCE が自動的に使用されます。質問 3 に進んでください。
    - いいえ、またはフィールドが欠落している: PKCE は **使用されません**。プロバイダーがそれを必要とする場合は `OIDC_PKCE` を `True` に設定してください。また、サーバーログで `Could not check the provider for PKCE support` を確認してください。これは、ディスカバリードキュメントを取得できなかったことを意味し、したがって PKCE はオフのままとなります。
3. **PKCE は本当に送信されましたか？** ログインを開始し、プロバイダーのログインページのアドレス (またはブラウザのネットワークタブの最初のリダイレクト) を確認します。`code_challenge=` と `code_challenge_method=S256` が含まれている必要があります。
    - 存在するが、ログインがコールバックで失敗する: プロバイダーがコード検証子を拒否しました。リダイレクトとコールバックの間にセッションクッキーが失われた可能性があります (上記のブランチ 3 を参照)、またはプロバイダーが `S256` をサポートしていない場合は、プロバイダーが PKCE を必要としない場合は `OIDC_PKCE` を `False` に設定します。
    - 存在しない: 上記の設定が適用されていません。環境変数が正しいプレフィックスと小文字の値を持っていることを確認してください (例: Docker では `GRAMPSWEB_OIDC_PKCE=true`、`True` はブール値として読み取られません)、サーバーを再起動し、設定を再確認してください。

!!! note
    プロバイダーで PKCE が *オプション* として有効になっている場合、またはまったく有効でない場合、Gramps Web がチャレンジを送信するかどうかに関係なく、ログインは機能します。*必須* として PKCE を構成されたプロバイダー (またはクライアント) のみが、この設定を重要にします。

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
OIDC_ROLE_CLAIM="groups"  # またはプロバイダーによっては "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # ポート 465 用の暗黙的 SSL を使用
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

Pocket ID でリダイレクト URI `<BASE_URL>/api/oidc/callback/custom` を使用して OIDC クライアントを作成します (詳細は [必要なリダイレクト URI](#required-redirect-uris) を参照)。クライアントに「PKCE を必須にする」を有効にした場合、Pocket ID がディスカバリードキュメントで PKCE サポートを広告しているため、追加の Gramps Web 設定は必要ありません。その後、次のように構成します：

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

Keycloak の設定のほとんどはデフォルトのままにできます (*クライアント → クライアントを作成 → クライアント認証 ON*)。
いくつかの例外があります：

1. **OpenID スコープ** – `openid` スコープはすべての Keycloak バージョンでデフォルトで含まれていません。問題を避けるために手動で追加してください: *クライアント → [Gramps クライアント] → クライアントスコープ → スコープを追加 → 名前: `openid` → デフォルトとして設定。*
2. **ロール** – ロールはクライアントレベルまたはレルムごとにグローバルに割り当てることができます。

    * クライアントロールを使用している場合は、`OIDC_ROLE_CLAIM` 設定オプションを次のように設定します: `resource_access.[gramps-client-name].roles`
    * Gramps にロールを表示させるには、*クライアントスコープ* (特定のクライアントの下ではなく、最上位のセクション) に移動し、次のようにします: *ロール → マッパー → クライアントロール → ユーザー情報に追加 → ON.*
