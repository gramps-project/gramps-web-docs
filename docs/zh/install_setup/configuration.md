# 服务器配置

使用默认的 Docker 镜像，所有必要的配置都可以通过浏览器进行。但是，根据部署情况，可能需要自定义服务器配置。

本页面列出了所有更改配置的方法和所有现有的配置选项。


## 配置文件与环境变量

对于设置，您可以使用配置文件或环境变量。

当您使用 [基于 Docker Compose 的设置](deployment.md) 时，可以通过在 `grampsweb:` 块的 `volumes:` 键下添加以下列表项来包含配置文件：

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
其中 `/path/to/config.cfg` 是您服务器文件系统中配置文件的路径（右侧指的是容器中的路径，必须保持不变）。

使用环境变量时，

- 每个设置名称前缀加上 `GRAMPSWEB_` 以获取环境变量的名称
- 使用双下划线表示嵌套字典设置，例如 `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` 将设置 `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` 配置选项的值

请注意，通过环境设置的配置选项优先于配置文件中的选项。如果两者都存在，环境变量“胜出”。

## 现有配置设置
以下配置选项是存在的。

### 必需设置

键 | 描述
----|-------------
`TREE` | 要使用的家谱数据库的名称。使用 `gramps -l` 显示可用的树。如果不存在此名称的树，将创建一个新的空树。
`SECRET_KEY` | Flask 的密钥。该密钥不得公开共享。更改它将使所有访问令牌失效。
`USER_DB_URI` | 用户数据库的数据库 URL。允许任何与 SQLAlchemy 兼容的 URL。

!!! info
    您可以通过以下命令生成一个安全的密钥

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### 可选设置

键 | 描述
----|-------------
`MEDIA_BASE_DIR` | 用作媒体文件的基础目录的路径，覆盖 Gramps 中设置的媒体基础目录。当使用 [S3](s3.md) 时，必须具有 `s3://<bucket_name>` 的形式
`SEARCH_INDEX_DB_URI` | 搜索索引的数据库 URL。仅允许 `sqlite` 或 `postgresql` 作为后端。默认为 `sqlite:///indexdir/search_index.db`，在运行脚本的路径下创建一个 SQLite 文件在 `indexdir` 文件夹中
`STATIC_PATH` | 提供静态文件的路径（例如，静态网页前端）
`BASE_URL` | API 可访问的基础 URL（例如，`https://mygramps.mydomain.com/`）。这在构建正确的密码重置链接时是必要的
`CORS_ORIGINS` | 允许 CORS 请求的来源。默认情况下，所有请求都被拒绝。使用 `"*"` 允许来自任何域的请求。
`EMAIL_HOST` | SMTP 服务器主机（例如，用于发送密码重置电子邮件）
`EMAIL_PORT` | SMTP 服务器端口。默认为 465
`EMAIL_HOST_USER` | SMTP 服务器用户名
`EMAIL_HOST_PASSWORD` | SMTP 服务器密码
`EMAIL_USE_TLS` | **已弃用**（请改用 `EMAIL_USE_SSL` 或 `EMAIL_USE_STARTTLS`）。布尔值，是否使用 TLS 发送电子邮件。默认为 `True`。使用 STARTTLS 时，将其设置为 `False` 并使用不同于 25 的端口。
`EMAIL_USE_SSL` | 布尔值，是否对 SMTP 使用隐式 SSL/TLS（v3.6.0+）。如果未显式设置 `EMAIL_USE_TLS`，则默认为 `True`。通常与端口 465 一起使用。
`EMAIL_USE_STARTTLS` | 布尔值，是否对 SMTP 使用显式 STARTTLS（v3.6.0+）。默认为 `False`。通常与端口 587 或 25 一起使用。
`DEFAULT_FROM_EMAIL` | 自动电子邮件的“发件人”地址
`THUMBNAIL_CACHE_CONFIG` | 用于缩略图缓存的设置字典。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`REQUEST_CACHE_CONFIG` | 用于请求缓存的设置字典。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`PERSISTENT_CACHE_CONFIG` | 用于持久缓存的设置字典，例如用于遥测。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`CELERY_CONFIG` | Celery 后台任务队列的设置。有关可能的设置，请参见 [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)。
`REPORT_DIR` | 运行 Gramps 报告的输出将存储的临时目录
`EXPORT_DIR` | 导出 Gramps 数据库的输出将存储的临时目录
`REGISTRATION_DISABLED` | 如果为 `True`，则不允许新用户注册（默认 `False`）
`DISABLE_TELEMETRY` | 如果为 `True`，则禁用统计遥测（默认 `False`）。有关详细信息，请参见 [telemetry](telemetry.md)。

!!! info
    使用环境变量进行配置时，布尔选项如 `EMAIL_USE_TLS` 必须是字符串 `true` 或 `false`（区分大小写！）。

### 仅适用于 PostgreSQL 后端数据库的设置

