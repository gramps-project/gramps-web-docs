# 服务器配置

使用默认的 Docker 镜像，所有必要的配置都可以通过浏览器进行。然而，根据部署情况，可能需要自定义服务器配置。

本页面列出了所有更改配置的方法和所有现有的配置选项。


## 配置文件与环境变量

对于设置，您可以使用配置文件或环境变量。

当您使用 [基于 Docker Compose 的设置](deployment.md) 时，可以通过在 `grampsweb:` 块的 `volumes:` 键下添加以下列表项来包含配置文件：

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
其中 `/path/to/config.cfg` 是您服务器文件系统中配置文件的路径（右侧指的是容器中的路径，不能更改）。

使用环境变量时，

- 每个设置名称前缀加上 `GRAMPSWEB_` 以获得环境变量的名称
- 对于嵌套字典设置，使用双下划线，例如 `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` 将设置 `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` 配置选项的值

请注意，通过环境设置的配置选项优先于配置文件中的选项。如果两者都存在，环境变量将“胜出”。

!!! warning "未加前缀的环境变量已被弃用"
    出于历史原因，一些设置 – `TREE`、`SECRET_KEY`、`USER_DB_URI`、`POSTGRES_USER`、`POSTGRES_PASSWORD`、`MEDIA_BASE_DIR`、`SEARCH_INDEX_DIR`、`EMAIL_HOST`、`EMAIL_PORT`、`EMAIL_HOST_USER`、`EMAIL_HOST_PASSWORD`、`DEFAULT_FROM_EMAIL`、`BASE_URL` 和 `STATIC_PATH` – 仍然可以通过不带 `GRAMPSWEB_` 前缀的环境变量进行设置。这已被弃用，在启动时会记录警告，并将在未来的版本中停止工作。始终使用带前缀的形式，例如 `GRAMPSWEB_TREE` 而不是 `TREE`。

    请注意，这仅涉及环境变量。在配置文件中，设置名称始终使用未加前缀的形式。

## 现有配置设置
以下配置选项是存在的。

### 必需设置

键 | 描述
----|-------------
`TREE` | 要使用的家谱数据库的名称。使用 `gramps -l` 显示可用的树。如果不存在具有此名称的树，将创建一个新的空树。
`SECRET_KEY` | Flask 的秘密密钥。该秘密不得公开共享。更改它将使所有访问令牌失效。
`USER_DB_URI` | 用户数据库的数据库 URL。允许任何与 SQLAlchemy 兼容的 URL。

!!! info
    您可以通过以下命令生成安全的秘密密钥

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### 可选设置

