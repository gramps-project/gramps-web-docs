# 使用 Docker 部署 Gramps Web

在您自己的服务器（或虚拟服务器）上托管 Gramps Web 的最方便选项是使用 Docker Compose。

我们假设您的系统中已经安装了 Docker 和 Docker Compose。您可以使用 Windows、Mac OS 或 Linux 作为主机系统。支持的架构不仅包括 x86-64（桌面系统），还包括 ARM 系统，例如 Raspberry Pi，它可以作为一个低成本但足够强大的 Web 服务器。

!!! note
    您不需要在服务器上安装 Gramps，因为它包含在 Docker 镜像中。


## 第一步：Docker 配置

在服务器上创建一个名为 `docker-compose.yml` 的新文件，并插入以下内容：[docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

这将生成六个命名卷，以确保所有相关数据在重启容器时能够持久化。

!!! warning
    上述配置将使 API 在主机机器的 80 端口上可用 **而没有 SSL/TLS 保护**。您可以将其用于本地测试，但请不要直接将其暴露于互联网，这完全不安全！

## 第二步：使用 SSL/TLS 保护访问

Web API **必须** 通过 HTTPS 提供给公共互联网。有几种选项，例如：

- 使用自动包含 SSL/TLS 的 Docker 托管
- 使用带有 Let's Encrypt 证书的 Nginx 反向代理

有关如何设置前者，请参见 [Docker with Let's Encrypt](lets_encrypt.md)。

如果您计划仅在本地网络上使用 Gramps Web，可以跳过此步骤。

## 第三步：启动服务器

运行

```
docker compose up -d
```

首次运行时，应用程序将显示首次运行向导，允许您：

- 为所有者（管理员）用户创建一个帐户
- 设置一些必要的配置选项
- 导入 Gramps XML (`.gramps`) 格式的家谱

## 第四步：上传媒体文件

有几种上传媒体文件的选项。

- 当使用存储在与 Gramps Web 相同服务器上的文件时，您可以将目录挂载到 Docker 容器中，而不是使用命名卷，即 `/home/server_user/gramps_media/:/app/media` 而不是 `gramps_media:/app/media`，并在此处上传您的媒体文件。
- 当使用 [托管在 S3 上的媒体文件](s3.md) 时，您可以使用 S3 媒体上传插件。
- 可以说最方便的选项是使用 [Gramps Web Sync](../administration/sync.md)。
