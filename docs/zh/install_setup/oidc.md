# OIDC 认证

Gramps Web 支持 OpenID Connect (OIDC) 认证，允许用户使用外部身份提供者登录。这包括 Google、Microsoft 和 GitHub 等流行提供者，以及 Keycloak、Authentik 等自定义 OIDC 提供者。

## 概述

OIDC 认证允许您：

- 使用外部身份提供者进行用户认证
- 同时支持多个认证提供者
- 将 OIDC 组/角色映射到 Gramps Web 用户角色
- 实现单点登录 (SSO) 和单点注销
- 可选择禁用本地用户名/密码认证

## 配置

要启用 OIDC 认证，您需要在 Gramps Web 配置文件或环境变量中配置适当的设置。有关可用 OIDC 设置的完整列表，请参见 [服务器配置](configuration.md#settings-for-oidc-authentication) 页面。

!!! info
    使用环境变量时，请记得在每个设置名称前加上 `GRAMPSWEB_` 前缀（例如，`GRAMPSWEB_OIDC_ENABLED`）。有关详细信息，请参见 [配置文件与环境变量](configuration.md#configuration-file-vs-environment-variables)。

### 内置提供者

Gramps Web 内置支持流行的身份提供者。要使用它们，您只需提供客户端 ID 和客户端密钥：

- **Google**: `OIDC_GOOGLE_CLIENT_ID` 和 `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` 和 `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` 和 `OIDC_GITHUB_CLIENT_SECRET`

您可以同时配置多个提供者。系统将根据配置值自动检测可用的提供者。

### 自定义 OIDC 提供者

对于自定义 OIDC 提供者（如 Keycloak、Authentik 或任何标准 OIDC 兼容提供者），请使用以下设置：

| Key                  | Description                                               |
|----------------------|-----------------------------------------------------------|
| `OIDC_ENABLED`       | 布尔值，是否启用 OIDC 认证。设置为 `True`。              |
| `OIDC_ISSUER`       | 您提供者的发行者 URL                                     |
| `OIDC_CLIENT_ID`    | 您的 OIDC 提供者的客户端 ID                              |
| `OIDC_CLIENT_SECRET` | 您的 OIDC 提供者的客户端密钥                            |
| `OIDC_NAME`         | 自定义显示名称（可选，默认为 "OIDC"）                    |
| `OIDC_SCOPES`       | OAuth 范围（可选，默认为 "openid email profile"）        |

## 必需的重定向 URI

在配置您的 OIDC 提供者时，您必须注册以下重定向 URI：

**对于支持通配符的 OIDC 提供者：（例如，Authentik）**

- `https://your-gramps-backend.com/api/oidc/callback/*`

其中 `*` 是正则表达式通配符。根据您提供者的正则表达式解释器，这也可以是 `.*` 或类似的。
如果您的提供者需要，请确保启用正则表达式（例如，Authentik）。

**对于不支持通配符的 OIDC 提供者：（例如，Authelia）**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

## 角色映射

Gramps Web 可以自动将来自您的身份提供者的 OIDC 组或角色映射到 Gramps Web 用户角色。这使您能够在身份提供者中集中管理用户权限。

### 配置

使用以下设置配置角色映射：

| Key                   | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `OIDC_ROLE_CLAIM`     | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"    |
| `OIDC_GROUP_ADMIN`    | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Admin" 角色 |
| `OIDC_GROUP_OWNER`    | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Owner" 角色 |
| `OIDC_GROUP_EDITOR`   | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Editor" 角色 |
| `OIDC_GROUP_CONTRIBUTOR` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Contributor" 角色 |
| `OIDC_GROUP_MEMBER`   | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Member" 角色 |
| `OIDC_GROUP_GUEST`    | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Guest" 角色 |

### 角色映射行为

- 如果未配置角色映射（未设置 `OIDC_GROUP_*` 变量），则保留现有用户角色
- 根据用户的组成员资格，用户将被分配他们有权获得的最高角色
- 默认情况下，角色映射区分大小写（取决于您的 OIDC 提供者）

## OIDC 注销

Gramps Web 支持 OIDC 提供者的单点注销 (SSO 注销)。当用户在通过 OIDC 认证后从 Gramps Web 注销时，如果提供者支持 `end_session_endpoint`，他们将自动重定向到身份提供者的注销页面。

### 后台注销

Gramps Web 实现了 OpenID Connect 后台注销规范。这允许身份提供者在用户从另一个应用程序或身份提供者本身注销时通知 Gramps Web。

#### 配置

要与您的身份提供者配置后台注销：

1. **在您的身份提供者的客户端配置中注册后台注销端点**：
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **配置您的提供者** 以发送注销通知。具体步骤取决于您的提供者：

   **Keycloak：**

   - 在您的客户端配置中，导航到 "设置"
   - 将 "后台注销 URL" 设置为 `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - 如果您希望基于会话的注销，请启用 "后台注销会话必需"

   **Authentik：**

   - 在您的提供者配置中，添加后台注销 URL
   - 确保提供者配置为发送注销令牌

!!! warning "令牌过期"
    由于 JWT 令牌的无状态特性，后台注销目前记录注销事件，但无法立即撤销已发出的 JWT 令牌。令牌将保持有效，直到过期（默认：访问令牌 15 分钟）。

    为了增强安全性，请考虑：

    - 减少 JWT 令牌过期时间 (`JWT_ACCESS_TOKEN_EXPIRES`)
    - 教育用户在从身份提供者注销时手动从 Gramps Web 注销

!!! tip "工作原理"
    当用户从您的身份提供者或其他应用程序注销时：

    1. 提供者向 Gramps Web 的后台注销端点发送 `logout_token` JWT
    2. Gramps Web 验证令牌并记录注销事件
    3. 注销令牌的 JTI 被添加到黑名单，以防止重放攻击
    4. 一旦令牌过期，任何带有用户 JWT 的新 API 请求将被拒绝

## 示例配置

### 自定义 OIDC 提供者 (Keycloak)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"

# 自定义 OIDC 配置
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # 可选：自动重定向到 SSO 登录
OIDC_DISABLE_LOCAL_AUTH=True  # 可选：禁用用户名/密码登录

# 可选：从 OIDC 组到 Gramps 角色的映射
OIDC_ROLE_CLAIM="groups"  # 或 "roles"，具体取决于您的提供者
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # 您的 SMTP 密码
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### 内置提供者 (Google)

```python
TREE="My Family Tree"
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
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"

# 自定义提供者
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

Gramps Web 的社区 OIDC 设置指南可在 [官方 Authelia 文档网站](https://www.authelia.com/integration/openid-connect/clients/gramps/) 上找到。

### Keycloak

Keycloak 的大部分配置可以保持默认设置（*客户端 → 创建客户端 → 客户端认证开启*）。
有几个例外：

1. **OpenID 范围** – 在所有 Keycloak 版本中，`openid` 范围并不默认包含。为避免问题，请手动添加：*客户端 → [Gramps 客户端] → 客户端范围 → 添加范围 → 名称: `openid` → 设置为默认。*
2. **角色** – 角色可以在客户端级别或每个领域全局分配。

    * 如果您使用客户端角色，请将 `OIDC_ROLE_CLAIM` 配置选项设置为：`resource_access.[gramps-client-name].roles`
    * 要使角色对 Gramps 可见，请导航到 *客户端范围*（顶级部分，而不是特定客户端下），然后：*角色 → 映射器 → 客户端角色 → 添加到用户信息 → 开启。*