键 | 描述
----|-------------
`MEDIA_BASE_DIR` | 用作媒体文件的基本目录的路径，覆盖 Gramps 中设置的媒体基本目录。当使用 [S3](s3.md) 时，必须具有 `s3://<bucket_name>` 的形式
`TREE_ID` | 在单树模式下使用的家谱数据库的目录名称（当 `TREE` 未设置为 `*` 时）。设置后，服务器通过其目录名称而不是显示名称来识别树，这对重命名更为稳健。如果您想通过 API 重命名树，则需要此设置。目录名称可以通过 `GET /api/trees/-` 找到（`id` 字段）。
`SEARCH_INDEX_DB_URI` | 搜索索引的数据库 URL。仅允许 `sqlite` 或 `postgresql` 作为后端。默认为 `sqlite:///indexdir/search_index.db`，在脚本运行路径下的 `indexdir` 文件夹中创建一个 SQLite 文件
`SEARCH_INDEX_DIR` | **已弃用**（请使用 `SEARCH_INDEX_DB_URI`）。包含搜索索引的目录。如果在 `SEARCH_INDEX_DB_URI` 未设置时设置，则搜索索引 URL 将推导为 `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`。
`STATIC_PATH` | 提供静态文件的路径（例如，一个静态网页前端）
`BASE_URL` | API 可访问的基本 URL（例如 `https://mygramps.mydomain.com/`）。这对于构建正确的密码重置链接是必要的
`CORS_ORIGINS` | 允许 CORS 请求的来源。默认情况下，所有请求都被拒绝。使用 `"*"` 允许来自任何域的请求。
`EMAIL_HOST` | SMTP 服务器主机（例如，用于发送密码重置电子邮件）
`EMAIL_PORT` | SMTP 服务器端口。默认为 465
`EMAIL_HOST_USER` | SMTP 服务器用户名
`EMAIL_HOST_PASSWORD` | SMTP 服务器密码
`EMAIL_USE_TLS` | **已弃用**（请使用 `EMAIL_USE_SSL` 或 `EMAIL_USE_STARTTLS`）。布尔值，是否在发送电子邮件时使用 TLS。默认为 `True`。使用 STARTTLS 时，将其设置为 `False`，并使用与 25 不同的端口。
`EMAIL_USE_SSL` | 布尔值，是否对 SMTP 使用隐式 SSL/TLS（v3.6.0+）。如果未显式设置 `EMAIL_USE_TLS`，则默认为 `True`。通常与端口 465 一起使用。
`EMAIL_USE_STARTTLS` | 布尔值，是否对 SMTP 使用显式 STARTTLS（v3.6.0+）。默认为 `False`。通常与端口 587 或 25 一起使用。
`DEFAULT_FROM_EMAIL` | 自动电子邮件的“发件人”地址
`THUMBNAIL_CACHE_CONFIG` | 包含缩略图缓存设置的字典。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`REQUEST_CACHE_CONFIG` | 包含请求缓存设置的字典。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`PERSISTENT_CACHE_CONFIG` | 包含持久缓存设置的字典，例如用于遥测。有关可能的设置，请参见 [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)。
`CELERY_CONFIG` | Celery 后台任务队列的设置。有关可能的设置，请参见 [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html)。
`REPORT_DIR` | 存储运行 Gramps 报告输出的临时目录
`EXPORT_DIR` | 存储导出 Gramps 数据库输出的临时目录
`REGISTRATION_DISABLED` | 如果为 `True`，则禁止新用户注册（默认 `False`）
`DISABLE_TELEMETRY` | 如果为 `True`，则禁用统计遥测（默认 `False`）。有关详细信息，请参见 [telemetry](telemetry.md)。
`PILLOW_MAX_IMAGE_PIXELS` | 设置 PIL.Image.MAX_IMAGE_PIXELS 参数，指示处理的图像可以包含的像素数量。有关详细信息，请参见 [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS)。
`MAX_THUMBNAIL_FILE_BYTES` | 设置缩略图的硬最大文件大小。默认为 `50 * 1024 * 1024`（50 MB）。提高此值可能会大大增加内存使用，并可能导致内存溢出崩溃或在内存中解压缩大文件时数据丢失。

!!! info
    使用环境变量进行配置时，布尔选项如 `EMAIL_USE_SSL` 必须是字符串 `true` 或 `false`（区分大小写！）。

### 仅适用于 PostgreSQL 后端数据库的设置

如果您已配置 Gramps 数据库以与 [PostgreSQL 插件](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) 一起使用，则需要此设置。

键 | 描述
----|-------------
`POSTGRES_USER` | 数据库连接的用户名
`POSTGRES_PASSWORD` | 数据库用户的密码

### 适用于托管多个树的设置

以下设置在 [托管多个树](multi-tree.md) 时相关。

键 | 描述
----|-------------
`MEDIA_PREFIX_TREE` | 布尔值，是否为每棵树的媒体文件使用单独的子文件夹。默认为 `False`，但在多树设置中强烈建议使用 `True`
`NEW_DB_BACKEND` | 新创建的家谱树要使用的数据库后端。必须是 `sqlite`、`postgresql` 或 `sharedpostgresql` 之一。默认为 `sqlite`。
`POSTGRES_HOST` | 在使用共享 PostgreSQL 后端的多树设置中，用于创建新树的 PostgreSQL 服务器的主机名
`POSTGRES_PORT` | 在使用共享 PostgreSQL 后端的多树设置中，用于创建新树的 PostgreSQL 服务器的端口

### OIDC 认证的设置

如果您想使用外部提供者的 OpenID Connect (OIDC) 认证，则需要这些设置。有关详细的设置说明和示例，请参见 [OIDC Authentication](oidc.md)。

