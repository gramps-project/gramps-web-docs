# Gramps Web DigitalOcean 一键应用

您可以使用 [Gramps Web DigitalOcean 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)，而不是 [自己设置 Gramps Web](deployment.md)。Digital Ocean 托管 Gramps Web 的演示版本。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean 推荐徽章" /></a>

作为设置过程的一部分，您需要注册一个 DigitalOcean 账户，并选择一个付费计划用于“滴水”（虚拟机）。

可以说，这目前是部署您自己的自托管 Gramps Web 实例的最简单方法，使用 SSL 进行安全保护，而无需使用您自己的硬件。

!!! info
    请注意，您将为 DigitalOcean 的托管服务付费。Gramps 开源项目不提供付费支持。

## 第一步：创建一个 DigitalOcean 账户

如果您还没有账户，请在 [DigitalOcean](https://www.digitalocean.com/) 创建一个账户。

## 第二步：创建滴水

- 前往 [Gramps Web 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)，点击“创建 Gramps Web 滴水”。
- 选择至少 2 GB RAM 的计划。
- 设置对您的滴水的身份验证。
- 点击“创建滴水”。

## 第三步：设置域名

您需要一个域名（或子域名）。如果您拥有一个域名，请将其指向您的滴水的 IP 地址。否则，您可以使用如 [DuckDNS](https://www.duckdns.org/) 的免费服务。

## 第四步：登录到您的滴水

通过 SSH 登录到您的滴水。您应该看到消息“欢迎使用 Gramps Web DigitalOcean 一键应用设置！”。如果不是这种情况，请等待几分钟再试一次（安装尚未完成）。

设置脚本会询问您域名（例如 `mygrampswebinstance.duckdns.org`）和电子邮件地址（需要用于 Let's Encrypt 证书）。可选地，它还会询问 Gramps Web 用于发送电子邮件的 SMTP 设置，例如用于密码重置；将 SMTP 主机留空以跳过此步骤。

完成后，请等待后台设置完成。

## 第五步：启动 Gramps Web

您的 Gramps Web 实例现在应该可以在您域名的根目录访问，并且具有有效的 SSL 证书，并且应该显示首次运行助手。

## 之后更改配置

设置脚本将基本 URL 和电子邮件设置存储在文件 `/root/letsencrypt.env` 中，作为以 `GRAMPSWEB_` 为前缀的 [配置选项](configuration.md)，例如：

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

要添加或更改设置，请编辑滴水上的此文件，并通过以下命令应用更改：

```bash
cd /opt/grampsweb && docker compose up -d
