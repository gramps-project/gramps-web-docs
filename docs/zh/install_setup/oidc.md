# OIDC 认证

Gramps Web 支持 OpenID Connect (OIDC) 认证，允许用户使用外部身份提供者登录。这包括内置的 Google 和 Microsoft 提供者，以及像 Keycloak、Authentik 和 Authelia 这样的自定义 OIDC 提供者。

!!! warning "GitHub 作为 OIDC 提供者不再受支持"
    如果您在早期版本中设置了 `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET`，请将其删除——它们现在被忽略，之前通过 GitHub 登录的用户无法再以这种方式登录。GitHub 是一个 OAuth 2.0 提供者，而不是 OpenID Connect 提供者，并且从未返回 Gramps Web 依赖于身份的声明，因此从未完全可靠。

## 概述

OIDC 认证允许您：

- 使用外部身份提供者进行用户认证
- 同时支持多个认证提供者
- 将 OIDC 组/角色映射到 Gramps Web 用户角色
- 实现单点登录 (SSO) 和单点注销
- 可选地禁用本地用户名/密码认证

## 配置

要启用 OIDC 认证，您需要在 Gramps Web 配置文件或环境变量中配置适当的设置。有关可用 OIDC 设置的完整列表，请参见 [服务器配置](configuration.md#settings-for-oidc-authentication) 页面。

!!! info
    使用环境变量时，请记得在每个设置名称前加上 `GRAMPSWEB_` 前缀（例如，`GRAMPSWEB_OIDC_ENABLED`）。有关详细信息，请参见 [配置文件与环境变量](configuration.md#configuration-file-vs-environment-variables)。

### 内置提供者

Gramps Web 内置支持流行的身份提供者。要使用它们，您只需提供客户端 ID 和客户端密钥：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` 和 `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` 和 `OIDC_MICROSOFT_CLIENT_SECRET`

您可以同时配置多个提供者。系统将根据配置值自动检测可用的提供者。

!!! tip "Microsoft: 单租户部署"
    内置的 Microsoft 提供者使用多租户的 `/common` 端点，并按设计接受来自任何 Microsoft 帐户的登录。如果您只想允许来自自己租户的用户，请使用 [自定义 OIDC 提供者](#custom-oidc-providers) 及您特定租户的发行者 URL，这样可以保持发行者验证处于活动状态，并将登录限制在该租户内。

### 自定义 OIDC 提供者

对于自定义 OIDC 提供者（如 Keycloak、Authentik、Authelia 或单租户 Microsoft Entra 租户），使用以下设置：

| 键                  | 描述                                                  |
|---------------------|-------------------------------------------------------|
| `OIDC_ENABLED`      | 布尔值，是否启用 OIDC 认证。设置为 `True`。          |
| `OIDC_ISSUER`      | 您提供者的发行者 URL。发现信息从 `<issuer>/.well-known/openid-configuration` 获取。 |
| `OIDC_CLIENT_ID`    | 您的 OIDC 提供者的客户端 ID                          |
| `OIDC_CLIENT_SECRET` | 您的 OIDC 提供者的客户端密钥                        |
| `OIDC_NAME`         | 自定义显示名称（可选，默认为 "OIDC"）                |
| `OIDC_SCOPES`       | OAuth 范围（可选，默认为 "openid email profile"）   |
| `OIDC_USERNAME_CLAIM` | 用于生成用户名的声明（可选，默认为 "preferred_username"） |
| `OIDC_PKCE`         | 是否使用 PKCE，见 [PKCE](#pkce)（可选，如果提供者支持则自动启用） |

### PKCE

自 Gramps Web API 3.23 起，Gramps Web 支持 [PKCE](https://datatracker.ietf.org/doc/html/rfc7636)（用于授权码流的证明密钥，`S256` 方法）。一些身份提供者，例如 Pocket ID，可以配置为 *要求* PKCE，并拒绝不使用它的登录。旧版本的 Gramps Web API 从不使用 PKCE，因此使用此类客户端的登录会失败。

是否使用 PKCE 在登录时决定如下：

- 如果 `OIDC_PKCE` 设置为 `True`，则使用 PKCE。
- 如果 `OIDC_PKCE` 设置为 `False`，则不使用 PKCE，即使提供者支持它。
- 如果 `OIDC_PKCE` 未设置，或设置但为空，则如果提供者的发现文档 (`/.well-known/openid-configuration`) 在 `code_challenge_methods_supported` 中列出了 `S256`，则使用 PKCE，否则不使用。

对于大多数设置，您不需要设置任何内容。如果您的提供者要求 PKCE 但未在其发现文档中宣传 `S256`，请将 `OIDC_PKCE` 设置为 `True`；如果您的提供者宣传 `S256` 但处理不当，则设置为 `False`。作为环境变量，布尔值必须为小写（`GRAMPSWEB_OIDC_PKCE=true`），请参见 [配置](configuration.md)。

对于内置提供者，相应的选项是 `OIDC_GOOGLE_PKCE` 和 `OIDC_MICROSOFT_PKCE`。

PKCE 代码验证器在用户的会话中保持在重定向到提供者和回调之间，因此这不需要更改重定向 URI。

### 多树设置

在多树服务器上，使用已链接到 Gramps Web 帐户的身份登录的用户将登录到该帐户的树，因此普通登录页面对他们有效。

要使用 OIDC 身份创建一个 *新* 帐户，Gramps Web 需要知道它应该属于哪个树。因此，新用户必须从树的注册链接 (`/register/<tree_id>`，请参见 [注册链接](../administration/users.md#registration-link-multi-tree-setup-only)) 或树的登录页面 (`/login/<tree_id>`) 开始。两者都提供配置的提供者。通过普通登录页面使用未知身份登录会被拒绝，并显示指向注册链接的消息。这需要 Gramps Web API 3.25.3 和 Gramps Web 26.11.2 或更高版本。

在后台，登录以以下方式开始：

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

其中 `tree` 是可选的，除非创建新帐户。传递不存在的树的 ID 会导致登录失败。在单树服务器上，`tree` 是可选的，但如果给出，它必须与配置的 `TREE` 匹配。

一个 OIDC 身份绑定到一个 Gramps Web 帐户，而该帐户又属于一个树——针对不同树的登录会失败，而不是移动帐户。没有办法将提供者中的单一身份链接到多个树中的帐户；需要访问多个树的用户需要在提供者中拥有单独的身份（例如不同的用户名或帐户）。

!!! warning
    没有关联树的站点管理员帐户（请参见 [创建管理员帐户](../administration/owner.md)）无法通过 OIDC 创建，因为通过 OIDC 登录创建的帐户始终属于一个树。请使用本地用户名和密码创建此类帐户。

### 原生应用

原生应用，例如 Gramps Web 的移动应用，可以让用户在系统浏览器中登录，并在应用的 `https` 链接中接收结果。自 Gramps Web API 3.26 起，如果链接在 `OIDC_ALLOWED_REDIRECT_URIS` 中列出，则此功能有效，例如：

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

应用的文档会告诉您要添加哪个链接。注册在身份提供者的重定向 URI 保持不变。

## 必需的重定向 URI

在配置您的 OIDC 提供者时，您必须注册以下重定向 URI：

**对于支持通配符的 OIDC 提供者：（例如，Authentik）**

- `https://your-gramps-backend.com/api/oidc/callback/*`

其中 `*` 是正则表达式通配符。根据您提供者的正则表达式解释器，这也可以是 `.*` 或类似的。
确保如果您的提供者要求启用正则表达式。

**对于不支持通配符的 OIDC 提供者：（例如，Authelia）**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

树从不作为重定向 URI 的一部分，即使在多树服务器上——它在会话中单独传递，因为提供者要求重定向 URI 必须与注册的 URI 完全匹配。

## 角色映射

Gramps Web 可以自动将 OIDC 组或角色从您的身份提供者映射到 Gramps Web 用户角色。这允许您在身份提供者中集中管理用户权限。角色映射对所有提供者（内置或自定义）都以相同的方式工作。

### 配置

使用以下设置配置角色映射：

| 键                  | 描述                                                  |
|---------------------|-------------------------------------------------------|
| `OIDC_ROLE_CLAIM`   | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"。支持点路径，例如 `realm_access.roles`。 |
| `OIDC_GROUP_ADMIN`  | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Admin" 角色 |
| `OIDC_GROUP_OWNER`  | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Owner" 角色 |
| `OIDC_GROUP_EDITOR` | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Editor" 角色 |
| `OIDC_GROUP_CONTRIBUTOR` | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Contributor" 角色 |
| `OIDC_GROUP_MEMBER` | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Member" 角色 |
| `OIDC_GROUP_GUEST`  | 来自您 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Guest" 角色 |

### 角色映射行为

如果没有配置任何 `OIDC_GROUP_*` 设置，则角色映射关闭，角色在 Gramps Web 中手动管理；新 OIDC 帐户将被创建为禁用状态，并需要现有所有者或管理员的批准（请参见 [首次登录和引导](#first-login-and-bootstrapping)）。

一旦配置了角色映射，每次登录时：

- 如果角色声明存在且用户属于映射的组，则他们将获得相应的角色。
- 如果角色声明存在但用户不属于任何映射的组，则其角色设置为禁用。这是一个故障关闭的默认值，而不是错误——Gramps Web 无法推断出它不识别的组的角色。
- 如果令牌中完全缺少角色声明，则现有角色保持不变；新帐户仍默认为禁用。

!!! warning "Google 不发送 groups 声明"
    Google 的令牌从不包括 `groups` 声明，因此在启用角色映射时，Google 登录将落入上述 "声明缺失"：现有用户保留其角色，但新 Google 用户被创建为禁用状态，并需要手动批准。在仅为其他提供者启用角色映射之前，请记住这一点——它本身并不会禁用现有的 Google 用户。

Microsoft Entra 仅在 ID 令牌中返回应用角色和组成员身份，而不是从用户信息端点返回。Gramps Web 将 ID 令牌的声明合并到用户信息响应中，以便 `OIDC_ROLE_CLAIM` 的工作方式与其他提供者相同；当两者都包含声明时，用户信息值优先。

## 首次登录和引导

通过 OIDC 创建的新帐户默认处于禁用状态，除非角色映射为其分配了角色（见上文）。在全新的实例中，没有人可以批准禁用帐户，如果 `OIDC_DISABLE_LOCAL_AUTH` 也启用，则没有密码登录可以回退。

!!! warning "在首次登录之前配置所有者/管理员组"
    在任何人首次通过 OIDC 登录之前，请设置 `OIDC_GROUP_OWNER`（或 `OIDC_GROUP_ADMIN`），并确保第一个用户在提供者中属于该组。否则，实例根本无法通过 OIDC 引导。

## 帐户和用户名

通过 OIDC 创建的帐户会获得一个生成的用户名，该用户名在帐户创建时分配，并在后续登录时不会更改：

- 内置提供者：`<provider>_<claim value>`，例如 `microsoft_alice@contoso.com`
- 自定义提供者：裸声明值，例如 `alice`

在冲突时会附加数字后缀。之后没有办法重命名 OIDC 创建的帐户的用户名；相比之下，完整名称和电子邮件地址在每次登录时都会刷新。

OIDC 登录从不附加到恰好共享其电子邮件地址的现有本地帐户——这是故意的，因为通过电子邮件链接帐户是一个帐户接管向量。已经拥有本地帐户的用户在第一次通过 OIDC 登录时会获得第二个独立帐户，除非他们首先将提供者链接到他们的帐户。

自 Gramps Web API 3.24 起，用户可以将 OIDC 身份链接到其现有帐户，并在 [用户设置 > 链接的登录方法](../user-guide/settings.md#linked-sign-in-methods) 下列出和取消链接。链接需要最近的登录，并通过用户自己的令牌确认，因此即使前端位于与 API 不同的来源上也能正常工作。一个身份只能属于一个帐户；要链接一个已经拥有自己帐户的身份，管理员首先需要删除该帐户（其编辑仍然保留，但修订历史不再显示其名称）。最后链接的身份只能使用帐户当前的密码取消链接，如果设置了 `OIDC_DISABLE_LOCAL_AUTH` 则根本无法取消链接。

只有在提供者将其标记为已验证（或完全省略 `email_verified` 声明）时，电子邮件地址才会被存储；否则，登录将继续而不存储电子邮件地址。由于电子邮件地址不必唯一（自 Gramps Web API 3.22 起），即使另一个帐户已经使用它，地址也会被存储。

## OIDC 注销

Gramps Web 支持 OIDC 提供者的单点注销 (SSO 注销)。`GET /api/oidc/logout/` 查找提供者的 `end_session_endpoint` 并将其作为 `logout_url` 返回；实际结束身份提供者会话的是 Gramps Web 前端导航浏览器到该 URL。 当提供者没有 `end_session_endpoint` 时，`logout_url` 为 `null`。

!!! warning "注销时令牌不会被撤销"
    注销仅结束浏览器会话；目前没有办法撤销已经发出的 Gramps Web 令牌。令牌在过期之前保持有效（`JWT_ACCESS_TOKEN_EXPIRES`，默认访问令牌为 15 分钟），无论用户是否已经在 Gramps Web 或身份提供者处注销。

## 故障排除

从登录停止的地方开始，并沿着分支进行。Gramps Web 记录了失败回调的原因（在服务器日志中查找 `OIDC callback error for provider`），这通常比浏览器中显示的消息更具体。

**1. 登录按钮缺失？**

- 检查 `<BASE_URL>/api/oidc/config/`。如果 `enabled` 为 `false` 或 `providers` 为空，则 OIDC 未配置：`OIDC_ENABLED` 必须为 `True`，并且自定义提供者需要同时设置 `OIDC_ISSUER` 和 `OIDC_CLIENT_ID`。
- 只有在设置了客户端 ID 和客户端密钥的情况下，内置提供者（Google、Microsoft）才会被注册。
- 在服务器日志的启动时查找 `Could not load discovery document`。这意味着服务器无法访问 `<issuer>/.well-known/openid-configuration`（或 `OIDC_OPENID_CONFIG_URL`）。它在首次使用时重试，但 Gramps Web 容器必须能够解析并访问发行者 URL，而不仅仅是您的浏览器。

**2. 浏览器在被发送到提供者后立即出现错误？**

错误由身份提供者显示，在您登录之前。

- *"重定向 URI 不匹配"*（或类似）：在提供者处注册的重定向 URI 必须完全匹配，包括方案、主机、端口和提供者 ID。请参见 [必需的重定向 URI](#required-redirect-uris)。请注意，它是从 `BASE_URL` 构建的，因此错误的 `BASE_URL` 会导致错误的重定向 URI。
- *PKCE 错误*（例如 `invalid_request`、"需要代码挑战" 或缺少 `code_challenge` 参数）：提供者要求 PKCE，但 Gramps Web 未发送。请转到下面的 [PKCE 分支](#pkce-branch)。

**3. 提供者接受登录，但 Gramps Web 随后显示错误？**

- *`mismatching_state`，或错误提到会话或状态*：浏览器未发送 Gramps Web 在登录开始时设置的会话 cookie。此 cookie 还携带 PKCE 代码验证器。确保浏览器中的地址与 `BASE_URL` 匹配（相同的方案和主机），反向代理能够传递 cookie 和原始主机，并且登录在同一浏览器标签或窗口中启动和完成。
- *`OIDC authentication failed for <provider>`（HTTP 401）*：检查服务器日志以获取潜在原因。常见原因包括错误的客户端密钥、与令牌的 `iss` 声明不匹配的发行者 URL，以及提供者在回调时返回错误（例如 PKCE，见下文）。
- *尝试次数过多*：登录和回调端点受到速率限制（每分钟 5 次请求）。等待一分钟后重试。

**4. 登录成功但您看到 "帐户正在审核" 或无法执行任何操作？**

新帐户在没有角色映射分配角色的情况下创建为禁用状态。请参见 [首次登录和引导](#first-login-and-bootstrapping) 和 [角色映射行为](#role-mapping-behavior)。管理员还可以在设置 > 管理 > 管理用户下激活帐户。

### PKCE 分支

Gramps Web 在登录开始时决定是否使用 PKCE（见 [PKCE](#pkce)）。要找出您的设置发生了什么，请按顺序逐一回答以下问题：

1. **`OIDC_PKCE` 是否设置？**（对于内置提供者，`OIDC_GOOGLE_PKCE` 或 `OIDC_MICROSOFT_PKCE`。）
    - `True`：使用 PKCE。跳到问题 3。
    - `False`：故意关闭 PKCE，提供者的发现文档被忽略。如果您的提供者要求 PKCE，请删除该设置或将其设置为 `True`。
    - 未设置或为空：继续回答问题 2。
2. **发现文档是否列出了 `S256`？** 打开 `<issuer>/.well-known/openid-configuration` 并查找 `code_challenge_methods_supported` 中的 `S256`。
    - 是：自动使用 PKCE。继续回答问题 3。
    - 否，或该字段缺失：**不**使用 PKCE。如果您的提供者要求它，请将 `OIDC_PKCE` 设置为 `True`。还要检查服务器日志中的 `Could not check the provider for PKCE support`，这意味着无法获取发现文档，因此 PKCE 被关闭。
3. **PKCE 是否真的被发送？** 开始登录并查看提供者登录页面的地址（或浏览器网络选项卡中的第一次重定向）。它应该包含 `code_challenge=` 和 `code_challenge_method=S256`。
    - 存在，但登录在回调时仍然失败：提供者拒绝了代码验证器。重定向和回调之间可能丢失了会话 cookie（见上面的分支 3），或者提供者不支持 `S256`，在这种情况下，如果提供者不要求 PKCE，请将 `OIDC_PKCE` 设置为 `False`。
    - 缺失：上述设置未应用。检查环境变量是否具有正确的前缀和小写值（例如，在 Docker 中为 `GRAMPSWEB_OIDC_PKCE=true`；`True` 不会被读取为布尔值），重启服务器，并再次查看配置。

!!! note
    在提供者将 PKCE 启用为 *可选*，或根本未启用的情况下，无论 Gramps Web 是否发送挑战，登录都能正常工作。只有配置为 *要求* PKCE 的提供者（或客户端）才会使此设置变得重要。

## 示例配置

### 自定义 OIDC 提供者（Keycloak）

```python
TREE="我的家谱"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"

# 自定义 OIDC 配置
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="家庭 SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # 可选：自动重定向到 SSO 登录
OIDC_DISABLE_LOCAL_AUTH=True  # 可选：禁用用户名/密码登录

# 可选：将 OIDC 组映射到 Gramps 角色
OIDC_ROLE_CLAIM="groups"  # 或 "roles"，具体取决于您的提供者
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 对于 465 端口使用隐式 SSL
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # 您的 SMTP 密码
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### 内置提供者（Google）

```python
TREE="我的家谱"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### 多个提供者

您可以同时启用多个 OIDC 提供者：

```python
TREE="我的家谱"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"

# 自定义提供者
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="公司 SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

在 Pocket ID 中创建一个 OIDC 客户端，重定向 URI 为 `<BASE_URL>/api/oidc/callback/custom`（请参见 [必需的重定向 URI](#required-redirect-uris)）。如果您为客户端启用 "要求 PKCE"，则无需额外的 Gramps Web 配置，因为 Pocket ID 在其发现文档中宣传 PKCE 支持。然后配置：

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Gramps Web 的社区制作 OIDC 设置指南可在 [官方 Authelia 文档网站](https://www.authelia.com/integration/openid-connect/clients/gramps/) 上找到。

### Keycloak

Keycloak 的大部分配置可以保持默认值（*客户端 → 创建客户端 → 启用客户端认证*）。
有几个例外：

1. **OpenID 范围** – 在所有 Keycloak 版本中，`openid` 范围默认不包含。为避免问题，请手动添加：*客户端 → [Gramps 客户端] → 客户端范围 → 添加范围 → 名称：`openid` → 设置为默认。*
2. **角色** – 角色可以在客户端级别或全局按领域分配。

    * 如果您使用客户端角色，请将 `OIDC_ROLE_CLAIM` 配置选项设置为：`resource_access.[gramps-client-name].roles`
    * 要使角色对 Gramps 可见，请导航到 *客户端范围*（顶级部分，而不是特定客户端下），然后：*角色 → 映射器 → 客户端角色 → 添加到用户信息 → 开。*
