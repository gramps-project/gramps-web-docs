---
hide:
  - toc
---

# Gramps Web разработка: обзор

Gramps Web — это веб-приложение, состоящее из двух компонентов, которые разрабатываются отдельно:

- **Gramps Web API** — это RESTful API, написанное на Python и основанное на Flask. Исходный код размещен на [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Оно управляет доступом к базе данных и генеалогическими функциями, непосредственно используя библиотеку Gramps на Python. Это служит бэкендом Gramps Web. Для документации по разработке смотрите [Backend](backend/index.md).
- **Gramps Web Frontend** — это веб-приложение на Javascript, которое служит фронтендом для Gramps Web. Исходный код размещен на [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Для документации по разработке смотрите [Frontend](frontend/index.md).

Примечание о версионировании: Gramps Web API и фронтенд Gramps Web имеют независимое версионирование. В настоящее время "Gramps Web" — объединенное приложение — не имеет отдельного номера версии. Оба проекта придерживаются [SemVer](https://semver.org/).

Если вы не являетесь разработчиком на Python или Javascript, но все же хотите внести свой вклад в Gramps Web, ознакомьтесь с разделом [Contribute](../contribute/contribute.md).
