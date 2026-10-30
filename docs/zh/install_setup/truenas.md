# TrueNAS 设置

本指南解释了如何在 TrueNAS Community Edition 25.04 上设置 Gramps Web。

!!! warning
    本指南适用于 TrueNAS Community Edition 25.04 或更高版本，该版本引入了基于 Docker Compose 的新应用程序系统。它不适用于早期版本的 TrueNAS。

## 先决条件

- TrueNAS Community Edition 25.04 或更高版本
- 对 TrueNAS 网络界面的基本熟悉
- 用于存储 Gramps Web 数据的数据集

## 概述

TrueNAS Community Edition 25.04 引入了一种基于 Docker Compose 的新应用程序系统，取代了以前基于 Helm 图表的方法。本指南将指导您使用 Docker Compose 为 Gramps Web 创建自定义应用程序。

## 第 1 步：准备存储

1. 在 TrueNAS 网络界面中导航到 **Datasets**
2. 创建一个新的数据集用于 Gramps Web（例如，`grampsweb`）。请记下此数据集的完整路径，例如 `/mnt/storage/grampsweb`，因为您稍后会需要它。

为各个组件创建子目录：
- `users` - 用户数据库
- `database` - Gramps 数据库文件
- `media` - 媒体文件

## 第 2 步：创建 Docker Compose 应用程序

1. 在 TrueNAS 网络界面中导航到 **Apps**
2. 点击 **Discover Apps**
3. 搜索 "Gramps Web" 并点击它
4. 点击 "Install"

这将带您进入应用程序配置页面。

## 第 3 步：配置应用程序

### Gramps Web 配置

- **时区：** 设置为您的本地时区（例如，`Europe/Berlin`）
- **Redis 密码：** 为 Redis 设置一个密码。此密码仅供应用程序内部使用。
- **禁用遥测：** 请保持此框未选中 – 详细信息请参见 [这里](telemetry.md)。
- **密钥：** 您必须将其设置为强大且唯一的值。有关生成随机密钥的说明，请参见 [服务器配置](configuration.md#existing-configuration-settings)。
- **附加环境变量：** 您需要将所有附加的 [配置选项](configuration.md) 设置为以 `GRAMPSWEB_` 为前缀的环境变量。请详细检查 [配置文档](configuration.md) – 例如，布尔值需要在环境变量中设置为 `true` 或 `false`（全小写），这是一个常见的陷阱。

请 **至少** 将 `GRAMPSWEB_BASE_URL` 设置为您的 Gramps Web 实例可访问的 URL – 这是正常操作所必需的。

您可能还希望在此阶段设置电子邮件配置，这在例如密码重置时是必需的。相关的环境变量包括：

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

所有配置设置可以通过在 TrueNAS Apps 界面中点击 "Edit" 后进行更改。

### 存储配置

- **用户存储：** 选择您之前创建的 `users` 目录的路径。
- **索引存储：** 您可以保留默认设置 "ixVolume (Dataset created automatically by the system)"
- **缩略图缓存存储：** 您可以保留默认设置 "ixVolume (Dataset created automatically by the system)"
- **缓存存储：** 您可以保留默认设置 "ixVolume (Dataset created automatically by the system)"
- **媒体存储：** 选择您之前创建的 `media` 目录的路径。
- **Gramps 数据库存储：** 选择您之前创建的 `database` 目录的路径。

### 资源配置

我们建议您分配至少 2 个 CPU 和 4096 MB 的 RAM 以确保顺利运行。

## 第 4 步：访问 Gramps Web

一旦应用程序部署完成，您可以通过点击 TrueNAS Apps 界面中的 "Web UI" 按钮访问 Gramps Web。您应该会看到入门向导 "Welcome to Gramps Web"。

如果您希望允许用户访问您的 Gramps Web 界面，请 **不要** 将应用程序直接暴露于互联网，而是继续执行下一步。

## 第 5 步：设置反向代理

为了安全地将您的 Gramps Web 实例暴露给用户，建议设置反向代理。这使您能够管理 SSL/TLS 证书并控制访问。

最简单的选项是使用官方的 TrueNAS Nginx Proxy Manager 应用程序。在 TrueNAS Apps 界面中搜索该应用程序并安装。您可以将所有设置保留为默认值，但我们建议您设置一个额外的环境变量：`DISABLE_IPV6`，值为 `true`，以避免潜在的 IPv6 相关问题。

部署完成后，打开 Nginx Proxy Manager 网络界面，并使用以下设置创建一个新的代理主机：

- 方案：`http`
- 转发主机名/IP：您的 TrueNAS 服务器的主机名（例如，`truenas`）
- 转发端口：分配给您的 Gramps Web 应用程序的端口（请检查 TrueNAS Apps 界面以获取确切端口）
- 在 "SSL" 选项卡中，勾选 "Force SSL"
- 在 "SSL Certificates" 下，选择 "Add SSL Certificate" > "Let's Encrypt" 为您的域名创建一个新的 Let's Encrypt 证书。

有关配置路由器和获取 SSL 证书的更多详细信息，请参见 [Nginx Proxy Manager 文档](https://nginxproxymanager.com/guide/)。
