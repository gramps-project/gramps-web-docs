---
hide:
  - toc
---

# Gramps Web 开发概述

Gramps Web 是一个由两个独立开发的组件组成的 web 应用程序：

- **Gramps Web API** 是一个用 Python 编写的 RESTful API，基于 Flask。源代码托管在 [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/)。它直接利用 Gramps Python 库管理数据库访问和家谱功能。它作为 Gramps Web 的后端。有关开发文档，请参见 [Backend](backend/index.md)。
- **Gramps Web 前端** 是一个 Javascript web 应用程序，作为 Gramps Web 的前端。源代码托管在 [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/)。有关开发文档，请参见 [Frontend](frontend/index.md)。

关于版本控制的说明：Gramps Web API 和 Gramps Web 前端是独立版本控制的。目前，“Gramps Web”&ndash; 这个组合应用 &ndash; 没有单独的版本号。这两个项目遵循 [SemVer](https://semver.org/)。

如果您不是 Python 或 Javascript 开发人员，但仍希望为 Gramps Web 做出贡献，请查看 [Contribute](../contribute/contribute.md)。
