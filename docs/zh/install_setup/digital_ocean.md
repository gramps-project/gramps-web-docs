# Gramps Web DigitalOcean 一键应用

您可以使用 [Gramps Web DigitalOcean 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)，而不是 [自己设置 Gramps Web](deployment.md)。Digital Ocean 托管 Gramps Web 的演示版本。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean 推荐徽章" /></a>

作为设置过程的一部分，您需要注册一个 DigitalOcean 帐户，并选择一个付费计划来使用“滴水”（虚拟机）。

可以说，这目前是部署您自己的自托管 Gramps Web 实例的最简单方法，使用 SSL 进行安全保护，而无需使用您自己的硬件。

!!! info
    请注意，您将为 DigitalOcean 的托管服务付费。Gramps 开源项目不提供付费支持。

## 第一步：创建 DigitalOcean 帐户

如果您还没有帐户，请在 [DigitalOcean](https://www.digitalocean.com/) 创建一个帐户。

## 第二步：创建滴水

- 前往 [Gramps Web 一键应用](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)，点击“创建 Gramps Web 滴水”。
- 选择至少 2 GB RAM 的计划。
- 设置对您的滴水的身份验证。
- 点击“创建滴水”。

!!! info
    您可能需要等待最多十分钟，以便一键应用安装最新的 `docker-compose` 版本。
    使用最新版本的 `docker-compose` 可以减轻与 `firstlogin.sh` 相关的错误。

## 第三步：设置域名

您需要一个域名（或子域名）。如果您拥有一个域名，请将其指向您滴水的 IP 地址。否则，您可以使用 [DuckDNS](https://www.duckdns.org/) 等免费服务。

## 第四步：登录到您的滴水

通过 SSH 登录到您的滴水。您应该看到“欢迎使用 Gramps Web DigitalOcean 一键应用设置！”的消息。如果不是，请等待几分钟再试一次（安装尚未完成）。

设置脚本将询问您域名（例如 `mygrampswebinstance.duckdns.org`）和电子邮件地址（需要用于 Let's Encrypt 证书）。

完成后，请等待后台设置完成。

## 第五步：启动 Gramps Web

您的 Gramps Web 实例现在应该可以在您的域名根目录访问，并且具有有效的 SSL 证书，并且应该显示首次运行助手。
