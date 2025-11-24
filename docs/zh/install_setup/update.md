# 更新 Gramps Web

如果您使用基于 Docker Compose 的安装方法，将 Gramps Web 更新到最新版本非常简单。在您的 `docker-compose.yml` 文件所在的文件夹中，运行以下命令

```bash
docker compose pull
docker compose up -d
```

对于 [Gramps Web API](https://github.com/gramps-project/gramps-web-api) 的小版本跳跃，这就是所需的全部。不过，请遵循 [Gramps Web API 的发布说明](https://github.com/gramps-project/gramps-web-api/releases)，因为可能会有需要额外关注或配置更改的重大更改。

请注意，默认的 `grampsweb:latest` docker 镜像始终将 API 的最新版本与前端的最新版本结合在一起。如果您想单独升级这两个组件 - 这是可能的 - 则需要比这里描述的更复杂的设置。
