---
hide:
  - navigation
---

如果您在使用 Gramps Web 时遇到问题或需要帮助，请选择以下选项之一。

[论坛 :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[后端问题 :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[前端问题 :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

请参阅以下内容以获取一些指导，了解首先该去哪里。

## 提问

官方的 Gramps Discourse 论坛有一个 [Gramps Web 的单独类别](https://gramps.discourse.group/c/gramps-web/)。请使用它来询问您可能对 Gramps Web 的任何问题，例如

- 关于 Gramps Web 使用的问题
- 关于 Gramps Web 配置的问题
- Gramps Web 部署的故障排除
- 关于 Gramps Web 改进的想法
- ...

## 报告问题

如果您遇到一个您认为是 Gramps Web 中的错误的问题，请通过 Github 进行支持。

Gramps Web 使用的代码有两个独立的 Github 存储库，一个用于用户界面（“前端”），一个用于服务器代码（“后端”）：

- [前端问题](https://github.com/gramps-project/gramps-web/issues)
- [后端问题](https://github.com/gramps-project/gramps-web-api/issues)

如果您不确定在哪里提交问题，请不要担心，只需选择其中一个 - 维护者在必要时将能够转移该问题。

在任何情况下，请始终在您的报告中包含以下信息：

- 有关您设置的详细信息（例如，带有敏感值已编辑的 docker-compose 文件，或您是否使用托管版本，例如 Grampshub，或预配置的镜像，例如 DigitalOcean）
- 版本信息。要获取它，请转到 Gramps Web 设置页面上的“系统信息”选项卡，并复制/粘贴框中的值，应该类似于以下内容：

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## 建议增强功能

有关未来改进的一般想法和讨论，请随时在 [论坛](https://gramps.discourse.group/c/gramps-web/) 中开启讨论。您可能还想查看问题页面（请参见上面的链接），以了解特定功能是否已经计划或正在开发中。

对于具有有限范围的具体增强功能，请随时在适当的前端或后端 Github 存储库中直接打开一个功能请求问题。
