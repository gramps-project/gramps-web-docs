# 服务器配置

使用默认 Docker 镜像时，所有必要的配置都可以通过浏览器完成。但是，根据部署方式的不同，可能需要自定义服务器配置。

本页面列出了更改配置的所有方法以及所有现有配置选项。


## 配置文件与环境变量

对于这些设置，您可以使用配置文件或环境变量。

使用基于 [Docker Compose 的设置](deployment.md) 时，您可以通过在 `grampsweb:` 块的 `volumes:` 键下添加以下列表项来包含配置文件：

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
其中，`/path/to/config.cfg` 是服务器文件系统中配置文件的路径（右侧指向容器中的路径，不得更改）。

使用环境变量时：

- 为每个设置名称添加 `GRAMPSWEB_` 前缀，以获得环境变量的名称
- 对于嵌套字典设置，请使用两个下划线，例如 `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` 将设置 `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` 配置选项的值

请注意，通过环境设置的配置选项优先于配置文件中的配置选项。如果两者同时存在，则以环境变量为准。

!!! warning "未加前缀的环境变量已弃用"
    出于历史原因，少数设置——`TREE`、`SECRET_KEY`、`USER_DB_URI`、`POSTGRES_USER`、`POSTGRES_PASSWORD`、`MEDIA_BASE_DIR`、`SEARCH_INDEX_DIR`、`EMAIL_HOST`、`EMAIL_PORT`、`EMAIL_HOST_USER`、`EMAIL_HOST_PASSWORD`、`DEFAULT_FROM_EMAIL`、`BASE_URL` 和 `STATIC_PATH`——仍然可以通过不带 `GRAMPSWEB_` 前缀的环境变量进行设置。此方式已弃用，启动时会记录警告，并将在未来版本中停止工作。请始终使用带前缀的形式，例如使用 `GRAMPSWEB_TREE`，而不是 `TREE`。

    请注意，这仅涉及环境变量。在配置文件中，设置名称始终不带前缀。

!!! tip "检查已弃用的选项"
    如果您的服务器仍依赖已弃用的配置选项（例如未加前缀的环境变量、`SEARCH_INDEX_DIR` 或 `EMAIL_USE_TLS`），启动时会将其记录为警告。自 Gramps Web API 3.22 起，当您以管理员身份登录时，这些选项还会显示在**系统信息**页面顶部（可通过顶部应用栏中的用户图标访问），并列出相应的替代选项以及支持将被移除的版本。

    旧版本首次运行向导存储在数据库中的电子邮件设置和基本 URL 也会列在那里。请在配置中将它们设置为存储的值；匹配后警告将消失。

## 现有配置设置
以下配置选项可用。

### 必需设置

键 | 描述
----|-------------
`TREE` | 要使用的家谱数据库名称。使用 `gramps -l` 显示可用的家谱。如果不存在此名称的家谱，将创建一个新的空家谱。
`SECRET_KEY` | Flask 的密钥。该密钥不得公开共享。更改它将使所有访问令牌失效。
`USER_DB_URI` | 用户数据库的数据库 URL。允许使用任何与 SQLAlchemy 兼容的 URL。

!!! info
    您可以使用以下命令生成安全的密钥，例如：

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### 可选设置

