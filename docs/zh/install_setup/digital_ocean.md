# Gramps Web DigitalOcean 一键应用

除了[自行设置 Gramps Web](deployment.md)之外，您还可以使用 [Gramps Web DigitalOcean 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)。Digital Ocean 托管 Gramps Web 的演示版本。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean 推荐徽章" /></a>

作为设置过程的一部分，您需要注册一个 DigitalOcean 账户，并为要使用的“droplet”（虚拟机）选择付费套餐。

可以说，目前这是部署您自己的自托管 Gramps Web 实例的最简单方式，而且无需使用您自己的硬件即可通过 SSL 保护实例。

!!! info
    请注意，您需要向 DigitalOcean 支付托管服务费用。Gramps 开源项目不提供付费支持。

## 第 1 步：创建 DigitalOcean 账户

如果您还没有 DigitalOcean 账户，请在 [DigitalOcean](https://www.digitalocean.com/) 创建一个账户。

## 第 2 步：创建 droplet

- 前往 [Gramps Web 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)，然后点击“Create Gramps Web Droplet”。
- 选择至少具有 2 GB RAM 的套餐。
- 设置 droplet 的身份验证
- 点击“Create Droplet”

## 第 3 步：设置域名

您需要一个域名（或子域名）。如果您拥有域名，请将其指向 droplet 的 IP 地址。否则，您可以使用 [DuckDNS](https://www.duckdns.org/) 等免费服务。

## 第 4 步：登录 droplet

通过 SSH 登录您的 droplet。您应该会看到消息“Welcome to the Gramps Web DigitalOcean 1-click app setup!”。如果没有看到，请等待几分钟后重试（安装尚未完成）。

设置脚本会要求您提供域名（例如 `mygrampswebinstance.duckdns.org`）和电子邮件地址（Let's Encrypt 证书所需）。此外，脚本还可能会询问 Gramps Web 用于发送电子邮件的 SMTP 设置，例如发送密码重置邮件；如果要跳过此步骤，请将 SMTP 主机留空。

完成后，请等待后台完成设置

## 第 5 步：启动 Gramps Web

现在，您应该可以在域名的根目录访问 Gramps Web 实例，并且该实例应具有有效的 SSL 证书，同时显示首次运行助手。

## 稍后更改配置

设置脚本会将基本 URL 和电子邮件设置作为[配置选项](configuration.md)存储在文件 `/root/letsencrypt.env` 中，并为选项添加 `GRAMPSWEB_` 前缀，例如：

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

要添加或更改设置，请在 droplet 上编辑此文件，然后运行以下命令应用更改：

```bash
cd /opt/grampsweb && docker compose up -d
```