如果您已配置 Gramps 数据库以与 [PostgreSQL 附加组件](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) 一起使用，则需要此设置。

键 | 描述
----|-------------
`POSTGRES_USER` | 数据库连接的用户名
`POSTGRES_PASSWORD` | 数据库用户的密码


### 适用于托管多个树的设置

以下设置在 [托管多个树](multi-tree.md) 时相关。

键 | 描述
----|-------------
`MEDIA_PREFIX_TREE` | 布尔值，是否为每棵树的媒体文件使用单独的子文件夹。默认为 `False`，但在多树设置中强烈建议使用 `True`
`NEW_DB_BACKEND` | 用于新创建家谱的数据库后端。必须是 `sqlite`、`postgresql` 或 `sharedpostgresql` 之一。默认为 `sqlite`。
`POSTGRES_HOST` | 使用 SharedPostgreSQL 后端在多树设置中创建新树时使用的 PostgreSQL 服务器的主机名
`POSTGRES_PORT` | 使用 SharedPostgreSQL 后端在多树设置中创建新树时使用的 PostgreSQL 服务器的端口


### OIDC 身份验证的设置

如果您想使用外部提供者的 OpenID Connect (OIDC) 身份验证，则需要这些设置。有关详细的设置说明和示例，请参见 [OIDC 身份验证](oidc.md)。

键 | 描述
----|-------------
`OIDC_ENABLED` | 布尔值，是否启用 OIDC 身份验证。默认为 `False`。
`OIDC_ISSUER` | OIDC 提供者的发行者 URL（用于自定义 OIDC 提供者）
`OIDC_CLIENT_ID` | OAuth 客户端 ID（用于自定义 OIDC 提供者）
`OIDC_CLIENT_SECRET` | OAuth 客户端密钥（用于自定义 OIDC 提供者）
`OIDC_NAME` | 提供者的自定义显示名称。默认为 "OIDC"
`OIDC_SCOPES` | OAuth 范围。默认为 "openid email profile"
`OIDC_USERNAME_CLAIM` | 用于用户名的声明。默认为 "preferred_username"
`OIDC_OPENID_CONFIG_URL` | 可选：OpenID Connect 配置端点的 URL（如果不使用标准的 `/.well-known/openid-configuration`）
`OIDC_DISABLE_LOCAL_AUTH` | 布尔值，是否禁用本地用户名/密码身份验证。默认为 `False`
`OIDC_AUTO_REDIRECT` | 布尔值，是否在仅配置一个提供者时自动重定向到 OIDC。默认为 `False`

#### 内置 OIDC 提供者

对于内置提供者（Google、Microsoft、GitHub），使用以下设置：

键 | 描述
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth 的客户端 ID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth 的客户端密钥
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth 的客户端 ID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth 的客户端密钥
`OIDC_GITHUB_CLIENT_ID` | GitHub OAuth 的客户端 ID
`OIDC_GITHUB_CLIENT_SECRET` | GitHub OAuth 的客户端密钥

#### OIDC 角色映射

这些设置允许您将来自身份提供者的 OIDC 组/角色映射到 Gramps Web 用户角色：

键 | 描述
----|-------------
`OIDC_ROLE_CLAIM` | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"
`OIDC_GROUP_ADMIN` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Admin" 角色
`OIDC_GROUP_OWNER` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Owner" 角色
`OIDC_GROUP_EDITOR` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Editor" 角色
`OIDC_GROUP_CONTRIBUTOR` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Contributor" 角色
`OIDC_GROUP_MEMBER` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Member" 角色
`OIDC_GROUP_GUEST` | 来自您的 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Guest" 角色

### 仅适用于 AI 功能的设置

如果您想使用 AI 驱动的功能，如聊天或语义搜索，则需要这些设置。

键 | 描述
----|-------------
`LLM_BASE_URL` | OpenAI 兼容聊天 API 的基础 URL。默认为 `None`，使用 OpenAI API。
`LLM_MODEL` | 用于 OpenAI 兼容聊天 API 的模型。如果未设置（默认），则禁用聊天。从 v3.6.0 开始，AI 助手使用具有工具调用能力的 Pydantic AI。
`VECTOR_EMBEDDING_MODEL` | 用于语义搜索向量嵌入的 [Sentence Transformers](https://sbert.net/) 模型。如果未设置（默认），则禁用语义搜索和聊天。
`LLM_MAX_CONTEXT_LENGTH` | 提供给 LLM 的家谱上下文的字符限制。默认为 50000。
`LLM_SYSTEM_PROMPT` | LLM 聊天助手的自定义系统提示（v3.6.0+）。如果未设置，则使用默认的家谱优化提示。


## 示例配置文件

一个用于生产的最小配置文件可能如下所示：
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 对于端口 465 使用隐式 SSL
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # 您的 SMTP 密码
DEFAULT_FROM_EMAIL="gramps@example.com"
