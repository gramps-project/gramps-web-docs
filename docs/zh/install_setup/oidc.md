# OIDC 认证

Gramps Web 支持 OpenID Connect (OIDC) 认证，允许用户使用外部身份提供者登录。这包括内置的 Google 和 Microsoft 提供者，以及像 Keycloak、Authentik 和 Authelia 这样的自定义 OIDC 提供者。

!!! warning "GitHub 作为 OIDC 提供者不再支持"
    如果您在早期版本中设置了 `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET`，请将其删除——它们现在被忽略，之前通过 GitHub 登录的用户将无法再以这种方式登录。GitHub 是一个 OAuth 2.0 提供者，而不是 OpenID Connect 提供者，并且从未返回 Gramps Web 依赖于身份的声明，因此它从未完全可靠。

## 概述

OIDC 认证允许您：

- 使用外部身份提供者进行用户认证
- 同时支持多个认证提供者
- 将 OIDC 组/角色映射到 Gramps Web 用户角色
- 实现单点登录 (SSO) 和单点注销
- 可选地禁用本地用户名/密码认证

## 配置

要启用 OIDC 认证，您需要在 Gramps Web 配置文件或环境变量中配置适当的设置。请参阅 [服务器配置](configuration.md#settings-for-oidc-authentication) 页面以获取可用 OIDC 设置的完整列表。

!!! info
    使用环境变量时，请记得在每个设置名称前加上 `GRAMPSWEB_` 前缀（例如，`GRAMPSWEB_OIDC_ENABLED`）。有关详细信息，请参阅 [配置文件与环境变量](configuration.md#configuration-file-vs-environment-variables)。

### 内置提供者

Gramps Web 内置支持流行的身份提供者。要使用它们，您只需提供客户端 ID 和客户端密钥：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` 和 `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` 和 `OIDC_MICROSOFT_CLIENT_SECRET`

您可以同时配置多个提供者。系统将根据配置值自动检测可用的提供者。

!!! tip "Microsoft: 单租户部署"
    内置的 Microsoft 提供者使用多租户的 `/common` 端点，并按设计接受任何 Microsoft 账户的登录。如果您只想允许来自自己租户的用户，请使用 [自定义 OIDC 提供者](#custom-oidc-providers) 并使用特定于您的租户的发行者 URL，这样可以保持发行者验证活动并限制登录到该租户。

### 自定义 OIDC 提供者

对于自定义 OIDC 提供者（如 Keycloak、Authentik、Authelia 或单租户 Microsoft Entra 租户），使用以下设置：

| 键                     | 描述                                           |
|------------------------|------------------------------------------------|
| `OIDC_ENABLED`         | 布尔值，是否启用 OIDC 认证。设置为 `True`。   |
| `OIDC_ISSUER`         | 您提供者的发行者 URL。发现信息从 `<issuer>/.well-known/openid-configuration` 获取。 |
| `OIDC_CLIENT_ID`      | 您的 OIDC 提供者的客户端 ID                  |
| `OIDC_CLIENT_SECRET`  | 您的 OIDC 提供者的客户端密钥                  |
| `OIDC_NAME`           | 自定义显示名称（可选，默认为 "OIDC"）        |
| `OIDC_SCOPES`         | OAuth 范围（可选，默认为 "openid email profile"） |
| `OIDC_USERNAME_CLAIM` | 用于生成用户名的声明（可选，默认为 "preferred_username"） |

### 多树设置

在多树服务器上，用户登录的树必须在 Gramps Web 重定向到身份提供者之前已知，因此登录以以下方式开始：

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

在多树设置中，`tree` 是必需的；省略它或传递一个不存在的树的 ID 将导致登录失败。在单树服务器上，`tree` 是可选的，但如果提供，它必须与配置的 `TREE` 匹配。

一个 OIDC 身份绑定到一个 Gramps Web 账户，而该账户又属于一个树——针对不同树的登录将失败，而不是移动账户。没有办法将提供者的单一身份链接到多个树中的账户；需要访问多个树的用户需要在提供者处拥有单独的身份（例如，不同的用户名或账户）。

!!! warning
    没有关联树的站点管理员账户（请参见 [创建管理员账户](../administration/owner.md)）无法通过 OIDC 登录，因为 OIDC 登录始终需要一个树。这些账户必须通过本地用户名/密码创建并进行身份验证。

## 必需的重定向 URI

在配置您的 OIDC 提供者时，您必须注册以下重定向 URI：

**对于支持通配符的 OIDC 提供者：（例如，Authentik）**

- `https://your-gramps-backend.com/api/oidc/callback/*`

其中 `*` 是正则表达式通配符。根据您提供者的正则表达式解释器，这也可以是 `.*` 或类似的内容。
确保如果您的提供者需要它，则启用正则表达式（例如，Authentik）。

**对于不支持通配符的 OIDC 提供者：（例如，Authelia）**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

树从不作为重定向 URI 的一部分，即使在多树服务器上——它在会话中单独传递，因为提供者要求重定向 URI 必须与注册的 URI 完全匹配。

## 角色映射

Gramps Web 可以自动将来自您的身份提供者的 OIDC 组或角色映射到 Gramps Web 用户角色。这允许您在身份提供者中集中管理用户权限。角色映射对所有提供者（内置或自定义）都以相同的方式工作。

### 配置

使用以下设置配置角色映射：

| 键                     | 描述                                           |
|------------------------|------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"。支持点路径，例如 `realm_access.roles`。 |
| `OIDC_GROUP_ADMIN`     | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Admin" 角色 |
| `OIDC_GROUP_OWNER`     | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Owner" 角色 |
| `OIDC_GROUP_EDITOR`    | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Editor" 角色 |
| `OIDC_GROUP_CONTRIBUTOR`| 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Contributor" 角色 |
| `OIDC_GROUP_MEMBER`    | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Member" 角色 |
| `OIDC_GROUP_GUEST`     | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Guest" 角色 |

### 角色映射行为

如果没有配置任何 `OIDC_GROUP_*` 设置，则角色映射关闭，角色在 Gramps Web 中手动管理；新 OIDC 账户将被创建为禁用状态，需要现有的所有者或管理员批准（请参见 [首次登录和引导](#first-login-and-bootstrapping)）。

一旦配置了角色映射，在每次登录时：

- 如果角色声明存在且用户属于映射的组，则他们将获得相应的角色。
- 如果角色声明存在但用户不属于任何映射的组，则他们的角色将被设置为禁用。这是一个关闭失败的默认行为，而不是错误——Gramps Web 无法推断出它不识别的组的角色。
- 如果令牌中完全缺少角色声明，则现有角色保持不变；新账户仍然默认为禁用。

!!! warning "Google 不发送 groups 声明"
    Google 的令牌从不包含 `groups` 声明，因此在启用角色映射的情况下，Google 登录将落入上述 "声明缺失" 的情况：现有用户保持其角色，但新的 Google 用户被创建为禁用状态，需要手动批准。在仅为另一个提供者启用角色映射之前，请记住这一点——它本身并不会禁用现有的 Google 用户。

Microsoft Entra 仅在 ID 令牌中返回应用角色和组成员资格，而不是从用户信息端点返回。Gramps Web 将 ID 令牌的声明合并到用户信息响应中，以便 `OIDC_ROLE_CLAIM` 的工作方式与其他提供者相同；当两者都包含声明时，用户信息值优先。

## 首次登录和引导

通过 OIDC 创建的新账户默认处于禁用状态，除非角色映射为其分配了角色（见上文）。在全新的实例中，没有人可以批准禁用账户，如果 `OIDC_DISABLE_LOCAL_AUTH` 也启用，则没有密码登录可以退回。

!!! warning "在首次登录之前配置所有者/管理员组"
    在任何人首次通过 OIDC 登录之前，请设置 `OIDC_GROUP_OWNER`（或 `OIDC_GROUP_ADMIN`），并确保第一个用户在提供者中属于该组。否则，实例根本无法通过 OIDC 引导。

## 账户和用户名

通过 OIDC 创建的账户会获得一个生成的用户名，该用户名在账户创建时分配，并在后续登录时不会更改：

- 内置提供者：`<provider>_<claim value>`，例如 `microsoft_alice@contoso.com`
- 自定义提供者：裸声明值，例如 `alice`

在冲突时会附加数字后缀。之后没有办法重命名 OIDC 创建的账户的用户名；相比之下，完整名称和电子邮件地址在每次登录时都会刷新。

OIDC 登录从不附加到恰好共享其电子邮件地址的现有本地账户——这是故意的，因为通过电子邮件链接账户是一个账户接管向量。已经拥有本地账户的用户在第一次通过 OIDC 登录时会获得一个第二个、独立的账户。

来自提供者的电子邮件地址仅在提供者标记其为已验证（或完全省略 `email_verified` 声明）且该地址未被其他账户使用时存储；否则，登录将继续而不存储电子邮件地址。

## OIDC 注销

Gramps Web 支持 OIDC 提供者的单点注销 (SSO 注销)。`GET /api/oidc/logout/` 查找提供者的 `end_session_endpoint` 并将其作为 `logout_url` 返回；实际上结束身份提供者会话的是 Gramps Web 前端，它会导航浏览器到那里。若提供者没有 `end_session_endpoint`，则 `logout_url` 为 `null`。

!!! warning "注销时令牌不会被撤销"
    注销仅结束浏览器会话；目前没有办法撤销已发出的 Gramps Web 令牌。令牌在过期之前保持有效（`JWT_ACCESS_TOKEN_EXPIRES`，默认 15 分钟用于访问令牌），无论用户是否已在 Gramps Web 或身份提供者处注销。

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

# 可选：从 OIDC 组到 Gramps 角色的角色映射
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

### Authelia

Gramps Web 的社区制作 OIDC 设置指南可在 [官方 Authelia 文档网站](https://www.authelia.com/integration/openid-connect/clients/gramps/) 上找到。

### Keycloak

Keycloak 的大部分配置可以保持默认设置（*客户端 → 创建客户端 → 启用客户端身份验证*）。
有几个例外：

1. **OpenID 范围** – 在所有 Keycloak 版本中，默认情况下不包括 `openid` 范围。为避免问题，请手动添加：*客户端 → [Gramps 客户端] → 客户端范围 → 添加范围 → 名称：`openid` → 设置为默认。*
2. **角色** – 角色可以在客户端级别或每个领域全局分配。

    * 如果您使用客户端角色，请将 `OIDC_ROLE_CLAIM` 配置选项设置为：`resource_access.[gramps-client-name].roles`
    * 要使角色对 Gramps 可见，请导航到 *客户端范围*（顶级部分，而不是特定客户端下），然后：*角色 → 映射器 → 客户端角色 → 添加到用户信息 → 开。*