键 | 描述
----|-------------
`MEDIA_BASE_DIR` | 用作媒体文件基目录的路径，可覆盖 Gramps 中设置的媒体基目录。使用 [S3](s3.md) 时，必须采用 `s3://<bucket_name>` 的形式
`TREE_ID` | 单家谱模式下要使用的家谱数据库目录名称（当 `TREE` 未设置为 `*` 时）。设置后，服务器会通过目录名称而不是显示名称识别家谱，这样对重命名更加稳健。如果您希望通过 API 重命名家谱，则必须设置此项。可通过 `GET /api/trees/-` 找到目录名称（`id` 字段）。
`SEARCH_INDEX_DB_URI` | 搜索索引的数据库 URL。仅允许使用 `sqlite` 或 `postgresql` 作为后端。默认为 `sqlite:///indexdir/search_index.db`，会在脚本运行路径下的 `indexdir` 文件夹中创建 SQLite 文件
`SEARCH_INDEX_DIR` | **已弃用**（请改用 `SEARCH_INDEX_DB_URI`）。包含搜索索引的目录。如果设置了此项而未设置 `SEARCH_INDEX_DB_URI`，则搜索索引 URL 将派生为 `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`。
`STATIC_PATH` | 提供静态文件的路径（例如静态 Web 前端）
`BASE_URL` | 可访问 API 的基本 URL（例如 `https://mygramps.mydomain.com/`）。例如，构建正确的密码重置链接时需要此项。Web Push 还需要一个可公开访问的 HTTPS URL；默认的 `http://localhost/` 会禁用 Web Push。通过环境配置此设置时，请使用 `GRAMPSWEB_BASE_URL`。
`CORS_ORIGINS` | 允许发起 CORS 请求的来源。默认情况下，所有来源都不允许。使用 `"*"` 可允许来自任何域的请求。
`EMAIL_HOST` | SMTP 服务器主机（例如用于发送密码重置电子邮件）
`EMAIL_PORT` | SMTP 服务器端口。默认为 465
`EMAIL_HOST_USER` | SMTP 服务器用户名
`EMAIL_HOST_PASSWORD` | SMTP 服务器密码
`EMAIL_USE_TLS` | **已弃用**（请改用 `EMAIL_USE_SSL` 或 `EMAIL_USE_STARTTLS`）。布尔值，表示发送电子邮件时是否使用 TLS。默认为 `True`。使用 STARTTLS 时，请将此项设置为 `False`，并使用不同于 25 的端口。
`EMAIL_USE_SSL` | 布尔值，表示 SMTP 是否使用隐式 SSL/TLS（v3.6.0+）。如果未明确设置 `EMAIL_USE_TLS`，则默认为 `True`。通常与端口 465 搭配使用。
`EMAIL_USE_STARTTLS` | 布尔值，表示 SMTP 是否使用显式 STARTTLS（v3.6.0+）。默认为 `False`。通常与端口 587 或 25 搭配使用。
`DEFAULT_FROM_EMAIL` | 自动发送电子邮件的“发件人”地址
`THUMBNAIL_CACHE_CONFIG` | 缩略图缓存的设置字典。有关可用设置，请参阅 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`REQUEST_CACHE_CONFIG` | 请求缓存的设置字典。有关可用设置，请参阅 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`PERSISTENT_CACHE_CONFIG` | 持久缓存的设置字典，例如用于遥测。有关可用设置，请参阅 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`CELERY_CONFIG` | Celery 后台任务队列的设置。有关可用设置，请参阅 [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)。
`REPORT_DIR` | 存储运行 Gramps 报告输出的临时目录
`EXPORT_DIR` | 存储导出 Gramps 数据库输出的临时目录
`BACKUP_DIR` | 存储[备份](../administration/backups.md)的目录，每个家谱使用一个子目录（v3.24.0+）。如果未设置（默认情况），则无法在服务器上存储备份，但仍可从上传的文件中恢复备份。请使用持久化位置，例如 Docker 卷，并最好确保该位置本身也已备份或同步到其他位置。
`BACKUP_KEEP` | 每个家谱保留的备份数量；创建新备份时会删除较早的备份（v3.24.0+）。默认为 `5`
`RATE_LIMIT_BACKUP` | 创建备份的速率限制，按家谱计算（v3.24.0+）。默认为 `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | 在导出页面创建媒体存档的速率限制。默认为 `"1 per hour"`
`REGISTRATION_DISABLED` | 如果为 `True`，则禁止新用户注册（默认为 `False`）。自 Gramps Web API 3.26 起，登录页面还会隐藏注册链接。
`PROXY_FIX_X_FOR` | Gramps Web 前方受信任的反向代理数量（v3.26.0+）。在单个反向代理后方设置为 `1`，这样速率限制将按客户端应用，而不是对所有用户统一应用。默认为 `0`。只有在服务器只能通过这些代理访问时才设置此项。
`DISABLE_TELEMETRY` | 如果为 `True`，则禁用统计遥测（默认为 `False`）。详情请参阅[遥测](telemetry.md)。
`PILLOW_MAX_IMAGE_PIXELS` | 设置 `PIL.Image.MAX_IMAGE_PIXELS` 参数，该参数表示所处理图像可以包含的像素数量。详情请参阅 [文档](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS)。
`MAX_THUMBNAIL_FILE_BYTES` | 为缩略图设置硬性最大文件大小。默认为 `50 * 1024 * 1024`（50 MB）。提高此值可能会大幅增加内存使用量；如果大文件在内存中解压，可能导致内存不足崩溃或数据丢失。


!!! info
    使用环境变量进行配置时，诸如 `EMAIL_USE_SSL` 之类的布尔选项必须是字符串 `true` 或 `false`（区分大小写）！


### PostgreSQL 数据库的设置

如果您的家谱托管在使用 SharedPostgreSQL 插件的 [PostgreSQL 数据库](postgres.md)中，则必须设置以下选项。

键 | 描述
----|-------------
`POSTGRES_USER` | 数据库连接的用户名
`POSTGRES_PASSWORD` | 数据库用户的密码


### 与托管多个家谱相关的设置

使用[托管多个家谱](multi-tree.md)时，以下设置与此相关。


键 | 描述
----|-------------
`MEDIA_PREFIX_TREE` | 布尔值，表示是否为每个家谱的媒体文件使用单独的子文件夹。默认为 `False`，但强烈建议在多家谱设置中使用 `True`
`NEW_DB_BACKEND` | 新创建家谱所使用的数据库后端。必须是 `sqlite` 或 `sharedpostgresql` 之一。默认为 `sqlite`。仍接受 `postgresql` 值，但已弃用，因为 PostgreSQL 后端将在 Gramps Web API 4.0 中移除。
`POSTGRES_HOST` | 使用 SharedPostgreSQL 后端的多家谱设置中，用于创建新家谱的 PostgreSQL 服务器主机名
`POSTGRES_PORT` | 使用 SharedPostgreSQL 后端的多家谱设置中，用于创建新家谱的 PostgreSQL 服务器端口


### OIDC 身份验证的设置

如果您希望使用外部提供商进行 OpenID Connect（OIDC）身份验证，则需要这些设置。有关详细的设置说明和示例，请参阅 [OIDC 身份验证](oidc.md)。

键 | 描述
----|-------------
`OIDC_ENABLED` | 布尔值，表示是否启用 OIDC 身份验证。默认为 `False`。
`OIDC_ISSUER` | OIDC 提供商颁发者 URL（用于自定义 OIDC 提供商）
`OIDC_CLIENT_ID` | OAuth 客户端 ID（用于自定义 OIDC 提供商）
`OIDC_CLIENT_SECRET` | OAuth 客户端密钥（用于自定义 OIDC 提供商）
`OIDC_NAME` | 提供商的自定义显示名称。默认为 "OIDC"
`OIDC_SCOPES` | OAuth 作用域。默认为 "openid email profile"
`OIDC_USERNAME_CLAIM` | 用于用户名的声明。默认为 "preferred_username"
`OIDC_OPENID_CONFIG_URL` | 可选：OpenID Connect 配置端点的 URL（如果不使用标准 `/.well-known/openid-configuration`）
`OIDC_PKCE` | 布尔值，表示是否使用 PKCE。如果未设置，则当提供商的发现文档列出 `S256` 时使用 PKCE。请参阅 [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | 布尔值，表示是否禁用本地用户名/密码身份验证。默认为 `False`
`OIDC_AUTO_REDIRECT` | 布尔值，表示配置的提供商只有一个时是否自动重定向到 OIDC。默认为 `False`
`OIDC_ALLOWED_REDIRECT_URIS` | 原生应用可接收登录结果的 `https` URI 列表（v3.26.0+），在环境变量中设置为 JSON 列表。默认为空。只有当原生应用的文档要求时才需要。请参阅[原生应用](oidc.md#native-apps)

#### 内置 OIDC 提供商

对于内置提供商（Google、Microsoft），请使用以下设置：

键 | 描述
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth 的客户端 ID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth 的客户端密钥
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth 的客户端 ID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth 的客户端密钥
`OIDC_GOOGLE_PKCE` | 布尔值，Google 的 PKCE 设置，请参阅 [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | 布尔值，Microsoft 的 PKCE 设置，请参阅 [PKCE](oidc.md#pkce)

#### OIDC 角色映射

这些设置允许您将身份提供商中的 OIDC 组/角色映射到 Gramps Web 用户角色：

键 | 描述
----|-------------
`OIDC_ROLE_CLAIM` | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"
`OIDC_GROUP_ADMIN` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“管理员”角色
`OIDC_GROUP_OWNER` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“所有者”角色
`OIDC_GROUP_EDITOR` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“编辑者”角色
`OIDC_GROUP_CONTRIBUTOR` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“贡献者”角色
`OIDC_GROUP_MEMBER` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“成员”角色
`OIDC_GROUP_GUEST` | OIDC 提供商中的组/角色名称，映射到 Gramps 的“访客”角色

### 仅适用于 AI 功能的设置

如果您希望使用 AI 聊天，则需要这些设置。详情请参阅 [设置 AI 聊天](chat.md)。

!!! note
    自 Gramps Web API 3.25 起，用于语义搜索的 `VECTOR_EMBEDDING_MODEL`、`VECTOR_EMBEDDING_BASE_URL` 和 `VECTOR_EMBEDDING_API_KEY` 设置会被忽略，因为该版本移除了语义搜索。AI 聊天只需要 `LLM_MODEL`。

键 | 描述
----|-------------
`LLM_BASE_URL` | 兼容 OpenAI 的聊天 API 的基本 URL。默认为 `None`，即使用 OpenAI API。
`LLM_MODEL` | 用于兼容 OpenAI 的聊天 API 的模型。如果未设置（默认情况），则禁用聊天功能。从 v3.6.0 起，AI 助手使用支持工具调用功能的 Pydantic AI。
`LLM_MAX_OUTPUT_TOKENS` | 模型在单次响应中可以生成的最大令牌数。默认未设置，此时限制由模型服务器决定。适用于自身没有限制的模型服务器，否则响应可能无限持续。
`LLM_MAX_CONTEXT_LENGTH` | 提供给 LLM 的家谱上下文字符数限制。默认为 50000。
`LLM_SYSTEM_PROMPT` | LLM 聊天助手的自定义系统提示词（v3.6.0+）。如果未设置，则使用针对家谱优化的默认提示词。
`LLM_VISION` | 布尔值，表示用户是否可以在问题中附加图像（v3.26.0+）。仅当模型接受图像时才启用。默认为 `False`。请参阅[问题中的图像](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | 布尔值，表示助手是否可以向用户提议对家谱进行更改，以供用户审核和应用（v3.26.0+）。默认为 `False`。请参阅[允许助手提议更改](chat.md#letting-the-assistant-propose-changes)


## 配置文件示例

用于生产环境的最小配置文件可能如下所示：
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
