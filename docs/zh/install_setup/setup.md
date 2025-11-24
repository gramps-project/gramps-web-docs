# Gramps Web 安装 / 设置

本节涉及 Gramps Web 的安装和设置，以及其他入门选项。

## 开始使用 Gramps Web

Gramps Web 是一个运行在服务器上的 Web 应用程序，通过 Web 浏览器访问。它旨在通过互联网向经过身份验证的用户提供访问。

如果您想使用 Gramps Web 进行家谱研究数据，您必须选择以下选项之一：

1. 在自己的硬件上自托管
2. 在云中自托管
3. 注册托管实例

虽然第一个选项为您提供了最大的灵活性和控制权，但它也可能在技术上具有挑战性。

!!! tip
    Gramps Web 的主要原则之一是让用户随时控制自己的数据，因此从一个实例迁移数据到另一个实例是简单的。无需担心在选择其中一个选项后被锁定！

## 在自己的硬件上自托管

在自己的硬件上自托管 Gramps Web 的最方便方法是通过 Docker Compose。我们还提供适用于 ARM 架构的 Docker 镜像，因此您可以在地下室的 Raspberry Pi 上运行 Gramps Web。

请参阅 [使用 Docker 部署](deployment.md) 获取设置说明。

## 在云中自托管

安装 Gramps Web 可能比其他简单的 Web 应用程序更具挑战性，并且与普通的“共享托管”提供商不兼容。您可以注册一个虚拟服务器并手动安装 Gramps Web [手动](deployment.md)。

一个更简单的选项是使用预安装的云镜像。一个例子是我们的 [DigitalOcean 一键应用](digital_ocean.md)。

## 注册托管实例

托管的 Gramps Web 是开始使用 Gramps Web 的最简单方法，因为不需要安装或配置。

以下是 Gramps Web 的专用托管提供商列表（Gramps 开源社区对其服务不承担责任）：

- Grampshub ([www.grampshub.com](https://www.grampshub.com))，由 Gramps Web 的主要贡献者之一提供

如果您使用 Gramps Web 的托管选项，可以跳过本节的其余部分，直接跳到 [管理](../administration/admin.md) 部分。
