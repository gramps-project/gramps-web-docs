# 使用 PostgreSQL 数据库

默认情况下，Gramps Web 将每个家谱存储在其自己的 SQLite 数据库文件中。这不需要额外的服务，备份也仅仅是复制文件，这对于大多数安装来说都很有效，包括 [托管多个家谱](multi-tree.md) 的安装。

另外，家谱可以使用 SharedPostgreSQL 插件托管在 PostgreSQL 服务器上，这样可以将所有家谱存储在一个数据库中。如果您已经运行 PostgreSQL 服务器并希望在其中管理备份和监控，或者如果您预计有许多用户同时编辑，这样做是有意义的。PostgreSQL 还可以独立于家谱存储位置，托管 [用户数据库](#using-a-postgresql-database-for-the-user-database) 和 [搜索索引](#using-a-postgresql-database-for-the-search-index)。

!!! warning "PostgreSQL 插件已弃用"
    较旧的 PostgreSQL 插件，每个数据库存储一个家谱，自 Gramps Web API 3.24 起已弃用，并且在 Gramps Web API 4.0 中将不再支持，因为它与托管多个家谱不兼容，而后者在该版本中成为默认。如果您正在使用它，请参见 [将树从 PostgreSQL 插件移动到 SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql)。

## 设置 PostgreSQL 服务器

最简单的选项是在与 Gramps Web 相同的 Docker 主机上使用 Docker Compose 在容器中运行 PostgreSQL 服务器。

Gramps 需要在 PostgreSQL 服务器上安装区域设置，以便在不同语言中正确排序对象，而默认的 PostgreSQL 镜像不包含任何区域设置。[`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) 镜像添加了这些区域设置。要使用它，请将以下部分添加到您的 `docker-compose.yml` 中：
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
并在该 YAML 文件的 `volumes:` 部分下添加 `postgres_data:` 作为键。该镜像包含两个数据库，每个数据库都有自己的用户和密码：`gramps` 用于家谱数据，`grampswebuser` 用于 Gramps Web 用户数据库。

如果您使用自己的 PostgreSQL 服务器，请创建一个名为 `gramps` 的数据库，以便配置的用户可以在其中创建表，并确保安装了用户所需的区域设置。

## 配置 Gramps Web

当 Gramps Web 在 [多树模式](multi-tree.md) 下运行，并且 `NEW_DB_BACKEND` 配置选项设置为 `sharedpostgresql` 时，会在 SharedPostgreSQL 数据库中创建新的家谱。使用上述 Docker Compose 设置，在 `docker-compose.yml` 中 `grampsweb` 服务的 `environment:` 键下添加以下内容：

```yaml
      # 启用多树模式
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # 在 SharedPostgreSQL 数据库中创建新树
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQL 服务器的主机和端口。主机是上面 PostgreSQL 服务的名称
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # 凭据必须与用于 PostgreSQL 容器的凭据一致
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

有关所有这些选项的描述，请参见 [配置](configuration.md)。请注意，主机和端口在创建每棵树时都会保存，因此稍后更改它们仅会影响新树。

## 创建树和导入数据

要创建新树，请向 `/trees/` 端点发送 POST 请求，如 [托管多个树的设置](multi-tree.md#create-a-new-tree) 中所述。响应包含新树的 ID，您需要该 ID 来 [创建树主账户](../administration/owner.md#multi-tree-setup-create-tree-owner-account)。

一旦树主登录，他们可以通过 Web 界面 [导入](../administration/import.md) 现有的家谱，例如从 Gramps Desktop 导出的 Gramps XML 文件。

## 使用 PostgreSQL 数据库作为用户数据库

用户数据库通常是一个 SQLite 文件，无论家谱托管在哪里。要改为使用 PostgreSQL，请将 `USER_DB_URI` 配置选项设置为 PostgreSQL 数据库 URL。使用上面的 `gramps-postgres` 镜像，使用其 `grampswebuser` 数据库：
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 使用 PostgreSQL 数据库作为搜索索引

默认情况下，搜索索引也存储在 SQLite 中。要改为使用 PostgreSQL，请将 `SEARCH_INDEX_DB_URI` 配置选项设置为 PostgreSQL 数据库 URL。使用上面的 `gramps-postgres` 镜像，您可以使用其 `gramps` 数据库，无论您的家谱是否也托管在那里：
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## 将树从 PostgreSQL 插件移动到 SharedPostgreSQL

较旧的安装可能使用 PostgreSQL 插件托管其家谱，该插件每个数据库存储一个家谱，并已弃用。要找出树使用的插件，请查看 Gramps 数据库目录中树的子目录中的文件 `database.txt`：它包含 `postgresql` 表示已弃用的 PostgreSQL 插件，`sharedpostgresql` 表示 SharedPostgreSQL。

要在同一安装中将树从 PostgreSQL 插件移动到 SharedPostgreSQL，同时保留您的用户账户和媒体文件：

1. [备份您的家谱](../administration/export.md#back-up-your-family-tree) 为 Gramps XML (`.gramps`) 文件，使用可以查看私有记录的账户。
2. 按照 [配置 Gramps Web](#configuring-gramps-web) 中的描述更改您的配置。您可以继续使用现有的 `gramps-postgres` 容器。
3. [创建新树](multi-tree.md#create-a-new-tree) 并记下其树 ID。
4. 按照 [迁移现有用户数据库](multi-tree.md#migrate-existing-user-database) 的描述，将您现有的用户账户分配给新树。
5. 按照 [迁移现有媒体文件](multi-tree.md#migrate-existing-media-files) 的描述，将您的媒体文件移动到新树预期的位置。
6. 登录并 [导入](../administration/import.md) Gramps XML 文件到新树中。

在您检查新树完整之前，请保留 Gramps XML 文件。

如果您要迁移到单独的 Gramps Web 安装，请按照 [迁移到不同的 Gramps Web 实例](../administration/export.md#move-to-a-different-gramps-web-instance) 中的步骤进行。

## 问题

如遇问题，请监控 Gramps Web 和 PostgreSQL 服务器的日志输出。在 Docker 的情况下，可以使用以下命令：

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

如果您怀疑 Gramps Web（或文档）存在问题，请在 [Github](https://github.com/gramps-project/gramps-web-api/issues) 上提交问题。