键 | 描述
----|-------------
`OIDC_ENABLED` | 布尔值，是否启用 OIDC 认证。默认为 `False`。
`OIDC_ISSUER` | OIDC 提供者发行者 URL（针对自定义 OIDC 提供者）
`OIDC_CLIENT_ID` | OAuth 客户端 ID（针对自定义 OIDC 提供者）
`OIDC_CLIENT_SECRET` | OAuth 客户端密钥（针对自定义 OIDC 提供者）
`OIDC_NAME` | 提供者的自定义显示名称。默认为 "OIDC"
`OIDC_SCOPES` | OAuth 范围。默认为 "openid email profile"
`OIDC_USERNAME_CLAIM` | 用于用户名的声明。默认为 "preferred_username"
`OIDC_OPENID_CONFIG_URL` | 可选：OpenID Connect 配置端点的 URL（如果不使用标准的 `/.well-known/openid-configuration`）
`OIDC_DISABLE_LOCAL_AUTH` | 布尔值，是否禁用本地用户名/密码认证。默认为 `False`
`OIDC_AUTO_REDIRECT` | 布尔值，是否在仅配置一个提供者时自动重定向到 OIDC。默认为 `False`

#### 内置 OIDC 提供者

对于内置提供者（Google、Microsoft），使用以下设置：

键 | 描述
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth 的客户端 ID
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth 的客户端密钥
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth 的客户端 ID
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth 的客户端密钥

#### OIDC 角色映射

这些设置允许您将身份提供者的 OIDC 组/角色映射到 Gramps Web 用户角色：

键 | 描述
----|-------------
`OIDC_ROLE_CLAIM` | OIDC 令牌中包含用户组/角色的声明名称。默认为 "groups"
`OIDC_GROUP_ADMIN` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Admin" 角色
`OIDC_GROUP_OWNER` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Owner" 角色
`OIDC_GROUP_EDITOR` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Editor" 角色
`OIDC_GROUP_CONTRIBUTOR` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Contributor" 角色
`OIDC_GROUP_MEMBER` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Member" 角色
`OIDC_GROUP_GUEST` | 来自 OIDC 提供者的组/角色名称，映射到 Gramps 的 "Guest" 角色

### 仅适用于 AI 功能的设置

如果您想使用 AI 驱动的功能，如聊天或语义搜索，则需要这些设置。

键 | 描述
----|-------------
`LLM_BASE_URL` | OpenAI 兼容聊天 API 的基本 URL。默认为 `None`，使用 OpenAI API。
`LLM_MODEL` | 用于 OpenAI 兼容聊天 API 的模型。如果未设置（默认），则禁用聊天。从 v3.6.0 开始，AI 助手使用具有工具调用能力的 Pydantic AI。
`VECTOR_EMBEDDING_MODEL` | 用于语义搜索向量嵌入的模型。当使用本地模型时，这必须是 [Sentence Transformers](https://sbert.net/) 模型名称。当使用远程 API（见 `VECTOR_EMBEDDING_BASE_URL`）时，这是传递给远程提供者的模型名称。如果未设置（默认），则禁用语义搜索和聊天。
`VECTOR_EMBEDDING_BASE_URL` | 远程 OpenAI 兼容嵌入 API 的基本 URL（例如 Ollama、OpenAI、LiteLLM）。如果未设置（默认），则使用本地 Sentence Transformers 模型。有关详细信息，请参见 [使用远程嵌入 API](chat.md#using-a-remote-embedding-api)。
`VECTOR_EMBEDDING_API_KEY` | 用于经过身份验证的远程嵌入提供者的 API 密钥。仅在设置了 `VECTOR_EMBEDDING_BASE_URL` 且提供者需要身份验证时需要。
`LLM_MAX_CONTEXT_LENGTH` | 提供给 LLM 的家谱上下文的字符限制。默认为 50000。
`LLM_SYSTEM_PROMPT` | LLM 聊天助手的自定义系统提示（v3.6.0+）。如果未设置，则使用默认的家谱优化提示。

## 示例配置文件

一个适用于生产的最小配置文件可能如下所示：
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # 您的秘密密钥
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 对于端口 465 使用隐式 SSL
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # 您的 SMTP 密码
DEFAULT_FROM_EMAIL="gramps@example.com"
