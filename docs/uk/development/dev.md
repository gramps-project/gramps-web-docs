---
hide:
  - toc
---

# Gramps Web розробка: огляд

Gramps Web – це веб-додаток, що складається з двох компонентів, які розробляються окремо:

- **Gramps Web API** – це RESTful API, написане на Python і засноване на Flask. Джерельний код розміщено на [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Воно управляє доступом до бази даних та генеалогічними функціями, безпосередньо використовуючи бібліотеку Gramps на Python. Це служить бекендом Gramps Web. Для документації з розробки дивіться [Backend](backend/index.md).
- **Gramps Web Frontend** – це веб-додаток на Javascript, який служить фронтендом для Gramps Web. Джерельний код розміщено на [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Для документації з розробки дивіться [Frontend](frontend/index.md).

Примітка щодо версій: Gramps Web API та Gramps Web фронтенд версіонуються незалежно. На даний момент "Gramps Web" – комбінований додаток – не має окремого номера версії. Обидва проекти дотримуються [SemVer](https://semver.org/).

Якщо ви не є розробником на Python або Javascript, але все ж хочете внести свій внесок у Gramps Web, ознайомтеся з [Contribute](../contribute/contribute.md).
