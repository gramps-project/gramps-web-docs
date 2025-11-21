# 使用 PostgreSQL 数据库

默认情况下，Gramps 使用基于文件的 SQLite 数据库来存储家谱。这对于 Gramps Web 完全可以正常工作，并且推荐给大多数用户。然而，从 Gramps Web API 版本 0.3.0 开始，也支持每个数据库一个家谱的 PostgreSQL 服务器，这得益于 [Gramps PostgreSQL 插件](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL)。自 [版本 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) 起，还支持 SharedPostgreSQL 插件，该插件允许在单个数据库中托管多个家谱，这在与 Gramps Web API 的 [多树支持](multi-tree.md) 一起使用时特别有用。

## 设置 PostgreSQL 服务器

如果您想为 PostgreSQLAddon 设置一个新的数据库，可以按照 [Gramps Wiki 中的说明](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) 来设置服务器。

或者，您也可以使用 Docker Compose 在与 Gramps Web 相同的 Docker 主机上运行 PostgreSQL 服务器。

使用 Docker 化的 PostgreSQL 与 Gramps 的唯一复杂之处在于默认的 PostgreSQL 镜像没有安装任何语言环境，而 Gramps 需要这些语言环境来进行对象的本地化排序。最简单的选择是使用在 [这个仓库](https://github.com/DavidMStraub/gramps-postgres-docker/) 中发布的 `gramps-postgres` 镜像。要使用它，请在您的 `docker-compose.yml` 中添加以下部分：
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
并在此 YAML 文件的 `volumes:` 部分下添加 `postgres_data:` 作为键。该镜像包含一个用于 Gramps 家谱数据的单独数据库和一个用于 Gramps 用户数据库的单独数据库；它们各自可以有不同的密码。

## 导入 Gramps 家谱

同样，如果您自己设置了 PostgreSQL 服务器，可以按照 [Gramps Wiki 中的说明](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) 将家谱导入数据库。

或者，如果您按照上述 Docker Compose 指令操作，可以使用以下命令导入位于 Docker 主机上的 Gramps XML 文件：

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## 配置 Web API 以使用数据库

要配置 Web API 以使用 PostgreSQL 数据库，请在 `docker-compose.yml` 中 `grampsweb` 服务的 `environment:` 键下添加以下内容：

```yaml
      # PostgreSQL 插件假设树名与
      # 数据库名相同，这里使用的是
      # PostgreSQL 镜像的默认数据库名
      TREE: postgres
      # 凭据必须与
      # PostgreSQL 容器中使用的凭据一致
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## 在多树安装中使用共享 PostgreSQL 数据库

在使用 [多树设置](multi-tree.md) 时，SharedPostgreSQL 插件是一个方便的选项，可以在单个 PostgreSQL 数据库中托管所有树，包括通过 API 新创建的树，而不影响隐私或安全性。

为此，按照上述描述基于 `gramps-postgres` 镜像设置一个容器，并简单地将配置选项 `NEW_DB_BACKEND` 设置为 `sharedpostgresql`，例如通过 `GRAMPSWEB_NEW_DB_BACKEND` 环境变量。

## 使用 PostgreSQL 数据库作为用户数据库

无论用于家谱数据的数据库后端是什么，用户数据库都可以通过提供适当的数据库 URL 在 PostgreSQL 数据库中托管。上述提到的 `gramps-postgres` Docker 镜像包含一个可以用于此目的的单独数据库 `grampswebuser`。在这种情况下，`USER_DB_URI` 配置选项的适当值将是
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## 使用 PostgreSQL 数据库作为搜索索引

自 Gramps Web API 版本 2.4.0 起，搜索索引可以托管在 SQLite 数据库（默认）或 PostgreSQL 数据库中。为了这个目的，也可以使用 `gramps-postgres` 镜像。对于搜索索引，我们可以使用镜像提供的 `gramps` 数据库，无论我们是否在 PostgreSQL 中托管我们的家谱数据（搜索索引和家谱数据可以共存于同一数据库中）。在上述示例中，可以通过将 `SEARCH_INDEX_DB_URI` 配置选项设置为
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```
来实现。

## 问题

如果出现问题，请监控 Gramps Web 和 PostgreSQL 服务器的日志输出。在 Docker 的情况下，可以使用以下命令：

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

如果您怀疑 Gramps Web（或文档）存在问题，请在 [Github](https://github.com/gramps-project/gramps-web-api/issues) 上提交问题。
