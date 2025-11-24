要在本地计算机（Linux、Mac 或 Windows）上试用 Gramps Web，而不干扰您的 Gramps Desktop 安装，您可以使用以下命令通过 Docker：

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

这将使一个新的空的 Gramps Web 实例在 [http://localhost:5055](http://localhost:5055) 可访问，您可以在此创建管理员用户并导入 Gramps XML 文件。

!!! info
    由于此简单设置不允许在单独的进程中运行长时间任务，因此导入大型 Gramps XML 文件可能会因为首次运行助手中的超时而失败。


要使用计算机上的媒体文件，您可以将 Gramps 媒体文件夹挂载到容器中，使用以下命令：

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

请注意，这不会在您重新启动容器时保留对数据库所做的更改。要正确设置 Gramps Web，请继续阅读 [部署](deployment.md) 的相关内容。
